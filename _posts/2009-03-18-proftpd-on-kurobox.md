---
layout: post
title: "proftpd on kurobox"
date: 2009-03-18T08:52:00.004Z
author: "歐巴計概"
permalink: /2009/03/proftpd-on-kurobox.html
---

$ apt-get install proftpd<br /><br />$ vi /etc/proftpd/proftpd.conf<br /><blockquote>ServerType standalone<br />DefaultServer on<br />Defaultroot ~ nogroup</blockquote>$ vi /etc/rc.local<br /><blockquote>/etc/init.d/proftpd start</blockquote>
