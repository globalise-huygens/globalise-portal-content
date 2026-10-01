"""Re-render the reference lists on a page (e.g. pages/resources/bibliography.md) from references.bib.

Every list item ends with its citation key in an HTML comment, e.g. "* ... <!-- Gaastra2003 -->".
To add a work, add a line containing only "* <!-- Key -->" to the right list and run this script.
Each block of consecutive items is re-rendered with Pandoc citeproc (Chicago author-date) and
sorted as citeproc sorts them.

Usage:
  python3 scripts/render_bibliography.py PANDOC PAGE BIB [OldKey=NewKey ...]
  e.g. python3 scripts/render_bibliography.py pandoc pages/resources/bibliography.md assets/references/references.bib

Optional OldKey=NewKey arguments rename keys on the page; "+Heading=Key" adds Key to the list
under the given heading. Requires Pandoc 3 or later.
"""
import re, subprocess, sys
PANDOC, PAGE, BIB = sys.argv[1], sys.argv[2], sys.argv[3]
RENAME = dict(a.split('=') for a in sys.argv[4:] if '=' in a and not a.startswith('+'))
ADD = {}  # +Section=Key adds Key to the block under the given heading
for a in sys.argv[4:]:
    if a.startswith('+'): h, k = a[1:].split('='); ADD.setdefault(h, []).append(k)
lines = open(PAGE).read().split('\n'); out = []; i = 0; heading = None
def render(keys):
    src = '---\nnocite: |\n  ' + ', '.join('@' + k for k in keys) + '\n---\n'
    h = subprocess.run([PANDOC, '-f', 'markdown', '-t', 'html', '--citeproc', '--bibliography', BIB], input=src, capture_output=True, text=True, check=True).stdout
    items = re.findall(r'<div id="ref-([^"]+)" class="csl-entry"[^>]*>\s*(.*?)\s*</div>', h, re.S)
    assert len(items) == len(keys), (keys, [k for k, _ in items])
    res = []
    for k, b in items:
        md = subprocess.run([PANDOC, '-f', 'html', '-t', 'gfm', '--wrap=none'], input=b, capture_output=True, text=True, check=True).stdout.strip()
        md = re.sub(r'<span class="nocase">(.*?)</span>', r'\1', md)
        res.append('* ' + md + ' <!-- ' + k + ' -->')
    return res
while i < len(lines):
    l = lines[i]
    if l.startswith('#'): heading = l.lstrip('# ').strip()
    if re.match(r'^\* .*<!-- \w+ -->$', l):
        keys = []
        while i < len(lines) and re.match(r'^\* .*<!-- \w+ -->$', lines[i]):
            keys.append(RENAME.get(re.search(r'<!-- (\w+) -->$', lines[i]).group(1), re.search(r'<!-- (\w+) -->$', lines[i]).group(1))); i += 1
        keys += ADD.pop(heading, [])
        out += render(keys); continue
    out.append(l); i += 1
assert not ADD, ADD
open(PAGE, 'w').write('\n'.join(out))
