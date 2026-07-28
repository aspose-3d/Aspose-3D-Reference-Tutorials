#!/usr/bin/env python3
"""Extract and verify C# code blocks from Aspose.3D tutorial files."""

import os
import re
import subprocess
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
    # Clean the code
    code = code.strip()
    
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
    md_files = sorted(base_dir.rglob("_index.md"))
    
    output_file = Path("/home/lexchou/workspace/aspose/ref-tutorial/csharp_verification_results.txt")
    
    total_blocks = 0
    verified_blocks = 0
    failed_blocks = 0
    errors = []
    
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("=== C# Code Verification Results for Aspose.3D 26.6.0 ===\n\n")
        
        for md_file in md_files:
            relative_path = str(md_file.relative_to(base_dir))
            out.write(f"\n{'='*80}\nFile: {relative_path}\n{'='*80}\n")
            
            blocks = extract_csharp_blocks(md_file)
            out.write(f"Found {len(blocks)} C# code blocks\n\n")
            total_blocks += len(blocks)
            
            for i, block in enumerate(blocks):
                out.write(f"--- Block {i+1} (first 60 chars): ---\n")
                out.write(block[:60] + "\n\n")
                
                is_valid, msg = verify_csharp_code(block)
                
                if is_valid is None:
                    out.write(f"ERROR: {msg}\n")
                    errors.append({
                        'file': relative_path,
                        'block': i+1,
                        'error': msg
                    })
                    failed_blocks += 1
                elif is_valid:
                    out.write(f"VERIFIED ✓\n")
                    verified_blocks += 1
                else:
                    out.write(f"FAILED ✗\n")
                    out.write(msg[:1000] + "\n")
                    errors.append({
                        'file': relative_path,
                        'block': i+1,
                        'error': msg[:500]
                    })
                    failed_blocks += 1
            
            out.flush()
    
    # Write summary
    with open(output_file, 'a', encoding='utf-8') as out:
        out.write(f"\n\n{'='*80}\n")
        out.write("=== SUMMARY ===\n")
        out.write(f"{'='*80}\n")
        out.write(f"Files reviewed: {len(md_files)}\n")
        out.write(f"Total code blocks: {total_blocks}\n")
        out.write(f"Verified successfully: {verified_blocks}\n")
        out.write(f"Failed: {failed_blocks}\n")
        
        if errors:
            out.write(f"\n{'='*80}\n")
            out.write("=== ERRORS ===\n")
            out.write(f"{'='*80}\n")
            for err in errors:
                out.write(f"\nFile: {err['file']}, Block: {err['block']}\n")
                out.write(f"Error: {err['error'][:200]}\n")

if __name__ == "__main__":
    main()
