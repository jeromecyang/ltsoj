---
layout: default
title: 節目集數索引（依地區、議題分類）
tags:
- Southeast Asia
- South Asia
- Central Asia
- Caucasus
- Eastern Europe
- Middle East
- North Africa
- West Africa
- East Africa
- Southeastern Europe
- Central Europe
- Northern Europe
- Western Europe
- Southern Europe
- US Northeast
- US Midwest
- US South
- US West
- Alaska
- North America
- Central America
- Caribbean
- South America
- Oceania
- Northeast Asia
- Taiwan
- Immigration
- Q&A
- Other
translation:
  Southeast Asia: 東南亞
  South Asia: 南亞
  Central Asia: 中亞
  Caucasus: 高加索
  Eastern Europe: 東歐
  Middle East: 中東
  North Africa: 北非
  West Africa: 西非
  East Africa: 東非
  Southeastern Europe: 東南歐
  Central Europe: 中歐
  Northern Europe: 北歐
  Western Europe: 西歐
  Southern Europe: 南歐
  US Northeast: 美國東北部
  US Midwest: 美國中西部
  US South: 美國南部
  US West: 美國西部
  Alaska: 阿拉斯加
  North America: 北美
  Central America: 中美
  Caribbean: 加勒比海
  South America: 南美
  Oceania: 大洋洲
  Northeast Asia: 東北亞
  Taiwan: 台灣
  Immigration: 移民與難民
  Other: 其他
---
<div class="page-content">

<h1>{{ page.title }}</h1>
<p>旅行熱炒店至今製作過的內容，涵蓋了世界上的許多不同地區與議題。若您想快速找到關於某個地區或是議題的集數，歡迎利用下面的分類清單與地圖！</p>

{% for tag in page.tags %}
  {% assign episodes = site.episodes | where_exp: "item", "item.tags contains tag" | reverse %}
  <h2>{{page.translation[tag]}} {{tag}} ({{episodes.size}})</h2>
  <ul>
  {% for episode in episodes %}
    <li><a href="{{ episode.url }}">{{ episode.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}

</div>