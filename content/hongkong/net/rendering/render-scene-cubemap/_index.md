---
title: 將場景渲染為具有六個面的立方體貼圖
linktitle: 將場景渲染為具有六個面的立方體貼圖
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 建立令人驚嘆的立方體貼圖。按照我們的分步指南將 3D 場景渲染為迷人的六面立方體貼圖。
type: docs
weight: 14
url: /zh-hant/net/rendering/render-scene-cubemap/
---
## 介紹
歡迎閱讀本逐步指南，了解如何使用 Aspose.3D for .NET 將場景渲染為具有六個面的立方體貼圖。在本教程中，我們將引導您完成透過渲染 3D 場景來建立令人驚嘆的立方體貼圖的過程。 Aspose.3D 是一個功能強大的 .NET API，可簡化 3D 圖形操作，透過本指南，您將利用其功能來創建迷人的立方體貼圖。
## 先決條件
在我們深入學習本教程之前，請確保您具備以下先決條件：
- 具備 C# 和 .NET 開發的實用知識。
- 安裝了 Aspose.3D for .NET。你可以下載它[這裡](https://releases.aspose.com/3d/net/).
- 用於渲染的 GLB 格式的 3D 場景檔案（例如“VirtualCity.glb”）。
## 導入命名空間
首先在 C# 程式碼中匯入 Aspose.3D 所需的命名空間：
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
## 第 1 步：載入場景
使用以下程式碼載入 3D 場景檔案：
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## 第 2 步：創建相機和燈光
創建一個相機和兩個燈光來照亮場景：
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
## 步驟3：建立渲染器和渲染目標
創建一個渲染器和一個具有深度紋理的立方體貼圖渲染目標：
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## 第 4 步：儲存立方體貼圖面
使用指定的檔案名稱將立方體貼圖的每個面儲存到磁碟：
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## 結論
恭喜！您已使用 Aspose.3D for .NET 成功將 3D 場景渲染為立方體貼圖。利用這個強大的 API 探索更多自訂選項並增強您的 3D 圖形專案。
## 經常問的問題
### Q：我可以將 Aspose.3D for .NET 與其他 3D 檔案格式一起使用嗎？
是的，Aspose.3D 支援各種 3D 檔案格式，為您的專案提供靈活性。
### Q：如何獲得 Aspose.3D 支援？
參觀[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持和討論。
### Q：有免費試用嗎？
是的，您可以免費試用[這裡](https://releases.aspose.com/).
### Q：我可以使用 Aspose.3D 渲染帶有動畫的場景嗎？
絕對地！ Aspose.3D支援渲染動畫3D場景。
### Q：在哪裡可以找到詳細的文件？
請參閱[Aspose.3D 文檔](https://reference.aspose.com/3d/net/)以獲得深入的資訊。