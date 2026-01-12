---
date: 2026-01-12
description: 學習如何使用 Aspose.3D for .NET 為 3D 場景新增中繼資料，包括如何新增供應商資訊以及匯出 3D 模型檔案。
linktitle: 'How to Add Metadata: Extracting Information to Scene Assets'
second_title: Aspose.3D .NET API
title: 如何添加元資料：將資訊提取至場景資產
url: /zh-hant/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何新增中繼資料：將資訊提取至場景資產

## 介紹

在本完整教學中，您將了解 **如何新增中繼資料** 到您的 3D 場景，使用 Aspose.3D for .NET。新增如供應商資訊、自訂測量單位以及其他資產資訊的中繼資料，可讓您的模型更具資訊性、可搜尋，並可直接用於遊戲引擎或 AR/VR 平台等下游管線。

## 快速解答
- **主要目的為何？** 將中繼資料（供應商資訊、單位、自訂標籤）直接嵌入 3D 場景中。  
- **使用哪個函式庫？** Aspose.3D for .NET。  
- **新增中繼資料後，我可以匯出模型嗎？** 是 – 您可以 **匯出 3D 模型** 檔案，例如另存為 FBX。  
- **我需要授權嗎？** 提供免費試用版；正式環境需購買商業授權。  
- **支援哪些 .NET 版本？** .NET Framework 4.5 以上、.NET Core 3.1 以上、.NET 5/6。

## 什麼是 3D 場景中的「如何新增中繼資料」？

新增中繼資料指的是將描述性資訊（例如應用程式名稱、供應商、測量單位或自訂標籤）附加於場景檔案本身。當您 **將場景另存為 FBX** 或其他支援格式時，這些資料會隨模型一起傳遞，使下游工具能在沒有外部檔案的情況下了解其背景。

## 為何要嵌入自訂中繼資料與供應商資訊？

- **可搜尋性：** 資產管理系統可依供應商或單位類型篩選模型。  
- **互通性：** 讀取 FBX 的引擎若您 **定義測量單位**，即可自動套用正確的比例。  
- **品牌化：** 加入應用程式名稱與供應商資訊，可加強所有權與授權合規性。  

## 前置條件

在開始之前，請確保您已具備以下條件：

- 已安裝 Aspose.3D for .NET。您可從 [Aspose.3D for .NET page](https://releases.aspose.com/3d/net/) 下載。

## 匯入命名空間

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 步驟 1：初始化 3D 場景

```csharp
Scene scene = new Scene();
```

建立一個全新的 `Scene` 物件，用於保存所有幾何與資產資訊。

## 步驟 2：設定應用程式與 **新增供應商資訊**

在此我們嵌入 **應用程式名稱** 與 **供應商資訊**。這是 **如何新增中繼資料** 的核心部分，用以識別模型的來源。

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

## 步驟 3：**定義測量單位** 以確保精確縮放

透過指定 `UnitName` 與 `UnitScaleFactor`，您告訴下游工具一個「pole」等於 0.6 公尺（60 cm）。此步驟在您之後 **匯出 3D 模型** 檔案時，確保實際尺寸正確，至關重要。

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

## 步驟 4：**將場景另存為 FBX** – **匯出 3D 模型** 並附帶中繼資料

`Save` 呼叫會將場景寫入 FBX 檔案，並嵌入我們先前新增的所有中繼資料。此示範了 **如何新增中繼資料**，接著 **將場景另存為 FBX**，有效 **匯出 3D 模型**，並攜帶完整資產資訊。

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## 步驟 5：顯示成功訊息

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

友善的主控台訊息會確認中繼資料已寫入，並顯示檔案位置。

## 常見問題與技巧

- **單位比例不正確：** 請再次確認 `UnitScaleFactor` 與實際換算相符；否則匯出的模型可能會過大或過小。  
- **缺少供應商資訊：** 若 `ApplicationVendor` 為空，部分檢視器會顯示「Unknown」。盡可能務必設定。  
- **檔案路徑錯誤：** 請確保輸出目錄已存在；否則 `scene.Save` 會拋出例外。

## 常見問答

### Q1：我可以將 Aspose.3D for .NET 與其他程式語言一起使用嗎？

A1：Aspose.3D 主要支援 .NET 語言，但您可探索與其他語言的互通選項。

### Q2：是否提供 Aspose.3D for .NET 的免費試用？

A2：是的，您可在此取得免費試用版 [here](https://releases.aspose.com/)。

### Q3：如何取得 Aspose.3D 相關問題的支援？

A3：請前往 [Aspose.3D forum](https://forum.aspose.com/c/3d/18) 取得社群與支援。

### Q4：我可以購買 Aspose.3D for .NET 的臨時授權嗎？

A4：是的，您可在此取得臨時授權 [here](https://purchase.aspose.com/temporary-license/)。

### Q5：在哪裡可以找到 Aspose.3D for .NET 的詳細文件？

A5：請參考 [documentation](https://reference.aspose.com/3d/net/) 以取得深入資訊。

## 結論

您現在已掌握使用 Aspose.3D for .NET 為 3D 場景 **新增中繼資料** 的技巧——設定應用程式與供應商資訊、**定義測量單位**，最後 **將場景另存為 FBX** 以 **匯出 3D 模型** 檔案，將所有寶貴資訊一併攜帶。運用這些方法，讓您的資產更豐富、可搜尋，並可隨時投入任何下游工作流程。

---

**最後更新：** 2026-01-12  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}