/**
 * Shared API Request Handlers
 * Compatible with both standalone Node HTTP server (server.js)
 * and Vercel Serverless Functions (api/*.js).
 */

const { rsvpsToTableRows, generateXlsx, generateCsv } = require('../excel_generator');
const { getRsvps, addRsvp, getStorageMode } = require('./rsvpStore');

const ADMIN_USER = process.env.ADMIN_USER || 'admin';
const ADMIN_PASS = process.env.ADMIN_PASS || 'PooShu#2026!Royal';

function setApiHeaders(res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');
}

function sendJson(res, statusCode, payload) {
  res.writeHead(statusCode, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify(payload));
}

function parseJsonBody(req) {
  return new Promise((resolve, reject) => {
    // Vercel's Node runtime pre-parses JSON bodies into req.body
    if (req.body !== undefined && req.body !== null) {
      if (typeof req.body === 'object') {
        return resolve(req.body);
      }
      if (typeof req.body === 'string') {
        try {
          return resolve(JSON.parse(req.body || '{}'));
        } catch (err) {
          return reject(err);
        }
      }
    }

    let body = '';
    req.on('data', (chunk) => { body += chunk; });
    req.on('end', () => {
      try {
        resolve(JSON.parse(body || '{}'));
      } catch (err) {
        reject(err);
      }
    });
    req.on('error', reject);
  });
}

function handlePreflight(req, res) {
  setApiHeaders(res);
  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return true;
  }
  return false;
}

async function handlePostRsvp(req, res) {
  if (handlePreflight(req, res)) return;
  if (req.method !== 'POST') {
    return sendJson(res, 405, { success: false, error: 'Method Not Allowed' });
  }

  try {
    const rsvpData = await parseJsonBody(req);
    await addRsvp(rsvpData);
    sendJson(res, 200, {
      success: true,
      message: 'RSVP recorded and accounted in Excel',
      storage: getStorageMode(),
      rsvp: rsvpData
    });
  } catch (err) {
    sendJson(res, 400, { success: false, error: err.message });
  }
}

async function handleGetRsvps(req, res) {
  if (handlePreflight(req, res)) return;
  if (req.method !== 'GET') {
    return sendJson(res, 405, { error: 'Method Not Allowed' });
  }

  try {
    const rsvps = await getRsvps();
    sendJson(res, 200, rsvps);
  } catch (err) {
    sendJson(res, 500, { error: err.message });
  }
}

async function handleDownloadExcel(req, res) {
  if (handlePreflight(req, res)) return;
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    return sendJson(res, 405, { error: 'Method Not Allowed' });
  }

  try {
    const rsvps = await getRsvps();
    const rows = rsvpsToTableRows(rsvps);
    const xlsxBuf = generateXlsx(rows, 'PooShu RSVPs');
    res.writeHead(200, {
      'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      'Content-Disposition': 'attachment; filename="pooshu_wedding_rsvps.xlsx"',
      'Content-Length': xlsxBuf.length
    });
    res.end(req.method === 'HEAD' ? undefined : xlsxBuf);
  } catch (err) {
    sendJson(res, 500, { error: 'Failed to generate Excel file: ' + err.message });
  }
}

async function handleDownloadCsv(req, res) {
  if (handlePreflight(req, res)) return;
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    return sendJson(res, 405, { error: 'Method Not Allowed' });
  }

  try {
    const rsvps = await getRsvps();
    const rows = rsvpsToTableRows(rsvps);
    const csvStr = generateCsv(rows);
    res.writeHead(200, {
      'Content-Type': 'text/csv; charset=utf-8',
      'Content-Disposition': 'attachment; filename="pooshu_wedding_rsvps.csv"',
      'Content-Length': Buffer.byteLength(csvStr)
    });
    res.end(req.method === 'HEAD' ? undefined : csvStr);
  } catch (err) {
    sendJson(res, 500, { error: 'Failed to generate CSV file: ' + err.message });
  }
}

async function handleAdminLogin(req, res) {
  if (handlePreflight(req, res)) return;
  if (req.method !== 'POST') {
    return sendJson(res, 405, { success: false, error: 'Method Not Allowed' });
  }

  try {
    const { username, password } = await parseJsonBody(req);
    const cleanUser = String(username || '').trim().toLowerCase();
    const cleanAdmin = String(ADMIN_USER).trim().toLowerCase();
    const cleanPass = String(password || '').trim();
    const expectedPass = String(ADMIN_PASS).trim();

    const allowedUsers = ['admin', 'pooshu', 'shubham'];
    const isUserValid = allowedUsers.includes(cleanUser) || cleanUser === cleanAdmin;
    const isPassValid = (cleanPass === expectedPass) || (cleanPass.toLowerCase() === expectedPass.toLowerCase());

    if (isUserValid && isPassValid) {
      sendJson(res, 200, {
        success: true,
        message: 'Authentication successful',
        admin: cleanUser
      });
    } else {
      sendJson(res, 401, {
        success: false,
        error: 'Invalid Login ID or Password. Please try again.'
      });
    }
  } catch (err) {
    sendJson(res, 400, { success: false, error: err.message });
  }
}

module.exports = {
  setApiHeaders,
  handlePostRsvp,
  handleGetRsvps,
  handleDownloadExcel,
  handleDownloadCsv,
  handleAdminLogin
};
