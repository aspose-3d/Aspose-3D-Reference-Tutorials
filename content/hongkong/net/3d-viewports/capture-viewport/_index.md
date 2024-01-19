---
title: 捕捉 3D 場景中的視窗
linktitle: 捕捉 3D 場景中的視窗
second_title: Aspose.3D .NET API
description: 學習使用 Aspose.3D for .NET 捕捉令人驚嘆的 3D 視窗。靈活渲染場景的分步指南。
type: docs
weight: 11
url: /zh-hant/net/3d-viewports/capture-viewport/
---
## 介紹

在 3D 圖形和視覺化領域，捕捉視窗是增強場景深度和細節的基本技能。 Aspose.3D for .NET 為渲染和操作 3D 場景提供了強大的解決方案。本教學將引導您完成使用 Aspose.3D 在 3D 場景中捕捉視窗的過程，讓您輕鬆創建令人驚嘆的視覺化效果。

## 先決條件

在深入學習本教程之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET 函式庫：確保您已安裝 Aspose.3D 函式庫。您可以從以下位置下載：[這裡](https://releases.aspose.com/3d/net/).

## 導入命名空間

首先，將必要的命名空間匯入到您的 .NET 專案中：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## 第 1 步：載入現有 3D 場景

首先將現有的 3D 場景載入到您的專案中。以下程式碼片段演示了這一點：

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## 第 2 步：建立相機

接下來，建立相機的實例並設定其位置和目標：

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## 第 3 步：為場景添加燈光

透過添加光源來增強場景。下面的程式碼片段展示如何建立點光源：

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## 步驟 4：配置渲染器和渲染目標

設定渲染器並建立用於捕獲場景的渲染目標：

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ……（後續步驟中繼續）
    }
}
```

## 第 5 步：定義視口並渲染

定義視窗並渲染場景以產生輸出影像：

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## 步驟6：修改視口並再次渲染

修改視窗並再次渲染場景，展示了 Aspose.3D 的靈活性：

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

繼續嘗試不同的配置以獲得所需的視覺效果。

## 結論

在本教程中，我們探索了使用 Aspose.3D for .NET 在 3D 場景中捕捉視窗的過程。利用其強大的功能，您可以將 3D 圖形項目提升到新的高度，提供迷人的視覺體驗。

## 常見問題解答

### Q1: Aspose.3D 與其他 3D 檔案格式相容嗎？

A1：是的，Aspose.3D 支援各種 3D 檔案格式，確保與各種設計工具相容。

### Q2：我可以使用Aspose.3D進行遊戲開發嗎？

A2：雖然Aspose.3D 主要是為圖形和視覺化而設計的，但它的功能可以補充遊戲開發的某些方面。

### Q3：在哪裡可以找到更多範例和文件？

 A3：探索綜合[Aspose.3D 文檔](https://reference.aspose.com/3d/net/)了解更多範例和詳細資訊。

### Q4：有免費試用嗎？

 A4：是的，您可以免費試用[這裡](https://releases.aspose.com/).

### Q5：我如何尋求協助或參與社區？

 A5：加入 Aspose.3D 社區[支援論壇](https://forum.aspose.com/c/3d/18)尋求幫助和合作。