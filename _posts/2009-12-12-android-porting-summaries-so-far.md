---
author: 歐巴計概
date: 2009-12-12 12:01:00.006000+00:00
layout: post
permalink: /2009/12/android-porting-summaries-so-far.html
published: false
title: android porting summaries so far
---

**kernel**

binder

framebuffer - double-buffering, pan display and RGB 454

ashmem

pmem - alloc physical memory for GPU or DSP

alarm

power manager

low memory

**android source**

use init.[ro.hareware].rc - this ro.hareware property is from /proc/cpuinfo

switch /dev/tty0 between KD\_TEXT and KD\_GRAPHIC

keymap - some parameters in qwerty.kl need power manager from kernel

battery check

bypass touch screen check in some App.

bypass network available check in some App. - check NetworkInfo and Connectivity Intent

sync - need network and correct date time, maybe also need DNS info from dhcpinfo

mount fake sd card - if execute these at start, take care the intent if the intent start or not

> setprop EXTERNAL\_STORAGE\_STATE mounted
>
> am broadcast -a android.intent.action.MEDIA\_MOUNTED --ez read-only false -d file:///sdcard

mount real sd card - need kernel support mmc and a correct vold.conf

mount ums storage - need to check code

Intent brordcast recivier - how to usr this, such fake sd card, and svc enable wifi and mobile network

enable wifi network - libhardware\_legecy, wpa\_supplicant and its config

audio - need kernel support alsa and external/alsa-lib...etc

bypass GoogleLoginSerive - need additional properties and independent of SetupWizard.apk

compile compatible shell on android

> 1. make in android source - put source into externel/ and write correct Android.mk
>
> 2. use Codesourary crosscompile to compile a static binary

TODO

how to make wifi device more stable on android

learn how to use android ndk

map other input device keycode to android keycode

add ethernet service into android

find out how to use ntp on android