(function() {
  const STORAGE_KEY = 'ts-theme';
  function getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }
  function getStoredTheme() {
    try { return localStorage.getItem(STORAGE_KEY); } catch(e) { return null; }
  }
  function setTheme(theme) {
    const root = document.documentElement;
    if (theme === 'light') root.setAttribute('data-theme', 'light');
    else root.removeAttribute('data-theme');
    try { localStorage.setItem(STORAGE_KEY, theme); } catch(e) {}
    updateToggleLabel(theme);
  }
  function getCurrentTheme() {
    return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  }
  function updateToggleLabel(theme) {
    const btn = document.querySelector('[data-theme-toggle]');
    if (!btn) return;
    btn.setAttribute('aria-label', theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode');
    btn.innerHTML = theme === 'light'
      ? '<span class="icon" aria-hidden="true">🌙</span><span>Dark</span>'
      : '<span class="icon" aria-hidden="true">☀️</span><span>Light</span>';
  }
  function initTheme() {
    const stored = getStoredTheme();
    setTheme(stored || getSystemTheme());
    document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
      btn.addEventListener('click', () => {
        setTheme(getCurrentTheme() === 'light' ? 'dark' : 'light');
      });
    });
    try {
      window.addEventListener('storage', e => {
        if (e.key === STORAGE_KEY) setTheme(e.newValue || getSystemTheme());
      });
    } catch(e) {}
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
  } else {
    initTheme();
  }
})();
