---
author: 歐巴計概
date: 2009-07-17 12:16:00.002000+00:00
layout: post
permalink: /2009/07/kerneltaskcpu-on-mac.html
title: kernel_task佔滿cpu資源 on Mac
---

參考資料: http://julianschrader.de/20080131-100-cpu-usage-caused-by-syslogd-leopard/

$ sudo launchctl stop com.apple.syslogd

$ sudo rm -r /var/log/asl

$ sudo launchctl start com.apple.syslogd

目前正常運作中