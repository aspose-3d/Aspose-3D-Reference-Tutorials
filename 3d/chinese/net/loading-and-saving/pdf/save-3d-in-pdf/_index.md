---
title: 将 3D 保存为 PDF
linktitle: 将 3D 保存为 PDF
second_title: Aspose.3D .NET API
description: 探索适用于 .NET 的 Aspose.3D。您的无缝 3D 建模和渲染首选库。轻松将 3D 模型保存为 PDF 格式。
weight: 19
url: /zh/net/loading-and-saving/pdf/save-3d-in-pdf/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 将 3D 保存为 PDF

## 介绍

欢迎使用我们关于使用 Aspose.3D for .NET 的综合指南！在本教程中，我们将引导您完成加载和保存 3D 模型的过程，重点关注以 PDF 格式保存 3D 模型的特定任务。 Aspose.3D for .NET 是一个功能强大的库，提供了处理 3D 文件的高效工具，使其成为该领域开发人员和爱好者的重要资源。

## 先决条件

在我们深入学习本教程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET：确保您已安装该库。如果没有，您可以从以下位置下载[Aspose.3D for .NET 文档](https://reference.aspose.com/3d/net/).

- 开发环境：设置您首选的 .NET 开发环境。

- 对 3D 概念的基本了解：熟悉基本的 3D 概念，因为本指南假定您具备 3D 建模的基本知识。

## 导入命名空间

在您的 .NET 项目中，确保导入必要的命名空间以访问 Aspose.3D 提供的功能：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using System.Drawing;
```

## 第 1 步：创建一个新场景

首先使用 Aspose.3D 库初始化一个新的 3D 场景。这是 3D 模型的基础。

```csharp
Scene scene = new Scene();
```

## 步骤2：添加Cylinder子节点

为了演示保存过程，让我们创建一个简单的 3D 模型 - 圆柱体。将圆柱体作为子节点添加到场景中。

```csharp
scene.RootNode.CreateChildNode("cylinder", new Cylinder()).Material = new PhongMaterial() { DiffuseColor = new Vector3(Color.DarkCyan) };
```

## 第三步：设置渲染模式和光照方案

定义 3D 场景的渲染模式和照明方案。此步骤允许您自定义模型的视觉外观。

```csharp
PdfSaveOptions opt = new PdfSaveOptions();
opt.LightingScheme = PdfLightingScheme.CAD;
opt.RenderMode = PdfRenderMode.ShadedIllustration;
```

## 第 4 步：保存为 PDF 格式

最后，通过指定输出目录和文件名来执行保存过程。在本例中，我们将 3D 模型保存为 PDF 格式。

```csharp
scene.Save("Your Output Directory" + "output_out.pdf", opt);
```

确保将“您的输出目录”替换为所需的路径。

## 结论

恭喜！您已成功学习了如何使用 Aspose.3D for .NET 创建简单的 3D 模型并将其保存为 PDF 格式。这只是您可以使用这个强大的库实现的目标的开始。探索更多功能和可能性[Aspose.3D 文档](https://reference.aspose.com/3d/net/).

## 常见问题解答

### Q1：Aspose.3D for .NET 是否兼容所有 3D 文件格式？

A1：是的，Aspose.3D for .NET 支持多种 3D 文件格式，确保与各种行业标准的兼容性。

### 问题 2：我可以在保存过程中自定义 3D 模型的视觉效果吗？

A2：当然！如教程中所示，您可以调整渲染模式、照明方案等以实现所需的视觉效果。

### 问题 3：在哪里可以找到对 Aspose.3D for .NET 的支持？

 A3：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)获取与 Aspose.3D for .NET 相关的社区支持和讨论。

### 问题 4：Aspose.3D for .NET 是否有免费试用版？

 A4：是的，您可以访问[免费试用](https://releases.aspose.com/)在购买之前探索 Aspose.3D for .NET 的功能。

### Q5：如何获得 Aspose.3D for .NET 的临时许可证？

 A5：要获得临时许可证，请访问[这个链接](https://purchase.aspose.com/temporary-license/)并按照提供的说明进行操作。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
