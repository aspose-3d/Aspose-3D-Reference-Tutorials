---
title: 将 PBR 材质应用到盒子上
linktitle: 将 PBR 材质应用到盒子上
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 图形世界。使用基于物理的渲染材质轻松创建身临其境的场景。
type: docs
weight: 10
url: /zh/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## 介绍

欢迎来到 3D 图形的迷人世界！在本分步指南中，我们将探索强大的 Aspose.3D for .NET 库，并学习如何使用基于物理的渲染 (PBR) 材质创建令人惊叹的 3D 场景。 Aspose.3D 简化了 3D 图形的复杂过程，并为开发人员开辟了可能性的领域。

## 先决条件

在我们进入令人兴奋的 3D 图形世界之前，让我们确保您已完成所有设置：

### 下载并安装 Aspose.3D for .NET

参观[Aspose.3D for .NET 文档](https://reference.aspose.com/3d/net/)有关下载和安装该库的详细说明。

### 获得许可证

要释放 Aspose.3D 的全部潜力，请获取有效的许可证。您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/)或购买完整许可证[这里](https://purchase.aspose.com/buy).

## 导入命名空间

首先，确保导入必要的命名空间以利用 Aspose.3D for .NET 的功能：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 第 1 步：初始化场景

首先使用以下代码片段初始化 3D 场景：

```csharp
Scene scene = new Scene();
```

## 第2步：初始化PBR材质

创建PBR材质对象以实现真实渲染：

```csharp
PbrMaterial mat = new PbrMaterial();
```

## 第 3 步：设置材料属性

微调材料属性，使其几乎是金属的并且非常粗糙：

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## 第四步：创建一个盒子

生成一个将应用 PBR 材质的盒子：

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## 第 5 步：将材料应用到盒子上

将PBR材质分配给创建的盒子节点：

```csharp
boxNode.Material = mat;
```

## 第 6 步：保存 3D 场景

使用所需的输出目录将 3D 场景保存为 STL 格式：

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

恭喜！您已使用 Aspose.3D for .NET 成功将 PBR 材质应用到 3D 场景中的盒子。

## 结论

使用 Aspose.3D for .NET 涉足 3D 图形领域，打开了无限创意可能性的大门。凭借其直观的 API 和强大的功能，创建视觉上令人惊叹的场景成为开发人员的一种愉快的体验。

## 常见问题解答

### Q1: Aspose.3D 与其他 3D 文件格式兼容吗？

A1：是的，Aspose.3D 支持各种 3D 文件格式，确保项目的灵活性。

### Q2：我可以将Aspose.3D用于商业应用吗？

A2：当然！ Aspose.3D 提供商业许可证，可无缝集成到您的应用程序中。

### Q3：有试用版吗？

 A3：是的，您可以通过下载免费试用版来探索 Aspose.3D 的功能[这里](https://releases.aspose.com/).

### Q4：我在哪里可以找到社区支持和讨论？

 A4：加入 Aspose.3D 社区：[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以寻求支持和讨论。

### Q5：如何获得Aspose.3D的临时许可证？

 A5：您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/)出于评估目的。