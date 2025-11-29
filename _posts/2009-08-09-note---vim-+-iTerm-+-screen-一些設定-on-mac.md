---
author: 歐巴計概
date: 2009-08-09 07:20:00.006000+00:00
layout: post
permalink: /2009/08/note-vim-iterm-screen-on-mac.html
title: note - vim + iTerm + screen 一些設定 on mac
---

iTerm+screen+vim 支援256色跟syntax on

$vi ~/.vimrc

set t\_Co=256 # 設定支援256色

set encoding=utf-8

set paste # 支援貼上模式 (copy前先按F9，copy後再按一次F9來回復)

let python\_highlight\_all = 1 # 支援更多python語法, 搭配[python.vim](http://www.vim.org/scripts/download_script.php?src_id=9293), 放至~/.vim/syntax/

syntax on

colorscheme wombat256 # [wombat256.vim](http://www.vim.org/scripts/download_script.php?src_id=9587), 放至~/.vim/colors/

$vi ~/.screenrc

termcapinfo xterm 'Co#256:AB=\E[48;5;%dm:AF=\E[38;5;%dm'

iTerm

Bookmarks-> Manage Profiles-> Terminal Profiles-> Default-> Type-> xterm-256color