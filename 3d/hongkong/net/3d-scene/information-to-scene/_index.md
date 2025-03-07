---
title: 將資訊提取到場景資產
linktitle: 將資訊提取到場景資產
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 輕鬆增強您的 3D 場景。學習逐步添加有價值的資產資訊。立即下載以獲得動態 3D 體驗。
weight: 10
url: /zh-hant/net/3d-scene/information-to-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 將資訊提取到場景資產

## 介紹

歡迎閱讀這個關於使用 Aspose.3D for .NET 提取有價值的資訊並增強 3D 場景的綜合教程。 Aspose.3D 是一個功能強大的程式庫，使開發人員能夠在 .NET 應用程式中無縫操作 3D 場景。在本教程中，我們將重點放在向場景中添加資產資訊的關鍵任務。

## 先決條件

在我們深入學習本教程之前，請確保您符合以下先決條件：

-  Aspose.3D for .NET：確保您已安裝該程式庫。您可以從[Aspose.3D for .NET 頁面](https://releases.aspose.com/3d/net/).

## 導入命名空間

在您的 .NET 專案中，請確保包含存取 Aspose.3D 功能所需的命名空間：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 第 1 步：初始化 3D 場景

```csharp
Scene scene = new Scene();
```

使用建立一個新的 3D 場景`Scene`班級。

## 第 2 步：設定應用程式和供應商信息

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

定義與您的 3D 場景關聯的應用程式和供應商名稱。

## 步驟 3：定義測量單位

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

指定場景中使用的測量單位。在此範例中，我們使用稱為「桿」的古埃及單位，1 桿等於 60 公分。

## 第 4 步：儲存場景

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

將新增了資產資訊的場景儲存為 3D 支援的文件格式。根據需要調整輸出目錄。

## 步驟5：顯示成功訊息

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

通知用戶資產資訊已成功添加，並保存文件。

## 結論

恭喜！您已成功學習如何使用 Aspose.3D for .NET 提取基本資產資訊並將其新增至 3D 情境中。這些知識為創造資訊豐富、引人入勝的 3D 內容開闢了無限的可能性。

## 常見問題解答

### Q1：我可以將 Aspose.3D for .NET 與其他程式語言一起使用嗎？

A1：Aspose.3D 主要支援 .NET 語言，但您可以探索其他語言的互通性選項。

### 問題 2：Aspose.3D for .NET 是否有免費試用版？

A2：是的，您可以免費試用[這裡](https://releases.aspose.com/).

### Q3：如何獲得 Aspose.3D 相關查詢的支援？

 A3：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區和支持。

### Q4：我可以購買 Aspose.3D for .NET 的臨時授權嗎？

 A4：是的，您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).

### Q5：在哪裡可以找到 Aspose.3D for .NET 的詳細文件？

 A5：請參閱[文件](https://reference.aspose.com/3d/net/)以獲得深入的資訊。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
