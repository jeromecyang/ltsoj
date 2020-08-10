setTimeout(() => {
    const podcastCollection = document.getElementById('podcast-collection');
    if (podcastCollection) {
        fetch('./podcast.xml').then(response => response.text()).then(text => xml2json(text, { compact: true }))
            .then(JSON.parse).then(({ rss: { channel: { item } } }) => {
                item.reverse();
                console.log(item);
                const collectionHtml = item.map(({ title: { _text }, ['itunes:image']: { _attributes: { href } } }) => `<div style='width: 300px; margin: 10px'><div><img src='${href}'></div><b>${_text}</b></div>`);
                podcastCollection.innerHTML = collectionHtml;
            });
    }
}, 200);