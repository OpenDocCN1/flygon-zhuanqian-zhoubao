import os
import sys

dirs = sys.argv[1:] or ['docs']
target = '作者：龙哥'
modified = []
errors = []

for d in dirs:
    for root, _folders, files in os.walk(d):
        for fn in sorted(files):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(root, fn)
            try:
                with open(p, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                errors.append(f'{p}: read error {e}')
                continue

            lines = content.split('\n')
            new_lines = [line for line in lines if line.strip() != target]
            if len(new_lines) != len(lines):
                text = '\n'.join(new_lines)
                if text != content:
                    try:
                        with open(p, 'w', encoding='utf-8') as f:
                            f.write(text)
                        modified.append(p)
                    except Exception as e:
                        errors.append(f'{p}: write error {e}')

print(f'MODIFIED {len(modified)}')
for m in modified:
    print(m)
if errors:
    print('ERRORS:')
    for e in errors:
        print(e)
