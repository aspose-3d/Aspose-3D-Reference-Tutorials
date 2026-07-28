#!/usr/bin/env python3
"""Process C# code blocks in small batches."""

import re
import subprocess
from pathlib import Path

def extract_csharp_blocks(filepath):
    """Extract all C# code blocks from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = []
    pattern = r'```csharp\s*\n(.*?)\s*```'
    for match in re.finditer(pattern, content, re.DOTALL):
        code = match.group(1)
        start_pos = match.start()
        line_num = content[:start_pos].count('\n') + 1
        blocks.append({
            'code': code,
            'line': line_num
        })
    
    return blocks

def verify_csharp_code(code, version="26.6.0"):
    """Verify C# code against Aspose.3D using aspose-cli."""
    code = code.strip()
    
    if not code:
        return None, "Empty code block", ""
    
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
        return result.returncode == 0, stdout, stderr
    except Exception as e:
        return None, "", str(e)

def main():
    base_dir = Path("/home/lexchou/workspace/aspose/ref-tutorial/3d/english/net")
    md_files = sorted(base_dir.rglob("_index.md"))
    
    output_file = Path("/home/lexchou/workspace/aspose/ref-tutorial/comprehensive_verification.txt")
    
    # Clear and write header
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("=== Comprehensive C# Code Verification for Aspose.3D 26.6.0 ===\n\n")
    
    total_blocks = 0
    verified_blocks = 0
    failed_blocks = 0
    all_errors = []
    
    # Process files in batches of 10
    batch_size = 10
    for batch_start in range(0, len(md_files), batch_size):
        batch_end = min(batch_start + batch_size, len(md_files))
        batch_files = md_files[batch_start:batch_end]
        
        print(f"Processing files {batch_start+1} to {batch_end} of {len(md_files)}")
        
        with open(output_file, 'a', encoding='utf-8') as out:
            for md_file in batch_files:
                relative_path = str(md_file.relative_to(base_dir))
                blocks = extract_csharp_blocks(md_file)
                
                out.write(f"\n{'='*80}\nFile: {relative_path}\n{'='*80}\n")
                out.write(f"Found {len(blocks)} C# code blocks\n\n")
                total_blocks += len(blocks)
                
                file_has_issues = False
                
                for i, block in enumerate(blocks):
                    is_valid, stdout, stderr = verify_csharp_code(block['code'])
                    
                    out.write(f"Block {i+1} (line {block['line']}):\n")
                    out.write(f"  First 60 chars: {block['code'][:60]}\n")
                    
                    if is_valid is None:
                        out.write(f"  ERROR: {stderr}\n")
                        all_errors.append({'file': relative_path, 'block': i+1, 'error': stderr})
                        failed_blocks += 1
                        file_has_issues = True
                    elif is_valid:
                        out.write(f"  VERIFIED ✓\n")
                        verified_blocks += 1
                    else:
                        out.write(f"  FAILED ✗\n")
                        if stdout:
                            out.write(f"  stdout: {stdout[:500]}\n")
                        if stderr:
                            out.write(f"  stderr: {stderr[:500]}\n")
                        all_errors.append({'file': relative_path, 'block': i+1, 'error': stdout + stderr})
                        failed_blocks += 1
                        file_has_issues = True
                
                if file_has_issues:
                    out.write(f"\n>>> File has issues\n")
            
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
        
        if all_errors:
            out.write(f"\n{'='*80}\n")
            out.write("=== ERRORS ===\n")
            out.write(f"{'='*80}\n")
            out.write(f"Total errors: {len(all_errors)}\n")
            for err in all_errors:
                out.write(f"\nFile: {err['file']}, Block: {err['block']}\n")
                error_msg = err['error'][:300] if err['error'] else "No error message"
                out.write(f"Error: {error_msg}\n")

if __name__ == "__main__":
    main()
