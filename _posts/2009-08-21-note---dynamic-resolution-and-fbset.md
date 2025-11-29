---
author: 歐巴計概
date: 2009-08-21 15:19:00.010000+00:00
layout: post
permalink: /2009/08/dynamic-resolution-and-fbset.html
title: note - dynamic resolution and fbset
---

This problem was not solved yet.

從framework著手

http://groups.google.com/group/android-porting/browse\_thread/thread/ed9368ceff194a88

動態改解析度得從下面兩點著手, 尚未找到具體的改法

1. DisplaySurface 2. WindowManager

從fbset著手

http://www.nabble.com/Re:-Overo,-no-HDMI-output-p21426504.html

http://orion.dherring.com/beagleTouchWiki/OmapFb

> The OMAP3 video driver does not currently support changing the resolution with fbset.
>
> Omapfb does not support changing the video timings with the fbset command
>
> 得再確認fbset可以做到什麼地步. 目前測試的結果是, 更改解析度後畫面會錯亂.
>
> 以及只能裁剪畫面

u-boot參數加入omapfb相關參數 - - 以1024x768為例

> setenv mmcargs setenv bootargs console=ttyS2,115200n8 androidboot.console=ttyS2 root=/dev/mmcblk0p2 rootdelay=2 omapfb.mode=dvi:1024x768MR-16@60 omapfb.debug=y omapdss.debug=y omapfb.test=y init=/init

裁剪畫面 - 以1024x768為例

> $ fbset -fb /dev/graphics/fb0 -xres 800 -yres 600

只顯示螢幕左上角800x600的畫面

PS: 也可以改position

> $ echo "x座標,y座標" > /sys/devices/platform/omapdss/overlay0/position

更改解析度及timings - 以1024x768為例

> $ echo "0" > /sys/devices/platform/omapdss/display0/enabled
>
> $ echo "0" > /sys/devices/platform/omapdss/overlay0/enabled
>
> $ fbset -fb /dev/graphics/fb0 -g 800 480 800 480 16
>
> $ echo "28800,800/80/48/32,480/3/6/7" > /sys/devices/platform/omapdss/display0/timings
>
> $ fbset -fb /dev/graphics/fb0 -t 28800 80 48 3 6 32 7
>
> $ echo "1" >/sys/devices/platform/omapdss/overlay0/enabled
>
> $ echo "1" >/sys/devices/platform/omapdss/display0/enabled

note

mode "800x480-60"

# D: 28.800 MHz, H: 30.000 kHz, V: 60.484 Hz

geometry 800 480 800 481 16

timings 34722 80 48 3 6 32 7

rgba 5/11,6/5,5/0,0/0

endmode

bash-3.2# cat timings

28800,800/80/48/32,480/3/6/7

mode "1024x768-62"

# D: 57.600 MHz, H: 48.649 kHz, V: 61.581 Hz

geometry 1024 768 1024 768 16

timings 17361 80 48 3 15 32 4

rgba 5/11,6/5,5/0,0/0

endmode

bash-3.2# cat timings

57600,1024/80/48/32,768/3/15/4