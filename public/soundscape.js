/**
 * #pooshu Soundscape & Audio Engine
 * Combines Web Audio API synthesized SFX (offline guaranteed)
 * with the Dual-Track Indian Wedding Soundtrack (Maithili & Assamese)
 */

class SoundscapeEngine {
  constructor() {
    this.ctx = null;
    this.ambientGain = null;
    this.isPlayingAmbient = false;
    this.currentTrack = 'as'; // Default song is Assamese ("Indradhanu") as requested
    this.isMuted = false;
    this.isPlayingMusic = false;
    this.autoPlayOnReady = false;
    this.ytPlayer = null;
    this.ytReady = false;

    // Track definitions
    this.tracks = {
      mai: {
        id: 'hCe23Bu28aY',
        title: 'Maithili Vivah Geet',
        artist: 'Traditional Maithili Special',
        culture: 'Traditional Maithili Wedding Song',
        langLabel: 'मैथिली गीत',
        startSeconds: 0
      },
      as: {
        id: '5GUBedDU_JI',
        title: 'Indradhanu',
        artist: 'Assamese Special',
        culture: 'Soulful Assamese Romantic Ballad',
        langLabel: 'অসমীয়া গান',
        startSeconds: 15 // Trimmed 15 seconds (10s + 5s more) from the beginning as requested
      }
    };

    this.initWebAudio();
    this.initYouTubeAPI();
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => this.initUIEvents());
    } else {
      this.initUIEvents();
    }
  }

  initUIEvents() {
    const playBtn = document.getElementById('music-toggle-btn');
    if (playBtn) {
      playBtn.onclick = (e) => {
        if (e) e.stopPropagation();
        this.togglePlay();
      };
    }

    const expandBtn = document.getElementById('music-expand-btn');
    const controller = document.getElementById('floating-audio-controller');
    if (expandBtn && controller) {
      expandBtn.onclick = (e) => {
        if (e) e.stopPropagation();
        controller.classList.toggle('minimized');
        const isMin = controller.classList.contains('minimized');
        expandBtn.setAttribute('title', isMin ? 'Expand Music Player' : 'Minimize Music Player');
        const iconSpan = expandBtn.querySelector('.expand-icon');
        if (iconSpan) iconSpan.textContent = isMin ? '▶' : '◀';
      };
    }
  }

  // Initialize Web Audio Context on first user gesture
  initWebAudio() {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) {
      this.ctx = new AudioContext();
    }
  }

  ensureAudioContext() {
    if (!this.ctx) {
      this.initWebAudio();
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  /* ----------------------------------------------------
   * Ceremonial SFX Sprites (Web Audio API Synthesized)
   * ---------------------------------------------------- */

  // SFX 1: Wax Seal Crack & Paper Rustle (< 300 ms)
  playSealBreak() {
    this.ensureAudioContext();
    if (!this.ctx) return;

    const t = this.ctx.currentTime;
    
    // 1. Snapping crack impulse (filtered noise)
    const bufferSize = this.ctx.sampleRate * 0.15;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (this.ctx.sampleRate * 0.025));
    }

    const noise = this.ctx.createBufferSource();
    noise.buffer = buffer;

    const filter = this.ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(1400, t);
    filter.Q.setValueAtTime(3.5, t);

    const gain = this.ctx.createGain();
    gain.gain.setValueAtTime(0.65, t);
    gain.gain.exponentialRampToValueAtTime(0.001, t + 0.15);

    noise.connect(filter);
    filter.connect(gain);
    gain.connect(this.ctx.destination);
    noise.start(t);

    // 2. Subtle low thump resonance of wax fracture
    const osc = this.ctx.createOscillator();
    const oscGain = this.ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(120, t);
    osc.frequency.exponentialRampToValueAtTime(30, t + 0.18);

    oscGain.gain.setValueAtTime(0.4, t);
    oscGain.gain.exponentialRampToValueAtTime(0.001, t + 0.18);

    osc.connect(oscGain);
    oscGain.connect(this.ctx.destination);
    osc.start(t);
    osc.stop(t + 0.2);
  }

  // SFX 2: Scratch Shimmer Chime (< 800 ms)
  // Sparkle arpeggio chord (E6, G#6, B6, E7) when scratching
  playScratchShimmer() {
    this.ensureAudioContext();
    if (!this.ctx) return;

    const t = this.ctx.currentTime;
    const frequencies = [1318.51, 1661.22, 1975.53, 2637.02]; // E6, G#6, B6, E7 celestial chime

    frequencies.forEach((freq, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, t + idx * 0.06);

      gain.gain.setValueAtTime(0, t + idx * 0.06);
      gain.gain.linearRampToValueAtTime(0.2, t + idx * 0.06 + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.0001, t + idx * 0.06 + 0.55);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(t + idx * 0.06);
      osc.stop(t + idx * 0.06 + 0.6);
    });
  }

  // SFX 3: RSVP Ceremonial Confirmation Chime & Conch Flourish
  playRsvpConfirm() {
    this.ensureAudioContext();
    if (!this.ctx) return;

    const t = this.ctx.currentTime;

    // Harmonious Indian wedding temple chime (Sa, Re, Ga, Pa, Dha chords)
    const notes = [523.25, 659.25, 783.99, 1046.50, 1318.51];
    notes.forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, t + i * 0.08);

      gain.gain.setValueAtTime(0, t + i * 0.08);
      gain.gain.linearRampToValueAtTime(0.28, t + i * 0.08 + 0.04);
      gain.gain.exponentialRampToValueAtTime(0.0001, t + i * 0.08 + 1.2);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(t + i * 0.08);
      osc.stop(t + i * 0.08 + 1.3);
    });

    // Deep auspicious bell undertone
    const bell = this.ctx.createOscillator();
    const bellGain = this.ctx.createGain();
    bell.type = 'sine';
    bell.frequency.setValueAtTime(220, t);
    bellGain.gain.setValueAtTime(0.35, t);
    bellGain.gain.exponentialRampToValueAtTime(0.0001, t + 1.8);

    bell.connect(bellGain);
    bellGain.connect(this.ctx.destination);
    bell.start(t);
    bell.stop(t + 1.9);
  }

  /* ----------------------------------------------------
   * Ambient Indian Flute & Tanpura Drone (Fallback & Background)
   * ---------------------------------------------------- */
  startAmbientRaga() {
    this.ensureAudioContext();
    if (!this.ctx || this.isPlayingAmbient) return;

    this.isPlayingAmbient = true;
    const t = this.ctx.currentTime;

    // Master ambient gain
    this.ambientGain = this.ctx.createGain();
    this.ambientGain.gain.setValueAtTime(0.001, t);
    this.ambientGain.gain.linearRampToValueAtTime(0.18, t + 2.0); // Gentle fade in
    this.ambientGain.connect(this.ctx.destination);

    // Tanpura Drone 1: Tonic C# (138.59 Hz)
    this.drone1 = this.ctx.createOscillator();
    this.drone1.type = 'triangle';
    this.drone1.frequency.setValueAtTime(138.59, t);
    this.drone1.connect(this.ambientGain);
    this.drone1.start(t);

    // Tanpura Drone 2: Fifth G# (207.65 Hz)
    this.drone2 = this.ctx.createOscillator();
    this.drone2.type = 'sine';
    this.drone2.frequency.setValueAtTime(207.65, t);
    this.drone2.connect(this.ambientGain);
    this.drone2.start(t);

    // Periodic gentle flute note in Raga Yaman
    this.fluteInterval = setInterval(() => {
      if (!this.isPlayingAmbient || !this.ctx) return;
      const ragaNotes = [277.18, 311.13, 349.23, 415.30, 466.16, 554.37];
      const note = ragaNotes[Math.floor(Math.random() * ragaNotes.length)];
      const now = this.ctx.currentTime;

      const fOsc = this.ctx.createOscillator();
      const fGain = this.ctx.createGain();
      fOsc.type = 'sine';
      fOsc.frequency.setValueAtTime(note, now);

      fGain.gain.setValueAtTime(0, now);
      fGain.gain.linearRampToValueAtTime(0.08, now + 0.3);
      fGain.gain.exponentialRampToValueAtTime(0.0001, now + 2.2);

      fOsc.connect(fGain);
      fGain.connect(this.ambientGain);

      fOsc.start(now);
      fOsc.stop(now + 2.3);
    }, 3200);
  }

  stopAmbientRaga() {
    if (!this.isPlayingAmbient) return;
    this.isPlayingAmbient = false;
    clearInterval(this.fluteInterval);
    if (this.ambientGain && this.ctx) {
      const t = this.ctx.currentTime;
      this.ambientGain.gain.linearRampToValueAtTime(0.001, t + 0.5);
      setTimeout(() => {
        try {
          if (this.drone1) this.drone1.stop();
          if (this.drone2) this.drone2.stop();
        } catch(e) {}
      }, 600);
    }
  }

  /* ----------------------------------------------------
   * YouTube IFrame API Dual-Song Engine
   * ---------------------------------------------------- */
  initYouTubeAPI() {
    window.onYouTubeIframeAPIReady = () => {
      this.ytReady = true;
      this.setupPlayer();
    };

    // Load YouTube API script if not already on page
    if (!document.getElementById('yt-iframe-script')) {
      const tag = document.createElement('script');
      tag.id = 'yt-iframe-script';
      tag.src = 'https://www.youtube.com/iframe_api';
      const firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    }
  }

  setupPlayer() {
    const activeTrack = this.tracks[this.currentTrack];
    const activeVideoId = activeTrack.id;
    const startSec = activeTrack.startSeconds || 0;
    try {
      this.ytPlayer = new window.YT.Player('yt-audio-container', {
        height: '1',
        width: '1',
        videoId: activeVideoId,
        playerVars: {
          autoplay: 0,
          controls: 0,
          disablekb: 1,
          fs: 0,
          modestbranding: 1,
          playsinline: 1,
          rel: 0,
          loop: 1,
          start: startSec,
          playlist: activeVideoId
        },
        events: {
          onReady: () => {
            console.log('YouTube Audio Player is ready.');
            if (this.autoPlayOnReady) {
              const activeTrack = this.tracks[this.currentTrack];
              const startSec = activeTrack.startSeconds || 0;
              if (this.ytPlayer && typeof this.ytPlayer.loadVideoById === 'function') {
                this.ytPlayer.loadVideoById({
                  videoId: activeTrack.id,
                  startSeconds: startSec,
                  suggestedQuality: 'small'
                });
              }
              if (startSec > 0 && this.ytPlayer && typeof this.ytPlayer.seekTo === 'function') {
                this.ytPlayer.seekTo(startSec, true);
              }
              if (this.ytPlayer && typeof this.ytPlayer.playVideo === 'function') {
                this.ytPlayer.playVideo();
                this.isPlayingMusic = true;
                this.updateUI();
              }
            } else if (startSec > 0 && this.ytPlayer && typeof this.ytPlayer.seekTo === 'function') {
              this.ytPlayer.seekTo(startSec, true);
            }
          },
          onStateChange: (event) => {
            if (event.data === window.YT.PlayerState.PLAYING) {
              this.isPlayingMusic = true;
              const activeTrackObj = this.tracks[this.currentTrack];
              const minStart = (activeTrackObj && activeTrackObj.startSeconds) ? activeTrackObj.startSeconds : 0;
              if (minStart > 0 && typeof this.ytPlayer.getCurrentTime === 'function') {
                const cur = this.ytPlayer.getCurrentTime();
                if (cur < minStart - 0.5) {
                  this.ytPlayer.seekTo(minStart, true);
                }
              }
              this.updateUI();
            } else if (event.data === window.YT.PlayerState.PAUSED) {
              this.isPlayingMusic = false;
              this.updateUI();
            } else if (event.data === window.YT.PlayerState.ENDED) {
              const currentTrackObj = this.tracks[this.currentTrack];
              const restartSec = (currentTrackObj && currentTrackObj.startSeconds) ? currentTrackObj.startSeconds : 0;
              if (this.ytPlayer && typeof this.ytPlayer.seekTo === 'function') {
                this.ytPlayer.seekTo(restartSec, true);
                this.ytPlayer.playVideo();
              }
            }
          },
          onError: () => {
            console.warn('YouTube embed restricted; transitioning to ceremonial Web Audio raga fallback.');
            this.startAmbientRaga();
          }
        }
      });
    } catch (e) {
      console.warn('YouTube player initialization notice:', e);
      this.startAmbientRaga();
    }
  }

  togglePlay() {
    this.ensureAudioContext();

    if (this.ytPlayer && typeof this.ytPlayer.getPlayerState === 'function') {
      try {
        const state = this.ytPlayer.getPlayerState();
        if (state === window.YT.PlayerState.PLAYING) {
          this.ytPlayer.pauseVideo();
          this.isPlayingMusic = false;
        } else {
          const track = this.tracks[this.currentTrack];
          if (track && track.startSeconds > 0 && typeof this.ytPlayer.getCurrentTime === 'function') {
            const curTime = this.ytPlayer.getCurrentTime();
            if (curTime < track.startSeconds) {
              this.ytPlayer.seekTo(track.startSeconds, true);
            }
          }
          this.ytPlayer.playVideo();
          this.isPlayingMusic = true;
          this.stopAmbientRaga();
        }
      } catch (err) {
        this.toggleAmbientFallback();
      }
    } else {
      this.toggleAmbientFallback();
    }
    this.updateUI();
  }

  toggleAmbientFallback() {
    if (this.isPlayingAmbient) {
      this.stopAmbientRaga();
      this.isPlayingMusic = false;
    } else {
      this.startAmbientRaga();
      this.isPlayingMusic = true;
    }
  }

  // Start default song (Assamese "Indradhanu") when user enters the main website
  startDefaultTrack() {
    this.ensureAudioContext();
    this.currentTrack = 'as';
    this.autoPlayOnReady = true;

    if (this.ytPlayer && typeof this.ytPlayer.playVideo === 'function') {
      const track = this.tracks['as'];
      const startSec = track.startSeconds || 15;
      try {
        if (typeof this.ytPlayer.loadVideoById === 'function') {
          this.ytPlayer.loadVideoById({
            videoId: track.id,
            startSeconds: startSec,
            suggestedQuality: 'small'
          });
        }
        if (startSec > 0 && typeof this.ytPlayer.seekTo === 'function') {
          this.ytPlayer.seekTo(startSec, true);
        }
        this.ytPlayer.playVideo();
        this.isPlayingMusic = true;
        this.stopAmbientRaga();
      } catch (e) {
        console.warn('startDefaultTrack error:', e);
      }
    }
    this.updateUI();
  }

  switchTrack(trackKey) {
    if (!this.tracks[trackKey]) return;
    this.ensureAudioContext();
    this.currentTrack = trackKey;
    this.autoPlayOnReady = true;
    const targetVideo = this.tracks[trackKey];
    const startSec = targetVideo.startSeconds || 0;

    if (this.ytPlayer && typeof this.ytPlayer.loadVideoById === 'function') {
      try {
        this.ytPlayer.loadVideoById({
          videoId: targetVideo.id,
          startSeconds: startSec,
          suggestedQuality: 'small'
        });
        if (startSec > 0) {
          setTimeout(() => {
            try { this.ytPlayer.seekTo(startSec, true); } catch(e) {}
          }, 200);
        }
        this.ytPlayer.playVideo();
        this.isPlayingMusic = true;
        this.stopAmbientRaga();
      } catch (e) {
        console.warn('Switching track error:', e);
      }
    } else if (this.ytPlayer && typeof this.ytPlayer.cueVideoById === 'function') {
      try {
        this.ytPlayer.cueVideoById({
          videoId: targetVideo.id,
          startSeconds: startSec,
          suggestedQuality: 'small'
        });
        this.ytPlayer.playVideo();
        this.isPlayingMusic = true;
        this.stopAmbientRaga();
      } catch (e) {
        console.warn('Switching track error:', e);
      }
    }
    this.updateUI();
  }

  // Hooked to language switcher: if lang is 'mai', switch to Maithili song; if 'as', switch to Assamese song
  syncWithLanguage(lang) {
    if (lang === 'mai') {
      this.switchTrack('mai');
    } else if (lang === 'as') {
      this.switchTrack('as');
    }
    // If 'en', keep current track undisturbed
  }

  updateUI() {
    const playBtn = document.getElementById('music-toggle-btn');
    const trackTitle = document.getElementById('music-track-title');
    const trackArtist = document.getElementById('music-track-artist');
    const eqBars = document.querySelectorAll('.eq-bar');
    const maiBtn = document.getElementById('track-mai-btn');
    const asBtn = document.getElementById('track-as-btn');

    const track = this.tracks[this.currentTrack];
    if (trackTitle) trackTitle.textContent = track.title;
    if (trackArtist) trackArtist.textContent = track.artist;

    if (playBtn) {
      playBtn.innerHTML = this.isPlayingMusic ? '⏸' : '▶';
      playBtn.setAttribute('aria-label', this.isPlayingMusic ? 'Pause Music' : 'Play Music');
    }

    if (maiBtn && asBtn) {
      if (this.currentTrack === 'mai') {
        maiBtn.classList.add('active');
        asBtn.classList.remove('active');
      } else {
        asBtn.classList.add('active');
        maiBtn.classList.remove('active');
      }
    }

    eqBars.forEach((bar) => {
      if (this.isPlayingMusic) {
        bar.classList.add('animating');
      } else {
        bar.classList.remove('animating');
      }
    });
  }
}

// Global instance attached to window
window.pooshuAudio = new SoundscapeEngine();
