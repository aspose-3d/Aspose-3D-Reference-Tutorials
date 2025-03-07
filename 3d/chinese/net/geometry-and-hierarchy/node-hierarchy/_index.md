---
title: 了解节点层次结构
linktitle: 了解节点层次结构
second_title: Aspose.3D .NET API
description: 释放 Aspose.3D for .NET 的强大功能！通过此分步指南深入了解节点层次结构操作。轻松创建令人惊叹的 3D 场景。
weight: 16
url: /zh/net/geometry-and-hierarchy/node-hierarchy/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 了解节点层次结构

## 介绍

欢迎来到 Aspose.3D for .NET 的世界，这是一个功能强大的库，使开发人员能够在其 .NET 应用程序中无缝处理 3D 场景和模型。在本教程中，我们将使用 Aspose.3D 深入了解 3D 场景中节点层次结构的复杂性。读完本指南后，您将牢牢掌握如何通过节点操纵 3D 场景的结构，从而创造出令人惊叹的视觉体验。

## 先决条件

在我们开始 3D 之旅之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET 库：确保您已将 Aspose.3D 库集成到您的 .NET 项目中。如果您还没有这样做，请前往[文档](https://reference.aspose.com/3d/net/)以获得指导。

- 下载库：如果您尚未下载 Aspose.3D 库，请从以下位置获取最新版本：[下载链接](https://releases.aspose.com/3d/net/)并按照文档中提供的安装说明进行操作。

- 获取许可证：要释放 Aspose.3D 的全部潜力，您需要有效的许可证。如果您没有，您可以获取[这里](https://purchase.aspose.com/buy)或选择一个[免费试用](https://releases.aspose.com/)探索其能力。

- 支持和社区：加入 Aspose.3D 社区[支持论坛](https://forum.aspose.com/c/3d/18)与其他开发人员联系、寻求帮助并了解最新动态。

- 临时许可证（可选）：如果您在购买前探索 Aspose.3D，请考虑获取[临时执照](https://purchase.aspose.com/temporary-license/)用于扩展访问。

现在我们已经准备好了工具，让我们深入了解使用 Aspose.3D 进行 3D 节点层次结构操作的令人兴奋的世界。

## 导入命名空间

在您的 .NET 项目中，确保导入必要的命名空间以利用 Aspose.3D 提供的功能。将以下行添加到您的代码中：

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

这些命名空间将使您能够访问处理 3D 场景的基本类和方法。

## 第 1 步：初始化场景对象

```csharp
Scene scene = new Scene();
```

首先使用创建一个新的 3D 场景`Scene`班级。

## 第2步：创建子节点

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

通过在节点之间创建父子关系来建立层次结构。在这个例子中，`cube1`和`cube2`是子节点`top`节点。

## 第 3 步：创建并分配网格

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

使用合适的方法生成网格（此处，`CreateMeshUsingPolygonBuilder`）并将其分配给子节点。

## 第 4 步：设置翻译

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

定义每个立方体节点的平移，将它们定位在 3D 空间中。

## 第5步：将旋转应用于父节点

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

旋转父节点（`top`），并观察此转换如何影响其所有子节点。

## 第 6 步：保存 3D 场景

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

指定输出目录并以所需的文件格式保存 3D 场景（此处为 FBX7500ASCII）。

## 第7步：显示成功消息

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

通知用户节点层次结构已成功添加以及保存的文件位置。

## 结论

恭喜！您已成功浏览了 Aspose.3D for .NET 中 3D 节点层次结构的复杂世界。本教程为您提供了轻松创建、操作和保存 3D 场景的知识。当您继续您的旅程时，探索更多功能并在您的 .NET 项目中释放 Aspose.3D 的全部潜力。

## 常见问题解答

### Q1：我可以在没有许可证的情况下使用 Aspose.3D for .NET 吗？

A1：虽然许可证可以解锁所有功能，但您可以使用免费试用版探索具有有限功能的 Aspose.3D。

### Q2：还有其他支持的文件格式来保存 3D 场景吗？

A2：是的，Aspose.3D支持多种格式；请参阅文档以获取完整列表。

### Q3：我如何为 Aspose.3D 社区做出贡献？

A3：加入支持论坛，分享您的经验，并通过帮助他人解决疑问来做出贡献。

### Q4：Aspose.3D适合游戏开发吗？

A4：当然！ Aspose.3D 用途广泛，可以集成到游戏开发项目中。

### Q5: 临时许可证和正式许可证有什么区别？

A5：临时许可证提供用于评估目的的短期访问，而完整许可证则提供无限制的使用。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
