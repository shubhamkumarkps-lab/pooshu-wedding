/**
 * #pooshu Delicate Flower Particle Physics Engine
 * Releases realistic, fluttering, delicate Indian wedding petals
 * EXACTLY at the cursor/touch location (1:1 coordinate precision).
 */

(function () {
  'use strict';

  class FlowerParticleEngine {
    constructor() {
      this.canvas = null;
      this.ctx = null;
      this.particles = [];
      this.animId = null;
      this.width = window.innerWidth;
      this.height = window.innerHeight;
      this.lastSpawn = 0;

      // Authentic Indian Wedding Palette: Kopou Orchid, Marigold, Lotus & Jasmine
      this.flowerTypes = [
        // 1. Assamese Kopou Phool (Orchid Pink)
        { color1: '#F48FB1', color2: '#D81B60', vein: '#FFFFFF' },
        // 2. Marigold / Genda (Warm Gold)
        { color1: '#FFD54F', color2: '#FF8F00', vein: '#FFE082' },
        // 3. Marigold (Saffron Orange)
        { color1: '#FF9800', color2: '#E65100', vein: '#FFCC80' },
        // 4. Sacred Lotus (Rose Crimson)
        { color1: '#F06292', color2: '#C2185B', vein: '#F8BBD0' },
        // 5. Fragrant Mogra / Jasmine (Ivory Cream)
        { color1: '#FFFDF9', color2: '#F5E6CC', vein: '#B8860B' },
        // 6. Gold Celebration Spark
        { color1: '#FFF8E1', color2: '#B8860B', vein: '#9E7422' }
      ];

      this.init();
    }

    init() {
      let cvs = document.getElementById('flower-particles-canvas');
      if (!cvs) {
        cvs = document.createElement('canvas');
        cvs.id = 'flower-particles-canvas';
        document.body.appendChild(cvs);
      }
      this.canvas = cvs;
      this.ctx = cvs.getContext('2d');

      // Style canvas fixed over viewport
      this.canvas.style.position = 'fixed';
      this.canvas.style.top = '0';
      this.canvas.style.left = '0';
      this.canvas.style.width = '100vw';
      this.canvas.style.height = '100vh';
      this.canvas.style.pointerEvents = 'none';
      this.canvas.style.zIndex = '999999';

      this.resize();
      window.addEventListener('resize', () => this.resize());

      // Global click & tap listener
      window.addEventListener('pointerdown', (e) => this.handlePointer(e), { passive: true });
    }

    resize() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
      // Use 1:1 pixel coordinates to match clientX/clientY exactly
      this.canvas.width = this.width;
      this.canvas.height = this.height;
    }

    handlePointer(e) {
      const now = performance.now();
      if (now - this.lastSpawn < 25) return;
      this.lastSpawn = now;

      // Ensure exact click location
      const x = e.clientX;
      const y = e.clientY;
      this.spawnBurst(x, y, 10);
    }

    spawnBurst(x, y, count = 10) {
      for (let i = 0; i < count; i++) {
        const type = this.flowerTypes[Math.floor(Math.random() * this.flowerTypes.length)];
        const angle = Math.random() * Math.PI * 2;
        const speed = 1.2 + Math.random() * 3.4;
        // Realistic, fluttery petal size (+50% enlarged: 6.6px to 12.3px)
        const size = 6.6 + Math.random() * 5.7;

        this.particles.push({
          x: x + (Math.random() - 0.5) * 4,
          y: y + (Math.random() - 0.5) * 4,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - 1.2, // gentle upward impulse
          rotation: Math.random() * Math.PI * 2,
          vRot: (Math.random() - 0.5) * 0.12,
          wobble: Math.random() * Math.PI * 2,
          vWobble: 0.05 + Math.random() * 0.06,
          size: size,
          scale: 0.65 + Math.random() * 0.45,
          alpha: 1.0,
          decay: 0.014 + Math.random() * 0.010,
          gravity: 0.10 + Math.random() * 0.06,
          drag: 0.965,
          type: type
        });
      }

      if (!this.animId) {
        this.loop();
      }
    }

    startShower() {
      if (this.showerInterval) return;
      this.isShowering = true;

      // Spawn drifting petals from the top of the viewport
      this.showerInterval = setInterval(() => {
        if (!this.isShowering) {
          clearInterval(this.showerInterval);
          this.showerInterval = null;
          return;
        }

        const count = 3;
        for (let i = 0; i < count; i++) {
          const type = this.flowerTypes[Math.floor(Math.random() * this.flowerTypes.length)];
          const size = 7.0 + Math.random() * 6.0; // 50% larger
          this.particles.push({
            x: Math.random() * this.width,
            y: -20,
            vx: (Math.random() - 0.5) * 1.5,
            vy: 0.8 + Math.random() * 1.6, // gentle drifting fall
            rotation: Math.random() * Math.PI * 2,
            vRot: (Math.random() - 0.5) * 0.08,
            wobble: Math.random() * Math.PI * 2,
            vWobble: 0.04 + Math.random() * 0.05,
            size: size,
            scale: 0.7 + Math.random() * 0.5,
            alpha: 1.0,
            decay: 0.005 + Math.random() * 0.004, // longer lasting flutter
            gravity: 0.02 + Math.random() * 0.02,
            drag: 0.99,
            type: type
          });
        }

        if (!this.animId) {
          this.loop();
        }
      }, 140);

      // Stop shower when user scrolls down
      const onUserScroll = () => {
        if (window.scrollY > 40) {
          this.stopShower();
          window.removeEventListener('scroll', onUserScroll);
        }
      };
      window.addEventListener('scroll', onUserScroll, { passive: true });
    }

    stopShower() {
      this.isShowering = false;
      if (this.showerInterval) {
        clearInterval(this.showerInterval);
        this.showerInterval = null;
      }
    }

    loop() {
      this.ctx.clearRect(0, 0, this.width, this.height);

      for (let i = this.particles.length - 1; i >= 0; i--) {
        const p = this.particles[i];

        // Physics
        p.vx *= p.drag;
        p.vy *= p.drag;
        p.vy += p.gravity;
        p.x += p.vx + Math.sin(p.wobble) * 0.6;
        p.y += p.vy;
        p.wobble += p.vWobble;
        p.rotation += p.vRot;

        p.alpha -= p.decay;

        if (p.alpha <= 0 || p.y > this.height + 20) {
          this.particles.splice(i, 1);
          continue;
        }

        // Draw delicate petal
        this.drawPetal(p);
      }

      if (this.particles.length > 0) {
        this.animId = requestAnimationFrame(() => this.loop());
      } else {
        this.animId = null;
      }
    }

    drawPetal(p) {
      const ctx = this.ctx;
      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate(p.rotation);
      ctx.scale(p.scale, p.scale * (0.8 + Math.sin(p.wobble) * 0.2));
      ctx.globalAlpha = Math.max(0, p.alpha);

      const r = p.size;
      const grad = ctx.createRadialGradient(0, -r * 0.3, 0.5, 0, 0, r);
      grad.addColorStop(0, p.type.color1);
      grad.addColorStop(1, p.type.color2);

      ctx.fillStyle = grad;
      ctx.strokeStyle = p.type.vein;
      ctx.lineWidth = 0.5;

      // Dainty petal shape
      ctx.beginPath();
      ctx.moveTo(0, -r);
      ctx.bezierCurveTo(r * 0.6, -r * 0.6, r * 0.7, r * 0.4, 0, r * 0.85);
      ctx.bezierCurveTo(-r * 0.7, r * 0.4, -r * 0.6, -r * 0.6, 0, -r);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      ctx.restore();
    }
  }

  window.addEventListener('DOMContentLoaded', () => {
    window.pooshuFlowerEngine = new FlowerParticleEngine();
    window.releaseFlowerBurst = function (x, y, count) {
      if (window.pooshuFlowerEngine) {
        window.pooshuFlowerEngine.spawnBurst(x, y, count || 12);
      }
    };
    window.startPetalShower = function () {
      if (window.pooshuFlowerEngine) {
        window.pooshuFlowerEngine.startShower();
      }
    };
    window.stopPetalShower = function () {
      if (window.pooshuFlowerEngine) {
        window.pooshuFlowerEngine.stopShower();
      }
    };
  });
})();
