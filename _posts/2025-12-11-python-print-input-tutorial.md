---
author: 歐巴計概
date: 2025-12-11 02:01:21 +0000
layout: post
permalink: /2025/12/python-print-input-tutorial.html
title: Python 基礎：print 和 input 輸入輸出基礎教學

categories: [教學, 程式教學]
tags: [Python, 程式教學, print, input]
---

# Python 基礎：print 和 input 輸入輸出基礎教學

<iframe width="560" height="315"
        src="https://www.youtube.com/embed/OCMkUz74R3s"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

## 課程概要
在這一單元中，我們將學習如何在 Python 中顯示文字以及如何從使用者那裡輸入資料。我們將主要介紹兩個功能：`print` 與 `input`。

## 1. print 輸出函數
`print` 用於將資料顯示在畫面上，類似於 App Inventor 中的標籤功能。

### 使用方法：
- 在 `print` 函數中放入需要顯示的文字，必須用雙引號括起來。
- 每呼叫一次 `print`，預設會換行。

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

### 將多段文字組合成一行
若要在同一行顯示多段文字，可以使用逗號 `,` 隔開：，兩個字串之間會自動補上一個空白

```python
print("國昌哥哥！", "我們來接你了唷！")
```
#### 執行結果：
```
國昌哥哥！ 我們來接你了唷！
```

### 改變結尾符號
若希望結尾不換行，可以使用 `end` 參數指定結尾符號，如點點號：

```python
print("國昌哥哥！", end="...")
print(" 我們來接你了唷！")
```
#### 執行結果：
```
國昌哥哥！... 我們來接你了唷！
```

## 2. input 輸入函數
`input` 用於從使用者那裡接收輸入資料。

### 使用方法：
- 使用 `input` 函數可以讓使用者輸入資料，並將這些資料存入變數中。
- 給 `input` 函數一個提示字串。（不一定要給，解題時通常都不給）

### 範例：
```python
name = input("請輸入要上車的名字：")
print(name,",我們來接你了唷")
```
#### 執行結果：
```
請輸入要上車的名字：文哲哥哥(請自行輸入任意文字)
文哲哥哥 ,我們來接你了唷
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
請輸入你的名字：宅爸
哈囉, 宅爸，歡迎來到Python世界！
```

## 課程小結
在本單元中，我們學習了 `print` 及 `input` 輸入輸出的基本使用方法。希望大家能夠加以練習，實際操作來熟悉這些功能。如果在過程中有任何問題，隨時可以在留言板提出。接下來，我們將有幾分鐘的時間進行練習！

## 換你動手做做看囉
- 連到解題網：http://163.30.43.15/
  - 註冊帳號且登入，加入課程，課程代碼：SzNTKb （已註冊過就不需再註冊）
  - 練習完成第1個作業：YouTube線上課程 - 課堂作業 print and input
