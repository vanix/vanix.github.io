---
author: 歐巴計概
date: 2009-08-28 05:43:00.004000+00:00
layout: post
permalink: /2009/08/modify-u-boot-environment-variables-in.html
title: modify U-boot environment variables in linux
---

從Angstrom on gumstix的fs裡, 挖出下列三個檔案

> /etc/fw\_env.config
>
> /usr/sbin/fw\_printenv
>
> /usr/sbin/fw\_setenv

也可利用這三個檔案在Android on gumstix上modify U-boot environment variables

顯示參數

> $ fw\_printenv

設定參數

> $ fw\_setenv mmcargs setenv bootargs console=ttyS2,115200n8 androidboot.console=ttyS2 root=/dev/mmcblk0p2 rootdelay=2 omapfb.mode=dvi:1024x768MR-16@60 init=/init