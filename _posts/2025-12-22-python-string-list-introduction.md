---
author: 歐巴計概
date: 2025-12-22 20:20:59 +0000
layout: post
permalink: /2025/12/python-string-list-introduction.html
title: Python 基礎：字串處理與串列

categories: [教學, 程式教學]
tags: [Python, 程式教學, 字串, 串列, List, String]
---

# Python 基礎：字串處理與串列的完整教學

在 Python 程式設計中，**字串（String）**和**串列（List）**是兩個最基本也最常用的資料結構。無論你是初學者還是有經驗的開發者，掌握這兩種資料類型的操作方法都是必備技能。本篇文章將帶你深入了解字串與串列的所有重要概念，以及常見的錯誤與重點整理，幫助你建立扎實的 Python 基礎。

## 1. 字串的基本概念

### 1.1 什麼是字串？

**字串（String）**是由零個或多個字元組成的有序序列，在 Python 中用單引號（''）或雙引號（""）包覆起來表示。字串是 Python 中最常見的資料類型之一，廣泛應用於文字處理、檔案操作、網路通訊等各種場景。

```python
# 字串的建立
str1 = 'Hello'
str2 = "World"
str3 = '你好，Python！'

print(str1)  # 輸出：Hello
print(str2)  # 輸出：World
print(str3)  # 輸出：你好，Python！
```

### 1.2 字串的特性

Python 的字串具有以下重要特性：

1. **不可變性（Immutable）**：字串一旦建立就不能直接修改，只能建立新的字串。
2. **有序性（Ordered）**：字串中的每個字元都有明確的索引位置，從 0 開始。
3. **可迭代（Iterable）**：可以使用 for 迴圈逐一存取字串中的每個字元。

### 1.3 字串的索引與切片

字串的索引從 0 開始，我們可以透過索引來存取特定的字元：

#### 索引存取

```python
text = "Python"
print(text[0])  # 輸出：P
print(text[1])  # 輸出：y
print(text[-1])  # 輸出：n（倒數第一個）
```
#### 切片操作
切片操作可指定起始值、結束值、間隔值，如：`text[起始值:結束值:間隔值]`
```python
text = "Python"
print(text[0:3])  # 輸出：Pyt（擷取索引 0 到 2）
print(text[::2])  # 輸出：Pto（每隔一個字元擷取）
print(text[::-1])  # 輸出：nohtyP（反轉字串）
```

## 2. 字串的常用方法

Python 提供了豐富的字串方法，以下是一些最常用的：

### 2.1 大小寫轉換

```python
text = "Hello Python"
print(text.upper())  # 轉換為大寫，輸出：HELLO PYTHON
print(text.lower())  # 轉換為小寫，輸出：hello python
print(text.title())  # 每個單字首字母大寫，輸出：Hello Python
print(text.capitalize())  # 句首字母大寫，輸出：Hello python
```

### 2.2 字串搜尋與取代

```python
text = "Hello, World!"
print(text.find("World"))   # 搜尋子字串位置，輸出：7
print(text.find("Python"))  # 搜尋子字串位置，輸出：-1（找不到）

print("World" in text)      # 檢查是否包含子字串，輸出：True

print(text.replace("World", "Python"))  # 取代字串，輸出：Hello, Python!
print(text.replace("o", "O", 1))        # 取代字串，輸出：HellO, World!（只取代第一個）
```

### 2.3 字串分割與合併

```python
text = "apple,banana,cherry"

fruits = text.split(",") # 分割字串
print(fruits)  # 輸出：['apple', 'banana', 'cherry']

poem = "春眠不覺曉\n處處聞啼鳥\n夜來風雨聲\n花落知多少" # 多行文字分割
lines = poem.split("\n")
print(lines)  # 輸出：['春眠不覺曉', '處處聞啼鳥', '夜來風雨聲', '花落知多少']

words = ['Hello', 'World'] # 用分隔符號合併串列
result = ' '.join(words)
print(result)  # 輸出：Hello World
```

