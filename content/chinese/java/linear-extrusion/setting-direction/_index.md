---
title: 使用 Aspose.3D for Java 设置线性拉伸方向
linktitle: 使用 Aspose.3D for Java 设置线性拉伸方向
second_title: Aspose.3D Java API
description: 使用 Aspose.3D for Java 掌握线性挤出！请遵循我们的无缝 3D 编程指南。立即下载以获得迷人的体验。
type: docs
weight: 12
url: /zh/java/linear-extrusion/setting-direction/
---
## 介绍

欢迎阅读我们关于使用 Aspose.3D for Java 设置线性挤出方向的分步指南。 Aspose.3D 是一个功能强大的 Java 库，允许开发人员无缝地处理 3D 文件和场景。在本教程中，我们将重点关注在线性挤出中设置方向的具体任务，以提高您在 3D 编程方面的熟练程度。

## 先决条件

在我们深入学习本教程之前，请确保您具备以下先决条件：

- Java 编程语言的基础知识。
-  Aspose.3D 库已安装。您可以从以下位置下载：[这里](https://releases.aspose.com/3d/java/).
- Java 集成开发环境 (IDE)，例如 Eclipse 或 IntelliJ。

## 导入包

确保导入必要的包来启动您的项目：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 第 1 步：初始化基本配置文件

首先初始化要拉伸的基础轮廓。在这个例子中，我们使用一个`RectangleShape`圆角半径为 0.3：

```java
//文档目录的路径。
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 第 2 步：创建场景

接下来，创建一个 3D 场景来包含挤出的对象：

```java
Scene scene = new Scene();
```

## 第三步：创建节点

在场景中创建左右节点：

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 第四步：对左节点进行线性挤压

使用以下命令对左侧节点执行线性挤压`LinearExtrusion`具有指定参数（例如扭曲和切片）的类：

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 步骤5：在右侧节点上进行有方向的线性挤压

对右侧节点进行线性挤压，引入`setDirection`属性来定义挤出方向：

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 第 6 步：保存 3D 场景

将 3D 场景保存为所需的文件格式。在此示例中，我们将其另存为 Wavefront OBJ 文件：

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 结论

恭喜！您已经成功学习了如何使用 Aspose.3D for Java 设置线性拉伸方向。本教程可增强您的 3D 编程技能，并为创意项目开辟新的可能性。

## 常见问题解答

### Q1：我可以将Aspose.3D与其他编程语言一起使用吗？

A1：Aspose.3D支持多种编程语言，包括.NET和Java。

### Q2。 Aspose.3D 是否有免费试用版？

 A2：是的，您可以通过免费试用探索 Aspose.3D 的功能[这里](https://releases.aspose.com/).

### Q3：在哪里可以找到 Aspose.3D for Java 的详细文档？

 A3：提供全面的文档[这里](https://reference.aspose.com/3d/java/).

### Q4：如何获得 Aspose.3D 的支持？

 A4：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)如有任何帮助或疑问。

### Q5：Aspose.3D 是否有临时许可证？

 A5：是的，您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).