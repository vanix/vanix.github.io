---
author: bin
date: 2009-12-16 11:19:00.004000+00:00
layout: post
permalink: /2009/12/make-module-with-kernel-headers.html
title: make module with kernel headers
---

以zd1211rw為例

# cd linux-source/drivers/net/wireless/zd1211rw/

# vi Makefile

> obj-(CONFIG\_NET\_ZD1211) -> obj-m =zd1211rw.o

# make -C ~/Work/kernel-header-2.6.27-android/ M=`pwd` CROSS\_COMPILE=/path/to/toolchain/bin/arm-eabi- ./zd1211.ko