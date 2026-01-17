---
author: 歐巴計概
layout: post 
title: "n8n + zrok 教學｜讓自架 n8n Webhook 對外服務（免公開且固定IP）" 
date: 2026-01-18
permalink: /2026/01/n8n-zrok-webhook.html

categories: [教學, n8n] 
tags: [n8n, zrok, webhook, tunnel]
---

👉 如果你還沒完成 n8n 安裝，可以先看上一篇：[在 Mac 上用 Docker 架設 n8n 教學](https://vanix.github.io/2026/01/mac-n8n-docker-setup.html)

## 為什麼自架 n8n 需要 Webhook 對外？

在上一篇文章中，我們已經成功在 **Mac 上用 Docker 自架 n8n**，並完成 Google API 的整合。但很快你會發現一個問題：

> ❌ 如果你的n8n在私有網路裡，導致無法使用外部服務去觸發n8n的workflow，例如：透過Line訊息觸發服務

所以為了讓外部服務可以觸發本機的服務，這時就需要一個 **安全又簡單的對外通道**。

👉 本篇將教你使用 **zrok**，讓你的 n8n Webhook：

- ✅ 對外公開（HTTPS）
- ✅ 不需要固定 IP
- ✅ 不用設定 Router / NAT
- ✅ 非常適合個人、自架、測試環境

---

## 架構說明

```
第三方服務
   │  HTTPS Webhook
   ▼
zrok 公開網址
   │
   ▼
本機 n8n（Docker） → Workflow
```

zrok 的角色就是：

> **幫你把本機服務「安全地」暴露到網際網路上**。

---

## 步驟一：安裝 zrok

### macOS（Homebrew）

```bash
brew install zrok
```

安裝完成後確認版本：

```bash
zrok version
```

---

## 步驟二：註冊並啟用 zrok 環境

1. 前往 [zrok 官方網站](https://myzrok.io/)註冊帳號
2. 註冊成功後再登入[zrok portal](https://api-v1.zrok.io/)，取得 **Account Token**
3. 在本機執行：

```bash
zrok enable <你的 Account token>
```

成功後會看到：

```
⣾  the zrok environment was successfully enabled...
```

---

## 步驟三：對外分享 n8n Webhook（TCP Tunnel）

n8n 預設 Web UI 與 Webhook 都在 **5678 port**，因此我們直接分享該 port。

```bash
zrok share public http://localhost:5678 --backend-mode proxy
```

成功後，終端機會顯示類似：

```
https://xxxxx.zrok.io
```

這就是你可以 **對外使用的公開網址**

---

## 步驟四：在 n8n 建立 Webhook Workflow

1. 開啟 n8n
2. 新增一個 **Webhook Trigger** 節點，先使用Test URL進行測試
3. 設定：
   - HTTP Method：`POST`
   - Path：`d42aedb3-69c9-4c85-abb8-4f3c4017621d`（每個webhook的path不同）

Webhook URL 會長得像：

```text
http://localhost:5678/webhook-test/d42aedb3-69c9-4c85-abb8-4f3c4017621d
```

---

## 步驟五：改用 zrok 公開網址呼叫

假設 zrok 提供的網址是：

```text
https://xxxxx.zrok.io
```

那實際對外的 Webhook URL 就是：

```text
https://xxxxx.zrok.io/webhook-test/d42aedb3-69c9-4c85-abb8-4f3c4017621d
```

你現在可以從：

- curl
- GitHub Webhook
- LINE / Discord / Stripe / 自動化服務

直接呼叫你的 **本機 n8n Workflow** 🚀

---

## 測試範例（curl）

```bash
curl -X POST https://xxxxx.zrok.io/test-webhook/你的path \
  -H "Content-Type: application/json" \
```

若 n8n 有成功接收到資料，會顯示下面訊息，代表有成功連到n8n裡的webhook
```bash
{"message":"Workflow was started"}
```

---

## 常見問題與注意事項

### 🔒 安全性建議

- 可在 Workflow 中加上 Header Token 驗證
- 正式環境請避免公開敏感資料

---

### ⚠️ zrok 程式中斷

zrok 是「即時通道」，若終端機關閉：

- ❌ Webhook 會立刻失效

建議：

- 使用 `tmux` / `screen`
- 或寫成系統服務（進階）

---

## 適合誰使用這個架構？

- 想自架 n8n，但沒有固定 IP
- 家用網路、公司網路、學校環境
- Webhook 開發 / 測試 / Demo

不適合：

- 高流量正式商業服務（請改用 VPS / Cloud）

---

## 小結

透過 **n8n + zrok**，你可以：

- 在本機自架 n8n
- 卻擁有像雲端服務一樣的 Webhook 能力
- 非常適合學習、開發與自動化實驗

---

## 下一篇預告

👉 **n8n + Webhook 實戰：Line 翻譯機器人、iOS捷徑串接webhook**

敬請期待 😎

