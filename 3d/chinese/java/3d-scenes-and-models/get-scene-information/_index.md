---
date: 2026-09-08
description: 了解如何使用 Aspose.3D 在 Java 中定义单位并导出场景为 FBX。本分步指南展示了设置应用程序名称、测量单位以及获取 3D
  场景信息的过程。
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: 如何在 Java 中保存 FBX 并获取 3D 场景信息
og_description: 了解如何使用 Aspose.3D 在 Java 中定义单位并导出场景为 FBX。指南涵盖了设置应用程序名称、测量单位以及在几步内获取
  3D 场景信息。
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: 如何在 Java 中定义单位并导出场景为 FBX
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: 如何在 Java 中定义单位并导出场景为 FBX
url: /zh/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Java 中定义单位并导出场景为 FBX

## 介绍

如果您正在寻找一份关于 **如何定义单位** 和 **导出场景为 FBX** 的清晰、动手指南，同时从 3D 场景中提取有用的元数据，那么您来对地方了。在本教程中，我们将使用 **Aspose.3D for Java** 库逐步演示：从创建场景、**设置应用程序名称**、**定义测量单位**，到最终 **导出场景为 FBX**。完成后，您将拥有一个可直接使用的 FBX 文件，携带下游流水线所需的资产信息。

## 快速答案

- **主要目标是什么？** 导出一个包含自定义资产信息的 FBX 场景。  
- **使用的库是什么？** Aspose.3D for Java。  
- **我需要许可证吗？** 免费试用可用于开发；生产环境需要商业许可证。  
- **我可以更改测量单位吗？** 可以——使用 `setUnitName` 和 `setUnitScaleFactor`。  
- **输出保存在哪里？** 保存到您在 `scene.save(...)` 中指定的路径。  

## 先决条件

在开始之前，请确保您拥有：

- 对核心 Java 语法的扎实掌握。  
- 已下载并添加到项目中的 **Aspose.3D for Java**（您可以从官方获取）[Aspose 3D 下载页面](https://releases.aspose.com/3d/java/)。  
- 正确配置的您喜欢的 Java IDE（IntelliJ IDEA、Eclipse、NetBeans 等）。

## 导入包

在您的 Java 源文件中，导入提供场景处理和文件格式支持的 Aspose.3D 类。

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **专业提示：** 保持 import 列表最小化，以避免不必要的依赖并提升编译速度。

## 保存 FBX 文件的流程是什么？

要将场景保存为 FBX 文件，您需要创建一个 `Scene`，设置所需的资产元数据，定义测量单位，然后调用 `scene.save(path, FileFormat.FBX7500ASCII)`。此过程会将几何体、材质和元数据写入可供下游工具检查或导入的 ASCII FBX。

### 步骤 1：初始化 3D 场景

`Scene` 类是 Aspose.3D 的顶层容器，表示整个 3D 场景，包括几何体、灯光、相机和元数据。首先，创建一个空的 `Scene` 对象。它将作为所有几何体、灯光、相机和资产元数据的容器。

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### 如何在 Java 中设置应用程序名称

`AssetInfo` 对象存储场景的元数据，如应用程序名称、供应商和版本。添加自定义元数据有助于下游工具识别文件来源。使用 `AssetInfo` 对象在保存文件之前 **设置应用程序名称**（以及供应商）。

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **为什么重要：** 许多流水线会根据来源应用程序对资产进行过滤或标记，这一步对大型项目至关重要。

### 步骤 3：定义测量单位

单位系统决定场景的真实世界比例；Aspose.3D 允许您指定单位名称以及相对于米的比例因子。在本例中，我们使用一种古埃及单位 “pole”，并设置自定义比例因子。

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **提示：** 调整 `unitScaleFactor` 以匹配模型的真实尺寸；1.0 表示与所选单位的 1:1 映射。

### 步骤 4：导出场景为 FBX

现在资产信息已附加，我们将场景保存为 FBX 文件。`FileFormat.FBX7500ASCII` 选项会生成可读的 ASCII FBX，便于调试。

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **请记住：** 将 `"Your Document Directory"` 替换为绝对路径或相对于项目工作目录的路径。

## 为什么使用 Aspose.3D 导出场景为 FBX？

Aspose.3D 支持 **50 多种输入和输出格式**，并且能够在不将整个文件加载到内存的情况下处理数百页的场景，让您完全控制导出文件的元数据、单位和几何体，而无需使用重量级的 3D 创作应用程序。这使得自动化资产生成、批处理以及服务器端转换既快速又可靠。

## 常见使用场景

- **游戏资产流水线** – 将创作者信息直接嵌入 FBX 文件，以便进行版本追踪。  
- **建筑可视化** – 存储项目特定的单位，以避免在导入渲染引擎时出现缩放错误。  
- **自动化报告** – 动态生成带有元数据的 FBX 文件，供下游分析工具读取。  
- **基于云的 3D 服务** – 通过编程方式创建并导出场景，无需 GUI，适合 SaaS 平台。  

## 故障排除与技巧

| 问题 | 解决方案 |
|-------|----------|
| **保存后文件未找到** | 确认 `MyDir` 指向一个已存在的文件夹，并且您的应用程序具有写入权限。 |
| **外部查看器中单位显示不正确** | 再次检查 `unitScaleFactor`；某些查看器将米作为基准单位。 |
| **资产元数据缺失** | 确保在保存之前调用 `scene.getAssetInfo()`；在 `save()` 之后所做的更改不会被保留。 |
| **大型场景的性能瓶颈** | 在保存之前使用 `scene.optimize()` 以降低内存使用。 |
| **ASCII FBX 文件过大** | 通过使用 `FileFormat.FBX7500` 切换为二进制 FBX（参见 FAQ）。 |

## 常见问题

**问：如何将输出格式更改为二进制 FBX？**  
**答：** 在调用 `scene.save(...)` 时，将 `FileFormat.FBX7500ASCII` 替换为 `FileFormat.FBX7500`。

**问：我可以在内置资产字段之外添加自定义用户元数据吗？**  
**答：** 可以，使用 `scene.getUserData().add("Key", "Value")` 来嵌入额外的键值对。

**问：Aspose.3D 是否支持其他导出格式，如 OBJ 或 GLTF？**  
**答：** 支持。只需将 `FileFormat` 枚举更改为 `OBJ` 或 `GLTF2` 即可。

**问：需要哪个版本的 Java？**  
**答：** Aspose.3D for Java 支持 Java 8 及以上版本。

**问：是否可以加载已有的 FBX，修改其资产信息后重新保存？**  
**答：** 完全可以。使用 `new Scene("input.fbx")` 加载文件，修改 `scene.getAssetInfo()`，然后保存。

---

**最近更新：** 2026-09-08  
**测试环境：** Aspose.3D for Java 24.11  
**作者：** Aspose

## 相关教程

- [减小 3D 文件大小 – 使用 Aspose.3D for Java 压缩场景](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [如何在 Java 中设置 vector3 颜色：使用 Aspose.3D 更改漫反射颜色并管理 Java 场景中的 3D 属性](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}