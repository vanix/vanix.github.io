---
author: 歐巴計概
date: 2025-04-11 08:08:00.002000+00:00
layout: post
permalink: /2025/04/dlib-and-ffmpeg-on-macos.html
title: dlib and ffmpeg on MacOS
---

不知道更新到什麼東西，導致無法使用dlib了

電腦環境

MacOS 15.3.2 Python 3.11.5

目前測出可用的Workaround如下

$ pip install dlib==19.24.4

$ brew install ffmpeg@6

$ sudo cp -r /opt/homebrew/opt/ffmpeg@6 /opt/homebrew/opt/ffmpeg