---
author: 歐巴計概
date: 2009-07-06 06:50:00.007000+00:00
layout: post
permalink: /2009/07/mount-sd-card-on-android.html
title: Mount SD card on android
---

參考資料: [Android: Fix to allow vold to detect the SD card](https://omapzoom.org/gf/project/omapandroid/mailman/?_forum_action=ForumMessageBrowse&thread_id=1640&action=ListThreads&mailman_id=22)

更改kernel的.config

> -CONFIG\_SYSFS\_DEPRECATED=y
>
> -CONFIG\_SYSFS\_DEPRECATED\_V2=y
>
> +# CONFIG\_SYSFS\_DEPRECATED\_V2 is not set

新增 /system/etc/vold.conf on android

> volume\_sdcard {
>
> ~~emu\_media\_path /devices/platform/mmci-omap-hs.0/mmc\_host/mmc0/mmc0:b368~~
>
> media\_path /devices/platform/mmci-omap-hs.0/mmc\_host/mmc0
> media\_type mmc
>
> mount\_point /sdcard
>
> ums\_path /devices/platform/usb\_mass\_storage/lun0
>
> }

media\_path可從dmesg裡面查到

這個解法還是有問題, 有時必須重開好幾次, mp3 player才找得到sdcard
雖然每次開機系統會將partition mount在/sdcard
但是logcat的vold error message還是會狂噴
~~暫時不清楚問題出在哪~~

Android 1.6就沒有這個問題了
可能是硬體問題，earth ok，air not

剛隨便亂塞兩個patch給mmc-twl4030, 但是看起來也是沒用
http://patchwork.kernel.org/patch/31733/
http://patchwork.kernel.org/patch/31970/