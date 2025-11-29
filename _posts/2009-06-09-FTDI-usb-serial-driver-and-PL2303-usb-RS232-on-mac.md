---
author: 歐巴計概
date: 2009-06-09 05:12:00.009000+00:00
layout: post
permalink: /2009/06/ftdi-usb-serial-driver-on-mac.html
title: FTDI usb-serial driver and PL2303 usb-RS232 on mac
---

http://www.ftdichip.com/Drivers/VCP.htm

安裝後重開機便可直接這類的device

如何連到gumstix的console, reference: [Terminal to Serial/USB Devices From a Mac](http://blogs.sun.com/blogsagainbynight/entry/terminal_to_serial_usb_devices)

> $ screen /dev/tty.usbxxxx 115200

PS: usb - RS232 driver [PL2303](http://sourceforge.net/projects/osx-pl2303/)