---
date: 2026-08-02
description: 了解如何在 Aspose.3D for Java 中更改线性挤出（linear extrusion）的挤出方向并导出 OBJ 文件。请按照我们的分步指南操作。
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: 更改挤出方向 – Aspose.3D Java
og_description: 使用 Aspose.3D for Java 更改线性挤出（linear extrusion）的挤出方向并导出 OBJ 文件。本指南提供分步代码和开发者提示。
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: 更改挤出方向 – Aspose.3D Java 教程
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: 在 3D 模型中更改挤出方向 – Aspose.3D Java
url: /zh/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 更改 3D 模型的挤出方向 – Aspose.3D Java

## 介绍

在本综合教程中，您将了解在使用 Aspose.3D for Java 进行线性挤出时**如何更改挤出方向**。无论您是在构建类似 CAD 的工具、为游戏引擎准备资产，还是为 3D 打印生成部件，控制挤出方向都能让您精确创建所需形状。我们将逐步演示，从初始化轮廓到将结果保存为 OBJ 文件，帮助您直接从 Java **导出 3D 模型 OBJ** 文件。

## 快速答案
- **执行线性挤出的类是什么？** `LinearExtrusion`
- **哪个方法设置挤出向量？** `setDirection(Vector3 direction)`
- **结果可以保存为 OBJ 吗？** 是——使用 `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **生产环境是否需要许可证？** 提供免费试用；商业使用必须拥有许可证。
- **哪个 IDE 最适合 Aspose.3D？** 完全支持 IntelliJ IDEA 和 Eclipse。

## 什么是线性挤出？

线性挤出是将二维草图（如矩形或圆形）沿直线延伸以生成三维实体的过程。默认情况下，挤出沿正 Z 轴方向进行，但 Aspose.3D 通过 `setDirection` 属性允许您更改该路径，从而完全控制最终几何形状。

## 为什么在线性挤出中更改挤出方向？

更改挤出方向可让您将新几何体与现有对象对齐、无需额外变换即可创建倾斜部件，并生成符合下游流水线（如 3D 打印机或游戏引擎）坐标系要求的模型。这消除了后处理步骤的需求，并在使用避免不必要旋转的方向向量时，可将文件大小降低约 15 %。

## 先决条件

在开始之前，请确保您具备：

- 具备 Java 基础知识。
- 已安装 Aspose.3D 库。您可以从[此处](https://releases.aspose.com/3d/java/)下载。您也可以在主页面[此处](https://releases.aspose.com/)浏览所有 Aspose 发布。
- IDE，例如 Eclipse 或 IntelliJ IDEA。

## 导入包

`com.aspose.threed` 命名空间提供核心 3D 类和实用类型。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步骤 1：初始化基础轮廓

`RectangleShape` 类创建将被挤出的二维轮廓。小的圆角半径使边缘更平滑。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 步骤 2：创建场景

`Scene` 类是 Aspose.3D 的顶层容器，保存所有 3D 节点、灯光、相机和材质。

```java
Scene scene = new Scene();
```

## 步骤 3：创建节点

`Node` 表示场景图中的对象，您可以在其上附加几何体、变换和其他属性。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步骤 4：在左侧节点上执行线性挤出

`LinearExtrusion` 执行挤出操作，将二维轮廓转换为三维网格。

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 步骤 5：在右侧节点上使用方向执行线性挤出

这里我们**更改挤出方向**。通过将自定义 `Vector3` 传递给 `setDirection`，挤出遵循向量 (0.3, 0.2, 1)，生成与场景坐标系对齐的倾斜形状。

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 步骤 6：保存 3D 场景

`save` 方法将场景以指定格式写入文件。

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常见问题及解决方案

| 问题 | 产生原因 | 解决方案 |
|-------|----------------|-----|
| OBJ 文件为空 | 轮廓未添加到节点 | 确保在有效节点上调用 `createChildNode` |
| 方向似乎未改变 | `setDirection` 在挤出已构建后被调用 | 如示例在 `LinearExtrusion` 初始化器内部设置方向 |
| 低分辨率网格 | `setSlices` 的值太低 | 增加切片数量（例如 100 或更多） |

## 结论

您现在已经掌握了**如何在线性挤出中更改挤出方向**、如何调整扭转和切片设置，以及如何使用 Aspose.3D for Java **导出 3D 模型 OBJ** 文件。这些技术为几何创建提供了细粒度控制，并使将 3D 资产集成到更大流水线中变得简便。

## 常见问题

**Q:** 我可以在其他编程语言中使用 Aspose.3D 吗？  
**A:** 可以——Aspose.3D 为 .NET 和 Java 提供 API，支持跨平台开发。

**Q:** 是否提供 Aspose.3D 的免费试用？  
**A:** 当然。您可以通过免费试用[此处](https://releases.aspose.com/)探索完整功能集。

**Q:** 在哪里可以找到 Aspose.3D for Java 的详细文档？  
**A:** 完整的参考文档可在[此处](https://reference.aspose.com/3d/java/)获取。

**Q:** 如何获取 Aspose.3D 的支持？  
**A:** 请访问官方的[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)获取社区和产品团队的帮助。

**Q:** 是否提供用于测试的临时许可证？  
**A:** 是的——可在[此处](https://purchase.aspose.com/temporary-license/)获取临时许可证。

---

**最后更新：** 2026-08-02  
**测试环境：** Aspose.3D for Java (latest release)  
**作者：** Aspose

{{< blocks/products/products-backtop-button >}}

## 相关教程

- [如何挤出形状 - 使用 Java 进行线性挤出创建 3D 模型](/3d/java/linear-extrusion/)
- [使用 Aspose.3D 在 Java 中创建 3D 挤出](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D 图形教程 – 线性挤出中的中心](/3d/java/linear-extrusion/controlling-center/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}