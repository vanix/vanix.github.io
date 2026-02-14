---
author: 歐巴計概
date: 2025-12-25 00:07:59 +0000
layout: post
permalink: /2025/12/python-built-in-functions.html
title: Python 基礎：常用內建函數教學

categories: [教學, 程式教學]
tags: [Python, 程式教學, 內建函數, Built-in Functions]
---

# Python 基礎：常用內建函數教學

Python 提供了豐富的**內建函數（Built-in Functions）**，這些函數是 Python 語言的一部分，無需額外匯入即可直接使用。熟悉這些內建函數可以讓你的程式碼更加簡潔、有效率。本篇文章將帶你深入了解 Python 常用的內建函數，並特別說明**全域變數**與**區域變數**在函數應用中的概念，以及常見的錯誤與重點整理。

## 1. 內建函數概述

### 1.1 什麼是內建函數？

**內建函數**是 Python 預先定義好的函數，可以直接呼叫使用。這些函數涵蓋了各種常用的操作，包括數學運算、類型轉換、資料結構操作、檔案處理等。

Python 的內建函數數量眾多，官方文件中列出超過 70 個。我們不可能一一介紹，但可以針對最常用的進行詳細說明。

### 1.2 內建函數的優點

1. **無需匯入**：直接使用，無需額外安裝或匯入模組。
2. **效能最佳化**：由 Python 核心團隊優化，執行效率高。
3. **語法簡潔**：使用內建函數通常比自行實作更簡潔、更易讀。
4. **跨平台**：在所有支援 Python 的平台上都能正常運作。

## 2. 數學相關內建函數

### 2.1 基本數學函數

```python
# abs() - 絕對值
print(abs(-5))      # 輸出：5
print(abs(3.14))    # 輸出：3.14

# pow() - 次方運算
print(pow(2, 3))    # 輸出：8（2 的 3 次方）
print(pow(2, 3, 3)) # 輸出：2（2 的 3 次方取餘數 3）

# round() - 四捨五入
print(round(3.7))   # 輸出：4
print(round(3.14159, 2))  # 輸出：3.14（保留兩位小數）

# divmod() - 商和餘數
print(divmod(10, 3))  # 輸出：(3, 1) - 商 3 餘數 1
```

### 2.2 最大值與最小值

```python
numbers = [1, 5, 3, 9, 2]

# max() - 最大值
print(max(numbers))      # 輸出：9
print(max(1, 5, 3))     # 輸出：5

# min() - 最小值
print(min(numbers))      # 輸出：1
print(min(1, 5, 3))      # 輸出：1

# 使用 key 參數
words = ['apple', 'banana', 'cherry', 'date']
print(max(words, key=len))   # 輸出：banana（最長的單字）
print(min(words, key=len))   # 輸出：apple（最短的單字）
```

### 2.3 sum() 加總

```python
numbers = [1, 2, 3, 4, 5]

# 基本加總
print(sum(numbers))           # 輸出：15

# 加總並指定起始值
print(sum(numbers, 10))       # 輸出：25（15 + 10）
```

## 3. 類型轉換內建函數

### 3.1 數字類型轉換

```python
# int() - 轉換為整數
print(int(3.14))       # 輸出：3
print(int("42"))       # 輸出：42
print(int("1010", 2))  # 輸出：10（二進位轉十進位）

# float() - 轉換為浮點數
print(float(10))       # 輸出：10.0
print(float("3.14"))   # 輸出：3.14

# complex() - 轉換為複數
print(complex(1, 2))  # 輸出：(1+2j)
```

### 3.2 字串與串列轉換

```python
# str() - 轉換為字串
print(str(123))        # 輸出：'123'
print(str([1, 2, 3]))  # 輸出：'[1, 2, 3]'

# list() - 轉換為串列
print(list("hello"))   # 輸出：['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3))) # 輸出：[1, 2, 3]

# tuple() - 轉換為元組
print(tuple([1, 2, 3]))  # 輸出：(1, 2, 3)
print(tuple("abc"))      # 輸出：('a', 'b', 'c')
```

### 3.3 布林值轉換

```python
# bool() - 轉換為布林值
print(bool(1))          # 輸出：True
print(bool(0))         # 輸出：False
print(bool(""))        # 輸出：False
print(bool("hello"))   # 輸出：True
print(bool([]))        # 輸出：False（空串列）
print(bool([1, 2]))    # 輸出：True
```

## 4. 迭代相關內建函數

