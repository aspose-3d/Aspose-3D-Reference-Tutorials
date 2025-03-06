---
title: 使用 Aspose.3D for Java 控制线性拉伸的中心
linktitle: 使用 Aspose.3D for Java 控制线性拉伸的中心
second_title: Aspose.3D Java API
description: 使用 Aspose.3D 探索 Java 中的 3D 图形世界。轻松控制线性挤压的中心。
weight: 11
url: /zh/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D for Java 控制线性拉伸的中心

## 介绍

在 3D 图形和 Java 编程领域，控制线性挤出的中心对于在项目中实现所需效果起着至关重要的作用。 Aspose.3D for Java 提供了一个强大的工具包来无缝处理此类任务。在本教程中，我们将深入研究使用 Aspose.3D for Java 控制线性挤出中心的过程，分解每个步骤以确保顺利、全面地理解。

## 先决条件

在我们开始本教程之旅之前，请确保您具备以下先决条件：

1. Java 开发环境：确保您的计算机上设置有 Java 开发环境。

2.  Aspose.3D for Java：下载并安装 Aspose.3D 库。您可以找到该库及其文档[这里](https://reference.aspose.com/3d/java/).

3. 文档目录：创建一个目录来存储您的 Java 文档。我们将其称为“您的文档目录”。

## 导入包

在您的 Java 开发环境中，导入 Aspose.3D 所需的包。这确保您的代码可以访问该库提供的功能。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 第 1 步：设置基本配置文件

初始化要拉伸的基础轮廓。在此示例中，我们将使用圆角半径为 0.3 的矩形。

```java
//文档目录的路径。
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 第 2 步：创建 3D 场景

通过创建场景来构建 3D 世界的基础。

```java
Scene scene = new Scene();
```

## 第三步：创建左右节点

在场景中建立左右节点。这些节点充当 3D 对象的画布。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 第 4 步：具有中心属性的线性拉伸

对左侧节点进行不居中的线性挤压，切片数设置为3。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## 步骤 5：设置参考地平面

通过向左侧节点添加地平面来增强视觉表示。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## 第6步：具有中心属性的线性拉伸（右节点）

在右侧节点上执行线性拉伸，这次使拉伸居中，并再次将切片数设置为 3。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## 步骤 7：设置参考地平面（右节点）

与左节点类似，为右节点添加地平面以供参考。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## 第 8 步：保存 3D 场景

以 Wavefront OBJ 格式保存 3D 场景。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 结论

使用 Aspose.3D for Java 控制线性挤压中心为 3D 图形开发带来了令人兴奋的可能性。通过遵循本分步指南，您已经了解了如何操作 center 属性，从而使您能够在 Java 项目中实现所需的视觉效果。

## 常见问题解答

### Q1：我可以在商业项目中使用Aspose.3D for Java吗？

 A1：是的，Aspose.3D for Java 可以用于商业用途。有关许可详细信息，请访问[这里](https://purchase.aspose.com/buy).

### Q2: 有免费试用吗？

A2：是的，您可以探索 Aspose.3D for Java 的免费试用版[这里](https://releases.aspose.com/).

### Q3：在哪里可以找到 Aspose.3D for Java 的支持？

A3：Aspose.3D 社区论坛是寻求支持和分享经验的好地方。访问论坛[这里](https://forum.aspose.com/c/3d/18).

### Q4：测试需要临时许可证吗？

A4：是的，如果您需要临时许可证用于测试目的，您可以获得一个[这里](https://purchase.aspose.com/temporary-license/).

### Q5：在哪里可以找到文档？

A5：Aspose.3D for Java 的文档可用[这里](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
