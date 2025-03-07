---
title: 使用 Aspose.3D for .NET 應用魚眼鏡頭效果
linktitle: 將魚眼鏡頭效果應用於 3D 場景
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 增強您的 3D 場景！了解如何逐步應用迷人的魚眼鏡頭效果。現在下載！
weight: 12
url: /zh-hant/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D for .NET 應用魚眼鏡頭效果

## 介紹
您是否希望增強 3D 場景的視覺吸引力？使用 Aspose.3D for .NET 深入探索魚眼鏡頭效果的迷人世界。本教學將逐步指導您如何將魚眼鏡頭效果應用到 3D 場景中，為它們提供獨特而迷人的視角。
## 先決條件
在我們開始之前，請確保您具備以下先決條件：
-  Aspose.3D for .NET：確保您已安裝 Aspose.3D for .NET 程式庫。如果沒有的話可以下載[這裡](https://releases.aspose.com/3d/net/).
- 範例 3D 場景：我們將使用範例 3D 場景檔案 (VirtualCity.glb)。您可以使用自己的場景或從以下位置下載範例[Aspose.3D 文檔](https://reference.aspose.com/3d/net/).
## 導入命名空間
在您的 .NET 專案中，包含存取 Aspose.3D 功能所需的命名空間。在程式碼開頭新增以下命名空間：
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## 第 1 步：載入 3D 場景
使用以下程式碼將 3D 場景檔案載入到您的專案中：
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## 第 2 步：設定相機和燈光
創建相機和燈光以增強場景的視覺效果。根據需要調整近平面、遠平面和旋轉模式等參數：
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## 第 3 步：建立渲染器和渲染目標
設定渲染器並為立方體貼圖和 2D 紋理建立渲染目標：
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## 第四步：應用魚眼鏡頭效果
對渲染的立方體貼圖執行魚眼鏡頭效果後處理：
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## 結論
恭喜！您已使用 Aspose.3D for .NET 成功將魚眼鏡頭效果套用到 3D 場景。嘗試不同的場景和參數來釋放您的創造力。
## 經常問的問題
### 我可以將魚眼效果應用於任何 3D 場景嗎？
是的，您可以將魚眼效果套用到任何 3D 場景。確保場景正確加載和照明以獲得最佳效果。
### 將視場角（fov）調整為360度有何意義？
360度的視野確保了完整的球面投影，創造出令人驚嘆的魚眼效果。
### 如何自訂 3D 場景中的照明？
您可以調整燈光的屬性，例如位置、類型和顏色，以實現所需的燈光效果。
### 可處理的 3D 場景的大小是否有限制？
3D 場景的大小主要受系統資源的限制。確保您的硬體可以處理場景的大小。
### 我可以使用不同的輸出格式而不是 PNG 來獲得魚眼效果結果嗎？
是的，您可以根據您的要求修改程式碼以將輸出儲存為不同的影像格式。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