### 4.1 range() 產生數列

```python
# range(stop)
for i in range(5):
    print(i)  # 輸出：0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 6):
    print(i)  # 輸出：2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 輸出：0, 2, 4, 6, 8

# 倒轉
for i in range(5, 0, -1):
    print(i)  # 輸出：5, 4, 3, 2, 1
```

### 4.2 enumerate() 取得索引和值

```python
fruits = ['apple', 'banana', 'cherry']

# 基本用法
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 輸出：
# 0: apple
# 1: banana
# 2: cherry

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 輸出：
# 1: apple
# 2: banana
# 3: cherry
```

### 4.3 zip() 合併多個串列

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['Taipei', 'Taichung', 'Kaohsiung']

# 合併多個串列
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age} 歲, 住在 {city}")
# 輸出：
# Alice, 25 歲, 住在 Taipei
# Bob, 30 歲, 住在 Taichung
# Charlie, 35 歲, 住在 Kaohsiung

# 轉換為串列
result = list(zip(names, ages))
print(result)  # 輸出：[('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

### 4.4 filter() 過濾元素

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 過濾偶數
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 輸出：[2, 4, 6, 8, 10]

# 過濾大於 5 的數
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(greater_than_5)  # 輸出：[6, 7, 8, 9, 10]
```

### 4.5 map() 轉換元素

```python
numbers = [1, 2, 3, 4, 5]

# 每個元素平方
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # 輸出：[1, 4, 9, 16, 25]

# 轉換為字串
str_numbers = list(map(str, numbers))
print(str_numbers)  # 輸出：['1', '2', '3', '4', '5']
```

### 4.6 sorted() 排序

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 升序排序
print(sorted(numbers))  # 輸出：[1, 1, 2, 3, 4, 5, 6, 9]

# 降序排序
print(sorted(numbers, reverse=True))  # 輸出：[9, 6, 5, 4, 3, 2, 1, 1]

# 按字串長度排序
words = ['apple', 'banana', 'cherry', 'date']
print(sorted(words, key=len))  # 輸出：['date', 'apple', 'cherry', 'banana']
```

## 5. 物件操作內建函數

### 5.1 len() 取得長度

```python
# 串列長度
print(len([1, 2, 3, 4, 5]))  # 輸出：5

# 字串長度
print(len("Hello"))  # 輸出：5

# 元組長度
print(len((1, 2, 3)))  # 輸出：3

# 字典長度
print(len({"a": 1, "b": 2}))  # 輸出：2
```

### 5.2 type() 取得類型

```python
print(type(123))       # 輸出：<class 'int'>
print(type(3.14))      # 輸出：<class 'float'>
print(type("hello"))   # 輸出：<class 'str'>
print(type([1, 2, 3])) # 輸出：<class 'list'>
print(type((1, 2, 3))) # 輸出：<class 'tuple'>

# 類型檢查
print(isinstance(123, int))       # 輸出：True
print(isinstance("hello", str))   # 輸出：True
print(isinstance([1, 2], list))   # 輸出：True
```

### 5.3 id() 取得物件識別碼

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))  # 輸出：140123456789012（某個記憶體位址）
print(id(b))  # 輸出：140123456789456（不同位址）
print(id(c))  # 輸出：140123456789012（與 a 相同）

# 使用 is 檢查是否同一物件
print(a is b)  # 輸出：False
print(a is c)  # 輸出：True
```

### 5.4 help() 取得說明

```python
# 取得函數說明
help(print)
help(len)
help(sorted)

# 取得模組說明
import os
help(os)
```

## 6. 全域變數與區域變數

### 6.1 什麼是區域變數？

**區域變數**是在函數內部定義的變數，只能在該函數內部使用：

```python
def 計算總和():
    total = 0  # 區域變數
    for i in range(5):
        total += i
    return total

print(計算總和())  # 輸出：10
# print(total)  # NameError: name 'total' is not defined
```

### 6.2 什麼是全域變數？

**全域變數**是在函數外部定義的變數，可以在整個程式中使用：

```python
base = 10  # 全域變數

def 加基礎值(num):
    return base + num  # 可以存取全域變數

print(加基礎值(5))  # 輸出：15
print(base)         # 輸出：10
```

### 6.3 在內建函數中使用全域變數

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

def 找最大值():
    return max(numbers)  # 使用全域變數

def 找最小值():
    return min(numbers)  # 使用全域變數

print(找最大值())  # 輸出：9
print(找最小值())  # 輸出：1
```

