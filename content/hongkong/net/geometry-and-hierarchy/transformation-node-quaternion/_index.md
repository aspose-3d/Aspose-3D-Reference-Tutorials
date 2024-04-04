---
title: 透過四元數變換節點
linktitle: 透過四元數變換節點
second_title: Aspose.3D .NET API
description: 學習使用 Aspose.3D for .NET 使用四元數轉換 3D 節點。初學者的逐步指南。
type: docs
weight: 20
url: /zh-hant/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## 介紹

歡迎閱讀使用 Aspose.3D for .NET 在 3D 場景中以四元數轉換節點的逐步指南。在本教程中，我們將探索 Aspose.3D for .NET 的強大功能，並逐步完成使用四元數向 3D 節點新增轉換的過程。

## 先決條件

在我們深入學習本教程之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET：確保您已安裝 Aspose.3D 函式庫。您可以從[發布頁面](https://releases.aspose.com/3d/net/).

- 開發環境：使用必要的工具和組態設定 .NET 開發環境。

- 對 3D 概念的基本了解：熟悉 3D 圖形和概念將會有所幫助。

## 導入命名空間

在您的 .NET 專案中，包含 Aspose.3D 所需的命名空間：

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## 第 1 步：初始化場景對象

```csharp
// ExStart：透過四元數新增變換到節點
//初始化場景對象
Scene scene = new Scene();
```

## 第2步：初始化節點類別對象

```csharp
//初始化Node類別物件
Node cubeNode = new Node("cube");
```

## 第 3 步：使用 Polygon Builder 建立網格

```csharp
//呼叫 Common 類別使用多邊形生成器方法建立網格來設定網格實例
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## 第 4 步：將節點指向網格幾何體

```csharp
//將節點指向網格幾何體
cubeNode.Entity = mesh;
```

## 第 5 步：使用四元數設定旋轉

```csharp
//設定旋轉
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## 第6步：設定翻譯

```csharp
//設定翻譯
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## 步驟7：將立方體加入場景中

```csharp
//將立方體加入場景中
scene.RootNode.ChildNodes.Add(cubeNode);
```

## 第 8 步：儲存 3D 場景

```csharp
//文檔目錄的路徑。
var output = "Your Output Directory" + "TransformationToNode.fbx";

//以支援的檔案格式儲存 3D 場景
scene.Save(output, FileFormat.FBX7500ASCII);
//ExEnd：透過四元數添加變換到節點
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## 結論

恭喜！您已經成功學習如何使用 Aspose.3D for .NET 在 3D 場景中透過四元數轉換節點。參考以下內容探索更多功能和可能性[文件](https://reference.aspose.com/3d/net/).

## 常見問題解答

### Q1：3D圖形中的四元數是什麼？

A1：四元數是用來表示 3D 空間中的旋轉的數學實體。

### Q2：如何下載 Aspose.3D for .NET？

 A2：您可以從以下位置下載該庫：[發布頁面](https://releases.aspose.com/3d/net/).

### 問題 3：Aspose.3D for .NET 是否有免費試用版？

 A3：是的，您可以從以下位置獲得免費試用[這裡](https://releases.aspose.com/).

### 問題 4：在哪裡可以找到對 Aspose.3D for .NET 的支援？

 A4：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以尋求支持和討論。

### Q5：如何取得Aspose.3D的臨時授權？

 A5：獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).