## 3. 串列的基本概念

### 3.1 什麼是串列？

**串列（List）**是 Python 中最常用的可變資料結構，可以容納多個元素，這些元素可以是不同的資料類型。串列使用方括號 [] 來表示，元素之間用逗號分隔。

#### 串列的建立


```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]

print(fruits)   # 輸出：['apple', 'banana', 'cherry']
print(numbers)  # 輸出：[1, 2, 3, 4, 5]
print(mixed)    # 輸出：['hello', 42, 3.14, True]
```

### 3.2 串列的特性

串列具有以下特性：

1. **可變性（Mutable）**：串列可以原地修改，新增、刪除、變更元素。
2. **有序性（Ordered）**：元素有明確的順序和索引位置。
3. **可包含不同類型**：一個串列可以同時包含整數、字串、浮點數等多種資料類型。
4. **可嵌套（Nested）**：串列可以包含其他串列，形成多維結構。

### 3.3 串列的索引與切片

與字串類似，串列也支援索引和切片操作：

#### 索引存取

```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[0])   # 輸出：0
print(numbers[-1]) # 輸出：5（倒數第一個）
```

#### 切片操作
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # 輸出：[1, 2, 3]
print(numbers[::2])   # 輸出：[0, 2, 4]（每隔一個）
print(numbers[::-1])  # 輸出：[5, 4, 3, 2, 1, 0]（反轉）
```

## 4. 串列的常用方法

### 4.1 新增元素

```python
fruits = ["apple", "banana"]

fruits.append("cherry") # 新增到末尾
print(fruits)  # 輸出：['apple', 'banana', 'cherry']

fruits.insert(1, "orange") # 新增到指定位置
print(fruits)  # 輸出：['apple', 'orange', 'banana', 'cherry']

fruits.extend(["grape", "melon"]) # 擴展串列
print(fruits)  # 輸出：['apple', 'orange', 'banana', 'cherry', 'grape', 'melon']

fruits = fruits + ["watermelon"] # 使用 + 運算子
print(fruits)  # 輸出：['apple', 'orange', 'banana', 'cherry', 'grape', 'melon', 'watermelon']
```

### 4.2 刪除元素

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana") # 刪除第一個匹配的元素
print(fruits)  # 輸出：['apple', 'cherry', 'banana']

deleted = fruits.pop() # 刪除指定索引的元素（預設最後一個）
print(deleted)  # 輸出：cherry
print(fruits)   # 輸出：['apple']

fruits.clear() # 清空串列
print(fruits)  # 輸出：[]
```

### 4.3 搜尋與排序

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(numbers.index(4))    # 搜尋元素位置，輸出：2
print(1 in numbers)        # 搜尋元素位置，輸出：True

print(numbers.count(1))    # 計算元素出現次數，輸出：2

numbers.sort()  # 排序，預設從小排到大
print(numbers)  # 輸出：[1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True) # 從大排到小
print(numbers)  # 輸出：[9, 6, 5, 4, 3, 2, 1, 1]
```

### 4.4 列表推導式

列表推導式是 Python 中強大且簡潔的語法，可以用一行程式碼建立新串列：

```python
squares = [x**2 for x in range(10)] # 建立一維串列
print(squares)  # 輸出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = [x**2 for x in range(10) if x % 2 == 0]  # 條件過濾並建立一維串列
print(even_squares)  # 輸出：[0, 4, 16, 36, 64]

matrix = [[i*j for j in range(3)] for i in range(3)] # 建立二維串列
print(matrix)  # 輸出：[[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

## 5. 字串與串列的轉換

字串和串列之間的轉換是 Python 程式設計中非常常見的操作：

### 5.1 字串轉串列

#### 使用 list() 將字串轉為字元串列
```python
text = "Python"
char_list = list(text)
print(char_list)  # 輸出：['P', 'y', 't', 'h', 'o', 'n']
```
#### 使用 split() 依分隔符號分割
```python
words = "apple banana cherry".split(" ")
print(words)  # 輸出：['apple', 'banana', 'cherry']
```

