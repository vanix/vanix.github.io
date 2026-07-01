---
author: 歐巴計概
date: 2026-07-01 00:07:59 +0000
layout: post
permalink: /2026/07/apcs_basic_level_review.html
title: APCS初級實作 - Python考前複習及注意事項

categories: [教學, 程式教學]
tags: [Python, 程式設計, 入門教學, 程式課程, APCS基礎, 實作初級]
---

以下內容以複習迴圈跟串列(倉庫)為主

### 1. 根據迴圈執行次數，決定迴圈如何運作

以[文文的求婚迴圈題目](http://163.30.43.15/ShowProblem?problemid=a025)來看，輸入資料為

```
4
1991
1992
1993
1994
```

你可以根據第一筆輸入，得知迴圈執行次數
接著便可以在迴圈裡面取得其他資料，並且判斷是否為閏年
程式範例如下

```python
n=int(input())

for i in range(n):
  year=int(input())
  if 是否為閏年:
    print("閏年")
  else:
    print("平年")
```

### 2. 使用迴圈掃描倉庫裡的所有資訊，並記錄需要的資訊

以[電腦教室題目](http://163.30.43.15/ShowProblem?problemid=a030)來看，輸入資料為

```
5
42 39 41 43 30
```

你可以根據第一筆資料得知倉庫裡面有幾個箱子
接著便可以使用迴圈，去檢查倉庫裡的每一個箱子，找出誰是最大值
程式範例如下

```python
n=int(input())
c=list(map(int,input().split()))
max=0

for i in range(n):
  if max<n[i]:
    max=n[i]

print(max)
```

以上可以學會三個基礎
- 根據輸入資料決定迴圈要執行幾次
- 使用迴圈依序取得倉庫資料
- 自行準備額外的箱子，記錄題目所需要的資訊

### 3. 倉庫有哪些內建功能可以使用

#### 3-1. 把輸入資料變成倉庫

```python
s=input().split()
n=list(map(int,s))
```
s為文字倉庫
n為整數倉庫


#### 3-2. 需要自行建立倉庫，並且附加資料

```python
n=[]
n.append("巧虎")
n.append("桃樂比")
```
如有很多資料要加入，也可使用迴圈協助加入資料

#### 3-3. 排序倉庫，把資料從小排到大

假設n已經是一個整數倉庫

```python
從小排到大
n.sort()
排序後反轉
n.reverse()
```

#### 3-4. 常用倉庫內建指令，以及內建函數

假設n已經是一個整數倉庫

```python
取得倉庫箱子數量
len(n)

取得倉庫裡的最大值
max(n)

取得倉庫裡的最小值
min(n)

加總倉庫裡面的所有數字
sum(n)

算出某個資料的數量
n.count(資料)

找出某個資料的位置
n.index(資料)

刪除特定資料，刪除最後一筆資料
n.remove(資料)
n.pop()
```

某些題目或許不用迴圈，直接使用既有的指令或函數就可以完成
以剛剛的[電腦教室題目](http://163.30.43.15/ShowProblem?problemid=a030)為例

```python
n=int(input())
c=list(map(int,input().split()))
print(max(n))
```
#### 3-5. 倉庫與迴圈的結合

假設n是一個倉庫，下述程式碼可以把倉庫裡面的資料依序印出來

```python
for i in n:
  print(i)
```

### 溫馨小提醒

應考APCS初級實作前，記得要刷[APCS考古題的第一題](https://sites.google.com/view/vanix-python-basic/apcs%E5%AF%A6%E4%BD%9C%E9%A1%8C)
也記得去看一下考前注意事項、跟作答系統說明

<iframe width="560" height="315"
        src="https://www.youtube.com/embed/sBNnrgcEqtc"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

<iframe width="560" height="315"
        src="https://www.youtube.com/embed/1F33cc92RiU"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

還沒有基礎的同學，可以到[文章分類](https://vanix.github.io/categories/%E7%A8%8B%E5%BC%8F%E6%95%99%E5%AD%B8/)裡觀看教學文章跟教學影片

也可以到以下平台進行實作練習
- 練習平台：[點此前往解題系統](http://163.30.43.15/){:target="_blank"}
- 課程代碼：SzNTKb
- 練習目標：完成「YouTube 線上課程」裡面所有作業
