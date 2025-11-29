---
author: 歐巴計概
date: 2011-08-01 14:19:00+00:00
layout: post
permalink: /2011/08/mac-app-store-note.html
title: mac app store note
---

1.

ref: [Where does the Mac AppStore download temp files to](http://www.ryanragle.com/index.php?/site/comments/where-does-the-mac-app-store-download-temp-files-to)

$ defaults write com.apple.appstore ShowDebugMenu -bool true

選擇 debug -> reset application

temp file存放在 ~/Library/Application Support/AppStore/

--

2.

前陣子用mac app store會有一些圖片無法顯示

$ rm -r ~/Library/Caches/com.apple.appstore/

刪掉快取後就好了