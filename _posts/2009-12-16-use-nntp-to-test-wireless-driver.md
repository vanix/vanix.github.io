---
author: bin
date: 2009-12-16 10:04:00.005000+00:00
layout: post
permalink: /2009/12/use-nntp-to-test-wireless-driver.html
title: use nntp to test wireless driver
---

server mac ----> client arm board

**Test 1 (ttcp-t: buflen=8192, nbuf=91920, align=16384/0, port=5001)**

sender - my notebook

ttcp -t -s -n91920 10.0.1.7

receiver - target board

ttcp -r -s

result:

ttcp-t: 753008640 bytes in 251.02 real seconds = 2929.49 KB/sec +++

ttcp-t: 91920 I/O calls, msec/call = 2.80, calls/sec = 366.19

ttcp-t: 0.1user 7.9sys 4:11real 3% 0i+0d 182272maxrss 0+3pf 31977+12361csw

同時傳送及接收

ttcp-t: 753008640 bytes in 605.00 real seconds = 1215.47 KB/sec +++

ttcp-t: 91920 I/O calls, msec/call = 6.74, calls/sec = 151.93

ttcp-t: 0.6user 57.8sys 10:05real 9%

ttcp-r: 753008640 bytes in 865.00 real seconds = 850.13 KB/sec +++

ttcp-r: 168399 I/O calls, msec/call = 5.26, calls/sec = 194.68

ttcp-r: 1.3user 89.4sys 14:25real 10%

**Test 2**

sender - my notebook

tar cf - Downloads/ | ttcp -t 10.0.1.4

receiver - target board

ttcp -r -B | tar xvpf -

目前使用的ralink會出現error

> BulkIn IRP Pending!!!
>
> BulkIn IRP Pending!!!
>
> BIRIdx(7): RXDMALen not multiple of 4.[113], BulkInBufLen = 20360)
>
> 0:3 LTL=0 , TL=0 L:0
>
> 0:3 LTL=0 , TL=0 L:0
>
> 0:3 LTL=0 , TL=0 L:0
>
> Qidx(0), not enough space in MgmtRing, MgmtRingFullCount=1!
>
> Qidx(0), not enough space in MgmtRing, MgmtRingFullCount=2!