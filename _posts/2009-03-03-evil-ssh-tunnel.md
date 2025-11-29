---
author: 歐巴計概
date: 2009-03-03 09:01:00.003000+00:00
layout: post
permalink: /2009/03/evil-ssh-tunnel.html
title: evil ssh tunnel
---

for example

ssh -NfR 36900:"某ip":22 user@moon

so... 在moon機器底下輸入

moon> ssh 127.0.0.1 -p 36900

則會連上某ip指定的pc

同理把22改成其他服務，也可使用

ex:VNC

sshd\_config設定說明

> AllowTCPForwarding yes
>
> GatewayPorts yes
>
> TCPKeepAlive yes
>
> ClientAliveInterval 100(?)
>
> PermitTunnel yes

另外sshd有些主機無法連上的問題

> UseDNS no