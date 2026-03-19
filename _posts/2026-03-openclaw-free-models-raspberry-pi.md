---
author: 歐巴計概
date: 2026-03-18 00:07:59 +0000
layout: post
permalink: /2026/03/openclaw-free-models-raspberry-pi.html
title: 樹莓派 + OpenClaw 免費 AI 模型設定教學 - Ollama 與 NVIDIA Kimi K2.5

categories: [教學, openclaw]
tags: [OpenClaw, 樹莓派, AI, Ollama, NVIDIA, Raspberry Pi, LLM, 免費AI]
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/xJsQBrSki1g" frameborder="0" allowfullscreen></iframe>

# 樹莓派 + OpenClaw 免費 AI 模型設定教學

還記得過年前介紹的 **OpenClaw** 嗎？當時我們搭配 Google 的 AntiGravity 模型使用，沒想到過完年後 Google AntiGravity 已經不能用了，甚至還有很多人被封號！

這篇文章將詳細教你如何在樹莓派上設定 **Ollama** 和 **NVIDIA** 兩個免費 AI 模型，讓你不用花錢也能繼續使用 AI 助理功能。

> 編按：輕量使用還可以，重度使用還是得花錢

## 1. 為什麼需要免費模型？

### 1.1 Google AntiGravity 的限制

過年前我們介紹的 Google AntiGravity 模型，現在已經完全無法使用。這個事件提醒我們：

- 要注意使用條款
- 要找尋合適的服務

### 1.2 兩個免費模型推薦

經過測試，目前有兩個可用的免費模型：

| 模型 | 特色 | 限制 |
|------|------|------|
| **Ollama** | 有提供雲端模型 | 每週有流量限制（約 5 天後重置） |
| **NVIDIA Kimi K2.5** | 每分鐘 40 個請求 | 有時會感到延遲 |

> 「所以我最近試了兩個免費的模型是可以用的，所以我們現在就操作給大家看。」

---

## 2. Ollama 免費雲端模型設定

### 2.1 Ollama 介紹

![Ollama 雲端模型設定](/assets/images/blog/adsense-ollama.gif)

Ollama 是一家提供本地端和雲端 AI 模型的服務商。對於樹莓派等硬體資源有限的設備，Ollama 提供了**雲端模型**的選項。

### 2.2 流量限制說明

- **流量限制**：每週有使用量上限
- **重置時間**：每週一自動重置流量
- **使用體驗**：如果密集使用，可能半天到一天流量就沒了

> 「測試之後發現如果你很密集使用的話，可能一個上午或一天流量就沒了，那要等它下次重置了，但是至少它免費，還是可以加減可以用。」

### 2.3 Ollama 帳號申請

1. 前往 Ollama 官網註冊帳號
2. 登入後取得 API Key
3. 在 OpenClaw 中設定 Ollama 模型

### 2.4 申請多個帳號的技巧

如果你的用量比較大，可以考慮申請多個 Ollama 帳號：

```bash
# 登出目前帳號
ollama sign out

# 登入新帳號
ollama sign in
```

> 「因為我有註冊好幾個帳號，所以我不確定這個做法是對還是允不允許的。」

---

## 3. NVIDIA Kimi K2.5 免費模型設定

### 3.1 NVIDIA Build 平台介紹

![NVIDIA 帳號註冊](/assets/images/blog/adsense-nvidia-signup.gif)

NVIDIA 提供了 **build.nvidia.com** 平台，讓使用者可以申請 API Key 來使用 Kimi K2.5 模型。

### 3.2 申請 NVIDIA API Key 步驟

1. **前往 NVIDIA Build 網站**
   - 網址：build.nvidia.com

2. **註冊新帳號**
   - 輸入 Email 和密碼
   - 需要完成電話驗證

3. **取得 API Key**
   - 登入後進入 API Key 頁面
   - 點擊「Create API Key」
   - 複製產生的 Key（有效期 12 個月）

### 3.3 流量限制

- **每分鐘請求數**：40 RPM（Requests Per Minute）
- **使用體驗**：有時會感到延遲，但勉強堪用

> 「它的流量目前網頁上寫起來是每分鐘有 40 個請求，我用起來有時候會覺得有點頓頓的，但是各位都可以試試看，純對話勉強可以。」

---

## 4. OpenClaw 安裝與問題排除

### 4.1 OpenClaw 安裝過程

![OpenClaw 安裝後遇到錯誤](/assets/images/blog/adsense-openclaw-error.gif)

在樹莓派上安裝 OpenClaw 的過程中，可能會遇到一些問題。以下是常見的安裝錯誤和解決方案。

### 4.2 3/2版本問題：Service Not Found

![問題排查與解決](/assets/images/blog/adsense-troubleshoot.gif)

安裝完成後，執行 `openclaw gateway start` 可能會遇到 **「Not Found」** 錯誤訊息。

**原因分析**：
- OpenClaw 在安裝時沒有正確建立 Systemd Service
- 導致系統無法找到 `openclaw` 指令

**解決方案**：

1. 手动建立 Service 檔案：
```bash
sudo nano /etc/systemd/system/openclaw.service
```

