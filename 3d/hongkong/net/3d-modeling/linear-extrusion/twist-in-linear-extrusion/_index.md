---
title: 線性擠壓扭轉
linktitle: 線性擠壓扭轉
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索迷人的 3D 圖形世界。逐步學習帶有扭曲的線性擠壓。
weight: 14
url: /zh-hant/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 線性擠壓扭轉

## 介紹

在不斷發展的 .NET 開發世界中，利用 3D 圖形的力量是一項令人興奮的努力。 Aspose.3D for .NET 成為一個有價值的工具包，使開發人員能夠無縫創建身臨其境且視覺震撼的應用程式。在本綜合指南中，我們將深入研究一個有趣的功能 - 扭曲的線性擠出。本教學將逐步引導您完成整個過程，釋放 Aspose.3D for .NET 的潛力。

## 先決條件

在我們開始 3D 之旅之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET：確保您已安裝 Aspose.3D 函式庫。如果沒有的話可以下載[這裡](https://releases.aspose.com/3d/net/).

- 基本的 .NET 開發知識：本教學假設您對 .NET 開發有基本的了解。

## 導入命名空間：

在任何 .NET 專案中，正確使用命名空間至關重要。首先導入必要的命名空間以有效地利用 Aspose.3D 的功能。這是一個指導您的片段：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

現在，讓我們將使用 Aspose.3D for .NET 進行線性擠壓和扭曲的有趣過程分解為易於理解的步驟：

## 第 1 步：初始化基本設定檔

```csharp
//初始化要擠出的基礎輪廓
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

首先設定擠出的基本輪廓。在此範例中，我們使用具有指定圓角半徑的矩形形狀。

## 第 2 步：建立 3D 場景

```csharp
//創建場景
Scene scene = new Scene();
```

建立一個 3D 場景，所有的魔法都將在其中發生。這是我們 3D 傑作的畫布。

## 第三步：建立左右節點

```csharp
//建立左節點
var left = scene.RootNode.CreateChildNode();
//建立右節點
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

在場景內產生左節點和右節點。調整左側節點的平移以放置在適當的位置。

## 步驟 4：在左節點上執行線性擠壓和扭曲

```csharp
//扭曲屬性定義擠壓輪廓時的旋轉程度
//使用扭曲和切片屬性對左側節點執行線性擠壓
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

這就是奇蹟發生的地方。在左側節點上執行線性拉伸，並結合扭曲屬性來定義旋轉程度。調整切片數量以獲得更精細的細節。

## 步驟5：在右側節點上執行線性擠壓並扭轉

```csharp
//使用扭曲和切片屬性在右側節點上執行線性擠壓
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

在右側節點上鏡像該過程，嘗試不同的扭曲值以觀察擠壓的變化。

## 第 6 步：儲存 3D 場景

```csharp
//儲存 3D 場景
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

最後，將您的 3D 傑作儲存到所需的輸出目錄。依照您的喜好調整檔案名稱。

## 結論

在本教程中，我們使用 Aspose.3D for .NET 探索了帶有扭曲的線性拉伸的迷人領域。此功能打開了創造可能性的大門，使開發人員能夠輕鬆地將動態視覺元素注入到他們的應用程式中。

## 常見問題解答

### Q1：我可以將帶有扭曲的線性擠壓應用於其他形狀嗎？

A1：當然！您可以嘗試矩形以外的各種基本輪廓，從而釋放無數的設計可能性。

### Q2：「扭曲」屬性在線性擠出中扮演什麼角色？

A2：「扭曲」屬性決定了擠出過程中的旋轉程度，影響最終的 3D 形狀。

### Q3：使用大量切片時是否有效能考量？

A3：雖然更多的切片可以增加細節，但它會影響性能。根據您的應用程式的要求取得平衡。

### Q4：我可以將線性拉伸與其他 Aspose.3D 功能結合嗎？

A4：當然！ Aspose.3D 提供了一組豐富的功能。您可以隨意將線性拉伸與其他功能結合起來，以實現更複雜的設計。

### Q5：有 Aspose.3D 支持和討論的社群嗎？

 A5：是的，加入 Aspose.3D 社群：[Aspose論壇](https://forum.aspose.com/c/3d/18)以獲得支持和參與討論。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
