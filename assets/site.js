/* ==========================================================================
   GermanyDreams - shared interaction layer
   Vanilla JS, no dependencies. Every behaviour degrades gracefully
   and is skipped entirely when the user prefers reduced motion.
   ========================================================================== */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------------------
     Scroll progress bar + back-to-top ring
     --------------------------------------------------------------------- */
  var bar = $('.scroll-progress');
  var toTop = $('.to-top');
  var ring = $('.to-top__ring circle');
  var ringLen = ring ? 2 * Math.PI * Number(ring.getAttribute('r')) : 0;

  if (ring) {
    ring.style.strokeDasharray = ringLen;
    ring.style.strokeDashoffset = ringLen;
  }

  function onScrollProgress() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var p = max > 0 ? Math.min(window.scrollY / max, 1) : 0;

    if (bar) bar.style.transform = 'scaleX(' + p + ')';
    if (ring) ring.style.strokeDashoffset = ringLen * (1 - p);
    if (toTop) toTop.classList.toggle('is-visible', window.scrollY > 600);
  }

  if (toTop) {
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
    });
  }

  /* ---------------------------------------------------------------------
     Nav: stuck state, mobile sheet, sliding pill, scroll-spy
     --------------------------------------------------------------------- */
  var nav = $('.nav');
  var burger = $('.nav__burger');
  var sheet = $('.nav__sheet');
  var pill = $('.nav__pill');
  var links = $$('.nav__links a');

  function onScrollNav() {
    if (nav) nav.classList.toggle('is-stuck', window.scrollY > 12);
  }

  if (burger && sheet) {
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      sheet.classList.toggle('is-open', !open);
    });
    // Close on link tap or Escape
    sheet.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        burger.setAttribute('aria-expanded', 'false');
        sheet.classList.remove('is-open');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && sheet.classList.contains('is-open')) {
        burger.setAttribute('aria-expanded', 'false');
        sheet.classList.remove('is-open');
        burger.focus();
      }
    });
  }

  function movePill(el) {
    if (!pill || !el) return;
    pill.style.width = el.offsetWidth + 'px';
    pill.style.transform = 'translateX(' + el.offsetLeft + 'px)';
    pill.style.opacity = '1';
  }

  links.forEach(function (a) {
    a.addEventListener('mouseenter', function () { movePill(a); });
  });

  if (pill) {
    var navLinksWrap = $('.nav__links');
    if (navLinksWrap) {
      navLinksWrap.addEventListener('mouseleave', function () {
        var active = $('.nav__links a.is-active');
        if (active) movePill(active); else pill.style.opacity = '0';
      });
    }
  }

  // Scroll-spy: highlight the section currently in view
  var spySections = $$('section[id], div[id].spy-target');
  function onScrollSpy() {
    if (!spySections.length || !links.length) return;
    var y = window.scrollY + window.innerHeight * 0.32;
    var current = '';
    spySections.forEach(function (s) {
      if (y >= s.offsetTop) current = s.id;
    });
    links.forEach(function (a) {
      a.classList.toggle('is-active', a.getAttribute('href') === '#' + current);
    });
    if (!$('.nav__links a:hover')) {
      var active = $('.nav__links a.is-active');
      if (active) movePill(active);
      else if (pill) pill.style.opacity = '0';
    }
  }

  /* ---------------------------------------------------------------------
     Throttled scroll handler
     --------------------------------------------------------------------- */
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      onScrollProgress();
      onScrollNav();
      onScrollSpy();
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });

  /* ---------------------------------------------------------------------
     Scroll reveal (staggered within each group)
     --------------------------------------------------------------------- */
  var reveals = $$('.reveal');
  // Give each element in a shared parent an increasing --i for stagger.
  var groups = new Map();
  reveals.forEach(function (el) {
    if (el.style.getPropertyValue('--i')) return;
    var p = el.parentElement;
    var n = groups.get(p) || 0;
    el.style.setProperty('--i', String(Math.min(n, 8)));
    groups.set(p, n + 1);
  });

  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------------------------------------------------------------------
     Count-up numbers  →  <span data-count="5200" data-suffix="+">
     --------------------------------------------------------------------- */
  function countUp(el) {
    var target = parseFloat(el.dataset.count);
    if (isNaN(target)) return;
    var suffix = el.dataset.suffix || '';
    var dur = 1500;
    var start = performance.now();

    function frame(now) {
      var t = Math.min((now - start) / dur, 1);
      var eased = 1 - Math.pow(1 - t, 3);
      var v = target * eased;
      el.textContent = (target >= 1000 ? Math.round(v).toLocaleString() : v.toFixed(target % 1 ? 1 : 0)) + suffix;
      if (t < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  var counters = $$('[data-count]');
  if (counters.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      counters.forEach(function (el) {
        var n = parseFloat(el.dataset.count);
        el.textContent = (n >= 1000 ? n.toLocaleString() : n) + (el.dataset.suffix || '');
      });
    } else {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { countUp(e.target); cio.unobserve(e.target); }
        });
      }, { threshold: 0.5 });
      counters.forEach(function (el) { cio.observe(el); });
    }
  }

  /* ---------------------------------------------------------------------
     Card spotlight - tracks the cursor via --mx / --my
     --------------------------------------------------------------------- */
  if (!reduce && window.matchMedia('(hover: hover)').matches) {
    $$('.spotlight').forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });

    /* -------------------------------------------------------------------
       3D tilt  →  add class "tilt", optional data-tilt="8" for max degrees
       ------------------------------------------------------------------- */
    $$('.tilt').forEach(function (el) {
      var max = Number(el.dataset.tilt || 8);
      var raf = null;

      el.addEventListener('pointermove', function (e) {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          var r = el.getBoundingClientRect();
          var px = (e.clientX - r.left) / r.width - .5;
          var py = (e.clientY - r.top) / r.height - .5;
          el.style.transform =
            'perspective(900px) rotateY(' + (px * max) + 'deg) rotateX(' + (-py * max) + 'deg) translateZ(0)';
          el.style.setProperty('--gx', ((px + .5) * 100) + '%');
          el.style.setProperty('--gy', ((py + .5) * 100) + '%');
          el.classList.add('is-tilting');
          raf = null;
        });
      });

      el.addEventListener('pointerleave', function () {
        el.style.transform = '';
        el.classList.remove('is-tilting');
      });
    });

    /* -------------------------------------------------------------------
       Magnetic buttons  →  wrap in .magnetic
       ------------------------------------------------------------------- */
    $$('.magnetic').forEach(function (wrap) {
      var child = wrap.firstElementChild;
      if (!child) return;

      wrap.addEventListener('pointermove', function (e) {
        var r = wrap.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2;
        var y = e.clientY - r.top - r.height / 2;
        child.style.transition = 'none';
        child.style.transform = 'translate(' + x * .25 + 'px,' + y * .35 + 'px)';
      });

      wrap.addEventListener('pointerleave', function () {
        child.style.transition = 'transform .5s cubic-bezier(.34,1.56,.64,1)';
        child.style.transform = '';
      });
    });
  }

  /* ---------------------------------------------------------------------
     Headline word reveal  →  <h1 data-words>Life in Germany</h1>
     --------------------------------------------------------------------- */
  $$('[data-words]').forEach(function (el) {
    if (reduce) return;
    var i = 0;
    // Walk only direct text nodes so nested spans (e.g. .grad-text) survive.
    Array.prototype.slice.call(el.childNodes).forEach(function (node) {
      if (node.nodeType === 3) {
        var frag = document.createDocumentFragment();
        node.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part.trim()) { frag.appendChild(document.createTextNode(part)); return; }
          var w = document.createElement('span');
          w.className = 'word';
          var inner = document.createElement('span');
          inner.textContent = part;
          w.appendChild(inner);
          w.style.setProperty('--w', String(i++));
          frag.appendChild(w);
        });
        el.replaceChild(frag, node);
      } else if (node.nodeType === 1 && node.tagName !== 'BR' && !node.classList.contains('word')) {
        var w2 = document.createElement('span');
        w2.className = 'word';
        w2.style.setProperty('--w', String(i++));
        node.parentNode.insertBefore(w2, node);
        w2.appendChild(node);
      }
    });
  });

  /* Kick everything off once at load. */
  onScrollProgress();
  onScrollNav();
  onScrollSpy();
})();
