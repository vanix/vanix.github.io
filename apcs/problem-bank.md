---
layout: apcs
title: 基本題庫
subtitle: 壽山高中解題網 + ZeroJudge + TCIRC 共 87 題・可依類別、觀念與評測網站篩選
permalink: /apcs/problem-bank/
description: "APCS 基本題庫 86 題：壽山高中解題網的輸入輸出與算術運算 23 題、條件判斷 21 題、迴圈 18 題，加上進階的字串 3 題、前綴和 2 題、二維陣列 5 題，以及搜尋、堆疊、遞迴、枚舉與組合等演算法 14 題。每題附線上評測連結、命題來源與寫法要求，可依類別、觀念、評測網站與關鍵字篩選，適合從零開始學 Python 的學生逐題練習。"
---

{% assign all_classes = site.data.apcs_problems.classes %}
{% assign sites = site.data.apcs_problems.sites %}
{% assign topics = "" | split: "" %}
{% assign site_list = "" | split: "" %}
{% for c in all_classes %}{% for g in c.groups %}{% for p in g.problems %}{% assign topics = topics | push: p.topic %}{% assign site_list = site_list | push: p.site %}{% endfor %}{% endfor %}{% endfor %}
{% assign topics = topics | uniq %}
{% assign site_list = site_list | uniq %}
{% assign total = 0 %}{% for c in all_classes %}{% for g in c.groups %}{% assign total = total | plus: g.problems.size %}{% endfor %}{% endfor %}

這份**基本題庫**收錄 **{{ total }} 題**，分成五大類：輸入輸出與算術運算 23 題、條件判斷 21 題、迴圈 18 題，進階的**字串、前綴和與二維陣列** 10 題，以及**搜尋、堆疊、遞迴、枚舉與組合**等演算法 14 題。

題目來自三個評測網站：**壽山高中解題網**（初級課程題）、**ZeroJudge**（前綴和、二維陣列、演算法等進階題）與 **TCIRC 串中電研OJ**（例題與競賽題）。**每一列的題號與題名都連到對應的評測系統**，點了就能直接寫；題號後面的標籤會標示這題來自哪個網站。

> 另有「APCS 題庫」收錄 ZeroJudge 上的歷屆實作題，會是獨立的一頁；基本題庫裡也會逐步加入 ZeroJudge 的題目，到時會多一個「評測網站」篩選可以切換。

<div class="apcs-tools">
  <input id="apcs-q" class="apcs-search" type="search" placeholder="搜尋題號或題名，例如 a050、面積、BMI">
  <div class="apcs-chips">
    <span class="apcs-chips-label">類別</span>
    <button class="apcs-chip active" data-filter="class" data-value="all">全部</button>
    {% for c in all_classes %}
      <button class="apcs-chip" data-filter="class" data-value="{{ c.id }}">{{ c.name }}</button>
    {% endfor %}
  </div>
  <div class="apcs-chips">
    <span class="apcs-chips-label">觀念</span>
    <button class="apcs-chip active" data-filter="topic" data-value="all">全部</button>
    {% for t in topics %}
      <button class="apcs-chip" data-filter="topic" data-value="{{ t }}">{{ t }}</button>
    {% endfor %}
  </div>
  <div class="apcs-chips">
    <span class="apcs-chips-label">評測網站</span>
    <button class="apcs-chip active" data-filter="site" data-value="all">全部</button>
    {% for s in site_list %}
      <button class="apcs-chip" data-filter="site" data-value="{{ s }}">{{ sites[s].name }}</button>
    {% endfor %}
  </div>
  <div class="apcs-chips">
    <label class="apcs-chip" style="cursor:pointer">
      <input type="checkbox" id="apcs-solved" style="vertical-align:-1px;margin-right:.3rem"> 只看有解題文章的題目
    </label>
  </div>
</div>

<div class="apcs-count" id="apcs-count">共 {{ total }} 題</div>

<div class="apcs-table-wrap">
<table class="apcs-table">
  <thead>
    <tr>
      <th style="width:7rem">題號</th>
      <th>題目</th>
      <th style="width:7rem">觀念</th>
      <th style="width:8rem">命題來源</th>
      <th style="width:8rem">解題文章</th>
    </tr>
  </thead>
  {% for c in all_classes %}
    {% for g in c.groups %}
      <tbody class="apcs-group" data-class="{{ c.id }}">
        <tr class="apcs-group-row"><td colspan="5">{{ c.name }}｜{{ g.name }}{% if g.note and g.note != '' %} <span class="apcs-note">（{{ g.note }}）</span>{% endif %}</td></tr>
        {% for p in g.problems %}
        <tr class="apcs-problem-row"
            data-class="{{ c.id }}"
            data-topic="{{ p.topic }}"
            data-site="{{ p.site }}"
            data-search="{{ p.id }} {{ p.title }} {{ p.source }} {{ p.note }} {{ sites[p.site].name }}"
            data-solution="{% if p.solution and p.solution != '' %}1{% else %}0{% endif %}">
          <td class="apcs-id"><a href="{{ p.judge }}" target="_blank" rel="noopener" title="{{ sites[p.site].name }} {{ p.id }}．{{ p.title }}">{{ p.id }}</a> <span class="apcs-site-tag apcs-site-{{ p.site }}">{{ sites[p.site].short }}</span></td>
          <td><a href="{{ p.judge }}" target="_blank" rel="noopener">{{ p.title }}</a>{% if p.note != '' %} <span class="apcs-note">（{{ p.note }}）</span>{% endif %}</td>
          <td><span class="apcs-tag">{{ p.topic }}</span></td>
          <td class="apcs-note">{{ p.source }}</td>
          <td class="apcs-solution">{% if p.solution and p.solution != '' %}<a href="{{ p.solution | relative_url }}">看解題 →</a>{% else %}<span class="apcs-note">—</span>{% endif %}</td>
        </tr>
        {% endfor %}
      </tbody>
    {% endfor %}
  {% endfor %}
</table>
</div>

<p class="apcs-empty" id="apcs-empty" style="display:none">找不到符合條件的題目，換個關鍵字試試。</p>

{% include apcs-filter.html %}

> 題庫資料放在 `_data/apcs_problems.yml`，每新增一題只要加一組 YAML，這個頁面就會自動多出一列。評測網站已支援 **壽山高中解題網**與 **ZeroJudge** 兩種：把該題的 `site` 設成 `sssh` 或 `zjudge`、`judge` 填對應網址即可，上方的「評測網站」篩選會自動多出選項。
