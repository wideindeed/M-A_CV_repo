/* ═══════════════════════════════════════════
   AFZAL M. HARISH — PORTFOLIO JS
   main_af.js
═══════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── CV DOWNLOAD HANDLER ── */
  const cvBtn = document.getElementById('cv-download');
  if (cvBtn) {
    cvBtn.addEventListener('click', function (e) {
      e.preventDefault();

      // Flash feedback
      const orig = cvBtn.innerHTML;
      cvBtn.innerHTML = '<span>✓ READY</span>';
      cvBtn.style.background = 'var(--cyan)';
      cvBtn.style.color = 'var(--bg)';

      setTimeout(() => {
        cvBtn.innerHTML = orig;
        cvBtn.style.background = '';
        cvBtn.style.color = '';
      }, 1800);

      // In production: replace with actual PDF path
      // window.open('afzal_harish_cv.pdf', '_blank');
      alert('CV download would trigger here in production.\nReplace with your actual PDF link in main_af.js.');
    });
  }

  /* ── ENTRY ANIMATION (class-based, no layout shift) ── */
  function revealOnLoad () {
    const items = document.querySelectorAll(
      '.exp-block, .project-block, .edu-block, .stack-category, .skills-strip__tags .tag'
    );

    items.forEach((el, i) => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(12px)';
      el.style.transition = `opacity 0.35s ease ${i * 30}ms, transform 0.35s ease ${i * 30}ms`;
    });

    // Trigger on next frame
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        items.forEach((el) => {
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        });
      });
    });
  }

  /* ── METRIC COUNTER ANIMATION ── */
  function animateMetrics () {
    const metrics = document.querySelectorAll('.metric__val');
    metrics.forEach(el => {
      const val = el.textContent.trim();
      const num = parseFloat(val);

      // Only animate numeric values
      if (!isNaN(num) && Number.isFinite(num)) {
        el.textContent = '0';
        let start = 0;
        const end = num;
        const duration = 900;
        const step = 16;
        const increment = (end / duration) * step;
        const isFloat = val.includes('.');

        const timer = setInterval(() => {
          start += increment;
          if (start >= end) {
            start = end;
            clearInterval(timer);
          }
          el.textContent = isFloat ? start.toFixed(2) : Math.floor(start);
        }, step);
      }
    });
  }

  /* ── STICKY BAR SCROLL INDICATOR ── */
  function initScrollIndicator () {
    const bar = document.querySelector('.sticky-bar');
    if (!bar) return;

    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          const scrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight);
          bar.style.setProperty('--scroll-pct', `${Math.min(scrolled * 100, 100)}%`);
          ticking = false;
        });
        ticking = true;
      }
    });

    // Inject scroll progress line into sticky bar
    const prog = document.createElement('div');
    prog.style.cssText = `
      position: absolute;
      bottom: 0; left: 0;
      height: 2px;
      width: var(--scroll-pct, 0%);
      background: var(--cyan);
      transition: width 0.1s linear;
      box-shadow: 0 0 8px var(--cyan);
    `;
    bar.style.position = 'fixed';
    bar.appendChild(prog);
  }

  /* ── COPY EMAIL ON CLICK ── */
  function initEmailCopy () {
    const links = document.querySelectorAll('a[href^="mailto:"]');
    links.forEach(link => {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        const email = this.href.replace('mailto:', '');
        if (navigator.clipboard) {
          navigator.clipboard.writeText(email).then(() => {
            const orig = link.textContent;
            link.textContent = 'COPIED!';
            setTimeout(() => { link.textContent = orig; }, 1500);
          }).catch(() => { window.location.href = link.href; });
        } else {
          window.location.href = link.href;
        }
      });
    });
  }

  /* ── TAG HOVER HIGHLIGHT ── */
  function initTagHover () {
    const tags = document.querySelectorAll('.tag');
    tags.forEach(tag => {
      tag.addEventListener('mouseenter', () => {
        tag.style.boxShadow = '0 0 10px rgba(0,240,255,0.4)';
      });
      tag.addEventListener('mouseleave', () => {
        tag.style.boxShadow = '';
      });
    });
  }

  /* ── INIT ── */
  document.addEventListener('DOMContentLoaded', () => {
    revealOnLoad();
    animateMetrics();
    initScrollIndicator();
    initEmailCopy();
    initTagHover();
  });

})();
