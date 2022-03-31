---
layout: post
title: 烏克蘭專區
date: 2022-02-26
---

<i style="color: red">本頁面為因應2022年2月24日俄羅斯入侵烏克蘭，作為資訊彙整分享用的專區！目前以提供難民概況與援助資訊為主，最新消息建議參考各大新聞來源。</i>

## 難民概況

<script>
Promise.all([
  fetch('https://data2.unhcr.org/population/get/sublocation?widget_id=285654&sv_id=54&population_group=5461&forcesublocation=0&fromDate=1900-01-01').then(r => r.json()),
  fetch('https://data2.unhcr.org/population/?widget_id=285660&sv_id=54&population_group=5460').then(r => r.json())
]).then(([{ data }, { data: [total] }]) => {
  const directory = {
    0: {name_zh: '總計', flag: '', color: '#888888'},
    10781: {name_zh: '波蘭', flag: '🇵🇱', color: '#003f5c', population: 38116000},
    10782: {name_zh: '羅馬尼亞', flag: '🇷🇴', color: '#ff6361', population: 19186201},
    10783: {name_zh: '匈牙利', flag: '🇭🇺', color: '#bc5090', population: 9689000},
    10784: {name_zh: '摩爾多瓦', flag: '🇲🇩', color: '#ffa600', population: 2597100},
    10785: {name_zh: '斯洛伐克', flag: '🇸🇰', color: '#58508d', population: 5452025},
    10786: {name_zh: '白羅斯', flag: '🇧🇾', color: '#888888'},
    10791: {name_zh: '俄羅斯', flag: '🇷🇺', color: '#888888'},
  };
  const rows = [{ ...total, geomaster_name: '', geomaster_id: 0 }, ...data].map(({ geomaster_name, geomaster_id, individuals, date }) => {
    const { name_zh, color, flag, population } = directory[geomaster_id];
    return `<div style="color: #ffffff; background-color: ${color}; margin: 10px 0; padding: 10px">
      <div>${name_zh} ${geomaster_name} ${flag}</div>
      <div style="font-size: 2rem; line-height: 2rem; margin-top: 0.5rem">
        ${Number(individuals).toLocaleString()}
        <span style="font-size: 0.8rem">(${date})</span>
      </div>
      ${population ? `<div>平均每 <span style="font-size: 1.5rem">${(population / Number(individuals)).toFixed(0)}</span> 人支持一位難民 <span style="font-size: 0.8rem">(總人口 ${population.toLocaleString()})</span></div>` : ``}
    </div>`;
  });
  document.getElementById('stats').innerHTML = rows.join('');
})
</script>
<div id="stats"></div>

