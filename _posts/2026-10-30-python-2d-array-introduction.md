---
author: 宅爸
date: 2026-10-30 09:00:00 +0800
layout: post
permalink: /2026/10/python-2d-array-introduction.html
title: APCS初級課程：Python 二維陣列教學｜宣告、存取、走訪與旋轉翻轉
description: "Python 二維陣列完整教學：二維陣列其實就是「串列裡再放串列」，本文從零開始講宣告方式（直接指定、用列表推導式建立 n × m 全 0 矩陣、從輸入讀取）、用 grid[i][j] 取得與修改資料、三種走訪所有格子的迴圈寫法，以及 APCS 最常考的陣列翻轉（上下、左右、轉置）與陣列旋轉（順時針 90 度、逆時針 90 度、180 度）。內含完整可執行程式碼、常見錯誤（別用 [[0]*m]*n！）與 FAQ，適合剛學完串列與迴圈、準備挑戰 APCS 初級的同學。"
categories: [資訊教學, 程式教學]
tags: [Python, APCS, 程式教學, 二維陣列, 巢狀迴圈, 陣列旋轉, 陣列翻轉]
image:
  path: /assets/images/cover/python-2d-array-introduction.png
  alt: Python 二維陣列教學封面，用格子矩陣示意列與欄的索引位置
---

💡 本篇教學重點

這篇是 APCS 初級／中級課程的二維陣列入門，從「怎麼宣告」一路講到「怎麼旋轉」。讀完你應該要能自己寫出：讀入一個 n × m 的矩陣、走訪每一格、把它上下翻轉、左右翻轉、轉置，以及順時針／逆時針旋轉 90 度。

