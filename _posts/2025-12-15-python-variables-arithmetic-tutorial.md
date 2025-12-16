---
author: 歐巴計概
date: 2025-12-15 08:36:19 +0000
layout: post
permalink: /2025/12/python-variables-arithmetic-tutorial.html
title: Python 基礎：變數與算術運算教學

categories: [教學, 程式教學]
tags: [Python, 程式教學, 變數, 算術運算]
---

# Python 基礎：變數與算術運算教學

<iframe width="560" height="315" src="https://www.youtube.com/embed/c6kWZHP2LGI" frameborder="0" allowfullscreen></iframe>

## 課程內容

### 1. 變數概念
- 變數可視為箱子，能存放四種數據：小數、整數、字串（文字）、布林值（True/False）。
- 每種數據類型對應不同的操作：
  - 小數：數值類型。
  - 整數：數值類型。
  - 字串：以雙引號包裹的文字。
  - 布林值：只有 True 和 False 兩種狀態。

### 2. 算術運算符號
- 常用算術運算符號有五種，依執行優先順序為：
  1. 括號
  2. 次方（使用 `**`）
  3. 乘除（`*`、`/`）
  4. 取餘數（使用 `%`）、取商數（使用 `//`）
  5. 加減（`+`、`-`）

#### 範例：
```python
result = (2 + 3) * 4
print(result)
```

#### 執行結果：
```
20
```

### 3. 使用變數
#### 定義變數並顯示內容：
```python
NUM = 100
STR = "100"
BOL = True
FLOAT_NUM = 10.5

print(NUM)  
print(STR)  
print(BOL)  
print(FLOAT_NUM)  
```

#### 執行結果：
```
100
100
True
10.5
```

### 4. 數字與字串相加的例子
#### 錯誤範例：文字相加
```python
I = input("請輸入第一個數字: ")
J = input("請輸入第二個數字: ")
result = I + J
print(result)
```

#### 執行結果：
```
如果輸入 100 和 200，輸出：100200
```

#### 正確範例：數字相加
```python
I = int(input("請輸入第一個數字: "))
J = int(input("請輸入第二個數字: "))
result = I + J
print(result)
```

#### 執行結果：
```
如果輸入 100 和 200，輸出：300
```

### 5. BMI 計算範例
#### 使用者輸入體重（公斤）與身高（公分）來計算 BMI：
```python
W = int(input("請輸入體重(公斤): "))
H = int(input("請輸入身高(公分): ")) / 100  
BMI = W / (H ** 2)
print(BMI) 
```

#### 執行結果：
```
如果輸入 100 和 200，輸出：25.0
```

### 6. 注意事項
- 在使用 `input()` 獲取資料後，資料預設為字串類型。
- 若想做數值計算，必須先將字串轉換為數字（使用 `int()` 或 `float()`）。
- 否則會導致計算錯誤。

### 7. 練習
- 完成兩個範例：兩數相加和 BMI 計算，並確認結果。

請依據課堂內容進行實作與練習，確保理解變數與算術運算的概念。