以上皆為直接來自[聯合國難民署](https://data2.unhcr.org/en/situations/ukraine)（UNHCR）之即時數據。

## 難民面對的挑戰

![](https://ichef.bbci.co.uk/news/976/cpsprodpb/1176F/production/_123453517_gettyimages-1373101584-594x594.jpg)
*圖片來源：[BBC](https://www.bbc.com/news/world-60555472)*

* 部分難民為非烏克蘭籍的第三國人士，在移動過程中有可能遭受歧視或者相對缺乏支持，有些政府與機構已經開始介入，確保第三國難民也能接受平等的待遇。
* 烏克蘭境內仍有許多因為戰事而流離失所者，但防禦工事使得國內部分地區的交通變得更加困難，當地目前許多人靠著加密通訊工具如Telegram群組交換相關訊息。
* 有些邊界的等待時間非常漫長，例如波蘭邊界等待時間可能長達數日。許多難民放棄車輛改用步行方式入境，但當地目前氣溫極低。

## 如何支持難民

### 提供住宿或其他支援

* [Support Ukraine Now](https://supportukrainenow.org/refuge-for-ukrainians)：歐洲各國的難民住宿資源列表，可以看看在各國能如何接待難民。
* [Airbnb.org](https://www.airbnb.org/help-ukraine)：在Airbnb上申請成為住宿提供者。
* [refugee.ro](https://refugees.ro/)：登錄可以提供的資源（以羅馬尼亞為主）。

### 捐款給能夠直接支持難民的單位

* 財團法人賑災基金會賑濟烏克蘭專戶（台灣）
  * 戶名：財團法人賑災基金會
  * 銀行名稱：土地銀行 長春分行
  * 銀行帳號：102-005-124-619
* [聯合國難民署](https://donate.unhcr.org/int/en/ukraine-emergency)
* [國際難民救援組織](https://help.rescue.org/donate/ukraine-acq)
* [GlobalGiving Ukraine Crisis Relief Fund](https://www.globalgiving.org/projects/ukraine-crisis-relief-fund/)
* [CARE.org](https://my.care.org/site/Donation2?df_id=31067)

其他可參考[Support Ukraine Now](https://supportukrainenow.org/refuge-for-ukrainians)（民間協作、烏克蘭官方支持的總整理），或自行上網搜尋。

## 了解更多

* [Refugee 101 Taiwan 概況整理](https://www.facebook.com/Refugee-101-Taiwan-104676894801001/posts/104676894801001)
* [from Syria：「我們比世界上任何人都清楚，烏克蘭現在正在經歷什麼。」—敘利亞女性聲援烏克蘭](https://www.facebook.com/fromsyriatw/posts/3167564573516383)
* [【投書】柏林台灣留學生當志工，協助安置烏克蘭難民：這是我人生中最震撼的一天（獨立評論＠天下）](https://opinion.cw.com.tw/blog/profile/52/article/12018)
* [【投書】那些與我在柏林月台相遇的烏克蘭難民：當失去一切，我們要用什麼姿態面對明天？（獨立評論＠天下）](https://opinion.cw.com.tw/blog/profile/52/article/12042)
* [英國國家廣播BBC針對難民目前概況作的整理](https://www.bbc.com/news/world-60555472)
* [聯合國難民署3/1的簡報](https://www.unhcr.org/en-us/news/briefing/2022/3/621deda74/unhcr-mobilizing-aid-forcibly-displaced-ukraine-neighbouring-countries.html)

## 旅行熱炒店相關集數

* [EP92 柏林中央車站月台上，當載著烏克蘭難民的專列緩緩進站：一位難民志工的第一線觀察 ft. 旅居柏林台灣人 劉時宏](podcast-ep092)
* [SP4 「Slava Ukraini!」「Heroiam slava!」 來自抗議現場的聲音，從烏克蘭民族主義語言變成一場全球運動的口號](podcast-sp004)
* [SP3 很久很久以前，那些烏俄戰爭開打之前發生的事](podcast-sp003)
* [EP7 蘇聯陰魂不散，即便到天涯海角仍與你相伴！ 斯瓦巴-巴倫支堡、克里米亞 ft. 鯨魚](podcast-ep007)
* [EP5 不顧基輔反對！烏克蘭的最東邊，竟然藏著兩個地圖上找不到的獨立國家!? 頓內次克、盧甘斯克、德涅斯特河沿岸 ft. 鯨魚](podcast-ep005)

![](https://imgur.com/fWUOtuA.jpg)
*根據3月1日數據製作之圖表*

## 戰爭相關資訊圖表

* [衛報 The Guardian](https://www.theguardian.com/world/2022/feb/25/russias-war-in-ukraine-complete-guide-in-maps-video-and-pictures) <span style="color: red"><- 非常清楚詳細，在此特別推薦！</span>
* [英國國家廣播公司 BBC](https://www.bbc.com/news/world-europe-60506682)
* [紐約時報 New York Times](https://www.nytimes.com/interactive/2022/world/europe/ukraine-maps.html)

## 提供即時動態更新的新聞頁面

### 中文

* [端傳媒](https://theinitium.com/article/20220224-whatsnew-ukraine-russia-war) <span style="color: red"><- 更新最快的中文頁面</span>
* [轉角國際](https://global.udn.com/global_vision/) <span style="color: red"><- 非動態更新，但隨時有新文章刊出</span>
* [g0v 俄羅斯入侵烏克蘭資訊野生整合平台 2022.2-](https://g0v.hackmd.io/@chihao/ukraine/) <span style="color: red"><- 台灣網友在零時政府g0v上建立的資訊整合頁面</span>

### 英文

* [紐約時報 New York Times](https://www.nytimes.com/)
* [美國有線電視新聞網 CNN](https://www.cnn.com/)
* [衛報 The Guardian](https://www.theguardian.com/)

## 如何盡一份心力

<i style="color: red">以下列表僅參考各方提供之捐款對象，若要捐款請務必確認該機構的性質與款項運用方式，判斷之後再行動。</i>
  
* [Support Ukraine Now](https://supportukrainenow.org/)：[Global Shapers](https://www.globalshapers.org/)組織建立的一站式援助資訊整合平台，由烏克蘭政府官方支持。

### 捐款（人道救援）

* [UN Crisis Relief](https://crisisrelief.un.org/t/ukraine)：聯合國危機救援，烏克蘭人道救援基金。
* [GlobalGiving Ukraine Crisis Relief Fund](https://www.globalgiving.org/projects/ukraine-crisis-relief-fund/)：烏克蘭以及附近難民收容地區人道救援。
* [Catholic Relief Services](https://support.crs.org/donate/donate-ukraine)：天主教救援機構，援助烏克蘭當地需要協助的家庭。
* [Nova Ukraine](https://novaukraine.org/)：提供人道援助給烏克蘭境內脆弱群體或個人的非營利組織。
* [Voices of Children](https://voices.org.ua/en/donat/)：支持戰爭中遭受創傷的兒童。
* [Red Cross](https://www.icrc.org/en/donate/ukraine)：紅十字會，預計提供300萬人乾淨的用水並援助66000位住所受損的災民。
* [Razom Inc](https://razomforukraine.org/)：強化烏克蘭社群參與。

### 捐款（烏克蘭政府或軍方）

* [National Bank of Ukraine](https://bank.gov.ua/en/news/all/natsionalniy-bank-vidkriv-spetsrahunok-dlya-zboru-koshtiv-na-potrebi-armiyi)：直接捐款到烏克蘭國家銀行。
* [Ukraine Ministry of Defence](https://www.mil.gov.ua/en/donate.html)：直接捐款烏克蘭國防部。
* [Come Back Alive](https://savelife.in.ua/en/donate/): 提供烏克蘭軍物資與技術支援。
* [United Help Ukraine](https://unitedhelpukraine.org/)：提供醫療支援給受傷的軍人並支持寡婦。
* [SGURTOVANI](https://www.betterplace.me/verteidigungsausruestung-fuer-die-ukraine)：立即購買當地急需之器材並且運送到當地。

### 集會遊行

* [Stop Putin](https://www.stopputin.net/)：世界各地抗議俄羅斯入侵烏克蘭集會活動列表。
* 建議在自己所在地刷Twitter，會更容易發現正在進行中的集會活動！

## 衝突脈絡討論

* [報導者：飛彈與坦克進逼，5位烏克蘭青年的求援、見證和反抗：「任何人都無法動搖我們對自由的珍愛」](https://www.twreporter.org/a/russia-ukraine-war-2022-youth-voice)
* [Institute for the Study of War](https://www.understandingwar.org/)
* [Cheap：恩怨一千年 ▶ 烏克蘭與俄羅斯有什麼深仇大恨? 克里米亞危機、頓巴斯戰爭的前因後果](https://www.youtube.com/watch?v=zuoqLNK8_mc) （Youtube）
* [端傳媒：獨立廿八年、兩度革命，烏克蘭還在問：我是誰？](https://theinitium.com/article/20190402-international-ukraine-identity-building/)
* [美國台灣觀測站：美國為什麼不出兵？](https://www.facebook.com/ustaiwanwatch/posts/1938707679646527)
* [美國台灣觀測站：台灣該怎麼看？](https://www.facebook.com/ustaiwanwatch/posts/1937674573083171)
* [麻瓜的語言學：烏克蘭語和俄羅斯語是不是同一個語言？](https://www.facebook.com/uegugu/posts/5657439294283280)
* [無國界譯師談烏克蘭的俄語政策](https://www.facebook.com/yianlanguage/posts/477458123838939)

## 旅行熱炒店相關圖表

<img src="https://imgur.com/BFJA8ngl.jpg" style="width: 300px">
[俄羅斯與他的快樂夥伴們，那些傻傻分不清楚的東方/共產陣營組織](https://ltsoj.com/map/eastern-bloc)

<img src="https://imgur.com/rwPR46Hl.jpg" style="width: 300px">
[從波羅的海、黑海到亞得里亞海都略懂：斯拉夫語族](https://ltsoj.com/map/slavic)

<img src="https://imgur.com/Dd2T18dl.jpg" style="width: 300px">
[「不顧基輔反對」從烏克蘭獨立的兩小國：盧甘斯克、頓內次克](https://ltsoj.com/map/east-ukraine)

<img src="https://imgur.com/YH3tQnfl.jpg" style="width: 300px">
[克里米亞半島](https://ltsoj.com/map/crimea)

<img src="https://imgur.com/I2CxNiLl.jpg" style="width: 300px">
[德涅斯特河沿岸（德左）](https://ltsoj.com/map/transnistria)

## 重要動態編譯

<i style="color: red">以下資訊僅編譯至3月1日為止。</i>
  
### 至 3/1 17:00 GMT 為止

* 2/28烏克蘭與俄羅斯雙方談判結束，兩方各自打道回府，可能會有下一次談判。
* 戰爭持續中，俄羅斯大舉將更多資源與人力送往基輔戰場。
* 烏克蘭第二大城受到猛烈攻擊。
* 瑞士破天荒加入制裁行列。
* 已經有超過60萬烏克蘭難民逃往其他國家。

### 至 2/28 6:30 GMT 為止

* 烏克蘭與俄羅斯雙方代表將於今（2/28）日於白羅斯邊界對談，烏克蘭駐美大使日前表示「我們準備好要對談，但我們並沒有準備要投降」。
* 過去兩天俄羅斯佔領區域並未明顯擴大；俄羅斯宣布將核子武器置於備戰狀態。
* 聯合國估計已有超過36萬烏克蘭居民離境，其中20萬前往波蘭。

### 至 2/27 2:00 GMT 為止

* 歐盟多國與美國決定將部分俄羅斯銀行逐出SWIFT（環球銀行金融電信協會），將使得這些銀行無法進行國際交易。
* 美國軍方人士認為，俄軍推進的速度低於預期，有可能至今仍未控制任何一座主要城市，顯示或許烏克蘭方防守力比預計的強，而俄羅斯在補給上越來越困難。
* 多達12萬烏克蘭難民已經離境，聯合國估計最後可能會有多達400萬的烏克蘭難民。

### 至 2/26 5:30 GMT 為止

* 俄軍已經逼近基輔市區，距離總統府可能只剩幾公里距離。
* 基輔整個夜晚都可聽到爆炸聲，總統澤倫斯基表示會繼續堅守基輔。
* 聯合國安理會投票通過譴責俄羅斯入侵烏克蘭，其中中國、印度與阿聯在投票中棄權。

### 至 2/25 17:00 GMT 為止

* 俄羅斯往基輔推進中，烏克蘭炸毀部分橋樑阻擋
* 烏克蘭開始徵召118-60歲後備軍力，並開始配發18000支步槍
* 大量烏克蘭居民跨越邊界進入波蘭
* 歐洲歌唱大賽(Eurovision)宣佈禁止俄羅斯參賽
* 土耳其表示因為蒙特勒公約(Montreux Convention)協定，無法禁止俄羅斯軍艦通過博斯普魯斯海峽進入黑海

## 製作者

本頁面由旅行熱炒店主廚Jerome獨立自行製作，若有資訊不全之處，或是想補充更多資源，非常歡迎隨時以email與我聯絡 travel.wok@ltsoj.com 。
