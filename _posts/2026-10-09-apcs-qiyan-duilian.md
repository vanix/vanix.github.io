---
author: 歐巴計概
date: 2026-10-09 09:00:00 +0800
layout: post
permalink: /2026/10/apcs-qiyan-duilian.html
title: APCS初級 七言對聯解題教學｜Python 三規則檢查與程式實作
description: "APCS 初級實作 2021 年 9 月第一題「七言對聯」完整解題教學。用 Python 判斷二四不同二六同、仄起平收、同聯相對三條規則，並依序輸出違規規則字母、全對輸出 None。含輸入格式、解題思路、逐行程式碼講解、範例走讀與常見錯誤，適合學會條件、迴圈、串列後挑戰 APCS 初級的同學，看完就能自己動手寫出解答。"
categories: [資訊教學, 程式教學]
tags: [Python, APCS, 程式教學, 七言對聯, ZeroJudge, 迴圈, 條件判斷, 實作初級]
image:
  path: /assets/images/cover/apcs-qiyan-duilian.png
  alt: APCS 初級七言對聯解題教學封面，用 Python 檢查平仄三規則
---

💡 APCS 初級解題重點

這篇是 APCS 初級實作範例「七言對聯」的解題教學，用 Python 檢查對聯平仄的三條規則（二四不同二六同、仄起平收、同聯相對），並依序輸出違規的規則字母。

