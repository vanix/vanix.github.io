---
author: 歐巴計概
date: 2010-03-15 09:24:00+00:00
layout: post
permalink: /2010/03/note-compile-android-21.html
title: note - compile android 2.1
---

1. BatteryService patch

http://labs.embinux.org/git/cgit.cgi/android-omap3/repo/android/platform/frameworks/base/commit/?h=beagle-eclair

2. libwebcore.a problem

cd external/webkit

git cherry-pick 18342a41ab72e2c21931afaaab6f1b9bdbedb9fa

...