---
author: 歐巴計概
date: 2010-01-04 03:40:00.005000+00:00
layout: post
permalink: /2010/01/test-android-ndk-sample.html
title: test android NDK sample
---

http://developer.android.com/sdk/ndk/1.6\_r1/index.html

**setup the environment**

$ cd ndk\_directory

$ ./build/host-setup.sh

**compile sample share library**

$ cd ndk\_directory

$ make APP=hello-jni

**open android project by eclipse**

重新compile .so之後必須對著project點refresh

**modify android platform compatibility**

不同的API Level改變不同minSdkVersion的值

ex: android 1.5 = 3

ex: android 1.6 = 4