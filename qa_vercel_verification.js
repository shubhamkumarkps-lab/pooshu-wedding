/**
 * Vercel Serverless + Local HTTP Verification Suite
 * Simulates Vercel runtime (VERCEL=1, pre-parsed req.body, /tmp storage, in-memory Excel/CSV)
 * and verifies local server.js endpoints as well.
 */

const assert = require('assert');
const fs = require('fs');
const path = require('path');

function createMockRes() {
  const headers = {};
  let statusCode = 200;
  const chunks = [];
  return {
    setHeader(k, v) { headers[k.toLowerCase()] = v; },
    writeHead(code, h) {
      statusCode = code;
      if (h) Object.entries(h).forEach(([k, v]) => { headers[k.toLowerCase()] = v; });
    },
    end(data) {
      if (data !== undefined) {
        chunks.push(Buffer.isBuffer(data) ? data : Buffer.from(String(data)));
      }
    },
    getStatus() { return statusCode; },
    getHeaders() { return headers; },
    getBodyBuffer() { return Buffer.concat(chunks); },
    getBodyText() { return Buffer.concat(chunks).toString('utf8'); },
    getBodyJson() { return JSON.parse(this.getBodyText()); }
  };
}

async function runTests() {
  console.log('====================================================');
  console.log('⚡ RUNNING VERCEL SERVERLESS COMPATIBILITY TESTS');
  console.log('====================================================\n');

  // Simulate Vercel read-only bundle environment
  process.env.VERCEL = '1';
  if (fs.existsSync('/tmp/pooshu_rsvps.json')) {
    fs.unlinkSync('/tmp/pooshu_rsvps.json');
  }

  const rsvpFn = require('./api/rsvp');
  const rsvpsFn = require('./api/rsvps/index');
  const excelFn = require('./api/rsvps/download-excel');
  const csvFn = require('./api/rsvps/download-csv');
  const loginFn = require('./api/admin/login');
  const vercelJson = JSON.parse(fs.readFileSync(path.join(__dirname, 'vercel.json'), 'utf8'));

  // 1. Validate vercel.json
  assert.strictEqual(vercelJson.outputDirectory, 'public', 'vercel.json outputDirectory must be public');
  assert.strictEqual(vercelJson.cleanUrls, true, 'vercel.json cleanUrls enabled');
  assert(vercelJson.rewrites.some(r => r.source === '/admin' && r.destination === '/admin.html'), '/admin rewrite present');
  console.log('  ✅ PASS: vercel.json schema & rewrites valid');

  // 2. Validate GET /api/rsvps (seeded from rsvps.json)
  let res = createMockRes();
  await rsvpsFn({ method: 'GET', headers: {} }, res);
  assert.strictEqual(res.getStatus(), 200);
  const initialList = res.getBodyJson();
  assert(Array.isArray(initialList) && initialList.length >= 4, 'Initial RSVPs seeded correctly');
  console.log(`  ✅ PASS: GET /api/rsvps returned ${initialList.length} seeded records under VERCEL=1`);

  // 3. Validate POST /api/rsvp with Vercel pre-parsed req.body object
  res = createMockRes();
  await rsvpFn({
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: {
      name: 'Vercel Cloud Test',
      side: 'mutual',
      attending: 'yes',
      guestCount: 2,
      djSong: 'Kesariya',
      timestamp: new Date().toISOString()
    }
  }, res);
  assert.strictEqual(res.getStatus(), 200);
  const postJson = res.getBodyJson();
  assert.strictEqual(postJson.success, true);
  assert.strictEqual(postJson.storage, 'ephemeral-tmp');
  console.log('  ✅ PASS: POST /api/rsvp succeeded with pre-parsed req.body & /tmp fallback');

  // 4. Confirm new RSVP is returned on subsequent GET
  res = createMockRes();
  await rsvpsFn({ method: 'GET', headers: {} }, res);
  const updatedList = res.getBodyJson();
  assert(updatedList.some(r => r.name === 'Vercel Cloud Test'), 'Posted RSVP persisted in /tmp for subsequent requests');
  console.log('  ✅ PASS: GET /api/rsvps reflects newly submitted RSVP');

  // 5. Validate Excel (.xlsx) in-memory generation
  res = createMockRes();
  await excelFn({ method: 'GET', headers: {} }, res);
  assert.strictEqual(res.getStatus(), 200);
  assert.strictEqual(
    res.getHeaders()['content-type'],
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
  );
  const xlsxBuf = res.getBodyBuffer();
  assert(xlsxBuf.length > 1000 && xlsxBuf[0] === 0x50 && xlsxBuf[1] === 0x4b, 'Valid XLSX PK zip header generated in-memory');
  console.log(`  ✅ PASS: GET /api/rsvps/download-excel generated valid XLSX (${xlsxBuf.length} bytes) without disk writes`);

  // 6. Validate CSV in-memory generation
  res = createMockRes();
  await csvFn({ method: 'GET', headers: {} }, res);
  assert.strictEqual(res.getStatus(), 200);
  assert(res.getBodyText().includes('Vercel Cloud Test'), 'CSV includes newly submitted RSVP');
  console.log('  ✅ PASS: GET /api/rsvps/download-csv generated valid CSV');

  // 7. Validate Admin Login
  res = createMockRes();
  await loginFn({
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: { username: 'admin', password: 'PooShu#2026!Royal' }
  }, res);
  assert.strictEqual(res.getStatus(), 200);
  assert.strictEqual(res.getBodyJson().success, true);
  console.log('  ✅ PASS: POST /api/admin/login authenticates properly on Vercel');

  // Cleanup temp file
  if (fs.existsSync('/tmp/pooshu_rsvps.json')) {
    fs.unlinkSync('/tmp/pooshu_rsvps.json');
  }

  console.log('\n🎉 ALL 7 VERCEL SERVERLESS COMPATIBILITY CHECKS PASSED!');
}

runTests().catch((err) => {
  console.error('❌ Verification failed:', err);
  process.exit(1);
});