### 6.4 使用 global 關鍵字

```python
count = 0

def 增加計數():
    global count
    count += 1

增加計數()
增加計數()
print(count)  # 輸出：2
```

## 7. 常見錯誤與解決方案

### 7.1 忘記內建函數的回傳值

**錯誤範例**：
```python
numbers = [5, 2, 8, 1]
sorted(numbers)
print(numbers)  # 輸出：[5, 2, 8, 1]（沒有改變！）
```

**解決方案**：使用回傳值或使用原地排序方法
```python
# 方案 1：使用回傳值
numbers = [5, 2, 8, 1]
numbers = sorted(numbers)
print(numbers)  # 輸出：[1, 2, 5, 8]

# 方案 2：使用原地排序
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)  # 輸出：[1, 2, 5, 8]
```

### 7.2 類型不匹配

**錯誤範例**：
```python
print(int("hello"))  # ValueError: invalid literal for int()
```

**解決方案**：先檢查是否為數字字串
```python
def 安全轉整數(s):
    try:
        return int(s)
    except ValueError:
        return None

print(安全轉整數("42"))   # 輸出：42
print(安全轉整數("hello")) # 輸出：None
```

### 7.3 filter() 和 map() 的結果是迭代器

**錯誤範例**：
```python
result = filter(lambda x: x > 2, [1, 2, 3, 4])
print(result[0])  # TypeError: 'filter' object is not subscriptable
```

**解決方案**：轉換為串列
```python
result = filter(lambda x: x > 2, [1, 2, 3, 4])
print(list(result)[0])  # 輸出：3
```

### 7.4 zip() 長度不一致

**錯誤範例**：
```python
a = [1, 2, 3]
b = [4, 5]
result = list(zip(a, b))
print(result)  # 輸出：[(1, 4), (2, 5)]（丢失元素！）
```

**解決方案**：使用 itertools.zip_longest
```python
from itertools import zip_longest

a = [1, 2, 3]
b = [4, 5]
result = list(zip_longest(a, b, fillvalue=0))
print(result)  # 輸出：[(1, 4), (2, 5), (3, 0)]
```

### 7.5 enumerate 起始索引錯誤

**錯誤範例**：
```python
fruits = ['apple', 'banana', 'cherry']
for i, f in enumerate(fruits):
    print(f"{i+1}. {f}")  # 每次都要寫 i+1，很麻煩
```

**解決方案**：使用 start 參數
```python
fruits = ['apple', 'banana', 'cherry']
for i, f in enumerate(fruits, start=1):
    print(f"{i}. {f}")
# 輸出：
# 1. apple
# 2. banana
# 3. cherry
```

## 8. 重點整理

### 8.1 數學相關函數

- **abs()**：絕對值
- **pow()**：次方運算
- **round()**：四捨五入
- **max() / min()**：最大值 / 最小值
- **sum()**：加總

### 8.2 類型轉換函數

- **int() / float() / str()**：基本類型轉換
- **list() / tuple()**：序列轉換
- **bool()**：布林轉換

### 8.3 迭代相關函數

- **range()**：產生數列
- **enumerate()**：取得索引和值
- **zip()**：合併多個串列
- **filter()**：過濾元素
- **map()**：轉換元素
- **sorted()**：排序

### 8.4 物件操作函數

- **len()**：取得長度
- **type() / isinstance()**：類型檢查
- **id()**：物件識別碼
- **help()**：說明文件

### 8.5 全域變數與區域變數

- **區域變數**：在函數內部定義，只能在函數內使用
- **全域變數**：在函數外部定義，可在整個程式使用
- **修改全域變數**：使用 global 關鍵字

### 8.6 常見錯誤提醒

1. sorted() 需要使用回傳值
2. 類型轉換要注意合法性
3. filter() / map() 返回的是迭代器
4. zip() 會截斷不同長度的串列
5. enumerate() 可用 start 指定起始索引

## 9. 結論

Python 的內建函數是程式設計的強大工具，熟練使用這些函數可以讓你的程式碼更加簡潔優雅。本篇文章介紹了最常用的各類內建函數，包括數學運算、類型轉換、迭代處理、物件操作等。

透過練習和實際應用，你會發現這些內建函數能大幅提升開發效率。建议在日常編程中多練習使用這些函數，逐漸形成使用內建函數的習慣。

持續學習，多練習、多應用，你會發現 Python 程式設計越來越順手！
