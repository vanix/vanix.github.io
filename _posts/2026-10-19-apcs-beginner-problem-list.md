---
author: 歐巴計概
date: 2026-10-19 16:00:00 +0800
layout: post
permalink: /2026/10/apcs-beginner-problem-list.html
title: APCS初級前的基礎練習｜從0開始的Python 分類清單（輸入輸出、條件判斷、迴圈、字串與串列）與線上評測連結
description: "APCS 初級前的基礎題單一次整理三大類：輸入輸出與變數算術運算、條件判斷、迴圈，每題都附線上評測系統（SSSH Zero Judge）的超連結，點題號就能直接練習。另附課堂作業分組、建議練習順序與常見問題，適合從零開始學 Python 的學生自學、老師派作業使用，題號與頁面標題一一對照，方便追蹤進度。"
categories: [資訊教學, 程式教學]
tags: [Python, APCS, 程式教學, APCS初級, 題單, 題庫, 評測系統, 練習題]
image:
  path: /assets/images/cover/apcs-beginner-problem-list.png
  alt: APCS 初級題單封面，從0開始的 Python 62 題分類練習清單與線上評測連結
---

💡 這份 **APCS 初級前的基礎題單**把三大類整理好：**輸入輸出與算術運算、條件判斷、迴圈**，每一題都附上評測系統的超連結，點題號就能直接寫。

