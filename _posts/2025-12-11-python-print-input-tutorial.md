---
author: 歐巴計概
date: 2025-12-11 02:01:21 +0000
layout: post
permalink: /2025/12/python-print-input-tutorial.html
title: Python 基礎：print 和 input 輸入輸出基礎教學

categories: [教學, 程式教學]
tags: [Python, 程式教學, print, input]
---

## 課程概要：你會學到什麼？
1. 用 `print()` 輸出文字、數字與變數  
2. 用 `sep`、`end` 控制輸出格式（空白與換行）  
3. 用 `input()` 接收輸入並存到變數  
4. 把輸入資料組成句子（字串相加 / f-string）  
 
<iframe width="560" height="315"
        src="https://www.youtube.com/embed/OCMkUz74R3s"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

## 課程概要
在這一單元中，我們將學習如何在 Python 中顯示文字以及如何從使用者那裡輸入資料。我們將主要介紹兩個功能：`print` 與 `input`。

## 1. `print()`：把內容顯示到螢幕上
`print()` 是 Python 最常用的輸出函數，可以印出字串、數字、或變數的值。

### 1-1 基本用法（預設會換行）
- 字串用引號包起來（單引號或雙引號都可以）
- 每次呼叫 `print()`，預設會在結尾加上換行

### 範例：
```python
print("國昌哥哥！")
print("我們來接你了唷！")
```
#### 執行結果：
```
國昌哥哥！
我們來接你了唷！
```

### 1-2 同一行輸出多個值：逗號 , 與 sep
你可以在 print() 內放多個值，用逗號 , 隔開。
預設會用一個空白把它們串起來。

```python
print("你好", "Python")
```
#### 執行結果：
```
你好 Python
```

如果你想改變中間的分隔符號，可以用 `sep`：
```python
print("2026", "01", "06", sep="-")
```
#### 執行結果：
```
2026-01-06
```

### 1-3 控制結尾不要換行：`end`
print() 預設結尾是換行（end="\n"）。
如果你希望不要換行，或想用別的符號結尾，可以設定 end。

```python
print("載入中", end="...")
print("完成！")
```
#### 執行結果：
```
載入中...完成！

```

### 1-4 印出變數與數字
變數相關內容請見下一篇教學

```python
name = "小明"
age = 12
print("名字：", name)
print("年齡：", age)
```
#### 執行結果：
```
名字： 小明
年齡： 12
```

## 2. `input()`：從使用者取得輸入
`input()` 用於接收使用者輸入。使用者在終端機（或互動視窗）輸入內容並按下 Enter 後，程式才會往下執行。


### 2-1 基本用法：把輸入存到變數
- `input("提示文字")` 的提示文字是可選的
- `input()` 回傳的結果永遠是字串（str）

### 範例：
```python
name = input("請輸入要上車的名字：")
print(name,",我們來接你了唷")
```
#### 執行結果：
```
請輸入要上車的名字：文哲哥哥
文哲哥哥 ,我們來接你了唷
```

### 2-2 把輸入組成句子：兩種常見寫法
寫法1：字串相加（需要注意空白與標點）

```python
name = input("請輸入你的名字：")
greeting = "哈囉，" + name + "，歡迎來到Python世界！"
print(greeting)
```
#### 執行結果：
```
請輸入你的名字：宅爸
哈囉，宅爸，歡迎來到Python世界！
```

寫法2：f-string（可讀性更好）
```python
name = input("請輸入你的名字：")
print(f"哈囉，{name}，歡迎來到 Python 世界！")
```
#### 執行結果：
```
請輸入你的名字：宅爸
哈囉，宅爸，歡迎來到Python世界！
```

### 2-3 新手注意！`input()` 是字串，輸入後無法直接做算數運算
```python
a = input("請輸入 a：")
b = input("請輸入 b：")
print(a + b)
```
#### 執行結果：
```
23
```
有關運算部分，請見下一篇教學文章

## 3. 常見錯誤
- 忘記引號：
`print(你好)` 會出錯，應該是 `print("你好")`

- 字串相加的型別錯誤：
`print("你好" + 123)` 會出錯
解法：`print("你好" + str(123))` 或用 f-string：`print(f"你好{123}")`


## 課程小結
在本單元中，我們學習了 `print()` 及 `input()` 輸入輸出的基本使用方法。希望大家能夠加以練習，實際操作來熟悉這些功能。如果在過程中有任何問題，隨時可以在留言板提出。

- `print()` 用來輸出內容到螢幕
  - 逗號可輸出多個值
  - sep 控制中間分隔符，end 控制結尾是否換行
- `input()` 用來接收使用者輸入
  - 回傳結果永遠是字串
