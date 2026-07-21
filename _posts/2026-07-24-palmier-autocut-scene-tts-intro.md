---
author: 宅爸
date: 2026-07-24 21:35:00 +0000
layout: post
permalink: /2026/07/palmier-autocut-scene-tts-intro.html
title: 場景式 AI 自動剪片進化版 — 自動切場景、寫旁白、合成語音，一條龍搞定！

categories: [教學, AI應用]
tags: [AI, Agent, OpenCode, Palmier Pro, 影片剪輯, 自動化, MCP, TTS, 台灣藍鵲, 場景剪輯]
---

如果你已經看過上一篇〈[自製 Palmier AutoCut Skill](/2026/07/palmier-autocut-skill-intro.html)〉，那套 Skill 解決的是「後製自動化」——幫你把已經拍好的素材做粗剪、上字幕、配樂。

但宅爸我後來遇到另一種需求：**旅遊 Vlog、開箱影片**。這類影片的痛點不是後製，而是**前製敘事**——素材東一段西一段，而且素材內容也沒有聲音，不知道怎麼組織成一個有頭有尾的故事。

於是我寫了第二個 Skill — **Palmier AutoCut Scene TTS**（[GitHub 開源](https://github.com/vanix/palmier-autocut-scene-tts)），專攻**場景式剪片**：自動切場景 → 視覺描述 → 寫旁白 → TTS 語音合成 → 組 timeline → 輸出 MP4。

整個過程嘗試使用開源軟體跟模型，目標是不花任何一毛錢就可以剪出成果，不過成品還有改善空間就是了

> 測試平台是Apple M2，記憶體16GB，AI Agent使用OpenCode，其他系統就得自行測試了

---

## Demo 影片

下面這支影片就是用這個 Skill 全自動剪輯出來的。從原始素材到最終輸出，全程 AI Agent 自動完成：

<iframe width="560" height="315" src="https://www.youtube.com/embed/WScbSQn-2KU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## 場景式剪片 vs 傳統剪片

傳統剪輯流程是你打開剪輯軟體，手動在時間軸上拉片段、加轉場、打字幕、錄旁白。做得好的話當然很讚，但每個步驟都很花時間。

場景式剪片的思路不同：

| | 傳統做法 | 場景式自動化 |
|:-:|:---------|:------------|
| 素材組織 | 手動看一遍，決定怎麼剪 | ffmpeg 自動偵測場景切換點，每段變一個 clip |
| 敘事架構 | 自己思考故事線 | Qwen2.5VL 逐畫面描述內容，AI 判斷哪些畫面有意義 |
| 旁白 | 自己寫稿、自己錄音 | AI 寫 15-25 字口語旁白 + TTS 語音合成 |
| 剪輯 | 手動拉時間軸 | Palmier Pro MCP 自動上片、上字幕、上音軌 |
| 輸出 | 手動渲染 | 一鍵輸出 MP4 |

---

## 完整流程拆解

這支 Skill 的完整流程分成 7 個階段：

### Phase 1：互動問卷

開工前先問 5 個問題：素材路徑、最大場景秒數、旁白風格、TTS 引擎（Edge TTS / 台灣藍鵲 TTS）、BGM 風格。問完確認後才開始。

### Phase 2：場景切割

用 ffmpeg 的 `scene detect` 功能，門檻值 0.15，自動找出影片中的場景切換點。小於 1 秒的走道晃動片段會自動合併到前後段，避免一堆垃圾片段。

每個場景裁成獨立的 MP4 檔，寫入 `temp/manifest.json`。

### Phase 3：視覺描述 + 過濾

Qwen2.5VL 對每個場景的縮圖做視覺描述。然後我依規則過濾：

- 模糊、晃動 → 跳過
- 畫面高度重複 → 只留代表性片段
- 與主題無關 → 跳過

這一步做完，素材從原始幾十段變成有敘事價值的 30-40 段。

### Phase 4：旁白撰寫（✋ 檢查點）

這是整個流程的關鍵。AI 同時參考 Qwen 的視覺描述與檔案名稱，寫 15-25 字的**輕鬆口語旁白**。

寫完後**暫停**，輸出旁白表給使用者確認：

```
=== 旁白檢查表 ===
001 │ 貴賓室位置        │  4.0s  │ 走～來看看日航貴賓室在哪
002 │ 躺著就到貴賓室的貴賓│  4.0s  │ 女兒躺著就到貴賓室，真不愧是貴賓
...
```

你可以逐句修改，滿意了再按 `y` 繼續。這個檢查點是我實際剪片後加的——AI 寫的旁白有時候太ㄎㄧㄤ，需要人拉回來。

### Phase 4b：TTS 語音合成

支援兩種 TTS 引擎：

| 引擎 | 優點 | 輸出格式 |
|:----|:-----|:---------|
| Edge TTS（微軟） | 免安裝、速度快 | MP3 |
| **台灣藍鵲 TTS** | 台灣華語、**支援自訂聲音向量** | WAV |

台灣藍鵲 TTS（[GitHub](https://github.com/OpenFormosa/BlueMagpie-TTS)）是 OpenFormosa 社群開發的開源 TTS 模型，專為台灣華語打造。最酷的是你可以用自己的聲音向量（`my_voice.pt`），AI 就用你的聲音來講旁白。

TTS 生成後會自動做兩件事：
1. **loudnorm 統一音量**－所有音檔正規化到 -16 LUFS，不會有的段落大聲、有的小聲
2. **淡入 0.5 秒**－每段旁白開頭平滑切入，不突兀

### Phase 4c：CC0 背景音樂

依問卷選擇的風格（輕鬆／活潑／寧靜／自訂），搜尋 CC0 授權的免費 BGM 下載到 `temp/bgm/`。

### Phase 5：Palmier Pro 自動剪輯

這一步讓所有東西兜起來。透過 MCP API 對 Palmier Pro 下指令：

1. 開新專案、匯入素材
2. `add_clips` 依序上 35 段場景（影片用 `source` 指定區間，圖片固定 4 秒）
3. `add_texts` 上字幕（白字 48pt，置中下方）
4. TTS 放到 **A1 音軌**（不指定 trackIndex，自動建立）
5. BGM 放到 **A2 音軌**（指定 `trackIndex: A1_index + 1`，音量 0.08 + 2 秒淡入淡出）
6. `export_project` 輸出 MP4

---

## 踩過的坑（經驗教訓）

寫這個 Skill 的過程踩了不少坑，整理成 SKILL.md 裡的 15 條鐵則。挑幾個經典的：

### 坑 1：BGM 被 TTS 蓋掉

第一次放 BGM 時沒指定 `trackIndex`，結果 BGM 跟 TTS 擠進同一條 A1 軌，BGM 直接把 TTS 蓋掉。解法：TTS 先放（auto-create A1），BGM 指定 `trackIndex: A1_index + 1` 放 A2。

### 坑 2：`endFrame` 超過音檔長度被拒絕

音檔 clip 用 `endFrame` 指定長度，如果超過音檔真實長度，Palmier Pro 會**靜默拒絕**該 clip。解法：改用 `source: [0, duration_sec]`，指定來源區間而非終點 frame。

### 坑 3：同一個 `add_clips` call 要塞全部 TTS，不要 for 迴圈逐個 call

一開始傻傻地在迴圈裡逐段 add TTS，結果每個 call 都要等 response，35 段 TTS 要等 35 次 round-trip。解法：一次 call 全部 35 段 TTS。

---

## 安裝與使用

### 安裝

```bash
# 下載 Skill
git clone https://github.com/vanix/palmier-autocut-scene-tts.git \
  ~/.config/opencode/skills/palmier-autocut-scene-tts

# 依賴
brew install ffmpeg
brew install ollama && ollama pull qwen2.5vl:7b

# TTS 引擎（二選一）
pip install edge-tts              # Edge TTS
pip install bluemagpie-tts soundfile  # 台灣藍鵲 TTS（選用）
```

### MCP 設定

在 `~/.config/opencode/opencode.json` 中加入：

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

### 使用

在 OpenCode 中輸入：

```
幫我剪片，素材在 ~/Desktop/影片主題資料夾/
```

依序回答問卷，旁白寫完後會暫停讓你修改，確認後自動完成 TTS → BGM → Palmier Pro 剪輯 → 輸出 MP4。

---

## 輸出產物

執行完後素材資料夾內會產生：

| 檔案 | 用途 |
|:----|:------|
| `影片主題-v?.mp4` | 最終影片 |
| `subtitles.srt` | 標準字幕檔 |
| `script_narrative.txt` | 給人看的剪輯腳本 |
| `temp/manifest.json` | 管線核心資料檔 |
| `temp/tts/*.wav` | TTS 旁白音檔 |
| `temp/bgm/bgm.mp3` | CC0 背景音樂 |

---

## 原始碼與授權

專案原始碼在 GitHub 上開源：

👉 [https://github.com/vanix/palmier-autocut-scene-tts](https://github.com/vanix/palmier-autocut-scene-tts)

MIT 授權，歡迎 fork、改寫、提交 PR。

---

## 下一步

- 旁白內容可以更符合素材
- 影片素材長度可以符合旁白長度
- 支援多語系字幕（日文、英文）

如果你對場景式 AI 自動剪片有興趣，歡迎試試這個 Skill，有任何問題或建議歡迎在 GitHub 上開 Issue！
