---
title: 在 3D 視窗中應用視覺效果
linktitle: 在 3D 視窗中應用視覺效果
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 視覺化世界。使用逐步教學學習如何將迷人的視覺效果應用到場景中。透過像素化、灰階、邊緣偵測和模糊效果來提升您的專案。
type: docs
weight: 10
url: /zh-hant/net/rendering/apply-visual-effects/
---
## 介紹

增強 3D 場景的視覺吸引力是創造沉浸式體驗的重要方面。 Aspose.3D for .NET 提供了一組強大的工具來將視覺效果應用於 3D 視窗。在本教程中，我們將逐步介紹在 3D 場景中應用各種效果的過程，包括像素化、灰階、邊緣偵測和模糊。

## 先決條件

在深入學習本教學之前，請確保您具備以下條件：

- 具備 C# 和 .NET 開發的實用知識。
- 安裝了 Aspose.3D for .NET 函式庫。您可以從以下位置下載：[這裡](https://releases.aspose.com/3d/net/).
- 用於實驗的 3D 場景檔案（例如“scene.obj”）。

## 導入命名空間

首先，匯入 Aspose.3D 和其他相依性所需的命名空間。將以下行加入您的程式碼：

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

使用以下命令載入 3D 場景`Scene`班級。

## 第 2 步：建立相機

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

建立一個相機實例並設定其位置和目標。

## 第 3 步：為場景添加燈光

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

引入燈光以增強視覺效果。

## 第 4 步：建立渲染器和渲染目標

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    //配置渲染器設定
    renderer.EnableShadows = false;

    //建立渲染目標
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        //配置視窗
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        //將場景渲染為紋理
        renderer.Render(rt);

        //將渲染的紋理儲存到檔案中
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        //繼續後製效果...
    }
}
```

建立渲染器和渲染目標來捕捉場景。

## 第 5 步：應用後處理效果

### 步驟5.1 像素化效果

```csharp
//創建像素化效果
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

套用像素化效果並儲存結果。

### 步驟5.2 灰階效果

```csharp
//創建灰階效果
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

套用灰階效果並儲存結果。

### 步驟 5.3 組合效果

```csharp
//結合灰階和像素化效果
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

結合多種效果以獲得獨特的效果。

### 步驟5.4 邊緣偵測效果

```csharp
//建立邊緣偵測效果
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

套用邊緣偵測效果並儲存結果。

### 步驟 5.5 模糊效果

```csharp
//創造模糊效果
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

套用模糊效果並儲存結果。

## 結論

在 3D 視窗中試驗視覺效果可以增加場景的深度和創造力。 Aspose.3D for .NET 簡化了這個過程，提供了一系列後製效果來提升您的專案。

## 常見問題解答

### Q1：我可以同時套用多種效果嗎？

A1：是的，您可以組合不同的後處理效果以獲得獨特且複雜的結果。

### Q2：如何調整視覺效果的強度？

A2：每種效果可能都有參數，您可以調整這些參數來控制其強度。具體細節請參閱文件。

### Q3：Aspose.3D適合遊戲開發嗎？

A3：雖然Aspose.3D主要是為3D建模和渲染而設計的，但它也可以用於遊戲開發的某些方面。

### Q4：有額外的後製效果嗎？

A4：Aspose.3D提供了多種內建的後處理效果，您可以使用該程式庫建立自訂效果。

### Q5：我可以將Aspose.3D用於商業項目嗎？

 A5：是的，您可以將Aspose.3D用於商業目的。請參閱[購買頁面](https://purchase.aspose.com/buy)了解許可詳細資訊。