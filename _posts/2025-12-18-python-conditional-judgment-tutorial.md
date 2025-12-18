---
author: 歐巴計概
date: 2025-12-18 11:05:01 +0000
layout: post
permalink: /2025/12/python-conditional-judgment-tutorial.html
title: Python 基礎：條件判斷觀念教學

categories: [教學, 程式教學]
tags: [Python, 程式教學, 條件判斷, if, else, elif]
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/KghpckpI8e4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Python 基礎：條件判斷觀念教學

在這堂課中，我們將學習如何在 Python 中使用條件判斷。以下是本課程的主要內容：

## 1. 單一條件的判斷
- 在 Python 中，條件判斷使用 `if` 來執行。
- 範例程式碼：
  ```python
  grade = int(input("請輸入成績："))
  if grade >= 60:
      print("恭喜及格")
  ```
- 執行結果：
  - 當輸入 `80`，顯示：恭喜及格
  - 當輸入 `30`，無顯示。

## 2. 二選一的條件判斷
- 使用 `if` 和 `else` 來進行條件判斷。
- 範例程式碼：
  ```python
  grade = int(input("請輸入成績："))
  if grade >= 60:
      print("恭喜及格")
  else:
      print("重補修建")
  ```
- 執行結果：
  - 當輸入 `100`，顯示：恭喜及格
  - 當輸入 `50`，顯示：重補修建。

## 3. 複數條件的判斷
- 使用 `elif` 來處理多個條件。
- 範例程式碼：
  ```python
  grade = int(input("請輸入成績："))
  if grade >= 80:
      print("考得不錯")
  elif grade >= 60:
      print("恭喜及格")
  else:
      print("重補修建")
  ```
- 執行結果：
  - 當輸入 `90`，顯示：考得不錯
  - 當輸入 `70`，顯示：恭喜及格
  - 當輸入 `50`，顯示：重補修建。

## 4. 條件判斷的語法
- `if` 語句後需接冒號 `:`
- 額外符合的程式碼需要縮排以表示其隸屬於 `if` 條件內。

## 5. 使用邏輯運算進行複雜條件判斷
- 範例程式碼：
  ```python
  grade = int(input("請輸入成績："))
  if grade >= 80 and grade <= 100:
      print("介於80到100之間")
  ```
- 執行結果：
  - 當輸入 `90`，顯示：介於80到100之間。

## 6. 數字猜測遊戲
- 擴展範例，讓玩家猜隨機生成的數字。
- 範例程式碼：
  ```python
  import random
  number = random.randint(1, 2)
  guess = int(input("猜一個數字（1或2）："))
  if guess == number:
      print("猜對了")
  else:
      print("猜錯了")
  ```
- 執行結果：
  - 若隨機生成數字為 `1` 且使用者輸入 `1`，顯示：猜對了。
  - 若使用者輸入 `2`，顯示：猜錯了。

## 7. 輸入檢查
- 確保輸入的是數字。
- 範例程式碼：
  ```python
  guess = input("請輸入數字：")
  if guess.isdigit():
      guess = int(guess)
      # 繼續進行猜數字的邏輯
  else:
      print("請重新輸入")
  ```
- 執行結果：
  - 若輸入 `abc`，顯示：請重新輸入。

透過本課程，你應該已經學會了如何在 Python 程式中使用條件判斷，並建立簡單的數字猜測遊戲。希望這對你未來的程式開發有幫助！
