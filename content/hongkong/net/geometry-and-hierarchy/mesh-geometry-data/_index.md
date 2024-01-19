---
title: 在 3D 場景中使用網格幾何數據
linktitle: 在 3D 場景中使用網格幾何數據
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 掌握 3D 圖形程式設計的藝術。輕鬆建立、操作和保存令人驚嘆的 3D 場景。
type: docs
weight: 15
url: /zh-hant/net/geometry-and-hierarchy/mesh-geometry-data/
---
## 介紹

歡迎來到使用 Aspose.3D for .NET 進行 3D 圖形編程的令人興奮的世界！在本教程中，我們將使用 Aspose.3D（面向 .NET 開發人員的強大且多功能的程式庫）深入研究在 3D 場景中處理網格幾何資料的複雜性。無論您是經驗豐富的程式設計師還是剛開始接觸 3D 圖形，本逐步指南都將幫助您輕鬆掌握處理網格幾何資料的藝術。

## 先決條件

在我們開始 3D 之旅之前，請確保您具備以下先決條件：

- 具備 C# 和 .NET 程式設計的實用知識。
- Visual Studio 安裝在您的電腦上。
-  Aspose.3D for .NET 函式庫，您可以下載[這裡](https://releases.aspose.com/3d/net/).

現在您已準備就緒，讓我們進入 3D 圖形編程的迷人世界！

## 導入命名空間

在您的 C# 專案中，首先匯入必要的命名空間：

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
```

這些命名空間提供對處理 3D 場景和網格幾何資料所需的基本類別和方法的存取。

## 第 1 步：初始化場景

```csharp
//初始化場景對象
Scene scene = new Scene();
```

這將創建一個空白的 3D 場景，您可以在其中建立和操作 3D 模型。

## 第 2 步：定義顏色向量

```csharp
//定義顏色向量
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

指定將套用於 3D 場景的不同部分的顏色向量陣列。

## 第 3 步：建立網格並設定顏色

```csharp
//呼叫 Common 類別使用多邊形生成器方法建立網格來設定網格實例
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();

int idx = 0;
foreach (Vector3 color in colors)
{
    //初始化立方體節點對象
    Node cube = new Node("cube");
    cube.Entity = mesh;
    LambertMaterial mat = new LambertMaterial();
    
    //設定顏色
    mat.DiffuseColor = color;
    
    //套裝材質
    cube.Material = mat;
    
    //設定翻譯
    cube.Transform.Translation = new Vector3(idx++ * 20, 0, 0);
    
    //加入立方體節點
    scene.RootNode.ChildNodes.Add(cube);
}
```

使用多邊形生成器方法建立網格並將顏色應用於場景的不同部分。

## 第 4 步：儲存 3D 場景

```csharp
//文檔目錄的路徑。
var output = "Your Output Directory" + "MeshGeometryData.fbx";

//以支援的檔案格式儲存 3D 場景
scene.Save(output, FileFormat.FBX7400ASCII);
```

指定輸出目錄並以 FBX7400ASCII 檔案格式儲存 3D 場景。

## 結論

恭喜！您已經成功學習如何使用 Aspose.3D for .NET 在 3D 場景中處理網格幾何資料。本教學為您提供了建立和操作 3D 模型的基本步驟。實驗、探索並將您的 3D 圖形程式設計技能提升到新的高度！

## 常見問題解答

### Q1：我可以將 Aspose.3D for .NET 與其他程式語言一起使用嗎？

A1：Aspose.3D 主要是為.NET 設計的，但您可以探索支援不同平台和語言的其他 Aspose 產品。

### Q2：Aspose.3D 有免費試用版嗎？

A2：是的，您可以免費試用[這裡](https://releases.aspose.com/).

### 問題 3：我可以在哪裡找到更多支援和資源？

 A3：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持和討論。

### Q4：如何取得Aspose.3D的臨時授權？

 A4：您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).

### Q5：3D場景支援哪些文件格式？

 A5：Aspose.3D支援多種檔案格式，包括FBX、STL等。請參閱[文件](https://reference.aspose.com/3d/net/)以獲得完整清單。