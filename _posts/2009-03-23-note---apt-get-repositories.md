---
author: 歐巴計概
date: 2009-03-23 03:38:00.007000+00:00
layout: post
permalink: /2009/03/note-apt-get-repositories.html
title: note - apt-get repositories
---

只是要編譯個metavnc, 結果apt-get一直出問題... ( ps: ubuntu on x86)

> deb http://ftp.twaren.net/Linux/Ubuntu/ubuntu/ hardy main universe restricted multiverse
>
> deb-src http://ftp.twaren.net/Linux/Ubuntu/ubuntu/ hardy main universe restricted multiverse
>
> #deb http://security.ubuntu.com/ubuntu/ hardy-security universe main multiverse restricted
>
> #deb-src http://security.ubuntu.com/ubuntu/ hardy-security universe main multiverse restricted
>
> deb http://ftp.twaren.net/Linux/Ubuntu/ubuntu/ hardy-security universe main multiverse restricted
>
> deb-src http://ftp.twaren.net/Linux/Ubuntu/ubuntu/ hardy-security universe main multiverse restricted
>
> deb http://ftp.twaren.net/Linux/Ubuntu/ubuntu/ hardy-updates universe main multiverse restricted
>
> deb-src http://ftp.twaren.net/Linux/Ubuntu/ubuntu/ hardy-updates universe main multiverse restricted