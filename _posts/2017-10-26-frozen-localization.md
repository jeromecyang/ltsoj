---
date: 2017-10-26 02:43:00+00:00
excerpt: 對一個同樣的產品進行局部改動，讓住在不同國家、使用不同語言的人都可以使用，這個工作叫做本地化（localization），《冰雪奇緣》就是透過本地化變成多種語言版本。除了迪士尼動畫之外，最常見需要本地化的產品其實就是軟體，我過去幾年在科技業的也參與了一些本地化的工作，這讓我對於迪士尼如何本地化他們的動畫產生了興趣。
layout: post
title: 從《冰雪奇緣》的多國語言版本談軟體的本地化（Localization）
tags:
- Cross-Culture
- Japan
- Music
- Arts
permalink: 2017/10/26/frozen-localization
image: https://lifetimesojournertravel.files.wordpress.com/2017/10/d98fe-b1sirg_iuaeso_e.jpg
featured: true
---

兩個月前的一天晚上，我正在網路上查「開ける」這個日文字的意思，結果Google打進去第一個跳出來的不是日文辭書，而是個youtube的影片，標題是《とびら開けて》，點進去原來是日文版《冰雪奇緣》（Frozen）裡的《Love Is An Open Door》，是由日文版的配音演員現場演唱，而且兩個人竟然還在舞台上做出和動畫中一樣的動作，實在是太可愛了（已融化）！於是那天晚上我像是發現新大陸一樣，把所有日文版《冰雪奇緣》的歌曲全部找出來聽了好幾次，嘗試從裡面抓到幾個剛學會的日文單字。

<iframe width="560" height="315" src="https://www.youtube.com/embed/xwNzzhOaMx4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

這件事情讓我想起了《冰雪奇緣》席捲全球那年，Youtube那支25語言版本的《Let It Go》影片。由於時間限制，每個語言都大概只唱了一句兩句，但這短短一兩句歌詞背後隱含著一個重要的訊息，就是整部電影的所有台詞、音樂、包裝和行銷，這麼大量的信息都在短時間內被從英文翻譯成了那個語言（Frozen實際的動畫和配音製作期不到一年）。迪士尼是如何做到的呢？

<iframe width="560" height="315" src="https://www.youtube.com/embed/BS0T8Cd4UhA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

對一個同樣的產品進行局部改動，讓住在不同國家、使用不同語言的人都可以使用，這個工作叫做本地化（localization），《冰雪奇緣》就是透過本地化變成多種語言版本。除了迪士尼動畫之外，最常見需要本地化的產品其實就是軟體，我過去幾年在科技業的也參與了一些本地化的工作，這讓我對於迪士尼如何本地化他們的動畫產生了興趣。

## 到底需要多少個版本？

根據維基百科上的列表，迪士尼官方把2013年出品的《冰雪奇緣》本地化成41個不同的版本（相較於1994年出品的《獅子王》只有15個版本），那麼這是否代表著該片總共被翻譯成41種語言、提供給41個國家的觀眾看呢？看起來並非如此。以下是這41個（官方）版本的列表：

* Arabic 阿拉伯語
* Brazilian Portuguese 巴西葡萄牙語
* Bulgarian 保加利亞語
* Canadian French 加拿大法語
* Cantonese Chinese 粵語
* Castilian Spanish 歐洲西班牙語
* Catalan 加泰羅尼亞語
* Croatian 克羅埃西亞語
* Czech 捷克語
* Danish 丹麥語
* Dutch 荷蘭語
* English 英語
* Estonian 愛沙尼亞語
* European French 歐洲法語
* European Portuguese 歐洲葡萄牙語
* Finnish 芬蘭語
* Flemish 比利時荷蘭語
* German 德語
* Greek 希臘語
* Hebrew 希伯來語
* Hindi 印地語
* Hungarian 匈牙利語
* Icelandic 冰島語
* Indonesian 印尼語
* Italian 義大利語
* Japanese 日語
* Kazakh 哈薩克語
* Korean 韓語
* Latin American Spanish 拉丁美洲西班牙語
* Latvian 拉脫維亞語
* Lithuanian 立陶宛語
* Malay 馬來語
* Mandarin Chinese (China) 漢語（中國）
* Mandarin Chinese (Taiwan) 漢語（台灣）
* Norwegian 挪威語
* Polish 波蘭語
* Romanian 羅馬尼亞語
* Russian 俄羅斯語
* Serbian 塞爾維亞語
* Slovak 斯洛伐克語
* Slovene 斯洛維尼亞語
* Swedish 瑞典語
* Thai 泰語
* Turkish 土耳其語
* Ukrainian 烏克蘭語
* Vietnamese 越南語

從這個清單裡可以看出，本地化後的《冰雪奇緣》並非一個語言一個版本或一個國家一個版本：

