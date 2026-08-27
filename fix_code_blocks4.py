#!/usr/bin/env python3
"""Fix code blocks by adding only the necessary missing using statements."""

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

def find_class_names_in_block(block_content, namespace_map):
    """Find class names in the block and map them to namespaces."""
    class_names = set()
    for line in block_content.split('\n'):
        # Match class instantiations like "new ClassName(" or "ClassName "
        # Or type declarations like "ClassName variable"
        # Look for common patterns
        matches = re.findall(r'\b(\w+Shape)\b', line)  # Shape classes
        for m in matches:
            if m not in ['new', 'var', 'using']:
                class_names.add(m)
    return class_names

def fix_code_block_with_imports(block_content, all_imports, needed_imports):
    """Fix a code block by adding only the needed imports."""
    existing = extract_existing_imports_from_block(block_content)
    missing = needed_imports - existing
    
    if not missing:
        return block_content
    
    # Insert missing imports at the very beginning of the block
    lines = block_content.split('\n')
    
    # Find the first content line
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
    
    # Find all code blocks
    blocks = []
    for match in re.finditer(r'```csharp\s*\n(.*?)\s*```', content, re.DOTALL):
        blocks.append({
            'original': match.group(0),
            'content': match.group(1),
            'pos': match.start()
        })
    
    if len(blocks) <= 1:
        return False
    
    # Sort by position in reverse order for safe replacement
    blocks.sort(key=lambda x: x['pos'], reverse=True)
    
    modified = False
    new_content = content
    
    for block in blocks:
        old_content = block['content']
        
        # Find which imports are needed by checking for class names that require specific namespaces
        # For now, we'll check if the block contains types from Aspose.ThreeD.Profiles
        needs_profiles = 'RectangleShape' in old_content or 'CircleShape' in old_content or 'HollowRectangleShape' in old_content or 'I beam' in old_content.lower() or 'TShape' in old_content or 'ZShape' in old_content
        
        needed_imports = set()
        if needs_profiles:
            needed_imports.add('Aspose.ThreeD.Profiles')
        
        # Also check for other specific namespaces if needed
        # For now, just add the missing profiles import
        fixed_content = fix_code_block_with_imports(old_content, all_imports, needed_imports)
        
        if fixed_content != old_content:
            old_block = block['original']
            new_block = '```csharp\n' + fixed_content + '\n```'
            
            if new_block != old_block:
                new_content = new_content.replace(old_block, new_block, 1)
                modified = True
                print(f"  Fixed block - added: {needed_imports}")
    
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
