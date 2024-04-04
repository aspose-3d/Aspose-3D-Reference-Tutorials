---
title: 按材质分割场景的所有网格
linktitle: 按材质分割场景的所有网格
second_title: Aspose.3D .NET API
description: 了解如何使用 Aspose.3D for .NET 按材质分割 3D 网格。按照我们的分步指南高效组织和管理 3D 模型。
type: docs
weight: 21
url: /zh/net/meshes/split-all-meshes-by-material/
---
## 介绍
欢迎阅读本分步指南，了解如何使用 Aspose.3D for .NET 按材质分割 3D 场景的所有网格。如果您正在使用 3D 模型并希望根据材质有效地组织网格，那么本教程适合您。 Aspose.3D 是一个功能强大的 .NET 库，提供了一系列用于处理 3D 文件的功能，使其成为开发人员的绝佳选择。
## 先决条件
在深入学习本教程之前，请确保您满足以下先决条件：
- 对 C# 编程语言有基本了解。
- Visual Studio 安装在您的计算机上。
-  Aspose.3D for .NET 库。您可以从以下位置下载：[这里](https://releases.aspose.com/3d/net/).
- 要分割的输入 3D 文件（例如“test.fbx”）。
## 导入命名空间
首先在 C# 项目中导入必要的命名空间：
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## 第 1 步：加载 3D 文件
```csharp
//文档目录的路径。
string input = RunExamples.GetDataFilePath("test.fbx");
//加载 3D 文件
Scene scene = new Scene(input);
```
在此步骤中，我们使用 Aspose.3D 加载 3D 文件`Scene`班级。
## 第2步：分割所有网格
```csharp
//分割所有网格
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
在这里，我们使用`SplitMesh`方法从`PolygonModifier`类根据材质分割所有网格。
## 第 3 步：保存分割场景
```csharp
//保存存档
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
将修改后的场景保存到新文件以保留更改。
## 第4步：显示成功消息
```csharp
//显示成功信息
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
打印一条成功消息，表明操作已成功完成。
## 结论
恭喜！您已成功学习如何使用 Aspose.3D for .NET 按材质分割 3D 场景的所有网格。这对于组织和管理复杂的 3D 模型来说是一种很有价值的技术。
## 常见问题解答
### 1. 我可以将Aspose.3D for .NET与其他编程语言一起使用吗？
Aspose.3D 主要是为.NET 设计的，但它通过.NET 语言绑定提供与其他语言的互操作性。
### 2. 有试用版吗？
是的，您可以访问免费试用版[这里](https://releases.aspose.com/).
### 3. 在哪里可以找到更多示例和文档？
浏览全面的文档，位于[Aspose.3D 文档](https://reference.aspose.com/3d/net/).
### 4. 如何获得对Aspose.3D的支持？
参观[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以获得社区支持和讨论。
### 5. 我可以获得临时许可证吗？
是的，您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).