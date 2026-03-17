# -*- coding: utf-8 -*-
r"""
Updates the stations (riddles) data in index.html from stations-data.json
Run from this folder:  python .\RefreshSTATIONS.py
"""
import json
import re
import os

DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(DIR, 'stations-data.json')
HTML_PATH = os.path.join(DIR, 'index.html')

def main():
    if not os.path.isfile(JSON_PATH):
        print('stations-data.json not found in this folder.')
        return
    if not os.path.isfile(HTML_PATH):
        print('index.html not found in this folder.')
        return

    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    json_str = json.dumps(data, ensure_ascii=False)

    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    pattern = r'(<script type="application/json" id="stations-data-embed">)(.*?)(</script>)'
    replacement = r'\g<1>' + json_str + r'\g<3>'
    new_html, n = re.subn(pattern, replacement, html, count=1, flags=re.DOTALL)
    if n == 0:
        print('stations-data-embed block not found in index.html.')
        return

    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Stations updated. Refresh index.html to see changes.')

if __name__ == '__main__':
    main()
