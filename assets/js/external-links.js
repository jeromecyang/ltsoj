setTimeout(() => {
  document.querySelectorAll('a[href]').forEach(e => {
    if (e.getAttribute('href').match(/^http/g)) {
      e.setAttribute('target', '_blank')
    }
  });
}, 2000);