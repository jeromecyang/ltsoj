setTimeout(() => {
    const podcastCollection = document.getElementById('podcast-collection');
    if (podcastCollection) {
        fetch('./podcast.xml').then(response => response.text()).then(text => xml2json(text, { compact: true }))
            .then(JSON.parse).then(({ rss: { channel: { item } } }) => {
                item.reverse();
                const collectionHtml = item.map(({ title: { _text: title }, ['itunes:image']: { _attributes: { href } } }) => `<div><div><img src='${href}' style='width: 300px'></div><div style='text-align: center'>${title}</div></div>`);
                podcastCollection.innerHTML = collectionHtml;
            });
    }
}, 200);