---
author: 歐巴計概
date: 2011-10-24 09:32:00.004000+00:00
layout: post
published: false
title: MIPSAndroid Note
---

\* prepare

arribaandroid\_eclair/mips-froyo

sigmakernel (optional)

mips-4.3

sigma vendor for eclair/froyo

tftp server and nfs server on britannia

\* compilation

\*\* eclair

get arriba.mipsel-eclair-vantage8654.sh

./arriba.mipsel-eclair-vantage8654.sh

cd workspace.mipsel-eclair-vantage8654/Arriba\_for\_Vantage\_8545\_Android\_Eclair

make download-android

make build-android

\*\* froyo

get mips-froyo from MIPSAndroid

add .repo/local\_manifest.xml

==

==

repo sync again

$ . ./vendor/sigma/smp86xx/vendorsetup.sh

$ chip

choose 8654, production, DTS

\* system startup with kernel from tftp server and rootfs from nfs server

copy prebuild/kernel/vmlinux.bin to tftp server

copy android/out/target/product/smp86xx/ root and system to nfs server

(make sure that permission is set correctly)

send boot command to board via minicom/screen

==

net init; load -b tftp://140.96.111.38/vmlinux.bin 0x84000000; \

go . root=/dev/nfs nfsroot=140.96.111.38:/home/vanix/android\_nfs \

ip=140.96.111.168:::::eth0:none: rdinit=/none init=/init console=ttyS0 \

mem=192M androidboot.hardware=smp86xx

==

connect HDMI output to TV

other

keyboard work fine

modify ir code mapping

nfs server setting

/home/vanix/android\_nfs \*(rw,no\_root\_squash,sync)

kernel exception

objcopy -O vmlinux.bin -R .note -R .note.gnu.build-id -R .comment -S vmlinux

缺什麼東西

virtual\_input.ko for 2.6.29

em8xxx\* source code including fb