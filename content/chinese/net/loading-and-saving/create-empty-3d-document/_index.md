---
title: 加载和保存 - 创建空 3D 文档
linktitle: 加载和保存 - 创建空 3D 文档
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 文档创建的世界。轻松创建、编辑和保存令人惊叹的 3D 场景。
type: docs
weight: 11
url: /zh/net/loading-and-saving/create-empty-3d-document/
---
## 介绍

欢迎来到使用 Aspose.3D for .NET 创建 3D 文档的世界！在本教程中，我们将探讨加载和保存 3D 文档的基础知识。 Aspose.3D for .NET 提供了一套强大的工具来处理 3D 场景，我们将指导您完成每个步骤，以帮助您顺利入门。

## 先决条件

在我们深入学习本教程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET：确保您已安装该库。您可以从以下位置下载：[这里](https://releases.aspose.com/3d/net/).

## 导入命名空间

首先，在 .NET 项目中导入必要的命名空间：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 加载和保存 - 创建空 3D 文档

### 第 1 步：设置输出目录

```csharp
//文档目录的路径。
var output = "Your Output Directory" + "document.fbx";
```

### 步骤 2：创建一个空的 3D 文档

```csharp
//ExStart：创建空3D文档

//创建Scene类的对象
Scene scene = new Scene();

//将 3D 场景文档保存为 FBX 格式
scene.Save(output, FileFormat.FBX7500ASCII);

//ExEnd：创建空3D文档
```

### 第 3 步：显示结果

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

恭喜！您刚刚使用 Aspose.3D for .NET 创建了第一个空 3D 文档。请随意探索更多特性和功能，以释放该库的全部潜力。

## 结论

在本教程中，我们介绍了使用 Aspose.3D for .NET 创建空 3D 文档的基础知识。当您继续 3D 开发之旅时，请参阅[文档](https://reference.aspose.com/3d/net/)以获得深入的见解和高级功能。

## 常见问题解答

### Q1：Aspose.3D for .NET适合初学者吗？

A1：是的，Aspose.3D for .NET 提供了一个用户友好的界面，无论是初学者还是经验丰富的开发人员都可以使用它。

### Q2：我可以在购买前试用 Aspose.3D for .NET 吗？

 A2：当然！您可以免费试用[这里](https://releases.aspose.com/).

### 问题 3：如何获得 Aspose.3D for .NET 支持？

 A3：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)寻求帮助并与社区建立联系。

### 问题 4：Aspose.3D for .NET 是否有临时许可证？

 A4：是的，您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).

### Q5：哪里可以购买 Aspose.3D for .NET？

 A5：您可以购买图书馆[这里](https://purchase.aspose.com/buy).