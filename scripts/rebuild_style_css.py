with open('public/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace :root gold variables with reduced darkness (radiant warm champagne gold)
old_root = """  --gold-foil-light: #F7DF94;
  --gold-foil-main: #A67C1E; /* Rich Antique Gold */
  --gold-foil-dark: #785309;
  --gold-foil-deep: #4E3504;
  --rose-gold: #B36858;
  
  --ceremonial-red: #C72C35;
  --deep-plum: #3D262A;
  --muted-mulberry: #6E4750;
  --slate-subtle: #59616D;
  
  /* Gradients */
  --grad-gold-foil: linear-gradient(135deg, #B8860B 0%, #855306 40%, #B8860B 70%, #683F04 100%);"""

new_root = """  --gold-foil-light: #FBF2D5;
  --gold-foil-main: #C49C35; /* Radiant Champagne & Antique Wedding Gold */
  --gold-foil-dark: #997322; /* Warm readable gold, no dark muddy brown */
  --gold-foil-deep: #785309;
  --rose-gold: #C58B7B;
  
  --ceremonial-red: #C72C35;
  --deep-plum: #3D262A;
  --muted-mulberry: #6E4750;
  --slate-subtle: #59616D;
  
  /* Gradients (Luminous, warm, elegant gold) */
  --grad-gold-foil: linear-gradient(135deg, #ECC880 0%, #D4AF37 35%, #F5DE8C 65%, #B8860B 100%);"""

if old_root in css:
    css = css.replace(old_root, new_root)
    print("Replaced root gold variables successfully.")

# Replace Envelope 3D section with Real Physical Envelope Image styling
old_envelope_section = """/* 3D Floating Envelope Wrapper with Pan & Zoom In (Pristine Geometry) */
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

new_envelope_section = """/* Authentic Physical Embossed Wedding Envelope Display */
.envelope-3d-scene {
  position: relative;
  width: 100%;
  max-width: 480px;
  height: 360px;
  perspective: 1200px;
  transform-style: preserve-3d;
  animation: panZoomIn 2s cubic-bezier(0.2, 0.8, 0.2, 1) forwards, floatBob 5s infinite ease-in-out 2s;
}

@media (max-width: 520px) {
  .envelope-3d-scene {
    max-width: 330px;
    height: 247px;
  }
}

@keyframes panZoomIn {
  0% {
    opacity: 0;
    transform: scale(0.82) translateY(35px) rotateX(10deg);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0) rotateX(4deg);
  }
}

@keyframes floatBob {
  0%, 100% {
    transform: scale(1) translateY(0) rotateX(4deg);
  }
  50% {
    transform: scale(1.015) translateY(-8px) rotateX(2deg);
  }
}

.envelope-3d-card {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 10px;
  box-shadow: 0 25px 60px rgba(25, 12, 16, 0.4), 0 0 35px rgba(196, 156, 53, 0.2);
  transform-style: preserve-3d;
}

.envelope-real-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
  display: block;
  pointer-events: none;
  z-index: 4;
  position: relative;
  transition: transform 1.2s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.8s ease;
}

.envelope-3d-scene.open-animation .envelope-real-img {
  transform: translateY(24px) scale(0.97);
  opacity: 0.85;
}

/* Layered Cards Stack Nesting Inside Envelope */
.floating-cards-stack {
  position: absolute;
  top: 18px;
  left: 18px;
  right: 18px;
  height: 250px;
  z-index: 2;
  transform-style: preserve-3d;
}

@media (max-width: 520px) {
  .floating-cards-stack {
    top: 12px;
    left: 12px;
    right: 12px;
    height: 180px;
  }
}

/* When envelope opens: Cards smoothly slide up in 3D staggered layers! */
.envelope-3d-scene.open-animation .card-layer-1 {
  transform: translateY(-145px) rotateZ(-2.5deg) scale(1.04);
  z-index: 6;
}

.envelope-3d-scene.open-animation .card-layer-2 {
  transform: translateY(-90px) rotateZ(2.5deg) scale(1.01);
  z-index: 5;
}

.envelope-3d-scene.open-animation .card-layer-3 {
  transform: translateY(-35px) scale(0.98);
  z-index: 4;
}"""

if old_envelope_section in css:
    css = css.replace(old_envelope_section, new_envelope_section)
    print("Replaced envelope section with physical envelope styling.")

# Update seal interaction box to position right on the embossed flap medallion (top: 48%, left: 50%)
old_seal_box = """.seal-interaction-box {
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
}"""

new_seal_box = """.seal-interaction-box {
  position: absolute;
  top: 48%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  cursor: pointer;
  width: 86px;
  height: 86px;
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
  -webkit-user-select: none;
  touch-action: none;
}

