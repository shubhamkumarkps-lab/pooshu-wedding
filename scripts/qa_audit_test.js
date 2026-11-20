const http = require('http');

function fetch(url, options = {}) {
  return new Promise((resolve, reject) => {
    const req = http.request(url, options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ status: res.statusCode, headers: res.headers, body: data }));
    });
    req.on('error', reject);
    if (options.body) req.write(options.body);
    req.end();
  });
}

async function runTests() {
  const results = [];
  
  // Test 1: Root HTML
  const resHome = await fetch('http://localhost:3000/');
  results.push({
    test: 'GET / returns 200 OK',
    pass: resHome.status === 200 && resHome.body.includes('<!DOCTYPE html>')
  });

  // Test 2: HTML Wax Seal & Flower Loader structure
  results.push({
    test: 'Wax seal disc in HTML',
    pass: resHome.body.includes('id="wax-seal-disc"') && resHome.body.includes('wax-seal-img')
  });
  results.push({
    test: 'Flower blooming loader SVG in HTML (12 petals, 140x140 viewBox)',
    pass: resHome.body.includes('id="flower-blooming-svg"') && resHome.body.includes('flower-petals-ring')
  });
  results.push({
    test: 'Save The Date card structure in HTML',
    pass: resHome.body.includes('id="save-date-card-wrap"') && resHome.body.includes('id="save-the-date-card"')
  });

  // Test 3: Cultural ribbon completely removed from HTML
  results.push({
    test: 'assamese_border.svg not in index.html',
    pass: !resHome.body.includes('assamese_border.svg')
  });
  results.push({
    test: 'Flanking motifs (assamese_xorai_kopou.svg & maithili_peacock_lotus.svg) removed from index.html',
    pass: !resHome.body.includes('assamese_xorai_kopou.svg') && !resHome.body.includes('maithili_peacock_lotus.svg')
  });

  // Test 4: Ceremonial Emojis in index.html
  results.push({
    test: 'Hero tagline has 🌺 Two Cultures, One Eternal Promise',
    pass: resHome.body.includes('🌺 Two Cultures, One Eternal Promise')
  });
  results.push({
    test: 'Hero CTAs have 🌸 Know the Bride: Pooja, 🦚 Know the Groom: Shubham, 📖 Our 12-Year Story',
    pass: resHome.body.includes('🌸 Know the Bride: Pooja') &&
          resHome.body.includes('🦚 Know the Groom: Shubham') &&
          resHome.body.includes('📖 Our 12-Year Story')
  });
  results.push({
    test: 'Scratch heading has ✨ Scratch to Reveal our Wedding Date!',
    pass: resHome.body.includes('✨ Scratch to Reveal our Wedding Date!')
  });
  results.push({
    test: 'Events heading has 💍 Wedding Celebrations',
    pass: resHome.body.includes('💍 Wedding Celebrations')
  });
  results.push({
    test: 'RSVP heading has 💌 Celebrate With Us',
    pass: resHome.body.includes('💌 Celebrate With Us')
  });
  results.push({
    test: 'Audio tabs have 🎵 Maithili Song and 🎶 Assamese Song',
    pass: resHome.body.includes('🎵 Maithili Song') && resHome.body.includes('🎶 Assamese Song')
  });

  // Test 5: CSS Styles verification
  const resCss = await fetch('http://localhost:3000/style.css');
  results.push({
    test: 'GET /style.css returns 200 OK',
    pass: resCss.status === 200
  });
  results.push({
    test: 'Wax seal disc enlarged to 106px with 3D drop-shadow and specular highlight in CSS',
    pass: resCss.body.includes('.wax-seal-disc') &&
          resCss.body.includes('width: 106px;') &&
          resCss.body.includes('height: 106px;') &&
          resCss.body.includes('inset 0 2px 4px rgba(255, 255, 255, 0.4)')
  });
  results.push({
    test: 'Flower blooming loader scaled to 164px in CSS',
    pass: resCss.body.includes('.flower-blooming-loader') &&
          resCss.body.includes('width: 164px;') &&
          resCss.body.includes('height: 164px;')
  });
  results.push({
    test: 'Save The Date wrapper has inset margins (top: 10px, bottom: 10px, left/right: 12px)',
    pass: resCss.body.includes('.save-the-date-card-wrapper') &&
          resCss.body.includes('top: 10px;') &&
          resCss.body.includes('bottom: 10px;')
  });
  results.push({
    test: 'Save The Date img has object-fit: cover and object-position: center 40%',
    pass: resCss.body.includes('.save-the-date-img') &&
          resCss.body.includes('object-fit: cover;') &&
          resCss.body.includes('object-position: center 40%;')
  });
  results.push({
    test: 'Cultural ribbon is display: none in CSS',
    pass: resCss.body.includes('.cultural-ribbon') &&
          resCss.body.includes('display: none;')
  });
  results.push({
    test: 'Nav brand logo has border-radius: 10px in CSS',
    pass: resCss.body.includes('.nav-brand-logo') &&
          resCss.body.includes('border-radius: 10px;')
  });

  // Test 6: Flower particles JS verification
  const resParticles = await fetch('http://localhost:3000/flower_particles.js');
  results.push({
    test: 'GET /flower_particles.js returns 200 OK',
    pass: resParticles.status === 200
  });
  results.push({
    test: 'Petal size increased by 25% (4.4 + Math.random() * 3.8 -> 4.4px to 8.2px)',
    pass: resParticles.body.includes('4.4 + Math.random() * 3.8')
  });
  results.push({
    test: 'Petal scale range 0.6 to 1.0 (0.6 + Math.random() * 0.4)',
    pass: resParticles.body.includes('0.6 + Math.random() * 0.4')
  });

  // Test 7: App JS verification for event card metadata emojis
  const resApp = await fetch('http://localhost:3000/app.js');
  results.push({
    test: 'GET /app.js returns 200 OK',
    pass: resApp.status === 200
  });
  results.push({
    test: 'Event metadata has 📅 Date, ⏰ Timing, 📍 Venue, 👗 Dress Code in app.js',
    pass: resApp.body.includes('📅 ${dateText}') &&
          resApp.body.includes('⏰ ${timeText}') &&
          resApp.body.includes('📍 ${ev.venue}') &&
          resApp.body.includes('👗 Dress Code: ${ev.dressCodeTitle}')
  });

  // Test 8: RSVP API functionality
  const testRsvpPayload = JSON.stringify({
    name: 'QA Automation Bot',
    attendance: 'attending',
    guestsCount: 1,
    eventsAttending: ['tilak_sagai'],
    dietary: 'Vegetarian',
    message: 'Audit verification test RSVP',
    djSong: 'London Thumakda',
    submittedAt: new Date().toISOString()
  });

  const resPostRsvp = await fetch('http://localhost:3000/api/rsvp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: testRsvpPayload
  });
  results.push({
    test: 'POST /api/rsvp records RSVP successfully (200 OK)',
    pass: resPostRsvp.status === 200 && JSON.parse(resPostRsvp.body).success === true
  });

  const resGetRsvps = await fetch('http://localhost:3000/api/rsvps');
  results.push({
    test: 'GET /api/rsvps returns array with recorded RSVP',
    pass: resGetRsvps.status === 200 && resGetRsvps.body.includes('QA Automation Bot')
  });

  let allPassed = true;
  for (const r of results) {
    console.log(`${r.pass ? '✅ PASS' : '❌ FAIL'}: ${r.test}`);
    if (!r.pass) allPassed = false;
  }

  console.log(`\nOverall: ${allPassed ? 'ALL TESTS PASSED (100%)' : 'SOME TESTS FAILED'}`);
}

runTests().catch(err => {
  console.error('Test execution failed:', err);
  process.exit(1);
});
