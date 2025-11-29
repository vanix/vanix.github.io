---
author: 歐巴計概
date: 2010-06-22 16:15:00.002000+00:00
layout: post
permalink: /2010/06/enable-bluetooth-on-android.html
title: enable bluetooth on android
---

在android donut測試藍芽耳機及wii remote，參考資料如下

連結文章中也包含部分基礎設定及教學

ref:

http://www.kumikomi.net/archives/2009/09/beagleboardandroid\_wii1.php

http://www.kumikomi.net/archives/2009/10/wii2\_beagleboardandroid.php

讓android提供bluetooth service

> $ vi BoardConfig.mk
> BOARD\_HAVE\_BLUETOOTH := true
> $ vi init.rc
> service hciattach /system/bin/hciattach -s 115200 ttyS1 csr 115200 noflow
>      disabled
>      oneshot

重新編譯後啟動android，便可以順利透過setting啟動bluetooth
並且可直接跟藍芽耳機配對，但是配對後發生android吃不到keyboard event的問題
暫時的解決方法是
> $ vi /system/etc/bluez/audio.conf
> [AVRCP]
> #InputDeviceName=AVRCP

還有一個聲音斷斷續續的問題 (問題真多 0rz)
另外driver的話，gumstix overo採用的是HCI UART driver

要使用wii remote的話，大致上參考第二篇文章即可完成，在此只有簡述
取得external/cwiid之後，google此檔案ep52android2\_cwiid-for-android.patch，並且patch
完成上述步驟並且重新編譯後
每當bluetooth啟動，只要按下wii remote的1+2 button就可完成配對
連結文章提供的架構圖

[![](http://www.kumikomi.net/archives/2009/10/ep52android2/ep52android2_f01_b.jpg)](http://www.kumikomi.net/archives/2009/10/ep52android2/ep52android2_f01_b.jpg)

其他要注意的是
1. kernel需要CONFIG\_INPUT\_UINPUT=y

2. wii remote配對: wminput -w -c /etc/cwiid/wminput/acc\_ptr

未整理:

ignore\_rfkill.patch