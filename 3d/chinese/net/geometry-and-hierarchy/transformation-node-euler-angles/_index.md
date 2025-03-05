---
title: 通过欧拉角变换节点
linktitle: 通过欧拉角变换节点
second_title: Aspose.3D .NET API
description: 学习使用 Aspose.3D for .NET 轻松转换 3D 节点。请遵循我们的分步指南，让您的项目取得令人惊叹的结果。
type: docs
weight: 19
url: /zh/net/geometry-and-hierarchy/transformation-node-euler-angles/
---
## 介绍

欢迎来到这个关于使用 Aspose.3D for .NET 在 3D 场景中通过欧拉角变换节点的综合教程。在本指南中，我们将深入研究令人兴奋的 3D 图形世界，并探索使用欧拉角向节点添加变换的过程。 Aspose.3D for .NET 提供了用于处理 3D 场景和网格的强大工具，使其成为寻求项目多功能性和效率的开发人员的绝佳选择。

## 先决条件

在我们深入学习本教程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET 库：确保您已安装 Aspose.3D 库。你可以下载它[这里](https://releases.aspose.com/3d/net/).

- 开发环境：设置您首选的 .NET 开发环境，例如 Visual Studio。

## 导入命名空间

首先导入必要的命名空间以访问 Aspose.3D for .NET 提供的功能：

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

现在，让我们将示例分解为多个步骤，以便清楚地理解。

## 第 1 步：初始化场景对象

```csharp
//ExStart:AddTransformationToNodeByEulerAngles
//初始化场景对象
Scene scene = new Scene();
```

首先使用创建一个新的 3D 场景`Scene`班级。


## 第 2 步：使用原始 Box 创建网格

```csharp
//调用 Common 类使用多边形生成器方法创建网格来设置网格实例
Mesh mesh = (new Box()).ToMesh();
```

调用一个方法（在本例中，`CreateMeshUsingPolygonBuilder`从一个习惯`Common`类）来生成 3D 对象的网格。

## 步骤 3：为网格创建容器节点

```csharp
//将节点指向网格几何体
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

使用以下命令在场景中创建一个节点`Node`班级。该节点将用作 3D 对象的容器。

## 第 4 步：设置欧拉角和平移

```csharp
//欧拉角
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
//设置翻译
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

定义节点的欧拉角和平移以将其定位在 3D 空间中。

## 第 5 步：保存 3D 场景

```csharp
//文档目录的路径。
var output = "TransformationToNode.fbx";

//以支持的文件格式保存 3D 场景
scene.Save(output);
//ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

指定输出目录并以所需的文件格式（本例中为 FBX7500ASCII）保存 3D 场景，包括变换后的节点。

## 结论

恭喜！您已经成功学习了如何使用 Aspose.3D for .NET 在 3D 场景中通过欧拉角变换节点。这个强大的库为 3D 图形开发打开了无限可能的大门。

## 常见问题解答

### Q1：Aspose.3D 与其他 3D 建模工具兼容吗？

A1：Aspose.3D支持各种3D文件格式，增强了与流行建模工具的兼容性。

### Q2：我可以对单个节点应用多个转换吗？

A2：是的，您可以组合并应用多种变换来实现复杂的效果。

### Q3：在哪里可以找到其他 Aspose.3D 文档？

 A3：请参阅[文档](https://reference.aspose.com/3d/net/)获取详细信息和示例。

### Q4：使用 Aspose.3D for .NET 需要许可证吗？

 A4：是的，您可以获得许可证[这里](https://purchase.aspose.com/buy)或探索一个[免费试用](https://releases.aspose.com/).

### Q5：需要帮助或有具体问题吗？

 A5：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以获得社区支持。