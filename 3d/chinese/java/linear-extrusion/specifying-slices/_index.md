---
title: 使用 Aspose.3D for Java 指定线性拉伸中的切片
linktitle: 使用 Aspose.3D for Java 指定线性拉伸中的切片
second_title: Aspose.3D Java API
description: 学习使用 Aspose.3D for Java 在线性拉伸中指定切片。通过本分步指南提高您的 3D 建模技能。
weight: 13
url: /zh/java/linear-extrusion/specifying-slices/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D for Java 指定线性拉伸中的切片

## 介绍

创建复杂的 3D 模型通常需要的不仅仅是创造力；它需要对您可以使用的工具有透彻的了解。 Aspose.3D for Java 在这方面是一个游戏规则改变者。在本教程中，我们将重点关注一个特定方面 - 指定线性挤出中的切片。

## 先决条件

在深入学习本教程之前，请确保您具备以下先决条件：

1. Java 环境：确保您的系统上设置了 Java 开发环境。
2.  Aspose.3D for Java：下载并安装 Aspose.3D 库。就可以找到需要的包了[这里](https://releases.aspose.com/3d/java/).

## 导入包

在您的 Java 项目中，导入 Aspose.3D 库。这对于访问我们将要使用的功能至关重要。将以下导入语句添加到您的代码中：

```java
import com.aspose.threed.*;

import java.io.IOException;
```

现在，让我们将该示例分解为多个步骤。

## 第 1 步：设置场景

初始化要挤出的基础轮廓，在本例中为`RectangleShape`具有指定的圆角半径。创建要在其中工作的 3D 场景。

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## 第2步：创建节点

在场景内生成左节点和右节点。调整左节点的平移以实现空间变化。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 第 3 步：带切片的线性挤出

在两个节点上执行线性拉伸，指定每个节点的切片数量。这就是奇迹发生的地方。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## 第 4 步：保存场景

以所需格式保存 3D 场景，在本例中为 Wavefront OBJ 文件。

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 结论

恭喜！您已经成功学习了如何使用 Aspose.3D for Java 在线性拉伸中指定切片。这项技能为您的 3D 建模之旅开辟了新的可能性。

## 常见问题解答

### Q1: 如何下载 Aspose.3D for Java？

 A1：您可以下载该库[这里](https://releases.aspose.com/3d/java/).

### Q2：哪里可以找到Aspose.3D的文档？

 A2：参考文档[这里](https://reference.aspose.com/3d/java/).

### Q3：有免费试用吗？

 A3：是的，您可以探索免费试用[这里](https://releases.aspose.com/).

### Q4：如何获得 Aspose.3D 的支持？

A4：访问支持论坛[这里](https://forum.aspose.com/c/3d/18).

### Q5：我可以购买临时许可证吗？

 A5：是的，可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
