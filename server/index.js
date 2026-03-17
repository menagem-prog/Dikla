/**
 * שרת שמקבל סרטון מהאפליקציה ושומר אותו מקומית במחשב שמריץ את השרת.
 * הרצה: npm install && npm start
 */
const express = require('express');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;
const VIDEOS_DIR = path.join(__dirname, 'videos');

// לוודא שתיקיית הווידאו קיימת
if (!fs.existsSync(VIDEOS_DIR)) {
  fs.mkdirSync(VIDEOS_DIR, { recursive: true });
}

// CORS – לאפשר לאפליקציה (גם מ-GitHub Pages) לשלוח סרטון
app.use(cors({
  origin: true,
  methods: ['POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type']
}));

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    const sessionId = (req.body && req.body.sessionId) ? req.body.sessionId.toString().replace(/[^a-zA-Z0-9._-]/g, '_') : 'no-session';
    const sessionDir = path.join(VIDEOS_DIR, sessionId);
    if (!fs.existsSync(sessionDir)) {
      fs.mkdirSync(sessionDir, { recursive: true });
    }
    cb(null, sessionDir);
  },
  filename: function (req, file, cb) {
    const original = (file.originalname || 'segment.webm').toString();
    const safeOriginal = original.replace(/[^a-zA-Z0-9._-]/g, '_');
    cb(null, safeOriginal);
  }
});

const upload = multer({
  storage: storage,
  limits: { fileSize: 100 * 1024 * 1024 }
});

app.post('/upload', upload.single('video'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ ok: false, error: 'No video file' });
  }
  const relativePath = path.relative(process.cwd(), req.file.path);
  res.json({
    ok: true,
    filename: req.file.filename,
    path: relativePath
  });
});

app.get('/health', (req, res) => {
  res.json({ ok: true, message: 'upload server running', saveTo: VIDEOS_DIR });
});

app.listen(PORT, () => {
  console.log('Server running on port', PORT, 'saving videos to', VIDEOS_DIR);
});
