---
title: 定制偏置顶缸
linktitle: 定制偏置顶缸
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 图形的奇迹。学习轻松创建定制的偏置顶部气缸。立即提升您的编码体验！
type: docs
weight: 11
url: /zh/net/working-with-cylinder/customized-offset-top-cylinder/
---
## 介绍
欢迎来到 Aspose.3D for .NET 的 3D 图形操作世界！在本教程中，我们将指导您完成使用 Aspose.3D 创建自定义偏移顶部圆柱体的过程，Aspose.3D 是一个功能强大的库，用于在 .NET 应用程序中处理 3D 场景、对象和格式。
## 先决条件
在我们深入学习本教程之前，请确保您具备以下先决条件：
- C# 编程语言的基础知识。
- Visual Studio 安装在您的计算机上。
- 下载 Aspose.3D for .NET 库并在您的项目中引用。
现在，让我们开始逐步指南！
## 导入命名空间
首先，确保在 C# 代码中导入必要的命名空间：
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## 第 1 步：创建场景
```csharp
//创建场景
Scene scene = new Scene();
```
这将使用 Aspose.3D 初始化一个新的 3D 场景。
## 第 2 步：初始化气缸
```csharp
//初始化气缸
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
在这里，我们创建一个具有特定参数（例如半径、高度和切片）的圆柱体。
## 步骤 3：设置第一个圆柱体的 OffsetTop
```csharp
//设置顶部偏移
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
这为第一个气缸设置了定制的偏移顶部。
## 步骤 4：为第一个圆柱体创建 ChildNode
```csharp
//创建子节点
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
我们将第一个圆柱体作为子节点添加到场景中，并调整其位置。
## 第 5 步：初始化第二个圆柱体
```csharp
//初始化第二个圆柱体，无需自定义OffsetTop
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
第二个气缸在没有定制偏移顶部的情况下初始化。
## 第6步：为第二个圆柱体创建ChildNode
```csharp
//创建子节点
scene.RootNode.CreateChildNode(cylinder2);
```
我们将第二个圆柱体作为子节点添加到场景中。
## 第7步：保存场景
```csharp
//节省
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
这会以 Wavefront OBJ 格式保存 3D 场景，包括自定义的偏移顶部圆柱体。
现在您已经使用 Aspose.3D for .NET 成功创建了自定义的偏移顶部圆柱体！
## 结论
在本教程中，我们探索了使用 Aspose.3D for .NET 创建自定义偏移顶部圆柱体的基础知识。该库为 .NET 应用程序中的 3D 图形操作开辟了无限的可能性。
## 常见问题解答
### 问：在哪里可以找到 Aspose.3D for .NET 的文档？
答：文档已提供[这里](https://reference.aspose.com/3d/net/).
### 问：如何下载 Aspose.3D for .NET？
答： 你可以下载[这里](https://releases.aspose.com/3d/net/).
### 问：Aspose.3D for .NET 是否有免费试用版？
答：是的，您可以免费试用[这里](https://releases.aspose.com/).
### 问：在哪里可以获得 Aspose.3D for .NET 支持？
答：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)为了支持。
### 问：我可以获得 Aspose.3D for .NET 的临时许可证吗？
答： 是的，您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).