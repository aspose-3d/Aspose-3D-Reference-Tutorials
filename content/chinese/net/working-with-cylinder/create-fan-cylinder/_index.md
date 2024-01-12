---
title: 创建风筒
linktitle: 创建风筒
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 解锁 3D 设计世界！轻松打造令人惊叹的风扇和非风扇气缸。立即下载试用版。
type: docs
weight: 10
url: /zh/net/working-with-cylinder/create-fan-cylinder/
---
## 介绍
欢迎来到 Aspose.3D for .NET 的 3D 建模和可视化世界！在本分步指南中，我们将探索如何使用 Aspose.3D for .NET 创建迷人的风筒。 Aspose.3D 是一个功能强大的库，提供了在 .NET 应用程序中处理 3D 内容的广泛功能。
## 先决条件
在我们深入探索令人兴奋的 3D 建模世界之前，请确保您具备以下先决条件：
- 对 .NET 编程有基本的了解。
- Visual Studio 安装在您的计算机上。
-  Aspose.3D for .NET 库，您可以下载[这里](https://releases.aspose.com/3d/net/).
- 对通过 3D 设计释放您的创造力有真正的兴趣。
## 导入命名空间
让我们首先导入必要的命名空间，以使 Aspose.3D 功能在您的 .NET 项目中可用。
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//导入 Aspose.3D 命名空间
```
现在我们已经完成所有设置，让我们将创建风筒的过程分解为可管理的步骤。
## 第 1 步：创建场景
```csharp
//创建场景
Scene scene = new Scene();
```
首先初始化一个新的 3D 场景。这是我们的风筒将变得栩栩如生的画布。
## 第 2 步：创建风筒
```csharp
//创建一个圆柱体
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
定义风筒的特性，指定半径、高度和分辨率等参数。
## 步骤 3：自定义风筒属性
```csharp
//将GenerateFanCylinder 设置为true
fan.GenerateFanCylinder = true;
//设置 Theta 长度
fan.ThetaLength = MathUtils.ToRadian(270);
```
通过启用风扇零件的生成并使用 ThetaLength 调整扫描角度来定制风扇气缸。
## 第 4 步：将风筒放置在场景中
```csharp
//创建子节点
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
将风扇气缸作为子节点添加到场景的根节点并将其放置在 3D 空间内。
## 第5步：创建一个非风扇圆柱体
```csharp
//创建一个没有风扇的圆柱体
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
通过创建没有风扇部分的圆柱体来探索 Aspose.3D 的灵活性。
## 步骤 6：自定义非风扇气缸属性
```csharp
//将GenerateFanCylinder 设置为 false
nonfan.GenerateFanCylinder = false;
//设置 Theta 长度
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
通过禁用风扇部分的生成来区分非风扇气缸。
## 第 7 步：将非风扇圆柱体放置在场景中
```csharp
//创建子节点
scene.RootNode.CreateChildNode(nonfan);
```
同样，将非扇形圆柱体作为子节点添加到场景的根节点中。
## 第 8 步：保存场景
```csharp
//保存场景
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
以所需的格式和位置保存您的杰作。现在，您已经使用 Aspose.3D for .NET 成功创建了风扇和非风扇气缸！
## 结论
祝贺您完成本使用 Aspose.3D for .NET 进行 3D 建模的实践指南！您已经在数字领域释放了创造力，轻松制作风扇和非风扇气缸。
## 经常问的问题
### 我可以将 Aspose.3D for .NET 与其他 .NET 框架一起使用吗？
是的，Aspose.3D 与各种 .NET 框架兼容，为您的开发项目提供多功能性。
### Aspose.3D for .NET 是否有免费试用版？
是的，您可以探索免费试用[这里](https://releases.aspose.com/).
### 在哪里可以找到 Aspose.3D for .NET 的详细文档？
文档可用[这里](https://reference.aspose.com/3d/net/).
### 如何获得 Aspose.3D for .NET 支持？
访问支持论坛[这里](https://forum.aspose.com/c/3d/18)寻求社区和 Aspose 专家的帮助。
### Aspose.3D for .NET 是否有临时许可证？
是的，可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).