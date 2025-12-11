---
author: 歐巴計概
date: 2025-12-11 02:01:21 +0000
layout: post
permalink: /2025/12/python-print-input-tutorial.html
title: Python 基礎：Print 和 Input 函數教學

categories: [教學, 程式教學]
tags: [Python, 程式教學, Print, Input]
---

# Python 基礎：Print 和 Input 函數教學

## 課程概要
在這一單元中，我們將學習如何在 Python 中顯示文字以及如何從使用者那裡輸入資料。我們將主要介紹兩個功能：`print` 與 `input`。

## 1. Print 函數
`print` 用於將資料顯示在畫面上，類似於 App Inventor 中的標籤功能。

### 使用方法：
- 在 `print` 函數中放入需要顯示的文字，必須用雙引號括起來。
- 每呼叫一次 `print`，預設會換行。

### 範例：
```python
print("你好，Python！")
print("最近的電腦功能一定很煩！")
```
#### 執行結果：
```
你好，Python！
最近的電腦功能一定很煩！
```

### 連續顯示多行文字
若要在同一行顯示多段文字，可以使用逗號 `,` 隔開：

```python
print("最近的電腦功能一定很煩！", "你好，Python！")
```
#### 執行結果：
```
最近的電腦功能一定很煩！ 你好，Python！
```

### 改變結尾符號
若希望結尾不換行，可以使用 `end` 參數指定結尾符號，如點點號：

```python
print("Hello", end="...")
print(" Python")
```
#### 執行結果：
```
Hello... Python
```

## 2. Input 函數
`input` 用於從使用者那裡接收輸入資料。

### 使用方法：
- 使用 `input` 函數可以讓使用者輸入資料，並將這些資料存入變數中。
- 必須給 `input` 函數一個提示字串。

### 範例：
```python
name = input("請輸入你的名字：")
print("哈囉,", name)
```
#### 執行結果：
```
請輸入你的名字：小明
哈囉, 小明
```

### 合併文字
可以將輸入的資料與其他文字結合，如下：

```python
name = input("請輸入你的名字：")
greeting = "哈囉," + name + "，歡迎來到Python世界！"
print(greeting)
```
#### 執行結果：
```
請輸入你的名字：小華
哈囉, 小華，歡迎來到Python世界！
```

## 課程小結
在本單元中，我們學習了 `print` 及 `input` 函數的基本使用方法。希望大家能夠加以練習，實際操作來熟悉這些功能。如果在過程中有任何問題，隨時可以在留言板提出。接下來，我們將有幾分鐘的時間進行練習！
