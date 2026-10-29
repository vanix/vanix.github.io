---
layout: apcs
title: 教學影片
heading: APCS 教學影片｜Python 初級到中級課程與解題影片
seo_title: APCS 教學影片｜Python 初級到中級課程與解題影片 - 充滿意外的宅爸人生
subtitle: 12 部影片・基礎語法、解題練習與中級範例題，點開就能上課
permalink: /apcs/videos/
icon: fab fa-youtube
description: "APCS 教學影片總整理：12 部 Python 程式實作課程影片，分成初級基礎語法（print／input、變數與算術運算、if 條件判斷、迴圈、遞迴）、初級解題練習（巢狀迴圈、字串與串列、七言對聯）與中級函數與範例題（自訂函數、特殊位置、字串解碼、蒐集寶石），每部影片都附長度、發布日期與對應的圖文教學文章，適合準備 APCS 初級與中級實作題的學生搭配刷題使用。"
---

{% assign groups = site.data.apcs_videos.groups %}
{% assign total = 0 %}
{% for g in groups %}{% assign total = total | plus: g.videos.size %}{% endfor %}

這裡把 YouTube 播放清單上的 **{{ total }} 部 APCS 教學影片**整理成一頁，分成**初級基礎語法**、**初級解題練習**與**中級函數與範例題**三段。影片長度都標在卡片上，想複習某個觀念直接點開看，不用再從播放清單裡撈。

> 建議搭配[學習地圖]({{ '/apcs/roadmap/' | relative_url }})的階段順序看：先看完基礎語法，再去[基本題庫]({{ '/apcs/problem-bank/' | relative_url }})挑題動手寫，卡住再回來看解題影片。
{: .prompt-tip }

{% for g in groups %}
  <section class="apcs-video-section">
    <h2 class="apcs-video-heading">{{ g.title }}<span class="apcs-video-count">{{ g.videos.size }} 部</span></h2>
    {% if g.note %}<p class="apcs-note">{{ g.note }}</p>{% endif %}
    <div class="apcs-videos-grid">
    {% for v in g.videos %}
      <figure class="apcs-video">
        <div class="apcs-video-frame">
          <iframe src="https://www.youtube.com/embed/{{ v.id }}" title="{{ v.title }}" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        <figcaption>
          <div class="apcs-video-title">{{ v.title }}</div>
          <div class="apcs-video-meta">
            <span class="apcs-video-dur"><i class="fas fa-clock"></i> {{ v.duration }}</span>
            <span>{{ v.date }}</span>
            {% if v.article %}<a href="{{ v.article | relative_url }}">看文章 →</a>{% endif %}
          </div>
        </figcaption>
      </figure>
    {% endfor %}
    </div>
  </section>
{% endfor %}

<p class="apcs-note">影片持續更新中，完整播放清單：<a href="{{ site.data.apcs_videos.playlist.url }}" target="_blank" rel="noopener">{{ site.data.apcs_videos.playlist.title }}</a>。</p>
