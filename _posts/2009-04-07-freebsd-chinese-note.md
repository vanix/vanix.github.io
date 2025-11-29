---
author: 歐巴計概
date: 2009-04-07 02:48:00.005000+00:00
layout: post
permalink: /2009/04/freebsd-chinese-note.html
title: freebsd chinese note
---

非常的粗淺... just note

ref: [Freebsd Chinese How-To](http://netlab.cse.yzu.edu.tw/~statue/freebsd/zh-tut/)

distribution : PC-BSD 7.02

常用cmd: locale, fc-list, fc-cache, setenv

\*中文設定

> $ locale //檢查現在系統所用的編碼
>
> $ cd /usr/port/misc/utf8locale
>
> $ make install (needed?)
>
> $ setenv LANG zh\_TW.UTF-8
>
> $ setenv LC\_CTYPE zh\_TW.UTF-8
>
> (把這兩行加至~/.cshrc)
>
> $ cd /usr/port/chinese/
>
> $ 安裝自己想要的中文字型, or others
>
> $ 把字體放到/usr/share/fonts, 或其他fonts.conf設定的目錄
>
> $ fc-cache -f -v //安裝字型
>
> $ fc-list :lang=zh-tw 檢查是否有安裝繁體字型

\*安裝輸入法

> $ cd /usr/port/chinese/gcin
>
> $ make install
>
> $ vi ~/.xinitrc
>
> setenv XMODIFIERS "@im=gcin"
>
> setenv GTK\_IM\_MODULE=xim
>
> gcin &