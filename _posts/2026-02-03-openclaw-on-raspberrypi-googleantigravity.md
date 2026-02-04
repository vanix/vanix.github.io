---
author: 宅爸
layout: post
title: "樹莓派 5 打造最強 AI 助理：OpenClaw 安裝、Gemini 模型設定與 Telegram 連動全攻略"
date: 2026-02-03
permalink: /2026/02/openclaw-on-raspberrypi-googleantigravity.html
categories: [教學, openclaw]
tags: [Clawdbot, AI Agent, Moltbot, Openclaw,  Googleantigravity, 自動化, 樹莓派5, RaspberryPi, 教學]

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/PCMNf-XINgw?si=9Dj9HxvhXTsWYLOC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

最近 AI 領域出現了一個超級火紅的助理軟體 —— **OpenClaw**。聽說這款軟體紅到連 Mac mini 都賣到缺貨！雖然網路上有很多安裝在 Mac 上的教學，但今天宅爸要帶大家走一條不一樣的路：使用 **樹莓派 5 (Raspberry Pi 5)** 來打造一個專屬、安全且成本更低的 AI 基地！

## 為什麼選擇樹莓派 5？

1.  **安全性**：使用全新的樹莓派系統與乾淨的 Gmail 帳號，不必擔心隱私資料與主電腦混在一起。
2.  **性價比**：相較於 Mac mini，樹莓派 5 是一個更親民的入門選擇。
3.  **效能穩定**：宅爸實測發現，樹莓派 5 運行 OpenClaw 的反應速度非常理想。

---

## 🛠️ 第一步：一鍵安裝 OpenClaw

安裝過程簡單到令人驚訝。只需打開樹莓派的瀏覽器，進入 OpenClaw 官網，複製那一長串安裝指令，並在終端機貼上執行即可。

![安裝指令](assets/images/blog/install_cmd.gif)
*只需一行指令，系統就會自動處理複雜的環境設定。*

---

## 🧠 第二步：選擇 AI 模型 (省錢小撇步)

宅爸一開始測試過 OpenAI，發現使用 API Key 跑應用的成本非常高（隨便測測就噴了 20 多塊美金！）。後來改用 **Google 的 AntiGravity (Gemini-3-Flash)**，不僅設定方便，流量也相對慷慨許多。

![模型認證](assets/images/blog/model_auth.gif)
*透過 Google 帳號快速認證，選擇 CP 值最高的 Gemini-3-Flash。*

---

## 📱 第三步：Telegram 遠端操控設定

為了讓 AI 助理隨時隨地為我們服務，**Telegram** 是最佳的通訊橋樑。

1.  找 **BotFather** 建立機器人。
2.  取得 **Token** 並貼回終端機。
3.  最關鍵的一步：在終端機執行 **`/pair`** 指令完成授權。

![Telegram 設定](assets/images/blog/tg_setup.gif)
*完成配對後，你就能直接在手機上跟你的樹莓派 AI 聊天了！*

---

## ⌨️ 第四步：中文化環境與角色設定

為了讓助理能用繁體中文流暢溝通，我們需要幫樹莓派安裝 `fcitx5-chewing` (酷音輸入法)。

![輸入法設定](assets/images/blog/input_method.gif)
*安裝完成並重啟後，就能順利在 Web UI 打中文字囉。*

接下來就是最有趣的環節：**賦予 AI 性格**。你可以叫他「經紀人」，讓他稱呼你為「明星」；或者讓他化身為「女僕」。他會完全依照你的設定來與你對答。

---

## ✅ 第五步：實測成功！

當一切設定就緒，在 Telegram 傳送一句「你好」，看到 AI 即時回覆的那一刻，你的專屬個人秘書就正式上線了！

![實測回覆](assets/images/blog/success_chat.gif)
*雖然回覆需要幾秒鐘的運算時間，但品質與精確度都非常高。*

## 結語

樹莓派 5 搭配 OpenClaw 的體驗非常棒。它提供了一個獨立、乾淨且強大的 AI 實驗空間。如果你也想體驗最近最紅的 AI 科技，不妨從樹莓派開始嘗試！

接下來宅爸還會分享如何連動 Google App（Gmail、日曆、雲端硬碟）等進階應用，記得持續關注喔！