[APCS教學文章列表](https://vanix.github.io/categories/%E7%A8%8B%E5%BC%8F%E6%95%99%E5%AD%B8/)

[APCS實作線上課程](https://www.youtube.com/playlist?list=PLN9g1rvyo05p70K3HU-hWhEkoNs26WhD0)

| 類別 | 重點觀念 | 建議時機 |
| --- | --- | --- |
| 第一類：輸入輸出、變數與算術運算 | `input()`／`print()`、變數、四則運算、整數除法與餘數 | 完全沒寫過程式 |
| 第二類：條件判斷 | `if`／`elif`／`else`、比較運算、邏輯判斷 | 會讀寫資料之後 |
| 第三類：迴圈 | `for`／`while`、巢狀迴圈、質數與費氏數列 | 會條件判斷之後 |

## APCS 初級前的基礎題單怎麼用？

**每一題的網址都長一樣，只有最後的題號不同。** 評測系統的網址格式是：

```text
http://163.30.43.15/ShowProblem?problemid=a001
```

把結尾的 `a001` 換成你要練的題號就對了，例如 `a050` 就是求矩形面積。下面題單裡的**題號和題目都已經做好超連結**，直接點就能開題目頁。

本篇題單的題目來自校內評測系統 **SSSH Zero Judge**，題目編號以 `a` 開頭，題名與頁面標題一致（例如 `a001. 哈囉`），照題號順序練最不容易漏。

> **先備能力**：第一類之前完全不用準備，會開瀏覽器就行。想先補觀念的話，可以看 [APCS 初級 裝飲料解題教學](https://vanix.github.io/2026/10/apcs-o711-pour-drink.html) 熟悉迴圈與條件判斷。
{: .prompt-tip }

## 第一類：輸入輸出、變數與算術運算

**這一類只考兩件事：讀得進來、算得出來、印得出去。** 每題都是固定的輸入輸出格式，重點在練 `input()`、`print()`、變數指派，以及整數除法與餘數（`//` 與 `%`）。

### 課堂作業：輸入與輸出

| 題號 | 題目 |
| --- | --- |
| [a007](http://163.30.43.15/ShowProblem?problemid=a007) | [K-I-S-S-I-N-G](http://163.30.43.15/ShowProblem?problemid=a007) |
| [a012](http://163.30.43.15/ShowProblem?problemid=a012) | [Johnny B. Goode](http://163.30.43.15/ShowProblem?problemid=a012) |
| [a033](http://163.30.43.15/ShowProblem?problemid=a033) | [hello, world](http://163.30.43.15/ShowProblem?problemid=a033) |
| [a013](http://163.30.43.15/ShowProblem?problemid=a013) | [You can say that again!](http://163.30.43.15/ShowProblem?problemid=a013) |

### 課堂作業：算術運算
| 題號 | 題目 |
| --- | --- |
| [a014](http://163.30.43.15/ShowProblem?problemid=a014) | [中華民國萬歲！](http://163.30.43.15/ShowProblem?problemid=a014) |
| [a046](http://163.30.43.15/ShowProblem?problemid=a046) | [簡單讀取](http://163.30.43.15/ShowProblem?problemid=a046) |
| [a048](http://163.30.43.15/ShowProblem?problemid=a048) | [攝氏轉華氏](http://163.30.43.15/ShowProblem?problemid=a048) |
| [a049](http://163.30.43.15/ShowProblem?problemid=a049) | [二數相加](http://163.30.43.15/ShowProblem?problemid=a049) |
| [a124](http://163.30.43.15/ShowProblem?problemid=a124) | [累加數字](http://163.30.43.15/ShowProblem?problemid=a124) |

### 基礎練習題

| 題號 | 題目 | 來源／備註 |
| --- | --- | --- |
| [a050](http://163.30.43.15/ShowProblem?problemid=a050) | [求矩形面積](http://163.30.43.15/ShowProblem?problemid=a050) | |
| [a056](http://163.30.43.15/ShowProblem?problemid=a056) | [整數商餘](http://163.30.43.15/ShowProblem?problemid=a056) | `//` 與 `%` |
| [a019](http://163.30.43.15/ShowProblem?problemid=a019) | [0 與 1](http://163.30.43.15/ShowProblem?problemid=a019) | 板橋高中教學題 |
| [a071](http://163.30.43.15/ShowProblem?problemid=a071) | [兩個數字的七種算術運算](http://163.30.43.15/ShowProblem?problemid=a071) | |
| [a072](http://163.30.43.15/ShowProblem?problemid=a072) | [計算圓面積](http://163.30.43.15/ShowProblem?problemid=a072) | |
| [a054](http://163.30.43.15/ShowProblem?problemid=a054) | [長寬高算體積](http://163.30.43.15/ShowProblem?problemid=a054) | arping瘋狂程設 |
| [a070](http://163.30.43.15/ShowProblem?problemid=a070) | [換匯：台幣換美金](http://163.30.43.15/ShowProblem?problemid=a070) | |
| [a015](http://163.30.43.15/ShowProblem?problemid=a015) | [妳那裡現在幾點了？](http://163.30.43.15/ShowProblem?problemid=a015) | |
| [a042](http://163.30.43.15/ShowProblem?problemid=a042) | [買鉛筆](http://163.30.43.15/ShowProblem?problemid=a042) | 板橋高中教學題 |
| [a076](http://163.30.43.15/ShowProblem?problemid=a076) | [定期儲蓄存款之整存整付：單利計算](http://163.30.43.15/ShowProblem?problemid=a076) | |
| [a075](http://163.30.43.15/ShowProblem?problemid=a075) | [段考加權平均計算程式](http://163.30.43.15/ShowProblem?problemid=a075) | |
| [a077](http://163.30.43.15/ShowProblem?problemid=a077) | [自動販賣機之找零程式](http://163.30.43.15/ShowProblem?problemid=a077) | |
| [a029](http://163.30.43.15/ShowProblem?problemid=a029) | [分組報告](http://163.30.43.15/ShowProblem?problemid=a029) | |
| [a035](http://163.30.43.15/ShowProblem?problemid=a035) | [伏林的三角地](http://163.30.43.15/ShowProblem?problemid=a035) | 海龍公式 |

## 第二類：條件判斷（

**這一類的關鍵是「分支」：同一批輸入，走不同的路。** 練 `if`／`elif`／`else`、大小比較、以及像「大月小月」「畢氏數」這種要分情況討論的題目。

### 課堂作業

| 題號 | 題目 |
| --- | --- |
| [a024](http://163.30.43.15/ShowProblem?problemid=a024) | [該減肥了！](http://163.30.43.15/ShowProblem?problemid=a024) |
| [a031](http://163.30.43.15/ShowProblem?problemid=a031) | [山六九之旅](http://163.30.43.15/ShowProblem?problemid=a031) |
| [a061](http://163.30.43.15/ShowProblem?problemid=a061) | [成績分級 1](http://163.30.43.15/ShowProblem?problemid=a061) |
| [a055](http://163.30.43.15/ShowProblem?problemid=a055) | [計算工讀生薪水 1](http://163.30.43.15/ShowProblem?problemid=a055) |

### 基礎練習題

| 題號 | 題目 | 來源／備註 |
| --- | --- | --- |
| [a067](http://163.30.43.15/ShowProblem?problemid=a067) | [季節判斷](http://163.30.43.15/ShowProblem?problemid=a067) | arping瘋狂程設 |
| [a020](http://163.30.43.15/ShowProblem?problemid=a020) | [ㄑㄧˊ 數？](http://163.30.43.15/ShowProblem?problemid=a020) | 板橋高中教學題 |
| [a021](http://163.30.43.15/ShowProblem?problemid=a021) | [三人行必有我師](http://163.30.43.15/ShowProblem?problemid=a021) | 板橋高中教學題 |
| [a051](http://163.30.43.15/ShowProblem?problemid=a051) | [計算BMI](http://163.30.43.15/ShowProblem?problemid=a051) | arping瘋狂程設 |
| [a060](http://163.30.43.15/ShowProblem?problemid=a060) | [計算工讀生薪水 2](http://163.30.43.15/ShowProblem?problemid=a060) | 2020wwonsssh |
| [a062](http://163.30.43.15/ShowProblem?problemid=a062) | [成績分級2](http://163.30.43.15/ShowProblem?problemid=a062) | 2020wwonsssh |
| [a063](http://163.30.43.15/ShowProblem?problemid=a063) | [求最大值](http://163.30.43.15/ShowProblem?problemid=a063) | 2020wwonsssh |
| [a064](http://163.30.43.15/ShowProblem?problemid=a064) | [大月小月](http://163.30.43.15/ShowProblem?problemid=a064) | arping瘋狂程設 |
| [a065](http://163.30.43.15/ShowProblem?problemid=a065) | [畢氏數](http://163.30.43.15/ShowProblem?problemid=a065) | arping瘋狂程設 |
| [a066](http://163.30.43.15/ShowProblem?problemid=a066) | [奇偶數的判斷](http://163.30.43.15/ShowProblem?problemid=a066) | arping瘋狂程設 |
| [a022](http://163.30.43.15/ShowProblem?problemid=a022) | [上學去吧！](http://163.30.43.15/ShowProblem?problemid=a022) | 板橋高中教學題 |
| [a079](http://163.30.43.15/ShowProblem?problemid=a079) | [百貨公司滿額折扣](http://163.30.43.15/ShowProblem?problemid=a079) | |
| [a081](http://163.30.43.15/ShowProblem?problemid=a081) | [停車費計算](http://163.30.43.15/ShowProblem?problemid=a081) | |
| [a082](http://163.30.43.15/ShowProblem?problemid=a082) | [判斷是否會被留級](http://163.30.43.15/ShowProblem?problemid=a082) | |
| [a083](http://163.30.43.15/ShowProblem?problemid=a083) | [判斷成績是否及格](http://163.30.43.15/ShowProblem?problemid=a083) | |
| [a080](http://163.30.43.15/ShowProblem?problemid=a080) | [輸入身分證字號，檢查字串長度以及判斷性別](http://163.30.43.15/ShowProblem?problemid=a080) | 字串長度 |
| [a023](http://163.30.43.15/ShowProblem?problemid=a023) | [文文的求婚--續集（1 行版）](http://163.30.43.15/ShowProblem?problemid=a023) | 板橋高中教學題 |

## 第三類：迴圈

**這一類要你把同樣的動作重複很多次。** 前半練 `for` 與固定次數的重複，後半練 `while`、巢狀迴圈，以及質數、最大公因數、費氏數列這類經典題。

| 題號 | 題目 | 備註 |
| --- | --- | --- |
| [a025](http://163.30.43.15/ShowProblem?problemid=a025) | [文文的求婚--續集（n 行版）](http://163.30.43.15/ShowProblem?problemid=a025) | 用 a023 的 1 行版改寫 |
| [a028](http://163.30.43.15/ShowProblem?problemid=a028) | [文文的求婚--續集（Case 版）](http://163.30.43.15/ShowProblem?problemid=a028) | 用 a023 的 1 行版改寫，可用 `str()` 把整數變成文字 |
| [a038](http://163.30.43.15/ShowProblem?problemid=a038) | [我不說髒話](http://163.30.43.15/ShowProblem?problemid=a038) | 板橋高中教學題 |
| [a101](http://163.30.43.15/ShowProblem?problemid=a101) | [尋找2或7的倍數](http://163.30.43.15/ShowProblem?problemid=a101) | |
| [a092](http://163.30.43.15/ShowProblem?problemid=a092) | [跟同學說哈囉](http://163.30.43.15/ShowProblem?problemid=a092) | |
| [a097](http://163.30.43.15/ShowProblem?problemid=a097) | [攝氏華氏對照表](http://163.30.43.15/ShowProblem?problemid=a097) | |
| [a093](http://163.30.43.15/ShowProblem?problemid=a093) | [顯示99乘法表中的某個區塊](http://163.30.43.15/ShowProblem?problemid=a093) | |
| [a099](http://163.30.43.15/ShowProblem?problemid=a099) | [顯示99乘法表](http://163.30.43.15/ShowProblem?problemid=a099) | 需使用巢狀迴圈 |
| [a094](http://163.30.43.15/ShowProblem?problemid=a094) | [星星直角三角形](http://163.30.43.15/ShowProblem?problemid=a094) | 需使用巢狀迴圈 |
| [a096](http://163.30.43.15/ShowProblem?problemid=a096) | [星星等腰三角形](http://163.30.43.15/ShowProblem?problemid=a096) | 需使用巢狀迴圈 |
| [a088](http://163.30.43.15/ShowProblem?problemid=a088) | [最大公因數](http://163.30.43.15/ShowProblem?problemid=a088) | wwon；建議使用 `while` 條件迴圈；講解影片 |
| [a104](http://163.30.43.15/ShowProblem?problemid=a104) | [小蝸要離開了](http://163.30.43.15/ShowProblem?problemid=a104) | 一定要用 `while` 條件迴圈 |
| [a030](http://163.30.43.15/ShowProblem?problemid=a030) | [電腦教室](http://163.30.43.15/ShowProblem?problemid=a030) | 板橋高中教學題；講解影片 |
| [a089](http://163.30.43.15/ShowProblem?problemid=a089) | [質數判別](http://163.30.43.15/ShowProblem?problemid=a089) | wwon；講解影片 |
| [a095](http://163.30.43.15/ShowProblem?problemid=a095) | [費氏數列](http://163.30.43.15/ShowProblem?problemid=a095) | 講解影片 |
| [a098](http://163.30.43.15/ShowProblem?problemid=a098) | [1到n的所有質數](http://163.30.43.15/ShowProblem?problemid=a098) | 需使用巢狀迴圈 |
| [a039](http://163.30.43.15/ShowProblem?problemid=a039) | [小明的作業](http://163.30.43.15/ShowProblem?problemid=a039) | 板橋高中教學題 |
| [a090](http://163.30.43.15/ShowProblem?problemid=a090) | [因數分解](http://163.30.43.15/ShowProblem?problemid=a090) | 使用 `while` |

## 第四類：串列與字串

**這一類要你學習基本串列與字串功能。** 如何把資料轉換成串列，串列如何與迴圈結合，還有Python的文字切片法。

| 題號 | 題目 | 備註 |
| --- | --- | --- |
| [a119](http://163.30.43.15/ShowProblem?problemid=a119) | [薩爾達傳說](http://163.30.43.15/ShowProblem?problemid=a119) | |
| [a120](http://163.30.43.15/ShowProblem?problemid=a120) | [薩爾達傳說之武器資料庫](http://163.30.43.15/ShowProblem?problemid=a120) | |
| [a110](http://163.30.43.15/ShowProblem?problemid=a110) | [氣泡排序練習](http://163.30.43.15/ShowProblem?problemid=a110) | 需用巢狀迴圈及 `if`，不可使用 `sort` |
| [a107](http://163.30.43.15/ShowProblem?problemid=a107) | [求百數的最大值](http://163.30.43.15/ShowProblem?problemid=a107) | |
| [a122](http://163.30.43.15/ShowProblem?problemid=a122) | [壽山動物園](http://163.30.43.15/ShowProblem?problemid=a122) | |
| [a010](http://163.30.43.15/ShowProblem?problemid=a010) | [聖經密碼](http://163.30.43.15/ShowProblem?problemid=a010) | |
| [a126](http://163.30.43.15/ShowProblem?problemid=a126) | [倒過來唸的句子](http://163.30.43.15/ShowProblem?problemid=a126) | |

## 第五類：綜合題

**這一類是綜合練習題，可放最後再嘗試。**

| 題號 | 題目 | 備註 |
| --- | --- | --- |
| [a008](http://163.30.43.15/ShowProblem?problemid=a008) | [盈虧互補](http://163.30.43.15/ShowProblem?problemid=a008) | |
| [a043](http://163.30.43.15/ShowProblem?problemid=a043) | [棄保效應](http://163.30.43.15/ShowProblem?problemid=a043) | |
| [a002](http://163.30.43.15/ShowProblem?problemid=a002) | [電話客服中心](http://163.30.43.15/ShowProblem?problemid=a002) | 板橋高中教學題 |


## 建議練習順序怎麼排？

1. **先寫第一類的課堂作業**（a033、a007、a012、a013）：這 4 題只是把指定文字印出來，先確認你的程式跑得起來、評測系統會過。
2. **再寫第一類的算術運算**（a014、a046、a048、a049、a124）：練會 `input()` 讀數字與四則運算。
3. **接第一類的基礎練習題**：從 a049／a050 這種單純算式的，一路寫到 a075、a077 這種要讀多筆資料的。
4. **進第二類**：先寫課堂作業 a024、a031、a061、a055，再往下寫到 a080 這種字串判斷。
5. **攻第三類**：先 a092、a097 這種單層迴圈，再挑 a099、a094、a096 巢狀迴圈，最後處理 a088、a089、a095、a098 這些經典迴圈題。
6. **最後練習第四類**：練習操作串列與字串的基本功能

**卡關超過 20 分鐘就先跳過、寫下一題**，過一兩天回頭往往就通了；真的解不出來再回去複習觀念文章，例如 [APCS 初級實作考前複習](https://vanix.github.io/2026/07/apcs_basic_level_review.html)。

## 常見問題（FAQ）

### APCS 初級前的基礎題單總共幾類題型？

**共四大類**：第一類輸入輸出與算術運算、第二類條件判斷、第三類迴圈、第四類字串與串列。

### 這些題目要去哪裡寫？

到評測系統 `http://163.30.43.15/ShowProblem?problemid=題號`，把題號換成例如 `a050` 即可。本篇每一列的題號與題目都已做好超連結，不用手動改網址。

### 第一類的課堂作業是哪幾題？

**輸入與輸出**：a007、a012、a033、a013；**算術運算**：a014、a046、a048、a049、a124。第二類條件判斷的課堂作業則是 a024、a031、a061、a055。

### 題目說「需使用巢狀迴圈」是評測系統會檢查嗎？

不會。**那是對寫法的要求**，目的是逼你練到那個觀念（例如 a099、a094、a096、a098），評測系統只比對輸出結果。同理 a104 指定一定要用 `while`、a088 建議用 `while`，也是針對練習方向的提醒。

---

還沒有基礎的同學，可以到[文章分類](https://vanix.github.io/categories/%E7%A8%8B%E5%BC%8F%E6%95%99%E5%AD%B8/)裡觀看教學文章跟教學影片。練到需要完整APCS初級解題示範時，可以看 [APCS 初級 遊戲選角解題教學](https://vanix.github.io/2026/10/apcs-game-character-selection.html) 與 [APCS 初級 裝飲料解題教學](https://vanix.github.io/2026/10/apcs-o711-pour-drink.html)，兩篇都有逐行程式碼講解。
