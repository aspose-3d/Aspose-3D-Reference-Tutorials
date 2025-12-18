---
date: 2025-12-18
description: 学习如何使用 Aspose.3D for Java 在线性挤压中添加地面平面并设置中心属性，提供逐步代码示例。
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 如何在 Aspose.3D for Java 中为线性挤压添加地面平面和控制中心
url: /zh/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Java 中使用 Aspose.3D 控制线性拉伸的中心

## 介绍

当您在 Java 中构建 3D 场景时，能够 **添加地面平面** 并精确 **设置线性拉伸的中心属性**，可以让原型从平面化提升到精致的视觉效果。在本教程中，我们将完整演示如何使用 Aspose.3D for Java 控制拉伸中心并添加地面平面。您将了解其重要性、设置方法，并获得可直接运行的代码示例，方便在自己的项目中进行适配。

## 快速回答
- **“add ground plane” 的作用是什么？** 它创建一个薄的参考几何体，帮助您查看拉伸相对于世界坐标轴的位置。  
- **如何设置线性拉伸的中心？** 在 `LinearExtrusion` 对象上使用 `setCenter(boolean)` 方法。  
- **运行示例是否需要许可证？** 临时许可证可用于测试；生产环境需要正式许可证。  
- **保存使用的文件格式是什么？** 示例保存为 Wavefront OBJ（`.obj`）。  
- **需要哪个 Java 版本？** Java 8 或更高版本即可。

## 在 3D 场景中，“add ground plane” 是什么？

添加地面平面是指在 X‑Z 平面上插入一个薄的矩形几何体（通常是厚度极小的盒子）。它充当可视化的地板，使您更容易判断其他对象的高度和对齐方式，尤其是在尝试拉伸中心时。

## 为什么要在线性拉伸上设置 center 属性？

默认情况下，线性拉伸从轮廓的原点开始。设置 center 属性（`setCenter(true)`）会将轮廓移动，使拉伸以原点为中心，这对于对称设计或在多个对象之间保持一致对齐非常有用。

## 先决条件

在开始本教程之前，请确保已具备以下先决条件：

1. **Java 开发环境** – 确保您的机器上已搭建好 Java 开发环境。  
2. **Aspose.3D for Java** – 下载并安装 Aspose.3D 库。您可以在[此处](https://reference.aspose.com/3d/java/)找到库及其文档。  
3. **文档目录** – 创建一个目录用于存放您的 Java 文档。我们称之为“Your Document Directory”。

## 导入包

在您的 Java 开发环境中，导入 Aspose.3D 所需的包。这可确保代码能够访问库提供的功能。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步骤 1：设置基础轮廓

初始化要进行拉伸的基础轮廓。在本例中，我们使用圆角半径为 0.3 的矩形形状。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 步骤 2：创建 3D 场景

通过创建场景来构建 3D 世界的基础。

```java
Scene scene = new Scene();
```

## 步骤 3：创建左侧和右侧节点

在场景中建立左侧和右侧节点。这些节点充当 3D 对象的画布。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步骤 4：使用 Center 属性进行线性拉伸（左侧节点）

在左侧节点上执行 **未居中** 的线性拉伸，并将切片数量设置为 3。注意 `setCenter(false)` 调用——这里我们将 **center 属性** 设置为 *false*。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## 步骤 5：为左侧节点添加参考地面平面

通过在左侧节点 **添加地面平面** 来增强可视化效果。薄盒子充当地板，使您能够清晰看到拉伸的高度。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## 步骤 6：使用 Center 属性进行线性拉伸（右侧节点）

现在在右侧节点上执行线性拉伸，这次 **居中拉伸**。`setCenter(true)` 调用演示了如何将 **center 属性** 设置为 *true*。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## 步骤 7：为右侧节点添加参考地面平面

与左侧相同，为右侧节点添加地面平面，以获得一致的视觉基准。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## 步骤 8：保存 3D 场景

将您的 3D 场景保存为 Wavefront OBJ 格式，以便在任何标准 3D 查看器中查看。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常见问题及解决方案

| 问题 | 原因 | 解决办法 |
|------|------|----------|
| 地面平面不可见 | 盒子厚度对查看器的比例来说太小。 | 增加厚度（`Box` 的第一个参数）或在查看器中缩小视图。 |
| 拉伸出现偏移 | `setCenter` 的值未按预期设置。 | 再次检查传递给 `setCenter` 的布尔值。 |
| 文件未保存 | 目录路径不正确或缺少写入权限。 | 确认 `MyDir` 指向具有写入权限的现有文件夹。 |

## 常见问答

**Q1：我可以在商业项目中使用 Aspose.3D for Java 吗？**  
A1：可以，Aspose.3D for Java 可用于商业用途。有关许可证详情，请访问[此处](https://purchase.aspose.com/buy)。

**Q2：是否提供免费试用？**  
A2：是的，您可以在[此处](https://releases.aspose.com/)体验 Aspose.3D for Java 的免费试用。

**Q3：在哪里可以找到 Aspose.3D for Java 的支持？**  
A3：Aspose.3D 社区论坛是寻求支持和分享经验的好地方。访问论坛[此处](https://forum.aspose.com/c/3d/18)。

**Q4：测试是否需要临时许可证？**  
A4：是的，如果您需要用于测试的临时许可证，可在[此处](https://purchase.aspose.com/temporary-license/)获取。

**Q5：在哪里可以找到文档？**  
A5：Aspose.3D for Java 的文档可在[此处](https://reference.aspose.com/3d/java/)获取。

## 结论

在 Aspose.3D for Java 中控制线性拉伸的中心 **并** 学会 **添加地面平面**，为 3D 图形开发打开了令人兴奋的可能性。通过上述步骤，您现在拥有了一个可复用的模式，用于创建居中拉伸、可视化参考平面，并将结果导出为 OBJ。欢迎尝试不同的轮廓、切片数量和变换，以满足您项目的需求。

---

**最后更新：** 2025-12-18  
**测试环境：** Aspose.3D 24.11 for Java (latest at time of writing)  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}