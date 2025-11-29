---
layout: post
title: "更新linux kernel"
date: 2006-10-11T10:46:00Z
author: "歐巴計概"
permalink: /2006/10/linux-kernel.html
---

1.安裝部份<br />tar -zxvf linux-2.6.18.tar.gz to /usr/src<br />make mrproper<br />make oldconfig(make menuconfig有error...不太清楚原因)<br />make clean<br />make bzImage<br />make modules<br />make modules_install<br />make install<br /><br />2.重複編譯注意事項<br />cd /lib/modules<br />mv 2.6.18 2.6.18.old<br /><br />3.grub多重開機部份<br />vi /boot/grub/menu.lst<br /><br />詳細參考資料<br />http://linux.vbird.org/linux_basic/0540kernel.php<br />http://linux.vbird.org/linux_basic/0510osloader.php#grub
