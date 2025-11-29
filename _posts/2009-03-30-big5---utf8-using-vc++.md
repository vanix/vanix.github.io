---
author: 歐巴計概
date: 2009-03-30 08:41:00.002000+00:00
layout: post
permalink: /2009/03/big5-utf8-using-vc.html
title: big5 <-> utf8 using vc++
---

知其然而不知其所以然, 太糟糕了!

big5->unicode
> len=MultiByteToWideChar (CP\_ACP, 0, sendbuf, -1, NULL,0) ;
> sendwbuf=new wchar\_t[iLen+1];
> MultiByteToWideChar(CP\_ACP, 0, sendbuf, -1, sendwbuf, iLen);

unicode->UTF-8
> len=WideCharToMultiByte (CP\_UTF8, 0, sendwbuf, -1, NULL,0 ,NULL, NULL);
> sendbuf\_utf8=new char[iLen+1];
> WideCharToMultiByte (CP\_UTF8, 0, sendwbuf, -1, sendbuf\_utf8,iLen, NULL, NULL);

參考資料: [每個軟體開發者都絕對一定要會的Unicode及字元集必備知識(沒有藉口！)](http://local.joelonsoftware.com/mediawiki/index.php/The_Joel_on_Software_Translation_Project:%E8%90%AC%E5%9C%8B%E7%A2%BC)