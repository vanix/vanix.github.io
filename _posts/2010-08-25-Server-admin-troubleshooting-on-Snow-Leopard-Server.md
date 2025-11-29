---
author: 歐巴計概
date: 2010-08-25 07:53:00.003000+00:00
layout: post
permalink: /2010/08/server-admin-trouble-shooting-on-snow.html
title: Server admin troubleshooting on Snow Leopard Server
---

設定 Snow Leopard Server 時，不小心把dns搞爛了

結果Server admin再也連不上server

從/var/log/system.log裡可以看到

> ReportCrash[1665:2a5b] Saved crash report for servermgrd[1676] version ??? (???) to /Library/Logs/DiagnosticReports/servermgrd\_2010-08-25-003012\_localhost.crash

表示Mac OS X Server administrative daemon爛掉了

雖然看不懂crash report，但是從裡面看到/usr/share/servermgrd/這個重要的路徑

servermgrd/bundle/裡面有所有service的plugin

直接把servermgr\_dns.bundle移至上層目錄，重跑servermgrd應該可以正常運作

不過這樣不是比較好的解法

另外嘗試從/private/var/db/launchd.db/com.apple.launchd/overrides.plist關掉org.isc.named

雖然named開機後不會自動啟動，但Server admin依然無法運作

可能原因應該是servermgr\_dns還是會檢查/var/named/的config

所以最後使出大絕，把/var/named/db\*及/var/named/zone/db\*全數刪除

Server admin終於恢復正常...開始重搞dns....