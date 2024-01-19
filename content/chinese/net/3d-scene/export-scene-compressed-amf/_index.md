---
title: 将 3D 场景导出为压缩的 AMF 格式
linktitle: 将 3D 场景导出为压缩的 AMF 格式
second_title: Aspose.3D .NET API
description: 了解如何使用 Aspose.3D for .NET 将 3D 场景导出为压缩的 AMF 格式。通过本分步指南增强您的开发技能。
type: docs
weight: 11
url: /zh/net/3d-scene/export-scene-compressed-amf/
---
## 介绍

在 3D 建模和渲染的动态世界中，效率和灵活性至关重要。 Aspose.3D for .NET 使开发人员能够将 3D 场景无缝导出为压缩的 AMF（增材制造文件）格式，确保最佳文件大小而不影响质量。本教程将逐步指导您完成整个过程，使初学者和经验丰富的开发人员都能轻松利用 Aspose.3D for .NET 的功能。

## 先决条件

在深入学习本教程之前，请确保您满足以下先决条件：

- 对 3D 建模概念的基本了解
- 您的计算机上安装了 Visual Studio
-  Aspose.3D for .NET 库。你可以下载它[这里](https://releases.aspose.com/3d/net/)
- 渴望提高您的 3D 开发技能！

## 导入命名空间

在您的项目中，确保导入必要的命名空间以利用 Aspose.3D for .NET 的功能：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 第 1 步：加载 3D 场景

首先使用 Aspose.3D for .NET 加载 3D 场景。创建一个场景对象并向其中添加盒子等实体：

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## 第 2 步：尺度变换

接下来，将缩放变换应用到场景中的另一个框：

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(5, 5, 5);
```

## 第 3 步：设置欧拉角

设置变换的欧拉角：

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## 第四步：创建子节点

通过创建子节点继续构建场景：

```csharp
scene.RootNode.CreateChildNode();
scene.RootNode.CreateChildNode().CreateChildNode(box);
scene.RootNode.CreateChildNode().CreateChildNode(box);
```

## 第5步：保存压缩的AMF文件

最后，将 3D 场景保存到所需输出目录中的压缩 AMF 文件中：

```csharp
scene.Save("Your Output Directory" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## 结论

恭喜！您已使用 Aspose.3D for .NET 成功将 3D 场景导出为压缩的 AMF 格式。这个强大的库为 3D 开发人员打开了一个充满可能性的世界，使他们能够创建高效且视觉上令人惊叹的模型。

## 常见问题解答

### Q1：Aspose.3D与流行的3D建模软件兼容吗？

A1：Aspose.3D支持各种文件格式，使其与流行的3D建模工具兼容。

### Q2：除了 AMF 之外，我还可以启用其他文件格式的压缩吗？

A2：是的，Aspose.3D 提供了启用各种文件格式压缩的选项。

### Q3：Aspose.3D 适合初学者和高级开发人员吗？

A3：当然！ Aspose.3D 为初学者提供简单性，为经验丰富的开发人员提供高级功能。

### Q4：导出的 3D 场景的大小有限制吗？

A4：Aspose.3D 旨在处理不同复杂程度的场景，并且没有严格的尺寸限制。

### Q5：我在哪里可以找到更多支持和社区讨论？

A5：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以寻求支持和讨论。