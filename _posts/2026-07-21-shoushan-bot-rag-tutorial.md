---
author: 宅爸
date: 2026-07-21 00:07:59 +0000
layout: post
permalink: /2026/07/shoushan-bot-rag-tutorial.html
title: RAG 是什麼？用壽山高中選課小助手看懂 AI 客服機器人的大腦

categories: [教學, AI應用]
tags: [RAG, 機器學習, AI, 客服機器人, 向量資料庫, Python應用, AI Agent, Opencode]
---

# RAG 是什麼？用壽山高中選課小助手看懂 AI 客服機器人的大腦

<iframe src="https://shoushan-bot.onrender.com/" width="100%" height="600" frameborder="0" style="border: 1px solid #ddd; border-radius: 8px; margin-bottom: 20px;"></iframe>


這是因為 ChatGPT 這類大型語言模型（LLM）是「通才」，它學過很多東西，但對特定的、最新的事就不一定準確。

**RAG 就是用來解決這個問題的技術。**

---

## 先講個故事 — 奇怪的通才

想像你到一個大型圖書館，裡面有一位超級厲害的通才管理員。

這位管理員看過全世界的書，幾乎什麼都知道。但他有個毛病：他不會去翻書回答你，而是憑記憶回答。

所以你問他：「壽山高中這個學期的選課時間是什麼時候？」

他可能說：「我記得好像是在 2 月開學的時候，大概是月中吧...」

但實際上學校公告可能是 2 月 10 日上午 8 點。他「大概」對了，但沒完全對。更糟的是，如果是學校今年剛改的新規定，他的記憶可能完全過時。

**RAG 的出現，就是給這位管理員一個明確的指令：不要憑記憶回答，先去翻書，找到答案再來告訴我。**

---

## RAG 是什麼？三個字拆開看

RAG 代表 **R**etrieval **A**ugmented **G**eneration，中文叫「檢索增強生成」。很難懂嗎？我們拆開來看：

### Retrieval（檢索）→ 翻書

使用者問問題後，先去指定的文件庫裡面找相關的段落。

### Augmented（增強）→ 找到的書頁夾進去

把找到的段落當作參考資料，夾進給 AI 的提示詞（prompt）裡面。

### Generation（生成）→ 根據書頁回答

AI 看著這些參考資料，根據資料內容回答問題。

---

## 壽山高中選課小助手

