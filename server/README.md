# שמירת סרטונים מקומית

השרת מקבל את הסרטון מהאפליקציה ושומר אותו כקובץ במחשב שמריץ את השרת.

## 1. מבנה

- תיקייה: `server/videos` – כאן יישמרו כל הקבצים.
- שם הקובץ: `dikla-journey-YYYY-MM-DD-HH-MM-SS.webm`

## 2. הגדרת השרת

בתיקייה `server`:

```bash
cp .env.example .env   # אופציונלי
```

אפשר להשאיר את ברירת המחדל:

- `PORT=3000`

## 3. הרצה

```bash
cd server
npm install
npm start
```

השרת יעלה על `http://localhost:3000` וישמור קבצים ב-`server/videos`.

## 4. התחברות מהאפליקציה

ב-`index.html` יש משתנה:

```js
var UPLOAD_VIDEO_URL = 'http://localhost:3000/upload';
```

כאשר האפליקציה מסיימת לבנות את הסרטון, היא שולחת אותו ב-`POST` לכתובת הזו בתור `FormData` עם שדה בשם `video`, והשרת שומר אותו מקומית.
