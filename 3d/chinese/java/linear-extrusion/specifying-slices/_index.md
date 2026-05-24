---
date: 2026-05-24
description: 了解如何使用 Aspose.3D for Java 通过切片创建 3D 拉伸。本分步指南涵盖线性拉伸、设置圆角半径以及导出 OBJ。
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: 使用切片创建 3D 拉伸 – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: 使用切片创建 3D 拉伸 – Aspose.3D for Java
url: /zh/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用切片创建 3D 拉伸 – Aspose.3D for Java

## 介绍

如果您需要 **创建平滑且精确的 3D 拉伸** 对象，控制切片数量是关键。在本教程中，我们将演示如何在使用 Aspose.3D for Java 进行线性拉伸时指定切片。您将了解切片数量为何重要、如何设置圆角半径，以及如何将结果导出为 OBJ 文件，以便在任何 3‑D 流程中使用。

## 快速答案
- **“切片” 控制什么？** 用于近似拉伸表面的中间横截面数量。  
- **哪个方法设置切片数量？** `LinearExtrusion.setSlices(int)`  
- **我可以更改轮廓的圆角半径吗？** 可以，通过 `RectangleShape.setRoundingRadius(double)`  
- **本示例使用的文件格式是什么？** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **运行代码是否需要许可证？** 免费试用可用于评估；生产环境需要商业许可证。

`LinearExtrusion.setSlices(int)` 设置拉伸将生成的中间切片数量。  
`RectangleShape.setRoundingRadius(double)` 定义矩形轮廓的角半径。

## 如何使用切片在 Java 中创建 3D 拉伸？

加载您的 2‑D 轮廓，选择切片数量，设置圆角半径，然后调用 `save` ——整个工作流只需几行代码。Aspose.3D for Java 自动处理几何体创建、切片插值和 OBJ 导出，让您专注于视觉质量，而无需关注底层网格计算。

## 什么是带切片的线性拉伸？

带切片的线性拉伸通过沿直线扫掠平面 2‑D 形状，并生成可配置数量的中间横截面，将其转化为 3‑D 实体。切片数量直接影响诸如圆角等曲线边缘的平滑程度。

## 为什么使用 Aspose.3D for Java 来创建 3D 拉伸？

Aspose.3D 提供 **对每个拉伸参数的完整编程控制**，支持 **50+ 输入和输出格式**（包括 OBJ、FBX、STL、GLTF），并且能够在不将整个文件加载到内存的情况下处理 **上百页的模型**。它可在任何支持 Java 的平台上运行，无需本机 DLL，并在 Windows、Linux、macOS 上保证确定性的结果。

## 前置条件

1. **Java Development Kit** – 已安装 JDK 8 或更高版本。  
2. **Aspose.3D for Java** – 从官方站点 [here](https://releases.aspose.com/3d/java/) 下载库。  
3. 您喜欢的 IDE 或文本编辑器。

## 导入包

将 Aspose.3D 命名空间添加到项目，以便访问 3‑D 建模类。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 分步指南

### 步骤 1：设置场景并定义轮廓

`RectangleShape` 是定义 2‑D 矩形轮廓的类。  
首先创建一个 `RectangleShape` 并为其设置 **圆角半径**，使角部平滑。  
`Scene` 是所有节点和几何体的根容器。  
随后初始化一个新的 `Scene` 来容纳所有几何体。

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### 步骤 2：为每个拉伸创建子节点对象

`Node` 表示场景图中的一个元素，可容纳几何体和变换。  
每个几何体都位于一个 `Node` 下。这里我们生成两个兄弟节点——一个用于低切片拉伸，另一个用于高切片拉伸，并将左侧节点稍微向侧面移动，以便更容易比较结果。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 步骤 3：执行线性拉伸并设置切片

`LinearExtrusion` 是通过线性扫掠轮廓创建实体的类。  
`LinearExtrusion` 是 Aspose.3D 用于沿直线拉伸 2‑D 轮廓生成实体的类。使用 **匿名内部类** 调用 `setSlices` 来控制平滑度。左侧节点仅使用 2 个切片（粗糙），右侧节点使用 10 个切片（平滑）。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### 步骤 4：导出 OBJ – 保存场景

最后我们将场景写入 Wavefront OBJ 文件，这是一种被众多 3‑D 编辑器和游戏引擎广泛支持的格式。这展示了 Aspose.3D 的 **导出 OBJ Java** 能力。

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常见问题及解决方案

| 问题 | 原因 | 解决方案 |
|-------|----------------|-----|
| **拉伸呈现平面** | 切片数量设置为 1 或 0 | 确保 `setSlices` 的值 ≥ 2。 |
| **圆角出现锯齿** | 圆角半径相对于切片数量太小 | 增大半径或增加切片数量以获得更平滑的曲线。 |
| **保存时文件未找到** | `MyDir` 指向不存在的文件夹 | 预先创建目录或使用绝对路径。 |

## 常见问题

**问：如何下载 Aspose.3D for Java？**  
答：您可以在 [here](https://releases.aspose.com/3d/java/) 下载库。

**问：在哪里可以找到 Aspose.3D 的文档？**  
答：请参阅文档 [here](https://reference.aspose.com/3d/java/)。

**问：是否提供免费试用？**  
答：是的，您可以在 [here](https://releases.aspose.com/) 体验免费试用。

**问：如何获取 Aspose.3D 的支持？**  
答：访问支持论坛 [here](https://forum.aspose.com/c/3d/18)。

**问：我可以购买临时许可证吗？**  
答：可以，临时许可证可在 [here](https://purchase.aspose.com/temporary-license/) 获取。

---

**最后更新：** 2026-05-24  
**测试环境：** Aspose.3D for Java 24.11（撰写时最新）  
**作者：** Aspose

## 相关教程

- [Create 3D Extrusion Java with Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [How to Set Direction in Linear Extrusion with Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Create 3D Scene with Twist in Linear Extrusion – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}