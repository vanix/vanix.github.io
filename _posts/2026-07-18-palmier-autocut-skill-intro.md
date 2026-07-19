---
author: 宅爸
date: 2026-07-18 00:07:59 +0000
layout: post
permalink: /2026/07/palmier-autocut-skill-intro.html
title: 自製 Palmier AutoCut Skill — 用 AI Agent 自動剪片，一句話搞定後製！

categories: [教學, AI應用, 影片剪輯]
tags: [AI, Agent, OpenCode, Palmier Pro, 影片剪輯, 自動化, MCP, Whisper, 字幕, 後製]
---

# Palmier AutoCut Skill — 用 AI Agent 自動剪片，一句話搞定後製！

你有沒有遇過這種情況：拍了一堆素材，想到要剪輯就頭痛？從素材整理、粗剪、上字幕、配樂到輸出，一套流程走下來動輒幾小時，甚至一整天。

為了解決這個問題，宅爸我寫了一個 OpenCode Skill — **Palmier AutoCut**（[GitHub 開源](https://github.com/vanix/palmier-autocut-skill)），讓 AI Agent 透過 [Palmier Pro MCP](https://palmier.pro) 自動執行完整後製流程。

你只需要說一句「**幫我剪片**」，剩下的交給 AI。

---

## 這支 Skill 能做什麼？

Palmier AutoCut 涵蓋了影片後製的完整流程，從素材匯入到最終輸出，全部自動化：

| 階段 | 內容 |
|:----:|:------|
| 1. 初始化 | 建立專案 + 匯入整個素材資料夾 |
| 2. 素材分析 | 自動分類 A-roll（主鏡頭）與 B-roll（輔助畫面） |
| 3. 精選素材 | 流水帳全上／AI 挑重點／自訂腳本，三種模式 |
| 4. 時間軸建構 | 上片 + 粗剪 + 自動刪除靜音段落 |
| 5. B-roll 覆疊 | 可選，疊加輔助畫面 |
| 6. 背景音樂 | 逐章節配樂、音量控制、淡入淡出 |
| 7. 字幕轉錄 | 外部 Whisper 引擎（GPU 加速），含除幻覺與錯字修正 |
| 8. 輸出 | H.264 / H.265 / ProRes 或 FCPXML |

---

## 為什麼需要這個 Skill？

### 痛點 1：剪輯流程繁瑣

影片剪輯涉及大量重複性操作：匯入素材、分類、上時間軸、剪掉空白段、上字幕、配樂、調整音量、輸出。每一步都要手動操作，耗時費力。

### 痛點 2：字幕工程尤其麻煩

Palmier Pro 內建的字幕功能（`add_captions`）斷句不自然、時間軸不準。手動調整字幕更是惡夢。這個 Skill 強制使用外部 Whisper 引擎進行轉錄，再透過 Python 腳本除幻覺、修正錯字，產出品質遠勝內建工具。

### 痛點 3：BGM 與 silence removal 的衝突

這是一個實際踩過的坑：如果先放背景音樂再做 `remove_silence`，靜音刪除的 ripple 會把 BGM 切成幾十段碎片。這個 Skill 的 SOP 嚴格規定**先 silence → 後 BGM**，避免這個問題。

---

## 核心功能介紹

### 三種剪輯風格

針對不同需求，提供了三種模式：

**A：流水帳模式**
適合 vlog 或活動紀錄，所有素材按時間順序全上，只做最小清理（去頭去尾）。

**B：AI 挑重點模式**
AI 逐段檢視素材，透過畫面抽幀與 ASR 語音辨識判斷內容重要性，自動保留精華段落。

**C：自訂腳本模式**
AI 產出逐字稿腳本，讓使用者手動編輯章節標題與刪除段落，再由 AI 依腳本建構時間軸。

### 外部 Whisper 字幕引擎

這大概是整個 Skill 最講究的部分：

- 強制使用 `mlx_whisper`（Apple Silicon GPU 加速）或 `openai-whisper`（CPU 備用）
- 從 silence-removed 後的 timeline 提取音訊，確保字幕 frame 與影片完全同步
- 自動清除 Whisper 的幻覺段落（連續重複字詞）
- 內建錯字修正表（在→再、因該→應該等）
- 提供 SRT→JSON 轉換腳本，直接對接 Palmier Pro 的 `add_texts`

> 有另外試過whisperx，但太多對話被略過（可能影片背景音太吵雜）

### 背景音樂智慧管理

- 逐章節配樂：AI 分析逐字稿找出話題轉折點，自動分章節配樂
- 多軌獨立音量控制（預設 -20dB）
- 2 秒淡入淡出
- BGM tail 自動裁切，避免尾段黑畫面配音樂

---

## 安裝與使用

總共需要三個步驟：安裝 Skill、設定 MCP、安裝依賴套件。

### 第一步：安裝 Palmier AutoCut Skill

將 Skill 複製到 OpenCode 的技能目錄：

```bash
git clone https://github.com/vanix/palmier-autocut-skill.git ~/.config/opencode/skills/palmier-autocut
```

OpenCode 會自動掃描 `~/.config/opencode/skills/` 底下所有的 `SKILL.md`，無需額外設定。

### 第二步：設定 Palmier Pro MCP

Palmier Pro 提供 MCP 協定讓 AI Agent 直接操作時間軸。在 `~/.config/opencode/opencode.json` 中加入 MCP 伺服器設定：

```json
{
  "mcp": {
    "palmier": {
      "type": "remote",
      "url": "http://127.0.0.1:19789/mcp",
      "enabled": true
    }
  }
}
```

設定完成後，**重啟 OpenCode** 讓設定生效。確認 MCP 連線成功後，OpenCode 就能透過 Palmier Pro 的 MCP 工具讀取素材、剪輯時間軸、上字幕、輸出影片。

> 如果你使用的是 Palmier Pro 雲端版（remote API），則改用 `"type": "remote"` 並填入 endpoint URL。

### 第三步：安裝依賴套件

字幕轉錄需要 Whisper 引擎，依照你的硬體選擇：

```bash
# Apple Silicon（M1/M2/M3）GPU 加速，推薦
pip install mlx-whisper

# Intel Mac 或無 GPU 環境，CPU 備用
pip install openai-whisper
```

### 使用方式

一切就緒後，在 OpenCode 中直接輸入：

```
幫我剪片
```

系統會依序詢問 7 個問題，全部回答完後自動開始執行：

### 7 題互動問卷

| 代號 | 問題 | 預設值 |
|:----:|:-----|:------:|
| ANS_1 | 影片主題是什麼？ | — |
| ANS_2 | 素材在哪個資料夾？ | — |
| ANS_3 | 剪輯風格？（A/B/C） | 流水帳 |
| ANS_4 | 主要語言？ | zh-TW |
| ANS_5 | 比例與解析度？ | 16:9 1080p |
| ANS_6 | 音樂需求？ | — |
| ANS_7 | 輸出編碼？ | H.264 |

### 驗證安裝

執行以下指令確認 Skill 已正確載入：

```bash
ls ~/.config/opencode/skills/palmier-autocut/
# 應該看到：README.md  SKILL.md

pip list 2>/dev/null | grep -i whisper
# 應該看到：mlx-whisper 或 openai-whisper
```

一切正常後，重啟 OpenCode 就可以開始使用了。

### 剪片成果輸出

剪輯完成後，支援兩種輸出格式，滿足不同需求：

**H.264 MP4** — 直接可用的影片檔
- 標準 H.264 編碼，MP4 容器，廣泛相容於各平台
- 可選擇 H.265（更小體積）或 ProRes（後製用）
- 輸出解析度依問卷設定（預設 1080p）
- 適合上傳 YouTube、社群媒體、直接交件

**FCPXML** — 保留完整時間軸，進 Final Cut Pro 手動微調
- 輸出 `.fcpxml` 格式，可直接匯入 Final Cut Pro 或 DaVinci Resolve
- 保留所有剪輯、字幕、BGM、轉場資訊
- 適合需要人工微調細修的進階使用者
- 不用從零開始，AI 先幫你剪好，你再手動調整細節

---

## 技術亮點

### 實戰經驗的結晶

SKILL.md 中收錄了 10 條從實際剪片專案中歸納的經驗教訓，例如：

- BGM 碎裂問題（先 silence 後 BGM）
- 追加字幕前要先清舊軌道（否則會疊出多軌）
- 每一步操作前先 `get_timeline()` 確認最新狀態
- 處理whisper幻覺、斷句，以及時間軸對齊問題

這些都是實際踩過的坑，轉化為 SOP 中的鐵則。

---

## Demo 影片

上面的嵌入影片就是使用這個 Skill 自動剪輯出來的成果。從素材匯入到最終輸出，全程由 AI Agent 自動執行，完全不需要手動操作 Palmier Pro。

<iframe width="560" height="315" src="https://www.youtube.com/embed/jOTInopBvF0" frameborder="0" allowfullscreen></iframe>

---

## 原始碼與授權

專案原始碼在 GitHub 上開源：

👉 [https://github.com/vanix/palmier-autocut-skill](https://github.com/vanix/palmier-autocut-skill)

採用 MIT 授權，歡迎 fork、改寫、提交 PR。

---

## 下一步規劃

- [ ] 之後還想要支援「純影片無語音」的影片類型
- [ ] 自動產生配音的免費方案

---

如果你也對 AI 自動化剪輯有興趣，歡迎試試這個 Skill，有任何問題或建議歡迎在 GitHub 上開 Issue！
