---
date: 2026-01-07
description: 学习如何在使用 Aspose.3D for .NET 进行线性拉伸时添加地面平面并导出 Wavefront OBJ 文件。掌握 3D 建模中的居中和接地技术。
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: 在线性挤压中添加基准平面和中心
url: /zh/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在线性拉伸中添加基准平面并居中

## 介绍

欢迎阅读本完整指南，学习如何使用 Aspose.3D for .NET 掌握线性拉伸技术。如果您希望 **向模型添加基准平面** 并 **导出 Wavefront OBJ** 文件，同时保持拉伸居中，那么您来对地方了。在本教程中，我们将深入探讨线性拉伸技巧，特别关注居中效果以及基准平面如何帮助您更清晰地可视化结果。

## 快速答疑
- **“添加基准平面”有什么作用？** 它提供了一个可视化参考，使您能够轻松看到拉伸在 X‑Z 平面上的位置。  
- **使用哪种格式导出模型？** 场景保存为 Wavefront OBJ 文件（`FileFormat.WavefrontOBJ`）。  
- **运行代码是否需要许可证？** 开发阶段可使用免费试用版；生产环境需要正式许可证。  
- **可以修改拉伸长度吗？** 可以——修改 `LinearExtrusion` 的第二个参数即可。  
- **居中是可选的吗？** 设置 `Center = true` 会使拉伸围绕轮廓中心；`false` 则对齐到一侧。

## 前置条件

在开始这段激动人心的旅程之前，请确保您已具备以下前置条件：

- 对 C# 编程语言有基本了解。  
- 机器上已安装 Visual Studio。  
- 已下载 Aspose.3D for .NET 库，可从 [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) 获取。  
- 确保在整个教程过程中可以访问 [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) 以供参考。

## 导入命名空间

首先，让我们导入必要的命名空间。这些将为我们的 3D 建模杰作奠定基础。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 步骤 1：初始化基础轮廓

我们先定义一个矩形轮廓，该轮廓将被拉伸。`RoundingRadius` 为角部添加了细微的圆角。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 步骤 2：创建 3D 场景

`Scene` 对象充当所有几何体、灯光和相机的容器。

```csharp
Scene scene = new Scene();
```

## 步骤 3：创建左、右节点

在根节点下创建两个兄弟节点。一个演示 **不居中** 的拉伸，另一个演示 **居中** 的拉伸。我们还会平移左侧节点，以防两个示例重叠。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## 步骤 4：在左节点执行线性拉伸（不居中）

这里我们在不居中的情况下拉伸轮廓。请注意 `Center = false` 标志。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## 步骤 5：为左节点添加基准平面（参考）

添加一个薄盒子作为 **基准平面**，这样您可以清晰地看到拉伸在基座上的位置。

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## 步骤 6：在右节点执行线性拉伸（居中）

现在我们对相同的轮廓进行拉伸，但启用居中。几何体将对称地围绕轮廓原点放置。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## 步骤 7：为右节点添加基准平面（参考）

在右节点再添加一个基准平面，以保持视觉比较的一致性。

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## 步骤 8：导出 Wavefront OBJ 文件

最后，我们 **导出 Wavefront OBJ**，以便结果可以在任何标准 3‑D 查看器中打开。

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 为什么要添加基准平面？

添加基准平面可以立即提供关于拉伸高度和对齐方式的可视化提示。当您需要比较居中与非居中结果时，这一点尤为有用，正如本教程所示。

## 常见问题与技巧

- **基准平面不可见：** 确保平面的厚度（`Box` 构造函数中的 `0.01`）足够小，不会遮挡拉伸，但又足够大以被渲染。  
- **导出失败：** 检查输出目录是否存在且您拥有写入权限。  
- **居中拉伸出现偏移：** 再次确认 `Center` 属性；`true` 使轮廓居中，`false` 则对齐到一侧。

## 常见问答

### Q1：我可以在其他编程语言中使用 Aspose.3D for .NET 吗？

A1：Aspose.3D 主要支持 .NET 语言，如 C# 和 VB.NET。

### Q2：在哪里可以找到 Aspose.3D 相关的支持？

A2：访问 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 获取专门的支持和讨论。

### Q3：Aspose.3D for .NET 有免费试用吗？

A3：有，您可以在 [此处](https://releases.aspose.com/) 获取免费试用。

### Q4：如何获取 Aspose.3D for .NET 的临时许可证？

A4：您可以在 [此处](https://purchase.aspose.com/temporary-license/) 获取临时许可证。

### Q5：在哪里购买 Aspose.3D for .NET 许可证？

A5：请在 [此处](https://purchase.aspose.com/buy) 购买许可证。

### Q6：我可以将场景导出为除 OBJ 之外的其他格式吗？

A6：可以，Aspose.3D 支持多种格式，如 STL、FBX 和 GLTF。只需在 `Save` 方法中更改 `FileFormat` 枚举值即可。

### Q7：如何更改拉伸的切片数量？

A7：在 `LinearExtrusion` 构造函数中调整 `Slices` 属性，以控制网格密度。

---

**最后更新：** 2026-01-07  
**测试环境：** Aspose.3D for .NET 最新版本  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}