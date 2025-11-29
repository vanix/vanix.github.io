---
author: 歐巴計概
date: 2009-07-01 00:36:00.007000+00:00
layout: post
permalink: /2009/07/zd1211-on-gumstix-overo.html
title: zd1211 and libertas_sdio on gumstix overo
---

zd1211的網卡放在gumstix overo上，load firmware的時候會出現一些error messages

最後雖然用好了，偶爾會有偵測不到裝置的問題，重新拔插即可

libertas\_sdio的問題必須要編成module且傳輸速度只有1mb/s左右

**Kernel**

查詢zd1211，將depends的項目build-in，zd1211的部份則勾選成"\*"，

查詢libertas，Marvell libertas的部份勾選成"\*"

**firmware**

http://sourceforge.net/projects/zd1211/

下載zd1211-firmware-1.4，解壓縮放置/lib/firmware/zd1211

http://elinux.org/Libertas\_SDIO，或是從Mtube II的/lib/firmware撈

**Setting**

網路速度過慢的話，自行設定bit rate看看

$ iwconfig interface rate 54M

--------------------------------------------------------------------------------------------------

補充資料, 應該不需要這個方法

假如遇到無法連接到AP和網卡無法ifup，則修改load firmware的shell script

udev setting

參考資料: http://phorum.study-area.org/index.php?topic=54732.0

$ vi /etc/udev/rules.d/udev.rules

> SUBSYSTEM=="firmware", ACTION=="add", RUN+="firmware.agent"

$ vi /lib/udev/firmware.agent

> #!/bin/sh -e
>
> #
>
> # firmware.agent
>
> #
>
> # firmware loader agent
>
> #
>
> cd /lib/udev/
>
> . ./hotplug.functions
>
> if [ ! -e /sys/$DEVPATH/loading ]; then
>
> mesg "/sys/$DEVPATH/ does not exist"
>
> exit 1
>
> fi
>
> for DIR in $FIRMWARE\_DIRS; do
>
> [ -e "$DIR/$FIRMWARE" ] || continue
>
> echo 1 > /sys/$DEVPATH/loading
>
> cat "$DIR/$FIRMWARE" > /sys/$DEVPATH/data
>
> echo 0 > /sys/$DEVPATH/loading
>
> exit 0
>
> done
>
> # the firmware was not found
>
> echo -1 > /sys/$DEVPATH/loading
>
> debug\_mesg "Cannot find the $FIRMWARE firmware"
>
> exit 1