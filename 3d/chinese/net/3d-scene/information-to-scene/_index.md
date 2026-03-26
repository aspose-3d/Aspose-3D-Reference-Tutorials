---
date: 2026-03-26
description: 了解如何向 3D 场景添加供应商信息以及如何使用 Aspose.3D for .NET 保存 FBX 文件。请按照本分步指南，使用可直接运行的代码。
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: 如何使用 Aspose.3D 添加供应商信息并保存 FBX 场景
url: /zh/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用 Aspose.3D 添加供应商信息并保存 FBX 场景

## 介绍

欢迎阅读本完整教程，展示 **如何添加供应商** 详细信息到 3D 场景，并随后 **如何保存 FBX** 文件，使用 Aspose.3D for .NET。无论您是构建建筑可视化、游戏资产还是工程模型，将供应商和应用程序元数据嵌入场景，都能使您的场景信息更丰富，后续管理更便捷。让我们一步步完成整个过程。

## 快速答案
- **“add vendor” 是什么意思？** 它将应用程序和供应商名称存储在场景的 AssetInfo 块中。  
- **哪种格式支持供应商信息？** FBX（ASCII 或二进制）在保存时保留元数据。  
- **如何保存 FBX？** 使用 `scene.Save(path, FileFormat.FBX7500ASCII)` 或其二进制等价方式。  
- **我需要许可证吗？** 免费试用可用于开发；生产环境需要商业许可证。  
- **我可以更改计量单位吗？** 可以，设置 `AssetInfo.UnitName` 和 `AssetInfo.UnitScaleFactor`。

## 在 3D 场景中，“如何添加供应商” 是什么？

添加供应商信息是指为 `Scene` 对象的 `AssetInfo` 属性赋值。这些属性随文件一起保存，使任何读取 FBX 文件的用户都能看到是哪个应用程序创建的以及供应商是谁。

## 为什么要添加供应商信息？

- **可追溯性：** 在大型流水线中快速识别模型的来源。  
- **合规性：** 某些行业要求对资产管理进行明确的供应商标记。  
- **自动化：** 脚本可以根据供应商元数据过滤或处理文件。

## 先决条件

- 已安装 Aspose.3D for .NET。您可以从 [Aspose.3D for .NET 页面](https://releases.aspose.com/3d/net/) 下载。

## 导入命名空间

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 如何添加供应商信息

### 步骤 1：初始化 3D 场景

```csharp
Scene scene = new Scene();
```

创建一个全新的 `Scene` 为您提供一个干净的工作画布。

### 步骤 2：设置应用程序和供应商信息

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

这里我们演示如何通过为 `ApplicationName` 和 `ApplicationVendor` 赋予有意义的字符串来 **添加供应商** 数据。

### 步骤 3：定义计量单位

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

指定单位系统可确保打开 FBX 文件的任何人都能正确解释尺寸。在本例中，1 个 “pole” 等于 60 cm。

## 如何保存 FBX 场景

### 步骤 4：保存场景（如何保存 fbx）

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

此行演示如何使用 FBX 7.5.0 的 ASCII 版本 **保存 fbx**。如果您更喜欢二进制格式，请将 `FBX7500ASCII` 替换为 `FBX7500Binary`。

> **专业提示：** 保持文件扩展名 `.fbx` 与所选格式一致；否则某些查看器可能会误解内容。

### 步骤 5：显示成功信息

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

友好的控制台消息确认场景已连同供应商元数据一起写入磁盘。

## 常见问题及解决方案

| 问题 | 解决方案 |
|-------|----------|
| **查看器中未显示供应商信息** | 确保您将文件保存为 **FBX ASCII** 或 **Binary**；某些旧版查看器只能读取一种格式。 |
| **路径包含空格** | 将路径用引号括起来或使用 `Path.Combine` 构建安全的文件路径。 |
| **单位比例看起来不对** | 仔细检查 `UnitScaleFactor`；它是相对于米的乘数。 |
| **许可证异常** | 使用免费试用进行测试；在生产构建中获取完整许可证。 |

## 常见问题

**问：我可以在其他编程语言中使用 Aspose.3D for .NET 吗？**  
答：Aspose.3D 主要支持 .NET 语言，但您可以探索与其他语言的互操作选项。

**问：Aspose.3D for .NET 是否提供免费试用？**  
答：是的，您可以在[此处](https://releases.aspose.com/)获取免费试用。

**问：如何获取 Aspose.3D 相关查询的支持？**  
答：访问 [Aspose.3D 论坛](https://forum.aspose.com/c/3d/18) 获取社区帮助和支持。

**问：我可以为 Aspose.3D for .NET 购买临时许可证吗？**  
答：是的，您可以在[此处](https://purchase.aspose.com/temporary-license/)获取临时许可证。

**问：在哪里可以找到 Aspose.3D for .NET 的详细文档？**  
答：请参阅[文档](https://reference.aspose.com/3d/net/)获取深入信息。

---

**最后更新：** 2026-03-26  
**测试环境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}