[APCS教學文章列表](https://vanix.github.io/categories/%E7%A8%8B%E5%BC%8F%E6%95%99%E5%AD%B8/)

[APCS實作線上課程](https://www.youtube.com/playlist?list=PLN9g1rvyo05p70K3HU-hWhEkoNs26WhD0)

## 快速答案：Python 的二維陣列怎麼用？

> **快速答案：** Python 沒有內建「二維陣列」這個型別，**二維陣列就是「串列裡面再放串列」**。宣告寫 `grid = [[1, 2, 3], [4, 5, 6]]`；取得某一格寫 `grid[i][j]`（第 i 列、第 j 欄，索引從 0 開始）；走訪所有格子用**兩層 for 迴圈**；旋轉與翻轉則是「依照新的索引規則，把舊矩陣的資料抄到新矩陣」。

一句話記住：**外層索引選「列」，內層索引選「欄」**。把這個順序記牢，後面所有存取、走訪、旋轉都不會亂。

## 二維陣列是什麼？用座位表來理解

想像教室的座位表：你要找到某個同學，會先說「第 3 排」，再說「第 5 個位置」。二維陣列就是這張座位表，每一列（row）本身是一個串列，而整個矩陣是「很多列串起來的串列」。

```text
       欄 0   欄 1   欄 2
列 0 ┌─────┬─────┬─────┐
     │  1  │  2  │  3  │
列 1 ├─────┼─────┼─────┤
     │  4  │  5  │  6  │
列 2 ├─────┼─────┼─────┤
     │  7  │  8  │  9  │
     └─────┴─────┴─────┘
```

對應到 Python 就是：

```python
grid = [
    [1, 2, 3],   # grid[0]
    [4, 5, 6],   # grid[1]
    [7, 8, 9],   # grid[2]
]
```

- `grid` 的長度是 **3**（有 3 列）
- `grid[0]` 的長度是 **3**（這一列有 3 欄）
- `grid[1][2]` 就是 **6**（第 1 列、第 2 欄）

| 名詞 | 英文 | 在 Python 裡的意思 |
| --- | --- | --- |
| 列 | row | 外層串列的索引 `i` |
| 欄 | column | 內層串列的索引 `j` |
| 維度 | dimension | 通常寫成「n × m」，n 是列數、m 是欄數 |

> **常見混淆**：數學上座標常寫成 (x, y)，但在程式裡我們幾乎都用 `grid[列][欄]`，也就是 `grid[row][col]`。APCS 題目的座標也大多是「先列後欄」，別把順序顛倒了。

## 如何宣告二維陣列？三種常見寫法

### 寫法 1：直接指定每一格（資料固定時）

資料量小、或題目直接給定內容時，最直覺的寫法就是把每一列寫出來：

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
print(grid)          # [[1, 2, 3], [4, 5, 6]]
print(len(grid))     # 2（2 列）
print(len(grid[0]))  # 3（每列 3 欄）
```

如果內容是**字元**（例如迷宮地圖），慣用寫法是：

```python
rows = ["..#", ".#.", "..."]
grid = [list(row) for row in rows]
print(grid[0][2])    # '#'
```

> 但這個比較像是一維的字串串列

### 寫法 2：先建立 n × m 的空矩陣（最常用）

絕大多數題目只給 n、m，資料要自己一格一格填，這時就用**列表推導式**建立全 0 矩陣：

```python
n, m = 3, 4                # 3 列 4 欄
grid = [[0] * m for _ in range(n)]

print(grid)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

要填值就搭配巢狀迴圈：

```python
n, m = 3, 4
grid = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        grid[i][j] = i * m + j   # 依序填 0, 1, 2, ...

print(grid)
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
```

如果想要「九九乘法表」這種有規律的內容，一行就能建好：

```python
table = [[i * j for j in range(1, 10)] for i in range(1, 10)]
print(table[2][3])   # 3 * 4 = 12
```

### 寫法 3：從輸入讀進來（APCS 最常見）

APCS 的輸入通常是「第一行給 n m，接下來 n 行、每行 m 個數字」。讀法如下：

我的基礎寫法如下，行數較多但適合初學者

```python
n, m = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
```

行數較短的寫法如下

```python
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
```

上面的 `[list(map(...)) for _ in range(n)]` 就是「讀 n 次，每次都把一整列轉成整數串列」，是解題時最標準的寫法。

### ⚠️ 千萬別這樣寫：`[[0] * m] * n`

這是初學者最常踩、也最難 debug 的雷：

```python
grid = [[0] * 3] * 3     # ❌ 錯誤示範
grid[0][0] = 9

print(grid)
# [[9, 0, 0], [9, 0, 0], [9, 0, 0]]   ← 三列全變了！
```

原因：`[[0] * 3] * 3` 是「把**同一個串列物件**重複 3 次」，三列其實指向同一塊記憶體。改一列等於改三列。

**正確寫法**是用串列推導式，每一列都重新建立：

```python
grid = [[0] * 3 for _ in range(3)]   # ✅ 每一列都是獨立物件
grid[0][0] = 9

print(grid)
# [[9, 0, 0], [0, 0, 0], [0, 0, 0]]
```

**判斷原則：只要看到 `* n` 套在「串列」外面，就要懷疑是不是共用了同一個物件。**

## 如何取得二維陣列的資料？

### 取得單一格：`grid[i][j]`

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(grid[0][0])   # 1（左上角）
print(grid[0][2])   # 3（右上角）
print(grid[2][2])   # 9（右下角）
print(grid[-1][-1]) # 9（負索引：最後一列、最後一欄）
print(grid[-1][0])  # 7（左下角）
```

Python 的負索引在二維陣列一樣好用：`-1` 代表最後一個。

### 取得一整列、一整欄

```python
print(grid[0])              # [1, 2, 3]      取得第 0 列（一整列）
print(grid[-1])             # [7, 8, 9]      最後一列
print([row[1] for row in grid])   # [2, 5, 8]  取得第 1 欄
```

**二維陣列沒有「直接取一整欄」的語法**，因為欄不是獨立的物件，只能靠迴圈或列表推導式把每一列的同一格挑出來。

### 取得一個子矩陣（切片）

切片對「列」有效，對「欄」就要自己處理：

```python
print(grid[0:2])            # [[1, 2, 3], [4, 5, 6]]  前兩列
print([row[0:2] for row in grid])   # 每一列只取前兩欄
# [[1, 2], [4, 5], [7, 8]]
```

## 如何修改二維陣列的資料？

二維串列是**可變（mutable）**的，可以直接指定位置改值，不必建立新物件。

### 修改單一格

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]

grid[1][2] = 99
print(grid)   # [[1, 2, 3], [4, 5, 99]]
```

### 修改一整列

```python
grid[0] = [7, 8, 9]
print(grid)   # [[7, 8, 9], [4, 5, 99]]
```

### 用迴圈批次修改

```python
n, m = 2, 3
grid = [[1] * m for _ in range(n)]

# 每一格都乘 2
for i in range(n):
    for j in range(m):
        grid[i][j] *= 2

print(grid)   # [[2, 2, 2], [2, 2, 2]]
```

### 搭配條件修改（把奇數變 0）

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] % 2 == 1:
            grid[i][j] = 0

print(grid)   # [[0, 2, 0], [4, 0, 6]]
```

> **小提醒**：`grid[0][0] = 9` 改的是「格子」；`grid[0] = [...]` 改的是「整列」。兩者層級不同，別混用了。

## 如何用迴圈走訪二維陣列的所有格子？

走訪（traversal）就是「每一格都拜訪一次」。以下三種寫法都要會，看場合選用。

### 方法一：索引式巢狀迴圈（最萬用）

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]

for i in range(len(grid)):          # 走訪每一列
    for j in range(len(grid[i])):   # 走訪這一列的每一欄
        print(f"({i},{j}) = {grid[i][j]}")
```

輸出：

```text
(0,0) = 1
(0,1) = 2
(0,2) = 3
(1,0) = 4
(1,1) = 5
(1,2) = 6
```

**需要「座標」時一定要用這一種**，例如要找最大值的位置、要輸出座標、要判斷鄰居。

### 方法二：串列結合迴圈的寫法

```python
for row in grid:
    for value in row:
        print(value, end=" ")
    print()
```

輸出：

```text
1 2 3
4 5 6
```

這種寫法讀起來最像人話：「對每一列，對這一列的每一個值」。缺點是**拿不到索引**。

### 方法三：`enumerate` 同時拿索引與內容

```python
for i, row in enumerate(grid):
    for j, value in enumerate(row):
        print(f"grid[{i}][{j}] = {value}")
```

`enumerate` 會回傳「索引 + 元素」，很適合需要索引但又不想寫 `range(len(...))` 的時候。

### 三種寫法怎麼選？

| 寫法 | 拿得到索引嗎 | 適合情境 | 範例 |
| --- | --- | --- | --- |
| `for i in range(n)` 巢狀 | ✅ 兩層都有 | 需要座標、要修改格子、要比較鄰居 | 找最大值位置、走迷宮 |
| `for row in grid` | ❌ 只有內容 | 只讀不寫、加總、列印 | 算總和、印出矩陣 |
| `for i, row in enumerate(grid)` | ✅ 兩層都有 | 想要索引又要程式碼簡短 | 印出「第幾列第幾欄」 |

### 實戰：走訪時做加總、找最大值

**加總所有格子：**

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]

