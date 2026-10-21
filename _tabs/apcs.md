---
layout: apcs
title: APCS教學專區
heading: APCS教學專區｜Python 基礎題 、考古題與線上刷題
seo_title: APCS教學專區｜Python 基礎題 、考古題與線上刷題 - 充滿意外的宅爸人生
subtitle: 從 0 開始的 Python 程式設計・各階段學習地圖
icon: fab fa-python
order: 4.5
permalink: /apcs/
description: "APCS教學專區一次整理：基本題庫、APCS 歷屆實作題庫、解題文章，以及一張照順序練的學習地圖。題庫每一題都連到線上評測系統，點題號就能直接寫。題目來自壽山高中解題網、ZeroJudge 與 TCIRC 串中電研OJ，可依類別、觀念、評測網站篩選，適合準備 APCS 初級／中級實作題的學生自學，也能當老師派作業的題庫。"
---

{% assign all_classes = site.data.apcs_problems.classes %}
{% assign total = 0 %}
{% for c in all_classes %}{% for g in c.groups %}{% assign total = total | plus: g.problems.size %}{% endfor %}{% endfor %}

這個專區包含：**基本題庫**、**APCS 歷屆實作題庫**、**解題文章**、以及一張**照順序練的學習地圖**。題庫每一題都連到評測系統，點題號就能直接寫，不用另外找網址。

<div class="apcs-cards">
{% for c in all_classes %}{% if c.id != 'extra' %}
  <div class="apcs-card">
    <div class="apcs-card-meta">{{ c.level }}</div>
    <h3>{{ c.name }}</h3>
    <p class="apcs-note">{{ c.desc }}</p>
    <p><a href="{{ '/apcs/problem-bank/' | relative_url }}">到題庫挑題 →</a></p>
  </div>
{% endif %}{% endfor %}
  <div class="apcs-card">
    <div class="apcs-card-meta">壽山高中解題網 + ZeroJudge + TCIRC</div>
    <h3>基本題庫</h3>
    <p class="apcs-note">初級三大類（輸入輸出／條件判斷／迴圈）加上字串、前綴和、二維陣列與演算法，可依觀念、評測網站與關鍵字篩選。</p>
    <p><a href="{{ '/apcs/problem-bank/' | relative_url }}">進入基本題庫 →</a></p>
  </div>
  <div class="apcs-card">
    <div class="apcs-card-meta">ZeroJudge</div>
    <h3>APCS 歷屆實作題庫</h3>
    <p class="apcs-note">初級、中級、中高級、高級四個等級的歷屆實作題，附考試場次、通過率與對應解題文章。</p>
    <p><a href="{{ '/apcs/exam-bank/' | relative_url }}">進入歷屆實作題庫 →</a></p>
  </div>
  <div class="apcs-card">
    <div class="apcs-card-meta">學習路徑</div>
    <h3>不知道從哪題開始？</h3>
    <p class="apcs-note">照七個階段的順序練，從「印出字串」一路到「函數與遞迴」，不跳級、不漏觀念。</p>
    <p><a href="{{ '/apcs/roadmap/' | relative_url }}">看學習地圖 →</a></p>
  </div>
</div>

## 基本題庫怎麼用？

基本題庫在 **[{{ '/apcs/problem-bank/' | relative_url }}](/apcs/problem-bank/)**，來自**壽山高中解題網**、**ZeroJudge** 與 **TCIRC 串中電研OJ**，分成五大類。頁面上可以直接：

- 用搜尋框找題號或題名（打 `a050` 或「面積」都找得到）
- 按**類別**、**觀念**（算術運算／條件判斷／while 迴圈…）、**評測網站**篩選
- 每題都附**命題來源**（板橋高中教學題、arping瘋狂程設、wwon…）與**寫法要求**（需巢狀迴圈、一定要用 while）

評測系統網址格式：壽山是 `http://163.30.43.15/ShowProblem?problemid=a001`，ZeroJudge 是 `https://zerojudge.tw/ShowProblem?problemid=o711`，TCIRC 是 `https://judge.tcirc.tw/problem/d010`。題號後面的標籤會標示來源網站。

## 歷屆實作題解題文章

這部分是 ZeroJudge 上 APCS 實作題的完整解題教學，每篇都有逐行程式碼講解、範例走讀與常見錯誤整理。

{% assign featured = site.data.apcs_featured %}
<ul>
{% for post in site.posts %}
  {% if featured contains post.url %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span class="apcs-note">（{{ post.date | date: "%Y-%m-%d" }}）</span>
  </li>
  {% endif %}
{% endfor %}
</ul>

<details>
  <summary>其他 APCS 相關文章（課程筆記、升學與學習規劃）</summary>
  <ul>
  {% for post in site.posts %}
    {% if post.tags contains 'APCS' %}
      {% unless featured contains post.url %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
      {% endunless %}
    {% endif %}
  {% endfor %}
  </ul>
</details>

> 還沒寫過任何一行程式？先看 [APCS 初級 遊戲選角解題教學]({{ '/2026/10/apcs-game-character-selection.html' | relative_url }}) 與 [APCS 初級 七言對聯解題教學]({{ '/2026/10/apcs-qiyan-duilian.html' | relative_url }})，把讀資料與條件判斷練熟再回來刷題庫。

## 這個專區的四件事

| 內容 | 形式 | 適合誰 |
| --- | --- | --- |
| 基本題庫（壽山 + ZeroJudge + TCIRC） | 可篩選表格，每題連到評測系統 | 想用零散時間刷題的學生 |
| APCS 歷屆實作題庫（ZeroJudge） | 四個等級 + 考試場次與通過率 | 想考正式題、想知道難度的人 |
| 歷屆實作題解題 | 逐行講解的長文章 | 需要有人帶著讀程式碼的人 |
| 學習地圖 | 七階段順序 + 可點擊的題號清單 | 不知道自己該練哪題的人 |

💡 題庫的資料放在 `_data/apcs_problems.yml`，**新增題目只要加一行 YAML，頁面會自動更新**，不用回頭改 HTML。
