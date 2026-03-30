---
author: 宅爸
layout: post
title: "打字就能做影片？用 AI Agent 操控 Remotion 自動產出影片"
date: 2026-04-01
permalink: /2026/04/ai-agent-remotion-tutorial.html
categories: [教學, remotion]
tags: [AI Agent, Remotion, 自動化, opencode,google antigravity]
---

# 打字就能做影片？用 AI Agent 操控 Remotion 自動產出 YouTube 影片

身為內容創作者，你是否曾覺得學習 Premiere Pro 等專業剪輯軟體耗時又費力？如果有一種方法，能讓你只要「打字」對著 AI 下達指令，它就能幫你把影片排版、加上動畫特效，最後直接渲染出高畫質的 MP4 檔案呢？

答案是：**AI Agent 加上 Remotion 框架！**

**[Remotion](https://www.remotion.dev/)** 是一個能用 React（HTML/CSS/JS）撰寫影片的強大框架，而當它結合了能自動寫 Code、下指令的 **AI Agent（例如 Google Antigravity 或 Opencode）**，你將擁有一個完全自動化的 AI 剪輯工具！

今天這篇文章，我將以我的 YouTube 頻道（**充滿意外的宅爸人生**）為例，帶你看看我是如何靠對話，一步步讓 AI Agent 幫我做出高品質的專屬結尾動畫 (Outro)。

---

## 為什麼讓 AI 寫 Remotion 而不是直接用主流 AI 生成影片？

你可能會問，現在不是有很多 AI 產片工具嗎（如 Sora, 剪映）？
市面的 AI 產片通常難以控制精準的「品牌字體」、「排版」與「按鈕動畫」。而讓 AI Agent 去寫出 Remotion 程式碼，好處在於：

1. **100% 精準與客製化**：AI 產出的是 React 程式碼，圖標位置、字型大小可以豪釐不差，完全套用你的個人品牌樣式。
2. **極致修改效率**：只要對 AI 說「幫我把解析度改成 YouTube Shorts 格式」，它幾秒鐘就能把長寬比改好，立刻產出直式影片。

---

## 實戰示範：用 AI Agent 製作YT結尾動畫

以下是真實的操作流程，你只要有一套 AI 輔助開發工具，就可以重現這個過程。

### Step 1：給予 AI 必備的 Skill

AI 雖然聰明，要讓 AI 寫出合適的動畫，最好的方式是在專案目錄建立一個 `skills` 資料夾，並匯入 [Remotion 官方Skill](https://github.com/remotion-dev/skills)，這樣AI就能夠自行挑選合適的工具去產生動畫。

### Step 2：用自然語言下達介面與視覺需求

設定好知識庫後，你只需要對 AI Agent 拋出你的需求。譬如：

> **我下的 Prompt (第一版)：**
> 「請幫我用 Remotion 製作一個短的 YouTube 結尾影片 (Outro)，可一併給AI參考圖片，讓AI了解我想要的風格。
> 1. 動畫風格維持黑色背景，科技且具有質感。
> 2. 頻道名稱叫做『充滿意外的宅爸人生』。
> 3. 下方加上『程式教學 | 親子旅遊 | 宅爸生活』的標籤。

AI 接收到指令後，立刻會為我們建立出對應的 `HomedadOutro.tsx` 檔案。

![Homedad Outro 第一版](assets/images/blog/homedad-outro.gif)

### Step 3：修改圖片與加入訂閱動畫，並修正成shorts版面

很明顯顯示圖片跟我的頻道圖片不符，並且我想要把下方文字改成訂閱動畫。

> **我下的 Prompt (第二版)：**
> 1. 我的顯示圖片請使用 public 裡的 `homedad.png`。
> 2. 放上一個 YouTube 訂閱鈴鐺動畫。」

做完橫向影片後，想要再馬上改成 YouTube Shorts 上的直立版本。我不用打開影片編輯器重新拉座標，也只要對 AI Agent 說：

> **我：**「請幫我把解析度改成 1080x1920，重新排版圖片大小與文字換行，並幫我 render 出來。」

AI Agent 馬上去修改了 `Root.tsx` 中的 `<Composition width={1080} height={1920} />`，自行放大了頭像尺寸，接著直接背景幫我執行終端機渲染指令：

```bash
npx remotion render HomedadOutro out/homedad-outro-v2.mp4
```

約莫 10 秒鐘後，一個高質感、包含流暢平滑動畫的 **1080x1920 MP4 垂直影片**就安安靜靜地躺在我的資料夾裡了！

![Homedad Outro 第二版](assets/images/blog/homedad-outro-v2.gif)

---

## 結語：未來做影片的全新樣貌

透過這次實戰你會發現，當我們將 **Remotion (影片視覺框架) + AI Agent (大腦與雙手)** 結合起來，未來甚至能夠做到：撈取最新的 API 資料 > AI 自動改寫提醒文案 > 自動渲染出 MP4 > 自動上傳社群媒體的一條龍式影音工廠。

對於前端工程師或是想經營自媒體的技術人來說，學會運用你的 AI 助理寫 Code 做影片，絕對是將技術變現與優化創作流程的最佳途徑。

如果你也覺得這套流程很酷，趕緊去下載 [Remotion](https://www.remotion.dev/) 搭配你身邊的 AI 開發工具，試著「打字」產生你的第一支影片吧！

> 編按：模型的選擇會影響最終產出的品質，建議可使用各種不同的模型生成看看。
