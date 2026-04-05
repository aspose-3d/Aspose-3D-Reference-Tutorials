---
date: 2026-02-22
description: 学习如何在 Aspose.3D for Java 中设置线性拉伸方向并导出 3D 模型 OBJ，按照我们的分步指南操作。
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 如何使用 Aspose.3D for Java 设置线性挤压的方向
url: /zh/java/linear-extrusion/setting-direction/
weight: 12
---

.

Translate bullet points.

Tables.

FAQ.

Make sure to keep markdown.

Let's craft.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D for Java 中设置线性拉伸的方向

## 简介

在本教程中，您将学习 **如何在使用 Aspose.3D for Java 进行线性拉伸时设置方向**。无论是构建类似 CAD 的工具，还是为游戏引擎生成几何体，控制拉伸方向都能让您精确地创建所需形状。我们将逐步演示从初始化轮廓到将结果保存为 OBJ 文件的全过程，让您能够直接从 Java **导出 3d model obj** 文件。

## 快速答案
- **线性拉伸的主要类是什么？** `LinearExtrusion`
- **哪个方法定义拉伸方向？** `setDirection(Vector3 direction)`
- **可以将结果导出为 OBJ 吗？** 可以，使用 `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **开发阶段需要许可证吗？** 提供免费试用版；生产环境需要许可证。
- **推荐使用哪款 Java IDE？** IntelliJ IDEA 或 Eclipse 均完全支持。

## 什么是线性拉伸？

线性拉伸将二维轮廓（如矩形或圆形）沿直线延伸，生成三维实体。默认情况下，拉伸沿正 Z 轴方向进行，但 Aspose.3D 允许您通过 `setDirection` 属性更改该路径。

## 为什么要在线性拉伸中设置方向？

自定义方向在以下情况下非常有用：
- 将几何体与场景中已有对象对齐。
- 在无需额外变换步骤的情况下创建倾斜或斜角部件。
- 导出必须匹配特定坐标系的模型（例如用于 3‑D 打印或游戏引擎）。

## 前置条件

在开始之前，请确保您具备：

- 基本的 Java 知识。
- 已安装 Aspose.3D 库。您可以从 [here](https://releases.aspose.com/3d/java/) 下载。
- 使用 Eclipse 或 IntelliJ IDEA 等 IDE。

## 导入包

首先，导入提供核心 3‑D 类和实用类型的命名空间。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步骤 1：初始化基础轮廓

创建将要被拉伸的形状。本例使用带有小圆角半径的 `RectangleShape`，以获得平滑的边缘。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 步骤 2：创建场景

`Scene` 对象充当所有 3‑D 节点、灯光、相机和材质的容器。

```java
Scene scene = new Scene();
```

## 步骤 3：创建节点

向场景根节点添加两个子节点——一个用于左侧拉伸，另一个用于右侧拉伸。右侧节点会平移，以防两个对象重叠。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步骤 4：在左侧节点执行线性拉伸

在左侧节点上使用默认的 Z 轴方向进行拉伸。我们还添加了完整的 360° 扭转，并增加了切片数量以获得更平滑的网格。

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 步骤 5：在右侧节点使用方向执行线性拉伸

这里是 **设置方向** 的关键。通过向 `setDirection` 传入自定义的 `Vector3`，拉伸将沿向量 (0.3, 0.2, 1) 进行，从而生成倾斜形状。

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 步骤 6：保存 3D 场景

最后，将场景导出为 Wavefront OBJ 格式。此步骤演示了如何 **save obj file java** 项目，并便于在任何 3‑D 查看器中查看结果。

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常见问题及解决方案

| 问题 | 产生原因 | 解决办法 |
|------|----------|----------|
| OBJ 文件为空 | 轮廓未添加到节点 | 确保在有效节点上调用 `createChildNode` |
| 方向未改变 | `setDirection` 在拉伸已构建后调用 | 如示例所示，在 `LinearExtrusion` 初始化时设置方向 |
| 网格分辨率低 | `setSlices` 值过低 | 增加切片数量（例如 100 或更高） |

## 结论

现在，您已经掌握了 **如何在线性拉伸中设置方向**，以及如何调节扭转和切片参数，并使用 Aspose.3D for Java **导出 3d model obj** 文件。这些技巧为几何体创建提供了细粒度控制，并使将 3‑D 资产集成到更大流水线中变得轻而易举。

## FAQ's

### Q1: 我可以在其他编程语言中使用 Aspose.3D 吗？

A1: Aspose.3D 支持多种编程语言，包括 .NET 和 Java。

### Q2. Aspose.3D 是否提供免费试用？

A2: 是的，您可以在此处免费试用 Aspose.3D 的功能 [here](https://releases.aspose.com/)。

### Q3: 哪里可以找到 Aspose.3D for Java 的详细文档？

A3: 完整文档可在此处获取 [here](https://reference.aspose.com/3d/java/)。

### Q4: 如何获取 Aspose.3D 的技术支持？

A4: 请访问 [Aspose.3D forum](https://forum.aspose.com/c/3d/18) 获取帮助或提问。

### Q5: 是否提供 Aspose.3D 的临时许可证？

A5: 可以，临时许可证获取地址在此 [here](https://purchase.aspose.com/temporary-license/)。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-22  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose