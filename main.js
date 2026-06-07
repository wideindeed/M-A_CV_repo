// Active nav highlight on scroll — no animations, just state tracking
(function () {
  const items = document.querySelectorAll('.sidenav-item');
  const sections = document.querySelectorAll('.section[id]');

  if (!sections.length || !items.length) return;

  function setActive() {
    let current = '';
    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - 80) current = sec.id;
    });
    items.forEach(item => {
      item.style.color = '';
      item.style.borderLeftColor = '';
      item.style.background = '';
      if (item.getAttribute('href') === '#' + current) {
        item.style.color = 'var(--text)';
        item.style.borderLeftColor = 'var(--accent)';
        item.style.background = 'var(--bg-overlay)';
      }
    });
  }

  window.addEventListener('scroll', setActive, { passive: true });
  setActive();
})();