total = 0
for row in grid:
    for value in row:
        total += value

print(total)   # 21
```

**找最大值與它的位置：**

```python
grid = [
    [3, 8, 1],
    [9, 2, 7],
]

max_value = grid[0][0]
max_pos = (0, 0)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] > max_value:
            max_value = grid[i][j]
            max_pos = (i, j)

print(max_value, max_pos)   # 9 (1, 0)
```

**印出整齊的矩陣：**

```python
for row in grid:
    print(*row)          # 1 2 3 ／ 4 5 6
    # 或 print(" ".join(map(str, row)))
```

## 二維陣列的列數與欄數怎麼算？

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]

rows = len(grid)        # 2（列數）
cols = len(grid[0])     # 3（第 0 列的長度，也就是欄數）
```

| 想知道的東西 | 寫法 | 注意事項 |
| --- | --- | --- |
| 有幾列 | `len(grid)` | 永遠安全 |
| 有幾欄 | `len(grid[0])` | 前提是**每一列等長**，且矩陣不是空的 |
| 第 i 列有幾欄 | `len(grid[i])` | 不規則矩陣時必須用這個 |

如果矩陣可能是空的，先判斷 `if not grid:` 再取 `grid[0]`，不然會噴 `IndexError`。

### 不規則的二維陣列（每列長度不同）

Python 允許「每列長度不一樣」，這叫**鋸齒狀陣列（jagged array）**：

```python
triangle = [
    [1],
    [2, 3],
    [4, 5, 6],
]

for i in range(len(triangle)):
    for j in range(len(triangle[i])):   # 用 len(triangle[i]) 才安全
        print(triangle[i][j], end=" ")
    print()
```

