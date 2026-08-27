#!/usr/bin/env python3
"""
Script to verify Java code snippets from tutorial files using javac directly.
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

def verify_snippet(code, snippet_id):
    """Verify a Java code snippet by compiling it. Returns (success, error_message)."""
    # Create a proper Java file
    java_code = f"""import com.aspose.threed.*;

public class TempVerify_{snippet_id} {{
    public static void main(String[] args) {{
{code}
    }}
}}
"""
    
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
            return True, None
        else:
            return False, result.stdout + result.stderr
            
    except Exception as e:
        return False, f"Verification error: {str(e)}"
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
            
            # Verify each snippet
            for i, snippet in enumerate(snippets):
                snippet_id = f"{file_name}_{i+1}"
                success, error = verify_snippet(snippet, i+1)
                
                if success:
                    stats['java_verified'] += 1
                else:
                    stats['java_failed'] += 1
                    stats['failed_snippets'].append({
                        'file': file_name,
                        'snippet_num': i + 1,
                        'error': error.strip() if error else 'Unknown error',
                        'code': snippet.strip()
                    })
                    
                    # Print error info to console
                    print(f"  ✗ Snippet #{i+1} FAILED in {file_name}")
                    print(f"    Error preview: {error.strip()[:200]}..." if len(error) > 200 else error)
        
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
