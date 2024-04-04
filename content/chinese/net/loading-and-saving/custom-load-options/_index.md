---
title: 自定义加载选项
linktitle: 自定义加载选项
second_title: Aspose.3D .NET API
description: 探索 Aspose.3D for .NET 无缝 3D 模型加载和保存的终极解决方案。
type: docs
weight: 15
url: /zh/net/loading-and-saving/custom-load-options/
---
## 介绍

欢迎来到 Aspose.3D for .NET 的世界——一个强大的库，使开发人员能够无缝地处理 3D 文件。在本教程中，我们将深入研究加载和保存 3D 模型的复杂性，重点关注自定义加载选项。无论您是经验丰富的开发人员还是新手，本指南都将逐步引导您完成整个过程，确保您充分利用 Aspose.3D for .NET 的全部潜力。

## 先决条件

在我们开始这一旅程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET：确保您已安装该库。你可以下载它[这里](https://releases.aspose.com/3d/net/).

- 文档目录：创建一个目录来存储 3D 模型文件。

现在您已经掌握了必需的知识，让我们深入了解 3D 模型操作的激动人心的世界吧！

## 导入命名空间

首先，让我们导入必要的名称空间。这将为我们进入 Aspose.3D 领域奠定基础。

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## 加载和保存 - 自定义加载选项

### 第 1 步：加载 Discreet3DS 文件

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //设置自定义选项
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //使用加载选项加载文件
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### 第2步：加载OBJ文件

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //设置自定义选项
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //使用加载选项加载文件
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### 第3步：加载STL文件

```csharp
private static void STLLoadOption()
{
    //文档目录的路径。
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //设置自定义选项
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //使用加载选项加载文件
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### 第4步：加载U3D文件

```csharp
private static void U3DLoadOption()
{
    //文档目录的路径。
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //设置自定义选项
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //使用加载选项加载文件
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### 第5步：加载glTF文件

```csharp
private static void glTFLoadOptions()
{
    //文档目录的路径。
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //设置自定义选项
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### 第6步：加载PLY文件

```csharp
private static void PlyLoadOptions()
{
    //文档目录的路径。
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //设置自定义选项
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### 第7步：加载FBX文件

```csharp
private static void FBXLoadOptions()
{
    //文档目录的路径。
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //设置自定义选项
    scene.Open("test.FBX", opt);

    //FBX 文件中 GlobalSettings 中定义的输出属性
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## 结论

恭喜！您已成功浏览使用 Aspose.3D for .NET 加载和保存 3D 模型的复杂世界。本教程涵盖了各种文件格式及其自定义加载选项，使您能够轻松操作 3D 资源。

## 常见问题解答

### Q1：Aspose.3D for .NET适合初学者吗？

A1：当然！ Aspose.3D for .NET 提供了用户友好的界面，使各个级别的开发人员都可以使用它。

### Q2：我可以将Aspose.3D用于商业项目吗？

A2：是的，Aspose.3D for .NET 附带商业许可证，允许您在项目中使用它。

### Q3：支持的文件格式有限制吗？

 A3：Aspose.3D for .NET 支持多种流行的 3D 文件格式，包括 OBJ、STL、FBX 等。请参阅[文档](https://reference.aspose.com/3d/net/)以获得完整的列表。

### Q4：有试用版吗？

A4：是的，您可以通过下载 Aspose.3D for .NET 来探索 Aspose.3D for .NET 的功能[免费试用](https://releases.aspose.com/).

### Q5：在哪里可以寻求 Aspose.3D for .NET 支持？

 A5：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以获得社区的支持和帮助。