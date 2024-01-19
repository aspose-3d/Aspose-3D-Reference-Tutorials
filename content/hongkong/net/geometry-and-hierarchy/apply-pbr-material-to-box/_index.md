---
title: 將 PBR 材質應用於 3D 場景中的盒子
linktitle: 將 PBR 材質應用於 3D 場景中的盒子
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 圖形世界。使用基於物理的渲染材質輕鬆創建身臨其境的場景。
type: docs
weight: 10
url: /zh-hant/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## 介紹

歡迎來到 3D 圖形的迷人世界！在本逐步指南中，我們將探索強大的 Aspose.3D for .NET 函式庫，並學習如何使用基於實體的渲染 (PBR) 材質來建立令人驚嘆的 3D 場景。 Aspose.3D 簡化了 3D 圖形的複雜過程，並為開發人員開闢了可能性的領域。

## 先決條件

在我們進入令人興奮的 3D 圖形世界之前，讓我們確保您已完成所有設定：

### 下載並安裝 Aspose.3D for .NET

參觀[Aspose.3D for .NET 文檔](https://reference.aspose.com/3d/net/)有關下載和安裝該庫的詳細說明。

### 獲得許可證

要釋放 Aspose.3D 的全部潛力，請取得有效的授權。您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/)或購買完整許可證[這裡](https://purchase.aspose.com/buy).

## 導入命名空間

首先，請確保導入必要的命名空間以利用 Aspose.3D for .NET 的功能：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 第 1 步：初始化場景

首先使用以下程式碼片段初始化 3D 場景：

```csharp
Scene scene = new Scene();
```

## 第2步：初始化PBR材質

建立PBR材質物件以實現真實渲染：

```csharp
PbrMaterial mat = new PbrMaterial();
```

## 第 3 步：設定材質屬性

微調材料屬性，使其幾乎是金屬的並且非常粗糙：

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## 第四步：創建一個盒子

產生一個將套用 PBR 材質的盒子：

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## 第 5 步：將材料應用到盒子上

將PBR材質分配給已建立的盒子節點：

```csharp
boxNode.Material = mat;
```

## 第 6 步：儲存 3D 場景

使用所需的輸出目錄將 3D 場景儲存為 STL 格式：

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

恭喜！您已使用 Aspose.3D for .NET 成功將 PBR 材質套用到 3D 場景中的盒子。

## 結論

使用 Aspose.3D for .NET 涉足 3D 圖形領域，打開了無限創意可能性的大門。憑藉其直覺的 API 和強大的功能，創建視覺上令人驚嘆的場景成為開發人員的一種愉快的體驗。

## 常見問題解答

### Q1: Aspose.3D 與其他 3D 檔案格式相容嗎？

A1：是的，Aspose.3D 支援各種 3D 檔案格式，確保專案的靈活性。

### Q2：我可以將Aspose.3D用於商業應用嗎？

A2：當然！ Aspose.3D 提供商業許可證，可無縫整合到您的應用程式中。

### Q3：有試用版嗎？

A3：是的，您可以透過下載免費試用版來探索 Aspose.3D 的功能[這裡](https://releases.aspose.com/).

### Q4：我可以在哪裡找到社區支持和討論？

 A4：加入 Aspose.3D 社群：[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以尋求支持和討論。

### Q5：如何取得Aspose.3D的臨時授權？

 A5：您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/)出於評估目的。