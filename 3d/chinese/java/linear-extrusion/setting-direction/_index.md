---
date: 2025-12-18
description: 学习如何使用 Aspose.3D for Java 创建 3D 场景并保存 OBJ 文件。请按照我们的逐步指南进行线性拉伸方向的操作。
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 创建 3D 场景 – 设置挤出方向 Aspose.3D Java
url: /zh/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 创建 3D 场景 – 设置挤出方向 Aspose.3D Java

## 介绍

在本教程中，您将学习 **如何创建 3d 场景** 对象并使用 Aspose.3D for Java 控制挤出方向。无论您是在构建建筑可视化、产品原型还是游戏资产，掌握线性挤出都能让您快速建模复杂形状。我们将一步步演示，从在 Java 中添加节点到 **导出 3d 模型 obj** 文件，让您即时看到结果。

## 快速回答
- **“创建 3d 场景” 是什么意思？** 它指的是初始化一个 Aspose.3D `Scene` 对象，用于容纳所有几何体、灯光和相机。  
- **如何设置挤出方向？** 在 `LinearExtrusion` 实例上使用 `setDirection(Vector3)` 方法。  
- **应该使用哪种格式导出？** OBJ 格式（`FileFormat.WAVEFRONTOBJ`）在 3‑D 工作流中得到广泛支持。  
- **使用 Aspose.3D 是否需要许可证？** 开发阶段可以使用免费试用版；生产环境需要商业许可证。  
- **可以在 Java 中添加更多节点吗？** 可以——使用 `scene.getRootNode().createChildNode()` 添加任意数量的对象。

## 什么是 “创建 3d 场景” 工作流？

**创建 3d 场景** 工作流从一个空的 `Scene` 对象开始，添加几何体（如挤出轮廓），通过变换定位，最后将场景保存为 OBJ 等文件格式。这一模式是基于 Aspose.3D 构建的大多数 3‑D 应用的核心。

## 为什么要设置挤出方向？

设置挤出方向可以在挤出过程中倾斜、旋转或倾斜形状，从而在无需后期处理的情况下控制最终几何体。它在以下场景中特别有用：

- 创建锥形柱或自定义形状的管道。  
- 将挤出与机械部件中的非标准轴对齐。  
- 为视觉特效生成艺术形状。

## 前置条件

在开始之前，请确保您具备：

- 基础的 Java 知识。  
- 已安装 Aspose.3D 库——可从 [here](https://releases.aspose.com/3d/java/) 下载。  
- 如 Eclipse 或 IntelliJ IDEA 等 IDE。

## 导入包

首先，导入所需的 Aspose.3D 类：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步骤 1：初始化基础轮廓

创建将被挤出的 2‑D 轮廓。本例使用圆角矩形：

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **专业提示：** 调整圆角半径可以控制矩形在挤出前的角部是尖锐还是平滑。

## 步骤 2：创建场景

现在我们 **创建 3d 场景**，用于容纳对象：

```java
Scene scene = new Scene();
```

## 步骤 3：添加节点 Java – 定位对象

我们向场景根节点添加两个子节点（左、右），并将左侧节点稍微向侧面移动：

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步骤 4：如何挤出 – 左节点（默认方向）

在左节点上使用默认 Z 轴方向挤出轮廓。我们还设置了完整的 360° 扭转，并增加切片数以提升平滑度：

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 步骤 5：如何设置方向 – 右节点

这里我们 **如何设置方向**，通过提供自定义 `Vector3`。该向量将挤出倾斜至 (0.3, 0.2, 1)：

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 步骤 6：保存 OBJ 文件 – 导出 3D 模型

最后，我们 **保存 obj 文件**，以便在任意 3‑D 查看器中查看结果：

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

打开生成的 OBJ 文件后，您会看到两个挤出的矩形：一个使用默认方向，另一个按照我们设置的向量倾斜。

## 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| OBJ 文件为空 | 场景未保存或路径错误 | 确认 `MyDir` 指向可写文件夹，且文件名以 `.obj` 结尾。 |
| 挤出看起来扁平 | `setSlices` 设置过低 | 增加 `setSlices`（例如 200）以获得更平滑的几何体。 |
| 方向似乎未改变 | 向量未归一化 | 使用归一化的 `Vector3`，或调整数值以实现期望的倾斜。 |

## 常见问答

### Q1: 我可以在其他编程语言中使用 Aspose.3D 吗？
A1: Aspose.3D 支持多种语言，包括 .NET 和 Java。

### Q2: Aspose.3D 有免费试用吗？
A2: 有，您可以在此处获取免费试用版 [here](https://releases.aspose.com/)。

### Q3: 哪里可以找到 Aspose.3D for Java 的详细文档？
A3: 完整文档可在此查看 [here](https://reference.aspose.com/3d/java/)。

### Q4: 如何获取 Aspose.3D 的支持？
A4: 请访问 [Aspose.3D 论坛](https://forum.aspose.com/c/3d/18) 获取帮助或提问。

### Q5: Aspose.3D 是否提供临时许可证？
A5: 有，您可以在此获取临时许可证 [here](https://purchase.aspose.com/temporary-license/)。

---

**最后更新：** 2025-12-18  
**测试环境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}