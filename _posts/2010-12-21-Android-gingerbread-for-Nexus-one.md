---
author: 歐巴計概
date: 2010-12-21 09:36:00.006000+00:00
layout: post
permalink: /2010/12/sign-apk.html
title: Android gingerbread for Nexus one
---

使用Android gingerbread的device/htc/passion編出一個給Nexus one的版本

update: 20101224
用warrper解決編譯問題

1. libcameraservice -> cameraif (warrper) -> libcamera.so (2.2)

問題看來是與HAL接口的function改名

ref: <http://pixass.online.ac/android:nexusone>

2. 直接編譯passion就ok啦～
note:
$ . build/envsetup.sh
$ lauch
$ unzip-file.sh passion-update.zip
$ make

白螢幕問題尚未解決，看網路上提供的ROM已經解決了...真是太厲害了...

dirty版本
@ root of android gingerbread source tree
1. 先編譯passion
2. unzip-file.sh passion-update.zip (這邊用2.2的版本)
3. 再編譯一次passion
4. 此時用編好的img燒錄至Nexus one，雖然大多看起來正常運作，但Camera畫面一片空白
於是...
5. 從xda撿到libcameraservice.so
(目前看起來是frameworks/base/services/camera/libcameraservice編譯有問題，需要libcamera.so for 2.3）

6. 取代原本編好的libcameraservice.so
finish!

目前Camera可用，其他靈異現象有待觀察

BTW

試裝Vending.apk，Gmail.apk from passion-update.zip

測試抓NinjaJump OK!

明天要在板子上試試看了

Appendix:
Sign apk with platform key

ref: <http://merckhung.blogspot.com/2009/08/sign-android-apk-with-platform-key-to.html>

ex:

java -jar out/host/linux-x86/framework/signapk.jar build/target/product/security/platform.x509.pem build/target/product/security/platform.pk8 /home/vanix/app/xxx.apk /home/vanix/app/xxx\_signed.apk