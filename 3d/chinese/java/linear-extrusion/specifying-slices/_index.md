---
date: 2026-02-22
description: 学习如何使用 Aspose.3D for Java 创建带切片的 3D 拉伸。本分步指南涵盖线性拉伸、设置圆角半径以及导出 OBJ。
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
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

如果您需要 **创建平滑且精确的 3d 拉伸** 对象，控制切片数量是关键。在本教程中，我们将演示如何在使用 Aspose.3D for Java 进行线性拉伸时指定切片。您将了解切片数量为何重要、如何设置圆角半径，以及如何将结果导出为 OBJ 文件，以便在任何 3D 流程中使用。

## 快速答疑
- **“切片”控制什么？** 用于近似拉伸表面的中间横截面数量。  
- **哪个方法设置切片数量？** `LinearExtrusion.setSlices(int)`  
- **我可以更改轮廓的圆角半径吗？** 可以，通过 `RectangleShape.setRoundingRadius(double)`  
- **本例使用的文件格式是什么？** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **运行代码是否需要许可证？** 免费试用可用于评估；生产环境需要商业许可证。

## 什么是带切片的线性拉伸？

线性拉伸将二维轮廓（如矩形）沿直线拉伸，形成三维实体。通过指定 **切片**，您告诉 Aspose.3D 生成多少个中间步骤，这直接影响诸如圆角矩形等曲线边缘的平滑程度。

## 为什么使用 Aspose.3D for Java 来创建 3d 拉伸？

* **完全控制** – 可以以编程方式调整切片数量、圆角半径和导出格式。  
* **跨平台** – 在任何支持 Java 的环境中运行，无需本地依赖。  
* **导出灵活** – 可直接保存为 OBJ、FBX、STL 等多种格式。

## 前置条件

1. **Java Development Kit** – 已安装 JDK 8 或更高版本。  
2. **Aspose.3D for Java** – 从官方站点 [here](https://releases.aspose.com/3d/java/) 下载库。  
3. 您喜欢的 IDE 或文本编辑器。

## 导入包

将 Aspose.3D 命名空间添加到项目中，以便访问 3‑D 建模类。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 步骤指南

### 步骤 1：设置场景并定义轮廓

首先创建一个 `RectangleShape` 并设置 **圆角半径**，使角部平滑。随后初始化一个新的 `Scene`，用于容纳所有几何体。

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### 步骤 2：为每个拉伸创建 **子节点** 对象

每个几何体都位于一个 `Node` 下。这里我们生成两个兄弟节点——一个用于低切片拉伸，另一个用于高切片拉伸——并将左侧节点稍微向侧面移动，以便更容易比较结果。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 步骤 3：执行线性拉伸并 **设置切片**

现在真正 **创建 3d 拉伸** 对象。`LinearExtrusion` 构造函数接受轮廓和拉伸深度。使用 **匿名内部类** 调用 `setSlices` 来控制平滑度。左侧节点仅使用 2 个切片（粗糙），右侧节点使用 10 个切片（平滑）。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### 步骤 4：**导出 OBJ** – 保存场景

最后将场景写入 Wavefront OBJ 文件，这是一种被众多 3‑D 编辑器和游戏引擎广泛支持的格式。此步骤演示了 Aspose.3D 的 **export obj java** 能力。

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常见问题及解决方案

| 问题 | 产生原因 | 解决办法 |
|------|----------|----------|
| **拉伸呈平面** | 切片数量设为 1 或 0 | 确保 `setSlices` 的值 ≥ 2。 |
| **圆角看起来锯齿状** | 圆角半径相对于切片数量太小 | 增大半径或提升切片数量，以获得更平滑的曲线。 |
| **保存时文件未找到** | `MyDir` 指向不存在的文件夹 | 事先创建目录或使用绝对路径。 |

## 常见问答

**Q: 如何下载 Aspose.3D for Java？**  
A: 您可以在此处下载库 [here](https://releases.aspose.com/3d/java/)。

**Q: 哪里可以找到 Aspose.3D 的文档？**  
A: 请参考文档 [here](https://reference.aspose.com/3d/java/)。

**Q: 是否提供免费试用？**  
A: 是的，您可以在此处获取免费试用 [here](https://releases.aspose.com/)。

**Q: 如何获取 Aspose.3D 的支持？**  
A: 访问支持论坛 [here](https://forum.aspose.com/c/3d/18)。

**Q: 我可以购买临时许可证吗？**  
A: 可以，临时许可证可在此处获取 [here](https://purchase.aspose.com/temporary-license/)。

---

**最后更新：** 2026-02-22  
**测试环境：** Aspose.3D for Java 24.11（撰写时的最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}