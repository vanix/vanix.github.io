---
author: 歐巴計概
date: 2009-04-22 02:02:00.006000+00:00
layout: post
permalink: /2009/04/share-app-between-linux-machines.html
title: share app between Linux machines
---

List: xmove, xpra, ssh X11 forwarding, shareappvnc, guievict, freeNX

**\*xmove** - 必須照流程設定

Server A

> unset DISPLAY
>
> xmove &
>
> export DISPLAY=ip(or dn):display\_number
>
> xterm &
>
> xeyes &
>
> xmovectrl -list

Host B

> vi /etc/gdm/gdm.conf -> DisallowTCP=false
>
> (x need to restart)
>
> xhost +Server A ip

Server A

> xmovectrl -moveall Host B ip(or dn)
>
> vi /etc/gdm/gdm.conf -> DisallowTCP=false
>
> (x need to restart)
>
> xhost + Host B ip
>
> xmovectrl -moveall Server A ip(or dn)

**\*xpra**

compile

> $ apt-get install libx11-dev libxtst-dev libxcomposite-dev \
>
> libxdamage-dev python-gobject-dev python-gtk2-dev xvfb python-pyrex
>
> $ wget http://partiwm.org/static/downloads/parti-all-0.0.5.tar.gz
>
> $ tar xvzf parti-all-0.0.5.tar.gz
>
> $ cd parti-all-0.0.5
>
> $ ./do-build
>
> $ export PYTHONPATH=$PWD/install/lib/python:$PYTHONPATH

Server A

> $ install/bin/xpra start :13
>
> $ export DISPLAY=:13
>
> $ firefox &
>
> $ xterm &
>
> $ install/bin/xpra attach :13 (顯示:13的app)
>
> $ vi ~/.xpra/run-xpra ->
>
> exec /home/vanix/parti-all-0.0.5/install/bin/xpra "$@"

Host B

> $ install/bin/xpra attach ssh:server A ip:13

**\*ssh X11 forwarding**

> $ vi /etc/ssh/sshd\_config -> X11Forward=yes
>
> $ ssh -X server\_ip
>
> $ exec\_app

**\*shareappvnc (under construction)**

guievict, freeNX (under construction)