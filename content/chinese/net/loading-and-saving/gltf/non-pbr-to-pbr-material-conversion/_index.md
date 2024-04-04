---
title: 非 PBR 到 PBR 材质转换
linktitle: 非 PBR 到 PBR 材质转换
second_title: Aspose.3D .NET API
description: 探索 Aspose.3D for .NET - 轻松将非 PBR 材质转换为 PBR 材质。全面的教程和强大的 API。
type: docs
weight: 16
url: /zh/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## 介绍

欢迎阅读本分步指南，了解如何使用 Aspose.3D for .NET 将非 PBR（基于物理的渲染）转换为 PBR 材质。 Aspose.3D 是一个功能强大的 API，允许开发人员在其 .NET 应用程序中无缝使用 3D 文件格式。

## 先决条件

在我们深入学习本教程之前，请确保您满足以下先决条件：

-  Aspose.3D for .NET：确保您已安装 Aspose.3D for .NET 库。你可以找到下载链接[这里](https://releases.aspose.com/3d/net/).

- C# 的基本了解：本教程假设您对 C# 编程有基本的了解。

- IDE（集成开发环境）：选择您首选的 .NET 开发 IDE，例如 Visual Studio。

## 导入命名空间

在 C# 代码中，首先导入必要的命名空间：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 第 1 步：初始化新的 3D 场景

首先使用以下代码创建一个新的 3D 场景：

```csharp
// ExStart:Non_PBRtoPBRMaterial
//初始化一个新的 3D 场景
var scene = new Scene();
```

## 第 2 步：创建 3D 对象

接下来，创建一个 3D 对象，例如一个盒子：

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## 步骤 3：配置材质转换

设置非 PBR 到 PBR 转换的材质转换选项：

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## 步骤 4：保存为 GLTF 2.0 格式

将转换后的场景保存为 GLTF 2.0 格式：

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

根据您的特定用例的需要重复这些步骤，确保每个细节都配置正确。

## 结论

恭喜！您已成功学习如何使用 Aspose.3D for .NET 将非 PBR 材质转换为 PBR 材质。这个强大的工具为 .NET 应用程序中的 3D 图形操作开辟了无限的可能性。

## 常见问题解答

### Q1：Aspose.3D 是否兼容所有 3D 文件格式？

A1：是的，Aspose.3D 支持多种 3D 文件格式，为您的项目提供灵活性。

### Q2：我可以将Aspose.3D用于商业应用吗？

 A2：当然！ Aspose.3D是商业产品，您可以购买[这里](https://purchase.aspose.com/buy).

### Q3：测试需要临时许可证吗？

 A3：是的，您可以获得临时许可证用于测试目的[这里](https://purchase.aspose.com/temporary-license/).

### Q4：哪里可以找到对 Aspose.3D 的支持？

 A4：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以获得社区支持和讨论。

### Q5: 有免费试用吗？

A5：是的，您可以探索免费试用版[这里](https://releases.aspose.com/).