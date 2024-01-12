---
title: 加载和保存 - 使用 CancellationToken
linktitle: 加载和保存 - 使用 CancellationToken
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 建模的无缝世界。了解使用 CancellationToken 高效加载和保存 3D 文档。
type: docs
weight: 10
url: /zh/net/loading-and-saving/cancellation-token/
---
## 介绍

欢迎阅读我们关于利用 Aspose.3D for .NET 来增强您的 3D 建模和渲染项目的综合指南。 Aspose.3D 是一个功能强大的库，使 .NET 开发人员能够无缝地处理 3D 文件。在本教程中，我们将深入研究加载和保存方面，特别关注如何使用 CancellationToken 来高效管理异步任务。

## 先决条件

在我们开始这一旅程之前，请确保您具备以下先决条件：

-  Aspose.3D for .NET：从以下位置下载并安装该库[这里](https://releases.aspose.com/3d/net/).
- .NET 环境：确保您设置了兼容的 .NET 开发环境。
- 对 C# 的基本了解：建议熟悉 C# 编程语言。

## 导入命名空间

首先，请确保您的项目中包含必要的命名空间。这些命名空间将提供对 3D 文件操作所需功能的访问。

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## 加载和保存 - 使用 CancellationToken

### 第 1 步：创建 CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

在这里，我们实例化一个 CancellationTokenSource，它是管理异步操作中取消的关键组件。

### 第 2 步：初始化 3D 场景

```csharp
Scene scene = new Scene();
```

创建 Scene 类的实例。这将成为您进行 3D 建模活动的画布。

### 第 3 步：设置 CancellationToken 超时

```csharp
cts.CancelAfter(1000);
```

使用以下命令设置取消超时`CancelAfter`方法。在此示例中，超时设置为 1000 毫秒（1 秒）。

### 第 4 步：打开 3D 文档

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

尝试在指定的时间范围内打开 3D 文档。这`cts.Token`参数确保如果超过设置的超时时间可以取消操作。

### 第5步：处理导入异常

如果出现 ImportException，请通过检查它是否是由 OperationCanceledException 引起的来优雅地处理它。

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## 结论

恭喜！您已成功完成使用 Aspose.3D for .NET 和 CancellationToken 来管理 3D 文档加载的过程。该技术可确保高效、及时的导入操作，从而增强 3D 应用程序的整体性能。

## 常见问题解答

### Q1：Aspose.3D 是否兼容所有 3D 文件格式？

 A1：Aspose.3D 支持多种 3D 文件格式，包括 FBX、STL、OBJ 等。请参阅[文档](https://reference.aspose.com/3d/net/)获取完整列表。

### Q2：如何获得 Aspose.3D 的临时许可证？

 A2：通过访问获得临时许可证[这个链接](https://purchase.aspose.com/temporary-license/).

### Q3：哪里可以找到对 Aspose.3D 的支持？

 A3：加入社区讨论[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18).

### Q4：购买前可以免费试用Aspose.3D吗？

 A4：是的，可以通过免费试用来探索功能[这里](https://releases.aspose.com/).

### Q5：Aspose.3D for .NET 的最新版本是什么？

 A5：查看最新信息[下载页面](https://releases.aspose.com/3d/net/)获取最新版本。