這是一個真實的開源專案（[GitHub](https://github.com/homedad-vanix/shoushan-bot)），直接在壽山高中上線給學生使用。學生登入後問選課問題，系統會從選課文件中找到相關內容，再由 AI 生成回答。

### 架構總覽

```
學生網頁 → Flask 後端 → RAG 檢索 → AI 回答 → 回傳網頁
```

整個流程是：

```
           ┌──────────────────────────────────┐
           │         選課文件（原始文件）       │
           │  ● 高二普通科A班群...             │
           │  ● 選課時間：2/10~2/14...        │
           └────────┬─────────────────────────┘
                    ▼
           ┌──────────────────────────────────┐
           │         RAG 檢索系統              │
           │  1. 把文件切成小塊（chunk）        │
           │  2. 每塊轉成「向量」（embedding）   │
           │  3. 存在向量資料庫（ChromaDB）      │
           └────────┬─────────────────────────┘
                    ▼
   學生問題 ──► ┌──────────────────────────────┐
   例如：         │  搜尋相關區塊                  │
   「高二A班群   │  - cosine 相似度比對           │
   有什麼課？」  │  - 找出最相關的 3~5 塊          │
               └────────┬─────────────────────────┘
                        ▼
               ┌──────────────────────────────────┐
               │  相關文件段落 + 學生問題           │
               │  一起送給 AI（opencode serve）     │
               └────────┬─────────────────────────┘
                        ▼
               ┌──────────────────────────────────┐
               │  AI 根據文件回答學生              │
               │  「高二普通科A班群有以下課程...」  │
               └──────────────────────────────────┘
```

---

## RAG 的實作 — 一步一步看

接下來我用這個專案的程式碼（`rag.py`），解釋 RAG 的每個步驟。

### Step 1：把文件切成小塊（Chunking）

原始選課文件是一大篇文章，不可能整篇丟給 AI（太長、太雜）。所以要先切成一個個小段落。

在 `rag.py` 中，根據文件格式做智慧切割：

```python
def _smart_split(self, text: str) -> List[str]:
    # 如果檔案是用 ● 分章節
    if "●" in text and "===" not in text:
        sections = [part.strip() for part in re.split(r"(?=\n●)", text) if part.strip()]
    # 如果檔案是用 === 分章節
    elif "===" in text:
        sections = [part.strip() for part in re.split(r"(?=^===)", text, flags=re.MULTILINE) if part.strip()]
    # 否則用空行分
    else:
        sections = [part.strip() for part in text.split("\n\n") if part.strip()]
```

每個小塊控制在 600 字以內，太長則再切，但會保留章節標題維持語意。

**Chunking 是 RAG 中非常重要的一步**：切太粗，撈到的段落不精準；切太細，可能遺漏上下文。

### Step 2：把小塊轉成向量（Embedding）

電腦聽不懂中文，但電腦懂數字。所以我們要把每個文字段落轉換成一串數字，這個過程叫 **Embedding**（嵌入）。

這個專案用的是 `paraphrase-multilingual-MiniLM-L12-v2`，一個支援多國語言的句子轉換模型：

```python
self.model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
embeddings = self.model.encode(chunks, normalize_embeddings=True).tolist()
```

這串數字（向量）就像一段文字的「指紋」— 意思相近的文字，向量也會相近。

想像一下：
- 「選課時間是何時？」 → [0.12, 0.87, -0.33, ...]  （768 個數字）
- 「什麼時候可以選課？」 → [0.11, 0.85, -0.30, ...]  （跟上面很像）
- 「今天天氣如何？」 → [-0.45, 0.21, 0.67, ...]     （跟上面差很多）

### Step 3：存進向量資料庫

切好的小塊跟它們的向量一起存進 ChromaDB（一個專門存向量的資料庫）：

```python
self.client = chromadb.PersistentClient(path=self.persist_dir)
self.collection = self.client.get_or_create_collection(
    COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
)

self.collection.add(
    ids=[f"source_{hash}_{index}" for index in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings,
    metadatas=[{
        "source": SOURCE_NAME,
        "source_hash": source_hash,
        "section": self._chunk_name(chunk),
    } for chunk in chunks],
)
```

注意到 `PersistentClient` 嗎？意思是索引會存到磁碟上，伺服器重啟後不用重新算一遍，直接讀取就好。

### Step 4：使用者問問題 → 找相關段落

這是 RAG 最核心的步驟。使用者問了「高二A班群有什麼課？」，系統怎麼找到相關段落？

**第一種：關鍵字精準匹配**

如果問題明確提到某個班群（如「高二普通科A班群」），系統會直接找出對應的章節，不經過語意搜尋：

```python
keyword_map = [
    ("高二普通科A班群", ["高二普通科A班群"]),
    ("高二普通科B班群", ["高二普通科B班群"]),
    ...
]
```

**第二種：語意相似度搜尋（Semantic Search）**

如果問題沒有明確關鍵字（如「我該怎麼選課？」），就用向量比對：

```python
query_embedding = self.model.encode([query], normalize_embeddings=True).tolist()
results = self.collection.query(
    query_embeddings=query_embedding,
    n_results=top_k * 2,  # 多撈一些再過濾
    include=["documents", "distances", "metadatas"],
)
```

這裡用 **cosine 距離** 來比對「問題的向量」跟「每個段落的向量」有多接近。數字越小越接近（0=完全一樣，2=完全相反）。

只要距離小於門檻值（`0.38`），就視為相關段落：

```python
score = 1 - float(distance)  # cosine distance → similarity score
if score >= DEFAULT_RELEVANCE_THRESHOLD:  # 0.38
    selected.append(doc)
```

門檻值 0.38 是調校出來的經驗值，太低會撈到不相干的內容，太高會錯失相關內容。

### Step 5：段落 + 問題 → 送給 AI 回答

找到相關段落後，把它們跟問題包在一起送給 AI：

```python
system_prompt = "你是壽山高中選課小助手..."
prompt = system_prompt + relevant_context + f"\n\n=====\n\n學生的問題：\n{question}"
```

這就像是給管理員說：「你先看這幾頁的內容，然後根據這些回答學生的問題。」AI 有了參考資料，就不會亂掰了。

### Step 6：問題過濾

系統收到問題後，會經過三層防護才送到 AI：

1. **關鍵字預篩選**：學生是不是問選課問題？還是在問天氣、聊八卦？
2. **頻率限制**：避免同一人短時間內大量發問
3. **RAG 檢索 + AI 回答**：通過以上檢查，才開始檢索文件並回答

---

## 為什麼 RAG 比直接把文件餵給 AI 好？

你可能會想：為什麼不直接把整份選課文件放在 AI 的提示詞（prompt）裡面就好？

原因有幾個：

| 問題 | 說明 |
|:----|:-----|
| **長度限制** | AI 模型能處理的文字長度有限（通常是幾千到十幾萬字），但學校文件可能幾萬字 |
| **注意力稀釋** | 文件越長，AI 越不容易找到正確的段落，就像叫你在一百頁的書中找一句話 |
| **更新成本** | 文件一改，就要重新上傳。RAG 只要更新文件庫，重新索引即可 |
| **可溯源** | RAG 可以告訴使用者「這個答案來自第 X 章節」，有憑有據 |

---

## RAG 的三個關鍵零件

總結來說，任何 RAG 系統都由三個核心零件組成：

### 1. Embedding 模型

負責把文字轉成向量。這個專案用 `paraphrase-multilingual-MiniLM-L12-v2`，**多語言** 模型，繁體中文也能處理得很好。

### 2. 向量資料庫

負責儲存向量並快速搜尋。這個專案用 **ChromaDB**，輕量級、支援持久化、支援 cosine 相似度搜尋。

### 3. 大型語言模型（LLM）

負責根據找到的段落生成回答。這個專案透過 **opencode serve** 呼叫 AI 模型來回答問題。

---

## 啟動與執行

整個專案已經部署在 Render.com（免費雲端平台），學生打開網頁即可使用。

### 本地開發

```bash
git clone https://github.com/homedad-vanix/shoushan-bot.git
cd shoushan-bot
pip install -r requirements.txt
python app.py
```

打開 `http://localhost:5000` 就可以看到登入頁面。

### 環境變數

| 變數 | 用途 |
|:----|:-----|
| `RAG_ADMIN_TOKEN` | RAG 管理 API 的密鑰 |
| `RAG_PERSIST_DIR` | 向量索引目錄（正式部署要設為持久化磁碟） |
| `RAG_RELEVANCE_THRESHOLD` | 相關度門檻（預設 0.38） |

### 部署到 Render

Render 會自動讀取 `Procfile`，一行指令都不用改，推上 GitHub 就能一鍵部署。

---

## 管理 RAG 系統

專案提供了完整的 RAG 管理 API，管理者可以：

- `GET /api/rag/stats` — 查看系統狀態（句塊數、模型維度等）
- `GET /api/rag/chunks` — 列出所有句塊
- `POST /api/rag/chunks` — 手動新增句塊（不用重新索引整個文件）
- `PUT /api/rag/chunks/:id` — 更新特定句塊
- `DELETE /api/rag/chunks/:id` — 刪除特定句塊
- `POST /api/rag/rebuild` — 從原始文件重建索引

所有管理 API 都需要 `RAG_ADMIN_TOKEN` 認證，避免被學生偷改。

---

## 結語：RAG 適合哪些場景？

RAG 不是萬能的，但在下列情境非常好用：

- **客服機器人**：根據產品手冊回答（不用把規格書背進 AI）
- **企業內部知識庫**：讓 AI 讀公司 SOP、薪資規定、差旅辦法
- **學校／補習班**：根據課綱、選課文件回答學生問題
- **法律／醫療**：根據法條或藥品說明回答（需要高準確度）

RAG 讓 AI 不再只能憑記憶回答，而是學會了「翻書找答案」，大幅提升了回答的正確性與可信度。

---

如果你對這個專案有興趣，完整的原始碼都在 GitHub 上：

👉 [https://github.com/homedad-vanix/shoushan-bot](https://github.com/homedad-vanix/shoushan-bot)

歡迎 fork、改寫、或實際部署使用！