2. 輸入以下內容：
```ini
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi
ExecStart=/usr/local/bin/openclaw gateway start
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

3. 啟用並啟動 Service：
```bash
sudo systemctl daemon-reload
sudo systemctl enable openclaw
sudo systemctl start openclaw
```

> 「研究一下，安裝的時候他有提到路徑的部分，不知道為什麼他沒有幫我們把設定加進去，所以我們這邊就把路徑貼上來。」

---

## 5. 模型切換實戰教學

### 5.1 Ollama 與 NVIDIA 雙模型設定

設定完成後，你可以同時擁有兩個免費模型，透過 OpenClaw 自由切換。

![AI 聊天測試](/assets/images/blog/adsense-ai-chat.gif)

### 5.2 設定步驟

1. **修改 OpenClaw 設定檔**
   - 進入 OpenClaw Dashboard
   - 選擇「Config」→「Raw」
   - 在 Provider 區塊新增 NVIDIA 設定

2. **NVIDIA JSON 設定範例**
```json
{
  "provider": "nvidia",
  "api_key": "你的NVIDIA_API_KEY"
}
```

3. **儲存設定**
   - 確認格式正確（注意逗號分隔）
   - 沒有錯誤訊息表示設定成功

### 5.3 模型切換方法

![模型切換功能](/assets/images/blog/adsense-model-switch.gif)

使用 OpenClaw 的 `/models` 指令查看所有可用模型，然後用 `/models <模型名稱>` 切換。

**常用指令**：
```bash
# 查看所有模型
/models

# 切換到 Ollama Kimi
/models ollama/kimi

# 切換到 NVIDIA Kimi K2.5
/models nvidia/kimi-k2.5-cloud
```

> 「所以現在你就可以兩個模型自由切換了，那接著下一步就是請各位再去 NVIDIA 的網站，把你的 API Key 貼過來就可以了。」

---

## 6. 流量管理與備援策略

### 6.1 建議的使用策略

**日常使用**：
1. 平常使用 Ollama 的免費流量
2. 當 Ollama 流量用完時，切換到 NVIDIA Kimi K2.5
3. 兩個模型輪流使用，延長使用時間

**緊急備援方案**：
- 如果你有多個 Ollama 帳號，可以註冊多個帳號輪流使用
- 透過 VNC 遠端連線到樹莓派切換帳號

### 6.2 遠端管理方案

如果你的樹莓派不是一直放在眼前，可以考慮：

1. **使用 Zrok 建立 Tunnel**
   - 免費的隧道服務
   - 可以從遠端存取樹莓派

2. **透過 Telegram 控制**
   - OpenClaw 支援 Telegram 整合
   - 可以遠端切換模型

### 6.3 流量監控

在 Ollama 網站的「Settings」→「Usage」中可以查看：
- Weekly Usage（每週使用量）
- 重置時間

---

## 7. 常見問題 FAQ

### Q1：Ollama 流量用完怎麼辦？

**解決方案**：
- 等待週一自動重置
- 申請多個帳號輪流使用（不確定是否可以這樣）
- 切換到 NVIDIA 模型作為備援（可設定為fallback）

### Q2：OpenClaw 無法啟動怎麼辦？

**解決方案**：
1. 檢查路徑設定是否正確
2. 手動建立 Systemd Service
3. 參考文章中的設定範例

### Q3：可以同時使用多個模型嗎？

**解決方案**：
- 可以，在設定檔中新增多個 Provider
- 透過 OpenClaw 的 `/models` 指令自由切換


---

## 8. 完整流程總整理

### 8.1 前置準備

1. 樹莓派（已安裝 Raspberry Pi OS）
2. OpenClaw 已安裝
3. Ollama 帳號
4. NVIDIA Build 帳號

### 8.2 設定流程

| 步驟 | 內容 |
|------|------|
| 1 | 申請 Ollama API Key |
| 2 | 申請 NVIDIA API Key |
| 3 | 在 OpenClaw 設定 Ollama |
| 4 | 在 OpenClaw 設定 NVIDIA |
| 5 | 測試模型切換功能 |

### 8.3 實用指令速查

```bash
# 啟動 OpenClaw Gateway
sudo systemctl start openclaw

# 查看服務狀態
sudo systemctl status openclaw

# 開啟 OpenClaw Dashboard
openclaw dashboard

# Ollama 登入/登出
ollama sign in
ollama sign out

# OpenClaw 模型指令
/models
/models <模型名稱>
```

---

## 9. 結論

透過本篇文章的教學，你現在應該能夠：

- ✅ 在樹莓派上成功安裝 OpenClaw
- ✅ 申請並設定 Ollama 免費雲端模型
- ✅ 申請並設定 NVIDIA Kimi K2.5 模型
- ✅ 解決 OpenClaw Service Not Found 問題
- ✅ 實現兩個模型之間的自由切換

### 推薦的使用方式

**最佳實踐**：
1. 日常使用 Ollama（流量充足時）
2. Ollama 流量用完後，切換到 NVIDIA
3. 申請多個 Ollama 帳號作為備援
4. 透過遠端方式管理流量

**不適合的使用場景**：
- 用量非常大的情況（免費流量很快就用完）
- 需要即時回應的場景
- 對延遲敏感的應用

---

如果你喜歡這篇文章，歡迎分享給其他在玩樹莓派和 AI 的朋友！如果有任何問題或建議，也歡迎在下方留言討論。

**相關影片**：
- [樹莓派安裝 OpenClaw 第一集 - openclaw搭配google antigravty，以及相關設定](https://youtu.be/PCMNf-XINgw)

**延伸閱讀**：
- [OpenClaw 官方網站](https://openclaw.ai)
- [Ollama 官網](https://ollama.com)
- [NVIDIA Build 平台](https://build.nvidia.com)
