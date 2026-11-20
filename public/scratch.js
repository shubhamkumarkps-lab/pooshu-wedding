/**
 * #pooshu 3-Circle HTML5 Canvas Scratch Engine
 * Metallic Gold Foil texture, real-time cleared pixel calculation,
 * celebratory golden petal burst, and Web Audio chime integration.
 */

class ScratchCardEngine {
  constructor() {
    this.circles = [
      { id: 'scratch-month', canvas: null, ctx: null, cleared: false, percent: 0, text: 'DECEMBER' },
      { id: 'scratch-day', canvas: null, ctx: null, cleared: false, percent: 0, text: '02' },
      { id: 'scratch-year', canvas: null, ctx: null, cleared: false, percent: 0, text: '2026' }
    ];
    this.isDrawing = false;
    this.allRevealed = false;
    this.scratchThreshold = 55; // 55% cleared unlocks celebration
  }

  init() {
    this.scratchImg = new Image();
    this.scratchImg.src = 'assets/scratch_cover.png';
    this.scratchImg.onload = () => {
      this.circles.forEach(circle => {
        if (circle.canvas && !circle.cleared) {
          this.paintGoldFoil(circle);
        }
      });
    };

    this.circles.forEach(circle => {
      const canvas = document.getElementById(circle.id);
      if (!canvas) return;

      circle.canvas = canvas;
      circle.ctx = canvas.getContext('2d', { willReadFrequently: true });

      // Handle HiDPI displays
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = (rect.width || 96) * dpr;
      canvas.height = (rect.height || 96) * dpr;
      circle.ctx.scale(dpr, dpr);

      this.paintGoldFoil(circle);
      this.attachEvents(circle);
    });

    const helperBtn = document.getElementById('scratch-reveal-all-btn');
    if (helperBtn) {
      helperBtn.addEventListener('click', () => this.revealAll());
    }
  }

  // Paint realistic scratch cover using Scratch.png with gold luster rim
  paintGoldFoil(circle) {
    const ctx = circle.ctx;
    const w = circle.canvas.width / (window.devicePixelRatio || 1);
    const h = circle.canvas.height / (window.devicePixelRatio || 1);

    ctx.save();
    ctx.globalCompositeOperation = 'source-over';
    ctx.clearRect(0, 0, w, h);

    // Clip to circle so scratch texture is perfectly round
    ctx.beginPath();
    ctx.arc(w / 2, h / 2, w / 2, 0, Math.PI * 2);
    ctx.closePath();
    ctx.clip();

    if (this.scratchImg && this.scratchImg.complete && this.scratchImg.naturalWidth > 0) {
      ctx.drawImage(this.scratchImg, 0, 0, w, h);

      // Subtle metallic luster sheen overlay
      const sheen = ctx.createLinearGradient(0, 0, w, h);
      sheen.addColorStop(0, 'rgba(255, 255, 255, 0.25)');
      sheen.addColorStop(0.35, 'rgba(212, 175, 55, 0.15)');
      sheen.addColorStop(0.7, 'rgba(255, 255, 255, 0.3)');
      sheen.addColorStop(1, 'rgba(184, 134, 11, 0.2)');
      ctx.fillStyle = sheen;
      ctx.fillRect(0, 0, w, h);
    } else {
      // Fallback procedural metallic foil
      const grad = ctx.createLinearGradient(0, 0, w, h);
      grad.addColorStop(0, '#E6C275');
      grad.addColorStop(0.3, '#FFF3C2');
      grad.addColorStop(0.6, '#D4AF37');
      grad.addColorStop(1, '#99732B');
      ctx.fillStyle = grad;
      ctx.fill();
    }

    // Elegant gold border rim
    ctx.strokeStyle = 'rgba(212, 175, 55, 0.6)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(w / 2, h / 2, (w / 2) - 1, 0, Math.PI * 2);
    ctx.stroke();

    // Subtle "SCRATCH" label in gold foil
    ctx.fillStyle = 'rgba(61, 38, 42, 0.55)';
    ctx.font = 'bold 10px "Raleway", sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.shadowColor = 'rgba(255, 255, 255, 0.6)';
    ctx.shadowBlur = 4;
    ctx.fillText('SCRATCH', w / 2, h / 2);

    ctx.restore();
  }

  attachEvents(circle) {
    const canvas = circle.canvas;

    const startScratch = (e) => {
      this.isDrawing = true;
      if (window.pooshuAudio) {
        window.pooshuAudio.ensureAudioContext();
      }
      this.scratchAt(circle, e);
    };

    const moveScratch = (e) => {
      if (!this.isDrawing) return;
      this.scratchAt(circle, e);
    };

    const stopScratch = () => {
      if (this.isDrawing) {
        this.isDrawing = false;
        this.calculateProgress(circle);
      }
    };

    // Pointer Events
    canvas.addEventListener('pointerdown', startScratch);
    window.addEventListener('pointermove', moveScratch);
    window.addEventListener('pointerup', stopScratch);

    // Touch Fallback
    canvas.addEventListener('touchstart', (e) => {
      e.preventDefault();
      startScratch(e.touches[0]);
    }, { passive: false });

    window.addEventListener('touchmove', (e) => {
      if (this.isDrawing) {
        e.preventDefault();
        moveScratch(e.touches[0]);
      }
    }, { passive: false });

    window.addEventListener('touchend', stopScratch);
  }

