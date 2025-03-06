---
title: 在 3D 场景中设置三维属性
linktitle: 在 3D 场景中设置三维属性
second_title: Aspose.3D .NET API
description: 探索有关设置 3D 属性的 Aspose.3D for .NET 教程。通过代码示例逐步学习。提高您的 3D 场景操作技能。
weight: 14
url: /zh/net/3d-scene/set-3d-properties/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 3D 场景中设置三维属性

## 介绍

创建迷人的三维场景通常需要能够操纵各种属性，为您的项目添加深度和真实感。 Aspose.3D for .NET 提供了强大的工具集来实现此目的，使您可以轻松地在 3D 场景中设置和修改三维属性。在本教程中，我们将逐步探索该过程，增强您对如何有效利用 Aspose.3D for .NET 的理解。

## 先决条件

在深入学习本教程之前，请确保您满足以下先决条件：

-  Aspose.3D for .NET：确保您已在 .NET 项目中安装了该库。你可以下载它[这里](https://releases.aspose.com/3d/net/).

- 文档目录：创建一个目录来存储您的 3D 文档。

现在您已经掌握了要点，让我们探索使用 Aspose.3D for .NET 在 3D 场景中设置三维属性的过程。

## 导入命名空间

首先，将必要的命名空间导入到您的项目中。这些命名空间提供了在 Aspose.3D for .NET 中处理三维属性所需的类和方法。

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

## 第 1 步：加载 3D 场景

首先加载 3D 场景。在此示例中，我们使用带有嵌入纹理的 FBX 文件。

```csharp
//ExStart：加载3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd：加载3DScene
```

## 第 2 步：访问材料属性

访问加载的 3D 场景的材质属性以操纵其特性。

```csharp
//ExStart：访问材料属性
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//结束：访问材料属性
```

## 第 3 步：列出所有属性

使用 foreach 循环或序数 for 循环列出材质的所有属性。

```csharp
//ExStart：列出所有属性
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//或使用序数 for 循环
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//结束：列出所有属性
```

## 步骤 4：按名称获取和修改属性

按名称检索和修改特定属性。

```csharp
//ExStart：GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//按名称修改属性值
props["Diffuse"] = new Vector3(1, 0, 1);
//结束：GetModifyPropertyByName
```

## 第5步：按名称获取属性实例

按名称检索属性实例以进行进一步操作。

```csharp
//ExStart：GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//结束：按名称获取属性实例
```

## 第6步：遍历Property的属性

自从`Property`继承自`A3DObject`，可以遍历一个属性的属性。

```csharp
//ExStart：TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//以及一些仅在 FBX 文件中定义的属性：
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//可以遍历财产的财产
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//结束：TraverseProperty属性
```

## 结论

恭喜！您现在已经掌握了使用 Aspose.3D for .NET 在 3D 场景中设置三维属性的艺术。尝试不同的属性和值，让您的 3D 项目栩栩如生。

## 常见问题解答

### Q1：我可以将 Aspose.3D for .NET 与其他 3D 文件格式一起使用吗？

A1：是的，Aspose.3D 支持各种 3D 文件格式，包括 FBX、STL 等等。

### Q2：如何获得 Aspose.3D for .NET 的临时许可证？

 A2：参观[这里](https://purchase.aspose.com/temporary-license/)获得临时许可证。

### Q3：有 Aspose.3D 用户的社区论坛吗？

 A3：是的，您可以在以下位置找到支持和讨论：[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18).

### Q4：在哪里可以找到 Aspose.3D for .NET 的详细文档？

 A4：请参阅[文档](https://reference.aspose.com/3d/net/)进行全面指导。

### Q5：我可以在购买前免费试用 Aspose.3D for .NET 吗？

 A5：当然！下载[免费试用版](https://releases.aspose.com/)来探索它的特点。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
