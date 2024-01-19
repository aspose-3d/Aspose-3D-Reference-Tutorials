---
title: 將球體基元轉換為網格
linktitle: 將球體基元轉換為網格
second_title: Aspose.3D .NET API
description: 探索 Aspose.3D for .NET，並透過自訂記憶體佈局輕鬆將球體網格轉換為三角形網格。請按照我們的逐步指南進行無縫整合。
type: docs
weight: 16
url: /zh-hant/net/objects/convert-sphere-primitive-to-mesh/
---
## 介紹
您是否希望利用 Aspose.3D for .NET 的強大功能將球體網格轉換為具有自訂記憶體佈局的三角形網格？本逐步指南將引導您完成整個過程，即使是初學者也可以輕鬆遵循。學完本教學後，您將充分了解如何使用 Aspose.3D for .NET 來實現此目的。
## 先決條件
在深入學習本教程之前，請確保您具備以下先決條件：
- .NET 程式設計的基礎知識。
- 安裝了 Aspose.3D for .NET 函式庫。您可以從[Aspose.3D for .NET 下載頁面](https://releases.aspose.com/3d/net/).
- 熟悉 C# 程式語言。
## 導入命名空間
在您的 C# 專案中，請確保匯入必要的命名空間以利用 Aspose.3D 功能：
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## 第 1 步：初始化場景對象
```csharp
//初始化場景對象
Scene scene = new Scene();
```
## 步驟2：初始化節點類別對象
```csharp
//初始化Node類別物件
Node cubeNode = new Node("sphere");
```
## 步驟 3：將球體網格轉換為類型化 TriMesh
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## 步驟4：取得自訂結構中的頂點數據
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## 第 5 步：取得 32 位元和 16 位元索引
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## 步驟6：將頂點和索引資料寫入記憶體流
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## 第 7 步：將節點指向網格幾何體
```csharp
cubeNode.Entity = sphere;
```
## 步驟8：將節點加入場景中
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## 第 9 步：儲存 3D 場景
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## 第10步：顯示結果
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## MyVertex 範例原始程式碼
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## 結論
恭喜！您已使用 Aspose.3D for .NET 成功將球體網格轉換為具有自訂記憶體佈局的三角形網格。這個功能強大的程式庫提供了一種在 .NET 應用程式中操作 3D 物件的無縫方法。
## 常見問題解答
### Q：我可以將 Aspose.3D for .NET 與其他 .NET 框架一起使用嗎？
答：是的，Aspose.3D for .NET 與各種 .NET 框架相容。
### Q：在哪裡可以找到 Aspose.3D for .NET 的詳細文件？
答：請參閱[Aspose.3D for .NET 文檔](https://reference.aspose.com/3d/net/)以獲得深入的資訊。
### Q：如何取得 Aspose.3D for .NET 的臨時授權？
答：訪問[這個連結](https://purchase.aspose.com/temporary-license/)獲得臨時許可證。
### Q：是否有適用於 Aspose.3D for .NET 的範例專案？
答：探索 Aspose.3D for .NET 文件並[GitHub 儲存庫](https://github.com/aspose-3d/Aspose.3D-for-.NET)對於範例項目。
### Q：是否有針對 .NET 支援的 Aspose.3D 的活躍社群？
答：是的，加入[Aspose.3D for .NET 論壇](https://forum.aspose.com/c/3d/18)獲得社區的協助。