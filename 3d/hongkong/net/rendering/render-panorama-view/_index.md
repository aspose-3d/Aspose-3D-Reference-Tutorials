---
title: 使用 Aspose.3D for .NET 輕鬆渲染 3D 全景圖
linktitle: 渲染 3D 場景的全景視圖
second_title: Aspose.3D .NET API
description: 了解如何使用 Aspose.3D for .NET 建立令人驚嘆的 3D 全景視圖。請按照我們的沉浸式場景渲染逐步指南進行操作。
weight: 13
url: /zh-hant/net/rendering/render-panorama-view/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D for .NET 輕鬆渲染 3D 全景圖

## 介紹
創建迷人的 3D 場景並將其渲染為全景視圖已成為現代應用程式的重要方面。 Aspose.3D for .NET 為希望將 3D 渲染功能無縫整合到其專案中的開發人員提供了強大的解決方案。在本教學中，我們將探索使用 Aspose.3D for .NET 渲染 3D 場景的全景視圖的過程。
## 先決條件
在深入學習本教程之前，請確保您具備以下先決條件：
-  Aspose.3D for .NET：下載並安裝 Aspose.3D 函式庫。您可以找到庫和文檔[這裡](https://releases.aspose.com/3d/net/).
- .NET 開發環境：確保您的電腦上設定了有效的 .NET 開發環境。
- 範例 3D 場景：下載範例 3D 場景文件，例如“VirtualCity.glb”，我們將使用它來渲染全景視圖。
## 導入命名空間
在您的 .NET 專案中，匯入使用 Aspose.3D 所需的命名空間：
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
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
使用 Aspose.3D 載入 3D 場景。將「VirtualCity.glb」替換為所需 3D 場景檔案的路徑。
## 第 2 步：設定相機和燈光
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
設定相機和燈光以適當捕捉 3D 場景。
## 第 3 步：建立渲染器和渲染目標
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024 * 3, 1024);
```
建立渲染器並定義立方體貼圖和最終全景影像的渲染目標。
## 第 4 步：配置視口和渲染
```csharp
rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
renderer.Render(rt);
```
使用相機配置視窗並渲染立方體貼圖。
## 第 5 步：對全景視圖套用後處理
```csharp
PostProcessing equirectangular = renderer.GetPostProcessing("equirectangular");
equirectangular.Input = rt.Targets[0];
renderer.Execute(equirectangular, final);
```
應用等距柱狀投影後處理來產生全景視圖。
## 第 6 步：儲存渲染的全景圖
```csharp
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "panorama.png", ImageFormat.Png);
```
將渲染後的全景影像儲存到指定的輸出目錄。
## 結論
透過 Aspose.3D for .NET，渲染 3D 場景的全景視圖變得非常簡單。透過無縫整合沉浸式 3D 視覺化增強您的應用程式。
## 經常問的問題
### Q：我可以使用自訂 3D 場景來渲染全景圖嗎？
是的，只需將範例場景檔案路徑替換為自訂 3D 場景的路徑即可。
### Q：是否有額外的後製效果？
Aspose.3D for .NET 提供各種後處理效果來增強渲染影像。
### Q：如何優化渲染效能？
根據應用程式的要求調整渲染參數和目標尺寸。
### Q：我可以將本教學整合到 Web 應用程式中嗎？
是的，透過將 Aspose.3D for .NET 合併到您的 .NET Web 專案中。
### Q：是否有支援 Aspose.3D 的社群論壇？
是的，請訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
