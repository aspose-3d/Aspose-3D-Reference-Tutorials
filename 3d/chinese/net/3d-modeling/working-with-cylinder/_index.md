---
date: 2026-01-12
description: 学习如何使用 Aspose.3D for .NET 创建剪切底部圆柱体以及如何导出 3D 模型 OBJ。请按照本分步指南，掌握 3D 建模。
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: 如何使用 Aspose.3D for .NET 创建剪切底部圆柱体
url: /zh/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 定制剪切底部圆柱体

## 介绍
欢迎阅读我们的完整指南，您将在本指南中 **学习如何使用 Aspose.3D for .NET 创建剪切底部圆柱体** 模型。无论您是在构建游戏资产、机械部件还是可视化演示，本教程都将一步步展示如何塑造圆柱体的底部、应用剪切，并最终 **导出 3D 模型 OBJ** 文件，以便在任何后续流水线中使用。让我们一起逐步操作，您即可在几分钟内开始生成自定义几何体。

## 快速答案
- **什么是剪切底部圆柱体？** 底面倾斜（剪切）而非平坦的圆柱体。  
- **使用哪个库？** Aspose.3D for .NET。  
- **如何导出模型？** 使用 `scene.Save(..., FileFormat.WavefrontOBJ)`。  
- **是否需要许可证？** 提供试用版；生产环境需商业许可证。  
- **需要哪些前置条件？** .NET 开发环境和 Aspose.3D NuGet 包。

## 什么是剪切底部圆柱体？
剪切底部圆柱体是指通过剪切操作对标准圆柱网格的底面进行变形的模型。这样您可以轻松创建倾斜的底座、斜坡或自定义连接件，而无需手动编辑顶点。

## 为什么在此任务中使用 Aspose.3D？
- **完整控制** 几何参数（半径、高度、段数）。  
- **内置剪切支持** 通过 `ShearBottom` 属性，免去低层网格操作。  
- **一键导出** 为 OBJ、FBX、STL 等流行格式，便于与其他工具无缝集成。

## 前提条件
在开始之前，请确保您具备：

- 基本的 C# 与 .NET 知识。  
- 已安装 Aspose.3D for .NET。您可以在 **[此处](https://releases.aspose.com/3d/net/)** 下载。  
- 一个兼容 .NET 的 IDE（Visual Studio、Rider 或 VS Code）。

## 导入命名空间
在您的 C# 文件中，首先导入必要的命名空间：

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

## 步骤 1：创建场景
实例化一个新的 3‑D 场景，用于容纳所有对象。

```csharp
Scene scene = new Scene();
```

## 步骤 2：创建圆柱体 1
创建我们将为其定制剪切底部的主圆柱体。

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 步骤 3：为圆柱体 1 定制剪切底部
应用剪切、启用扇形生成，并调整其他属性以获得所需形状。

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 步骤 4：将圆柱体 1 添加到场景
将定制好的圆柱体放入场景，并稍微向右移动，以便并排查看两个对象。

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 步骤 5：创建圆柱体 2
创建第二个普通圆柱体用于对比。

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 步骤 6：将圆柱体 2 添加到场景
将第二个圆柱体直接加入场景——不做任何剪切——以帮助展示前面步骤的效果。

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 步骤 7：保存场景
最后，将整个场景导出为 OBJ 文件，您可以在 Blender、Maya 或其他 3‑D 查看器中打开。

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## 常见问题与技巧
- **剪切值**：`Vector2` 接受 X、Y 两个剪切因子。`0.83` 大约对应 47.5°，您可以根据需要调整角度。  
- **导出路径**：确保指定的文件夹已存在且具有写入权限，否则 `scene.Save` 会抛出异常。  
- **性能**：对于段数极高的圆柱体，建议降低段数（示例中为 `20`），以保持 OBJ 文件大小在可接受范围。

## 常见问答

### Aspose.3D for .NET 适合初学者吗？
当然！Aspose.3D for .NET 提供友好的 API，既适合初学者，也适合有经验的开发者。

### 我可以对圆柱体应用不同的剪切角度吗？
可以，您可以为每个圆柱体单独自定义 `ShearBottom`，实现独特效果。

### 有试用版吗？
有，您可以在 **[此处](https://releases.aspose.com/)** 免费试用。

### 我在哪里可以找到额外支持？
请访问 **[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)** 获取社区支持与讨论。

### 我如何获取临时许可证？
请在 **[此处](https://purchase.aspose.com/temporary-license/)** 获取临时许可证。

**附加问答**

**Q: 如何将导出格式改为 FBX？**  
A: 在 `scene.Save` 调用中将 `FileFormat.WavefrontOBJ` 替换为 `FileFormat.FBX`。

**Q: 导出后可以给圆柱体添加动画吗？**  
A: OBJ 不支持动画；如果需要动画数据，请使用 FBX 或 GLTF。

**Q: 如果需要更大的圆柱体半径怎么办？**  
A: 调整 `Cylinder` 构造函数的前两个参数（例如 `new Cylinder(4, 4, …)`）。

## 结论
您已经掌握了如何使用 Aspose.3D for .NET **创建剪切底部圆柱体** 模型并将其导出为 OBJ 文件。请尝试不同的剪切值、段数和导出格式，以满足项目需求。祝您建模愉快！

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}