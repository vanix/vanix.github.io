---
author: 歐巴計概
date: 2010-07-20 08:47:00.003000+00:00
layout: post
permalink: /2010/07/fbset-note.html
title: fbset note
---

純粹記錄...

echo "0" > /sys/devices/platform/omapdss/display0/enabled

fbset -fb /dev/graphics/fb0 -xres 800 -yres 480 -vxres 800 -vyres 480 -depth 16

echo "28800,800/80/48/32,480/3/6/7" > /sys/devices/platform/omapdss/display0/timings

echo "34722,800/80/48/32,480/3/6/7" > /sys/devices/platform/omapdss/display0/timings

fbset -fb /dev/graphics/fb1 -xres 1024 -yres 768 -vxres 1024 -vyres 768 -depth 16

echo "57600,1024/80/48/32,768/3/15/4" > /sys/devices/platform/omapdss/display0/timings

echo "1" >/sys/devices/platform/omapdss/display0/enabled

fbset -fb /dev/graphics/fb0 -g 800 480 800 480 16

fbset -fb /dev/graphics/fb0 -match

fbset -fb /dev/graphics/fb0 -xres 800 -yres 480 -depth 16 -match

fbset -fb /dev/graphics/fb0 -t 28800 80 48 3 6 32 7

fbset -fb /dev/graphics/fb0 -t 57600 80 48 3 15 32 4

fbset -fb /dev/graphics/fb0  -g 1024 768 1024 768 16

fbset -fb /dev/graphics/fb0  -g 800 480 800 480 16

fbset -fb /dev/graphics/fb0  -g 800 480 800 480 16 --timings 34722 80 48 3 6 32 7

fbset -fb /dev/graphics/fb0 -t 34722 80 48 3 6 32 7

mode "800x480-60"

# D: 28.800 MHz, H: 30.000 kHz, V: 60.484 Hz

geometry 800 480 800 481 16

timings 34722 80 48 3 6 32 7

rgba 5/11,6/5,5/0,0/0

endmode

clock: clksel\_round\_rate\_div: dpll4\_m4\_ck target\_rate 28800000

clock: new\_div = 15, new\_rate = 28800000

bash-3.2# cat timings

28800,800/80/48/32,480/3/6/7

57600,1024/80/48/32,768/3/15/4

mode "1024x768-62"

# D: 57.600 MHz, H: 48.649 kHz, V: 61.581 Hz

geometry 1024 768 1024 768 16

timings 17361 80 48 3 15 32 4

rgba 5/11,6/5,5/0,0/0

endmode

setenv mmcargs setenv bootargs console=ttyS2,115200n8 androidboot.console=ttyS2 root=/dev/mmcblk0p2 rootdelay=2 omapfb.mode=dvi:800x480MR-16@60 omapfb.debug=y omapdss.debug=y omapfb.test=y init=/init

setenv mmcargs setenv bootargs console=ttyS2,115200n8 androidboot.console=ttyS2 root=/dev/mmcblk0p2 rootdelay=2 omapfb.mode=dvi:1024x768MR-16@60 omapfb.debug=y omapdss.debug=y omapfb.test=y omapfb.rotate=0 init=/init