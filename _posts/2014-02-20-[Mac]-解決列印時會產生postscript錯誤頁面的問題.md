---
author: 歐巴計概
date: 2014-02-20 06:48:00.006000+00:00
layout: post
permalink: /2014/02/mac-postscript.html
title: '[Mac] 解決列印時會產生postscript錯誤頁面的問題'
---

2025/09/08更新：使用airprint連接網路印表機，如果印表機不支援，再改用PCL吧，教學影片如下，請參考

以下內容來自[討論串](https://discussions.apple.com/thread/5471125?tstart=0)，如果不想這麼麻煩，新增一般PCL印表機加減用

This copier is about 9 years old. As far as I know there isn't going to be a new driver/ppd written for this device. That said the built in generic ps and pcl drivers in 10.9 work pritty well over TCP IP.

My setup went as follows.

Click the Apple in the left corner of the menu bar.

System Prefrences.

Printers and Scanners.

Click the + sign.

Select IP.

In "Address:" type the IP address of the machine.

Next to "use:" pick Generic Post Script Printer or Generic PCL Printer.

If you pick PostScript and you get code printing out insted of your print job, your printer may not have the PostScript opption. If you don't, pick the PCL.

Click Add.

If you have the duplexer unit check Duplex Printing Unit and press OK.

Thats what I did for 10.8 and 10.9. Good luck!