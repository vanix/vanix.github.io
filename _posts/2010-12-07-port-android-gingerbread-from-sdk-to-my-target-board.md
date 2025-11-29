---
author: 歐巴計概
date: 2010-12-07 12:50:00.001000+00:00
layout: post
permalink: /2010/12/port-android-gingerbread-from-sdk-to-my.html
title: port android gingerbread from sdk to my target board
---

google稍早放出薑餅人沒多久

已經有人把薑餅人放到beagle board了

ref: [Gingerbread を BeagleBoard と Armadillo にのせてみた](http://blog.sola-dolphin-1.net/archives/3135091.html#more)

因此也花了一個下午的時間來嘗試這件事情

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFQkTZxtT9fhsuHwx1k8v9CL0Qy08Nm_HKPflRypWexMhIlwqEKTdrxWlDf45X859Y95dkZGbwumZMQrDwdneoOv92FYpL0O03P-98p8QpLMRk7zd4AEs9qYCbloGJpllWoOfqMw/s200/%25E8%259E%25A2%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2010-12-07+%25E4%25B8%258B%25E5%258D%25887.41.41.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFQkTZxtT9fhsuHwx1k8v9CL0Qy08Nm_HKPflRypWexMhIlwqEKTdrxWlDf45X859Y95dkZGbwumZMQrDwdneoOv92FYpL0O03P-98p8QpLMRk7zd4AEs9qYCbloGJpllWoOfqMw/s1600/%25E8%259E%25A2%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2010-12-07+%25E4%25B8%258B%25E5%258D%25887.41.41.png)

有kernel source 及 android source，這應該已經不算難題

以我的狀況來說，解決battery跟權限問題之後便可順利進入android