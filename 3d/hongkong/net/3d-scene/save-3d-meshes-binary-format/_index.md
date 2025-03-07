---
title: 以自訂二進位格式儲存 3D 網格
linktitle: 以自訂二進位格式儲存 3D 網格
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 世界。了解以自訂二進位格式儲存網格。
weight: 13
url: /zh-hant/net/3d-scene/save-3d-meshes-binary-format/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 以自訂二進位格式儲存 3D 網格

## 介紹

歡迎來到 Aspose.3D for .NET 的世界，這是一個功能強大的程式庫，使開發人員能夠輕鬆處理 3D 檔案。在本教程中，我們將深入研究使用 Aspose.3D for .NET 以自訂二進位格式儲存 3D 網格的過程。本指南假設您對 C# 有基本了解並熟悉 Aspose.3D 函式庫。

## 先決條件

在我們開始學習本教學之前，請確保您已準備好以下內容：

-  Aspose.3D for .NET：確保您已安裝 Aspose.3D 函式庫。您可以從以下位置下載：[這裡](https://releases.aspose.com/3d/net/).

- 開發環境：設定您首選的 C# 開發環境，例如 Visual Studio。

- 輸入 3D 檔案：有一個要轉換為自訂二進位格式的 3D 檔案（例如 test.fbx）。

## 導入命名空間

在您的 C# 程式碼中，包含存取 Aspose.3D 功能所需的命名空間：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## 第 1 步：載入 3D 文件

使用 Aspose.3D 載入 3D 檔案。在此範例中，我們載入一個名為「test.fbx」的檔案：

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## 第 2 步：定義自訂二進位格式

定義要儲存 3D 網格的自訂二進位格式的結構。此範例使用以 MeshBlock、Vertex 和 Triangle 作為元件的結構。

```csharp
//頂點的記憶體佈局是
//浮動[3]位置；
//浮動[3]正常；
//浮動[3]紫外線；
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## 第三步：開啟檔案進行寫入

開啟一個用於寫入的二進位文件，其中將保存轉換後的 3D 網格：

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## 第 4 步：迭代節點與實體

存取 3D 場景中的每個節點並將網格實體轉換為自訂二進位格式。忽略燈光、攝影機和其他非網格實體：

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ……（繼續處理）
    }
    return true;
});
```

## 第 5 步：轉換並寫入控制點和三角形

對於每個網格實體，將控制點轉換為世界空間並將它們與三角形索引一起寫入二進位檔案：

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//網格的記憶體佈局是：
//浮動[16]變換矩陣；
// int vertices_count；
// int 索引計數；
//頂點[vertices_count]個頂點；
// ushort[indices_count] 索引；


//寫變換
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//寫入頂點/索引的數量
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//寫入頂點和索引
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## 結論

在本教程中，我們介紹了使用 Aspose.3D for .NET 以自訂二進位格式儲存 3D 網格的過程。這個強大的程式庫為開發人員提供了無縫操作 3D 檔案所需的工具。嘗試不同的格式和設置，以釋放 Aspose.3D 在您的專案中的全部潛力。

## 常見問題解答

### Q1：我可以將 Aspose.3D for .NET 與其他程式語言一起使用嗎？

A1：Aspose.3D 主要支援 .NET 語言，但您可以探索其他語言的兼容性選項。

### Q2：在哪裡可以找到更多範例和資源？

 A2: 的[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)是尋找支持、範例以及與社區互動的好地方。

### Q3：Aspose.3D 有試用版嗎？

 A3：是的，您可以從以下位置獲得免費試用[這裡](https://releases.aspose.com/).

### Q4：如何取得Aspose.3D的臨時授權？

 A4：參觀[這個連結](https://purchase.aspose.com/temporary-license/)取得用於測試目的的臨時許可證。

### Q5：我可以購買 Aspose.3D for .NET 嗎？

 A5：是的，您可以從[購買頁面](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
