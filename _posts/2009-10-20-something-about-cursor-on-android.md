---
author: 歐巴計概
date: 2009-10-20 02:36:00.005000+00:00
layout: post
permalink: /2009/10/something-about-cursor-on-android.html
title: something about cursor on android
---

問題發生在enable home key這件事情之後
系統進入鍵盤鎖時, 得按下menu key解鎖
此時不管怎麼按menu key都沒有反應
從logcat得知
> W/WindowManager( 876): No focus window, dropping: KeyEvent{action=0 code=82 repeat=0 meta=0 scancode=126 mFlags=8}

後來發現在patch WindowManagerService.java之後就會發生這個問題
繼續等待網路上的能人異者解決這個問題~