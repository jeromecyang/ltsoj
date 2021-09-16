setTimeout(() => {
  document.querySelectorAll('a[href]').forEach(e => {
    if (e.getAttribute('href').match(/^http/g) && !e.getAttribute('href').match(/^ltsoj\.com/g)) {
      e.setAttribute('target', '_blank');
      e.setAttribute('rel', 'noopener');
    }
  });
}, 2000);