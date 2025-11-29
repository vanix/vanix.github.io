---
author: 歐巴計概
date: 2009-06-27 18:16:00.004000+00:00
layout: post
permalink: /2009/06/ipod-touch-as-wifi-adapter-for-pc.html
title: iPod touch as wifi adapter for PC
---

這個需求看起來很詭異 :p

由於某台NB無法連線到我的mac所分享的internet

因此把腦筋動到手邊的ipod touch上

希望那台windows xp的NB，可以透過ipod touch上網

首先是ipod touch必須要Jail break

reference: [iPhone第一代破解教學(Mac系統)-3.0韌體](http://www.itouchtw.com/archives/2118)

然後透過Cydia安裝OpenSSH，順便裝個XGSP、Mxtube :P

windows安裝相關軟體

1. [iPhone Tunnel Suite 2.7](http://www.makkiaweb.net/itunnel/data/its-setup27.zip)
2. iTune 8.2 beta - 聽說這個版本跟上面那軟體相容性較高，就沒試其他版本了
3. firefox - 目前只用firefox測瀏覽網頁就是了，不過有sockscap的話....

設定

1. move C:\Program Files\iPhone Tunnel Suite 2.7 BETA\iTunnel\ and rename iTunesMobileDevice.dll to iTunesMobileDevice.dll.ori
2. Copy C:\Program Files\Common Files\Apple\Mobile Device Support\bin\iTunesMobileDevice.dll to C:\Program Files\iPhone Tunnel Suite 2.7 BETA\iTunnel\
3. 開啟firefox，在某個分頁上輸入about:config，double click "network.proxy.socks\_remote\_dns" 這個項目，false改為true
4. 到firefox的偏好設定 -> 進階 -> 網路 -> 連線設定 -> 手動設定socks5 主機，ip:127.0.0.1 port: 1080
5. 開啟iPhone Tunnel Suite，Device Setting的部份分別設定，Device Name - 隨便打，Model - ipod touch，Firmware - 2.0.2，size - 8G，Wifi ip - ipod touch目前所取得的ip，Root Password - alpine (OpenSSH預設的密碼)，最後按下Save
6. 之後點選iTunnel、iConnect，確認status處在running狀態後，在點選Terminal，便可以連線至ipod touch，並且也建立好Tunnel了(應該在點選iTunnel及iConnect之後就做好這件事情了)
7. 最後確定ipod touch能否上網，可以的話，firefox應該也可以瀏覽網頁了

Reference

http://www.itouchtw.com/archives/2118

http://www.ipodtouchfans.com/forums/showthread.php?t=92113

http://www.webisee.com/2009/06/22/download-working-iphone-tunnel-suite-27-for-os-30/

http://www.ipodtouchfans.com/forums/showthread.php?t=206096

http://getitgiveit.wordpress.com/2008/09/08/iphone-tunnel-suite，iphone的文件管理利器/