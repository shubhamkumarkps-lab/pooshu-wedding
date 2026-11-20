content = '''/**
 * #pooshu Interactive Wedding Web Application v3.0
 * Responsive Full Webpage & Phone Architecture
 * Flower-Based Hold-to-Open Wax Seal with Radial Petal Bloom
 * Trilingual Navigation: The Wedding, Know the Bride, Know the Groom, Our Story, Events, RSVP
 * Interactive Flower Click Particle Engine
 */

class PooshuApp {
  constructor() {
    this.currentLang = 'en';
    this.currentPage = 'home';
    this.i18nData = {};
    this.storyIndex = 0;
    this.activeEventFilter = 'all';
    this.weddingDate = new Date('2026-12-02T20:00:00+05:30'); // Dec 2, 2026, 8 PM IST
    this.countdownInterval = null;

    // Hold-to-open state
    this.holdTimer = null;
    this.isOpened = false;
    this.isHolding = false;

    this.init();
  }

  async init() {
    await this.loadTranslations();
    this.setupNavigation();
    this.setupLanguageSwitcher();
    this.setup3DEnvelopeHoldToOpen();
    this.setupStoryCarousel();
    this.setupStoryThumbnails();
    this.setupEventFilters();
    this.setupRsvpForm();
    this.startCountdown();

    if (window.pooshuScratch) {
      window.pooshuScratch.init();
    }

    // Handle initial URL hash
    const initialHash = (window.location.hash || '').replace('#', '').toLowerCase();
    if (['bride', 'groom', 'home'].includes(initialHash)) {
      this.navigateToPage(initialHash, false);
    }

    window.addEventListener('hashchange', () => {
      const hash = (window.location.hash || '').replace('#', '').toLowerCase();
      if (['bride', 'groom', 'home'].includes(hash) && hash !== this.currentPage) {
        this.navigateToPage(hash, false);
      }
    });

    this.renderLanguage(this.currentLang);
  }

  /* ----------------------------------------------------
   * 1. Subpage Navigation (The Wedding, Bride, Groom)
   * ---------------------------------------------------- */
  setupNavigation() {
    document.querySelectorAll('.nav-link-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const targetNav = btn.getAttribute('data-nav');
        if (targetNav) {
          e.preventDefault();
          this.navigateToPage(targetNav);
        }
      });
    });
  }

  navigateToPage(pageId, updateHash = true) {
    if (!['home', 'bride', 'groom'].includes(pageId)) pageId = 'home';
    this.currentPage = pageId;

    const pageHome = document.getElementById('page-home');
    const pageBride = document.getElementById('page-bride');
    const pageGroom = document.getElementById('page-groom');

    if (pageHome) pageHome.classList.toggle('hidden', pageId !== 'home');
    if (pageBride) pageBride.classList.toggle('hidden', pageId !== 'bride');
    if (pageGroom) pageGroom.classList.toggle('hidden', pageId !== 'groom');

    // Update active state in nav menu
    document.querySelectorAll('.nav-link-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-nav') === pageId);
    });

    if (updateHash) {
      window.location.hash = pageId;
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  /* ----------------------------------------------------
   * 2. Translations & i18n Engine
   * ---------------------------------------------------- */
  async loadTranslations() {
    try {
      const [enRes, asRes, maiRes] = await Promise.all([
        fetch('data/en.json'),
        fetch('data/as.json'),
        fetch('data/mai.json')
      ]);

      this.i18nData.en = await enRes.json();
      this.i18nData.as = await asRes.json();
      this.i18nData.mai = await maiRes.json();
    } catch (e) {
      console.error('Failed to load translations:', e);
    }
  }

  setupLanguageSwitcher() {
    const langButtons = document.querySelectorAll('.lang-btn');
    langButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        const targetLang = e.currentTarget.getAttribute('data-lang');
        if (targetLang && targetLang !== this.currentLang) {
          this.switchLanguage(targetLang);
        }
      });
    });
  }

  switchLanguage(lang) {
    if (!this.i18nData[lang]) return;
    this.currentLang = lang;

    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    if (window.pooshuAudio) {
      window.pooshuAudio.syncWithLanguage(lang);
    }

    this.renderLanguage(lang);
  }

  renderLanguage(lang) {
    const t = this.i18nData[lang];
    if (!t) return;

    // Welcome Screen
    this.setText('env-instruction', t.envelope.instruction);
    this.setText('flower-status-text', t.envelope.instruction);

    // Hero Section
    this.setText('hero-invocation', t.hero.invocation);
    this.setText('hero-bride-name', t.hero.bride);
    this.setText('hero-groom-name', t.hero.groom);
    this.setText('hero-tagline', t.hero.tagline);
    this.setText('hero-bride-line', t.hero.brideLine);
    this.setText('hero-groom-line', t.hero.groomLine);
    this.setText('hero-invitation-text', t.hero.invitationText);

    // Countdown Header & Units
    this.setText('countdown-title', t.countdown.title);
    this.setText('unit-days', t.countdown.days);
    this.setText('unit-hours', t.countdown.hours);
    this.setText('unit-mins', t.countdown.mins);
    this.setText('unit-secs', t.countdown.secs);

    // Scratch Section
    this.setText('scratch-heading', t.scratch.heading);
    this.setText('scratch-subheading', t.scratch.subheading);
    this.setText('scratch-reveal-all-btn', t.scratch.revealAllBtn);
    this.setText('scratch-unlocked-banner', t.scratch.unlockedNotice);

    // Story Section
    this.setText('story-sec-title', t.story.sectionTitle);
    this.setText('story-sec-sub', t.story.sectionSubtitle);
    this.renderCurrentStoryCard();

    // Events Section
    this.setText('events-sec-title', t.events.sectionTitle);
    this.setText('events-sec-sub', t.events.sectionSubtitle);
    this.setText('filter-btn-all', t.events.filterAll);
    this.setText('filter-btn-bride', t.events.filterBride);
    this.setText('filter-btn-groom', t.events.filterGroom);
    this.renderEventsList();

    // RSVP Section
    this.setText('rsvp-sec-title', t.rsvp.sectionTitle);
    this.setText('rsvp-sec-sub', t.rsvp.sectionSubtitle);
    this.setText('lbl-fullname', t.rsvp.fullName);
    this.setPlaceholder('input-fullname', t.rsvp.fullNamePlaceholder);
    this.setText('lbl-side', t.rsvp.sideLabel);
    this.setText('opt-side-bride', t.rsvp.sideBride);
    this.setText('opt-side-groom', t.rsvp.sideGroom);
    this.setText('opt-side-mutual', t.rsvp.sideMutual);
    this.setText('lbl-attending', t.rsvp.attendingLabel);
    this.setText('opt-attending-yes', t.rsvp.attendingYes);
    this.setText('opt-attending-no', t.rsvp.attendingNo);
    this.setText('lbl-guest-count', t.rsvp.guestCount);
    this.setText('lbl-dietary', t.rsvp.dietary);
    this.setText('opt-diet-veg', t.rsvp.dietaryVeg);
    this.setText('opt-diet-nonveg', t.rsvp.dietaryNonVeg);
    this.setText('opt-diet-jain', t.rsvp.dietaryJain);
    this.setText('lbl-djsong', t.rsvp.djSong);
    this.setPlaceholder('input-djsong', t.rsvp.djSongPlaceholder);
    this.setText('btn-rsvp-submit', t.rsvp.submitBtn);

    // Subpage: Know the Bride
    if (t.bridePage) {
      this.setText('bride-page-badge', t.bridePage.badge);
      this.setText('bride-page-title', t.bridePage.title);
      this.setText('bride-page-subtitle', t.bridePage.subtitle);
      this.setText('bride-page-motto', t.bridePage.motto);
      this.setText('bride-heritage-title', t.bridePage.heritageTitle);
      this.setText('bride-heritage-text', t.bridePage.heritageText);
      this.setText('bride-story-title', t.bridePage.storyTitle);
      this.setText('bride-story-text', t.bridePage.storyText);
      this.setText('bride-facts-title', t.bridePage.factsTitle);
      this.setText('bride-family-title', t.bridePage.familyTitle);
      this.setText('bride-family-text', t.bridePage.familyText);
      this.setText('bride-blessing-text', t.bridePage.blessing);
    }

    // Subpage: Know the Groom
    if (t.groomPage) {
      this.setText('groom-page-badge', t.groomPage.badge);
      this.setText('groom-page-title', t.groomPage.title);
      this.setText('groom-page-subtitle', t.groomPage.subtitle);
      this.setText('groom-page-motto', t.groomPage.motto);
      this.setText('groom-heritage-title', t.groomPage.heritageTitle);
      this.setText('groom-heritage-text', t.groomPage.heritageText);
      this.setText('groom-story-title', t.groomPage.storyTitle);
      this.setText('groom-story-text', t.groomPage.storyText);
      this.setText('groom-facts-title', t.groomPage.factsTitle);
      this.setText('groom-family-title', t.groomPage.familyTitle);
      this.setText('groom-family-text', t.groomPage.familyText);
      this.setText('groom-blessing-text', t.groomPage.blessing);
    }

    // Footer
    this.setText('footer-blessing', t.footer.blessings);
    this.setText('footer-credits', t.footer.withLove);
  }

  setText(id, text) {
    const el = document.getElementById(id);
    if (el && text) el.textContent = text;
  }

  setPlaceholder(id, text) {
    const el = document.getElementById(id);
    if (el && text) el.setAttribute('placeholder', text);
  }

  /* ----------------------------------------------------
   * 3. 3D Floating Envelope with Flower-Based Hold-To-Open
   * ---------------------------------------------------- */
  setup3DEnvelopeHoldToOpen() {
    const sealBtn = document.getElementById('wax-seal-btn');
    const sealDisc = document.getElementById('wax-seal-disc');
    const progressTrack = document.getElementById('seal-flower-progress');
    const statusText = document.getElementById('flower-status-text');
    const petals = document.querySelectorAll('.flower-petal-group');
    const scene = document.getElementById('envelope-scene');
    const overlay = document.getElementById('welcome-overlay');

    if (!sealBtn || !scene || !overlay) return;

    const circumference = 440; // 2 * PI * 70
    const holdDuration = 650; // ms for satisfying hold feeling

    const triggerOpen = () => {
      if (this.isOpened) return;
      this.isOpened = true;
      this.isHolding = false;
      clearInterval(this.holdTimer);

      // Light up all petals fully
      petals.forEach(p => p.classList.add('bloomed'));
      if (progressTrack) progressTrack.style.strokeDashoffset = '0';
      if (statusText) statusText.textContent = (this.i18nData[this.currentLang]?.envelope?.unveiled || 'Unveiled!');

      // Release a grand burst of wedding flowers from the seal button!
      const rect = sealBtn.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      if (window.releaseFlowerBurst) {
        window.releaseFlowerBurst(centerX, centerY, 30);
      }

      // Play wax fracture SFX
      if (window.pooshuAudio) {
        window.pooshuAudio.playSealBreak();
      }

      // 3D Flap Opening & Layered Cards Emerging Animation
      scene.classList.add('open-animation');

      // Start background wedding music
      setTimeout(() => {
        if (window.pooshuAudio) {
          window.pooshuAudio.togglePlay();
        }
      }, 600);

      // Smoothly unveil the main website
      setTimeout(() => {
        overlay.classList.add('opened');
      }, 1600);
    };

    const startHolding = (e) => {
      if (this.isOpened) return;
      if (e) {
        // Prevent unwanted gesture scrolling/zooming on mobile touch
        if (e.cancelable) e.preventDefault();
      }

      this.isHolding = true;
      if (sealDisc) sealDisc.classList.add('pressing');
      if (window.pooshuAudio) window.pooshuAudio.ensureAudioContext();

      const startTime = Date.now();
      clearInterval(this.holdTimer);

      const bloomingLabel = this.i18nData[this.currentLang]?.envelope?.blooming || 'Blooming...';

      this.holdTimer = setInterval(() => {
        if (!this.isHolding) {
          clearInterval(this.holdTimer);
          return;
        }

        const elapsed = Date.now() - startTime;
        const progress = Math.min(1, elapsed / holdDuration);

        // Update progress circular ring
        if (progressTrack) {
          const offset = circumference - (progress * circumference);
          progressTrack.style.strokeDashoffset = offset;
        }

        // Incrementally bloom the 12 petals around the ring
        const bloomedCount = Math.floor(progress * 12);
        petals.forEach((p, idx) => {
          if (idx <= bloomedCount) {
            p.classList.add('bloomed');
          } else {
            p.classList.remove('bloomed');
          }
        });

        // Update micro-status text with percentage
        if (statusText) {
          const pct = Math.min(100, Math.round(progress * 100));
          statusText.textContent = `${bloomingLabel} ${pct}%`;
        }

        if (progress >= 1) {
          clearInterval(this.holdTimer);
          triggerOpen();
        }
      }, 16);
    };

    const stopHolding = () => {
      if (this.isOpened) return;
      this.isHolding = false;
      clearInterval(this.holdTimer);

      if (sealDisc) sealDisc.classList.remove('pressing');
      if (progressTrack) progressTrack.style.strokeDashoffset = circumference;
      petals.forEach(p => p.classList.remove('bloomed'));

      const defaultText = this.i18nData[this.currentLang]?.envelope?.instruction || 'Press & Hold to Unveil';
      if (statusText) statusText.textContent = defaultText;
    };

    // Cross-platform pointer & touch bindings
    sealBtn.addEventListener('pointerdown', startHolding);
    sealBtn.addEventListener('touchstart', startHolding, { passive: false });
    sealBtn.addEventListener('mousedown', startHolding);

    window.addEventListener('pointerup', stopHolding);
    window.addEventListener('pointercancel', stopHolding);
    window.addEventListener('touchend', stopHolding);
    window.addEventListener('touchcancel', stopHolding);
    window.addEventListener('mouseup', stopHolding);

    // Fallback click handler so no user gets stuck if holding was interrupted
    sealBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (!this.isOpened) {
        triggerOpen();
      }
    });
  }

  /* ----------------------------------------------------
   * 4. Live Heartbeat Countdown Timer
   * ---------------------------------------------------- */
  startCountdown() {
    const update = () => {
      const now = new Date().getTime();
      const diff = this.weddingDate.getTime() - now;

      if (diff <= 0) {
        this.setText('count-days', '00');
        this.setText('count-hours', '00');
        this.setText('count-mins', '00');
        this.setText('count-secs', '00');
        clearInterval(this.countdownInterval);
        return;
      }

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const secs = Math.floor((diff % (1000 * 60)) / 1000);

      this.setText('count-days', String(days).padStart(2, '0'));
      this.setText('count-hours', String(hours).padStart(2, '0'));
      this.setText('count-mins', String(mins).padStart(2, '0'));
      this.setText('count-secs', String(secs).padStart(2, '0'));
    };

    update();
    this.countdownInterval = setInterval(update, 1000);
  }

  /* ----------------------------------------------------
   * 5. 12-Year Love Story Interactive Timeline (11 Chapters)
   * ---------------------------------------------------- */
  setupStoryCarousel() {
    const prevBtn = document.getElementById('story-prev-btn');
    const nextBtn = document.getElementById('story-next-btn');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        this.storyIndex = (this.storyIndex - 1 + 11) % 11;
        this.renderCurrentStoryCard();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        this.storyIndex = (this.storyIndex + 1) % 11;
        this.renderCurrentStoryCard();
      });
    }
  }

  setupStoryThumbnails() {
    const container = document.getElementById('story-thumbnails-container');
    if (!container) return;

    container.innerHTML = '';
    for (let i = 0; i < 11; i++) {
      const thumb = document.createElement('div');
      thumb.className = `story-thumb-pill ${i === this.storyIndex ? 'active' : ''}`;
      thumb.setAttribute('data-index', i);

      const yearNum = 2014 + i + (i >= 2 ? 0 : 0);
      const years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2024', '2026'];
      thumb.innerHTML = `<span class="thumb-pill-year">${years[i] || '2026'}</span>`;

      thumb.addEventListener('click', () => {
        this.storyIndex = i;
        this.renderCurrentStoryCard();
      });

      container.appendChild(thumb);
    }
  }

  renderCurrentStoryCard() {
    const t = this.i18nData[this.currentLang];
    if (!t || !t.story || !t.story.chapters) return;

    const chapter = t.story.chapters[this.storyIndex];
    if (!chapter) return;

    this.setText('story-card-year', chapter.year);
    this.setText('story-step-indicator', `${this.storyIndex + 1} / 11`);
    this.setText('story-card-title', chapter.title);
    this.setText('story-card-sub', chapter.subtitle);
    this.setText('story-card-desc', chapter.desc);

    const img = document.getElementById('story-card-img');
    if (img && chapter.image) {
      img.src = chapter.image;
    }

    // Update dots track
    const dotsContainer = document.getElementById('story-dots-container');
    if (dotsContainer) {
      dotsContainer.innerHTML = '';
      for (let i = 0; i < 11; i++) {
        const dot = document.createElement('span');
        dot.className = `story-track-dot ${i === this.storyIndex ? 'active' : ''}`;
        dot.addEventListener('click', () => {
          this.storyIndex = i;
          this.renderCurrentStoryCard();
        });
        dotsContainer.appendChild(dot);
      }
    }

    // Highlight thumbnail
    document.querySelectorAll('.story-thumb-pill').forEach((pill, idx) => {
      pill.classList.toggle('active', idx === this.storyIndex);
    });
  }

  /* ----------------------------------------------------
   * 6. Ceremonial Event Itinerary & Side Filter
   * ---------------------------------------------------- */
  setupEventFilters() {
    const filterButtons = document.querySelectorAll('.filter-tab-pill');
    filterButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        filterButtons.forEach(b => b.classList.remove('active'));
        e.currentTarget.classList.add('active');
        this.activeEventFilter = e.currentTarget.getAttribute('data-filter') || 'all';
        this.renderEventsList();
      });
    });
  }

  renderEventsList() {
    const t = this.i18nData[this.currentLang];
    if (!t || !t.events || !t.events.items) return;

    const container = document.getElementById('events-grid-container');
    if (!container) return;

    container.innerHTML = '';

    const filtered = t.events.items.filter(ev => {
      if (this.activeEventFilter === 'all') return true;
      if (this.activeEventFilter === 'bride') return ev.side === 'bride' || ev.side === 'both';
      if (this.activeEventFilter === 'groom') return ev.side === 'groom' || ev.side === 'both';
      return true;
    });

    filtered.forEach(ev => {
      const card = document.createElement('div');
      card.className = 'event-card';

      const swatches = (ev.colors || []).map(c => `<span class="swatch-circle" style="background-color: ${c};" title="${c}"></span>`).join('');

      card.innerHTML = `
        <div class="event-card-header">
          <span class="event-side-badge side-${ev.side}">${ev.sideLabel || ev.side.toUpperCase()}</span>
          <h3 class="event-title-text">${ev.title}</h3>
          <div class="event-datetime-badge">
            <span>📅 ${ev.date}</span>
            <span>⏰ ${ev.time}</span>
          </div>
        </div>

        <div class="event-venue-block">
          <div class="venue-location-name">📍 ${ev.venue}</div>
          <div class="venue-address-sub">${ev.address}</div>
        </div>

        <div class="event-dresscode-box">
          <div class="dresscode-title">👗 ${ev.dressCodeTitle}</div>
          <div class="dresscode-palette-swatches">
            ${swatches}
            <span class="dresscode-palette-names">${ev.colorNames || ''}</span>
          </div>
        </div>

        <div class="event-buttons-bar">
          <a href="${ev.mapUrl}" target="_blank" rel="noopener noreferrer" class="btn-card-action btn-map-link">
            <span>🗺️</span> View Google Map
          </a>
          <button type="button" class="btn-card-action btn-cal-link" onclick="window.pooshuApp.downloadIcs('${ev.id}')">
            <span>📅</span> Add to Calendar
          </button>
        </div>
      `;

      container.appendChild(card);
    });
  }

  downloadIcs(eventId) {
    const t = this.i18nData[this.currentLang];
    if (!t || !t.events) return;
    const ev = t.events.items.find(e => e.id === eventId);
    if (!ev) return;

    const icsContent = `BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//PooShu Wedding 2026//EN
CALSCALE:GREGORIAN
BEGIN:VEVENT
SUMMARY:#pooshu Wedding: ${ev.title}
DESCRIPTION:Celebrating Pooja Haloi & Shubham Kumar Thakur. ${ev.venue}, ${ev.address}
LOCATION:${ev.venue}, ${ev.address}
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR`;

    const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `pooshu_${eventId}.ics`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  /* ----------------------------------------------------
   * 7. RSVP Form (Centered, Celebratory Flower Burst)
   * ---------------------------------------------------- */
  setupRsvpForm() {
    const form = document.getElementById('wedding-rsvp-form');
    if (!form) return;

    const pills = document.querySelectorAll('.attending-pill');
    pills.forEach(pill => {
      pill.addEventListener('click', (e) => {
        pills.forEach(p => p.classList.remove('selected'));
        e.currentTarget.classList.add('selected');
        const input = document.getElementById('rsvp-attending-val');
        if (input) input.value = e.currentTarget.getAttribute('data-value');
      });
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      this.handleRsvpSubmit();
    });
  }

  handleRsvpSubmit() {
    const name = document.getElementById('input-fullname')?.value || 'Honored Guest';
    const side = document.getElementById('select-side')?.value || 'mutual';
    const attending = document.getElementById('rsvp-attending-val')?.value || 'yes';
    const guestCount = document.getElementById('input-guest-count')?.value || '1';
    const dietary = document.getElementById('select-dietary')?.value || 'veg';
    const djSong = document.getElementById('input-djsong')?.value || '';

    // Play ceremonial confirm chime
    if (window.pooshuAudio) {
      window.pooshuAudio.playRsvpConfirm();
    }

    // Release multiple bursts of celebration wedding flowers!
    if (window.releaseFlowerBurst) {
      window.releaseFlowerBurst(window.innerWidth / 2, window.innerHeight * 0.45, 35);
      setTimeout(() => {
        window.releaseFlowerBurst(window.innerWidth * 0.35, window.innerHeight * 0.55, 25);
        window.releaseFlowerBurst(window.innerWidth * 0.65, window.innerHeight * 0.55, 25);
      }, 250);
    }

    // Show celebration banner
    const banner = document.getElementById('rsvp-success-banner');
    const form = document.getElementById('wedding-rsvp-form');
    const msg = document.getElementById('rsvp-success-message');

    if (banner) banner.classList.remove('hidden');
    if (form) form.classList.add('hidden');
    if (msg) {
      msg.textContent = `Honored ${name}, your RSVP (${attending === 'yes' ? 'Joyfully Attending' : 'Regretfully Declining'} with ${guestCount} guest(s)) has been registered with love. We eagerly await celebrating #pooshu with you!`;
    }

    // Post to local server API
    fetch('/api/rsvp', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, side, attending, guestCount, dietary, djSong, timestamp: new Date().toISOString() })
    }).catch(e => console.log('RSVP stored locally:', e));
  }
}

window.addEventListener('DOMContentLoaded', () => {
  window.pooshuApp = new PooshuApp();
});
'''

with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated public/app.js successfully!')
