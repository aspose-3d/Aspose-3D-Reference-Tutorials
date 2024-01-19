---
title: 将信息提取到场景资产
linktitle: 将信息提取到场景资产
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 轻松增强您的 3D 场景。学习逐步添加有价值的资产信息。立即下载以获得动态 3D 体验。
type: docs
weight: 10
url: /zh/net/asset-information/information-to-scene/
---
## 介绍

欢迎阅读这个关于使用 Aspose.3D for .NET 提取有价值的信息并增强 3D 场景的综合教程。 Aspose.3D 是一个功能强大的库，使开发人员能够在 .NET 应用程序中无缝操作 3D 场景。在本教程中，我们将重点关注向场景添加资产信息的关键任务。

## 先决条件

在我们深入学习本教程之前，请确保您满足以下先决条件：

- Aspose.3D for .NET：确保您已安装该库。您可以从[Aspose.3D for .NET 页面](https://releases.aspose.com/3d/net/).

## 导入命名空间

在您的 .NET 项目中，请确保包含访问 Aspose.3D 功能所需的命名空间：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 第 1 步：初始化 3D 场景

```csharp
Scene scene = new Scene();
```

使用创建一个新的 3D 场景`Scene`班级。

## 第 2 步：设置应用程序和供应商信息

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

定义与您的 3D 场景关联的应用程序和供应商名称。

## 步骤 3：定义测量单位

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

指定场景中使用的测量单位。在此示例中，我们使用称为“杆”的古埃及单位，1 杆等于 60 厘米。

## 第 4 步：保存场景

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

将添加了资产信息的场景保存为 3D 支持的文件格式。根据需要调整输出目录。

## 第5步：显示成功消息

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

通知用户资产信息已成功添加，并保存文件。

## 结论

恭喜！您已成功学习如何使用 Aspose.3D for .NET 提取基本资产信息并将其添加到 3D 场景中。这些知识为创建信息丰富、引人入胜的 3D 内容开辟了无限的可能性。

## 常见问题解答

### Q1：我可以将 Aspose.3D for .NET 与其他编程语言一起使用吗？

A1：Aspose.3D 主要支持 .NET 语言，但您可以探索其他语言的互操作性选项。

### 问题 2：Aspose.3D for .NET 是否有免费试用版？

A2：是的，您可以免费试用[这里](https://releases.aspose.com/).

### Q3：如何获得 Aspose.3D 相关查询的支持？

 A3：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以获得社区和支持。

### Q4：我可以购买 Aspose.3D for .NET 的临时许可证吗？

 A4：是的，您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).

### Q5：在哪里可以找到 Aspose.3D for .NET 的详细文档？

 A5：请参阅[文档](https://reference.aspose.com/3d/net/)以获得深入的信息。