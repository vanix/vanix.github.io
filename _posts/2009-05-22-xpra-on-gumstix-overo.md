---
author: 歐巴計概
date: 2009-05-22 07:48:00.003000+00:00
layout: post
permalink: /2009/05/xpra-on-gumstix-overo.html
title: xpra on gumstix overo
---

1. 透過opkg及[angstrom-distribution的package browser](http://www.angstrom-distribution.org/repo/)

將下述套件安裝至系統上 (套件名稱會有一些差異)

> libx11-dev libxtst-dev libxcomposite-dev libxdamage-dev python-gobject-dev python-gtk2-dev xvfb python-pyrex python-compiler python- subprocess imake makedepend ...etc

2. 自行compile [mesa](http://sourceforge.net/project/showfiles.php?group_id=3) 取得swrast\_dri.so

3. 下載Dri2proto, 將dir2token.h copy至 /usr/include (?)

4. vi /usr/lib/python2.6/sitexxxx/pyrex/Distutil/extension.py
> # \_Extension......doc

5. compile xpra

> $ cd parti-0.0.5
>
> $ ./do-build
>
> $ cp -r install/lib/xpra /usr/lib/python2.6/
>
> $ cp -r install/lib/wimmgy /usr/lib/python2.6/
>
> $ cp install/bin/xpra /usr/bin

憑印象寫的，有空再勘誤