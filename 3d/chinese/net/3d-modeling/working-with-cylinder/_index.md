---
title: 定制剪底油缸
linktitle: 定制剪底油缸
second_title: Aspose.3D .NET API
description: 通过我们详细的分步指南，学习使用 Aspose.3D for .NET 创建定制的剪切底部圆柱体。立即提升您的 3D 建模技能！
type: docs
weight: 12
url: /zh/net/3d-modeling/working-with-cylinder/
---
## 介绍
欢迎阅读我们有关使用 Aspose.3D for .NET 创建定制圆柱体的综合指南。如果您希望提高 3D 建模技能并为您的项目添加独特的功能，那么您来对地方了。在本教程中，我们将使用清晰的解释和代码片段逐步引导您完成该过程。
## 先决条件
在我们深入学习本教程之前，请确保您具备以下条件：
- 对 C# 和 .NET 编程有基本了解。
- 安装了 Aspose.3D for .NET 库。你可以下载它[这里](https://releases.aspose.com/3d/net/).
- 为 .NET 编程设置的开发环境。
## 导入命名空间
在 C# 代码中，首先导入必要的命名空间：
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
首先使用 Aspose.3D 创建 3D 场景：
```csharp
Scene scene = new Scene();
```
## 步骤 2：创建圆柱体 1
生成第一个圆柱体并设置其属性：
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## 步骤 3：为气缸 1 定制剪切底部
将定制的剪切底部应用于第一个圆柱体：
```csharp
//xy 平面（z 轴）剪切 47.5 度
cylinder1.ShearBottom = new Vector2(0, 0.83); 

//将GenerateFanCylinder 设置为true
cylinder1.GenerateFanCylinder = true;
//设置 Theta 长度
cylinder1.ThetaLength = MathUtils.ToRadian(270);

//设置顶部偏移
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## 第 4 步：将圆柱体 1 添加到场景中
将第一个圆柱体添加到场景中并设置其平移：
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## 第 5 步：创建圆柱体 2
生成具有相似属性的第二个圆柱体：
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## 第 6 步：将圆柱体 2 添加到场景中
将第二个圆柱体添加到场景中，无需自定义参数：
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## 第7步：保存场景
将场景另存为文档目录中的 Wavefront OBJ 文件：
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## 结论
恭喜！您已使用 Aspose.3D for .NET 成功创建了自定义剪切底部圆柱体。本教程旨在为具有不同 3D 建模和编程专业知识水平的用户提供分步指南。
## 经常问的问题
### Aspose.3D for .NET 适合初学者吗？
绝对地！ Aspose.3D for .NET 提供了一个用户友好的界面，使初学者和经验丰富的开发人员都可以使用它。
### 我可以对圆柱体应用不同的剪切角度吗？
是的，您可以单独定制每个圆柱体的剪切底部，从而实现独特的效果。
### 有试用版吗？
是的，您可以探索免费试用版[这里](https://releases.aspose.com/).
### 我在哪里可以找到额外的支持？
参观[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以获得社区支持和讨论。
### 我怎样才能获得临时许可证？
获取您的临时许可证[这里](https://purchase.aspose.com/temporary-license/).