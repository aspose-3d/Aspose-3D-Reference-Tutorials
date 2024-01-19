---
title: 使用 Aspose.3D 在 Java 中使用欧拉角变换 3D 节点
linktitle: 使用 Aspose.3D 在 Java 中使用欧拉角变换 3D 节点
second_title: Aspose.3D Java API
description: 使用 Aspose.3D 探索 Java 中的 3D 转换世界。按照我们的分步指南将动态欧拉角添加到您的 3D 节点。
type: docs
weight: 19
url: /zh/java/geometry/transform-3d-nodes-with-euler-angles/
---
## 介绍

欢迎来到这个关于使用 Aspose.3D 在 Java 中通过欧拉角变换 3D 节点的分步教程。在本指南中，我们将深入研究向 3D 节点添加变换的过程，使用欧拉角实现动态定位和定向。

## 先决条件

在我们深入学习本教程之前，请确保您具备以下先决条件：

- Java 编程的基础知识。
- 您的计算机上安装了 Java 开发工具包 (JDK)。
-  Aspose.3D 库，您可以从中获取[Aspose.3D Java 文档](https://reference.aspose.com/3d/java/).

## 导入包

首先将必要的包导入到您的 Java 项目中。确保 Aspose.3D 库已正确添加到您的类路径中。如果您还没有下载，可以找到下载链接[这里](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## 步骤1.初始化场景和节点

```java
//ExStart:AddTransformationToNodeByEulerAngles
//初始化场景对象
Scene scene = new Scene();

//初始化Node类对象
Node cubeNode = new Node("cube");
```

## 步骤 2. 创建网格并设置几何体

```java
//调用 Common 类使用多边形生成器方法创建网格来设置网格实例
Mesh mesh = Common.createMeshUsingPolygonBuilder();

//将节点指向网格几何体
cubeNode.setEntity(mesh);
```

## 步骤 3. 设置欧拉角和平移

```java
//欧拉角
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

//设置翻译
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## 步骤 4. 将节点添加到场景

```java
//将立方体添加到场景中
scene.getRootNode().getChildNodes().add(cubeNode);
```

## 步骤 5. 保存 3D 场景

```java
//文档目录的路径。
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

//以支持的文件格式保存 3D 场景
scene.save(MyDir, FileFormat.FBX7500ASCII);
//ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

确保将“您的文档目录”替换为计算机上的适当路径。

## 结论

恭喜！您已通过 Aspose.3D 在 Java 中使用欧拉角成功转换了 3D 节点。尝试不同的角度和平移来创建动态且引人入胜的 3D 场景。

## 常见问题解答

### Q1：我可以在商业项目中使用Aspose.3D for Java吗？

 A1: 是的，可以。参观[购买页面](https://purchase.aspose.com/buy)了解许可详细信息。

### Q2：在哪里可以找到对 Aspose.3D 的支持？

 A2: 的[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)是寻求帮助和与社区联系的地方。

### Q3：有免费试用吗？

 A3：是的，您可以探索[免费试用](https://releases.aspose.com/)体验Aspose.3D的功能。

### Q4：如何获得临时驾照？

 A4：您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).

### Q5：在哪里可以找到文档？

A5: 的[文档](https://reference.aspose.com/3d/java/)提供有关使用 Aspose.3D for Java 的全面指南。