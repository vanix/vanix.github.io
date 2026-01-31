---
author: 歐巴計概
layout: post
title: "Mac mini的Moltbot安裝，並且串接Telegram"
date: 2026-01-30
permalink: /2026/01/mac-moltbot-telegram-reminder.html
categories: [教學, moltbot]
tags: [mac, moltbot, clawdbot, telegram, reminder, 教學]
---

# 前言

Moltbot 是一款以 Node.js 編寫的多通道聊天機器人框架，它能輕鬆串接各種通訊平台、外部 API 以及自動化工作。本文將示範如何：

1. 在Mac本機裡安裝與設定 Moltbot  
2. 串接 Telegram Bot  
3. 透過 Telegram Bot指派任務

> 手邊剛好有台Mac mini M2 16GB，這幾天剛裝好，趁還有印象的時候趕快來記錄一下，如果有一些疏漏，請見諒
> 通訊部分測試了Telegram跟Line，Telegram設定非常簡單，建議先串接Telegram
> 語言模型部分，目前是使用OpenAI API，費用消耗的有點快，ollama的部分則是速度太慢，之後在試試看串接google antigravity
---

## 事前準備：建立 Telegram Bot

### Telegram Bot 設定

1. 在 @BotFather 輸入`/newbot`，建立一個新 Bot，接著幫bot取名，便能取得 **Bot Token**  
2. 複製此Token，待會moltbot初始設定時會用到

---

## 一、Moltbot 安裝與啟動

```bash
# 1. 打開終端機，安裝 Moltbot
curl -fsSL https://openclaw.ai/install.sh | bash

# 2. 第一次設定
clawdbot onboard --install-daemon

# 設定細節如下
I understand this is powerful and inherently risky. Continue? 選擇Yes
Onboarding mode 選擇QuickStart
Model/auth provider 這裡以OpenAI為例（手邊沒有相關服務的話，可嘗試google antigravity，或是直接使用ollama，試了一下超卡)
OpenAI auth method 這裡以OpenAI API key為例
OPENAI_API_KEY 貼上你的API Key
Default model 這裡選擇openai/codex-mini-latest
Select channel 建議選擇telegram，設定非常方便（如要設定line也是可以，步驟麻煩一些，有機會再寫下一篇）
Telegram Bot Token 貼上你在telegram取得的token，取得方式在事前準備的步驟裡
Configure skills now? 可先略過，之後再來安裝你想要使用的skill
Enable hooks? 選擇Skip for now
安裝Gateway Service
How do you want to hatch your bot? 選擇Open the Web UI

（沒意外的話，moltbot已經順利啟動）
```

> 執行後，Moltbot 會在本機開啟預設的 HTTP 伺服器（http://127.0.0.1:18789），可在瀏覽器中使用 Dashboard 管理設定。

---

## 二、串接 Telegram Bot

### 打開剛剛建立好的Telegram Bot對話視窗
```配對訊息
Clawdbot: access not configured.

Your Telegram user id: 857xxxxxxx

Pairing code: SCJxxxxxx

Ask the bot owner to approve with:
clawdbot pairing approve telegram <code>
```

1. 複製 Pairing code
2. 回到本機的終端機，執行下列指令
```bash
clawdbot pairing approve telegram SCJxxxxxx
```

> 配對後，可傳送訊息測試是否成功，如果串接Line，則需要另外設定Webhook。

---

## 三、透過 Telegram Bot指派任務

### 請Bot設定提醒
1. 傳訊息給Bot`五分鐘後用telegram提醒我該去睡覺了`
```Bot回覆
好的，已設定「五分鐘後用telegram提醒我該去睡了」的單次提醒（Job ID: 35574992-f097-4cc0-8b74-8006f2b6edb9）。
五分鐘後系統會在主 session 發出 Reminder: 該去睡了，並自動刪除該排程。
```
2. 到主控台的Cron Jobs觀看是否有成功建立job
3. 等待五分鐘後的提醒
```Bot主動提醒
好的，該睡了！晚安，祝你好夢
```

---

## 結語

本文示範了：
- Moltbot 的安裝與設定  
- Telegram 串接  
- 透過 Telegram Bot指派提醒任務

由於moltbot可以跟本機系統串接，可透過CLI執行更多指令，也能夠控制本機端，帶來便利性的同時，也增加不少安全性的疑慮。
這個簡單的範例驗證的兩個功能，`主動推播`以及`定時執行任務`，讓AI助理看起來更加主動了。希望我可以想到更多有趣又實用的應用。
