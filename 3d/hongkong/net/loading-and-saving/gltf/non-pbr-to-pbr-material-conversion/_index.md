---
title: 非 PBR 到 PBR 材質轉換
linktitle: 非 PBR 到 PBR 材質轉換
second_title: Aspose.3D .NET API
description: 探索 Aspose.3D for .NET - 輕鬆將非 PBR 材質轉換為 PBR 材質。全面的教程和強大的 API。
type: docs
weight: 16
url: /zh-hant/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## 介紹

歡迎閱讀本逐步指南，了解如何使用 Aspose.3D for .NET 將非 PBR（基於實體的渲染）轉換為 PBR 材質。 Aspose.3D 是一個功能強大的 API，允許開發人員在其 .NET 應用程式中無縫使用 3D 檔案格式。

## 先決條件

在我們深入學習本教程之前，請確保您符合以下先決條件：

-  Aspose.3D for .NET：確保您已安裝 Aspose.3D for .NET 程式庫。你可以找到下載鏈接[這裡](https://releases.aspose.com/3d/net/).

- C# 的基本了解：本教學假設您對 C# 程式設計有基本的了解。

- IDE（整合開發環境）：選擇您首選的 .NET 開發 IDE，例如 Visual Studio。

## 導入命名空間

在 C# 程式碼中，首先匯入必要的命名空間：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 第 1 步：初始化新的 3D 場景

首先使用以下程式碼建立一個新的 3D 場景：

```csharp
// ExStart:Non_PBRtoPBRMaterial
//初始化一個新的 3D 場景
var scene = new Scene();
```

## 第 2 步：建立 3D 對象

接下來，建立一個 3D 對象，例如一個盒子：

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## 步驟 3：配置材質轉換

設定非 PBR 到 PBR 轉換的材質轉換選項：

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## 步驟 4：儲存為 GLTF 2.0 格式

將轉換後的場景儲存為 GLTF 2.0 格式：

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

根據您的特定用例的需要重複這些步驟，確保每個細節都配置正確。

## 結論

恭喜！您已成功學習如何使用 Aspose.3D for .NET 將非 PBR 材質轉換為 PBR 材質。這個強大的工具為 .NET 應用程式中的 3D 圖形操作開啟了無限的可能性。

## 常見問題解答

### Q1：Aspose.3D 是否相容於所有 3D 檔案格式？

A1：是的，Aspose.3D 支援多種 3D 檔案格式，為您的專案提供靈活性。

### Q2：我可以將Aspose.3D用於商業應用嗎？

 A2：當然！ Aspose.3D是商業產品，您可以購買[這裡](https://purchase.aspose.com/buy).

### Q3：測試需要臨時許可證嗎？

 A3：是的，您可以獲得臨時許可證用於測試目的[這裡](https://purchase.aspose.com/temporary-license/).

### Q4：哪裡可以找到對 Aspose.3D 的支援？

 A4：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持和討論。

### Q5: 有免費試用嗎？

A5：是的，您可以探索免費試用版[這裡](https://releases.aspose.com/).