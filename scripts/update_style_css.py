with open('public/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .envelope-3d-scene and envelope flaps
old_envelope_block = """/* 3D Floating Envelope Wrapper with Pan & Zoom In */
.envelope-3d-scene {
  position: relative;
  width: 100%;
  max-width: 440px;
  height: 290px;
  perspective: 1400px;
  transform-style: preserve-3d;
  animation: panZoomIn 2.2s cubic-bezier(0.2, 0.8, 0.2, 1) forwards, floatBob 5s infinite ease-in-out 2.2s;
}

@keyframes panZoomIn {
  0% {
    opacity: 0;
    transform: scale(0.75) translateY(50px) rotateX(15deg) rotateY(-12deg);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0) rotateX(6deg) rotateY(-4deg);
  }
}

@keyframes floatBob {
  0%, 100% {
    transform: scale(1) translateY(0) rotateX(6deg) rotateY(-4deg);
  }
  50% {
    transform: scale(1.02) translateY(-14px) rotateX(2deg) rotateY(2deg);
  }
}

.envelope-3d-card {
  position: relative;
  width: 100%;
  height: 100%;
  background: #FDF3F5;
  border-radius: 12px;
  box-shadow: var(--shadow-envelope);
  border: 1px solid rgba(200, 162, 83, 0.4);
  transform-style: preserve-3d;
}

/* Envelope Flaps */
.flap-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 0;
  border-bottom: 145px solid #F5E2E6;
  border-left: 220px solid transparent;
  border-right: 220px solid transparent;
  z-index: 4;
  filter: drop-shadow(0 -4px 6px rgba(61, 38, 42, 0.08));
}

.flap-left {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 0;
  border-left: 220px solid #EED4D8;
  border-top: 145px solid transparent;
  border-bottom: 145px solid transparent;
  z-index: 3;
}

.flap-right {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 0;
  border-right: 220px solid #EED4D8;
  border-top: 145px solid transparent;
  border-bottom: 145px solid transparent;
  z-index: 3;
}

/* 3D Top Flap */
.flap-top {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 0;
  border-top: 150px solid #FDF0F2;
  border-left: 220px solid transparent;
  border-right: 220px solid transparent;
  transform-origin: top center;
  transition: transform 1.2s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 6;
  filter: drop-shadow(0 6px 12px rgba(61, 38, 42, 0.15));
}

.envelope-3d-scene.open-animation .flap-top {
  transform: rotateX(180deg);
  z-index: 1;
}"""

new_envelope_block = """/* 3D Floating Envelope Wrapper with Pan & Zoom In (Pristine Geometry) */
.envelope-3d-scene {
  position: relative;
  width: 100%;
  max-width: 420px;
  height: 270px;
  perspective: 1400px;
  transform-style: preserve-3d;
  animation: panZoomIn 2.2s cubic-bezier(0.2, 0.8, 0.2, 1) forwards, floatBob 5s infinite ease-in-out 2.2s;
}

@keyframes panZoomIn {
  0% {
    opacity: 0;
    transform: scale(0.8) translateY(40px) rotateX(14deg) rotateY(-10deg);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0) rotateX(5deg) rotateY(-3deg);
  }
}

@keyframes floatBob {
  0%, 100% {
    transform: scale(1) translateY(0) rotateX(5deg) rotateY(-3deg);
  }
  50% {
    transform: scale(1.02) translateY(-10px) rotateX(2deg) rotateY(1deg);
  }
}

.envelope-3d-card {
  position: relative;
  width: 100%;
  height: 100%;
  background: #FAF2F4;
  border-radius: 14px;
  box-shadow: 0 30px 70px rgba(30, 18, 20, 0.45), 0 0 50px rgba(166, 124, 30, 0.25);
  border: 1.5px solid rgba(166, 124, 30, 0.35);
  transform-style: preserve-3d;
}

.envelope-back-wall {
  position: absolute;
  inset: 0;
  border-radius: 12px;
  background: linear-gradient(180deg, #F9EEF0 0%, #F5E2E6 100%);
  z-index: 1;
}

/* Envelope Flaps Meeting at Center (X=210px, Y=135px) */
.flap-left {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 0;
  height: 0;
  border-left: 210px solid #EAD4D8;
  border-top: 135px solid transparent;
  border-bottom: 135px solid transparent;
  z-index: 3;
}

.flap-right {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 0;
  height: 0;
  border-right: 210px solid #EAD4D8;
  border-top: 135px solid transparent;
  border-bottom: 135px solid transparent;
  z-index: 3;
}

.flap-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  width: 0;
  height: 0;
  border-bottom: 135px solid #F2DEE2;
  border-left: 210px solid transparent;
  border-right: 210px solid transparent;
  z-index: 4;
  filter: drop-shadow(0 -3px 6px rgba(61, 38, 42, 0.08));
}

/* 3D Top Flap */
.flap-top {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  width: 0;
  height: 0;
  border-top: 140px solid #FBF0F2;
  border-left: 210px solid transparent;
  border-right: 210px solid transparent;
  transform-origin: top center;
  transition: transform 1.2s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 6;
  filter: drop-shadow(0 6px 12px rgba(61, 38, 42, 0.15));
}

.envelope-3d-scene.open-animation .flap-top {
  transform: rotateX(180deg);
  z-index: 1;
}"""

if old_envelope_block in css:
    css = css.replace(old_envelope_block, new_envelope_block)
    print("Replaced envelope 3d block successfully.")
else:
    print("Warning: old_envelope_block not matched directly, checking partial replace...")

# 2. Update .seal-interaction-box, .flower-blooming-loader, .wax-seal-disc
old_seal_block = """.emerge-logo-img {
  width: 112px;
  height: 112px;
  object-fit: contain;
  margin-bottom: 4px;
  filter: drop-shadow(0 4px 10px rgba(138, 90, 18, 0.35));
}

/* Wax Seal Button & Flower-Based Hold Loader */
.seal-interaction-box {
  position: absolute;
  top: 105px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 15;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  user-select: none;
  -webkit-user-select: none;
  touch-action: none;
}

.flower-blooming-loader {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 174px;
  height: 174px;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 1;
}

.flower-petal-path {
  fill: rgba(184, 134, 11, 0.2);
  stroke: #A67C1E;
  stroke-width: 1.2;
  transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), fill 0.25s ease, stroke 0.25s ease, filter 0.25s ease;
  transform-origin: 0 0;
}

.petal-stamen {
  fill: #855306;
  transition: fill 0.2s ease, transform 0.2s ease;
}

.flower-petal-group.bloomed .flower-petal-path {
  fill: #FFB300;
  fill: url(#petal-bloom-grad);
  stroke: #FFE082;
  stroke-width: 1.8;
  filter: drop-shadow(0 0 6px rgba(255, 179, 0, 0.8));
  transform: scale(1.15);
}

.flower-petal-group.bloomed .petal-stamen {
  fill: #FFFDF9;
  transform: scale(1.3);
}

.flower-ring-track {
  fill: none;
  stroke: rgba(166, 124, 30, 0.25);
  stroke-width: 4;
}

.flower-ring-progress {
  fill: none;
  stroke: #ECC880;
  stroke: url(#vine-track-grad);
  stroke-width: 5;
  stroke-linecap: round;
  stroke-dasharray: 440;
  stroke-dashoffset: 440;
  transition: stroke-dashoffset 0.04s linear;
  filter: drop-shadow(0 0 6px rgba(255, 213, 79, 0.7));
  transform: rotate(-90deg);
  transform-origin: 90px 90px;
}

.wax-seal-disc {
  position: relative;
  width: 114px;
  height: 114px;
  border-radius: 50%;
  overflow: hidden;
  z-index: 2;
  box-shadow: 0 10px 28px rgba(138, 44, 48, 0.5), 0 0 16px rgba(166, 124, 30, 0.4);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.wax-seal-disc:hover {
  transform: scale(1.05);
  box-shadow: 0 0 25px rgba(236, 200, 128, 0.85), 0 12px 30px rgba(138, 44, 48, 0.6);
}

.wax-seal-disc.pressing {
  transform: scale(0.94);
  box-shadow: 0 4px 15px rgba(138, 44, 48, 0.7), 0 0 25px rgba(255, 179, 0, 0.85);
}

.wax-seal-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  clip-path: circle(49.2% at 50% 50%);
  display: block;
}

.flower-loader-status {
  margin-top: 32px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(26, 13, 17, 0.85);
  border: 1px solid rgba(236, 200, 128, 0.4);
  border-radius: 20px;
  padding: 6px 16px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 5;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.flower-status-icon {
  font-size: 1rem;
  animation: petalSpin 4s infinite linear;
}

@keyframes petalSpin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.flower-status-text {
  font-family: var(--font-base);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: #FFD54F;
  text-transform: uppercase;
}"""

new_seal_block = """/* Original Size 75px Monogram Crest on Emerge Card */
.emerge-logo-img {
  width: 75px;
  height: 75px;
  object-fit: contain;
  margin-bottom: 4px;
  filter: drop-shadow(0 3px 6px rgba(138, 90, 18, 0.3));
}

/* Wax Seal Button Centered Exactly on Flaps Intersection */
.seal-interaction-box {
  position: absolute;
  top: 135px;
  left: 210px;
  transform: translate(-50%, -50%);
  z-index: 10;
  cursor: pointer;
  width: 92px;
  height: 92px;
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
  -webkit-user-select: none;
  touch-action: none;
}

.flower-blooming-loader {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 136px;
  height: 136px;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 1;
}

.flower-petal-path {
  fill: rgba(184, 134, 11, 0.2);
  stroke: #A67C1E;
  stroke-width: 1.1;
  transition: transform 0.22s cubic-bezier(0.34, 1.56, 0.64, 1), fill 0.2s ease, stroke 0.2s ease;
  transform-origin: 0 0;
}

.petal-stamen {
  fill: #855306;
  transition: fill 0.2s ease, transform 0.2s ease;
}

.flower-petal-group.bloomed .flower-petal-path {
  fill: #FFB300;
  stroke: #FFE082;
  stroke-width: 1.6;
  filter: drop-shadow(0 0 5px rgba(255, 179, 0, 0.85));
  transform: scale(1.15);
}

.flower-petal-group.bloomed .petal-stamen {
  fill: #FFFDF9;
  transform: scale(1.25);
}

.flower-ring-track {
  fill: none;
  stroke: rgba(166, 124, 30, 0.25);
  stroke-width: 3.5;
}

.flower-ring-progress {
  fill: none;
  stroke: #ECC880;
  stroke-width: 4.5;
  stroke-linecap: round;
  stroke-dasharray: 314;
  stroke-dashoffset: 314;
  transition: stroke-dashoffset 0.04s linear;
  filter: drop-shadow(0 0 5px rgba(255, 213, 79, 0.8));
  transform: rotate(-90deg);
  transform-origin: 70px 70px;
}

.wax-seal-disc {
  position: relative;
  width: 92px;
  height: 92px;
  border-radius: 50%;
  overflow: hidden;
  z-index: 2;
  box-shadow: 0 8px 24px rgba(138, 44, 48, 0.45), 0 0 14px rgba(166, 124, 30, 0.35);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.wax-seal-disc:hover {
  transform: scale(1.05);
  box-shadow: 0 0 20px rgba(236, 200, 128, 0.85), 0 10px 26px rgba(138, 44, 48, 0.6);
}

.wax-seal-disc.pressing {
  transform: scale(0.94);
  box-shadow: 0 3px 12px rgba(138, 44, 48, 0.7), 0 0 20px rgba(255, 179, 0, 0.85);
}

.wax-seal-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  clip-path: circle(49% at 50% 50%);
  display: block;
}

.hint-progress-badge {
  display: inline-block;
  margin-top: 8px;
  background: rgba(26, 13, 17, 0.85);
  border: 1px solid rgba(236, 200, 128, 0.45);
  border-radius: 20px;
  padding: 5px 16px;
  font-family: var(--font-base);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: #FFD54F;
  text-transform: uppercase;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}"""

if old_seal_block in css:
    css = css.replace(old_seal_block, new_seal_block)
    print("Replaced seal block successfully.")
else:
    print("Warning: old_seal_block not matched directly.")

# 3. Update Nav Brand & Nav Logo: #pooshu 25% larger than original (1.7rem), logo original 44px
old_nav_block = """.nav-brand {
  display: flex;
  align-items: center;
  gap: 14px;
  font-family: var(--font-base);
  font-size: 2.1rem; /* 50% larger */
  font-weight: 900;
  letter-spacing: 5px;
  color: #633F17;
  text-transform: uppercase;
  cursor: pointer;
  flex-shrink: 0;
}

.nav-brand-logo {
  width: 66px; /* 50% larger */
  height: 66px;
  object-fit: contain;
  filter: drop-shadow(0 3px 8px rgba(138, 90, 18, 0.45));
  transition: transform 0.25s ease;
}"""

new_nav_block = """.nav-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-base);
  font-size: 1.7rem; /* Exactly 25% larger than original 1.35rem */
  font-weight: 800;
  letter-spacing: 3.5px;
  color: #785309;
  text-transform: uppercase;
  cursor: pointer;
  flex-shrink: 0;
}

.nav-brand-logo {
  width: 44px; /* Original size */
  height: 44px;
  object-fit: contain;
  filter: drop-shadow(0 2px 6px rgba(138, 90, 18, 0.35));
  transition: transform 0.25s ease;
}"""

if old_nav_block in css:
    css = css.replace(old_nav_block, new_nav_block)
    print("Replaced nav block successfully.")
else:
    print("Warning: old_nav_block not matched.")

# 4. Hero Crest Image: original 76px
old_crest_block = """.hero-crest-img {
  width: 115px; /* 50% larger */
  height: 115px;
  object-fit: contain;
  background: #FFFDFB;
  border-radius: 50%;
  padding: 6px;
  border: 2.5px solid var(--gold-foil-main);
  box-shadow: 0 6px 22px rgba(61, 38, 42, 0.22);
  transition: transform 0.3s ease;
}"""

new_crest_block = """.hero-crest-img {
  width: 76px; /* Original size */
  height: 76px;
  object-fit: contain;
  background: #FFFDFB;
  border-radius: 50%;
  padding: 4px;
  border: 2px solid var(--gold-foil-main);
  box-shadow: 0 4px 16px rgba(61, 38, 42, 0.18);
  transition: transform 0.3s ease;
}"""

if old_crest_block in css:
    css = css.replace(old_crest_block, new_crest_block)
    print("Replaced crest block successfully.")

# 5. Footer Logo & Hashtag: original 100px logo, hashtag 1.55rem (25% larger than original 1.25rem)
old_footer_block = """.footer-logo-img {
  width: 150px; /* 50% larger */
  height: 150px;
  object-fit: contain;
  margin: 0 auto 16px;
  display: block;
  filter: drop-shadow(0 6px 18px rgba(138, 90, 18, 0.4));
  transition: transform 0.3s ease;
}

.footer-logo-img:hover {
  transform: scale(1.06);
}

.footer-motif-center {
  width: 100%;
  max-width: 220px;
  margin: 0 auto 16px;
  display: block;
}

.footer-hashtag-brand {
  font-family: var(--font-base);
  font-size: 1.9rem; /* 50% larger */
  font-weight: 900;
  letter-spacing: 5px;
  color: #8A5A12;
  margin-bottom: 10px;
}"""

new_footer_block = """.footer-logo-img {
  width: 100px; /* Original size */
  height: 100px;
  object-fit: contain;
  margin: 0 auto 12px;
  display: block;
  filter: drop-shadow(0 4px 12px rgba(138, 90, 18, 0.3));
  transition: transform 0.3s ease;
}

.footer-logo-img:hover {
  transform: scale(1.05);
}

.footer-motif-center {
  width: 100%;
  max-width: 220px;
  margin: 0 auto 14px;
  display: block;
}

.footer-hashtag-brand {
  font-family: var(--font-base);
  font-size: 1.55rem; /* Exactly 25% larger than original 1.25rem */
  font-weight: 800;
  letter-spacing: 4px;
  color: #785309;
  margin-bottom: 8px;
}"""

if old_footer_block in css:
    css = css.replace(old_footer_block, new_footer_block)
    print("Replaced footer block successfully.")

# 6. Make ALL Section Wrappers transparent so background shows through paddings!
css = re.sub(
    r'\.hero-wrapper\s*\{[^}]*\}',
    '''.hero-wrapper {
  padding: 30px 0 45px;
  background: transparent;
  border-bottom: none;
}''',
    css
)

css = re.sub(
    r'\.scratch-section-wrap\s*\{[^}]*\}',
    '''.scratch-section-wrap {
  padding: 35px 0 45px;
  background: transparent;
}''',
    css
)

css = re.sub(
    r'\.story-section-wrap\s*\{[^}]*\}',
    '''.story-section-wrap {
  padding: 35px 0 45px;
  background: transparent;
}''',
    css
)

css = re.sub(
    r'\.events-section-wrap\s*\{[^}]*\}',
    '''.events-section-wrap {
  padding: 35px 0 45px;
  background: transparent;
}''',
    css
)

css = re.sub(
    r'\.rsvp-section-wrap\s*\{[^}]*\}',
    '''.rsvp-section-wrap {
  padding: 35px 0 50px;
  background: transparent;
  border-top: none;
}''',
    css
)

css = re.sub(
    r'\.subpage-view\s*\{[^}]*\}',
    '''.subpage-view {
  display: block;
  animation: fadeInSubpage 0.35s ease-out;
  padding: 30px 0 60px;
  background: transparent;
}''',
    css
)

with open('public/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated public/style.css successfully!')
