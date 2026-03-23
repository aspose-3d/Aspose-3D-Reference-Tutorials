---
date: 2026-03-23
description: 学习如何使用 Aspose.3D for .NET 进行切片线性拉伸。通过一步步的代码示例创建详细的 3D 模型。
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: 如何使用 Aspose.3D for .NET 通过切片实现线性拉伸
url: /zh/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D for .NET 进行切片线性拉伸

## 介绍

欢迎来到使用 Aspose.3D for .NET 的 3D 设计世界！在本教程中，您将学习 **如何使用切片进行线性拉伸**，这是一种可以控制模型细节层级的技术。无论您是经验丰富的开发者还是刚入门，我们都会逐步引导您，解释每一步背后的原因，并提供可立即应用的实用技巧。

## 快速解答
- **线性拉伸与切片是什么？** 它是一种将二维轮廓扩展为三维的方式，同时指定生成多少个中间横截面（切片）。  
- **为什么使用切片？** 更多的切片可以获得更平滑的曲率；较少的切片则保持网格轻量。  
- **先决条件？** Aspose.3D for .NET、兼容 .NET 的 IDE，以及基本的 C# 知识。  
- **典型运行时间？** 示例在现代 PC 上运行时间不足一秒。  
- **输出格式？** 示例保存为 Wavefront OBJ，但 Aspose.3D 支持多种格式。

## 什么是带切片的线性拉伸？

线性拉伸将二维形状（轮廓）沿直线拉伸，以创建三维实体。**Slices** 属性决定在拉伸的起始和结束之间插入多少个中间横截面，从而影响平滑度和多边形数量。

## 为什么在线性拉伸中使用切片？

- **控制网格密度：** 微调视觉质量与文件大小之间的平衡。  
- **优化性能：** 在实时应用中使用更少的切片，在高分辨率渲染中使用更多切片。  
- **创意灵活性：** 在不同对象上组合不同的切片数量，以突出设计意图。

## 先决条件

在开始之前，请确保您已拥有：

- Aspose.3D for .NET 库 – 从 [here](https://releases.aspose.com/3d/net/) 下载。  
- 支持 C# 的 IDE（如 Visual Studio、Rider、VS Code 等）。  
- 对 C# 语法和面向对象概念有基本了解。  
- 对 3D 几何进行实验的好奇心！

## 导入命名空间

首先，导入命名空间以获取对核心 Aspose.3D 类的访问权限。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 步骤指南

### 步骤 1：初始化基础轮廓

我们从一个简单的矩形形状开始，并为其添加一个小的圆角半径，使边缘不再完全锐利。

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### 步骤 2：创建 3D 场景

`Scene` 充当所有节点、网格、灯光和相机的容器。

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### 步骤 3：添加左侧和右侧节点

我们将在场景根节点下创建两个兄弟节点。左侧节点使用低切片数，右侧节点使用高切片数，以便您比较视觉差异。

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### 步骤 4：在左侧节点上执行线性拉伸（低细节）

这里我们仅使用 **2 个切片** 对矩形进行拉伸。这会生成粗糙的网格——非常适合快速预览。

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### 步骤 5：在右侧节点上执行线性拉伸（高细节）

现在我们使用 **10 个切片**，得到更平滑的结果。请注意几何体变得更细致。

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### 步骤 6：保存 3D 场景

最后，将场景写入 OBJ 文件。将 `"Your Output Directory"` 替换为您机器上有效的路径。

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|-------|----------------|-----|
| **未创建文件** | 输出路径无效或缺少写入权限。 | 使用绝对路径并确保文件夹存在。 |
| **对象看起来平坦** | `Slices` 设置为 1 或 0。 | 将 `Slices` 设置为至少 2，以实现可见的拉伸。 |
| **几何体异常** | 圆角半径对于矩形尺寸来说过大。 | 将 `RoundingRadius` 调整为小于矩形最小边一半的值。 |

## 常见问答

**问：我可以更改拉伸方向吗？**  
答：可以。使用节点的 `Transform` 属性在保存之前旋转或平移拉伸的几何体。

**问：Aspose.3D 支持其他拉伸类型吗？**  
答：当然。除了 `LinearExtrusion`，您还可以使用 `RevolveExtrusion`、`SweepExtrusion` 等。

**问：我可以导出哪些文件格式？**  
答：Aspose.3D 支持 OBJ、STL、FBX、3MF、Collada 等多种格式。只需更改 `FileFormat` 枚举即可。

**问：有没有办法以编程方式设置材质？**  
答：有。创建节点后，将 `Material` 分配给其 `Entity` 集合。

**问：切片数量如何影响内存使用？**  
答：更多的切片会增加顶点和面数，从而成比例地提升内存消耗。使用性能分析来找到适合目标平台的最佳平衡点。

## 原始常见问题

### Q1: 我可以将 Aspose.3D for .NET 与其他编程语言一起使用吗？

A1: Aspose.3D 主要面向 .NET 设计，但您可以通过 .NET 绑定探索与 Python 等语言的互操作性选项。

### Q2: 我在哪里可以找到 Aspose.3D for .NET 的详细文档？

A2: 请参阅文档 [here](https://reference.aspose.com/3d/net/) ，了解 Aspose.3D 功能和使用的深入信息。

### Q3: 是否有 Aspose.3D for .NET 的免费试用版？

A3: 有，您可以在 [here](https://releases.aspose.com/) 获取免费试用，以在购买前探索库的功能。

### Q4: 我如何获取 Aspose.3D for .NET 的技术支持？

A4: 请访问 Aspose.3D 论坛 [here](https://forum.aspose.com/c/3d/18) 寻求帮助并与社区互动。

### Q5: 我可以为 Aspose.3D for .NET 使用临时许可证吗？

A5: 可以，在 [here](https://purchase.aspose.com/temporary-license/) 获取临时许可证用于评估。

## 结论

您已经了解了使用 Aspose.3D for .NET 通过切片 **进行线性拉伸** 的方法，探讨了不同切片数量的影响，并学习了如何导出作品。尝试其他轮廓，调节 `Slices` 值，并集成材质或灯光，以创建可用于生产的 3D 资产。

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}