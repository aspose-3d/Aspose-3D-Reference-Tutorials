---
title: 定制偏置頂缸
linktitle: 定制偏置頂缸
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 圖形的奇蹟。學習輕鬆創建定制的偏置頂部氣缸。立即提升您的程式設計體驗！
type: docs
weight: 11
url: /zh-hant/net/working-with-cylinder/customized-offset-top-cylinder/
---
## 介紹
歡迎來到 Aspose.3D for .NET 的 3D 圖形操作世界！在本教程中，我們將指導您完成使用Aspose.3D 建立自訂偏移頂部圓柱體的過程，Aspose.3D 是一個功能強大的庫，用於在.NET 應用程式中處理3D 場景、物件和格式。
## 先決條件
在我們深入學習本教程之前，請確保您具備以下先決條件：
- C# 程式語言的基礎知識。
- Visual Studio 安裝在您的電腦上。
- 下載 Aspose.3D for .NET 函式庫並在您的專案中引用。
現在，讓我們開始逐步指南！
## 導入命名空間
首先，確保在 C# 程式碼中匯入必要的命名空間：
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## 第 1 步：建立場景
```csharp
//創建場景
Scene scene = new Scene();
```
這將使用 Aspose.3D 初始化一個新的 3D 場景。
## 第 2 步：初始化氣缸
```csharp
//初始化氣缸
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
在這裡，我們建立一個具有特定參數（例如半徑、高度和切片）的圓柱體。
## 步驟 3：設定第一個圓柱體的 OffsetTop
```csharp
//設定頂部偏移
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
這為第一個氣缸設定了定制的偏移頂部。
## 步驟 4：為第一個圓柱體建立 ChildNode
```csharp
//建立子節點
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
我們將第一個圓柱體作為子節點加入到場景中，並調整其位置。
## 第 5 步：初始化第二個圓柱體
```csharp
//初始化第二個圓柱體，無需自訂OffsetTop
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
第二個氣缸在沒有定制偏移頂部的情況下初始化。
## 步驟6：為第二個圓柱體建立ChildNode
```csharp
//建立子節點
scene.RootNode.CreateChildNode(cylinder2);
```
我們將第二個圓柱體作為子節點加入場景。
## 第7步：儲存場景
```csharp
//節省
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
這會以 Wavefront OBJ 格式儲存 3D 場景，包括自訂的偏移頂部圓柱體。
現在您已經使用 Aspose.3D for .NET 成功建立了自訂的偏移頂部圓柱體！
## 結論
在本教程中，我們探索了使用 Aspose.3D for .NET 建立自訂偏移頂部圓柱體的基礎知識。該程式庫為 .NET 應用程式中的 3D 圖形操作開啟了無限的可能性。
## 常見問題解答
### Q：在哪裡可以找到 Aspose.3D for .NET 的文檔？
答：文檔已提供[這裡](https://reference.aspose.com/3d/net/).
### Q：如何下載 Aspose.3D for .NET？
答： 你可以下載[這裡](https://releases.aspose.com/3d/net/).
### Q：Aspose.3D for .NET 是否有免費試用版？
答：是的，您可以免費試用[這裡](https://releases.aspose.com/).
### Q：在哪裡可以獲得 Aspose.3D for .NET 支援？
答：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)為了支持。
### Q：我可以取得 Aspose.3D for .NET 的臨時授權嗎？
答： 是的，您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).