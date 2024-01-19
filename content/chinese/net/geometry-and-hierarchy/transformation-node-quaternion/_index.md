---
title: 在 3D 场景中通过四元数变换节点
linktitle: 在 3D 场景中通过四元数变换节点
second_title: Aspose.3D .NET API
description: 学习使用 Aspose.3D for .NET 使用四元数转换 3D 节点。初学者的分步指南。
type: docs
weight: 20
url: /zh/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## 介绍

欢迎阅读有关使用 Aspose.3D for .NET 在 3D 场景中按四元数转换节点的分步指南。在本教程中，我们将探索 Aspose.3D for .NET 的强大功能，并逐步完成使用四元数向 3D 节点添加转换的过程。

## 先决条件

在我们深入学习本教程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET：确保您已安装 Aspose.3D 库。您可以从[发布页面](https://releases.aspose.com/3d/net/).

- 开发环境：使用必要的工具和配置设置 .NET 开发环境。

- 对 3D 概念的基本了解：熟悉 3D 图形和概念将会有所帮助。

## 导入命名空间

在您的 .NET 项目中，包含 Aspose.3D 所需的命名空间：

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## 第 1 步：初始化场景对象

```csharp
// ExStart：通过四元数添加变换到节点
//初始化场景对象
Scene scene = new Scene();
```

## 步骤2：初始化节点类对象

```csharp
//初始化Node类对象
Node cubeNode = new Node("cube");
```

## 第 3 步：使用 Polygon Builder 创建网格

```csharp
//调用 Common 类使用多边形生成器方法创建网格来设置网格实例
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## 第 4 步：将节点指向网格几何体

```csharp
//将节点指向网格几何体
cubeNode.Entity = mesh;
```

## 第 5 步：使用四元数设置旋转

```csharp
//设置旋转
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## 第6步：设置翻译

```csharp
//设置翻译
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## 第7步：将立方体添加到场景中

```csharp
//将立方体添加到场景中
scene.RootNode.ChildNodes.Add(cubeNode);
```

## 第 8 步：保存 3D 场景

```csharp
//文档目录的路径。
var output = "Your Output Directory" + "TransformationToNode.fbx";

//以支持的文件格式保存 3D 场景
scene.Save(output, FileFormat.FBX7500ASCII);
//ExEnd：通过四元数添加变换到节点
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## 结论

恭喜！您已经成功学习了如何使用 Aspose.3D for .NET 在 3D 场景中通过四元数转换节点。参考以下内容探索更多功能和可能性[文档](https://reference.aspose.com/3d/net/).

## 常见问题解答

### Q1：3D图形中的四元数是什么？

A1：四元数是用于表示 3D 空间中的旋转的数学实体。

### Q2：如何下载 Aspose.3D for .NET？

 A2：您可以从以下位置下载该库：[发布页面](https://releases.aspose.com/3d/net/).

### 问题 3：Aspose.3D for .NET 是否有免费试用版？

 A3：是的，您可以从以下位置获得免费试用[这里](https://releases.aspose.com/).

### 问题 4：在哪里可以找到对 Aspose.3D for .NET 的支持？

 A4：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以寻求支持和讨论。

### Q5：如何获得Aspose.3D的临时许可证？

 A5：获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).
