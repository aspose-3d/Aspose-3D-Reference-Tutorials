---
title: 了解 3D 場景中的節點層次結構
linktitle: 了解 3D 場景中的節點層次結構
second_title: Aspose.3D .NET API
description: 釋放 Aspose.3D for .NET 的強大功能！透過此逐步指南深入了解節點層次結構操作。輕鬆創建令人驚嘆的 3D 場景。
type: docs
weight: 16
url: /zh-hant/net/geometry-and-hierarchy/node-hierarchy/
---
## 介紹

歡迎來到 Aspose.3D for .NET 的世界，這是一個功能強大的程式庫，使開發人員能夠在其 .NET 應用程式中無縫處理 3D 場景和模型。在本教學中，我們將使用 Aspose.3D 深入了解 3D 場景中節點層次結構的複雜度。閱讀本指南後，您將牢牢掌握如何透過節點操縱 3D 場景的結構，從而創造出令人驚嘆的視覺體驗。

## 先決條件

在我們開始 3D 之旅之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET 函式庫：確保您已將 Aspose.3D 函式庫整合到您的 .NET 專案中。如果您還沒有這樣做，請前往[文件](https://reference.aspose.com/3d/net/)以獲得指導。

- 下載庫：如果您尚未下載 Aspose.3D 庫，請從以下位置取得最新版本：[下載連結](https://releases.aspose.com/3d/net/)並按照文件中提供的安裝說明進行操作。

- 取得許可證：要釋放 Aspose.3D 的全部潛力，您需要有效的許可證。如果您沒有，您可以獲得[這裡](https://purchase.aspose.com/buy)或選擇一個[免費試用](https://releases.aspose.com/)探索其能力。

- 支持與社區：加入 Aspose.3D 社區[支援論壇](https://forum.aspose.com/c/3d/18)與其他開發人員聯繫、尋求協助並了解最新動態。

- 臨時許可證（可選）：如果您在購買前探索 Aspose.3D，請考慮獲取[臨時執照](https://purchase.aspose.com/temporary-license/)用於擴展存取。

現在我們已經準備好了工具，讓我們深入了解使用 Aspose.3D 進行 3D 節點層次結構操作的令人興奮的世界。

## 導入命名空間

在您的 .NET 專案中，請確保匯入必要的命名空間以利用 Aspose.3D 提供的功能。將以下行加入您的程式碼：

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

這些命名空間將使您能夠存取處理 3D 場景的基本類別和方法。

## 第 1 步：初始化場景對象

```csharp
Scene scene = new Scene();
```

首先使用建立一個新的 3D 場景`Scene`班級。

## 步驟2：建立子節點

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

透過在節點之間建立父子關係來建立層次結構。在這個例子中，`cube1`和`cube2`是子節點`top`節點。

## 第 3 步：建立並指派網格

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

使用合適的方法產生網格（此處，`CreateMeshUsingPolygonBuilder`）並將其指派給子節點。

## 第 4 步：設定翻譯

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

定義每個立方體節點的平移，將它們定位在 3D 空間。

## 步驟5：將旋轉應用於父節點

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

旋轉父節點（`top`），並觀察此轉換如何影響其所有子節點。

## 第 6 步：儲存 3D 場景

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

指定輸出目錄並以所需的檔案格式儲存 3D 場景（此處為 FBX7500ASCII）。

## 步驟7：顯示成功訊息

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

通知使用者節點層次結構已成功新增以及已儲存的檔案位置。

## 結論

恭喜！您已成功瀏覽了 Aspose.3D for .NET 中 3D 節點層次結構的複雜世界。本教學為您提供了輕鬆建立、操作和保存 3D 場景的知識。當您繼續您的旅程時，探索更多功能並在您的 .NET 專案中釋放 Aspose.3D 的全部潛力。

## 常見問題解答

### Q1：我可以在沒有許可證的情況下使用 Aspose.3D for .NET 嗎？

A1：雖然許可證可以解鎖所有功能，但您可以使用免費試用版探索具有有限功能的 Aspose.3D。

### Q2：還有其他支援的檔案格式來保存 3D 場景嗎？

A2：是的，Aspose.3D支援多種格式；請參閱文件以取得完整清單。

### Q3：我如何為 Aspose.3D 社群做出貢獻？

A3：加入支援論壇，分享您的經驗，並透過幫助他人解決疑問來做出貢獻。

### Q4：Aspose.3D適合遊戲開發嗎？

A4：當然！ Aspose.3D 用途廣泛，可整合到遊戲開發專案中。

### Q5: 臨時許可證和正式許可證有什麼不同？

A5：臨時許可證提供用於評估目的的短期訪問，而完整許可證則提供無限制的使用。