@media (max-width: 520px) {
  .seal-interaction-box {
    width: 72px;
    height: 72px;
  }
}"""

if old_seal_box in css:
    css = css.replace(old_seal_box, new_seal_box)
    print("Replaced seal interaction box position successfully.")

# Update Navigation Bar CSS for Single-Bar, Non-Wrapping layout
old_nav_css = """.top-nav-bar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 253, 250, 0.94);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 2px solid rgba(166, 124, 30, 0.35);
  box-shadow: 0 4px 20px rgba(61, 38, 42, 0.08);
}

.top-nav-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  gap: 16px;
}

/* 50% Enlarged #POOSHU & Crest */
.nav-brand {
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
}

.nav-brand:hover .nav-brand-logo {
  transform: scale(1.08) rotate(3deg);
}

.nav-brand span {
  background: linear-gradient(135deg, #B8860B 0%, #855306 40%, #B8860B 70%, #683F04 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 1px 2px rgba(85, 59, 11, 0.4));
}

/* Navigation Menu Links */
.nav-menu-links {
  display: none;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

@media (min-width: 960px) {
  .nav-menu-links {
    display: flex;
  }
}

.nav-link-btn {
  background: none;
  border: 1px solid transparent;
  font-family: var(--font-base);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.8px;
  color: var(--deep-plum);
  text-decoration: none;
  padding: 7px 14px;
  border-radius: 18px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.nav-link-btn:hover, .nav-link-btn.active {
  background: #FFF8E1;
  color: #8A5A12;
  border-color: rgba(166, 124, 30, 0.35);
  box-shadow: 0 2px 8px rgba(166, 124, 30, 0.15);
}"""

new_nav_css = """.top-nav-bar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 253, 250, 0.96);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1.5px solid rgba(196, 156, 53, 0.3);
  box-shadow: 0 2px 14px rgba(61, 38, 42, 0.05);
}

.top-nav-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  gap: 10px;
  flex-wrap: nowrap; /* Never wrap */
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-base);
  font-size: 1.38rem;
  font-weight: 800;
  letter-spacing: 2.5px;
  color: var(--gold-foil-dark);
  text-transform: uppercase;
  cursor: pointer;
  flex-shrink: 0;
}

.nav-brand-logo {
  width: 36px;
  height: 36px;
  object-fit: contain;
  filter: drop-shadow(0 2px 4px rgba(166, 124, 30, 0.25));
  transition: transform 0.25s ease;
}

.nav-brand:hover .nav-brand-logo {
  transform: scale(1.06);
}

.nav-brand span {
  background: linear-gradient(135deg, #D4AF37 0%, #C49C35 50%, #997322 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Nav Menu Links - Sleek Single Bar */
.nav-menu-links {
  display: flex;
  align-items: center;
  gap: 4px;
  flex-shrink: 1;
  overflow-x: auto;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}

.nav-menu-links::-webkit-scrollbar {
  display: none;
}

.nav-link-btn {
  background: none;
  border: 1px solid transparent;
  font-family: var(--font-base);
  font-size: 0.76rem;
  font-weight: 600;
  letter-spacing: 0.3px;
  color: var(--deep-plum);
  text-decoration: none;
  padding: 5px 9px;
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.nav-link-btn:hover {
  background: rgba(251, 240, 242, 0.7);
  color: var(--ceremonial-red);
}

.nav-link-btn.active {
  background: #FFF9E6;
  color: #997322;
  border-color: rgba(196, 156, 53, 0.4);
  font-weight: 700;
  box-shadow: 0 2px 6px rgba(196, 156, 53, 0.15);
}"""

if old_nav_css in css:
    css = css.replace(old_nav_css, new_nav_css)
    print("Replaced nav css with sleek single bar layout.")

# Add subpage-peer-group style
if '.subpage-peer-group' not in css:
    css += """\n.subpage-peer-group {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.btn-cta-story {
  background: #EFF5F2;
  color: #2E5B4B;
  border: 1.5px solid #C8DDD3;
}
.btn-cta-story:hover {
  background: #2E5B4B;
  color: #FFF;
  transform: translateY(-2px);
}
"""

with open('public/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated public/style.css successfully!')
