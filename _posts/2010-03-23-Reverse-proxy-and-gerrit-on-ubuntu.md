---
author: 歐巴計概
date: 2010-03-23 10:42:00.001000+00:00
layout: post
permalink: /2010/03/reverse-proxy-and-gerrit-on-ubuntu.html
title: Reverse proxy and gerrit on ubuntu
---

gerrit.conf
> [gerrit]
>         basePath = git
>         canonicalWebUrl = http://140.96.111.36/review/
> [database]
>         type = H2
>         database = db/ReviewDB
> [auth]
>         type = OpenID
> [sendemail]
>         smtpServer = localhost
> [container]
>         user = gerrit2
>         javaHome = /usr/lib/jvm/java-6-sun-1.6.0.15/jre
> [sshd]
>         listenAddress = \*:29418
> [httpd]
>         listenUrl = proxy-http://127.0.0.1:8081/
> [cache]
>         directory = cache

額外補充
~/.h2.server.properties
0=Generic H2 |org.h2.Driver|jdbc:h2:/usr/home/gerrit2/review\_site/db/ReviewDB;FILE\_LOCK=NO;AUTO\_SERVER=FALSE;DB\_CLOSE\_ON\_EXIT=FALSE|

httpd.conf (下列設定設定在VirtualHost裡)
>     ProxyRequests Off
>     ProxyVia Off
>     ProxyPreserveHost On
>         Order deny,allow
>         Deny from all
>         Allow from x.x.x.0/255.255.255.0
>   ProxyPass /review/ http://127.0.0.1:8081/