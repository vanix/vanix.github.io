---
author: 歐巴計概
layout: post 
title: "n8n + Webhook 教學｜製作 LINE AI 翻譯機器人（即時中英日韓都可）" 
date: 2026-01-22
permalink: /2026/01/n8n-webhooh-line-ai-translate.html


categories: [教學, n8n] 
tags: [n8n, webhook, LINE Bot, AI 翻譯]

---

如果你還沒設定好 zrok，可以先看上一篇：[n8n + zrok 教學｜讓自架 n8n Webhook 對外服務](https://vanix.github.io/2026/01/n8n-zrok-webhook.html)


## 為什麼要用 n8n 做 LINE 翻譯機器人？

LINE 是台灣最常用的通訊軟體，如果能做到：

- 傳一句話給 LINE Bot
- 自動翻譯成指定語言
- 即時回傳結果

那不論是學語言、工作、旅遊或親子學習都非常實用。

👉 本篇教你用 **n8n + Webhook + AI API**， 快速打造一個 **LINE 翻譯機器人**。

---

## 系統架構

```
LINE 使用者
   │
   ▼
LINE Webhook
   │
   ▼
 n8n Webhook Trigger
   │
   ▼
 AI 翻譯（Gemini / OpenAI / LLM）
   │
   ▼
 LINE Reply API
```

---

## 步驟一：建立 LINE Bot

1. 前往 [LINE Developers](https://developers.line.biz/console/)，並登入
2. 建立 `Create Provider`
3. 建立 `Create a new Channel`，選擇`Messaging API`，接著選擇`Create a Line Official Account`
4. 前往 [LINE Official Account Manager](https://manager.line.biz/)
   - 選擇你要使用的官方帳號
   - 左側選單點擊「聊天」 > 「設定」 > Messaging API > 啟用Messaging API
5. 回到 [Line Developers](https://developers.line.biz/console/)，點選剛建立好的Channel在Basic settings取得
   - 在Basic settings分頁中取得`Channel Secret`
   - 在Messaging API分頁中取得`Channel Access Token`

---

## 步驟二：建立n8n Line AI 翻譯機器人 Workflow(文章最後會附上此workflow的json內容)

需先建立好zrok，請參閱[n8n + zrok 教學](https://vanix.github.io/2026/01/n8n-zrok-webhook.html)

```workflow流程
Webhook Trigger 
   │            │
   │            ▼
   │   Gemini Message Model (需先取得API key)
   │     │
   ▼     ▼
 Merge Node
   │     
   ▼  
HTTPS Request (使用LINE Reply API)
```

1. 準備Gemini API Key
   - 先到[Google AI Studio](https://aistudio.google.com/)，點選左下方`Get API key`，再點選`Create API key`   
   - 建立成功後，複製API key
2. 新增`Webhook`節點
   - 測試階段先使用Test URL
   - HTTP Method設定為`POST`
3. 新增Google Gemini的`Message a model`節點
   - 建立Credential，在API Key欄位貼上剛剛複製的API Key，確認是否連線成功
   - Operation: `Message a Model`
   - Model: `Gemini-2.5-flash`
   - Prompt: 請幫我這句話：{{ $json.body.events[0].message.text }}翻譯成英文，除了翻譯內容之外，其他文字都不需要回應我
   - Role: `User`
   - 可依需求更改prompt裡的語言
4. 新增`Merge`節點
   - Mode: `Combine`
   - Combine By: `Position`
   - Number of Inputs: `2`
5. 新增`HTTP Request`節點
   - Method: POST
   - URL: https://api.line.me/v2/bot/message/reply
   - Send Header
      - Specify Headers: `Using Fields Below`
	  - Name: `Authorization`, Value: `Bearer 你的Channel access token`
	  - Name: `Content-Type`, Value: `application/json`
   - Send Body
       - Body Content Type: `JSON`
	   - Specify Body: `Using JSON`
	   - JSON設定如下
```
{
  "replyToken": "{{ $json.body.events[0].replyToken }}",
  "messages": [
    {
      "type": "text",
      "text": "{{ $json.content.parts[0].text }}"
    }
  ]
}
```  
---


## 步驟三：設定 LINE Webhook

1. 先複製Webhook節點的`Test URL`(測試用)或`Production URL`(Active用)
2. 設定 Line Developers > Messaging API分頁 > Webhook URL
3. 貼上剛剛複製的網址，但網址要處理一下

```測試用
https://你的zrok網址/webhook-test/path
```

```Active用
https://你的zrok網址/webhook/path
```

> 提醒：記得先啟動你電腦的zrok

4. path內容請到Webhook節點裡查詢

---

## 步驟四：測試n8n workflow

1. 按下`Execute workflow`
2. 使用Line傳訊息給官方帳號
3. 觀察workflow是否有順利完成

---

## 步驟五：啟用n8n workflow

1. 按下workflow右上的Active按鈕
2. 複製Webhook的Produciton URL
3. 更新Line Developers > Messaging API分頁 > Webhook URL
4. 傳訊息給官方帳號確認是否成功

---

## 測試成果

- 使用者傳：`今天會下雨嗎？`
- Bot 回：`Will it rain today?`

---

## 延伸玩法

- 搭配iOS捷徑，變成AI翻譯語音機器人
- 自動判斷要翻譯成什麼語言
- 中英對照輸出
- 翻譯後存 Google Sheet

---

## 小結

透過 n8n，你可以不用寫後端程式， 就完成一個 **可實際使用的 LINE AI 機器人**。

---

## 系列回顧

- 在 Mac 上用 Docker 架設 n8n
- n8n + zrok 對外 Webhook
- n8n + LINE AI 翻譯機器人 

下一篇，n8n + Webhook 自動發文到GitHub Pages 🚀

---

## 此篇workflow的json檔案

```JSON
{
  "name": "Line 翻譯機器人 - Gemini",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "70cfd869-5c07-4876-acd9-4a95c75fc7a0",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2.1,
      "position": [
        -144,
        -32
      ],
      "id": "c673215e-c0a0-4945-a688-bc40ca882b03",
      "name": "Webhook",
      "webhookId": "70cfd869-5c07-4876-acd9-4a95c75fc7a0"
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.line.me/v2/bot/message/reply",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer 你的channel access token"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"replyToken\": \"{{ $json.body.events[0].replyToken }}\",\n  \"messages\": [\n    {\n      \"type\": \"text\",\n      \"text\": \"{{ $json.content.parts[0].text }}\"\n    }\n  ]\n}",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.3,
      "position": [
        640,
        -48
      ],
      "id": "47fce030-b022-423f-977c-0067a6cf40b0",
      "name": "HTTP Request"
    },
    {
      "parameters": {
        "mode": "combine",
        "combineBy": "combineByPosition",
        "options": {}
      },
      "type": "n8n-nodes-base.merge",
      "typeVersion": 3.2,
      "position": [
        416,
        -48
      ],
      "id": "af0e7e19-664b-41b2-968c-20da0cbc0043",
      "name": "Merge"
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "models/gemini-2.5-flash",
          "mode": "list",
          "cachedResultName": "models/gemini-2.5-flash"
        },
        "messages": {
          "values": [
            {
              "content": "=請幫我這句話：{{ $json.body.events[0].message.text }}\n翻譯成英文，除了翻譯內容之外，其他文字都不需要回應我"
            }
          ]
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.googleGemini",
      "typeVersion": 1,
      "position": [
        80,
        -128
      ],
      "id": "8bad0a01-6a92-4337-9004-32f7e3e126bc",
      "name": "Message a model1",
      "credentials": {
        "googlePalmApi": {
          "id": "MTTWBjXhmcEYvKKJ",
          "name": "Google Gemini(PaLM) Api account"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          },
          {
            "node": "Message a model1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        []
      ]
    },
    "Merge": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Message a model1": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "937eeed6-83ec-4cdb-bf0f-5ac292e2b4dd",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "2eace1461374a3b35f69ebe0fe0ef31453318131a4bd5f7a7a129d2b3ac7c20c"
  },
  "id": "DJcITNrixNUqQ93P",
  "tags": []
}
```

