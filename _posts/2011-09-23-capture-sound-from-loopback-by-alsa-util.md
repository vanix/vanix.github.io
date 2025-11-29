---
author: 歐巴計概
date: 2011-09-23 10:05:00.002000+00:00
layout: post
permalink: /2011/09/capture-sound-from-loopback-by-alsa.html
published: false
title: capture sound from loopback by alsa-util
---

Test on Ubuntu 11.04

$ modprobe snd-aloop

$ vi .asoundrc

> pcm.!default {
>     type hw
>     card 1
>     device 0
> }

$ mplayer -ao alsa some.mp3

$ arecord -D hw:1,1 -f cd | aplay -D hw:0 -f cd

假如同時播放好幾個影音

$ mplayer -ao alsa some.mp3

$ arecord -D hw:1,1,0 -f cd | aplay -D hw:0 -f cd

$ mplayer -ao alsa some.mp4

$ arecord -D hw:1,1,1 -f cd | aplay -D hw:0 -f cd

Porting snd-aloop.ko to arm platform
1. git clone the kernel source is provided by rowboat
2. download alsa-driver
3. patch aloop.c from alsa-driver to kernel
4. make ARCH=arm omap3\_beagle\_android\_defconfig
5. make menuconfig, check SND-ALOOP to built-in
6. make ARCH=arm CROSS\_COMPILE=xxxx uImage

Test on beagleboard xm, rowboat-gingerbread
1. 修改asound.conf
> config參考後述config章節
> 要注意alsa device的編號
> 本例中, card0為loopback, card1為音效卡

2.
example 1: 預設播放裝置改為Loopback
因此android完全不會有音效, 只能透過arecord擷取出loopback的音效

$ alsa\_arecord -D hw:0,1 -f cd | alsa\_aplay -D hw:1 -f cd

example 2: 將聲音同時導向loopback及音效卡
因此android會有音效, 同時也能夠從loopback擷取音效
在此直接將檔案擷取成wave, 並且驗證是否有音效
$ alsa\_arecord -D hw:0,1 -f cd alsaout.wav

other cmd:

alsamixer (ubuntu)

amixer (ubuntu)

alsa\_aplay (android)
alsa\_arecord (android)
alsa\_amixer (android)
alsa\_ctl (android)

config:
> pcm.!default { #example 1.
>     type hw
>     card 0
>     device 0
> }

> pcm.!default{ #example 2.
> type plug
> slave.pcm mdev
> route\_policy "duplicate"
> }
>
> pcm.mdev {
> type multi
> slaves.a.pcm "hw:Loopback,0,0"
> slaves.a.channels 2
> slaves.b.pcm "hw:1,0"
> slaves.b.channels 2
> bindings.0.slave a
> bindings.0.channel 0
> bindings.1.slave a
> bindings.1.channel 1
> bindings.2.slave b
> bindings.2.channel 0
> bindings.3.slave b
> bindings.3.channel 1
> }

note:
.asoundrc
cat /proc/asound/cards
cat /proc/asound/devices

TODO:

把聲音同時丟到loopback, 以及音效卡的playback (done 11/10/03)

ref:

<https://bbs.archlinux.org/viewtopic.php?id=97598>

<http://ubuntuforums.org/showthread.php?t=914405>

<http://www.alsa-project.org/main/index.php/Asoundrc>
<http://ffmpeg.org/sample.html>
<http://rxwen.blogspot.com/2010/05/use-ffmpeg-to-setup-streaming-server-on.html>