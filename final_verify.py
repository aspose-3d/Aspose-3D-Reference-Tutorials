#!/usr/bin/env python3
"""Final comprehensive verification of all code blocks."""

import re
import subprocess
from pathlib import Path

def extract_code_blocks(filepath):
    """Extract all C# code blocks from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = []
    pattern = r'```csharp\s*\n(.*?)\s*```'
    for match in re.finditer(pattern, content, re.DOTALL):
        blocks.append(match.group(1))
    
    return blocks

def verify_block(code, version="26.6.0"):
    """Verify a C# code block."""
    code = code.strip()
    if not code:
        return None, "Empty block"
    
    try:
        result = subprocess.run(
            ['aspose-cli', 'verify', 'csharp', version, '-'],
            input=code,
            capture_output=True,
            text=True,
            timeout=60
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        
        if result.returncode == 0:
            return True, stdout or "OK"
        else:
            return False, (stdout + " " + stderr).strip()
    except Exception as e:
        return None, str(e)

def main():
    base_dir = Path("/home/lexchou/workspace/aspose/ref-tutorial/3d/english/net")
    md_files = list(base_dir.rglob("_index.md"))
    
    print(f"Found {len(md_files)} markdown files\n")
    
    total_blocks = 0
    verified_blocks = 0
    failed_blocks = 0
    errors = []
    
    for md_file in sorted(md_files):
        rel_path = str(md_file.relative_to(base_dir))
        blocks = extract_code_blocks(md_file)
        
        total_blocks += len(blocks)
        
        for i, block in enumerate(blocks):
            is_valid, msg = verify_block(block)
            
            if is_valid:
                verified_blocks += 1
            elif is_valid is None:
                failed_blocks += 1
                errors.append((rel_path, i+1, msg))
            else:
                failed_blocks += 1
                errors.append((rel_path, i+1, msg))
    
    print(f"=== SUMMARY ===")
    print(f"Total files: {len(md_files)}")
    print(f"Total code blocks: {total_blocks}")
    print(f"Verified successfully: {verified_blocks}")
    print(f"Failed: {failed_blocks}")
    
    if errors:
        print(f"\n=== ERRORS ===")
        for file, block, msg in errors[:30]:
            print(f"\n{file}, Block {block}:")
            print(f"  {msg[:200]}")
    
    if len(errors) > 30:
        print(f"\n... and {len(errors) - 30} more errors")

if __name__ == "__main__":
    main()
