---
author: 歐巴計概
date: 2010-01-05 03:49:00.009000+00:00
layout: post
permalink: /2010/01/setup-git-server-on-freebsd.html
title: setup git server on Freebsd
---

**Part.1.1 Using Git without http

install git server**
> $ cd /usr/port/devel/git
>
> $ make install clean

**modify /etc/rc.conf**

> git\_daemon\_enable="YES"
>
> git\_daemon\_directory="/usr/local/git/repo"
>
> git\_daemon\_flags="--export-all --syslog --enable=receive-pack --listen=ip\_address –verbose "

**add user - git**

> $ pw user add git
>
> $ passwd git

**start git daemon**

> $ /usr/local/etc/rc.d/git\_daemon start

**build local repository**

> $ mkdir /usr/local/git/repo/mydroid.git
>
> $ cd /usr/local/git/repo/mydroid.git
>
> $ git --bare init
>
> $ chown -R git mydroid.git
>
> $ chgrp -R git mydroid.git

**commit to remote repository**

> $ mkdir mydroid.git
>
> $ cd mydroid.git
>
> $ git init
>
> $ cp mydroid directory to this folder
>
> $ git add mydroid/
>
> $ git commit -m 'first commit'
>
> $ git remote add origin git@REMOTE\_SERVER:/usr/local/git/repo/mydroid.git
>
> $ git push origin master

將android source code git至自己的server時，必須先把原有的.git/刪除

才能夠順利git commit

Part.1-2 Using Git with http

**install apache server and start server**

> $ cd /usr/port/www/apache22
>
> $ make install
>
> $ echo apache22\_enable="YES" > /etc/rc.conf
>
> $ hostname localhost (because I don't have any DN)
>
> $ /usr/local/etc/rc.d/apache22 start

**configure httpd.conf**

> ServerName ip\_address
>
> DavLockDB "/usr/local/var/DavLock/DAVLockDB"
>
> DAV on
>
> AuthType Basic
>
> AuthName "Git"
>
> AuthUserFile /usr/local/etc/apache22/passwd.git
>
> Require valid-user

**init git repository at www directory**

> $ cd /usr/local/www/apache22/data
>
> $ mkdir mydroid.git
>
> $ cd mydroid.git
>
> $ git --bare init
>
> $ git update-server-info
>
> $ chown -R www:www .
>
> $ htpasswd -c /usr/local/etc/apache22/passwd.git git

**test dav using cadaver**

> $ cd /usr/port/www/cadaver
>
> $ make install clean
>
> $ cadaver http://ip\_address/mydroid.git

**setup the client**

> $ vi ~/.netrc
>
> machine ip\_address
>
> login username
>
> password passwd
>
> $ chmod 600 ~/.netrc
>
> $ curl --netrc --location -v http://usename@servername/mydroid.git/HEAD (測試是否設定成功)
>
> $ git init
>
> $ git config remote.upload.url http://username@servername/mydroid.git/
>
> $ touch test
>
> $ git add .
>
> $ git commit -m 'test'
>
> $ git push upload master
>
> (一開始repo沒資料的話, 直接下git push會失敗, 先建立master之後才能git push)

Part.2.1 setup Gitweb

**install git with gitweb**

> **$ cd /usr/ports/devel/git**
>
> **$ make config
>
> 將gitweb項目打勾
>
> $ make install**

****install and configure apache**

> 參考Part.1-2相關步驟

**configure gitweb**

> $ mkdir /usr/local/www/apache22/data/gitweb
>
> $ cp /usr/local/share/examples/git/gitweb/\* /usr/local/www/apache22/data/gitweb

**create /usr/local/etc/gitweb.conf**

> $feature{'blame'}{'default'} = [undef];
>
> $feature{'pickaxe'}{'default'} = [undef];
>
> $feature{'search'}{'default'} = [undef];
>
> $feature{'grep'}{'default'} = 1;
>
> $feature{'snapshot'}{'default'} = ['tgz', 'gzip', 'zip'];
>
> $feature{'snapshot'}{'override'} = 1;
>
> $projects\_list = $projects\_list = $projectroot;
>
> $export\_ok = "";
>
> $strict\_export = "true";
>
> $site\_name = "The Average Geek's Git Repo";
>
> $fallback\_encoding = 'utf-8';
>
> @stylesheets = ("gitweb.css");
>
> $projects\_list\_description\_width = 50;
>
> # This lets it make the URLs you see in the header
>
> @git\_base\_url\_list = ( 'git://my.domain.com');
>
> # Title
>
> $home\_link\_str = 'The Average Geek';
>
> # nicer-looking URLs
>
> $feature{'pathinfo'}{'default'} = [1];
>
> $my\_uri = "http://my.domain.com/gitweb/gitweb.cgi";
>
> $home\_link = "http://my.domain.com/gitweb/";

**configure httpd.conf with gitweb support**

> Alias /gitweb/ /usr/local/www/apache22/data/gitweb/
>
> RewriteEngine On
>
> RewriteRule ^gitweb$ gitweb/ [R]
>
> SetEnv GITWEB\_CONFIG /usr/local/etc/gitweb.conf
>
> AllowOverride AuthConfig
>
> Options +ExecCGI +Indexes
>
> Order allow,deny
>
> Allow from all
>
> DirectoryIndex gitweb.cgi
>
> SetEnv GITWEB\_CONFIG "/usr/local/etc/gitweb.conf"
>
> AddHandler cgi-script .cgi
>
> RewriteEngine On
>
> RewriteBase /gitweb/
>
> RewriteCond %{REQUEST\_FILENAME} !-f
>
> RewriteCond %{REQUEST\_FILENAME} !-d
>
> RewriteRule ^.\* /gitweb.cgi/$0 [L,PT]

重新啟動apache, 大功告成

gitweb ref: http://ask.metafilter.com/120273/Getting-redirects-to-work-in-Apache-for-Gitweb**