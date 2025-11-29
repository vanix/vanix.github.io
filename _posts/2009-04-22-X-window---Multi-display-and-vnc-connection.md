---
author: 歐巴計概
date: 2009-04-22 01:40:00.003000+00:00
layout: post
permalink: /2009/04/x-window-multi-display-and-vnc.html
title: X window - Multi-display and vnc connection
---

**scenario 1**

display:0 with vino-server

vnc:1 + gnome-session

vnc:2 + gnome-session

...

vnc:n + gnome-session

Config

~/.vnc/xstartup

> #!/bin/sh
>
> # Uncomment the following two lines for normal desktop:
>
> unset SESSION\_MANAGER
>
> #exec /etc/X11/xinit/xinitrc
>
> [ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
>
> [ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
>
> xsetroot -solid grey
>
> vncconfig -iconic &
>
> xterm -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &
>
> gnome-session &

**scenario 2**

display:0 with vino-server

display:1 with vino-server

...

display:n with vino-server

Config

1. startx --number

2. 啟動gnome remote desktop (啟動vino-server)