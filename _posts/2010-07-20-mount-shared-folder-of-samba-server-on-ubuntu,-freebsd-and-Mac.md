---
author: 歐巴計概
date: 2010-07-20 06:59:00+00:00
layout: post
permalink: /2010/07/mount-shared-folder-of-samba-server-on.html
title: mount shared folder of samba server  on ubuntu, freebsd and Mac
---

@ ubuntu

smbmount //ip/volume /des -o user=username

@ freebsd

mount\_smbfs -I ip //username@custom\_name/volume /des

@ Mac

press cmd+k in finder

type smb://ip