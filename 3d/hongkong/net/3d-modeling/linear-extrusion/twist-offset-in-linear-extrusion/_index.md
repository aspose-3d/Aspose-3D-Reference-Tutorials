---
title: 線性擠壓中的扭轉偏移
linktitle: 線性擠壓中的扭轉偏移
second_title: Aspose.3D .NET API
description: 透過我們有關線性拉伸中扭曲偏移的分步指南，探索 Aspose.3D for .NET 的魔力。輕鬆提升您的 3D 專案。
weight: 15
url: /zh-hant/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 線性擠壓中的扭轉偏移

## 介紹

歡迎來到 Aspose.3D for .NET 的世界，這是一個多功能函式庫，讓開發人員能夠輕鬆處理 3D 操作。在本教程中，我們將深入研究其中一個有趣的功能 - “線性擠出中的扭曲偏移”。如果您已準備好提升 3D 程式設計技能，那就讓我們開始吧！

## 先決條件

在我們踏上這趟令人興奮的旅程之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET 函式庫：從下列位置下載並安裝該函式庫：[發布頁面](https://releases.aspose.com/3d/net/).

- 您的開發環境：確保您的開發環境已設定並準備就緒。

## 導入命名空間

首先導入必要的命名空間以存取 Aspose.3D for .NET 提供的功能。在您的程式碼中，這可能如下所示：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

現在，讓我們將範例分解為可管理的步驟，以掌握線性拉伸中的扭曲偏移：

## 第 1 步：初始化基本設定檔

首先建立基本輪廓，此處以指定圓角半徑的矩形形狀為例。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 第 2 步：建立場景

產生 3D 場景來託管節點和形狀。

```csharp
Scene scene = new Scene();
```

## 第三步：建立節點

在場景中建構左側和右側節點。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## 第4步：左節點線性拉伸

使用扭曲和切片屬性對左側節點執行線性擠壓。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## 第 5 步：在右側節點上使用扭曲偏移進行線性擠壓

在右側節點上，使用扭曲、扭曲偏移和切片屬性執行線性擠出。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## 第 6 步：儲存 3D 場景

將 3D 場景儲存到所需的輸出目錄，並將檔案格式指定為 WavefrontOBJ。

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

恭喜！您已使用 Aspose.3D for .NET 成功實現了線性拉伸中的扭曲偏移。

## 結論

在本教程中，我們探索了 Aspose.3D for .NET 的強大功能，特別關注線性拉伸中的扭曲偏移。有了這些新發現的技能，您就可以為 3D 專案注入活力。

## 常見問題解答

### Q1：我可以將 Aspose.3D for .NET 與其他程式語言一起使用嗎？

A1：Aspose.3D 主要支援.NET 語言，但Aspose 為Java 和其他平台提供了類似的函式庫。

### 問題 2：如何取得 Aspose.3D for .NET 的臨時授權？

 A2：參觀[這個連結](https://purchase.aspose.com/temporary-license/)取得用於測試目的的臨時許可證。

### Q3：是否有 Aspose.3D for .NET 社群論壇？

 A3：當然！加入社群：[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)與其他開發人員接觸並尋求協助。

### Q4：是否有其他可用的範例和文件？

A4：探索[文件](https://reference.aspose.com/3d/net/)取得廣泛的指南和範例。

### Q5：哪裡可以購買 Aspose.3D for .NET？

 A5：前往[這個連結](https://purchase.aspose.com/buy)進行購買並釋放 Aspose.3D 的全部潛力。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