[APCS教學文章列表](https://vanix.github.io/categories/%E7%A8%8B%E5%BC%8F%E6%95%99%E5%AD%B8/)

[APCS實作線上課程](https://www.youtube.com/playlist?list=PLN9g1rvyo05p70K3HU-hWhEkoNs26WhD0)

[ZeroJudge 七言對聯 題目連結](https://zerojudge.tw/ShowProblem?problemid=g275){:target="_blank"}

<iframe width="560" height="315"
        src="https://www.youtube.com/embed/Ooy1F6ye2Yo"
        title="APCS初級 七言對聯解題教學影片"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

## 七言對聯這題在考什麼？

**七言對聯要你用程式檢查每首對聯的平仄是否符合「二四不同二六同」「仄起平收」「同聯相對」三條規則，並把違反的規則字母列出來；三條都符合就輸出 None。**

這是 APCS 程式實作初級 2021 年 9 月範例的第一題（ZeroJudge 編號 [g275](https://zerojudge.tw/ShowProblem?problemid=g275){:target="_blank"}），也是典型的「讀資料 → 條件判斷 → 依結果輸出」題型。

> **先備能力**：建議先學會 **條件判斷（if/else）**、**迴圈（for）** 與一點點 **串列（list／倉庫）** 再來挑戰。這些基礎可以看 [APCS初級 Python基礎文章](https://vanix.github.io/categories/%E7%A8%8B%E5%BC%8F%E6%95%99%E5%AD%B8/)，練過迴圈與串列的練習題後再回來這題會順很多。
{: .prompt-tip }

## 輸入格式怎麼看？

中文字依發音分平聲與仄聲，題目用 **0 代表平聲、1 代表仄聲**。一個七言對聯有兩句，每句恰好七個字。

輸入規則如下：

| 欄位 | 內容 | 說明 |
| --- | --- | --- |
| 第 1 行 | 一個正整數 `n` | 有幾首對聯（也是迴圈要跑幾次） |
| 之後 `2n` 行 | 每行 7 個 0/1 | 每兩行是一首對聯：第一行第一句，第二行第二句 |

![APCS 初級七言對聯題目示意：每首兩句、每句七字，0代表平聲、1代表仄聲](/assets/images/blog/apcs-qiyan-duilian/01-problem-overview.png){: .normal}
_題目示意圖：每一句有七個字，用 0（平聲）與 1（仄聲）表示。_

## 三條規則一次看懂

題目要檢查的三條規則，是整題的核心邏輯：

### 規則 A：二四不同二六同

**每一句的第二個字與第四個字的平仄要不同，第二個字與第六個字的平仄要相同。** 兩句都要檢查。

以程式索引來說，句子的第二、四、六個字（人類數的第 2、4、6 個）其實是索引 `1`、`3`、`5`，因為索引從 `0` 開始。

- 第二字（索引 1）≠ 第四字（索引 3）
- 第二字（索引 1）= 第六字（索引 5）

![七言對聯規則A 二四不同二六同示意](/assets/images/blog/apcs-qiyan-duilian/02-rule-a-24-diff-26-same.png){: .normal}
_規則 A：二四不同、二六相同，兩句都要成立。_

### 規則 B：仄起平收

**第一句的最後一個字（第七字）必須是仄聲（1），第二句的最後一個字必須是平聲（0）。**

「仄起平收」講的是收尾：第一句收在仄聲，第二句收在平聲。程式上只要看兩句的索引 `6`。

![七言對聯規則B 仄起平收示意](/assets/images/blog/apcs-qiyan-duilian/03-rule-b-zeqi-pingshou.png){: .normal}
_規則 B：第一句第七字為仄聲(1)、第二句第七字為平聲(0)。_

### 規則 C：同聯相對

**第一句的第二、四、六個字，平仄要分別與第二句的第二、四、六個字相反。** 也就是同一位置上下兩句必須「相對」。

- 第一句索引 1 ≠ 第二句索引 1
- 第一句索引 3 ≠ 第二句索引 3
- 第一句索引 5 ≠ 第二句索引 5

![七言對聯規則C 同聯相對示意](/assets/images/blog/apcs-qiyan-duilian/04-rule-c-couplet-opposite.png){: .normal}
_規則 C：上下兩句在第二、四、六字必須剛好相反。_

## 輸出要怎麼寫？

**依規則筆畫順序，把「有違反」的規則字母 A、B、C 連在一起印出來（中間不換行）；如果三個規則都符合，就輸出 `None`。** 每一首對聯印出一行結果。

| 情況 | 輸出 |
| --- | --- |
| 只違反規則 A | `A` |
| 違反 A 與 C | `AC` |
| 三條全違反 | `ABC` |
| 三條全符合 | `None` |

![七言對聯輸出解說：依序印出違規規則字母，全對輸出 None](/assets/images/blog/apcs-qiyan-duilian/05-output-explanation.png){: .normal}
_輸出規則：違規字母依序排列且不換行，全對輸出 None。_

## 解題思路：一輪迴圈抓兩句、三個 if、一個計數器

整題的骨架其實很固定，就是「**跑 n 次的外層迴圈**，每次都**讀兩句**，再用**三個 if** 分別檢查 A、B、C」：

1. 讀 `n`，決定迴圈跑幾次。
2. 迴圈內讀兩行，各自 `split()` 成一個「文字倉庫」（串列）。
3. 用三個 `if` 檢查 A、B、C。
4. 條件**不符合**就把對應字母用 `print(..., end="")` 接在後面。
5. 另外用一個計數器記錄「符合幾個規則」，等都檢查完後，若等於 3 就補印 `None`。
6. 每首對聯印完，補一個 `print()` 換行，換到下一首。

> **為什麼要用計數器？** 因為只有「不符合」的規則才會被印出來，若三條都符合，畫面會是空白。我們需要計數器判斷「是不是三個都通過」，才能補印 `None`。
{: .prompt-info }

## Python 程式碼逐步講解

先看完整程式碼，再逐段拆解：

```python
n = int(input())

for i in range(n):
    s1 = input().split()
    s2 = input().split()
    cnt = 0

    # 規則 A：二四不同、二六相同（兩句都要）
    if s1[1] != s1[3] and s1[1] == s1[5] and s2[1] != s2[3] and s2[1] == s2[5]:
        cnt += 1
    else:
        print("A", end="")

    # 規則 B：仄起平收
    if s1[6] == "1" and s2[6] == "0":
        cnt += 1
    else:
        print("B", end="")

    # 規則 C：同聯相對
    if s1[1] != s2[1] and s1[3] != s2[3] and s1[5] != s2[5]:
        cnt += 1
    else:
        print("C", end="")

    if cnt == 3:
        print("None", end="")

    print()
```

### 讀入資料

```python
n = int(input())
for i in range(n):
    s1 = input().split()
    s2 = input().split()
```

先讀 `n` 決定有幾首對聯。每次迴圈讀兩行，用 `split()` 以空白切開，變成文字倉庫。因為每個字都是 `0` 或 `1` 的**文字**，之後比較時記得用引號，例如 `s1[6] == "1"`。

### 規則 A

```python
if s1[1] != s1[3] and s1[1] == s1[5] and s2[1] != s2[3] and s2[1] == s2[5]:
    cnt += 1
else:
    print("A", end="")
```

四個條件用 `and` 串起來：`s1` 要二四不同、二六相同，`s2` 也要二四不同、二六相同。全部成立才算通過 A。

### 規則 B

```python
if s1[6] == "1" and s2[6] == "0":
    cnt += 1
else:
    print("B", end="")
```

第一句第七字（索引 6）要是 `"1"`（仄聲），第二句第七字要是 `"0"`（平聲）。

### 規則 C

```python
if s1[1] != s2[1] and s1[3] != s2[3] and s1[5] != s2[5]:
    cnt += 1
else:
    print("C", end="")
```

上下兩句在第二、四、六字都必須不同。

### 輸出 None 與換行

```python
if cnt == 3:
    print("None", end="")

print()
```

三個規則都符合時 `cnt` 會是 3，補印 `None`。因為前面 A、B、C 都用 `end=""` 不換行，最後用 `print()` 補上換行，才能正確換到下一首對聯。

## 範例輸出走讀

以題目的第二個範例（`n = 3`）來走一遍，輸出應該是 `None`、`AB`、`ABC`：

輸入：

```
3
0 1 0 0 0 1 1
1 0 1 1 1 0 0
0 1 0 1 1 1 0
1 0 0 0 0 0 1
0 1 0 0 1 1 1
1 0 0 0 0 1 1
```

輸出：

```
None
AB
ABC
```

第一首兩句在三條規則都符合 → `None`；第二首違反 A 與 B → `AB`；第三首三條都違反 → `ABC`。

## 常見錯誤與除錯

- **索引從 0 開始**：題目的「第二個字」是索引 `1`、「第七個字」是索引 `6`，不要直接寫成 `s1[2]`。
- **文字比較要加引號**：`s1[6] == "1"` 才是比文字，漏了引號就變成跟數字比，永遠不成立。
- **忘記印 None**：只有違規才會印出字母，三條全過若不補印 `None`，答案會空白。
- **`end=""` 與換行**：A、B、C 之間不能換行，最後記得補一個 `print()`。
- **記得 `.split()`**：輸入是一行七個數字，要切開才抓得到每一個字。

## 常見問題（FAQ）

### 平聲和仄聲用什麼代表？

題目用 **0 代表平聲、1 代表仄聲**，輸入的每個字都是 0 或 1。因為讀進來是文字，比大小時要寫成 `s1[6] == "1"` 這種字串比較。

### 「二四不同二六同」是什麼意思？

每個句子的第二字與第四字平仄要**不同**，第二字與第六字平仄要**相同**，而且**兩句都要**符合。程式上是檢查 `s1[1] != s1[3]`、`s1[1] == s1[5]`，`s2` 也一樣。

### 為什麼全部符合要輸出 None，不是空的？

題目規定違反的規則才列出來，若三條都沒違反，正確答案就是輸出 `None`。所以要用一個計數器記「通過幾個規則」，等於 3 時補印 `None`。

### 這題適合什麼程度的學生？

適合已經學會條件判斷、迴圈與基本串列操作的同學，是 APCS 初級實作的入門練習題。可以先用 [APCS 初級實作考前複習](https://vanix.github.io/2026/07/apcs_basic_level_review.html)暖身，再回來寫這題。

---

還沒有基礎的同學，可以到[文章分類](https://vanix.github.io/categories/%E7%A8%8B%E5%BC%8F%E6%95%99%E5%AD%B8/)裡觀看教學文章跟教學影片，記得看完要寫作業。有基礎後再來寫這題，寫完可以到 [ZeroJudge g275](https://zerojudge.tw/ShowProblem?problemid=g275){:target="_blank"} 送出測驗，確認自己的程式邏輯沒有問題。
