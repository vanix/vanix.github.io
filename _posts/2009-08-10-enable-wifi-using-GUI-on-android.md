---
author: 歐巴計概
date: 2009-08-10 08:47:00.010000+00:00
layout: post
permalink: /2009/08/enable-wifi-used-gui-on-android.html
title: enable wifi using GUI on android
---

**Kernel**

將wireless adapter driver編成module, 放置android fs的/system/lib/modules

**The patches for android source**

$ vi external/wpa\_supplicant/Android.mk

> WPA\_BUILD\_SUPPLICANT := true

$ vi external/wpa\_supplicant/.config

> CONFIG\_DRIVER\_WEXT=y

$ vi build/target/board/generic/system.prop

> wifi.interface=wlan0

$ vi hardware/libhardware\_legacy/wifi/wifi.c

> //vanix
>
> static const char DRIVER\_MODULE\_NAME[] = "zd1211";
>
> static const char DRIVER\_MODULE\_TAG[] = "zd1211 ";
>
> static const char DRIVER\_MODULE\_PATH[] = "/system/lib/modules/zd1211rw.ko";
>
> //註解wifi\_load\_driver function
>
> int wifi\_load\_driver()
>
> {
>
> char driver\_status[PROPERTY\_VALUE\_MAX];
>
> int count = 100; /\* wait at most 20 seconds for completion \*/
>
> return 0;
>
> /\*
>
> if (check\_driver\_loaded()) {
>
> return 0;
>
> }
>
> if (insmod(DRIVER\_MODULE\_PATH) <>
>
> return -1;
>
> property\_set("ctl.start", FIRMWARE\_LOADER);
>
> sched\_yield();
>
> while (count-- > 0) {
>
> if (property\_get(DRIVER\_PROP\_NAME, driver\_status, NULL)) {
>
> if (strcmp(driver\_status, "ok") == 0)
>
> return 0;
>
> else if (strcmp(DRIVER\_PROP\_NAME, "failed") == 0)
>
> return -1;
>
> }
>
> usleep(200000);
>
> }
>
> property\_set(DRIVER\_PROP\_NAME, "timeout");
>
> return -1;
>
> \*/
>
> }

$ vi frameworks/base/wifi/java/android/net/wifi/WifiStateTracker.java

> private static final boolean LOCAL\_LOGD = Config.LOGD || true;

**The patches for android fs**

$ vi init.rc

> #wifi
>
> mkdir /data/misc/wifi 0770 wifi wifi
>
> mkdir /data/misc/wifi/sockets 0770 wifi wifi
>
> mkdir /data/system/wpa\_supplicant 0770 wifi wifi
>
> mkdir /data/misc/dhcp 0770 dhcp dhcp
>
> chown dhcp dhcp /data/misc/dhcp
>
> #service name一定要是wlan\_loader
>
> service wlan\_loader /sbin/wlan\_loader
>
> oneshot
>
> disable
>
> service wpa\_supplicant /system/bin/wpa\_supplicant -Dwext -iwlan0 -c /system/etc/wifi/wpa\_supplicant.conf
>
> group system wifi
>
> disabled
>
> oneshot
>
> service dhcpcd /system/bin/dhcpcd wlan0
>
> group system dhcp
>
> disabled
>
> oneshot

$ vi /sbin/wlan\_load

> #!/system/bin/sh
>
> insmod /system/lib/modules/zd1211rw.ko

$ vi /system/etc/wifi/wpa\_supplicant.conf

> ctrl\_interface=DIR=/data/system/wpa\_supplicant GROUP=system
>
> update\_config=1
>
> # 如果有紀錄加入過的網路的話, 會自動出現在檔案下方
>
> network={
>
> ssid="W320AP4"
>
> key\_mgmt=NONE
>
> }
>
> network={
>
> ssid="Mtube5566"
>
> psk="password"
>
> proto=RSN
>
> key\_mgmt=WPA-PSK
>
> group=CCMP TKIP
>
> priority=4
>
> }