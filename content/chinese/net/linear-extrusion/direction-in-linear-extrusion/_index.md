---
title: 线性挤出方向
linktitle: 线性挤出方向
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 开启 3D 建模世界。学习方向线性挤压、提高创造力并轻松制作沉浸式应用程序。
type: docs
weight: 11
url: /zh/net/linear-extrusion/direction-in-linear-extrusion/
---
## 介绍

在软件开发的动态世界中，创建沉浸式 3D 模型是一项不可或缺的技能。 Aspose.3D for .NET 为开发人员提供了一组强大的工具，以在其应用程序中发挥 3D 建模的潜力。在本教程中，我们将深入研究线性挤出的有趣世界，并探索“线性挤出方向”功能的细微差别。

## 先决条件

在我们踏上这一激动人心的旅程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET：从以下位置下载并安装该库[Aspose.3D .NET 文档](https://reference.aspose.com/3d/net/).

- 开发环境：确保您已设置有效的 .NET 开发环境。

## 导入命名空间

在您的 .NET 项目中，导入必要的命名空间以访问 Aspose.3D 的功能。将以下行添加到代码的开头：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 第 1 步：初始化基本配置文件

首先初始化要拉伸的基础轮廓。在此示例中，我们创建一个圆角半径为 0.3 的矩形。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 第 2 步：创建 3D 场景

通过创建场景为您的 3D 杰作奠定基础。

```csharp
Scene scene = new Scene();
```

## 第三步：创建节点

在场景中生成节点来表示 3D 环境的不同组件。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## 第四步：无方向线性挤压

使用以下命令对左侧节点执行线性挤压`Twist`和`Slices`特性。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## 第5步：带方向的线性挤压

通过结合扩展挤出能力`Direction`属性在右节点。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## 第 6 步：保存 3D 场景

通过保存 3D 场景来保留您的创作。代替`"Your Output Directory"`与所需的目录。

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

恭喜！您已经使用 Aspose.3D for .NET 成功实现了线性挤出，探索了传统方法和定向方法。

## 结论

在本教程中，我们使用 Aspose.3D for .NET 浏览了 3D 建模的迷人领域。线性挤压，无论有没有方向，都为寻求创建视觉上令人惊叹的应用程序的开发人员提供了无限的可能性。借助 Aspose.3D，3D 建模的力量触手可及。

## 常见问题解答

### Q1：如何获得 Aspose.3D for .NET 的临时许可证？

 A1：参观[申请临时许可证](https://purchase.aspose.com/temporary-license/)获得临时许可证。

### Q2：在哪里可以找到对 Aspose.3D 的支持？

 A2：加入[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)寻求帮助并与社区建立联系。

### Q3：有免费试用吗？

 A3：是的，通过免费试用探索这些功能[Aspose.3D 发布](https://releases.aspose.com/).

### Q4：如何购买 Aspose.3D for .NET？

 A4：导航至[Aspose 购买页面](https://purchase.aspose.com/buy)了解许可选项和购买详细信息。

### Q5：在哪里可以找到 Aspose.3D for .NET 的详细文档？

 A5：参考综合[Aspose.3D .NET 文档](https://reference.aspose.com/3d/net/)以获得深入的信息。