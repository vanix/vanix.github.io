---
author: 歐巴計概
date: 2010-02-25 05:27:00.001000+00:00
layout: post
permalink: /2010/02/gerrit-on-freebsd-8.html
title: Gerrit on Freebsd 8
---

準備好jdk16 on Freebsd之後，可以開始動工了

ref:

<http://gerrit.googlecode.com/svn/documentation/2.1/index.html>

<http://blog.cyberion.net/2009/11/my-take-on-installing-gerrit-git-code-review-tool-on-ubuntu.html>

<http://unethicalblogger.com/node/241>

<http://github.com/guides/providing-your-ssh-key>

**Initialize the Site**

> sudo adduser gerrit2
> sudo su gerrit2
> cd ~gerrit2
> fetch http://gerrit.googlecode.com/files/gerrit-2.1.1.1.war
> java -jar gerrit-2.1.1.1.war init -d review\_site
> 依照步驟設定database, ssh, http...etc

**Start/Stop Daemon** - ssh跟http的服務在此時啟動

> review\_site/bin/gerrit.sh start
>
> review\_site/bin/gerrit.sh stop
>
> review\_site/bin/gerrit.sh restart
>
> 我這台機器的perl，會導致gerrit.sh無法start
>
> 因此刪除或註解這幾行 in review\_site/bin/gerrit.sh
>
> if test -x /usr/bin/perl ; then
>
> # If possible, use Perl to mask the name of the process so its
>
> # something specific to us rather than the generic 'java' name.
>
> #
>
> RUN\_EXEC=/usr/bin/perl
>
> RUN\_Arg1=-e
>
> RUN\_Arg2='$x=shift @ARGV;exec $x @ARGV;die $!'
>
> RUN\_Arg3="-- $JAVA GerritCodeReview"
>
> else
>
> fi

**Project Setup**

> Open browser to connect http://domain:8080/#admin,projects
>
> 第一次進去網頁時或在Setting可設定Contact Information, SSH Keys
>
> Contact Information > full name
>
> SSH Keys > SSH Username, Add Key and copy server host key to local machine
>
> generate key的部份參考http://github.com/guides/providing-your-ssh-key

**Setting git config at local machine**

> git config --global user.name "Contact Information的full name"
>
> git config --global user.email "Contact Information的email"
>
> 這些設定儲存在~/.gitconfig，此外這設定可解決git push的"you are not committer"的問題

**Create repository through ssh**

> ssh -p 29418 review.example.com gerrit create-project --name new/project

**Setting the repository permission through web ui**

> Admin > projects > choose project name > Access > Add Access Right
>
> 新增Verify及Push Branch

**Get the repository**

> git clone ssh://username@domain:29418/projectname
>
> if this project is empty
>
> cd projectname
>
> work...
>
> git add .
>
> git commit -m 'comment'
>
> git push origin master

**Create change**

> cd projectname
>
> git add .
>
> git commit -m 'comment'
>
> git push ssh://username@domain:29418/projectname HEAD:refs/for/master

**Create branch**

> cd projectname
>
> git branch branchname //建立branch
>
> git push ssh://username@domain:29418/projectname branchname