#!/usr/bin/env python3
"""Turn the YouTube thumbnails into embedded players, for the published site.

The Markdown sources keep a thumbnail linking to YouTube, because that is what
GitHub renders: it strips <iframe> and shows MyST directives as raw text. This
script is run by the deploy workflow, on the runner only, just before the site
is built — the files in git are never modified.
"""
import pathlib
import re
import sys

BLOCK = re.compile(
    r'<p align="center">\s*'
    r'<a href="[^"]*"><img src="https://img\.youtube\.com/vi/(?P<id>[\w-]+)/mqdefault\.jpg"'
    r'[^>]*></a><br>\s*'
    r'<a href="[^"]*">▶ Video: (?P<title>[^<]+)</a>\s*'
    r'</p>')

TEMPLATE = ':::{{iframe}} https://www.youtube.com/embed/{id}\n:width: 100%\n{title}\n:::'


def main(root='doc'):
    converted = 0
    for path in sorted(pathlib.Path(root).rglob('*.md')):
        text = path.read_text()
        if 'img.youtube.com' not in text:
            continue
        new, n = BLOCK.subn(
            lambda m: TEMPLATE.format(id=m.group('id'), title=m.group('title')), text)
        if n:
            path.write_text(new)
            converted += n
            print(f'  {path}: {n}')
        left = new.count('img.youtube.com')
        if left:
            print(f'ERROR: {path} still has {left} thumbnail(s) the pattern did not match',
                  file=sys.stderr)
            return 1
    print(f'{converted} video(s) embedded')
    return 0 if converted else 1


if __name__ == '__main__':
    sys.exit(main())
