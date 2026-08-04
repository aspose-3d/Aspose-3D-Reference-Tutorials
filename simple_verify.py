#!/usr/bin/env python3
"""Simple verification - extract and verify each code block."""

import re
import subprocess
from pathlib import Path

def extract_code_blocks(filepath):
    """Extract all C# code blocks from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = []
    # Match ```csharp ... ``` blocks
    pattern = r'```csharp\s*\n(.*?)\s*```'
    for match in re.finditer(pattern, content, re.DOTALL):
        blocks.append(match.group(1))
    
    return blocks

def verify_block(code, version="26.6.0"):
    """Verify a C# code block using aspose-cli."""
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
    
    print(f"Found {len(md_files)} markdown files")
    
    # Process files and collect issues
    issues = []
    
    for md_file in sorted(md_files)[:5]:  # Test with first 5 files first
        rel_path = str(md_file.relative_to(base_dir))
        blocks = extract_code_blocks(md_file)
        
        print(f"\nFile: {rel_path} ({len(blocks)} blocks)")
        
        for i, block in enumerate(blocks):
            is_valid, msg = verify_block(block)
            
            if is_valid:
                status = "OK"
            elif is_valid is None:
                status = f"ERROR: {msg}"
                issues.append((rel_path, i+1, msg))
            else:
                status = f"FAILED: {msg[:100]}"
                issues.append((rel_path, i+1, msg))
            
            first_line = block.strip().split('\n')[0][:50]
            print(f"  Block {i+1}: {status}")
            print(f"    First: {first_line}...")
    
    print(f"\n\nTotal issues found: {len(issues)}")
    for file, block, msg in issues:
        print(f"  {file}, Block {block}: {msg[:150]}")

if __name__ == "__main__":
    main()
