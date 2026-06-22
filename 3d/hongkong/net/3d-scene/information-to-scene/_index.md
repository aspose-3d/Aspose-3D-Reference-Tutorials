---
date: 2026-03-26
description: 學習如何在 3D 場景中加入供應商資訊，以及如何使用 Aspose.3D for .NET 儲存 FBX 檔案。請跟隨此一步一步的教學，內含可直接執行的程式碼。
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: 如何使用 Aspose.3D 添加供應商資訊並儲存 FBX 場景
url: /zh-hant/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D 中加入供應商資訊並儲存 FBX 場景

## 介紹

歡迎閱讀本完整教學，說明 **如何加入供應商** 資訊至 3D 場景，並 **如何使用 Aspose.3D for .NET 儲存 FBX** 檔案。無論您是製作建築視覺化、遊戲資產或工程模型，將供應商與應用程式的中繼資料嵌入場景，都能讓您的檔案更具資訊性，且在後續管理時更為便利。讓我們一步一步完成整個流程。

## 快速解答
- **「加入供應商」是什麼意思？** 它會將應用程式與供應商名稱儲存在場景的 `AssetInfo` 區塊內。  
- **哪種格式支援供應商資訊？** FBX（ASCII 或 binary）在儲存時會保留此中繼資料。  
- **如何儲存 FBX？** 使用 `scene.Save(path, FileFormat.FBX7500ASCII)` 或相對應的 binary 版本。  
- **需要授權嗎？** 開發階段可使用免費試用版；正式上線則需購買商業授權。  
- **可以變更測量單位嗎？** 可以，設定 `AssetInfo.UnitName` 與 `AssetInfo.UnitScaleFactor` 即可。

## 什麼是 3D 場景中的「加入供應商」？
加入供應商資訊即是為 `Scene` 物件的 `AssetInfo` 屬性填入相關資料。這些屬性會隨檔案一起寫入，讓任何讀取 FBX 的使用者都能看到是由哪個應用程式與哪個供應商產生的。

## 為什麼要加入供應商資訊？
- **可追溯性：** 在大型製作流程中快速辨識模型來源。  
- **合規性：** 某些產業需要明確的供應商標記以便資產管理。  
- **自動化：** 腳本可依供應商中繼資料過濾或處理檔案。

## 前置條件

- 已安裝 Aspose.3D for .NET。可從 [Aspose.3D for .NET 頁面](https://releases.aspose.com/3d/net/) 下載。

## 匯入命名空間

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 如何加入供應商資訊

### 步驟 1：初始化 3D 場景

```csharp
Scene scene = new Scene();
```

建立全新的 `Scene`，即可得到一個乾淨的畫布供後續操作。

### 步驟 2：設定應用程式與供應商資訊

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

此範例示範 **如何加入供應商** 資料，透過為 `ApplicationName` 與 `ApplicationVendor` 指定具意義的字串來完成。

### 步驟 3：定義測量單位

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

指定單位系統可確保任何開啟 FBX 檔案的人，都能正確解讀尺寸。此例中，一「桿」等於 60 cm。

## 如何儲存 FBX 場景

### 步驟 4：儲存場景（how to save fbx）

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

此行程式碼示範 **如何儲存 fbx**，使用 FBX 7.5.0 的 ASCII 版。如需 binary 版，請將 `FBX7500ASCII` 改為 `FBX7500Binary`。

> **小技巧：** 請確保檔案副檔名 `.fbx` 與所選格式相符，否則部分檢視器可能會誤判內容。

### 步驟 5：顯示成功訊息

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

在主控台顯示友善訊息，確認已將包含供應商中繼資料的場景寫入磁碟。

## 常見問題與解決方案

| 問題 | 解決方案 |
|-------|----------|
| **檢視器中未顯示供應商資訊** | 確認已以 **FBX ASCII** 或 **Binary** 格式儲存；部分舊版檢視器僅支援其中一種。 |
| **路徑包含空格** | 將路徑加上引號，或使用 `Path.Combine` 產生安全的檔案路徑。 |
| **單位比例顯示異常** | 再次檢查 `UnitScaleFactor`；它是相對於公尺的乘數。 |
| **授權例外** | 測試時可使用免費試用版；正式產品請取得完整授權。 |

## 常見問答

**Q: 可以在其他程式語言中使用 Aspose.3D for .NET 嗎？**  
A: Aspose.3D 主要支援 .NET 語言，但您可探索與其他語言的互操作性方案。

**Q: Aspose.3D for .NET 有提供免費試用嗎？**  
A: 有，請點擊[此處](https://releases.aspose.com/)取得免費試用。

**Q: 如何取得 Aspose.3D 相關支援？**  
A: 前往 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)取得社群與技術支援。

**Q: 可以購買臨時授權嗎？**  
A: 可以，請至[此處](https://purchase.aspose.com/temporary-license/)取得臨時授權。

**Q: 哪裡可以找到 Aspose.3D for .NET 的詳細文件？**  
A: 請參考[文件說明](https://reference.aspose.com/3d/net/)以取得深入資訊。

---

**最後更新：** 2026-03-26  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}