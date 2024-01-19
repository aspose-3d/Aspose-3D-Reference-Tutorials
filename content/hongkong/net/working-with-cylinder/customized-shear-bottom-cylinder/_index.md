---
title: 客製化剪底油缸
linktitle: 客製化剪底油缸
second_title: Aspose.3D .NET API
description: 透過我們詳細的逐步指南，學習使用 Aspose.3D for .NET 建立客製化的剪切底部圓柱體。立即提升您的 3D 建模技能！
type: docs
weight: 12
url: /zh-hant/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## 介紹
歡迎閱讀我們有關使用 Aspose.3D for .NET 建立自訂剪切底部圓柱體的綜合指南。如果您希望提高 3D 建模技能並為您的專案添加獨特的功能，那麼您來對地方了。在本教程中，我們將使用清晰的解釋和程式碼片段逐步引導您完成該過程。
## 先決條件
在我們深入學習本教學之前，請確保您具備以下條件：
- 對 C# 和 .NET 程式設計有基本了解。
- 安裝了 Aspose.3D for .NET 函式庫。你可以下載它[這裡](https://releases.aspose.com/3d/net/).
- 為 .NET 程式設定的開發環境。
## 導入命名空間
在 C# 程式碼中，首先匯入必要的命名空間：
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
首先使用 Aspose.3D 建立 3D 場景：
```csharp
Scene scene = new Scene();
```
## 步驟 2：建立圓柱體 1
產生第一個圓柱體並設定其屬性：
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## 步驟 3：為汽缸 1 訂製剪切底部
將定制的剪切底部應用於第一個圓柱體：
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); //xy 平面（z 軸）剪 47.5 度
```
## 第 4 步：將圓柱體 1 加入場景中
將第一個圓柱體加入場景並設定其平移：
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## 第 5 步：建立圓柱體 2
產生具有相似屬性的第二個圓柱體：
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## 第 6 步：將圓柱體 2 加入場景中
將第二個圓柱體加入沒有剪切底部的場景：
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## 第7步：儲存場景
將場景儲存為文件目錄中的 Wavefront OBJ 檔案：
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## 結論
恭喜！您已使用 Aspose.3D for .NET 成功建立了自訂剪切底部圓柱體。本教程旨在為具有不同 3D 建模和程式設計專業知識水平的使用者提供逐步指南。
## 經常問的問題
### Aspose.3D for .NET 適合初學者嗎？
絕對地！ Aspose.3D for .NET 提供了一個使用者友善的介面，使初學者和經驗豐富的開發人員都可以使用它。
### 我可以對圓柱體施加不同的剪切角度嗎？
是的，您可以單獨自訂每個圓柱體的剪切底部，從而實現獨特的效果。
### 有試用版嗎？
是的，您可以探索免費試用版[這裡](https://releases.aspose.com/).
### 我可以在哪裡找到額外的支援？
參觀[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持和討論。
### 我怎麼才能獲得臨時許可證？
取得您的臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).