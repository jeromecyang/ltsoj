---
layout: default
title: 內容索引（依地區、議題分類）
areas:
  Asia:
  - Taiwan
  - Northeast Asia
  - Southeast Asia
  - South Asia
  - Central Asia
  - Caucasus
  - Middle East
  Africa:
  - North Africa
  - West Africa
  - East Africa
  Europe:
  - Eastern Europe
  - Southeastern Europe
  - Central Europe
  - Northern Europe
  - Western Europe
  - Southern Europe
  Americas:
  - US Northeast
  - US South
  - US Midwest
  - US West
  - Alaska
  - North America
  - Central America
  - Caribbean
  - South America
  Oceania:
  - Oceania
topics:
- Immigration
- Sustainability
- Landscape
- Indigenous
- Outdoor
- Food
- Q&A
- Other
tags:
- Southeast Asia
- South Asia
- Central Asia
- Caucasus
- Middle East
- North Africa
- West Africa
- East Africa
- Eastern Europe
- Southeastern Europe
- Central Europe
- Northern Europe
- Western Europe
- Southern Europe
- US Northeast
- US South
- US Midwest
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
- Sustainability
- Landscape
- Indigenous
- Outdoor
- Food
- Q&A
- Other
translation:
  Asia: 亞洲
  Africa: 非洲
  Europe: 歐洲
  Americas: 美洲
  Oceania: 大洋洲
  Southeast Asia: 東南亞
  South Asia: 南亞
  Central Asia: 中亞
  Caucasus: 高加索
  Middle East: 中東
  North Africa: 北非
  West Africa: 西非
  East Africa: 東非
  Eastern Europe: 東歐
  Southeastern Europe: 東南歐
  Central Europe: 中歐
  Northern Europe: 北歐
  Western Europe: 西歐
  Southern Europe: 南歐
  US Northeast: 美國東北部
  US South: 美國南部
  US Midwest: 美國中西部
  US West: 美國西部
  Alaska: 阿拉斯加
  North America: 北美
  Central America: 中美
  Caribbean: 加勒比海
  South America: 南美
  Oceania: 大洋洲
  Northeast Asia: 東北亞
  Taiwan: 台灣
  Immigration: 人口遷移
  Sustainability: 環境與永續
  Landscape: 特殊地景
  Indigenous: 原住民
  Outdoor: 戶外運動
  Food: 飲食文化
  Q&A: Q&A
  Other: 其他
---
<h1>{{ page.title }}</h1>
<p>旅行熱炒店至今製作過的內容，涵蓋了世界上的許多不同地區與議題。若您想快速找到關於某個地區或是議題的集數，歡迎利用下面的分類清單與地圖！</p>

### 依地區分類

{% for area in page.areas %}
  <div style="display: flex; flex-wrap: wrap">
    {% assign continent = area[0] %}
    {% assign regions = area[1] %}
    <div style="margin: 8px 4px 8px 0">{{page.translation[continent]}}</div>
    {% for region in regions %}
    <div style="background-color: #eeeeee; margin: 4px; padding: 4px 8px; border-radius: 16px">
      <a href="#{{region}}" style="text-decoration: none">{{page.translation[region]}}</a>
    </div>
    {% endfor %}
  </div>
{% endfor %}

### 依議題分類

<div style="display: flex; flex-wrap: wrap">
  {% for topic in page.topics %}
  <div style="background-color: #eeeeee; margin: 4px; padding: 4px 8px; border-radius: 16px">
    <a href="#{{topic}}" style="text-decoration: none">{{page.translation[topic]}}</a>
  </div>
  {% endfor %}
</div>
---

{% for tag in page.tags %}
  {% assign episodes = site.episodes | where_exp: "item", "item.tags contains tag" | reverse %}
  <div id="{{tag}}" style="position: relative; top: -56px"></div>
  <h3>{{page.translation[tag]}} ({{episodes.size}})</h3>
  {% for episode in episodes %}
  <div style="font-size: 0.9rem; margin: 8px 0">
    <a href="{{ episode.url }}" style="text-decoration: none">{{ episode.title }}</a>
  </div>
  {% endfor %}
{% endfor %}