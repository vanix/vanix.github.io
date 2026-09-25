---
author: 歐巴計概
date: 2025-04-11 08:08:00.002000+00:00
layout: post
permalink: /2025/04/dlib-and-ffmpeg-on-macos.html
title: dlib and ffmpeg on MacOS
description: "MacOS 15.3.2 更新後 dlib 無法使用的修復方法：pip install dlib==19.24.4、brew install ffmpeg@6，再把 ffmpeg@6 複製為 /opt/homebrew/opt/ffmpeg。"
---
💡 dlib 修復重點速記

MacOS 更新後 dlib 無法使用的解法：執行 pip install dlib==19.24.4、brew install ffmpeg@6，並用 sudo cp -r 把 ffmpeg@6 複製為 /opt/homebrew/opt/ffmpeg。

不知道更新到什麼東西，導致無法使用dlib了

電腦環境

MacOS 15.3.2 Python 3.11.5

目前測出可用的Workaround如下

$ pip install dlib==19.24.4

$ brew install ffmpeg@6

$ sudo cp -r /opt/homebrew/opt/ffmpeg@6 /opt/homebrew/opt/ffmpeg
