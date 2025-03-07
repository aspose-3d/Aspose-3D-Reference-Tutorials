---
title: 捕获 3D 场景中的视口
linktitle: 捕获 3D 场景中的视口
second_title: Aspose.3D .NET API
description: 学习使用 Aspose.3D for .NET 捕捉令人惊叹的 3D 视口。灵活渲染场景的分步指南。
weight: 11
url: /zh/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 捕获 3D 场景中的视口

## 介绍

在 3D 图形和可视化领域，捕获视口是增强场景深度和细节的一项基本技能。 Aspose.3D for .NET 为渲染和操作 3D 场景提供了强大的解决方案。本教程将指导您完成使用 Aspose.3D 在 3D 场景中捕获视口的过程，让您轻松创建令人惊叹的可视化效果。

## 先决条件

在深入学习本教程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET 库：确保您已安装 Aspose.3D 库。您可以从以下位置下载：[这里](https://releases.aspose.com/3d/net/).

## 导入命名空间

首先，将必要的命名空间导入到您的 .NET 项目中：

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

首先将现有的 3D 场景加载到您的项目中。以下代码片段演示了这一点：

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## 第 2 步：创建相机

接下来，创建相机的实例并设置其位置和目标：

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## 第 3 步：向场景添加灯光

通过添加光源来增强场景。下面的代码片段展示了如何创建点光源：

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## 步骤 4：配置渲染器和渲染目标

设置渲染器并创建用于捕获场景的渲染目标：

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ...（后续步骤中继续）
    }
}
```

## 第 5 步：定义视口并渲染

定义视口并渲染场景以生成输出图像：

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## 第6步：修改视口并再次渲染

修改视口并再次渲染场景，展示了 Aspose.3D 的灵活性：

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

继续尝试不同的配置以获得所需的视觉效果。

## 结论

在本教程中，我们探索了使用 Aspose.3D for .NET 在 3D 场景中捕获视口的过程。利用其强大的功能，您可以将 3D 图形项目提升到新的高度，提供迷人的视觉体验。

## 常见问题解答

### Q1: Aspose.3D 与其他 3D 文件格式兼容吗？

A1：是的，Aspose.3D 支持各种 3D 文件格式，确保与各种设计工具兼容。

### Q2：我可以使用Aspose.3D进行游戏开发吗？

A2：虽然Aspose.3D 主要是为图形和可视化而设计的，但它的功能可以补充游戏开发的某些方面。

### Q3：在哪里可以找到更多示例和文档？

 A3：探索综合[Aspose.3D 文档](https://reference.aspose.com/3d/net/)了解更多示例和详细信息。

### Q4：有免费试用吗？

A4：是的，您可以免费试用[这里](https://releases.aspose.com/).

### Q5：我如何寻求帮助或参与社区？

 A5：加入 Aspose.3D 社区[支持论坛](https://forum.aspose.com/c/3d/18)寻求帮助和合作。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
