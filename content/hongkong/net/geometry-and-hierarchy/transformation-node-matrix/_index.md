---
title: 在 3D 場景中透過變換矩陣變換節點
linktitle: 在 3D 場景中透過變換矩陣變換節點
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 在 3D 場景中輕鬆變換節點。透過教程學習分步節點轉換。
type: docs
weight: 21
url: /zh-hant/net/geometry-and-hierarchy/transformation-node-matrix/
---
## 介紹

在 3D 圖形和視覺化的動態領域中，操縱場景中的物件的能力是一個至關重要的方面。 Aspose.3D for .NET 使開發人員能夠使用變換矩陣無縫變換節點，為 3D 場景添加一層創造力和控制力。本教學將引導您逐步完成 3D 場景中節點的變換過程。

## 先決條件

在深入學習本教程之前，請確保您具備以下先決條件：

1.  Aspose.3D for .NET 函式庫：確保您的 .NET 專案中安裝了 Aspose.3D 函式庫。你可以下載它[這裡](https://releases.aspose.com/3d/net/).

2. 開發環境：設定一個工作的 .NET 開發環境，如果還沒有，請建立一個新項目，在其中實現轉換。

## 導入命名空間

首先將必要的命名空間匯入到您的 .NET 專案中。這些命名空間提供了 3D 場景操作的基本類別和方法。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

現在我們已經介紹了基礎知識，讓我們將轉換過程分解為逐步指南。

## 第1步：初始化場景和節點

```csharp
//ExStart：透過變換矩陣新增變換到節點
//初始化場景對象
Scene scene = new Scene();

//初始化Node類別物件
Node cubeNode = new Node("cube");
```

在此步驟中，我們建立一個新的 3D 場景以及該場景中名為「cube」的節點。

## 第 2 步：建立網格並設定幾何圖形

```csharp
//呼叫 Common 類別使用多邊形生成器方法建立網格來設定網格實例
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

//將節點指向網格幾何體
cubeNode.Entity = mesh;
```

在這裡，我們使用多邊形生成器方法來產生網格並將其分配給節點，從而為立方體建立幾何形狀。

## 第3步：設定自訂翻譯矩陣

```csharp
//設定自訂翻譯矩陣
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

定義自訂轉換矩陣以確定應用於節點的特定轉換。根據所需轉換的需要調整矩陣值。

## 第 4 步：將節點加入場景中

```csharp
//將立方體加入場景中
scene.RootNode.ChildNodes.Add(cubeNode);            
```

將立方體節點包含在場景中，使其成為整個 3D 環境的一部分。

## 第 5 步：儲存場景

```csharp
//文檔目錄的路徑。
var output = "Your Output Directory" + "TransformationToNode.fbx";

//以支援的檔案格式儲存 3D 場景
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd：透過變換矩陣加入變換到節點
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

指定輸出目錄和檔案名，然後以所需的檔案格式儲存 3D 場景。在此範例中，我們將其儲存為 FBX7500ASCII 格式。

## 結論

恭喜！您已使用 Aspose.3D for .NET 在 3D 場景中使用變換矩陣成功變換了節點。此功能為多樣化且視覺吸引力的 3D 應用程式打開了大門。

## 常見問題解答

### Q1：3D圖形中的變換矩陣是什麼？

A1：變換矩陣是一種數學表示，用於對 3D 空間中的物件應用各種變換（平移、旋轉、縮放）。

### Q2：我可以對單一節點套用多個轉換嗎？

A2：是的，您可以透過將各自的矩陣相乘並將結果應用到節點來組合多個變換。

### Q3：還有其他支援的檔案格式來保存 3D 場景嗎？

 A3：Aspose.3D for .NET 支援多種檔案格式，包括 STL、GLTF、OBJ 等。請參閱[文件](https://reference.aspose.com/3d/net/)以獲得完整的清單。

### Q4：如何取得 Aspose.3D for .NET 的臨時授權？

 A4：訪問[臨時許可證頁面](https://purchase.aspose.com/temporary-license/)在 Aspose 網站上取得用於評估目的的臨時許可證。

### Q5：我可以在哪裡尋求協助或與 Aspose.3D 社群聯繫？

A5：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)使用 Aspose.3D 提出問題、分享經驗並與其他開發人員聯繫。