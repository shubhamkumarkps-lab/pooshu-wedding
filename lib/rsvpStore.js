/**
 * Unified RSVP Storage Layer
 * Works seamlessly across:
 * 1. Vercel KV / Upstash Redis (persistent cloud storage when env vars are set)
 * 2. Local / Render filesystem (rsvps.json + rsvps.xlsx + rsvps.csv)
 * 3. Vercel read-only filesystem fallback (/tmp + seed from bundled rsvps.json)
 */

const fs = require('fs');
const path = require('path');
const { rsvpsToTableRows, generateXlsx, generateCsv } = require('../excel_generator');

const ROOT_RSVP_FILE = path.join(__dirname, '..', 'rsvps.json');
const ROOT_XLSX_FILE = path.join(__dirname, '..', 'rsvps.xlsx');
const ROOT_CSV_FILE = path.join(__dirname, '..', 'rsvps.csv');
const TMP_RSVP_FILE = '/tmp/pooshu_rsvps.json';
const KV_KEY = 'pooshu:rsvps';

// Load bundled seed data via require so Vercel's file tracer always includes rsvps.json
let bundledSeed = [];
try {
  bundledSeed = require('../rsvps.json');
  if (!Array.isArray(bundledSeed)) bundledSeed = [];
} catch (_) {
  bundledSeed = [];
}

function getSeedCopy() {
  return JSON.parse(JSON.stringify(bundledSeed));
}

function getRedisConfig() {
  const url = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  if (url && token) {
    return { url: url.replace(/\/+$/, ''), token };
  }
  return null;
}

async function redisCommand(config, commandArray) {
  const res = await fetch(config.url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${config.token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(commandArray)
  });
  if (!res.ok) {
    throw new Error(`Redis HTTP ${res.status}`);
  }
  return res.json();
}

function isRootWritable() {
  // Vercel serverless runtime mounts the deployment bundle read-only at /var/task
  if (process.env.VERCEL) return false;
  try {
    fs.accessSync(path.dirname(ROOT_RSVP_FILE), fs.constants.W_OK);
    return true;
  } catch (_) {
    return false;
  }
}

function syncLocalSpreadsheets(rsvps) {
  if (!isRootWritable()) return;
  try {
    const rows = rsvpsToTableRows(rsvps);
    fs.writeFileSync(ROOT_XLSX_FILE, generateXlsx(rows, 'PooShu RSVPs'));
    fs.writeFileSync(ROOT_CSV_FILE, generateCsv(rows), 'utf-8');
  } catch (err) {
    console.error('[Spreadsheet Sync Error]:', err.message);
  }
}

function readFsRsvps() {
  if (isRootWritable() && fs.existsSync(ROOT_RSVP_FILE)) {
    try {
      const parsed = JSON.parse(fs.readFileSync(ROOT_RSVP_FILE, 'utf-8') || '[]');
      if (Array.isArray(parsed)) return parsed;
    } catch (_) {}
  }

  if (fs.existsSync(TMP_RSVP_FILE)) {
    try {
      const parsed = JSON.parse(fs.readFileSync(TMP_RSVP_FILE, 'utf-8') || '[]');
      if (Array.isArray(parsed)) return parsed;
    } catch (_) {}
  }

  return getSeedCopy();
}

function writeFsRsvps(rsvps) {
  if (isRootWritable()) {
    fs.writeFileSync(ROOT_RSVP_FILE, JSON.stringify(rsvps, null, 2), 'utf-8');
    syncLocalSpreadsheets(rsvps);
    return;
  }

  try {
    fs.writeFileSync(TMP_RSVP_FILE, JSON.stringify(rsvps, null, 2), 'utf-8');
  } catch (err) {
    console.warn('[Temp RSVP Write Notice]:', err.message);
  }
}

async function getRsvps() {
  const redis = getRedisConfig();
  if (redis) {
    try {
      const data = await redisCommand(redis, ['GET', KV_KEY]);
      if (data && data.result) {
        const parsed = JSON.parse(data.result);
        if (Array.isArray(parsed)) return parsed;
      }
      // First-time seed into Redis
      const seed = getSeedCopy();
      await redisCommand(redis, ['SET', KV_KEY, JSON.stringify(seed)]);
      return seed;
    } catch (err) {
      console.warn('[Redis Read Fallback]:', err.message);
    }
  }
  return readFsRsvps();
}

async function addRsvp(rsvpData) {
  const existing = await getRsvps();
  existing.push(rsvpData);

  const redis = getRedisConfig();
  if (redis) {
    try {
      await redisCommand(redis, ['SET', KV_KEY, JSON.stringify(existing)]);
      return existing;
    } catch (err) {
      console.warn('[Redis Write Fallback]:', err.message);
    }
  }

  writeFsRsvps(existing);
  return existing;
}

function getStorageMode() {
  if (getRedisConfig()) return 'redis';
  if (isRootWritable()) return 'local-fs';
  return 'ephemeral-tmp';
}

module.exports = {
  getRsvps,
  addRsvp,
  syncLocalSpreadsheets,
  getStorageMode
};