輸出：

```text
1
2 3
4 5 6
```

這種結構在「巴斯卡三角形」、「楊輝三角」等題目很常見。**走訪時養成用 `len(grid[i])` 的習慣，就不會越界。**

## 基本題型一：陣列翻轉

翻轉（flip）是「不改變內容，只改變位置」。以下每一種翻轉都會給你**兩種寫法**：

- **寫法 A：迴圈（通用寫法）**：先開一個新矩陣，再用兩層迴圈把舊資料一格一格搬到新位置。程式碼囉嗦，但索引關係一目了然，**任何形狀的矩陣都能用，換成 C、Java 也照樣寫得出來**。
- **寫法 B：切片／列表推導式（Python 捷徑）**：利用 Python 語法一行解決，短、快，但要看得懂才不會誤用。

> 兩種寫法都是**回傳新矩陣**，不會改到原本的 `grid`。先準備一個共用的測試矩陣：

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

### 1. 上下翻轉（垂直翻轉）

把第 0 列和第 n−1 列對調、第 1 列和第 n−2 列對調……索引關係是 **`new[i][j] = old[n-1-i][j]`**。

#### 寫法 A：迴圈（通用寫法）

```python
def flip_vertical_loop(grid):
    n = len(grid)        # 列數
    m = len(grid[0])     # 欄數

    new = [[0] * m for _ in range(n)]      # 新矩陣，大小跟原本一樣

    for i in range(n):
        for j in range(m):
            new[i][j] = grid[n - 1 - i][j]  # 第 i 列抄第 n-1-i 列

    return new

print(flip_vertical_loop(grid))
# [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
```

因為這裡是「整列搬過去」，其實一層迴圈就夠了：

```python
def flip_vertical_loop2(grid):
    n = len(grid)
    new = []
    for i in range(n):
        new.append(grid[n - 1 - i][:])   # [:] 複製一整列，避免共用
    return new
```

#### 寫法 B：切片

```python
def flip_vertical(grid):
    return grid[::-1]      # 反轉「列的順序」

print(flip_vertical(grid))
# [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
```

> 切片版只反轉「外層」的列順序，**內層的列物件還是跟原矩陣共用**。若之後要改動結果，記得每一列也複製：`[row[:] for row in grid[::-1]]`。

### 2. 左右翻轉（水平翻轉）

每一列自己反轉，但列的順序不變。索引關係是 **`new[i][j] = old[i][m-1-j]`**。

#### 寫法 A：迴圈（通用寫法）

```python
def flip_horizontal_loop(grid):
    n = len(grid)
    m = len(grid[0])

    new = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new[i][j] = grid[i][m - 1 - j]   # 同一列，欄反過來

    return new

print(flip_horizontal_loop(grid))
# [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
```

#### 寫法 B：列表推導式

```python
def flip_horizontal(grid):
    return [row[::-1] for row in grid]

print(flip_horizontal(grid))
# [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
```

### 3. 轉置（行列互換，transpose）

把「第 i 列第 j 欄」搬到「第 j 列第 i 欄」。索引關係是 **`new[j][i] = old[i][j]`**，注意新矩陣是 **m 列 × n 欄**（長寬互換）。

#### 寫法 A：迴圈（通用寫法）

```python
def transpose_loop(grid):
    n = len(grid)        # 原來的列數
    m = len(grid[0])     # 原來的欄數

    new = [[0] * n for _ in range(m)]   # 新矩陣：m 列 × n 欄

    for i in range(n):
        for j in range(m):
            new[j][i] = grid[i][j]      # 列欄對調

    return new

print(transpose_loop(grid))
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

> 這裡最容易錯的是 `new` 的大小：**新矩陣是「原本的欄數」列、「原本的列數」欄**。寫成 `[[0] * m for _ in range(m)]` 在方形矩陣剛好不會出錯，遇到長方形就會爆，考試要特別小心。

#### 寫法 B：列表推導式與 `zip`

```python
def transpose(grid):
    n = len(grid)
    m = len(grid[0])
    return [[grid[i][j] for i in range(n)] for j in range(m)]

print(transpose(grid))
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