  scratchAt(circle, e) {
    const rect = circle.canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const ctx = circle.ctx;
    ctx.save();
    ctx.globalCompositeOperation = 'destination-out';
    ctx.beginPath();
    ctx.arc(x, y, 16, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    // Occasional real-time progress check
    if (Math.random() < 0.2) {
      this.calculateProgress(circle);
    }
  }

  calculateProgress(circle) {
    if (circle.cleared) return;

    const ctx = circle.ctx;
    const canvas = circle.canvas;
    const w = canvas.width;
    const h = canvas.height;

    try {
      const imgData = ctx.getImageData(0, 0, w, h);
      const pixels = imgData.data;
      let transparentCount = 0;
      let totalSampled = 0;

      // Sub-sample every 16th pixel for high performance
      for (let i = 3; i < pixels.length; i += 16) {
        totalSampled++;
        if (pixels[i] < 40) {
          transparentCount++;
        }
      }

      const percent = Math.round((transparentCount / totalSampled) * 100);
      circle.percent = percent;

      if (percent >= this.scratchThreshold) {
        circle.cleared = true;
        this.fadeCircle(circle);
        this.checkAllRevealed();
      }
    } catch (err) {
      console.warn('Scratch progress check error:', err);
    }
  }

  fadeCircle(circle) {
    const ctx = circle.ctx;
    const canvas = circle.canvas;
    let alpha = 1.0;
    const fadeTimer = setInterval(() => {
      alpha -= 0.15;
      if (alpha <= 0) {
        clearInterval(fadeTimer);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      } else {
        ctx.save();
        ctx.globalCompositeOperation = 'destination-out';
        ctx.fillStyle = `rgba(0,0,0,0.2)`;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.restore();
      }
    }, 40);
  }

  checkAllRevealed() {
    const allCleared = this.circles.every(c => c.cleared);
    if (allCleared && !this.allRevealed) {
      this.allRevealed = true;
      this.onCelebration();
    }
  }

  revealAll() {
    this.circles.forEach(c => {
      c.cleared = true;
      this.fadeCircle(c);
    });
    this.allRevealed = true;
    this.onCelebration();
  }

  onCelebration() {
    // 1. Play celestial shimmer sound
    if (window.pooshuAudio) {
      window.pooshuAudio.playScratchShimmer();
    }

    // 2. Trigger golden petal and sparkle confetti
    this.launchGoldPetals();

    // 3. Show unlocked notice
    const banner = document.getElementById('scratch-unlocked-banner');
    if (banner) banner.style.display = 'block';

    const promptText = document.getElementById('scratch-progress-text');
    if (promptText) {
      promptText.textContent = '✨ 100% Unlocked • Save the Date: Dec 02, 2026 ✨';
      promptText.style.color = '#C72C35';
    }

    const helperBtn = document.getElementById('scratch-reveal-all-btn');
    if (helperBtn) helperBtn.style.display = 'none';
  }

  launchGoldPetals() {
    const canvas = document.getElementById('confetti-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const colors = ['#ECC880', '#D4AF37', '#F8BBD0', '#F48FB1', '#C72C35', '#FFFFFF'];

    for (let i = 0; i < 90; i++) {
      particles.push({
        x: canvas.width / 2 + (Math.random() * 200 - 100),
        y: canvas.height * 0.45 + (Math.random() * 100 - 50),
        vx: (Math.random() * 8 - 4),
        vy: (Math.random() * -10 - 4),
        size: Math.random() * 8 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        rotation: Math.random() * 360,
        vRot: (Math.random() * 6 - 3),
        opacity: 1,
        life: 0
      });
    }

    let frame = 0;
    const animate = () => {
      frame++;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      let alive = false;
      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.22; // gravity
        p.rotation += p.vRot;
        p.life++;

        if (p.life > 70) {
          p.opacity -= 0.02;
        }

        if (p.opacity > 0 && p.y < canvas.height + 20) {
          alive = true;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rotation * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.globalAlpha = Math.max(0, p.opacity);

          // Oval petal shape
          ctx.beginPath();
          ctx.ellipse(0, 0, p.size, p.size * 0.6, 0, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }
      });

      if (alive && frame < 200) {
        requestAnimationFrame(animate);
      } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    };

    requestAnimationFrame(animate);
  }
}

window.pooshuScratch = new ScratchCardEngine();
