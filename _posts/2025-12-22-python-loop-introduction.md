---
author: 歐巴計概
date: 2025-12-22 02:07:14 +0000
layout: post
permalink: /2025/12/python-loop-introduction.html
title: Python 回圈介紹與使用

categories: [教學, 程式教學]
tags: [Python, 程式教學, 回圈, 程式設計]
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/X_w3U5izmJM" frameborder="0" allowfullscreen></iframe>

# Python 回圈介紹與使用

## 1. 回圈的基本概念
- 回圈可分為兩類：
  - 技術回圈：使用指定的開始值、結束值和間隔值決定執行次數。
  - 條件回圈：基於特定條件持續執行，直到條件不成立。

## 2. 技術回圈（For 回圈）的使用
- **範例程式碼**
```python
for i in range(5):
    print("Hello World")
```

- **執行結果**
```
Hello World
Hello World
Hello World
Hello World
Hello World
```

### 2.1 Range 函數的細節
- `range(n)` 的開始值為 0，結束值為 n-1。
- `range(5)` 的值為：0, 1, 2, 3, 4。

### 2.2 範圍指定
- `range(3)` 則會執行 3 次，範圍為：0, 1, 2。

## 3. 2 的 5 次方計算
- **範例程式碼**
```python
result = 1
for i in range(5):
    result *= 2
print(result)
```

- **執行結果**
```
32
```

## 4. 5 階層計算
- **範例程式碼**
```python
result = 1
for i in range(1, 6):
    result *= i
print(result)
```

- **執行結果**
```
120
```

## 5. 條件回圈的使用
- 條件回圈執行直至指定條件不成立。

- **範例程式碼**
```python
result = 1
i = 1
while i < 6:
    result *= 2
    i += 1
print(result)
```

- **執行結果**
```
32
```

## 6. 繪製星星形狀
### 6.1 繪製 3x5 星星
- **範例程式碼**
```python
for _ in range(3):
    for _ in range(5):
        print("*", end="")
    print()  # 換行
```

- **執行結果**
```
*****
*****
*****
```

### 6.2 繪製倒三角形星星
- **範例程式碼**
```python
rows = 3
for j in range(rows):
    for star in range(rows - j):
        print("*", end="")
    print()  # 換行
```

- **執行結果**
```
***
**
*
```

這份教學涵蓋了 Python 回圈的基本概念與實作範例，並詳細介紹了如何使用 `for` 與 `while` 迴圈進行各種計算與形狀繪製。希望能幫助學習者熟悉回圈的使用及其應用。
