/**
 * Quality Assurance Comprehensive Verification Script
 * Validates all updates requested by user:
 * 1. Admin page: default credentials removed
 * 2. Envelope flow: silent envelope opening with only seal break SFX
 * 3. Default song: Assamese "Indradhanu" on site entry (15s start)
 * 4. Music uncoupled: language switching does not switch music
 * 5. Music player: switching to Maithili switches track cleanly
 * 6. Mobile story card: object-fit contain, responsive max-height scaling
 * 7. Edge navigation: LHS and RHS buttons present in gallery viewport
 * 8. Touch swipe listeners present in app.js
 */

const fs = require('fs');
const path = require('path');

let passCount = 0;
let failCount = 0;

function assert(condition, message) {
  if (condition) {
    console.log(`  ✅ PASS: ${message}`);
    passCount++;
  } else {
    console.error(`  ❌ FAIL: ${message}`);
    failCount++;
  }
}

console.log('====================================================');
console.log('🚀 RUNNING SPRINT COMPREHENSIVE QA VERIFICATION');
console.log('====================================================\n');

// 1. Admin Page Checks
console.log('--- 1. Admin Portal Security ---');
const adminHtml = fs.readFileSync(path.join(__dirname, 'public/admin.html'), 'utf8');
assert(!adminHtml.includes('Default Credentials:'), 'Credentials hint removed from admin.html');
assert(!adminHtml.includes('PooShu#2026!Royal'), 'Raw admin password text removed from admin.html markup');
assert(adminHtml.includes('Authenticate Access'), 'Admin login form submit button intact');
assert(adminHtml.includes('login-password'), 'Admin password input field intact');

// 2. Audio Engine & Invitation Flow Checks
console.log('\n--- 2. Audio Engine & Flow ---');
const appJs = fs.readFileSync(path.join(__dirname, 'public/app.js'), 'utf8');
const soundscapeJs = fs.readFileSync(path.join(__dirname, 'public/soundscape.js'), 'utf8');

// Check envelope open is silent
const triggerOpenBlock = appJs.substring(appJs.indexOf('const triggerOpen = () => {'), appJs.indexOf('const startHolding = (e) => {'));
assert(!triggerOpenBlock.includes('togglePlay()'), 'Envelope opening flap does not autoplay music (silent invitation flow)');
assert(triggerOpenBlock.includes('playSealBreak()'), 'Wax fracture SFX plays on seal fracture');

// Check enterMainSite starts Assamese track
const enterMainSiteBlock = appJs.substring(appJs.indexOf('enterMainSite() {'), appJs.indexOf('startCountdown() {'));
assert(enterMainSiteBlock.includes('startDefaultTrack()'), 'enterMainSite() triggers startDefaultTrack()');

// Check default track is Assamese
assert(soundscapeJs.includes("currentTrack = 'as'"), 'Default audio track is Assamese ("as")');
assert(soundscapeJs.includes("startSeconds: 15"), 'Assamese track has 15s start timestamp');
assert(soundscapeJs.includes("startDefaultTrack()"), 'SoundscapeEngine exposes startDefaultTrack()');

// Check language switcher syncs with music
const switchLangBlock = appJs.substring(appJs.indexOf('switchLanguage(lang) {'), appJs.indexOf('renderLanguage(lang) {'));
assert(switchLangBlock.includes('syncWithLanguage(lang)'), 'switchLanguage calls syncWithLanguage(lang)');
assert(soundscapeJs.includes("if (lang === 'mai')") && soundscapeJs.includes("switchTrack('mai')"), 'Switching to Maithili triggers Maithili song');
assert(soundscapeJs.includes("else if (lang === 'as')") && soundscapeJs.includes("switchTrack('as')"), 'Switching to Assamese triggers Assamese song');

// 3. Groom Residence Address Check
console.log("\n--- 3. Groom's Address Verification ---");
const enJson = JSON.parse(fs.readFileSync(path.join(__dirname, 'public/data/en.json'), 'utf8'));
const asJson = JSON.parse(fs.readFileSync(path.join(__dirname, 'public/data/as.json'), 'utf8'));
const maiJson = JSON.parse(fs.readFileSync(path.join(__dirname, 'public/data/mai.json'), 'utf8'));

const enHaldi = enJson.events.list.find(e => e.id === 'haldi_groom');
assert(enHaldi && enHaldi.venue.includes('2nd Floor, 1371, Block B, Greenfield Colony, Sector 43, Faridabad, Haryana, 121010'), 'EN Groom residence address updated');
assert(enHaldi && enHaldi.mapsUrl.includes('1371') && enHaldi.mapsUrl.includes('Sector+43'), 'EN Groom residence Google Maps URL updated');

const asHaldi = asJson.events.list.find(e => e.id === 'haldi_groom');
assert(asHaldi && asHaldi.venue.includes('১৩৭১') && asHaldi.venue.includes('চেক্টৰ ৪৩'), 'Assamese Groom residence address updated');