Python 還有個更短的寫法，用 `zip(*grid)` 把每一欄「打包」起來：

```python
result = [list(col) for col in zip(*grid)]
print(result)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

`zip(*grid)` 會把 `[[1,2,3],[4,5,6],[7,8,9]]` 拆成 `(1,4,7)`、`(2,5,8)`、`(3,6,9)` 三組，剛好就是轉置的結果。注意 `zip` 回傳的是 tuple，外層要再用 `list()` 轉回來，題目要求串列時才不會出錯。

### 翻轉範例對照表（以 3 × 3 為例）

原始矩陣：

```text
1 2 3
4 5 6
7 8 9
```

| 操作 | 結果 |
| --- | --- |
| 上下翻轉 | `7 8 9` / `4 5 6` / `1 2 3` |
| 左右翻轉 | `3 2 1` / `6 5 4` / `9 8 7` |
| 轉置 | `1 4 7` / `2 5 8` / `3 6 9` |

### 兩種寫法怎麼選？

| 比較項目 | 寫法 A：迴圈 | 寫法 B：切片／推導式 |
| --- | --- | --- |
| 速度 | 較慢（Python 迴圈逐格處理） | 較快（底層用 C 實作） |
| 好不好懂 | 高，每個索引都看得到 | 中，要先熟悉切片 |
| 彈性 | 高，可加條件、可中途印出來除錯 | 低，只能整批處理 |
| 出錯風險 | 索引或新矩陣大小寫錯就爆 | 語法短，但容易誤用共用物件 |
| 適用時機 | 初學、長方形矩陣、需要除錯 | 已懂原理、追求程式碼簡潔 |

**建議學習順序：先用迴圈版確認自己真的懂「哪一格搬到哪一格」，再改用切片版加速。** 考場上兩種都寫得出來，才是真的會。

## 基本題型二：陣列旋轉

旋轉是翻轉的進階版：同一個矩陣轉 90 度，所有格子的位置都會變。這裡一樣給你**迴圈版**與**切片版**，最後再整理成一張公式表。

> 寫迴圈版時，建議用「**搬移角度**」思考：`新位置 = 舊位置`，一次只看一格，比較不容易亂。

### 順時針旋轉 90 度

規則：**原本最左邊那一欄，會變成新矩陣的最上面那一列。**

搬移關係是：舊矩陣第 i 列第 j 欄 → 新矩陣第 j 列、第 n−1−i 欄，寫成程式就是 `new[j][n-1-i] = old[i][j]`。

#### 寫法 A：迴圈（通用寫法）

```python
def rotate_clockwise_loop(grid):
    n = len(grid)        # 原列數
    m = len(grid[0])     # 原欄數

    new = [[0] * n for _ in range(m)]   # 新矩陣：m 列 × n 欄

    for i in range(n):
        for j in range(m):
            new[j][n - 1 - i] = grid[i][j]   # 舊(i,j) → 新(j, n-1-i)

    return new

print(rotate_clockwise_loop(grid))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

怕寫錯的話，把迴圈裡的 `i, j` 印出來跑一次 3 × 3，就會看到 `(0,0) → (0,2)`、`(0,1) → (1,2)`、`(0,2) → (2,2)`，剛好是最右邊那一欄。

#### 寫法 B：列表推導式

反過來用「新矩陣座標」的角度看：`new[i][j] = old[n-1-j][i]`，寫成推導式：

```python
def rotate_clockwise(grid):
    n = len(grid)
    m = len(grid[0])
    # 新矩陣是 m 列 × n 欄
    return [[grid[n - 1 - j][i] for j in range(n)] for i in range(m)]

print(rotate_clockwise(grid))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

### 逆時針旋轉 90 度

規則：**原本最右邊那一欄，會變成新矩陣的最上面那一列。**

搬移關係：舊矩陣第 i 列第 j 欄 → 新矩陣第 m−1−j 列、第 i 欄，也就是 `new[m-1-j][i] = old[i][j]`。

#### 寫法 A：迴圈（通用寫法）

```python
def rotate_counterclockwise_loop(grid):
    n = len(grid)
    m = len(grid[0])

    new = [[0] * n for _ in range(m)]   # 新矩陣：m 列 × n 欄

    for i in range(n):
        for j in range(m):
            new[m - 1 - j][i] = grid[i][j]   # 舊(i,j) → 新(m-1-j, i)

    return new