### 5.2 串列轉字串

#### 使用 join() 將串列合併為字串
```python
char_list = ['P', 'y', 't', 'h', 'o', 'n']
text = ''.join(char_list)
print(text)  # 輸出：Python
```
#### 用分隔符號連接
```python
words = ['apple', 'banana', 'cherry']
result = ', '.join(words)
print(result)  # 輸出：apple, banana, cherry
```

### 5.3 實際應用範例

#### 範例：計算字串中每個字元出現的次數
```python
text = "hello world"
char_count = {}

for char in text:
    if char != ' ':  # 忽略空格
        char_count[char] = char_count.get(char, 0) + 1

print(char_count)  # 輸出：{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

#### 範例：檢查回文
```python
def 是回文(word):
    return word == word[::-1]

print(是回文("madam"))   # 輸出：True
print(是回文("hello"))   # 輸出：False
```

## 6. 字串、串列與迴圈的結合

字串和串列可以直接結合for迴圈。

### 6.1 字串與迴圈

字串有幾個字，迴圈就執行幾次，並且每一回合會把一個字母放進迴圈的變數裡
```python
text="Python"
for i in text:
  print(i)
```
```輸出
P
y
t
h
o
n
```

### 6.2 串列與迴圈

串列有幾筆資料，迴圈就執行幾次，並且每一回合會把一筆資料放進迴圈的變數裡
```python
fruits=["apple","banana","grapes"]
for i in fruits:
  print(i)
```
```輸出
apple
banana
grapes
```
## 7. 常見錯誤與解決方案

### 7.1 字串不可變導致的錯誤

**錯誤範例**：
```python
text = "Hello"
text[0] = "J"  # TypeError: 'str' object does not support item assignment
```

**解決方案**：建立新的字串
```python
text = "Hello"
text = "J" + text[1:]
print(text)  # 輸出：Jello
```

### 7.2 串列切片越界

**錯誤範例**：
```python
numbers = [1, 2, 3]
print(numbers[10])  # IndexError: list index out of range
```

**解決方案**：先檢查長度
```python
numbers = [1, 2, 3]
if len(numbers) > 10:
    print(numbers[10])
else:
    print("索引越界")
```

### 7.3 修改串列時漏用回傳值

**錯誤範例**：
```python
def 排序串列(items):
    items.sort()  # 原地排序，但忘記回傳

numbers = [3, 1, 2]
result = 排序串列(numbers)
print(result)  # 輸出：None
```

**解決方案**：確保函數有回傳值
```python
def 排序串列(items):
    return sorted(items)  # 返回新串列

numbers = [3, 1, 2]
result = 排序串列(numbers)
print(result)  # 輸出：[1, 2, 3]
```

### 7.4 字串編碼問題

**錯誤範例**：
```python
text = "你好"
print(text.encode('ascii'))  # UnicodeEncodeError
```

**解決方案**：指定正確的編碼
```python
text = "你好"
print(text.encode('utf-8'))  # 正常輸出
```

## 8. 結論

字串和串列是 Python 程式設計中最基本也最重要的資料結構。透過本篇文章，我們學習了：

- 字串的基本概念、常用方法與格式化技巧
- 串列的建立、操作與列表推導式
- 字串與串列之間的轉換方法
- 常見的錯誤類型與解決方案


## 9. 換你動手做做看囉


程式設計最重要的是動手實作！快來挑戰看看：

- **步驟 1**：連到解題網：[http://163.30.43.15/](http://163.30.43.15/)
- **步驟 2**：註冊帳號且登入，加入課程。
    - **課程代碼**：`SzNTKb` （若已註冊過就不需再註冊）
- **步驟 3**：練習完成以下作業：
    1. **第 8 個作業**：YouTube 線上課程 - 字串與串列

持續練習，將所學應用於解題中，有助於鞏固這些基礎概念，並提升你的 Python 程式設計能力！

