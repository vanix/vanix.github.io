---
author: 歐巴計概
date: 2010-04-11 12:21:00.003000+00:00
layout: post
permalink: /2010/04/third-party-class-for-apk-using-eclipse.html
title: third-party class for apk using eclipse
---

還沒找到embed third-party class into apk的方法 0rz

在eclipse裡，properties -> build path -> add external JAR

即可在java裡import third-party class

但在emulator執行時，會顯示找不到third-party class的錯誤訊息

需要另外設定三個步驟，並且將apk安裝到自己的平台上測試

1. 將class檔案轉換成dalvik可讀取的dex格式

$ dx -dex --output=filename.jar xxx.class ...

2. cp filename.jar /system/framework

3. vi init.rc -

將/system/framework/file.jar加至BOOTCLASSPATH