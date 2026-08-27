#!/usr/bin/env python3
"""Fix code blocks by adding missing using statements."""

import re
from pathlib import Path

def get_missing_imports(code, all_imports):
    """Check which imports from all_imports are missing in the code."""
    # Extract existing imports from the code
    existing = set()
    for line in code.split('\n'):
        line = line.strip()
        if line.startswith('using '):
            # Extract the namespace
            ns = line[6:].rstrip(';').strip()
            existing.add(ns)
    
    # Return imports that are needed but missing
    needed = all_imports - existing
    return sorted(needed)

def fix_code_block(code, missing_imports):
    """Add missing imports to a code block."""
    if not missing_imports:
        return code
    
    lines = code.split('\n')
    
    # Find where to insert imports - after any existing using statements or at the top
    insert_pos = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('using '):
            insert_pos = i + 1
        elif line.strip() and not line.strip().startswith('//'):
            # First non-empty, non-comment line
            break
    
    # Insert the missing imports
    new_lines = lines[:insert_pos]
    for imp in missing_imports:
        new_lines.append(f"using {imp};")
    new_lines.extend(lines[insert_pos:])
    
    return '\n'.join(new_lines)

def process_file(filepath, base_dir):
    """Process a single file and fix code blocks."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all using statements from the first code block
    first_block_match = re.search(r'```csharp\s*\n(.*?)\s*```', content, re.DOTALL)
    if not first_block_match:
        return False  # No code blocks
    
    first_block = first_block_match.group(1)
    
    # Extract all using statements from first block
    all_imports = set()
    for line in first_block.split('\n'):
        line = line.strip()
        if line.startswith('using '):
            ns = line[6:].rstrip(';').strip()
            all_imports.add(ns)
    
    # Find all code blocks
    blocks = []
    for match in re.finditer(r'```csharp\s*\n(.*?)\s*```', content, re.DOTALL):
        blocks.append(match)
    
    if not blocks:
        return False
    
    # Process each block
    modified = False
    new_content = content
    
    # Process blocks in reverse order to maintain correct positions
    for match in reversed(blocks):
        code = match.group(1)
        
        # Get missing imports for this block
        missing = get_missing_imports(code, all_imports)
        
        if missing:
            fixed_code = fix_code_block(code, missing)
            old_block = match.group(0)
            new_block = '```csharp\n' + fixed_code + '\n```'
            new_content = new_content.replace(old_block, new_block, 1)
            modified = True
            print(f"  Fixed block at line {content[:match.start()].count(chr(10)) + 1}")
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Modified {filepath}")
        return True
    
    return False

def main():
    base_dir = Path("/home/lexchou/workspace/aspose/ref-tutorial/3d/english/net")
    md_files = sorted(base_dir.rglob("_index.md"))
    
    modified_count = 0
    
    for md_file in md_files:
        rel_path = str(md_file.relative_to(base_dir))
        blocks = re.findall(r'```csharp\s*\n(.*?)\s*```', open(md_file).read(), re.DOTALL)
        
        if len(blocks) > 1:  # Only process files with multiple blocks
            print(f"\nProcessing: {rel_path} ({len(blocks)} blocks)")
            if process_file(md_file, base_dir):
                modified_count += 1
    
    print(f"\n\nTotal files modified: {modified_count}")

if __name__ == "__main__":
    main()
