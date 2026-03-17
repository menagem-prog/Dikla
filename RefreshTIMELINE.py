# -*- coding: utf-8 -*-
"""
מעדכן את הנתונים של ציר הזמן ב-index.html מתוך timeline-data.json
הרצה: פתחו טרמינל בתיקייה והריצו:  python עדכן-ציר-זמן.py
אחרי ההרצה – פתחו את index.html (לחיצה כפולה) והציר יוצג עם העדכונים.
"""
import json
import re
import os

DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(DIR, 'timeline-data.json')
HTML_PATH = os.path.join(DIR, 'index.html')

def main():
    if not os.path.isfile(JSON_PATH):
        print('לא נמצא הקובץ timeline-data.json בתיקייה.')
        return
    if not os.path.isfile(HTML_PATH):
        print('לא נמצא הקובץ index.html בתיקייה.')
        return

    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    json_str = json.dumps(data, ensure_ascii=False)

    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    pattern = r'(<script type="application/json" id="timeline-data-embed">)(.*?)(</script>)'
    replacement = r'\g<1>' + json_str + r'\g<3>'
    new_html, n = re.subn(pattern, replacement, html, count=1, flags=re.DOTALL)
    if n == 0:
        print('לא נמצא מקום הנתונים ב-index.html.')
        return

    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('הציר עודכן. פתחו את index.html (לחיצה כפולה) כדי לראות את השינויים.')

if __name__ == '__main__':
    main()
