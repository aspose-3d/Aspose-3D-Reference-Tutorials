---
date: 2026-06-13
description: 学习使用 Aspose.3D 在 java 中进行 3D 图形教程，控制线性挤压中的中心，包括如何设置 rounding radius 并保存
  OBJ 文件。
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: 使用 Aspose.3D for Java 控制线性挤压中的中心
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: 创建 3D Mesh Java – 线性挤压中的中心
url: /zh/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 创建 3D 网格 Java – 线性拉伸中的中心

## 介绍

如果您正在使用 Java 构建 3‑D 可视化，掌握拉伸技术至关重要。此 **java 3d graphics tutorial** 向您展示如何通过 Aspose.3D for Java 控制线性拉伸的中心来 **create 3d mesh java** 对象。阅读本指南后，您将了解 `center` 属性为何重要，如何 **set rounding radius**，以及如何 **save obj file java** 兼容的输出。您还将看到如何 **export 3d model obj** 以在任何主流 3‑D 编辑器中使用。

## 快速答案
- **center 属性有什么作用？** 它决定拉伸是否相对于轮廓原点对称。  
- **运行代码是否需要许可证？** 临时许可证可用于测试；生产环境需要完整许可证。  
- **结果使用哪种文件格式？** 场景保存为 Wavefront OBJ 文件。  
- **我可以更改切片数量吗？** 可以，在 `LinearExtrusion` 对象上使用 `setSlices(int)`。  
- **Aspose.3D 是否兼容 Java 8+？** 当然——它支持所有现代 Java 版本。

## 什么是 java 3d graphics tutorial？
一个 **java 3d graphics tutorial** 是一步步的指南，教您如何使用 Java 库来创建、操作和渲染三维对象。在本教程中，您将学习通过将 2‑D 轮廓转换为完整的 3‑D 模型来 **create 3d mesh java**，控制其中心对齐，圆化拉伸角，并最终将结果导出为任何 3‑D 程序都能读取的 OBJ 文件。

## 为什么使用 Aspose.3D for Java？
Aspose.3D for Java 提供了高级 API，消除了手动网格计算的需求，让您专注于设计而不是底层几何。它支持 **50+ input and output formats**——包括 OBJ、FBX、STL 和 GLTF——因此您可以通过一次方法调用 **export 3d model obj** 或任何其他格式。该库能够在不将整个文件加载到内存的情况下处理数百页的场景，在典型服务器硬件上相比原始 OpenGL 管线提供 **up to 3× faster performance**。

## 先决条件

在开始之前，请确保您拥有：

1. **Java Development Environment** – 已安装 JDK 8 或更高版本。  
2. **Aspose.3D for Java** – 在此下载库和文档 [here](https://reference.aspose.com/3d/java/)。  
3. **Document Directory** – 在您的机器上创建一个文件夹用于存放生成的文件，我们将其称为 **“Your Document Directory.”**

## 导入包

在您的 Java IDE 中，导入所需的 Aspose.3D 类。这为编译器提供对拉伸和场景构建功能的访问。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 分步指南

### 步骤 1：设置基础轮廓

首先，创建将要被拉伸的 2‑D 形状。这里我们使用矩形并 **set rounding radius** 为 0.3，以平滑角并演示如何 **round extrusion corners**。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### 步骤 2：创建 3D 场景

**Scene** 是顶层容器，保存所有 3‑D 对象、灯光和相机。

```java
Scene scene = new Scene();
```

### 步骤 3：添加左侧和右侧节点

**Node** 表示场景图中的可变换对象，允许定位和层级结构。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 步骤 4：线性拉伸 – 无中心（左节点）

**LinearExtrusion** 将 2‑D 轮廓沿直线扫掠生成 3‑D 网格。**setCenter(boolean)** 用于切换拉伸是否以轮廓原点为中心。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### 步骤 5：添加参考地面平面（左节点）

一个薄盒子充当可视化地面，帮助您观察拉伸的方向。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### 步骤 6：线性拉伸 – 居中（右节点）

现在重复拉伸，这次启用 `center`。几何体将在轮廓原点周围对称，从而得到完美平衡的 **create 3d mesh java** 结果。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### 步骤 7：添加参考地面平面（右节点）

右侧使用相同的地面平面，以便清晰对比。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### 步骤 8：保存 3D 场景

最后，将整个场景导出为 Wavefront OBJ 文件——这是一种可在大多数 3‑D 编辑器中直接使用的格式。`save` 方法会自动将网格转换为 OBJ 规范，使您能够 **save obj file java** 而无需额外后处理。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常见问题及解决方案

| 问题 | 原因 | 解决方案 |
|-------|----------------|-----|
| **拉伸出现偏移** | `setCenter(false)` leaves the profile anchored at its corner. | Use `setCenter(true)` for symmetric results. |
| **OBJ 文件为空** | Output directory path is incorrect or missing write permissions. | Verify `MyDir` points to an existing folder and the application has write access. |
| **圆角看起来很锐利** | Rounding radius is too small relative to rectangle size. | Increase the radius value (e.g., `setRoundingRadius(0.5)`). |

## 常见问题

### Q1：我可以在商业项目中使用 Aspose.3D for Java 吗？

A1：可以，Aspose.3D for Java 可用于商业项目。有关授权详情，请访问 [here](https://purchase.aspose.com/buy)。

### Q2：是否提供免费试用？

A2：是的，您可以在此处探索 Aspose.3D for Java 的免费试用 [here](https://releases.aspose.com/)。

### Q3：在哪里可以找到 Aspose.3D for Java 的支持？

A3：Aspose.3D 社区论坛是获取支持和分享经验的好地方。访问论坛 [here](https://forum.aspose.com/c/3d/18)。

### Q4：测试是否需要临时许可证？

A4：是的，如果您需要用于测试的临时许可证，可在此获取 [here](https://purchase.aspose.com/temporary-license/)。

### Q5：在哪里可以找到文档？

A5：Aspose.3D for Java 的文档可在 [here](https://reference.aspose.com/3d/java/) 获取。

## 结论

通过完成本 **java 3d graphics tutorial**，您现在了解如何 **create 3d mesh java** 对象，控制线性拉伸的中心，调整圆化半径，并使用 Aspose.3D **save obj file java** 输出。这些技术为您提供对网格对称性的细粒度控制，对游戏资产、CAD 原型和科学可视化至关重要。欢迎尝试不同的轮廓、切片数量和导出格式，以扩展您的 3‑D 工具箱。

---

**最后更新：** 2026-06-13  
**测试环境：** Aspose.3D for Java 24.11  
**作者：** Aspose

## 相关教程

- [使用 Aspose.3D 创建 3D 拉伸 Java](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [如何在 Aspose.3D for Java 中设置线性拉伸方向](/3d/java/linear-extrusion/setting-direction/)
- [使用扭转的线性拉伸创建 3D 场景 – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}