print(rotate_counterclockwise_loop(grid))
# [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
```

#### 寫法 B：列表推導式

```python
def rotate_counterclockwise(grid):
    n = len(grid)
    m = len(grid[0])
    # 新矩陣是 m 列 × n 欄
    return [[grid[j][m - 1 - i] for j in range(n)] for i in range(m)]

print(rotate_counterclockwise(grid))
# [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
```

### 旋轉 180 度

轉 180 度＝上下翻轉＋左右翻轉，搬移關係是 `new[n-1-i][m-1-j] = old[i][j]`。

#### 寫法 A：迴圈（通用寫法）

```python
def rotate_180_loop(grid):
    n = len(grid)
    m = len(grid[0])

    new = [[0] * m for _ in range(n)]   # 新矩陣：n 列 × m 欄

    for i in range(n):
        for j in range(m):
            new[n - 1 - i][m - 1 - j] = grid[i][j]

    return new

print(rotate_180_loop(grid))
# [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
```

#### 寫法 B：切片

```python
def rotate_180(grid):
    return [row[::-1] for row in grid[::-1]]

print(rotate_180(grid))
# [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
```

### 旋轉公式總整理

假設原矩陣是 **n 列 × m 欄**，新矩陣叫 `new`：

| 操作 | 新矩陣大小 | `new[i][j]` 等於 | 搬移寫法（`新[?][?] = 舊[i][j]`） | 白話記法 |
| --- | --- | --- | --- | --- |
| 上下翻轉 | n × m | `old[n-1-i][j]` | `new[n-1-i][j]` | 列反過來 |
| 左右翻轉 | n × m | `old[i][m-1-j]` | `new[i][m-1-j]` | 每列反過來 |
| 轉置 | m × n | `old[j][i]` | `new[j][i]` | 行列對調 |
| 順時針 90° | m × n | `old[n-1-j][i]` | `new[j][n-1-i]` | 左欄變上列 |
| 逆時針 90° | m × n | `old[j][m-1-i]` | `new[m-1-j][i]` | 右欄變上列 |
| 旋轉 180° | n × m | `old[n-1-i][m-1-j]` | `new[n-1-i][m-1-j]` | 上下＋左右 |

> **背不起來怎麼辦？** 拿一張 3 × 3 的紙寫上 1～9，實際轉一次，然後對照公式。自己推過一次，比死背有用十倍。真的記不住時，就**用迴圈版慢慢推**，至少寫得出來。

### 用「轉置 + 翻轉」理解旋轉

如果你已經會轉置與左右翻轉，旋轉可以這樣拆：

| 想要 | 做法 |
| --- | --- |
| 順時針 90° | 先**轉置**，再**左右翻轉** |
| 逆時針 90° | 先**轉置**，再**上下翻轉** |
| 180° | 先**上下翻轉**，再**左右翻轉** |

```python
def rotate_clockwise_by_steps(grid):
    t = transpose(grid)                     # 先轉置
    return [row[::-1] for row in t]         # 再左右翻轉

def rotate_counterclockwise_by_steps(grid):
    t = transpose(grid)                     # 先轉置
    return t[::-1]                          # 再上下翻轉
```

這裡的 `transpose` 用前面的切片版或 `transpose_loop` 都可以，結果完全相同。考試時選你記得住的那一種就好，**能跑對比寫得短重要**。

## 常見錯誤與除錯

### 錯誤 1：用 `[[0] * m] * n` 建立矩陣

前面提過，這會讓所有列共用同一個物件。**改成 `[[0] * m for _ in range(n)]`。**

### 錯誤 2：把「列數」和「欄數」搞反

```python
grid = [[1, 2, 3], [4, 5, 6]]
print(grid[0][1])   # 2（第 0 列第 1 欄）
print(grid[1][0])   # 4（第 1 列第 0 欄）
```

寫巢狀迴圈時，**外層一定是列、內層一定是欄**，`grid[i][j]` 的 `i` 對應外層、`j` 對應內層。

### 錯誤 3：`b = a` 以為是複製

```python
a = [[1, 2], [3, 4]]
b = a           # ❌ 只是別名，不是複製
b[0][0] = 99
print(a)        # [[99, 2], [3, 4]]  a 也被改了
```

要真正複製，用：

```python
b = [row[:] for row in a]   # ✅ 每一列都複製一份
```

### 錯誤 4：內層迴圈用錯長度

```python
for i in range(len(grid)):
    for j in range(len(grid)):      # ❌ 若是長方形矩陣，這裡會越界
        print(grid[i][j])
