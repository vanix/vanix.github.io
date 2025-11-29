---
author: 歐巴計概
date: 2009-07-10 01:30:00.002000+00:00
layout: post
permalink: /2009/07/gumstix-overo-on-android.html
title: Android donut on Gumstix overo  - 相關設定整理
---

Shell - copy shell on Angstrom to android

> $ wget http://www.gumstix.net/overo-gm-images/v0.92/omap3-console-image-overo-v0.92.tar.bz2
>
> $ tar -jxvf omap3-console-image-overo-v0.92.tar.bz2
>
> $ cp bin/ sbin/ lib/ usr/bin/ usr/sbin/ usr/lib usr/share/usb.ids /media/android\_fs\_partition

lsusb
> $ mount -t usbfs none /proc/bus/usb
> 應該也可以寫到init.rc裡面
> 寫在fstab沒有作用

Ctrl+c

> u-boot參數多加一個androidboot.console
>
> $ setenv mmcargs setenv bootargs console=ttyS2,115200n8 androidboot.console=ttyS2 root=/dev/mmcblk0p2 rootdelay=2 omapfb.mode=dvi:800x480MR-16@60 init=/init
>
> 意外解決scp的鬼問題 good :p

Read-Only filesystem

> $ vi init.rc
>
> comment mount rootfs rootfs / ro remount

GPIO and 800x480

u-boot參數

kerner driver

DNS

> $ vi init.rc
>
> #basic network init
>
> setprop net.dns1 140.96.254.100

Ethernet

> $ make menuconfig
>
> Device Drivers -> Network device support -> USB Network Adapters -> Multi-purpose USB Networking Framework -> ASIX AX88xxx Based USB2.0 Ethernet Adapter
>
> $ vi init.rc
>
> #basic network init
>
> ifup eth0
>
> service dhcp /system/bin/netcfg eth0 dhcp
>
> oneshot
>
> (上面兩行擺在init.rc的最後面即可)

Wireless Network - zd1211

> $ make menuconfig
>
> Device Drivers -> Network device support -> Wireless LAN -> Wireless LAN and ZyDAS ZD1211/ZD1211B USB-wireless support
>
> $ cp zd1211-firmware /system/etc/firmware/zd1211
>
> $ vi init.rc
>
> #basic network init
>
> ifup wlan0
>
> $ iwconfig wlan0 essid xxx
>
> $ netcfg wlan0 dhcp

ALSA - sample config: [asound.conf](http://docs.google.com/Doc?id=dfkx5km7_18fq9fqrc2&hl=zh_TW), [init.rc](http://docs.google.com/View?id=dfkx5km7_20cfh5mxf5)

> $ make menuconfig
>
> Device Driver -> Sound card support -> Advanced Linux Sound Architecture -> ALSA for Soc audio support -> 全選
>
> (其餘項目還沒確定哪些可選可不選)
>
> 編譯alsa-utils, alsa-lib, alsa-sound
>
> 內容太過冗長, 請參考[android 1.5 on gumstix overo](http://vanix.blogspot.com/2009/06/android-15-on-gumstix-overo.html)的 ALSA Setting
>
> $ vi init.rc
>
> $ vi /system/etc/asound.conf
>
> 可參考上面所附的config file

tty

> $ vi init.rc
>
> service getty /sbin/getty 38400 tty1
>
> oneshot

ssh and scp (android內建的)

> $ ln -s /system/xbin/ssh /system/bin/ssh
>
> $ mv /dev/random /dev/random.bk
>
> $ ln -s /dev/urandom /dev/random
>
> ~~ps: 設定後scp還是無法使用~~
>
> ps: u-boot參數多加一個androidboot.console=ttyS2, 意外解決這個問題

Mount SD card

> $ vi .config (接著重編kernel)
>
> -CONFIG\_SYSFS\_DEPRECATED=y
>
> -CONFIG\_SYSFS\_DEPRECATED\_V2=y
>
> +# CONFIG\_SYSFS\_DEPRECATED\_V2 is not set
>
> $ vi /system/etc/vold.conf
>
> volume\_sdcard {
>
> emu\_media\_path /devices/platform/mmci-omap-hs.0/mmc\_host/mmc0/mmc0:b368
>
> media\_type mmc
>
> mount\_point /sdcard
>
> ums\_path /devices/platform/usb\_mass\_storage/lun0
>
> }

ehci

> 阿志大大從oe copy出來的kernel source裡面所附的[overo-ehci.patch](http://docs.google.com/View?id=dfkx5km7_19d3kdqcch)
>
> 無法順利patch的話, 手動改一下就可以了, 然後重編kernel即可支援ehci
>
> ps: 找不到usb device? 換個主板試試手氣 :p

adb tip - 在linux的環境下，透過sdk內附的adb連至remote android

> $ export ADBHOST=192.168.0.133
>
> $ ~/sdk/android-sdk-mac\_x86-1.5\_r2/tools/adb shell
>
> (還沒試過 :p)

Keylayout

> 直接拿android on beagle的qwerty.kl來用

Battery

> patch this file: frameworks/base/services/jni/com\_android\_server\_BatteryService.cpp

touch problem

> patch this file: frameworks/base/libs/utils/ResourceTypes.cpp

Display on Jipin TV through HDMI

> u-boot設定 (800x480還沒成功, 電視偵測到的訊息是800x600@59Hz)
>
> setenv mmcargs setenv bootargs console=ttyS2,115200n8 androidboot.console=ttyS2 root=/dev/mmcblk0p2 rootdelay=2 omapfb.mode=dvi:800x600@60,vxres=800,vyres=600 init=/init
>
> 另外一個設定，解決顏色不對的問題，此外測了三組板子只有一組可正常顯示
>
> setenv mmcargs setenv bootargs console=ttyS2,115200n8 androidboot.console=ttyS2 root=/dev/mmcblk0p2 rootdelay=2 omapfb.mode=dvi:800x600R-16@60 init=/init