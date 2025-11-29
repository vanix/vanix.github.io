---
author: 歐巴計概
date: 2009-10-07 11:27:00.005000+00:00
layout: post
permalink: /2009/10/enable-home-key-on-android.html
title: enable home key on android
---

1.
cd /data/data/com.android.providers.settings/databases
sqlite3 settings.db
INSERT INTO secure (name, value) VALUES ('device\_provisioned', 1);
UPDATE "secure" SET value='0' WHERE name='device\_provisioned';

2.vi mydroid/build/target/board/system.prop
加上 keyguard.no\_require\_sim=1

~~3.~~
~~development/apps/SdkSetup/Android.mk~~
~~LOCAL\_MODULE\_TAGS := eng~~

~~4. frameworks/base/packages/SettingsProvider/src/com/android/providers/settings/DatabaseHelper.java~~