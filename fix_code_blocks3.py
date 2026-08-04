#!/usr/bin/env python3
"""Fix code blocks by adding missing using statements at the beginning."""

import re
from pathlib import Path

def get_all_imports_from_first_block(content):
    """Extract all using statements from the first code block."""
    first_match = re.search(r'```csharp\s*\n(.*?)\s*```', content, re.DOTALL)
    if not first_match:
        return set()
    
    first_block = first_match.group(1)
    imports = set()
    for line in first_block.split('\n'):
        line = line.strip()
        if line.startswith('using '):
            ns = line[6:].rstrip(';').strip()
            imports.add(ns)
    return imports

def extract_existing_imports_from_block(block_content):
    """Extract existing using statements from a code block."""
    imports = set()
    for line in block_content.split('\n'):
        line = line.strip()
        if line.startswith('using '):
            ns = line[6:].rstrip(';').strip()
            imports.add(ns)
    return imports

def fix_code_block_with_imports(block_content, all_imports):
    """Fix a code block by ensuring it has all necessary imports at the beginning."""
    existing = extract_existing_imports_from_block(block_content)
    missing = all_imports - existing
    
    if not missing:
        return block_content
    
    # Find the first non-empty line (after stripping)
    lines = block_content.split('\n')
    
    # Find where the first content line starts (skip empty lines)
    first_content_idx = 0
    for i, line in enumerate(lines):
        if line.strip():
            first_content_idx = i
            break
    
    # Insert missing imports at the very beginning
    new_lines = []
    for imp in sorted(missing):
        new_lines.append(f"using {imp};")
    
    # Add original lines
    new_lines.extend(lines)
    
    return '\n'.join(new_lines)

def process_file(filepath):
    """Process a single file and fix code blocks."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    all_imports = get_all_imports_from_first_block(content)
    
    if not all_imports:
        return False
    
    # Find all code blocks and their positions
    blocks = []
    for match in re.finditer(r'```csharp\s*\n(.*?)\s*```', content, re.DOTALL):
        blocks.append({
            'match': match,
            'original': match.group(0),
            'content': match.group(1),
            'pos': match.start()
        })
    
    if not blocks:
        return False
    
    # Sort by position in reverse order for safe replacement
    blocks.sort(key=lambda x: x['pos'], reverse=True)
    
    modified = False
    new_content = content
    
    for block in blocks:
        old_content = block['content']
        fixed_content = fix_code_block_with_imports(old_content, all_imports)
        
        if fixed_content != old_content:
            old_block = block['original']
            new_block = '```csharp\n' + fixed_content + '\n```'
            
            if new_block != old_block:
                new_content = new_content.replace(old_block, new_block, 1)
                modified = True
                print(f"  Fixed block at position {block['pos']}")
    
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
        
        with open(md_file, 'r') as f:
            content = f.read()
        blocks = re.findall(r'```csharp\s*\n(.*?)\s*```', content, re.DOTALL)
        
        if len(blocks) > 1:
            print(f"\nProcessing: {rel_path} ({len(blocks)} blocks)")
            if process_file(md_file):
                modified_count += 1
    
    print(f"\n\nTotal files modified: {modified_count}")

if __name__ == "__main__":
    main()
