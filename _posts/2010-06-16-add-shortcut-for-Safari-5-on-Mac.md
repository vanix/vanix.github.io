---
author: 歐巴計概
date: 2010-06-16 17:13:00.004000+00:00
layout: post
permalink: /2010/06/add-shortcut-for-safari-5-on-mac.html
title: add shortcut for Safari 5 on Mac
---

用Interface builder編輯 /Application/Safari.app/Content/Resources/zh\_TW.lproj/MainMenu.nib
但是會顯示錯誤訊息 "Interface builder cannot open compiled nibs"
開啟大多數的nib會顯示此項訊息，少部分nib可順利開啟
從可開啟的nib裡，複製class.nib及info.nib至MainMenu.nib，則可順利開啟MainMenu.nib

即可透過Interface builder增加safari 5的快速鍵
"重新打開上一次連線時段的所有視窗" 對應 command+shift+R
類似chrome同樣功能的快速鍵

更改後如下圖

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXxa3dgJVJxvc_05MjcAGUYU9PKOsOnEhBjOIVOYHXetYtwGM5XqZr5iql87NNIwKynIq7FGFTlQU4yb8y3GjpXWwpvHiKrlTWxS0zCYQJ7GGAXNCzPgybXMonqZhksd9z74OZCw/s320/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7+2010-06-21+%E4%B8%8B%E5%8D%881.42.41.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXxa3dgJVJxvc_05MjcAGUYU9PKOsOnEhBjOIVOYHXetYtwGM5XqZr5iql87NNIwKynIq7FGFTlQU4yb8y3GjpXWwpvHiKrlTWxS0zCYQJ7GGAXNCzPgybXMonqZhksd9z74OZCw/s1600/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7+2010-06-21+%E4%B8%8B%E5%8D%881.42.41.png)