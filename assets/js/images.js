setTimeout(() => {
  document.querySelectorAll('.many-post img').forEach(e => {
    const src = e.getAttribute('src');
    if (src.match(/imgur/g)) {
      e.setAttribute('src', src.replace(/m?\.jpg/, 'm.jpg'));
    }
  })
});
