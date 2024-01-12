---
title: 加载和保存 - 保存 3D 场景
linktitle: 加载和保存 - 保存 3D 场景
second_title: Aspose.3D .NET API
description: 探索 Aspose.3D for .NET 的强大功能。用于无缝 3D 场景操作的多功能库。轻松加载、保存和压缩。
type: docs
weight: 20
url: /zh/net/loading-and-saving/save-3d-scene/
---
## 介绍

欢迎来到使用 Aspose.3D for .NET 进行 3D 场景操作领域的激动人心的旅程！无论您是经验丰富的开发人员还是好奇的爱好者，本教程都将指导您轻松完成加载、保存和压缩 3D 场景的过程。

## 先决条件

在深入 3D 场景操作的迷人世界之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET：从以下位置下载并安装 Aspose.3D 库：[下载链接](https://releases.aspose.com/3d/net/).
- 文档：通过全面的文档熟悉库的功能[文档](https://reference.aspose.com/3d/net/).
- 您的输出目录：设置一个目录来存储教程期间生成的输出文件。

## 导入命名空间

让我们通过将必要的命名空间导入到 .NET 环境中来开始我们的探索：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## 加载和保存 - 保存 3D 场景

### 第 1 步：加载 3D 文档

```csharp
Scene scene = new Scene();
scene.Open(RunExamples.GetDataFilePath("document.fbx"));
```

在这一步中，我们创建一个新的`Scene`对象并使用以下命令加载现有的 3D 文档`Open`方法。

### 第 2 步：将场景保存到流中

```csharp
MemoryStream dstStream = new MemoryStream();
scene.Save(dstStream, FileFormat.FBX7500ASCII);
```

使用以下命令将加载的 3D 场景保存到内存流`Save`方法，指定所需的文件格式（在本例中为 FBX7500ASCII）。

### 第 3 步：倒回流位置

```csharp
dstStream.Position = 0;
```

重置流位置以为下一个读取器做好准备，确保无缝处理。

### 步骤 4：将场景保存到本地路径

```csharp
scene.Save("Your Output Directory" + "output_out.fbx", FileFormat.FBX7500ASCII);
```

将 3D 场景保存到本地路径，提供有意义的输出目录和文件名。

## 压缩

现在，让我们探索 3D 场景的压缩选项。

### 第 1 步：加载 3D 文档

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("document.fbx"));
```

与前面的示例类似，将 3D 文档加载到`Scene`目的。

### 第 2 步：禁用压缩并保存

```csharp
scene.Save("Your Output Directory" + "UncompressedDocument.fbx", new FbxSaveOptions(FileFormat.FBX7500ASCII) { EnableCompression = false });
```

保存 3D 场景时禁用压缩，提供清晰的输出路径和文件名。

## 结论

在本教程中，我们深入研究了使用 Aspose.3D for .NET 加载、保存和压缩 3D 场景的基本方面。掌握了这些知识，您就可以开始自己的 3D 之旅，并在 Aspose.3D 领域释放创意的可能性。

## 常见问题解答

### Q1：Aspose.3D 是否兼容各种3D 文件格式？

A1：是的，Aspose.3D 支持多种 3D 文件格式，为您的项目提供灵活性。

### Q2：我可以将 Aspose.3D 与其他 .NET 库集成吗？

A2：当然！ Aspose.3D 与其他 .NET 库无缝集成，增强了应用程序的功能。

### Q3：如何获得 Aspose.3D 的临时许可？

 A3：访问[临时执照](https://purchase.aspose.com/temporary-license/) Aspose 网站上的页面以获得临时许可证。

### Q4：我可以在哪里寻求帮助或与社区联系？

 A4：加入充满活力的 Aspose.3D 社区[论坛](https://forum.aspose.com/c/3d/18)寻求支持、分享经验并与其他爱好者合作。

### Q5：Aspose.3D 有免费试用版吗？

 A5：是的，通过抓住您的[免费试用](https://releases.aspose.com/)今天！