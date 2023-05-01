---
layout: wide
title: 來賓名人堂
---
旅行熱炒店能有精彩的內容，來賓的參與功不可沒！點選頭像進入來賓頁面，可詳閱合作集數與相關連結。

{% assign posts1 = site.guests | where: 'highlight', true | sort: 'title' %}
{% assign posts2 = site.guests | where_exp: 'item', 'item.highlight != true' | sort: 'title' %}
{% assign posts = posts1 | concat: posts2 %}
{% include post-preview-grid.html %}