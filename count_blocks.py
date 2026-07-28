#!/usr/bin/env python3
import re
from pathlib import Path

base_dir = Path('3d/english/net')
md_files = list(base_dir.rglob('_index.md'))
print(f'Total files: {len(md_files)}')

files_with_csharp = []
for f in md_files:
    with open(f, 'r') as fp:
        content = fp.read()
    count = len(re.findall(r'```csharp', content))
    if count > 0:
        files_with_csharp.append((str(f.relative_to(base_dir)), count))

print(f'Files with C# blocks: {len(files_with_csharp)}')
for path, count in sorted(files_with_csharp):
    print(f'{path}: {count}')
