import os
import re
import sys

dirs = sys.argv[1:]

# 广告/营销行关键词：包含任一即整行删除
AD_KEYWORDS = [
    'lazyhelper',
    '懒人专属群',
    '👸号懒人搜索',
    '付费社群',
    '免责声明',
    'feishu.cn',
    '社群已稳定运营',
    '社群更新记录',
    '推荐小懒的付费社群',
    '微软：lazyhelper',
    '抵御信息过载',
    '懒人🦏',  # 懒人🛰️
]

AD_EXACT_STRIP = {
    '懒人搜索', '懒人专属群', '👸号',
    '懒人专属群（介绍）',
}


def is_ad_line(line):
    for kw in AD_KEYWORDS:
        if kw in line:
            return True
    if line.strip() in AD_EXACT_STRIP:
        return True
    return False


def process(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    changed = False
    title_idx = None

    for i, line in enumerate(lines):
        if is_ad_line(line):
            changed = True
            continue
        new_lines.append(line)
        if title_idx is None and line.startswith('# '):
            title_idx = len(new_lines) - 1

    # 将作者改为“龙哥”：标题行后插入“作者：龙哥”
    if title_idx is not None:
        nxt = new_lines[title_idx + 1] if title_idx + 1 < len(new_lines) else ''
        if not nxt.startswith('作者：'):
            new_lines.insert(title_idx + 1, '作者：龙哥')
            changed = True

    # 把开头自我介绍里的“我是 XX”改为“我是龙哥”（标题后前20行内）
    if title_idx is not None:
        j = title_idx + 1
        scanned = 0
        while j < len(new_lines) and scanned < 20:
            if new_lines[j].strip():
                m = re.search(
                    r'我是\s*([^\s，。,：:、\n]{2,8})([，,。.：:、])',
                    new_lines[j],
                )
                if m:
                    new_lines[j] = (
                        new_lines[j][:m.start(1)] + '龙哥' + new_lines[j][m.end(1):]
                    )
                    changed = True
                    break  # 每篇文章只替换开头第一处自我介绍
            scanned += 1
            j += 1

    text = '\n'.join(new_lines)
    if changed and text != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    return False


modified = []
errors = []
for d in dirs:
    for root, _folders, files in os.walk(d):
        for fn in sorted(files):
            if fn.endswith('.md'):
                p = os.path.join(root, fn)
                try:
                    if process(p):
                        modified.append(p)
                except Exception as e:
                    errors.append(f'{p}: {e}')

print(f'MODIFIED {len(modified)}')
for m in modified:
    print(m)
if errors:
    print('ERRORS:')
    for e in errors:
        print(e)
