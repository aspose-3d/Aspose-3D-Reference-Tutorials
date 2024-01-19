---
title: 在 3D 場景中透過歐拉角變換節點
linktitle: 在 3D 場景中透過歐拉角變換節點
second_title: Aspose.3D .NET API
description: 學習使用 Aspose.3D for .NET 輕鬆轉換 3D 節點。請遵循我們的逐步指南，讓您的專案取得令人驚嘆的結果。
type: docs
weight: 19
url: /zh-hant/net/geometry-and-hierarchy/transformation-node-euler-angles/
---
## 介紹

歡迎來到這個關於使用 Aspose.3D for .NET 在 3D 場景中透過歐拉角變換節點的綜合教學。在本指南中，我們將深入研究令人興奮的 3D 圖形世界，並探索使用歐拉角向節點添加變換的過程。 Aspose.3D for .NET 提供了用於處理 3D 場景和網格的強大工具，使其成為尋求專案多功能性和效率的開發人員的絕佳選擇。

## 先決條件

在我們深入學習本教程之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET 函式庫：確保您已安裝 Aspose.3D 函式庫。你可以下載它[這裡](https://releases.aspose.com/3d/net/).

- 開發環境：設定您首選的 .NET 開發環境，例如 Visual Studio。

## 導入命名空間

首先匯入必要的命名空間以存取 Aspose.3D for .NET 提供的功能：

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

現在，讓我們將範例分解為多個步驟，以便清楚地理解。

## 第 1 步：初始化場景對象

```csharp
//ExStart:AddTransformationToNodeByEulerAngles
//初始化場景對象
Scene scene = new Scene();
```

首先使用建立一個新的 3D 場景`Scene`班級。

## 步驟2：初始化節點類別對象

```csharp
//初始化Node類別物件
Node cubeNode = new Node("cube");
```

使用以下命令在場景中建立一個節點`Node`班級。該節點將用作 3D 物件的容器。

## 第 3 步：使用多邊形生成器建立網格

```csharp
//呼叫 Common 類別使用多邊形生成器方法建立網格來設定網格實例
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 
```

呼叫一個方法（在本例中，`CreateMeshUsingPolygonBuilder`從一個習慣`Common`類別）來產生 3D 物件的網格。

## 第 4 步：將節點指向網格幾何體

```csharp
//將節點指向網格幾何體
cubeNode.Entity = mesh;
```

將建立的網格與節點關聯。

## 第 5 步：設定歐拉角和平移

```csharp
//歐拉角
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
//設定翻譯
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

定義節點的歐拉角和平移以定位在 3D 空間。

## 第 6 步：將立方體加入場景中

```csharp
//將立方體加入場景中
scene.RootNode.ChildNodes.Add(cubeNode);
```

將節點合併到場景的層次結構中。

## 第 7 步：儲存 3D 場景

```csharp
//文檔目錄的路徑。
var output = "Your Output Directory" + "TransformationToNode.fbx";

//以支援的檔案格式儲存 3D 場景
scene.Save(output, FileFormat.FBX7500ASCII);
//ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

指定輸出目錄並以所需的檔案格式（本例為 FBX7500ASCII）儲存 3D 場景，包括變換後的節點。

## 結論

恭喜！您已經成功學習如何使用 Aspose.3D for .NET 在 3D 場景中透過歐拉角變換節點。這個強大的函式庫為 3D 圖形開發打開了無限可能的大門。

## 常見問題解答

### Q1：Aspose.3D 與其他 3D 建模工具相容嗎？

A1：Aspose.3D支援各種3D檔案格式，增強了與流行建模工具的兼容性。

### Q2：我可以對單一節點套用多個轉換嗎？

A2：是的，您可以組合併套用多種變換來實現複雜的效果。

### Q3：在哪裡可以找到其他 Aspose.3D 文件？

 A3：請參閱[文件](https://reference.aspose.com/3d/net/)取得詳細資訊和範例。

### Q4：使用 Aspose.3D for .NET 需要授權嗎？

 A4：是的，您可以獲得許可證[這裡](https://purchase.aspose.com/buy)或探索一個[免費試用](https://releases.aspose.com/).

### Q5：需要幫助或有具體問題嗎？

A5：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持。