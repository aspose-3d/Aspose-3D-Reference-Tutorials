---
title: 通过变换矩阵变换节点
linktitle: 通过变换矩阵变换节点
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 在 3D 场景中轻松变换节点。通过教程学习分步节点转换。
weight: 21
url: /zh/net/geometry-and-hierarchy/transformation-node-matrix/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 通过变换矩阵变换节点

## 介绍

在 3D 图形和可视化的动态领域中，操纵场景中的对象的能力是一个至关重要的方面。 Aspose.3D for .NET 使开发人员能够使用变换矩阵无缝变换节点，为 3D 场景添加一层创造力和控制力。本教程将指导您逐步完成 3D 场景中节点的变换过程。

## 先决条件

在深入学习本教程之前，请确保您具备以下先决条件：

1.  Aspose.3D for .NET 库：确保您的 .NET 项目中安装了 Aspose.3D 库。你可以下载它[这里](https://releases.aspose.com/3d/net/).

2. 开发环境：设置一个工作的 .NET 开发环境，如果还没有，请创建一个新项目，在其中实现转换。

## 导入命名空间

首先将必要的命名空间导入到您的 .NET 项目中。这些命名空间提供了 3D 场景操作的基本类和方法。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

现在我们已经介绍了基础知识，让我们将转换过程分解为分步指南。

## 第 1 步：初始化场景

```csharp
// ExStart：通过变换矩阵添加变换到节点
//初始化场景对象
Scene scene = new Scene();

```

在此步骤中，我们创建一个新的空 3D 场景。

## 第 2 步：创建网格并附加到场景

```csharp
//调用 Common 类使用多边形生成器方法创建网格来设置网格实例
Mesh mesh = (new Box()).ToMesh();

//为网格创建一个容器节点。
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

在这里，我们使用多边形生成器方法生成网格并将其分配给节点，从而为立方体建立几何形状。

## 第3步：设置自定义翻译矩阵

```csharp
//设置自定义翻译矩阵
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

定义自定义转换矩阵以确定应用于节点的特定转换。根据所需转换的需要调整矩阵值。

将立方体节点包含在场景中，使其成为整个 3D 环境的一部分。

## 第 4 步：保存场景

```csharp
//文档目录的路径。
var output = "TransformationToNode.fbx";

//以支持的文件格式保存 3D 场景
scene.Save(output);
// ExEnd：通过变换矩阵添加变换到节点
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

指定输出目录和文件名，然后以所需的文件格式保存 3D 场景。在此示例中，我们将其保存为 FBX7500ASCII 格式。

## 结论

恭喜！您已使用 Aspose.3D for .NET 在 3D 场景中使用变换矩阵成功变换了节点。此功能为多样化且具有视觉吸引力的 3D 应用打开了大门。

## 常见问题解答

### Q1：3D图形中的变换矩阵是什么？

A1：变换矩阵是一种数学表示，用于对 3D 空间中的对象应用各种变换（平移、旋转、缩放）。

### Q2：我可以对单个节点应用多个转换吗？

A2：是的，您可以通过将各自的矩阵相乘并将结果应用到节点来组合多个变换。

### Q3：还有其他支持的文件格式来保存 3D 场景吗？

 A3：Aspose.3D for .NET 支持多种文件格式，包括 STL、GLTF、OBJ 等。请参阅[文档](https://reference.aspose.com/3d/net/)以获得完整的列表。

### Q4：如何获得 Aspose.3D for .NET 的临时许可证？

 A4：访问[临时许可证页面](https://purchase.aspose.com/temporary-license/)在 Aspose 网站上获取用于评估目的的临时许可证。

### Q5：我可以在哪里寻求帮助或与 Aspose.3D 社区联系？

 A5：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)使用 Aspose.3D 提出问题、分享经验并与其他开发人员联系。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
