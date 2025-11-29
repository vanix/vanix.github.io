---
author: 歐巴計概
date: 2009-10-13 09:45:00.004000+00:00
layout: post
permalink: /2009/10/enable-pci-gw-usmicron-on-linux-and.html
title: Enable PCI GW-USMicroN on Linux and Android
---

Driver and firmware
> 先到Ralink網站下載linux driver and firmware, chip是rt3070USB
> http://www.ralinktech.com.tw/support.php?s=2

Compile - Linux (x86)
> $ cd driver\_folder
> $ make

Compile - Android (omap35xx)
> $ cd driver\_folder
> $ vi Makefile
> PLATFORM=ARM
> ifeq ($(PLATFORM),ARM)
> LINUX\_SRC = /home/vanix/embinux\_android\_on\_beagle\_0708/kernel
> CROSS\_COMPILE = /home/vanix/CodeSourcery/Sourcery\_G++\_Lite/bin/arm-none-linux-gnueabi-
> endif
> $ vi os/linux/config.mk
> ifeq ($(PLATFORM), ARM)
> EXTRA\_CFLAGS := -D\_\_KERNEL\_\_ -I$(LINUX\_SRC)/include -I$(RT28xx\_DIR)/include -mlittle-endian -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Os -marm -fno-omit-frame-pointer -mapcs -mno-sched-prolog -mabi=aapcs-linux -mno-thumb-interwork -D\_\_LINUX\_ARM\_ARCH\_\_=7 -march=armv7-a -msoft-float -Uarm -fno-stack-protector -fno-omit-frame-pointer -fno-optimize-sibling-calls -g -Wdeclaration-after-statement -Wno-pointer-sign -fwrapv -DMODULE $(WFLAGS)
> export EXTRA\_CFLAGS
> endif
> $ vi os/linux/usb\_device.xxx
> 把device id加進去，可用lsusb查詢

Copy firmware to special path
$ cp RT2870STA.dat /etc/Wireless/RT2870STA/

Insert module
$ insmod driver\_folder/os/linux/rt3070sta.ko