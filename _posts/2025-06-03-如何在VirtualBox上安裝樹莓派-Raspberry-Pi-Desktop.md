---
author: 歐巴計概
date: 2025-06-03 08:31:00.003000+00:00
layout: post
permalink: /2025/06/virtualboxraspberry-pi-desktop.html
title: 如何在VirtualBox上安裝樹莓派 Raspberry Pi Desktop
description: "在 VirtualBox 虛擬機上安裝 Raspberry Pi Desktop 的教學：下載來源、建立虛擬機、掛載 ISO、安裝流程與 Guest Additions 設定。"
categories: [資訊教學,軟體工具]
tags: [VirtualBox, Raspberry Pi, 樹莓派, 系統安裝, 教學筆記, 虛擬機]
---
💡 VirtualBox 安裝樹莓派桌面重點

這篇教學示範如何在 Windows/Mac 的 VirtualBox 虛擬機器上安裝 Raspberry Pi Desktop，讓沒有樹莓派實機的人也能練習 Linux 環境。


<iframe width="560" height="315"
        src="https://www.youtube.com/embed/SBbgGC4ybYc"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>

Hello 大家好！歡迎回到資訊小教室！今天我們將介紹虛擬機器的應用：

如何在VirtualBox上安裝Raspberry Pi Desktop！通常，我們習慣在虛擬機器中運行Windows或Linux系統，但這次，我們將帶您進一步。我們將逐步指導您如何使用VirtualBox來安裝這個有趣的系統。（安裝指令可參閱影片內容）

## 安裝步驟：

1. 首先，[下載](https://www.virtualbox.org/wiki/Download_Old_Builds_6_1)並安裝X64版本的VirtualBox。

2. 前往樹莓派官網[下載](https://www.raspberrypi.com/software/raspberry-pi-desktop/)Raspberry Pi Desktop的映像檔。

3. 使用VirtualBox將下載的ISO檔案安裝到虛擬機器中。

這一步比較繁瑣，但不需擔心，我們將一步一步來。首先，創建一個新的虛擬機器，為它命名（名稱可隨意），然後選擇Linux系統的Debian 32位版本。

調整記憶體分配建議設置為2GB以上，並選擇固定大小的硬碟。讓我們將硬碟大小設為15GB到20GB之間。

## 設置虛擬機器：

建立虛擬機器後，我們將設定虛擬光碟機，並掛載下載的Raspberry Pi ISO檔案。開機後虛擬機會從這個“光碟片”啟動，進入安裝界面。

在安裝過程中，選擇Chinese鍵盤佈局，然後按照系統建議進行硬碟分割。完成後，系統將開始安裝，並設置開機選單與其他初始選項。

## 後續設置：Guest Additions[下載](https://download.virtualbox.org/virtualbox/6.1.50/)及安裝

系統啟動後，進一步設置將包括調整解析度和建立共享資料夾與剪貼簿。這些設置會大大提升虛擬機器的使用便捷性。

最終設置成功後，您可以探索虛擬機器下的Raspberry Pi系統，測試其功能並體驗多系統運作的便利性。

裝有Raspberry Pi Desktop的虛擬機器，讓您在不擁有物理樹莓派硬體的情況下，也能體驗Linux系統與相關樹莓派專案。

---

## 常見問題（FAQ）

### Raspberry Pi Desktop 可以用虛擬機跑嗎？

可以。在 VirtualBox 下載 ISO 後以虛擬光碟機開機安裝；VirtualBox 要用 6.1 等 X64 版本，虛擬機作業系統型別選 Linux 的 Debian 32-bit。

### 虛擬機資源要配多少？

記憶體建議 2GB 以上，硬碟選固定大小、設 15GB 到 20GB 之間。

### 裝好系統後還要做什麼？

安裝 VirtualBox Guest Additions，可提升顯示解析度，並建立共享資料夾與剪貼簿更方便使用。
