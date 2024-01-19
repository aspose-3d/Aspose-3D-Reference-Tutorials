---
title: 线性挤压中的扭转偏移
linktitle: 线性挤压中的扭转偏移
second_title: Aspose.3D .NET API
description: 通过我们有关线性拉伸中扭曲偏移的分步指南，探索 Aspose.3D for .NET 的魔力。轻松提升您的 3D 项目。
type: docs
weight: 15
url: /zh/net/linear-extrusion/twist-offset-in-linear-extrusion/
---
## 介绍

欢迎来到 Aspose.3D for .NET 的世界，这是一个多功能库，使开发人员能够轻松处理 3D 操作。在本教程中，我们将深入研究其中一个有趣的功能 - “线性挤出中的扭曲偏移”。如果您已准备好提高 3D 编程技能，那就让我们开始吧！

## 先决条件

在我们踏上这一激动人心的旅程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET 库：从以下位置下载并安装该库：[发布页面](https://releases.aspose.com/3d/net/).

- 您的开发环境：确保您的开发环境已设置并准备就绪。

## 导入命名空间

首先导入必要的命名空间以访问 Aspose.3D for .NET 提供的功能。在您的代码中，这可能如下所示：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

现在，让我们将示例分解为可管理的步骤，以掌握线性拉伸中的扭曲偏移：

## 第 1 步：初始化基本配置文件

首先创建基本轮廓，此处以具有指定圆角半径的矩形形状为例。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 第 2 步：创建场景

生成 3D 场景来托管节点和形状。

```csharp
Scene scene = new Scene();
```

## 第三步：创建节点

在场景中构造左侧和右侧节点。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## 第4步：左节点线性拉伸

使用扭曲和切片属性对左侧节点执行线性挤压。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## 第 5 步：在右侧节点上使用扭曲偏移进行线性挤压

在右侧节点上，使用扭曲、扭曲偏移和切片属性执行线性挤出。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## 第 6 步：保存 3D 场景

将 3D 场景保存到所需的输出目录，并将文件格式指定为 WavefrontOBJ。

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

恭喜！您已使用 Aspose.3D for .NET 成功实现了线性拉伸中的扭曲偏移。

## 结论

在本教程中，我们探索了 Aspose.3D for .NET 的强大功能，特别关注线性拉伸中的扭曲偏移。有了这些新发现的技能，您就可以为 3D 项目注入活力。

## 常见问题解答

### Q1：我可以将 Aspose.3D for .NET 与其他编程语言一起使用吗？

A1：Aspose.3D 主要支持.NET 语言，但Aspose 为Java 和其他平台提供了类似的库。

### 问题 2：如何获得 Aspose.3D for .NET 的临时许可证？

 A2：参观[这个链接](https://purchase.aspose.com/temporary-license/)获得用于测试目的的临时许可证。

### Q3：是否有 Aspose.3D for .NET 社区论坛？

A3：当然！加入社区：[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)与其他开发人员接触并寻求帮助。

### Q4：是否有其他可用的示例和文档？

A4：探索[文档](https://reference.aspose.com/3d/net/)获取广泛的指南和示例。

### Q5：哪里可以购买 Aspose.3D for .NET？

 A5：前往[这个链接](https://purchase.aspose.com/buy)进行购买并释放 Aspose.3D 的全部潜力。