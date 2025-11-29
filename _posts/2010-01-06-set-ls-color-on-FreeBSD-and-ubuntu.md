---
author: 歐巴計概
date: 2010-01-06 17:09:00.004000+00:00
layout: post
permalink: /2010/01/set-ls-color-on-freebsd-and-ubuntu.html
title: set ls color on FreeBSD and ubuntu
---

**Set ls color on FreeBSD using tcsh**
> $ echo "alias ls ls -GF" >> ~/.cshrc
>
> $ echo "setenv LSCOLORS Cxfxcxdxbxegedabagacad" >> ~/.cshrc
>
> $ source ~/.cshrc

ref: about color value, please man ls

**Set ls color on ubuntu using bash**

> $ vi ~/.bashrc
>
> alias ls='ls -F --color=auto'
>
> $ dircolors --print-database >> .dircolors
>
> $ vi .dircolors (change colors you like)
>
> $ source .dircolors

add color support for other file format

ex: export LS\_COLORS=$LS\_COLORS:"\*.wma=01;35":"\*.m4a=01;35"

ref: about color value, <http://www.linux-sxs.org/housekeeping/lscolors.html>