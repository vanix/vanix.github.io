---
author: 歐巴計概
date: 2009-03-19 02:52:00.005000+00:00
layout: post
permalink: /2009/03/rsync-note.html
title: rsync note
---

rsync server (debian)

$ apt-get install rsync

$ vi /etc/rsyncd.conf

[vanix\_mac]
> path = /home/vanix/rsync/
> uid = vanix
> gid = vanix
> auth users = vanix\_mac
> secrets file = /etc/rsyncd.secrets

其他預設設定不動

$ vi /etc/rc.local
> /usr/bin/rsync --daemon

$ vi /etc/rsyncd.secrets
> auth\_user:password

$ chown root.root rsyncd.secrets

$ chmod 600 rsyncd.secrets

rsync client

~~$ rsync -rvlHpogDts ~/ vanix\_mac@ip:vanix\_mac~~
update: $ rsync -rvlHpogDtS ~/ vanix\_mac@ip::vanix\_mac

解釋--> rsync 參數 source\_directory auth\_user@ip:module\_name

取回rsync的檔案

$ rsync -azv vanix\_mac@ip::vanix\_mac/ ~/

解釋--> rsync -azv <帳號>@<主機名稱>::<模組名稱>/<檔案或是目錄名稱> <目的位置>