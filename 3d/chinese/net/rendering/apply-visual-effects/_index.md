---
title: 在 3D 视口中应用视觉效果
linktitle: 在 3D 视口中应用视觉效果
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 可视化世界。使用分步教程学习如何将迷人的视觉效果应用到场景中。通过像素化、灰度、边缘检测和模糊效果提升您的项目。
weight: 10
url: /zh/net/rendering/apply-visual-effects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 3D 视口中应用视觉效果

## 介绍

增强 3D 场景的视觉吸引力是创造沉浸式体验的一个重要方面。 Aspose.3D for .NET 提供了一组强大的工具来将视觉效果应用于 3D 视口。在本教程中，我们将逐步介绍向 3D 场景应用各种效果的过程，包括像素化、灰度、边缘检测和模糊。

## 先决条件

在深入学习本教程之前，请确保您具备以下条件：

- 具备 C# 和 .NET 开发的实用知识。
- 安装了 Aspose.3D for .NET 库。您可以从以下位置下载：[这里](https://releases.aspose.com/3d/net/).
- 用于实验的 3D 场景文件（例如“scene.obj”）。

## 导入命名空间

首先，导入 Aspose.3D 和其他依赖项所需的命名空间。将以下行添加到您的代码中：

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

## 第 1 步：加载现有 3D 场景

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

使用以下命令加载 3D 场景`Scene`班级。

## 第 2 步：创建相机

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

创建一个相机实例并设置其位置和目标。

## 第 3 步：为场景添加灯光

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

引入灯光以增强视觉效果。

## 第 4 步：创建渲染器和渲染目标

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    //配置渲染器设置
    renderer.EnableShadows = false;

    //创建渲染目标
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        //配置视口
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        //将场景渲染为纹理
        renderer.Render(rt);

        //将渲染的纹理保存到文件中
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        //继续后期处理效果...
    }
}
```

创建渲染器和渲染目标来捕获场景。

## 第 5 步：应用后处理效果

### 步骤5.1 像素化效果

```csharp
//创建像素化效果
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

应用像素化效果并保存结果。

### 步骤5.2 灰度效果

```csharp
//创建灰度效果
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

应用灰度效果并保存结果。

### 步骤 5.3 组合效果

```csharp
//结合灰度和像素化效果
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

结合多种效果以获得独特的效果。

### 步骤5.4 边缘检测效果

```csharp
//创建边缘检测效果
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

应用边缘检测效果并保存结果。

### 步骤 5.5 模糊效果

```csharp
//创建模糊效果
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

应用模糊效果并保存结果。

## 结论

在 3D 视口中试验视觉效果可以增加场景的深度和创造力。 Aspose.3D for .NET 简化了这一过程，提供了一系列后处理效果来提升您的项目。

## 常见问题解答

### Q1：我可以同时应用多种效果吗？

A1：是的，您可以组合不同的后处理效果以获得独特且复杂的结果。

### Q2：如何调整视觉效果的强度？

A2：每种效果可能都有参数，您可以调整这些参数来控制其强度。具体细节请参阅文档。

### Q3：Aspose.3D适合游戏开发吗？

A3：虽然Aspose.3D主要是为3D建模和渲染而设计的，但它也可以用于游戏开发的某些方面。

### Q4：有额外的后期处理效果吗？

A4：Aspose.3D提供了多种内置的后处理效果，您可以使用该库创建自定义效果。

### Q5：我可以将Aspose.3D用于商业项目吗？

 A5：是的，您可以将Aspose.3D用于商业目的。请参阅[购买页面](https://purchase.aspose.com/buy)了解许可详细信息。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
