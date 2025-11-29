---
author: 歐巴計概
date: 2010-04-30 06:57:00.002000+00:00
layout: post
permalink: /2010/04/bootchart-on-android.html
title: bootchart on android
---

ref: <http://elinux.org/Using_Bootchart_on_Android>

@ host

$ apt-get install bootchart

$ export INIT\_BOOTCHART=true

compile android source code then copy android fs to destination

@ destination

$ mkdir /data/bootchart

$ echo 120 > /data/bootchart-start

after android boot @ host

$ export ADBHOST=android\_ip

$ system/core/init/grab-bootchart.sh

$ bootchart bootchart.tgz

finally, generate a bootchart.png at current folder