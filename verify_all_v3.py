#!/usr/bin/env python3
"""
Script to verify Java code snippets from tutorial files using javac directly.
This version properly handles snippets with imports and partial code.
"""

import os
import re
import subprocess
import tempfile
import shutil

TUTORIAL_DIR = "/home/lexchou/workspace/aspose/ref-tutorial/3d/english/java"
OUTPUT_DIR = "/home/lexchou/workspace/aspose/ref-tutorial/java_verification"
VERSION = "26.6.0"
JAR_FILE = "/home/lexchou/workspace/aspose/ref-tutorial/aspose-3d-26.6.0.jar"

def extract_java_snippets(content):
    """Extract all Java code blocks from markdown content."""
    # Remove HTML-like template tags
    clean_content = re.sub(r'\{\{[^}]*\}\}', '', content)
    # Find all ```java ... ``` blocks
    pattern = re.compile(r'```java\s*\n(.*?)\n```', re.DOTALL | re.IGNORECASE)
    return pattern.findall(clean_content)

def create_composite_java(snippets):
    """Create a composite Java file from multiple snippets.
    
    This approach:
    1. Collects all import statements
    2. Puts them at the top
    3. Wraps all code in a main method
    """
    imports = []
    code_parts = []
    
    for snippet in snippets:
        lines = snippet.strip().split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('import ') or line.startswith('package '):
                if line not in imports:
                    imports.append(line)
            elif line and not line.startswith('//') and not line.startswith('*'):
                code_parts.append(line)
    
    # Build the composite Java file
    java_code = "import com.aspose.threed.*;\n\n"
    
    for imp in imports:
        if not imp.startswith('import com.aspose.threed'):
            java_code += imp + "\n"
    
    java_code += """
public class CompositeVerify {
    public static void main(String[] args) {
"""
    
    for part in code_parts:
        java_code += "        " + part + "\n"
    
    java_code += """
    }
}
"""
    
    return java_code

def verify_snippets(snippets, file_id):
    """Verify a list of snippets together. Returns (success, error_message, snippet_results)."""
    if not snippets:
        return True, None, []
    
    # Create composite Java file
    java_code = create_composite_java(snippets)
    
    # Write to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.java', delete=False) as f:
        f.write(java_code)
        temp_file = f.name
    
    try:
        # Compile with javac
        result = subprocess.run(
            ['javac', '-cp', JAR_FILE, temp_file],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            return True, None, [{'snippet_num': i+1, 'success': True, 'error': None} for i in range(len(snippets))]
        else:
            # Parse the error to identify which snippet(s) failed
            error_output = result.stdout + result.stderr
            snippet_results = []
            
            for i in range(len(snippets)):
                snippet_results.append({
                    'snippet_num': i+1,
                    'success': False,
                    'error': error_output
                })
            
            return False, error_output, snippet_results
            
    except Exception as e:
        snippet_results = [{'snippet_num': i+1, 'success': False, 'error': str(e)} for i in range(len(snippets))]
        return False, str(e), snippet_results
    finally:
        # Clean up
        try:
            os.unlink(temp_file)
        except:
            pass

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Find all _index.md files
    pattern = os.path.join(TUTORIAL_DIR, "**", "_index.md")
    md_files = sorted([f for f in __import__('glob').glob(pattern, recursive=True)])
    
    print(f"Found {len(md_files)} tutorial files to process")
    
    # Statistics
    stats = {
        'total_files': 0,
        'java_snippets': 0,
        'java_verified': 0,
        'java_failed': 0,
        'failed_snippets': []
    }
    
    # Process each file
    for md_file in md_files:
        file_name = os.path.basename(os.path.dirname(md_file))
        stats['total_files'] += 1
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            snippets = extract_java_snippets(content)
            stats['java_snippets'] += len(snippets)
            
            if snippets:
                success, error, results = verify_snippets(snippets, file_name)
                
                if success:
                    stats['java_verified'] += len(snippets)
                    print(f"  ✓ All {len(snippets)} snippets verified in {file_name}")
                else:
                    stats['java_failed'] += len(snippets)
                    
                    # Record each failed snippet
                    for result in results:
                        stats['failed_snippets'].append({
                            'file': file_name,
                            'snippet_num': result['snippet_num'],
                            'error': result['error'].strip() if result['error'] else 'Unknown error',
                            'code': snippets[result['snippet_num'] - 1].strip() if result['snippet_num'] <= len(snippets) else ''
                        })
                    
                    print(f"  ✗ {len(snippets)} snippets failed in {file_name}")
                    print(f"    Error preview: {error.strip()[:150]}..." if len(error) > 150 else error)
        
        except Exception as e:
            print(f"  Error processing {file_name}: {str(e)}")
    
    # Print summary
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY")
    print("="*80)
    print(f"Total files reviewed: {stats['total_files']}")
    print(f"Java code snippets found: {stats['java_snippets']}")
    print(f"Java snippets verified successfully: {stats['java_verified']}")
    print(f"Java snippets with errors: {stats['java_failed']}")
    
    # Save detailed results
    results_file = os.path.join(OUTPUT_DIR, "results_summary.txt")
    with open(results_file, 'w', encoding='utf-8') as f:
        f.write("Java Code Verification Summary\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Version: {VERSION}\n")
        f.write(f"Total files reviewed: {stats['total_files']}\n")
        f.write(f"Java code snippets found: {stats['java_snippets']}\n")
        f.write(f"Java snippets verified successfully: {stats['java_verified']}\n")
        f.write(f"Java snippets with errors: {stats['java_failed']}\n\n")
        
        if stats['failed_snippets']:
            f.write("FAILED SNIPPETS:\n")
            f.write("-" * 40 + "\n\n")
            
            for failure in stats['failed_snippets']:
                f.write(f"File: {failure['file']} (Snippet #{failure['snippet_num']})\n")
                f.write(f"Error:\n```\n{failure['error']}\n```\n\n")
                f.write("Code:\n```\n")
                f.write(failure['code'])
                f.write("\n```\n\n")
    
    print(f"\nDetailed results saved to: {results_file}")
    
    # Show failed snippets count
    if stats['failed_snippets']:
        print(f"\n{len(stats['failed_snippets'])} snippets failed verification")
    
    return stats

if __name__ == "__main__":
    main()
