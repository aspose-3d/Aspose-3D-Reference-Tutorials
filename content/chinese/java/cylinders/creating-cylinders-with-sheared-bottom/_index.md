---
title: 在 Aspose.3D for Java 中创建具有剪切底部的圆柱体
linktitle: 在 Aspose.3D for Java 中创建具有剪切底部的圆柱体
second_title: Aspose.3D Java API
description: 学习使用 Aspose.3D for Java 创建具有剪切底部的定制圆柱体。通过本分步指南提高您的 3D 建模技能。
type: docs
weight: 12
url: /zh/java/cylinders/creating-cylinders-with-sheared-bottom/
---
## 介绍

欢迎阅读本分步指南，了解如何使用 Aspose.3D for Java 创建具有剪切底部的圆柱体。 Aspose.3D 是一个功能强大的 Java 库，可让您轻松处理 3D 文件。在本教程中，我们将深入创建具有剪切底部的定制圆柱体，为您提供使用 Aspose.3D 的实践经验，以增强您的 3D 建模技能。

## 先决条件

在我们开始之前，请确保您具备以下先决条件：
- 您的系统上安装了 Java 开发工具包 (JDK)。
- 下载 Aspose.3D for Java 库并将其添加到您的项目中。你可以找到下载链接[这里](https://releases.aspose.com/3d/java/).

## 导入包

首先，导入在 Java 应用程序中使用 Aspose.3D 所需的包：
```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 第 1 步：创建场景

首先创建一个 3D 场景，您将在其中添加和操作圆柱体：
```java
//起始时间：3
//创建场景
Scene scene = new Scene();
//结束：3
```

## 步骤 2：创建圆柱体 1

现在，让我们创建第一个带有剪切底部的圆柱体：
```java
//起始时间：4
//创建圆柱体 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
//气缸1定制剪底
cylinder1.setShearBottom(new Vector2(0, 0.83)); //xy 平面（z 轴）剪切 47.5 度
//将圆柱体 1 添加到场景中
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
//结束：4
```

## 第 3 步：创建圆柱体 2

接下来，让我们在场景中添加第二个没有剪切底部的圆柱体：
```java
//起始时间：5
//创建圆柱体 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
//将没有 ShearBottom 的圆柱体 2 添加到场景中
scene.getRootNode().createChildNode(cylinder2);
//结束：5
```

## 第 4 步：保存场景

将带有自定义圆柱体的场景保存到文档目录中：
```java
//起始时间：6
//保存场景
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
//结束：6
```

恭喜！您已使用 Aspose.3D for Java 成功创建了底部被剪切的圆柱体。

## 结论

在本教程中，我们探讨了如何利用 Aspose.3D for Java 来增强您的 3D 建模项目。创建具有剪切底部的定制圆柱体可为您的设计增添独特的触感，而 Aspose.3D 则简化了流程。

## 常见问题解答

### Q1：我可以将 Aspose.3D for Java 与其他 Java 3D 库一起使用吗？

A1：Aspose.3D for Java 被设计为独立工作。虽然您可以将其与其他库集成，但它的功能足够强大，可以自行处理大多数 3D 建模任务。

### Q2：Aspose.3D适合3D建模初学者吗？

A2：是的，Aspose.3D提供了用户友好的API，使其适合3D建模的初学者和经验丰富的开发人员。

### 问题 3：在哪里可以找到 Aspose.3D for Java 的其他支持？

 A3：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)以获得社区支持和讨论。

### Q4：如何获得Aspose.3D的临时许可证？

 A4：您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).

### Q5: 我可以购买 Aspose.3D for Java 吗？

 A5：是的，您可以购买Aspose.3D for Java[这里](https://purchase.aspose.com/buy).