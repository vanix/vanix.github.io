---
author: 歐巴計概
date: 2009-03-25 01:04:00.006000+00:00
layout: post
permalink: /2009/03/setup-environment-to-compile-metavnc-on.html
title: Setup environment to compile metavnc on Angstrom (ARM-base)
---

1. No xmkmf, imake and makedepend packages on Repo of Angstrom on gumstix

> Download <http://www.angstrom-distribution.org/repo/?pkgname=makedepend>

> Download [http://www.angstrom-distribution.org/repo/?pkgname=imake](http://www.angstrom-distribution.org/repo/?pkgname=makedepend)

> (bad method -> $ cp Angstrom on beagle的xmkmf, imake, makedepend to Angstrom on gumstix /usr/bin/)

better的解法可採用Repo of Angstrom on beagle

> http://www.angstrom-distribution.org/repo/ <---?

2. link paths of gcc shells

> $ cd /usr/sbin/
>
> $ ln -s arm-angstrom-linux-gnueabi-gcc gcc
>
> $ ln -s arm-angstrom-linux-gnueabi-g++ g++
>
> $ ln -s arm-angstrom-linux-gnueabi-cpp cpp
>
> 以此類推

3. 安裝developed library

> $ opkg install libboost-dev libxaw-dev libxmu-dev libz-dev libjpeg cpp(?) g++(?)

4. 缺少/usr/share/X11/config and /usr/share/font

> $ cp the two folder on ubuntu (x86) to Angstrom on gumstix

5. compile metavnc

> $ cd metavnc
>
> $ xmkmf
>
> $ make World