1. 有些語言同時有多個版本，例如：西班牙語版分成歐洲西班牙語版和拉丁美洲西班牙語版、葡萄牙語版分成歐洲葡萄牙語版和巴西葡萄牙語版、法語分成歐洲法語版和加拿大法語版等。
2. 有些國家內存在多種語言版本，例如：西班牙境內有西班牙語和加泰羅尼亞語、中國國內有普通話版和粵語版等。


所以，無論是只考慮國家或只考慮語言都是不夠的，兩者必須同時考量。軟體的「地區設定」（locale）概念就是將兩者組合，用來表示一個本地化版本涵蓋的文化或地區。例如，台灣的繁體中文版通常標示成zh-TW，表示中文——台灣，同樣也有zh-CN（中文——中國）、fr-CA（法語——加拿大）、pt-BR（葡萄牙語——巴西）。這些編碼是根據國際通用的ISO 639-1語言代碼與ISO 3166-1國家代碼決定。同理我們也可以知道，如果要標示台語翻唱神人柏慎的《讓他去》（台語版的《Let It Go》），那地區設定就是nan-TW（閩南語——台灣），而台灣客家話與阿美語則可分別被標示成hak-TW與ami-TW。

<iframe width="560" height="315" src="https://www.youtube.com/embed/2PdOl5o1gxg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

這裡一個有趣的現象是：有些語言的使用者非常多，但迪士尼並沒有製作這些語言的本地化版本，像是孟加拉語（Bengali）、旁遮普語（Punjabi）、吳語（Wu）、爪哇語（Javanese）、泰盧固語（Telugu）、馬拉地語（Marathi）、泰米爾語（Tamil）等，這些語言的母語使用者都在7000萬人以上，但或許是因為有廣泛使用的替代性語言，因此就沒有必要另外製作本地化版本；反倒是歐洲不少小國，包括人口只有100萬出頭的愛沙尼亞、30萬出頭的冰島，仍然有自己的本地化版本。

