---
author: 歐巴計概
date: 2009-03-18 08:58:00.003000+00:00
layout: post
permalink: /2009/03/lighttpd-note.html
title: lighttpd note
---

$ apt-get install lighttpd

$ vi /etc/lighttp/lighttp.conf
> "mod\_userdir" ,
>
> userdir.path ="public\_html"

$ vi /etc/rc.local

/usr/sbin/lighttpd -f /etc/lighttpd/lighttpd.conf