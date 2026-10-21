---
layout: apcs
title: APCS 學習地圖
subtitle: 七個階段、68 題完整分配，題號可直接點去刷題
permalink: /apcs/roadmap/
description: "APCS 學習地圖：把題庫 68 題拆成七個階段——讓程式跑起來、算得動、會分支、會重複、迴圈應用、串列與字串、函數與遞迴，每個階段都附對應的教學文章與可直接點擊刷題的題號連結，不會不知道該從哪題開始。"
---

{% assign stages = site.data.apcs_roadmap %}
{% assign all_classes = site.data.apcs_problems.classes %}
{% assign all_count = 0 %}
{% for s in stages %}{% assign all_count = all_count | plus: s.problems.size %}{% endfor %}

不知道從哪一題下手？**照順序練就好**。這張地圖把題庫 {{ all_count }} 題拆成七個階段，每一階段都附上**對應的教學文章**與**可直接點擊去刷題的題號**。

> 前綴和、二維陣列與演算法共 18 題不在這條路徑裡（在[基本題庫](/apcs/problem-bank/)的進階分類），適合初級練完、有基礎之後再挑戰。

| 階段 | 主題 | 題數 | 核心觀念 |
| --- | --- | --- | --- |
{% for s in stages %}|{{ s.stage }}|{{ s.title }}|{{ s.problems.size }} 題|{% for t in s.topics %}{{ t }}{% unless forloop.last %}・{% endunless %}{% endfor %}|
{% endfor %}

<div class="apcs-stages">
{% for s in stages %}
  <section class="apcs-stage">
    <div class="apcs-stage-head">
      <div class="apcs-stage-no">階段 {{ s.stage }}</div>
      <h3>{{ s.title }}</h3>
      <p class="apcs-stage-goal">{{ s.goal }}</p>
      <div class="apcs-stage-topics">
        {% for t in s.topics %}<span class="apcs-tag">{{ t }}</span>{% endfor %}
      </div>
      <div class="apcs-note">本階段 {{ s.problems.size }} 題</div>
    </div>

    <div class="apcs-stage-body">
      <div class="apcs-stage-block">
        <h4>題目 <span class="apcs-note">點題號直接開啟評測系統</span></h4>
        <div class="apcs-ids">
          {% for pid in s.problems %}
            {% assign pkey = pid %}
            {% unless pid contains "-" %}
              {% assign pkey = s.site | default: "sssh" %}
              {% assign pkey = pkey | append: "-" | append: pid %}
            {% endunless %}
            {% assign judge = "" %}{% assign jtitle = "" %}{% assign jsite = "" %}{% assign jid = "" %}
            {% for c in all_classes %}{% for g in c.groups %}{% for p in g.problems %}
              {% if p.key == pkey %}{% assign judge = p.judge %}{% assign jtitle = p.title %}{% assign jsite = p.site %}{% assign jid = p.id %}{% endif %}
            {% endfor %}{% endfor %}{% endfor %}
            <a class="apcs-id-chip{% if jsite == 'zjudge' %} is-zjudge{% endif %}" href="{{ judge }}" target="_blank" rel="noopener" title="{{ jtitle }}">{{ jid }}</a>
          {% endfor %}
        </div>
      </div>

      <div class="apcs-stage-block">
        <h4>先看這幾篇</h4>
        <ul class="apcs-article-list">
          {% for a in s.articles %}
            <li><a href="{{ a.url | relative_url }}">{{ a.title }}</a></li>
          {% endfor %}
        </ul>
      </div>
    </div>
  </section>
{% endfor %}
</div>

## 卡關怎麼辦？

**一題卡超過 20 分鐘就先跳過**，寫完別的回頭往往就通了。真的解不出來，再回來看上面那幾篇教學文章對照著寫——先自己想過一次再看答案，效果差很多。

題庫頁在 [{{ '/apcs/problem-bank/' | relative_url }}](/apcs/problem-bank/)，可以只顯示「條件判斷」或「while 條件迴圈」這種觀念的題目，練單一主題時很好用。
