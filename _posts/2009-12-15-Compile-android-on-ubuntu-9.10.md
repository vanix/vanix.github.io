---
author: bin
date: 2009-12-15 04:42:00.003000+00:00
layout: post
permalink: /2009/12/compile-android-on-ubuntu-910.html
title: Compile android on ubuntu 9.10
---

1.
vi build/tools/findleaves.sh
#find "${@:0:$nargs}" $findargs -type f -name "$filename" -print |
find "${@:1:$nargs-1}" $findargs -type f -name "$filename" -print |

2.
apt-get install gcc-4.3 g++-4.3
rm /usr/bin/gcc /usr/bin/g++
ln -s /usr/bin/gcc-4.3 /usr/bin/gcc
ln -s /usr/bin/g++-4.3 /usr/bin/g++

look like a problem about complier version. orz