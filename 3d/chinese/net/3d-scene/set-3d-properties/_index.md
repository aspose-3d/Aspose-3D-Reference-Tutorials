---
date: 2026-03-28
description: 学习如何使用 Aspose.3D for .NET 列出材质属性、更改漫反射颜色以及修改 3D 材质属性。附带一步一步的代码示例。
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: 使用 Aspose.3D 列出 3D 场景中的材质属性
url: /zh/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 3D 场景中列出材料属性 - 使用 Aspose.3D

## 介绍

如果您需要 **列出 3D 模型的材料属性** 并随后调整诸如漫反射颜色之类的属性，您来对地方了。Aspose.3D for .NET 提供了干净的面向对象 API，让您可以在 C# 代码中检查、检索和修改材料属性。本教程将演示如何加载场景、枚举其材料属性，并更改诸如漫反射分量的值——帮助您为模型赋予理想的外观。

## 快速答案
- **主要目标是什么？** 列出材料属性并修改它们（例如，漫反射颜色）。  
- **需要哪个库？** Aspose.3D for .NET。  
- **我需要许可证吗？** 生产使用需要临时或完整许可证。  
- **支持的文件格式？** FBX、OBJ、STL、STL‑ASCII、3MF 等。  
- **典型实现时间？** 基本属性列出脚本大约需要 10‑15 分钟。

## 什么是 **列出材料属性**？
列出材料属性是指遍历材料的 `PropertyCollection`，读取每个属性名称及其当前值。这对于调试、可视化检查或构建允许用户在运行时调整材料设置的 UI 控件非常有用。

## 为什么使用 Aspose.3D 来 **访问材料属性**？
- **无需外部转换器** – 直接使用原生 .NET 对象。  
- **丰富的属性模型** – 除了标准 PBR 值外，还支持自定义 FBX 特定属性。  
- **跨平台** – 在 .NET Framework、.NET Core 和 .NET 5/6+ 上均可运行。  

## 先决条件

- 在项目中安装 Aspose.3D for .NET。点击[此处](https://releases.aspose.com/3d/net/)下载。  
- 磁盘上的文件夹用于存放 3‑D 源文件（例如，带有嵌入纹理的 FBX 文件）。

现在您已经掌握了基础，让我们深入代码。

## 导入命名空间

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 步骤 1：加载 3D 场景

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## 步骤 2：**访问第一个节点的材料属性**

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## 步骤 3：**列出材料属性** – 查看每个名称/值对

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## 步骤 4：**如何更改漫反射** – 修改 Diffuse 属性

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## 步骤 5：**按名称检索属性** – 获取强类型实例

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## 步骤 6：遍历属性自身的属性（高级）

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## 如何 **在漫反射之外更改 3D 材料颜色**
如果需要影响高光、环境光或自发光颜色，只需在上面的 `props["..."]` 赋值中将 `"Diffuse"` 替换为 `"Specular"` 或 `"Ambient"`。同样适用 `Vector3` 或 `Vector4` 结构。

## 如何 **在 C# 中更新材料颜色**
更改材料的视觉外观归结为在 `PropertyCollection` 中更新相应属性。无论是修改漫反射、高光还是任何自定义颜色属性，步骤都是相同的：

1. 按确切名称（区分大小写）检索属性。  
2. 赋予新的 `Vector3`（RGB）或 `Vector4`（RGBA）值。  

由于 API 直接使用 C# 对象，您可以在 **C# 中更新材料颜色** 的代码时无需任何中间文件或转换器。这使其非常适合实时编辑器或批处理流水线。

## 常见陷阱与技巧
- **属性名称大小写敏感** – Aspose.3D 的属性键区分大小写；请使用列表输出中显示的确切名称。  
- **属性缺失** – 并非所有材料都公开每个 PBR 属性。访问前请检查 `props.ContainsKey("Specular")`。  
- **保存更改** – 修改属性后，调用 `scene.Save("output.fbx");` 以持久化更改。

## 结论

您现在已经学会了使用 Aspose.3D for .NET **列出材料属性**、**按名称检索属性**以及**更改漫反射颜色**（或任何其他材料属性）。尝试不同的属性类型，以微调 3‑D 资产的外观，并记住您只需一行代码即可 **在 C# 中更新材料颜色**。

## 常见问题

### Q1：我可以在 .NET 中使用 Aspose.3D 处理其他 3D 文件格式吗？

A1：是的，Aspose.3D 支持多种 3D 文件格式，包括 FBX、STL 等。

### Q2：如何获取 Aspose.3D for .NET 的临时许可证？

A2：访问[此处](https://purchase.aspose.com/temporary-license/)获取临时许可证。

### Q3：是否有 Aspose.3D 用户的社区论坛？

A3：是的，您可以在 [Aspose.3D 论坛](https://forum.aspose.com/c/3d/18) 找到支持和讨论。

### Q4：在哪里可以找到 Aspose.3D for .NET 的详细文档？

A4：请参考[文档](https://reference.aspose.com/3d/net/)获取全面指导。

### Q5：在购买前我可以免费试用 Aspose.3D for .NET 吗？

A5：当然可以！下载[免费试用版](https://releases.aspose.com/)以体验其功能。

## 常见问答

**问：`Vector3(1, 0, 1)` 表示什么？**  
**答：** 它将漫反射颜色设置为洋红色（线性颜色空间中红=1，绿=0，蓝=1）。

**问：更改属性后需要调用 `scene.Save` 吗？**  
**答：** 是的，持久化场景会将修改写入磁盘；否则更改仅保留在内存中。

**问：我可以枚举自定义 FBX 属性吗？**  
**答：** 当然可以。`PropertyCollection` 会包含所有自定义属性，您可以通过 `GetProperty("customName")` 访问它们。

**问：有没有办法批量更新多个材料？**  
**答：** 遍历 `scene.RootNode.ChildNodes`，对每个材料重复属性修改步骤。

**问：Aspose.3D 支持 .NET 6 吗？**  
**答：** 是的，该库完全兼容 .NET 6 及更高版本。

---

**最后更新：** 2026-03-28  
**测试环境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}