![](https://lifetimesojournertravel.files.wordpress.com/2017/10/4b9b9-avcw-63011.jpg)
*Source: http://www.disney.co.jp/movie/anayuki/character/character01.html*


![](https://lifetimesojournertravel.files.wordpress.com/2017/10/4b9b9-avcw-63011.jpg)
*Source: http://www.disney.co.jp/movie/anayuki/character/character01.html*


## 有哪些東西需要本地化？

最常見的本地化就是把使用者介面上的文字變成本地的文字，或是像《冰雪奇緣》加上本地的配音或是字幕，不過本地化的範圍並不僅止於此，無論是軟體或是動畫，其實還有其他必須本地化的部分。

當一個軟體要被本地化的時候，除了文字之外最常見的就是時間和數字的本地化，這對於在美國業界工作的人來說感受尤其深刻呀！美國幾乎所有記量單位都不使用公制，所以長度必須使用英里（mile）、英尺（feet）、英吋（inch），重量必須使用磅（pound），容量必須使用加侖（gallon）；除此之外，美國使用的日期通常是月、日、年的順序，這和世界上多數地方的年、月、日或歐洲常見的日、月、年都不一樣，而且使用12小時制加上AM和PM、一週是由週日而非週一開始⋯⋯。

雖然說美國是個比較誇張的特例，但其他各國在許多細節上仍然有各自習慣的用法，像是歐陸語言裡面小數點使用逗號（，），而千位分隔符號則是一點（·），和英文的慣例正好相反；德文裡面所有名詞字首都要大寫⋯⋯，所以軟體的本地化絕對不是把所有的文字變成另外一個語言就可以，還有各種多如牛毛的小細節。幸好這些東西在業界行之有年，基本上已經有公認的規則可循，大部分高階的程式或腳本語言（scripting language）本身也都支援這些時間和數字的轉換，對我們這些工程師來說並不麻煩，只要心裡記得要考慮這件事情就可以了。而一般文字翻譯的工作，幾乎都是直接外包出去，軟體公司只負責把翻譯好的文字加到使用者介面上。



![](https://lifetimesojournertravel.files.wordpress.com/2017/10/88b39-decimalseparator.png)
*綠色：小數點使用逗號的地區藍色：小數點使用一點的地區紅色：小數點使用阿拉伯式逗號的地區By NuclearVacuum - File:BlankMap-World6.svgiThe source code of this SVG is valid., CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10843055*

至於《冰雪奇緣》的本地化，除了配音和字幕之外，比較有趣的部分是如何在41個語言裡面找到艾莎（Elsa）和安娜（Anna），不僅要為他們配對白，也要能夠唱他們的歌曲。讓我意外的是，這個高難度的任務並不是像軟體翻譯那樣直接外包出去，而是由Disney Character Voices International這個迪士尼的子公司全權負責。迪士尼對配音與配唱者的要求是：聲線必須和原本的艾莎與安娜相似、是該語言的母語使用者、在當地有一定知名度，所以光是為了找41種語言裡的艾莎就試鏡了200多人。除此之外，迪士尼也有考慮到各國在音樂上的偏好，例如廣東話以及台灣版本的艾莎聲音必須比其他國家的細一些，「因為那是（這些地方）文化的一部分。」除此之外，更不用說翻譯的歌詞如何和動畫完美對嘴、有的配音者必須由其他人代唱這些細節了。

由此可見為了要真正打入一個市場，《冰雪奇緣》的本地化已經完全超越了語言和文字的層次，連挑選歌手、如何演唱這些細節都本地化了。如果迪士尼真的這麼有誠意，不知道有沒有考慮下一部動畫真的請柏慎唱台語版主題曲，或是採用類似台灣版《我們這一家》（あたしんち）裡面花媽式的國台語夾雜配音？



![](https://lifetimesojournertravel.files.wordpress.com/2017/10/3aa64-4884.jpg?w=210)
*Source: https://tw.movies.yahoo.com/movieinfo_main.html/id=4884*


## 使用者介面的本地化

最後來談談我自己實際參與過的使用者介面本地化。前面有提到，軟體的翻譯基本上是全部外包，公司裡面只有該語言的管理者負責溝通和審核，那麼工程師應該就只要把介面上會出現的所有文字換成翻譯好的該國語言版本就可以吧？

某個程度上來說是這樣沒錯。通常我們會先把使用者介面上會出現的文字全部換成替代符號（token）。例如，如果在HTML裡面有一個「取消」的按鈕，像這樣：

Cancel

因為Cancel是英文，我們必須把它置換成替代符號，像是：

@@__cancel__@@

「@@__cancel__@@」就是「取消」這個字的替代符號，使用者不會看到，只會在原始碼裡面出現。當原始碼要被押製（build）成為出廠的版本的時候，通常每個語言版本會有一份文件，定義在這個語言裡面@@__cancel__@@應該要被取代成什麼。像這樣：



<table style="border-collapse:collapse;border:none;" >



<tbody >
<tr style="height:0;" >

<td style="padding:5pt;vertical-align:top;border:solid #000000 1pt;" >en-US
</td>

<td style="padding:5pt;vertical-align:top;border:solid #000000 1pt;" >{ "@@__cancel__@@": "Cancel" }
</td>
</tr>
<tr style="height:0;" >

<td style="padding:5pt;vertical-align:top;border:solid #000000 1pt;" >zh-TW
</td>

<td style="padding:5pt;vertical-align:top;border:solid #000000 1pt;" >{ "@@__cancel__@@": "取消" }
</td>
</tr>
</tbody>
</table>

於是在押製過程中這個替代符號就會被置換，在英文版裡面會顯示成「Cancel」，在台灣中文版裡面則顯示成「取消」。說穿了就是一連串的「尋找」（Find）和「取代」（Replace）工作。

這個使用者介面本地化過程聽起來很簡單，但實際執行上還是有很多必須注意的地方。最常見的例子就是阿拉伯文和希伯來文是從右向左書寫，但幾乎所有的使用者介面在設計時都是從左到右，本地化完之後這些文字還能出現在應該出現的位置上嗎？有沒有變得無法閱讀？另外一個常見例子則是日耳曼語系的語言（尤其是德語）單字通常比較長，很多時候前端工程師預留的空間足夠放入那個英文單字，但是翻譯成德語之後就放不下了，這個字有可能就會被切掉或是超出邊界。對於一個前端工程師來說，諸如此類的考量不少。我們並不需要真的懂這些語言，但是語言本身的特性（書寫方向、單字長度）會直接影響到使用者介面的外觀，所以還是得留意這些差異，甚至是在編寫的時候就意識到這類翻譯之後才會出現的問題。

上面講的這個就是我在2012年剛進業界時的第一個任務：把Esri的招牌產品ArcGIS online在不同語言環境下打開，然後一個一個進去看本地化之後是不是所有功能都還可以正常運作。因為產品支持14個語言（後來還一路增加到27個），也就是同樣的事情要重複做14次，憑良心講根本就是一個超級無聊的工作呀！但回過頭來看，那時雖然對語言沒有太大興趣，每天這樣重複看著這些各國文字，慢慢習慣了他們的樣貌，因而對那些語言有了粗略的了解，這對一個明明喜歡地理、在地理資訊公司工作、卻不能到處跑的人來說，真的是在那狹小無趣的辦公室裡開了一扇通往世界的窗啊（遠目配上手勢）！

補充：關於《冰雪奇緣》的本地化，可以參考洛杉磯時報的文章：
['Frozen': Finding a diva in 41 languages](http://articles.latimes.com/2014/jan/24/entertainment/la-et-mn-frozen-how-disney-makes-a-musical-in-41-languages-20140124)



![](https://lifetimesojournertravel.files.wordpress.com/2017/10/d98fe-b1sirg_iuaeso_e.jpg)
*Source: https://www.boston.com/culture/movies/2014/10/31/they-cant-let-it-go-elsa-costumes-are-here-to-stay*








