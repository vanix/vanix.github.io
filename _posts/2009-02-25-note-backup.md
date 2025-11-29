---
author: 歐巴計概
date: 2009-02-25 06:22:00.006000+00:00
layout: post
permalink: /2009/02/note-backup.html
published: false
title: note backup
---

X Toolkit 去除邊框及title

XtVaCreatePopupShell()

要加上 XtNoverrideRedirect, 1,

如要去除vncviewer的邊框

則更改vncviewer.c 的 XtVaAppInitalize

加上XtNoverrideRedirect, 1

更改Dock 小圓點

要先改名成對應的名稱

indicator\_large.png之類的

然後認證

開終端機執行 killall Dock 按ente

VLC note

VLC server

vlc test01.mpg --sout #transcode{vcodec=mp1v,vb=800,scale=1,acodec=mpga,ab=128,channels=2}:duplicate{dst=display,dst=rtp{dst=140.96.111.214,mux=ts,port=1234}}

VLC client

vlc -vvv rtp://

VLC for mac

還無法發/收 stream, 不確定原因

svn note

svn checkout http://url/

enter the directory

svn update

svn add myfile.c

svn commit -m "comments for this commit"