---
date: 2026-02-20
description: 学习使用 Aspose.3D 在 Java 中进行线性拉伸时控制中心的 3D 图形教程，包括如何设置圆角半径以及保存 OBJ 文件。
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Java 3D 图形教程 – 线性挤出中的中心
url: /zh/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D 图形教程 – 线性挤压的中心

## 介绍

如果你在 Java 中构建 3D 可视化，掌握挤压技术是必不可少的。本 **java 3d graphics tutorial** 将手把手教你如何使用 Aspose.3D for Java 控制线性挤压的中心，从而在无需额外数学计算的情况下创建精确、对称的模型。阅读完本指南后，你将了解 `center` 属性为何重要，如何 **set rounding radius**，以及如何 **save OBJ file java**‑兼容的输出。

## 快速回答
- **center 属性有什么作用？** 它决定挤压是否围绕轮廓原点对称。  
- **运行代码是否需要许可证？** 临时许可证可用于测试；生产环境需要正式许可证。  
- **结果使用哪种文件格式？** 场景会保存为 Wavefront OBJ 文件。  
- **可以更改切片数量吗？** 可以，使用 `LinearExtrusion` 对象的 `setSlices(int)` 方法。  
- **Aspose.3D 是否兼容 Java 8+？** 完全兼容——支持所有主流的 Java 版本。

## 什么是 java 3d graphics tutorial？

**java 3d graphics tutorial** 逐步说明如何使用 Java 库创建、操作和渲染三维对象。本教程聚焦于 Aspose.3D 的挤压 API，将二维轮廓转换为完整的三维网格。

## 为什么选择 Aspose.3D for Java？

- **高级 API** – 无需编写底层网格计算代码。  
- **跨格式支持** – 可导出为 OBJ、FBX、STL 等多种格式。  
- **性能优化** – 高效处理大型场景。  
- **丰富文档** – 包含本文所示的示例代码。

## 前置条件

在开始之前，请确保你已经：

1. **Java 开发环境** – 已安装 JDK 8 或更高版本。  
2. **Aspose.3D for Java** – 在 [这里](https://reference.aspose.com/3d/java/) 下载库及文档。  
3. **文档目录** – 在本机创建一个文件夹用于存放生成的文件，我们将其称为 **“Your Document Directory”。**

## 导入包

在你的 Java IDE 中导入所需的 Aspose.3D 类，以便编译器能够访问挤压和场景构建功能。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步骤指南

### 步骤 1：设置基础轮廓

首先创建将要被挤压的二维形状。这里使用矩形并 **set rounding radius** 为 0.3，以平滑角部。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### 步骤 2：创建 3D 场景

`Scene` 对象充当所有 3‑D 节点、灯光和相机的容器。

```java
Scene scene = new Scene();
```

### 步骤 3：添加左侧和右侧节点

我们将在左右两侧各放置一个节点，以便比较有无居中设置的挤压效果。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 步骤 4：线性挤压 – 不居中（左侧节点）

在左侧节点上创建挤压，关闭居中，并将网格限制为三层切片，以获得低多边形预览。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### 步骤 5：为左侧节点添加参考地面

使用一个薄盒子作为可视化地面，帮助你观察挤压的方向。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### 步骤 6：线性挤压 – 居中（右侧节点）

现在在右侧节点重复挤压，这次启用 `center`。几何体将围绕轮廓原点对称。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### 步骤 7：为右侧节点添加参考地面

右侧同样使用地面盒子，以便清晰对比。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### 步骤 8：保存 3D 场景

最后，将整个场景导出为 Wavefront OBJ 文件——这种格式可在大多数 3‑D 编辑器中直接使用。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常见问题及解决方案

| 问题 | 产生原因 | 解决办法 |
|------|----------|----------|
| **挤压出现偏移** | `setCenter(false)` 使轮廓锚定在角落。 | 使用 `setCenter(true)` 以获得对称结果。 |
| **OBJ 文件为空** | 输出目录路径错误或缺少写入权限。 | 确认 `MyDir` 指向已存在的文件夹且应用拥有写入权限。 |
| **圆角看起来很锐利** | 相对于矩形尺寸，圆角半径太小。 | 增大半径值（例如 `setRoundingRadius(0.5)`）。 |

## 常见问答

### Q1：可以在商业项目中使用 Aspose.3D for Java 吗？

A1：可以，Aspose.3D for Java 可用于商业用途。许可证详情请访问 [here](https://purchase.aspose.com/buy)。

### Q2：是否提供免费试用？

A2：是的，你可以在 [here](https://releases.aspose.com/) 试用 Aspose.3D for Java 的免费版本。

### Q3：在哪里可以获得 Aspose.3D for Java 的支持？

A3：Aspose.3D 社区论坛是获取帮助和分享经验的好地方。访问论坛请点 [here](https://forum.aspose.com/c/3d/18)。

### Q4：测试时需要临时许可证吗？

A4：需要。如果你需要临时许可证进行测试，可在 [here](https://purchase.aspose.com/temporary-license/) 获取。

### Q5：文档在哪里可以找到？

A5：Aspose.3D for Java 的文档可在 [here](https://reference.aspose.com/3d/java/) 查看。

## 结论

通过完成本 **java 3d graphics tutorial**，你现在已经掌握了如何控制线性挤压的中心、调整圆角半径，并使用 Aspose.3D **save OBJ file java** 输出。这些技巧让你能够细致地控制网格对称性，对游戏资产、CAD 原型以及科学可视化等场景尤为重要。欢迎尝试不同的轮廓、切片数量和导出格式，进一步丰富你的 3‑D 工具箱。

---

**最后更新：** 2026-02-20  
**测试环境：** Aspose.3D for Java 24.11  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}