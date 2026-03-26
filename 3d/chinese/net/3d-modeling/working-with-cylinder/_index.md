---
date: 2026-03-26
description: 学习如何使用 Aspose.3D for .NET 创建圆柱体并导出 OBJ 文件。本初学者友好指南涵盖 3D 场景设置和 OBJ 导出。
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: 如何创建带剪切底部的圆柱体 – Aspose.3D for .NET
url: /zh/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用剪切底部创建圆柱体 – Aspose.3D for .NET

## 介绍
如果你想了解 **如何创建圆柱体** 并在 .NET 环境中自定义剪切底部，你来对地方了。在本教程中，我们将逐步演示从搭建 3‑D 场景到将最终模型导出为 OBJ 文件的全部过程，帮助你使用 **Aspose.3D for .NET** 提升 *初学者 3D 建模* 技能。

## 快速答疑
- **启动 3D 模型的主要类是什么？** `Scene` 用于创建所有几何体的根容器。  
- **哪个方法将模型导出为 OBJ？** `scene.Save(..., FileFormat.WavefrontOBJ)`。  
- **测试是否需要许可证？** 提供免费试用 — 请参阅 FAQ 中的试用链接。  
- **我可以更改剪切角度吗？** 可以，使用 `Vector2` 值修改 `ShearBottom`。  
- **这适合初学者吗？** 绝对适合；API 抽象了底层网格处理。

## 什么是 3D 场景？
*3D 场景* 是一个层级容器，包含所有几何实体、灯光、相机和变换。在 Aspose.3D 中，`Scene` 类提供了一种简洁的方式来组织并随后导出模型。

## 为什么导出为 OBJ？
OBJ 是一种被广泛支持的基于文本的格式，许多 3‑D 应用程序（Blender、Maya、Unity）都可以导入。导出为 OBJ 可让你在 .NET 之外共享或进一步编辑圆柱体模型。

## 前置条件
在开始之前，请确保你具备以下条件：

- 基本的 C# 和 .NET 开发知识。  
- 已安装 **Aspose.3D for .NET** – 你可以在 **[此处](https://releases.aspose.com/3d/net/)** 下载。  
- 已准备好用于编码的 .NET IDE（Visual Studio、Rider 或 VS Code）。

## 导入命名空间
首先，将所需的命名空间引入作用域，以便识别 API 类型。

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

## 步骤 1：创建 3D 场景
`Scene` 对象充当模型层级的根节点。

```csharp
Scene scene = new Scene();
```

## 步骤 2：创建圆柱体 1
我们生成第一个圆柱体，半径为 2，高度为 10，且具有 20 条径向细分。

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 步骤 3：为圆柱体 1 定制剪切底部
应用剪切变换，启用扇形圆柱体生成，并调整其他属性以实现所需形状。

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 步骤 4：将圆柱体 1 添加到场景
使用平移变换将第一个圆柱体放置在合适的位置。

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 步骤 5：创建圆柱体 2
第二个圆柱体使用相同的基础尺寸，但不进行自定义剪切——非常适合并排对比。

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 步骤 6：将圆柱体 2 添加到场景
我们只需将第二个圆柱体附加到场景图中。

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 步骤 7：将场景导出为 OBJ 文件
最后，将整个场景保存为 OBJ 文件，以便在任何标准 3‑D 查看器中打开。

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## 常见问题及解决方案
| 问题 | 产生原因 | 解决办法 |
|------|----------|----------|
| **OBJ 文件为空** | 场景中没有附加几何体。 | 确保两个圆柱体都已添加到 `scene.RootNode`。 |
| **剪切效果不正确** | `ShearBottom` 需要角度的正切值。 | 使用 `Math.Tan(angleInRadians)`，或使用约为 47.5° 的 `0.83`。 |
| **文件路径错误** | 目录无效或缺失。 | 使用 `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`。 |

## 常见问答
### Aspose.3D for .NET 适合初学者吗？
当然！Aspose.3D for .NET 提供了高级 API，抽象了 3‑D 建模中数学密集的部分，使任何技能水平的开发者都能轻松上手。

### 我可以为不同的圆柱体应用不同的剪切角度吗？
可以，每个 `Cylinder` 实例都有独立的 `ShearBottom` 属性，你可以为每个对象分配不同的角度。

### 是否提供试用版本？
是的，你可以在 **[此处](https://releases.aspose.com/)** 体验免费试用版。

### 哪里可以获得更多支持？
访问 **[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)** 获取社区帮助、代码示例和讨论。

### 如何获取临时许可证？
获取临时许可证请前往 **[此处](https://purchase.aspose.com/temporary-license/)**。

**附加问答**

**问：如何将模型导出为其他格式，例如 STL？**  
答：在 `scene.Save` 调用中将 `FileFormat.WavefrontOBJ` 替换为 `FileFormat.STL`。

**问：创建圆柱体后可以为其添加动画吗？**  
答：可以，使用 Aspose.3D 提供的 `Animation` 类为节点变换添加关键帧动画。

**问：API 是否支持 .NET Core？**  
答：该库完全兼容 .NET Core、.NET 5+ 和 .NET 6+。

---

**最后更新：** 2026-03-26  
**测试环境：** Aspose.3D for .NET（最新发布）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}