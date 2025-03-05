---
title: 依材質分割場景的所有網格
linktitle: 依材質分割場景的所有網格
second_title: Aspose.3D .NET API
description: 了解如何使用 Aspose.3D for .NET 依材質分割 3D 網格。按照我們的逐步指南高效組織和管理 3D 模型。
type: docs
weight: 21
url: /zh-hant/net/meshes/split-all-meshes-by-material/
---
## 介紹
歡迎閱讀本逐步指南，以了解如何使用 Aspose.3D for .NET 依材質分割 3D 場景的所有網格。如果您正在使用 3D 模型並希望根據材質有效地組織網格，那麼本教學適合您。 Aspose.3D 是一個功能強大的 .NET 程式庫，提供了一系列用於處理 3D 檔案的功能，使其成為開發人員的絕佳選擇。
## 先決條件
在深入學習本教程之前，請確保您符合以下先決條件：
- 對 C# 程式語言有基本了解。
- Visual Studio 安裝在您的電腦上。
-  Aspose.3D for .NET 函式庫。您可以從以下位置下載：[這裡](https://releases.aspose.com/3d/net/).
- 要分割的輸入 3D 檔案（例如“test.fbx”）。
## 導入命名空間
首先在 C# 專案中導入必要的命名空間：
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## 第 1 步：載入 3D 文件
```csharp
//文檔目錄的路徑。
string input = RunExamples.GetDataFilePath("test.fbx");
//載入 3D 文件
Scene scene = new Scene(input);
```
在此步驟中，我們使用 Aspose.3D 載入 3D 文件`Scene`班級。
## 步驟2：分割所有網格
```csharp
//分割所有網格
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
在這裡，我們使用`SplitMesh`方法從`PolygonModifier`類別根據材質分割所有網格。
## 第 3 步：儲存分割場景
```csharp
//保存存檔
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
將修改後的場景儲存到新檔案以保留變更。
## 步驟4：顯示成功訊息
```csharp
//顯示成功訊息
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
列印成功訊息，表示操作已成功完成。
## 結論
恭喜！您已成功學習如何使用 Aspose.3D for .NET 依材質分割 3D 場景的所有網格。這對於組織和管理複雜的 3D 模型來說是一種有價值的技術。
## 常見問題解答
### 1. 我可以將Aspose.3D for .NET與其他程式語言一起使用嗎？
Aspose.3D 主要是為.NET 設計的，但它透過.NET 語言綁定提供與其他語言的互通性。
### 2. 有試用版嗎？
是的，您可以存取免費試用版[這裡](https://releases.aspose.com/).
### 3. 在哪裡可以找到更多範例和文件？
瀏覽全面的文檔，位於[Aspose.3D 文檔](https://reference.aspose.com/3d/net/).
### 4. 如何獲得對Aspose.3D的支援？
參觀[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持和討論。
### 5. 我可以獲得臨時許可證嗎？
是的，您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).