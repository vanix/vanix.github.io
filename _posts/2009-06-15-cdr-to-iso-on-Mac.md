---
author: 歐巴計概
date: 2009-06-15 09:17:00.004000+00:00
layout: post
permalink: /2009/06/cdr-to-iso-on-mac.html
title: cdr to iso on Mac
---

update: 直接用disk utility燒錄cdr就可以了... 0rz

純粹只是cdr檔案轉成iso
> hdiutil makehybrid -iso -joliet -o FILENAME.iso FILENAME.cdr

另外一個是將檔案轉成cdr之後再轉成iso
reference: [Convert .cdr to .iso Mac OSX 10.5 (leopard)](http://blog.andypeters.org/post/49316583/convert-cdr-to-iso-in-mac-leopard)
> 1 - Go into Disk Utility and highlight the CD which is in the drive.
> 2 - Click “New Image” in the toolbar up above.
> 3 - Image format should be “DVD/CD master”. Name it whatever you want and save it where you like.
> 4 - Wait.
> 5 - When that is done, open up your Terminal.
> 6 - Goto the path where you saved it (ie: “cd ~/Desktop”).
> 7 - Issue this command:
> hdiutil makehybrid -iso -joliet -o FILENAME.iso FILENAME.cdr
> 8 - Rejoice and burn your ISO. Or just burn your CDR since Mac’s support that.