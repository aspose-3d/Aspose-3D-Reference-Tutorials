---
title: 使用 Aspose.3D 通过变换矩阵变换 3D 节点
linktitle: 使用 Aspose.3D 在 Java 中通过变换矩阵变换 3D 节点
second_title: Aspose.3D Java API
description: 使用 Aspose.3D 探索 Java 中的 3D 图形世界。学习使用变换矩阵轻松变换节点。
type: docs
weight: 21
url: /zh/java/geometry/transform-3d-nodes-with-matrices/
---
## 介绍

欢迎阅读本分步指南，了解如何使用 Aspose.3D 在 Java 中通过变换矩阵变换 3D 节点。如果您是一位希望提高 3D 图形和建模技能的 Java 开发人员，那么您来对地方了。在本教程中，我们将深入探讨在 Aspose.3D 框架内将转换应用于 3D 节点的过程。

## 先决条件

在我们开始之前，请确保您满足以下先决条件：

- Java 编程的基础知识。
-  Aspose.3D 库已安装。您可以从以下位置下载：[这里](https://releases.aspose.com/3d/java/).
- 用于 Java 开发的工作集成开发环境 (IDE)。

## 导入包

在您的 Java 项目中，从 Aspose.3D 导入必要的包。确保您的项目配置正确以使用 Aspose.3D 库。这是一个示例导入语句：

```java
import com.aspose.threed.*;

```

## 变换 3D 节点

### 第 1 步：初始化场景对象

首先初始化一个场景对象，该对象充当 3D 元素的容器。

```java
Scene scene = new Scene();
```

### 步骤2：初始化节点类对象

创建一个 Node 类对象，例如一个立方体，它将进行转换。

```java
Node cubeNode = new Node("cube");
```

### 第 3 步：使用多边形生成器创建网格

利用 Common 类使用多边形生成器方法创建网格。这将设置立方体的网格实例。

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### 第 4 步：将节点指向网格几何体

将创建的网格分配给立方体节点。

```java
cubeNode.setEntity(mesh);
```

### 第5步：设置自定义翻译矩阵

将自定义平移矩阵应用到立方体节点。此示例设置用于平移的变换矩阵。

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### 第 6 步：将立方体添加到场景中

将立方体节点包含在场景的根节点中。

```java
scene.getRootNode().addChildNode(cubeNode);
```

### 第 7 步：保存 3D 场景

指定以支持的文件格式（例如 FBX）保存 3D 场景的目录和文件名。

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## 结论

恭喜！您已经成功学习了如何在 Java 中使用 Aspose.3D 转换 3D 节点。尝试不同的矩阵并探索 3D 图形的无限可能性。

## 常见问题解答

### Q1：我可以对单个 3D 节点应用多个变换吗？

A1：是的，您可以连接多个变换矩阵以进行复杂的变换。

### Q2：如何在Aspose.3D中旋转3D对象？

A2：在变换矩阵中使用适当的旋转矩阵来实现所需的旋转。

### Q3：我可以创建的 3D 场景的大小有限制吗？

A3：3D 场景的大小可能会受到系统资源的限制，但 Aspose.3D 是为了提高效率而设计的。

### Q4：在哪里可以找到更多示例和文档？

 A4：访问[Aspose.3D 文档](https://reference.aspose.com/3d/java/)了解更多示例和详细信息。

### Q5：如何获得Aspose.3D的临时许可证？

 A5：您可以获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).