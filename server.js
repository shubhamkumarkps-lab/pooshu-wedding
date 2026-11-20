const http = require('http');
const fs = require('fs');
const path = require('path');
const { rsvpsToTableRows, generateXlsx, generateCsv } = require('./excel_generator');

const PORT = process.env.PORT || 3000;
const PUBLIC_DIR = path.join(__dirname, 'public');
const RSVP_FILE = path.join(__dirname, 'rsvps.json');
const RSVP_XLSX_FILE = path.join(__dirname, 'rsvps.xlsx');
const RSVP_CSV_FILE = path.join(__dirname, 'rsvps.csv');

// Admin Credentials
const ADMIN_USER = process.env.ADMIN_USER || 'admin';
const ADMIN_PASS = process.env.ADMIN_PASS || 'PooShu#2026!Royal';

// Ensure rsvps.json exists
if (!fs.existsSync(RSVP_FILE)) {
  fs.writeFileSync(RSVP_FILE, JSON.stringify([], null, 2), 'utf-8');
}

// Sync RSVPs to Excel (.xlsx) and CSV files
function syncSpreadsheets() {
  try {
    const raw = fs.readFileSync(RSVP_FILE, 'utf-8');
    const rsvps = JSON.parse(raw || '[]');
    const rows = rsvpsToTableRows(rsvps);
    const xlsxBuf = generateXlsx(rows, 'PooShu RSVPs');
    const csvStr = generateCsv(rows);
    fs.writeFileSync(RSVP_XLSX_FILE, xlsxBuf);
    fs.writeFileSync(RSVP_CSV_FILE, csvStr, 'utf-8');
    console.log(`[Spreadsheet Sync] Accounted ${rsvps.length} RSVPs into rsvps.xlsx and rsvps.csv`);
  } catch (err) {
    console.error('[Spreadsheet Sync Error]:', err.message);
  }
}

// Initial accounting on server boot
syncSpreadsheets();

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

const server = http.createServer((req, res) => {
  const reqUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  let pathname = reqUrl.pathname;
  const normalizedPath = (pathname.length > 1 ? pathname.replace(/\/+$/, '') : pathname).toLowerCase();

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  // Prevent caching on dynamic API endpoints
  if (normalizedPath.startsWith('/api/')) {
    res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
    res.setHeader('Pragma', 'no-cache');
    res.setHeader('Expires', '0');
  }

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // API Endpoint: RSVP Submission (Appends to JSON and accounts into Excel & CSV)
  if (normalizedPath === '/api/rsvp' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const rsvpData = JSON.parse(body || '{}');
        const existing = JSON.parse(fs.readFileSync(RSVP_FILE, 'utf-8') || '[]');
        existing.push(rsvpData);
        fs.writeFileSync(RSVP_FILE, JSON.stringify(existing, null, 2), 'utf-8');

        // Automatically account in Excel format (.xlsx) and CSV
        syncSpreadsheets();

        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, message: 'RSVP recorded and accounted in Excel', rsvp: rsvpData }));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, error: err.message }));
      }
    });
    return;
  }

  // API Endpoint: Get All RSVPs JSON
  if (normalizedPath === '/api/rsvps' && req.method === 'GET') {
    try {
      const data = fs.readFileSync(RSVP_FILE, 'utf-8');
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(data);
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: e.message }));
    }
    return;
  }

  // API Endpoint: Download Excel Spreadsheet (.xlsx)
  if ((normalizedPath === '/api/rsvps/download-excel' || normalizedPath === '/api/rsvps/export.xlsx' || normalizedPath === '/api/rsvps/export/excel' || normalizedPath === '/api/rsvps/excel') && (req.method === 'GET' || req.method === 'HEAD')) {
    try {
      syncSpreadsheets();
      const fileContent = fs.readFileSync(RSVP_XLSX_FILE);
      res.writeHead(200, {
        'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'Content-Disposition': 'attachment; filename="pooshu_wedding_rsvps.xlsx"',
        'Content-Length': fileContent.length
      });
      if (req.method === 'HEAD') {
        res.end();
      } else {
        res.end(fileContent);
      }
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'Failed to generate Excel file: ' + e.message }));
    }
    return;
  }

  // API Endpoint: Download CSV Spreadsheet (.csv)
  if ((normalizedPath === '/api/rsvps/download-csv' || normalizedPath === '/api/rsvps/export.csv') && (req.method === 'GET' || req.method === 'HEAD')) {
    try {
      syncSpreadsheets();
      const fileContent = fs.readFileSync(RSVP_CSV_FILE);
      res.writeHead(200, {
        'Content-Type': 'text/csv; charset=utf-8',
        'Content-Disposition': 'attachment; filename="pooshu_wedding_rsvps.csv"',
        'Content-Length': Buffer.byteLength(fileContent)
      });
      if (req.method === 'HEAD') {
        res.end();
      } else {
        res.end(fileContent);
      }
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'Failed to generate CSV file: ' + e.message }));
    }
    return;
  }

  // API Endpoint: Admin Login Authentication
  if (normalizedPath === '/api/admin/login' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const { username, password } = JSON.parse(body || '{}');
        const cleanUser = String(username || '').trim().toLowerCase();
        const cleanAdmin = String(ADMIN_USER).trim().toLowerCase();
        const cleanPass = String(password || '').trim();
        const expectedPass = String(ADMIN_PASS).trim();

        const allowedUsers = ['admin', 'pooshu', 'shubham'];
        const isUserValid = allowedUsers.includes(cleanUser) || cleanUser === cleanAdmin;
        const isPassValid = (cleanPass === expectedPass) || (cleanPass.toLowerCase() === expectedPass.toLowerCase());

        if (isUserValid && isPassValid) {
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({
            success: true,
            message: 'Authentication successful',
            admin: cleanUser
          }));
        } else {
          res.writeHead(401, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({
            success: false,
            error: 'Invalid Login ID or Password. Please try again.'
          }));
        }
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, error: err.message }));
      }
    });
    return;
  }

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
