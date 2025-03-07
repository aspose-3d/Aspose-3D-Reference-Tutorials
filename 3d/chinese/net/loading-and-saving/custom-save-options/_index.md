---
title: 自定义保存选项
linktitle: 自定义保存选项
second_title: Aspose.3D .NET API
description: 探索 Aspose.3D for .NET 的强大功能。了解如何通过 Collada、USD、3DS、FBX、OBJ、STL、U3D、glTF、DRC 和 RVM 格式的分步指南自定义 3D 场景保存。
weight: 21
url: /zh/net/loading-and-saving/custom-save-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 自定义保存选项

## 介绍

欢迎来到 Aspose.3D for .NET 的世界！如果您希望增强 3D 开发能力，那么您来对地方了。在本教程中，我们将深入探讨加载和保存功能，特别关注自定义保存选项。 Aspose.3D for .NET 是一个功能强大的库，使开发人员能够有效地操作和保存 3D 场景。

## 先决条件

在我们开始探索 Aspose.3D 令人兴奋的功能之前，请确保您具备以下先决条件：

- 对 C# 和 .NET 开发有基本了解。
- 安装了 Aspose.3D for .NET 库。您可以从[发布页面](https://releases.aspose.com/3d/net/).
- 使用 Visual Studio 或任何其他首选 C# IDE 设置的开发环境。

## 导入命名空间

首先，让我们导入必要的命名空间：

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

现在我们已经做好了准备，让我们将教程分解为多个步骤。

## 第 1 步：Collada 保存选项

让我们从 Collada 开始，这是一种流行的 3D 文件格式。请按照以下步骤自定义 Collada 保存选项：

### 1. 设置目录：
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. 初始化 Collada 保存选项：
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. 配置选项：
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## 第 2 步：谨慎的 3DS 保存选项

现在，让我们探索 Discreet 3DS 及其自定义选项：

### 1. 设置目录：
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. 初始化 3DS 保存选项：
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. 配置选项：
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   //附加配置选项...
   ```

对 FBX、OBJ、STL、U3D、glTF 和 DRC 保存选项继续此分步方法，根据您的要求自定义每个选项。

## 第 3 步：glTF 保存选项

现在，让我们关注 glTF，一种广泛用于 Web 和移动应用程序的格式。通过以下步骤自定义 glTF 保存选项：

### 1.初始化场景对象：
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. 设置 glTF 保存选项：
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3.保存glTF文件：
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

其他保存选项（例如 DRC 和 RVM）遵循类似的结构。

## 结论

恭喜！您已成功探索了 Aspose.3D for .NET 中的自定义保存选项。这个强大的库提供了无数的选项来定制您的 3D 场景保存过程。

## 常见问题解答

### Q1：我可以将 Aspose.3D for .NET 与其他 .NET 框架一起使用吗？

A1：是的，Aspose.3D 与各种.NET 框架兼容，确保您的开发环境的灵活性。

### 问题 2：Aspose.3D 有可用的许可选项吗？

 A2：是的，您可以探索许可选项[这里](https://purchase.aspose.com/buy).

### Q3：在哪里可以找到对 Aspose.3D 相关查询的支持？

 A3：您可以通过以下方式寻求支持[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18).

### Q4：有免费试用吗？

A4：是的，您可以免费试用[这里](https://releases.aspose.com/).

### Q5：如何获得Aspose.3D的临时许可证？

 A5：获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
