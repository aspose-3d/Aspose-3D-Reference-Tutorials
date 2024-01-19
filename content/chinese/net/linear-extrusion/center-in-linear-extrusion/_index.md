---
title: 线性挤压中心
linktitle: 线性挤压中心
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 建模世界。集中线性挤压技术，创造令人惊叹的设计，并释放您的创造力。
type: docs
weight: 10
url: /zh/net/linear-extrusion/center-in-linear-extrusion/
---
## 介绍

欢迎阅读这份关于使用 Aspose.3D for .NET 掌握线性挤出的综合指南。如果您希望提高 3D 建模技能并创建令人惊叹的挤压件，那么您来对地方了。在本教程中，我们将深入研究线性挤出技术，特别关注居中方面，将您的设计提升到一个全新的水平。

## 先决条件

在我们踏上这一激动人心的旅程之前，请确保您具备以下先决条件：

- 对 C# 编程语言有基本了解。
- Visual Studio 安装在您的计算机上。
-  Aspose.3D for .NET 库，您可以从[Aspose.3D .NET 文档](https://reference.aspose.com/3d/net/).
- 确保您有权访问[Aspose.3D .NET 文档](https://reference.aspose.com/3d/net/)供整个教程参考。

## 导入命名空间

首先，让我们导入必要的命名空间。这些将为我们的 3D 建模杰作奠定基础。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 第 1 步：初始化基本配置文件

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 第 2 步：创建 3D 场景

```csharp
Scene scene = new Scene();
```

## 第三步：创建左右节点

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## 第四步：对左节点进行线性挤压

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## 步骤 5：设置参考地平面

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## 第6步：对右侧节点进行线性挤压

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## 步骤 7：设置参考地平面（右节点）

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## 第 8 步：保存 3D 场景

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 结论

恭喜！您已经成功掌握了使用 Aspose.3D for .NET 进行居中线性挤出的艺术。请随意尝试不同的参数并探索该技术提供的巨大可能性。

## 常见问题解答

### Q1：我可以将 Aspose.3D for .NET 与其他编程语言一起使用吗？

A1：Aspose.3D主要支持.NET语言，例如C#和VB.NET。

### Q2：在哪里可以找到对 Aspose.3D 相关查询的支持？

 A2：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)专门的支持和讨论。

### 问题 3：Aspose.3D for .NET 是否有免费试用版？

 A3：是的，您可以免费试用[这里](https://releases.aspose.com/).

### Q4：如何获得 Aspose.3D for .NET 的临时许可证？

A4：您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).

### Q5: 在哪里可以购买 Aspose.3D for .NET 许可证？

 A5：购买您的许可证[这里](https://purchase.aspose.com/buy).