```

正確是 `range(len(grid[i]))`。**矩形矩陣**剛好不會出錯，但**不規則矩陣**一定爆。

### 錯誤 5：翻轉時把原矩陣改掉了

`grid[::-1]` 會回傳新串列，但 `grid.reverse()` 是**原地修改**。如果後面還要拿原始資料比對，請用切片版本，或先複製一份。

## 常見問題（FAQ）

### Q1：Python 的二維陣列跟 NumPy 的 array 差在哪？

Python 原生只有「串列嵌套串列」，速度快但功能陽春；NumPy 的 `ndarray` 支援向量化運算、矩陣乘法、轉置 `.T` 等，適合資料分析。**APCS 與大多數解題場合不能用 NumPy，請老老實實用串列。**

### Q2：為什麼 `[[0] * 3] * 3` 改一格會三格都變？

因為 `* 3` 重複的是「同一個串列的參考」，三列指向同一塊記憶體。改成 `[[0] * 3 for _ in range(3)]`，每一列都會重新建立，才是三個獨立物件。

### Q3：走訪二維陣列一定要用兩層迴圈嗎？

讀取資料時可以用 `for row in grid:` 一層迴圈搭配 `for value in row:`，或直接用 `sum(map(sum, grid))` 加總。但只要**需要索引**（找位置、改值、比較上下左右鄰居），就得用兩層 `range` 的巢狀迴圈。

### Q4：二維陣列裡可以放不同型別的資料嗎？

可以，Python 的串列不限制型別，`[[1, "a"], [True, 3.14]]` 是合法的。但解題時建議保持一致，才不會在比較或加總時噴 `TypeError`。

### Q5：旋轉一定要開一個新矩陣嗎？

不一定。方陣（n × n）可以「原地旋轉」，做法是先轉置再反轉每一列，空間複雜度 O(1)。但初學階段建議先開新矩陣，程式碼清楚、不容易寫錯，等熟悉了再研究原地版本。

### Q6：APCS 常考哪些二維陣列的題型？

常見的有：矩陣翻轉與旋轉、走訪加總與找最大值、上下左右鄰居判斷（走迷宮、踩地雷）、二維前綴和、以及把二維陣列當成「表格」排序。這篇講的存取與走訪是全部題型的基礎。

## 小結：二維陣列的學習路線

把這篇的四件事練熟，二維陣列就算入門了：

1. **宣告**：`[[0] * m for _ in range(n)]`，別用 `* n` 踩共用物件的雷
2. **存取**：`grid[列][欄]`，索引從 0 開始，負索引可用
3. **走訪**：外層列、內層欄，需要座標就用兩層 `range`
4. **翻轉與旋轉**：先畫 3 × 3 的表格推一次，再記索引公式

建議的練習順序：先自己把 3 × 3 矩陣印出來 → 試著上下翻轉 → 左右翻轉 → 轉置 → 順時針 90 度。每一種都自己從零寫一次，不要直接複製，手感才會留下來。

如果串列的基本操作還不熟，建議先看 [Python 字串與串列完整教學](https://vanix.github.io/2025/12/python-string-list-introduction.html)；迴圈還卡卡的話，先補 [Python 迴圈介紹](https://vanix.github.io/2025/12/python-loop-introduction.html)。都準備好了，就可以挑戰 [APCS 中級「特殊位置」](https://vanix.github.io/2026/10/apcs-k732-special-position.html)，那題就是二維陣列加上距離判斷的綜合應用。

---

還沒有基礎的同學，可以到[文章分類](https://vanix.github.io/categories/%E7%A8%8B%E5%BC%8F%E6%95%99%E5%AD%B8/)觀看教學文章與教學影片。寫完記得自己造幾組測資驗證，尤其是**不規則矩陣**與**非方形矩陣**的旋轉，這兩種最容易在邊界出錯。
