---
author: 歐巴計概
date: 2009-07-07 09:17:00.005000+00:00
layout: post
permalink: /2009/07/angstrom-on-gumstix-overo.html
title: Angstrom on gumstix overo
---

這些相關資料跟檔案給大家參考

Gumstix說明文件

<http://www.gumstix.net/Software/cat/Software-Overo/111.html>

Gumstix提供的kernel and file system

<http://www.gumstix.net/overo-gm-images/v0.92/>

同事提供的linux-omap3-2.6.29 kernel

<http://mtube.name/svn/MTube/sandbox/bin/linux-omap3-2.6.29-rc0.tar.gz>

zd1211的driver要另外勾選

CodeSourcery提供的cross compiler

<http://mtube.name/svn/MTube/sandbox/bin/CodeSourcery.tar.gz>

Compile kernel

> $ cd kernel\_dir
>
> $ make CROSS\_COMPILE=/path/CodeSourcery/Sourcery\_G++\_Lite/bin/arm-none-linux-gnueabi- uImage