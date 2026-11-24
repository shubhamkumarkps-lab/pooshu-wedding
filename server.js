const http = require('http');
const fs = require('fs');
const path = require('path');
const { getRsvps, syncLocalSpreadsheets } = require('./lib/rsvpStore');
const {
  handlePostRsvp,
  handleGetRsvps,
  handleDownloadExcel,
  handleDownloadCsv,
  handleAdminLogin
} = require('./lib/handlers');

const PORT = process.env.PORT || 3000;
const PUBLIC_DIR = path.join(__dirname, 'public');

// Initial accounting on server boot when filesystem is writable
getRsvps()
  .then((rsvps) => {
    syncLocalSpreadsheets(rsvps);
    console.log(`[Spreadsheet Sync] Accounted ${rsvps.length} RSVPs into rsvps.xlsx and rsvps.csv`);
  })
  .catch((err) => console.error('[Spreadsheet Sync Error]:', err.message));

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.mp3': 'audio/mpeg',
  '.wav': 'audio/wav',
  '.ico': 'image/x-icon',
  '.ics': 'text/calendar; charset=utf-8',
  '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  '.csv': 'text/csv; charset=utf-8'
};

const API_ROUTES = {
  '/api/rsvp': handlePostRsvp,
  '/api/rsvps': handleGetRsvps,
  '/api/rsvps/download-excel': handleDownloadExcel,
  '/api/rsvps/export.xlsx': handleDownloadExcel,
  '/api/rsvps/export/excel': handleDownloadExcel,
  '/api/rsvps/excel': handleDownloadExcel,
  '/api/rsvps/download-csv': handleDownloadCsv,
  '/api/rsvps/export.csv': handleDownloadCsv,
  '/api/admin/login': handleAdminLogin
};

const server = http.createServer((req, res) => {
  const reqUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  let pathname = reqUrl.pathname;
  const normalizedPath = (pathname.length > 1 ? pathname.replace(/\/+$/, '') : pathname).toLowerCase();

  // API endpoints (delegated to shared handlers)
  const apiHandler = API_ROUTES[normalizedPath];
  if (apiHandler) {
    apiHandler(req, res).catch((err) => {
      console.error('[API Error]:', err);
      if (!res.headersSent) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Internal Server Error' }));
      }
    });
    return;
  }

  // CORS headers for non-API requests
  res.setHeader('Access-Control-Allow-Origin', '*');

  // Admin routing shortcut
  if (normalizedPath === '/admin') {
    pathname = '/admin.html';
  }

  // Default homepage
  if (pathname === '' || pathname === '/') {
    pathname = '/index.html';
  }

  // Static File Serving
  const filePath = path.join(PUBLIC_DIR, pathname);

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      const fallbackPath = path.join(PUBLIC_DIR, 'index.html');
      fs.readFile(fallbackPath, (fallbackErr, content) => {
        if (fallbackErr) {
          res.writeHead(404, { 'Content-Type': 'text/plain' });
          res.end('404 Not Found');
        } else {
          res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
          res.end(content);
        }
      });
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    fs.readFile(filePath, (readErr, content) => {
      if (readErr) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('500 Internal Server Error');
      } else {
        res.writeHead(200, { 'Content-Type': contentType });
        res.end(content);
      }
    });
  });
});

server.listen(PORT, () => {
  console.log(`====================================================`);
  console.log(`🌺 #pooshu Interactive Wedding Invitation Server v2 🌺`);
  console.log(`💍 Pooja Haloi & Shubham Thakur`);
  console.log(`✨ Local URL:     http://localhost:${PORT}`);
  console.log(`✨ Admin Portal:  http://localhost:${PORT}/admin`);
  console.log(`✨ RSVPs API:     http://localhost:${PORT}/api/rsvps`);
  console.log(`✨ Excel Export:  http://localhost:${PORT}/api/rsvps/download-excel`);
  console.log(`====================================================`);
});
