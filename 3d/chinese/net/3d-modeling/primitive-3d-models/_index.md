---
title: 创建原始 3D 模型
linktitle: 创建原始 3D 模型
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 建模世界。轻松创建令人惊叹的原始模型。
weight: 10
url: /zh/net/3d-modeling/primitive-3d-models/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 创建原始 3D 模型

## 介绍

欢迎来到 Aspose.3D for .NET 的令人兴奋的 3D 建模世界！在这个综合教程中，我们将逐步探索使用 Aspose.3D 创建原始 3D 模型的过程。无论您是经验丰富的开发人员还是好奇的初学者，本指南都将帮助您利用 Aspose.3D 的强大功能为您的项目制作视觉上令人惊叹的 3D 元素。

## 先决条件

在我们深入研究 3D 建模的迷人领域之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET：从以下位置下载并安装 Aspose.3D for .NET 库：[下载链接](https://releases.aspose.com/3d/net/).

- 开发环境：搭建.NET开发环境，确保与Aspose.3D的兼容性。

现在您已经具备了必要条件，让我们开始一步步创建原始 3D 模型的旅程。

## 导入命名空间

首先导入必要的命名空间以访问 Aspose.3D 提供的功能：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

有了这些命名空间，您就可以在 .NET 应用程序中释放 Aspose.3D 的强大功能了。

## 第 1 步：初始化场景对象

```csharp
//初始化场景对象
Scene scene = new Scene();
```

创建一个新的场景对象，作为 3D 杰作的画布。

## 第 2 步：创建盒子模型

```csharp
//创建盒子模型
scene.RootNode.CreateChildNode("box", new Box());
```

将盒模型添加到场景的根部。根据您的创意愿景定制盒子的尺寸和属性。

## 第 3 步：创建圆柱体模型

```csharp
//创建圆柱体模型
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

通过引入圆柱体模型来增强您的场景。调整其参数以获得所需的形状和尺寸。

## 步骤 4：以 FBX 格式保存绘图

```csharp
//以 FBX 格式保存绘图
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

以 FBX 格式保存您的 3D 杰作。为您的创建选择合适的输出目录和文件名。

## 第5步：显示成功消息

```csharp
//显示成功信息
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

庆祝你的成就！场景已从原始 3D 模型成功构建，并且文件已保存。

## 结论

恭喜！您已经使用 Aspose.3D for .NET 成功创建了令人惊叹的 3D 模型。本指南涵盖了基础知识，但可能性是无限的。探索[文档](https://reference.aspose.com/3d/net/)了解更高级的功能和技术。

## 常见问题解答

### Q1：我可以将 Aspose.3D for .NET 与其他编程语言一起使用吗？

A1：Aspose.3D 主要支持.NET，但还有其他版本可用于 Java 和其他平台。

### Q2: 有免费试用吗？

 A2：是的，您可以通过以下方式探索 Aspose.3D 的功能：[免费试用](https://releases.aspose.com/).

### 问题 3：在哪里可以找到对 Aspose.3D for .NET 的支持？

 A3：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以获得社区支持和讨论。

### Q4：如何获得临时驾照？

 A4：您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).

### Q5: 有可用的示例教程吗？

 A5：是的，请探索更多教程和示例[文档](https://reference.aspose.com/3d/net/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
