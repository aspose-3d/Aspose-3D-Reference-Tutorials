#!/usr/bin/env python3
"""Extract and verify C# code blocks from Aspose.3D tutorial files."""

import os
import re
import subprocess
import tempfile
from pathlib import Path

def extract_csharp_blocks(filepath):
    """Extract all C# code blocks from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match ```csharp ... ```
    pattern = r'```csharp\s*(.*?)\s*```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    return matches

def verify_csharp_code(code, version="26.6.0"):
    """Verify C# code against Aspose.3D using aspose-cli."""
    # Clean the code - remove leading/trailing whitespace and common prefixes
    lines = code.strip().split('\n')
    # Remove any leading blank lines
    while lines and not lines[0].strip():
        lines.pop(0)
    # Remove any trailing blank lines
    while lines and not lines[-1].strip():
        lines.pop()
    
    code = '\n'.join(lines)
    
    if not code:
        return None, "Empty code block"
    
    try:
        result = subprocess.run(
            ['aspose-cli', 'verify', 'csharp', version, '-'],
            input=code,
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return None, str(e)

def main():
    base_dir = Path("/home/lexchou/workspace/aspose/ref-tutorial/3d/english/net")
    
    # Find all _index.md files
    md_files = list(base_dir.rglob("_index.md"))
    print(f"Found {len(md_files)} _index.md files")
    
    total_blocks = 0
    verified_blocks = 0
    failed_blocks = 0
    errors = []
    
    for md_file in sorted(md_files):
        relative_path = md_file.relative_to(base_dir)
        print(f"\nProcessing: {relative_path}")
        
        blocks = extract_csharp_blocks(md_file)
        print(f"  Found {len(blocks)} C# code blocks")
        total_blocks += len(blocks)
        
        for i, block in enumerate(blocks):
            print(f"  Block {i+1} (first 50 chars): {block[:50]}...")
            
            is_valid, msg = verify_csharp_code(block)
            
            if is_valid is None:
                print(f"    ERROR: {msg}")
                errors.append({
                    'file': str(relative_path),
                    'block': i+1,
                    'error': msg
                })
                failed_blocks += 1
            elif is_valid:
                print(f"    VERIFIED ✓")
                verified_blocks += 1
            else:
                print(f"    FAILED ✗")
                print(f"    {msg[:500]}")
                errors.append({
                    'file': str(relative_path),
                    'block': i+1,
                    'error': msg
                })
                failed_blocks += 1
    
    print(f"\n\n=== SUMMARY ===")
    print(f"Files reviewed: {len(md_files)}")
    print(f"Total code blocks: {total_blocks}")
    print(f"Verified successfully: {verified_blocks}")
    print(f"Failed: {failed_blocks}")
    
    if errors:
        print(f"\n=== ERRORS ===")
        for err in errors[:20]:  # Show first 20 errors
            print(f"\nFile: {err['file']}, Block: {err['block']}")
            print(f"Error: {err['error'][:200]}")

if __name__ == "__main__":
    main()