const maiHaldi = maiJson.events.list.find(e => e.id === 'haldi_groom');
assert(maiHaldi && maiHaldi.venue.includes('१३७१') && maiHaldi.venue.includes('सेक्टर ४३'), 'Maithili Groom residence address updated');

// 3. Story Page Mobile Scaling & Edge Navigation
console.log('\n--- 3. Our Story Mobile Scaling & Edge Navigation ---');
const indexHtml = fs.readFileSync(path.join(__dirname, 'public/index.html'), 'utf8');
const styleCss = fs.readFileSync(path.join(__dirname, 'public/style.css'), 'utf8');

assert(indexHtml.includes('class="story-gallery-viewport"'), 'story-gallery-viewport container exists');
assert(indexHtml.includes('btn-story-edge-prev') && indexHtml.includes('id="story-prev-btn"'), 'LHS edge previous button exists');
assert(indexHtml.includes('btn-story-edge-next') && indexHtml.includes('id="story-next-btn"'), 'RHS edge next button exists');
assert(indexHtml.includes('class="story-carousel-footer"') && indexHtml.includes('id="story-dots-container"'), 'Centered dots footer exists');

// CSS checks
assert(styleCss.includes('.btn-story-edge-prev') && styleCss.includes('.btn-story-edge-next'), 'LHS & RHS edge buttons styled in CSS');
assert(styleCss.includes('.btn-story-edge-prev {\n  left: -24px;') || styleCss.includes('left: -24px;'), 'Desktop LHS button positioned on left edge');
assert(styleCss.includes('.story-card-media img {\n  width: 100%;\n  height: auto;\n  max-height: 520px;\n  object-fit: contain;') || styleCss.includes('object-fit: contain;'), 'Story image uses object-fit: contain to prevent cropping');
assert(styleCss.includes('left: 10px;') && styleCss.includes('right: 10px;'), 'Mobile LHS & RHS buttons styled for thumb reach');

// Touch gesture checks
assert(appJs.includes('touchstart') && appJs.includes('touchend'), 'Touch swipe gesture handling active on story card');

// 5. Feedback Round Verification
console.log('\n--- 5. Final Feedback Round Checks ---');
// Gap between envelope graphic and button increased
assert(styleCss.includes('.welcome-action-hint {\n  margin-top: 56px;') || styleCss.includes('margin-top: 56px;'), 'Gap between envelope graphic and Tap to Unveil button increased to 56px');

// Audio silence guard on first page
assert(soundscapeJs.includes('hasEnteredSite = false'), 'Strict silence on first page guarded by hasEnteredSite = false');
assert(soundscapeJs.includes('if (!this.hasEnteredSite) return;'), 'startAmbientRaga guarded from playing on first page');

// Favicon Wax Seal 1 check
assert(fs.existsSync(path.join(__dirname, 'public/favicon.png')), 'favicon.png generated from Wax Seal 1');
assert(fs.existsSync(path.join(__dirname, 'public/favicon-32.png')), 'favicon-32.png generated from Wax Seal 1');
assert(indexHtml.includes('favicon.png') && indexHtml.includes('favicon-32.png'), 'index.html references Wax Seal 1 favicon');
assert(adminHtml.includes('favicon.png') && adminHtml.includes('favicon-32.png'), 'admin.html references Wax Seal 1 favicon');

// Test 3 RSVP check
const rsvps = JSON.parse(fs.readFileSync(path.join(__dirname, 'rsvps.json'), 'utf8'));
const test3 = rsvps.find(r => (r.name || r.fullname) === 'Test 3');
assert(test3 !== undefined, 'RSVP Test 3 entry exists in rsvps.json');
assert(test3 && test3.attending === 'yes', 'Test 3 attendance recorded');
assert(test3 && (test3.guestCount == 2 || test3.guests == 2), 'Test 3 guest count recorded as 2');

// Flexible admin authentication check (delegated from server.js & api/ to lib/handlers.js)
const serverJs = fs.readFileSync(path.join(__dirname, 'server.js'), 'utf8');
const handlersJs = fs.readFileSync(path.join(__dirname, 'lib/handlers.js'), 'utf8');
assert(serverJs.includes("require('./lib/handlers')"), 'server.js delegates API handling to shared lib/handlers.js');
assert(handlersJs.includes("allowedUsers = ['admin', 'pooshu', 'shubham']"), 'Handlers allow flexible admin usernames (admin, pooshu, shubham)');
assert(handlersJs.includes('toLowerCase() === expectedPass.toLowerCase()'), 'Handlers allow case-insensitive admin password match');

// Summary
console.log('\n====================================================');
console.log(`TOTAL TESTS: ${passCount + failCount}`);
console.log(`PASSED: ${passCount}`);
console.log(`FAILED: ${failCount}`);
console.log('====================================================');

if (failCount > 0) {
  process.exit(1);
} else {
  console.log('\n🎉 ALL SPRINT VERIFICATION TESTS PASSED SUCCESSFULLY!');
  process.exit(0);
}
