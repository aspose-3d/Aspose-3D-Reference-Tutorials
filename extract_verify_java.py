#!/usr/bin/env python3
"""
Script to extract and verify Java code snippets from Aspose.3D Java tutorial files.
Optimized for performance and error handling.
"""

import os
import re
import glob
import subprocess
import tempfile

TUTORIAL_DIR = "/home/lexchou/workspace/aspose/ref-tutorial/3d/english/java"
OUTPUT_DIR = "/home/lexchou/workspace/aspose/ref-tutorial/java_verification"
VERSION = "26.6.0"

# Patterns to extract code blocks
JAVA_PATTERN = re.compile(r'```java\s*\n(.*?)\n```', re.DOTALL | re.IGNORECASE)
CSHARP_PATTERN = re.compile(r'```(?:csharp|C#)\s*\n(.*?)\n```', re.DOTALL | re.IGNORECASE)

def extract_java_snippets(content):
    """Extract all Java code blocks from markdown content."""
    # Remove HTML-like comments and template tags first
    clean_content = re.sub(r'\{\{[^}]*\}\}', '', content)
    return JAVA_PATTERN.findall(clean_content)

def extract_csharp_snippets(content):
    """Extract all C# code blocks from markdown content."""
    clean_content = re.sub(r'\{\{[^}]*\}\}', '', content)
    return CSHARP_PATTERN.findall(clean_content)
def verify_java_code(code_snippet):
    """Verify a Java code snippet by compiling it with javac. Returns (success, error_message)."""
    # Check if snippet starts with import - if so, we need to wrap differently
    snippet_stripped = code_snippet.strip()
    
    # Check if snippet already has imports
    has_imports = snippet_stripped.startswith('import')
    
    if has_imports:
        # Snippet contains imports - extract just the non-import code
        lines = code_snippet.split('\n')
        code_lines = [l for l in lines if not l.strip().startswith('import')]
        code_without_imports = '\n'.join(code_lines)
        
        java_code = f"""import com.aspose.threed.*;
public class TempVerify {{
    public static void main(String[] args) {{
{code_without_imports}
    }}
}}
"""
    else:
        # Snippet contains code without imports - wrap in class with imports at top
        java_code = f"""import com.aspose.threed.*;
public class TempVerify {{
    public static void main(String[] args) {{
{code_snippet}
    }}
}}
"""
    
    try:
        # Write to temp file - use .java extension, javac will create class in current dir
        temp_dir = tempfile.mkdtemp()
        temp_file = os.path.join(temp_dir, "TempVerify.java")
        
        with open(temp_file, 'w') as f:
            f.write(java_code)
        
        # Compile with javac
        result = subprocess.run(
            ["javac", "-cp", "/home/lexchou/workspace/aspose/ref-tutorial/aspose-3d-26.6.0.jar", temp_file],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Clean up
        try:
            os.unlink(temp_file)
            os.unlink(os.path.join(temp_dir, "TempVerify.class"))
        except:
            pass
        try:
            os.rmdir(temp_dir)
        except:
            pass
        
        if result.returncode == 0:
            return True, None
        
        return False, result.stdout + result.stderr
        
    except subprocess.TimeoutExpired:
        try:
            os.unlink(temp_file)
        except:
            pass
        return False, "Compilation timed out"
    except Exception as e:
        try:
            os.unlink(temp_file)
        except:
            pass
        return False, f"Error: {str(e)}"
def process_file(file_path, stats, detailed_results):
    """Process a single tutorial file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        file_name = os.path.basename(os.path.dirname(file_path))
        
        # Extract snippets
        java_snippets = extract_java_snippets(content)
        csharp_snippets = extract_csharp_snippets(content)
        
        stats['total_files'] += 1
        stats['java_snippets'] += len(java_snippets)
        stats['csharp_snippets'] += len(csharp_snippets)
        
        # Verify Java snippets
        for i, snippet in enumerate(java_snippets):
            snippet_file = f"{file_name}_java_{i+1}"
            success, error = verify_java_code(snippet)
            
            if success:
                stats['java_verified'] += 1
            else:
                stats['java_failed'] += 1
                detailed_results.append({
                    'file': file_name,
                    'snippet_num': i + 1,
                    'error': error.strip() if error else 'Unknown error',
                    'code_preview': snippet[:200] + '...' if len(snippet) > 200 else snippet
                })
        
        return True
    except Exception as e:
        stats['total_files'] += 1
        stats['java_failures'].append({
            'file': os.path.basename(os.path.dirname(file_path)),
            'error': str(e)
        })
        return False

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Find all _index.md files
    pattern = os.path.join(TUTORIAL_DIR, "**", "_index.md")
    md_files = glob.glob(pattern, recursive=True)
    
    print(f"Found {len(md_files)} tutorial files to process")
    
    # Statistics
    stats = {
        'total_files': 0,
        'java_snippets': 0,
        'csharp_snippets': 0,
        'java_verified': 0,
        'java_failed': 0,
        'java_failures': [],
        'csharp_found': 0
    }
    
    # Detailed failure results
    detailed_results = []
    
    # Process files
    processed = 0
    for md_file in sorted(md_files):
        if process_file(md_file, stats, detailed_results):
            processed += 1
            if processed % 10 == 0:
                print(f"Processed {processed}/{len(md_files)} files...")
    
    # Print summary
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY")
    print("="*80)
    print(f"Total files reviewed: {stats['total_files']}")
    print(f"Java code snippets found: {stats['java_snippets']}")
    print(f"Java snippets verified successfully: {stats['java_verified']}")
    print(f"Java snippets with errors: {stats['java_failed']}")
    print(f"C# snippets found (not verified): {stats['csharp_snippets']}")
    
    if detailed_results:
        print("\nFAILED SNIPPETS:")
        for i, failure in enumerate(detailed_results[:20]):  # Show first 20
            print(f"\n  [{i+1}] File: {failure['file']} (Snippet #{failure['snippet_num']})")
            print(f"      Error: {failure['error'][:100]}..." if len(failure['error']) > 100 else failure['error'])
        if len(detailed_results) > 20:
            print(f"\n  ... and {len(detailed_results) - 20} more failures")
    
    # Save detailed results
    results_file = os.path.join(OUTPUT_DIR, "results_summary.txt")
    with open(results_file, 'w') as f:
        f.write("Java Code Verification Summary\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total files reviewed: {stats['total_files']}\n")
        f.write(f"Java code snippets found: {stats['java_snippets']}\n")
        f.write(f"Java snippets verified successfully: {stats['java_verified']}\n")
        f.write(f"Java snippets with errors: {stats['java_failed']}\n")
        
        if detailed_results:
            f.write("\nFAILED SNIPPETS:\n")
            for failure in detailed_results:
                f.write(f"\n  File: {failure['file']} (Snippet #{failure['snippet_num']})\n")
                f.write(f"  Error: {failure['error']}\n")
                f.write(f"  Code preview:\n")
                f.write("  " + failure['code_preview'].replace('\n', '\n  ') + "\n")
        
        if stats['java_failures']:
            f.write("\nFILE PROCESSING ERRORS:\n")
            for failure in stats['java_failures']:
                f.write(f"\n  File: {failure['file']}\n")
                f.write(f"  Error: {failure['error']}\n")
    
    print(f"\nDetailed results saved to: {results_file}")
    print(f"\nVerification completed!")
    
    return stats, detailed_results

if __name__ == "__main__":
    main()
