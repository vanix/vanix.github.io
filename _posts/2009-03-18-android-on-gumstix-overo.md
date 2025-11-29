---
author: 歐巴計概
date: 2009-03-18 08:52:00.019000+00:00
layout: post
permalink: /2009/03/android-on-gumstix-overo.html
title: android on gumstix overo
---

First, Creating a bootable microSD card for gumstix

http://www.gumstix.net/Overo/view/Overo/Creating-a-bootable-microSD-card/115.html

切出兩個partition, 一個是FAT, 另一個是ext3

在 http://www.gumstix.net/overo-gm-images/v0.91/ 下載ML0, u-boot.bin, 放至FAT partition

Second, Compile gumstix kernel fitted android and configure boot args

參考 http://labs.embinux.org/index.php/Android\_Porting\_Guide\_to\_Beagle\_Board

使用beagle board已經patch好的kernel

menuconfig的設定, star system type-> gumstix overo

並且勾選zd1211的項目, 讓wifi可以運作

使用CodeSourcery的toolchain編譯

> $ make arch=arm CROSS\_COMPILE= PATH\_TO\_CODE\_SOURCERY \_TOOL\_CHAIN uImage

> update: android on beagle的kernel似乎有新版的

最後把uImage放置FAT的partition

Boot arguments of Gumstix

> $ setenv mmcargs setenv bootargs console=ttyS2,115200n8, video= omapfb:mode:1280x720@50, root=/dev/mmcblk0p2 rootdelay=2 init=/init

> update: ttyS2,115200n8兩個參數之間不能有空白...亂碼狂噴...orz

Third, Compile RFS and configure it

參考 http://source.android.com/download

下載source並且set up environment

$ cd ~/mydroid

$ make (make showcommands for debug)

編譯好的RFS會放在 mydroid/out/target/product/generic/

$ cp -a root/\* /media/ext3\_partition/

$ cp -a data/\* /media/ext3\_partition/data/

$ cp -a system/\* /media/ex3\_partition/system/

init.rc patch http://labs.embinux.org/images/6/6c/Initrc.patch

$ cd /media/ext3\_partition/

$ patch -p1 < initrc.patch

Qwerty patch http://labs.embinux.org/images/f/fd/Qwerty.patch

$ cd /media/ext3\_partition/system/usr/keylayout

$ patch -p1 < Qwery.patch

權限設定

$ cd /media/ext3\_partition/

$ chown -R root.root \*

$ chmod -R 777 data/ system/

網路設定

$ vi /media/ext3\_partition/init.rc
> #basic network init
>
> ifup eth0(or wlan0)
>
> setprop net.dns1

新增tty1

$ vi /media/ext3\_partition/init.rc

> service getty /sbin/getty 38400 tty1

新增額外的shell, ex: iwconfig, ifconfig...etc

把Angstrom的/bin, /sbin, /lib丟到/media/ext3\_partitaion

系統boot之後, 使用下面指令啟動dhcp

$ netcfg eth0(or wlan0) dhcp

debug

$ logcat