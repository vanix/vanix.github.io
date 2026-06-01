---
author: 歐巴計概
layout: post 
title: 在 Mac 上架設 n8n 教學｜Docker 快速自架自動化流程（含 Google API）
date: 2026-01-14 
permalink: /2026/01/mac-n8n-docker-setup.html

categories: [教學, n8n] 
tags: [n8n, Docker, Mac, 自動化]
---

n8n 是一套強大的自動化工作流程工具，本文將教你如何在 Mac 上使用 Docker 自架 n8n，並完成 Google API（Gmail、Calendar、Sheet）整合，新手也能順利完成。

## 安裝步驟

### 安裝 Docker

前往 Docker 官方網站下載並安裝 **Docker Desktop**：

- [下載 Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/)

安裝完成後，請確認 Docker 已成功啟動並正在執行。

---

### 部署 n8n

#### 編輯 `docker-compose.yml`

1. 在你的電腦上建立一個資料夾（例如：`n8n-project`）
2. 在該資料夾內建立一個名為 `docker-compose.yml` 的檔案
3. 將以下內容貼入 `docker-compose.yml`

```yaml
version: "3.8"
services:
  n8n:
    image: n8nio/n8n:latest
    ports:
      - "5678:5678"
    volumes:
      - ./n8n_data:/home/node/.n8n
    restart: always
```

> 📌 `./n8n_data` 用來保存 n8n 設定與資料，避免容器刪除後資料遺失。透過volumes，可將本機端資料夾掛載到容器裡

4. 打開終端機（Terminal），進入該資料夾

```bash
cd n8n-project
```

5. 啟動 n8n

```bash
docker compose up -d
```

6. 開啟瀏覽器，進入

```
http://localhost:5678
```

看到 n8n 介面後，再註冊帳號且登入即可

---

## 準備 API 金鑰

### Google API 設定

#### 建立 Google Cloud 專案

- 前往：[https://console.cloud.google.com/](https://console.cloud.google.com/)
- 開啟「專案挑選器」→ 新增專案 → 輸入專案名稱 → 建立

---

#### 設定 OAuth 同意畫面與用戶端

前往：[https://console.cloud.google.com/auth/](https://console.cloud.google.com/auth/)

**設定 Google 驗證平台**

1. 輸入應用程式資訊
2. 設定目標對象
3. 填寫聯絡資訊
4. 完成並建立

**建立 OAuth 用戶端**

- 點選「用戶端」→ 建立用戶端
- 應用程式類型：**網頁應用程式**
- 輸入名稱 → 建立

建立完成後，會取得：

- **用戶端ID**
- **用戶端密碼**

> 請自行複製，待會建立憑證會用到

已授權的重新導向 URI，設定如下

- http://localhost:5678/rest/oauth2-credential/callback

---

**加入測試使用者**

- 點選「目標對象」→ 測試使用者 → Add users
- 輸入你的 Google 信箱

---

#### 啟用需要的 Google API

- 左上選單 → API 和服務 → 已啟用的 API 和服務
- 點選「啟用 API 和服務」
- 搜尋並啟用你需要的 API（可重複此步驟）

本例中啟用了：

- Gmail API
- Google Calendar API
- Google Sheets API
- Google Drive API
- YouTube Data API

---

## 在 n8n 中建立 Google 憑證

1. 進入 n8n 首頁
2. 右上角選單 → **Create credentials**
3. 搜尋 **Google OAuth2 API**

填入以下資訊：

- **Client ID**：你的 用戶端ID
- **Client Secret**：你的 用戶端密碼
- **Scope**（依需求調整，此範例會把下面五行貼到此欄位）：

```text
https://www.googleapis.com/auth/gmail.modify
https://www.googleapis.com/auth/calendar
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/youtube.force-ssl
https://www.googleapis.com/auth/drive.file
```

4. 複製 **OAuth Redirect URL**，待會用會到
5. 點選 **Sign in with Google**
6. 使用剛剛加入的測試使用者信箱登入
7. 勾選允許存取的範圍

---

### 回到 Google Cloud Console 設定 Redirect URI

前往：[https://console.cloud.google.com/auth/](https://console.cloud.google.com/auth/)

- 點選「用戶端」→ 選擇剛剛建立的用戶端
- 已授權的重新導向 URI → 新增

```text
http://localhost:5678/rest/oauth2-credential/callback
```

---

## 測試 Workflow

1. 回到 n8n 首頁
2. 點選 **Create workflow**
3. **Credentials to connect with**欄位，選擇剛剛設定好的credential
4. 無法選取剛剛設定好的credential，則選取**Create new credential**再重新設定一次，步驟與上述**在 n8n 中建立 Google 憑證**相同
5. 接者進行測試，這邊使用Chat Trigger測試 Gmail API 是否能運作，例如：輸入Email，Gmail寄信給對方（收件者、主旨跟內文都是一樣的文字）

```
Chat Trigger
   └─ Gmail: Send a message
```

若可成功執行，即代表設定完成 ✅，以下為此範例的JSON，可自行匯入測試

```json
{
  "name": "Gmail API Testing",
  "nodes": [
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "typeVersion": 1.4,
      "position": [
        -368,
        -32
      ],
      "id": "b3e7fe33-4c1f-488b-bfa4-c695ecb54c77",
      "name": "When chat message received",
      "webhookId": "5c867db3-9346-4310-a5f4-1a2da95502b7"
    },
    {
      "parameters": {
        "sendTo": "={{ $json.chatInput }}",
        "subject": "={{ $json.chatInput }}",
        "message": "={{ $json.chatInput }}",
        "options": {}
      },
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 2.2,
      "position": [
        -176,
        -32
      ],
      "id": "b71a215d-a943-4dbf-a4b9-291e7bc44d26",
      "name": "Send a message",
      "webhookId": "37d983b0-4f2c-4699-9731-977a6878f4f4",
      "credentials": {
        "gmailOAuth2": {
          "id": "Qq4CeeObRGnR12t1",
          "name": "Gmail account"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "When chat message received": {
      "main": [
        [
          {
            "node": "Send a message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send a message": {
      "main": [
        []
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "30bd1831-7a3c-4fec-a33c-a919cbac1457",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "2e9d3b299f8c8237d63a2d1fd0d4c2d7f9404ea120656e0a688429513dd75435"
  },
  "id": "egd8zEYjfNLCNazj",
  "tags": []
}
```

---

## 下一步：Webhook 與對外存取

若你是 **自行架設 n8n**，並希望使用 **Webhook** 對外服務，則需要搭配 **zrok** 工具，這樣就能夠串接Line的服務。

👉 **敬請期待下篇文章說明 🚀**

