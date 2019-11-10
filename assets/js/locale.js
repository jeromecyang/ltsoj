const LOCALE_ITEM_KEY = 'ltsoj-locale';

const locales = [
  { value: 'zh-tw', label: '繁體中文', pathname: '/' },
  { value: 'en-us', label: 'English', pathname: '/en/' },
];

const selectLocale = code => {
  localStorage.setItem(LOCALE_ITEM_KEY, code);
  window.location.href = './';
};

const clearLocale = () => {
  localStorage.removeItem(LOCALE_ITEM_KEY);
};

const localeNode = document.getElementById('locale');
const selectedLocaleValue = localStorage.getItem(LOCALE_ITEM_KEY);

if (localeNode) {
  if (selectedLocaleValue) {
    const selectedLocale = locales.find(
      ({ value }) => value === selectedLocaleValue
    );
    if (window.location.pathname !== selectedLocale.pathname) {
      window.location.pathname = selectedLocale.pathname;
    }
  } else {
    const node = document.createElement('div');
    node.style.height = '180px';
    node.style['text-align'] = 'center';
    node.style['padding-top'] = '40px';
    node.style.color = '#ffffff';
    node.style['background-image'] = 'url(/assets/img/IMG_4974.JPG)';
    node.style['background-position'] = 'center bottom';
    node.style['background-repeat'] = 'no-repeat';
    node.style['background-size'] = 'cover';
    node.style['font-family'] = '\'Roboto\', sans-serif;';
    node.style['font-weight'] = 400;
    node.innerHTML = '<div>歡迎您蒞臨本站！請選擇您偏好的語言</div><div>Welcome! Which language would you prefer?</div>';
    const flexNode = document.createElement('div');
    flexNode.style.display = 'flex';
    flexNode.style['justify-content'] = 'center';
    locales.forEach(({ value, label }) => {
      const button = document.createElement('div');
      button.innerText = label;
      button.addEventListener('click', () => selectLocale(value));
      button.style.width = '200px';
      button.style['line-height'] = '50px';
      button.style['font-size'] = '24px';
      button.style.background = 'rgba(0, 0, 0, 0.75)';
      button.style['border-radius'] = '5px';
      button.style.color = '#ffffff';
      button.style.margin = '8px 4px';
      button.style.cursor = 'pointer';
      flexNode.appendChild(button);
    });
    node.appendChild(flexNode);
    localeNode.appendChild(node);
  }
}

if (selectedLocaleValue === 'en-us') {
  Array.from(document.getElementsByClassName('base-menu-link')).forEach(
    link => {
      link.style.display = 'none';
    }
  );
  Array.from(
    document.querySelectorAll('.menu-list, .dropdown-content.collapsed')
  ).forEach(menu => {
    const link = document.createElement('a');
    //link.href = '/';
    link.innerText = 'About';
    link.className = 'menu-link';
    menu.insertBefore(link, menu.childNodes[0]);
    const link2 = document.createElement('a');
    link2.href = '/';
    link2.innerText = '中文';
    link2.className = 'menu-link';
    link2.addEventListener('click', () => selectLocale('zh-tw'));
    menu.insertBefore(link2, menu.childNodes[0]);
  });
}

Array.from(document.querySelectorAll('.menu-link.english')).forEach(link => {
  link.addEventListener('click', () => selectLocale('en-us'));
});
