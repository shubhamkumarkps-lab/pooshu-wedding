/**
 * Pure Node.js Excel (.xlsx) & CSV Generator
 * Creates valid Microsoft Excel 2007+ (.xlsx) and UTF-8 CSV files
 * without requiring any third-party npm packages.
 */

const zlib = require('zlib');

// Precomputed CRC32 table
const crcTable = new Int32Array(256);
for (let i = 0; i < 256; i++) {
  let c = i;
  for (let k = 0; k < 8; k++) {
    c = ((c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1));
  }
  crcTable[i] = c;
}

function calculateCrc32(buf) {
  let crc = 0 ^ (-1);
  for (let i = 0; i < buf.length; i++) {
    crc = (crc >>> 8) ^ crcTable[(crc ^ buf[i]) & 0xFF];
  }
  return (crc ^ (-1)) >>> 0;
}

function escapeXml(str) {
  if (str == null) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

function createZip(files) {
  const fileEntries = [];
  let offset = 0;

  files.forEach(file => {
    const data = Buffer.from(file.content, typeof file.content === 'string' ? 'utf8' : undefined);
    const compressed = zlib.deflateRawSync(data);
    const useCompressed = compressed.length < data.length;
    const finalData = useCompressed ? compressed : data;
    const method = useCompressed ? 8 : 0;
    const crc = calculateCrc32(data);
    const nameBuf = Buffer.from(file.name, 'utf8');

    // Local file header (30 bytes)
    const localHeader = Buffer.alloc(30 + nameBuf.length);
    localHeader.writeUInt32LE(0x04034b50, 0); // Local header signature
    localHeader.writeUInt16LE(20, 4);         // Version needed
    localHeader.writeUInt16LE(0, 6);          // General purpose bit flag
    localHeader.writeUInt16LE(method, 8);     // Compression method
    localHeader.writeUInt16LE(0, 10);         // Mod time
    localHeader.writeUInt16LE(0, 12);         // Mod date
    localHeader.writeUInt32LE(crc, 14);       // CRC32
    localHeader.writeUInt32LE(finalData.length, 18); // Comp size
    localHeader.writeUInt32LE(data.length, 22);      // Uncomp size
    localHeader.writeUInt16LE(nameBuf.length, 26);   // Filename length
    localHeader.writeUInt16LE(0, 28);                // Extra field length
    nameBuf.copy(localHeader, 30);

    fileEntries.push({
      nameBuf,
      localHeader,
      finalData,
      offset,
      crc,
      compSize: finalData.length,
      uncompSize: data.length,
      method
    });

    offset += localHeader.length + finalData.length;
  });

  const cdEntries = [];
  let cdSize = 0;
  fileEntries.forEach(entry => {
    const cd = Buffer.alloc(46 + entry.nameBuf.length);
    cd.writeUInt32LE(0x02014b50, 0); // Central header signature
    cd.writeUInt16LE(20, 4);         // Version made by
    cd.writeUInt16LE(20, 6);         // Version needed
    cd.writeUInt16LE(0, 8);          // General purpose bit flag
    cd.writeUInt16LE(entry.method, 10);
    cd.writeUInt16LE(0, 12);
    cd.writeUInt16LE(0, 14);
    cd.writeUInt32LE(entry.crc, 16);
    cd.writeUInt32LE(entry.compSize, 20);
    cd.writeUInt32LE(entry.uncompSize, 24);
    cd.writeUInt16LE(entry.nameBuf.length, 28);
    cd.writeUInt16LE(0, 30);
    cd.writeUInt16LE(0, 32);
    cd.writeUInt16LE(0, 34);
    cd.writeUInt32LE(0, 36);
    cd.writeUInt32LE(entry.offset, 42);
    entry.nameBuf.copy(cd, 46);

    cdEntries.push(cd);
    cdSize += cd.length;
  });

  const eocd = Buffer.alloc(22);
  eocd.writeUInt32LE(0x06054b50, 0);
  eocd.writeUInt16LE(0, 4);
  eocd.writeUInt16LE(0, 6);
  eocd.writeUInt16LE(fileEntries.length, 8);
  eocd.writeUInt16LE(fileEntries.length, 10);
  eocd.writeUInt32LE(cdSize, 12);
  eocd.writeUInt32LE(offset, 16);
  eocd.writeUInt16LE(0, 20);

  const parts = [];
  fileEntries.forEach(e => {
    parts.push(e.localHeader);
    parts.push(e.finalData);
  });
  cdEntries.forEach(cd => parts.push(cd));
  parts.push(eocd);

  return Buffer.concat(parts);
}

/**
 * Generate a valid Microsoft Excel .xlsx Buffer from tabular rows
 */
function generateXlsx(rows, sheetName = 'RSVPs') {
  let sheetData = '';
  rows.forEach((row, rIdx) => {
    const rowNum = rIdx + 1;
    let rowXml = `<row r="${rowNum}">`;
    row.forEach((cellVal, cIdx) => {
      let colLetter = '';
      let n = cIdx;
      while (n >= 0) {
        colLetter = String.fromCharCode((n % 26) + 65) + colLetter;
        n = Math.floor(n / 26) - 1;
      }
      const cellRef = `${colLetter}${rowNum}`;

      if (typeof cellVal === 'number') {
        rowXml += `<c r="${cellRef}"><v>${cellVal}</v></c>`;
      } else {
        rowXml += `<c r="${cellRef}" t="inlineStr"><is><t>${escapeXml(cellVal)}</t></is></c>`;
      }
    });
    rowXml += '</row>';
    sheetData += rowXml;
  });

  const files = [
    {
      name: '[Content_Types].xml',
      content: `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>`
    },
    {
      name: '_rels/.rels',
      content: `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>`
    },
    {
      name: 'xl/_rels/workbook.xml.rels',
      content: `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>`
    },
    {
      name: 'xl/workbook.xml',
      content: `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="${escapeXml(sheetName)}" sheetId="1" r:id="rId1"/>
  </sheets>
</workbook>`
    },
    {
      name: 'xl/styles.xml',
      content: `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="1"><font><name val="Calibri"/><sz val="11"/></font></fonts>
  <fills count="1"><fill><patternFill patternType="none"/></fill></fills>
  <borders count="1"><border/></borders>
  <cellStyleXfs count="1"><xf/></cellStyleXfs>
  <cellXfs count="1"><xf/></cellXfs>
</styleSheet>`
    },
    {
      name: 'xl/worksheets/sheet1.xml',
      content: `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <sheetData>${sheetData}</sheetData>
</worksheet>`
    }
  ];

  return createZip(files);
}

/**
 * Generate UTF-8 CSV with Excel-compatible BOM
 */
function generateCsv(rows) {
  const BOM = '\uFEFF';
  const lines = rows.map(row => {
    return row.map(val => {
      const str = val == null ? '' : String(val);
      if (str.includes(',') || str.includes('"') || str.includes('\n')) {
        return `"${str.replace(/"/g, '""')}"`;
      }
      return str;
    }).join(',');
  });
  return BOM + lines.join('\r\n');
}

/**
 * Convert an array of RSVP objects into 2D tabular rows
 */
function rsvpsToTableRows(rsvps) {
  const headers = [
    'S.No.',
    'Guest Full Name',
    'Affiliation / Side',
    'Attendance Status',
    'Number of Guests',
    'DJ Song Request',
    'RSVP Timestamp (ISO)',
    'RSVP Date (Local)'
  ];

  const rows = [headers];

  rsvps.forEach((rsvp, idx) => {
    let sideLabel = 'Mutual Guest';
    if (rsvp.side === 'bride') sideLabel = "Bride's Guest (Pooja Haloi)";
    else if (rsvp.side === 'groom') sideLabel = "Groom's Guest (Shubham Thakur)";

    let attendingLabel = 'Joyfully Accept';
    if (rsvp.attending === 'no') attendingLabel = 'Regretfully Decline';

    let localDateStr = '';
    if (rsvp.timestamp) {
      try {
        localDateStr = new Date(rsvp.timestamp).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });
      } catch (e) {
        localDateStr = rsvp.timestamp;
      }
    }

    rows.push([
      idx + 1,
      rsvp.name || 'Honored Guest',
      sideLabel,
      attendingLabel,
      parseInt(rsvp.guestCount, 10) || 1,
      rsvp.djSong || '—',
      rsvp.timestamp || '',
      localDateStr
    ]);
  });

  return rows;
}

module.exports = {
  generateXlsx,
  generateCsv,
  rsvpsToTableRows
};
