---
author: 歐巴計概
date: 2025-12-23 00:07:59 +0000
layout: post
permalink: /2025/12/custom-functions-introduction.html
title: Python 基礎：自訂函數的基礎介紹

categories: [教學, 程式教學]
tags: [Python, 程式教學, 自訂函數]
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/qx0jy-Pzn0k" frameborder="0" allowfullscreen></iframe>

# Python 基礎：自訂函數的基礎介紹

## 1. 函數的基本概念
- 函數分為內建函數和自訂函數。
- 內建函數：Python已經幫你做好，如取最大值、取最小值等。
- 自訂函數：可以自己設計的函數。

例子：將函數視為「烤箱」，輸入食材（input），經過處理後給予成品（output）。

## 2. 自訂函數如何運作
- 當你呼叫一個函數，需給它參數。
- 函數處理並回傳結果。

### 程式碼範例
```python
def 攝氏轉華氏(C):
    F = 1.8 * C + 32
    return F
```
### 執行結果
- 假設C=50，呼叫後會回傳122（華氏）。

## 3. 有回傳和不回傳的函數
- 回傳結果的函數：會返回處理結果。
- 不回傳結果的函數：如垃圾車，處理完不會給你回傳。

### 範例：不回傳結果的函數
```python
def 打招呼(name):
    print("哈囉，" + name)
```
### 執行結果
- 若輸入「宅爸」，則會顯示「哈囉，宅爸」。

## 4. 練習與應用
- 建議將之前的題目重新整理成函數的方式，例如判斷閏年與判斷質數的功能。

### 程式碼範例
```python
def 判斷閏年(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
```
### 執行結果
- 若輸入2020，函數回傳True，表示是閏年。

## 結論
- 自訂函數能讓重複的功能變得簡化，提高程式的可讀性和效率。
- 練習將日常的功能模組化，有助於鞏固函數的概念。
