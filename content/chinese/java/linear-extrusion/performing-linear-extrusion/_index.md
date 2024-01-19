---
title: 在 Aspose.3D for Java 中执行线性挤出
linktitle: 在 Aspose.3D for Java 中执行线性挤出
second_title: Aspose.3D Java API
description: 使用 Aspose.3D for Java 探索 3D 建模世界。学习轻松执行线性挤压。
type: docs
weight: 10
url: /zh/java/linear-extrusion/performing-linear-extrusion/
---
## 介绍

欢迎来到这个关于在 Aspose.3D for Java 中执行线性拉伸的综合教程！如果您希望使用 Java 增强 3D 建模技能，那么您来对地方了。在本教程中，我们将指导您完成使用 Aspose.3D（一个用于 3D 建模的强大 Java 库）执行线性挤压的过程。

## 先决条件

在深入学习本教程之前，请确保您具备以下先决条件：

1. Java 开发环境：确保您的计算机上设置有 Java 开发环境。

2.  Aspose.3D 库：下载并安装 Aspose.3D 库。你可以找到图书馆[这里](https://releases.aspose.com/3d/java/).

## 导入包

设置开发环境并安装 Aspose.3D 库后，就可以导入必要的包了。在您的 Java 代码中，包含以下内容：

```java
import com.aspose.threed.*;
```

让我们分解每个步骤以确保清晰的理解。

## 第1步：设置文档目录

定义文档目录的路径：

```java
String MyDir = "Your Document Directory";
```

这可确保生成的 3D 模型将保存在指定目录中。

## 第 2 步：初始化基础形状

创建一个矩形形状作为挤出的基本轮廓：

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

根据需要调整圆角半径以自定义形状。

## 步骤 3：执行线性挤压

在基础轮廓上执行线性挤压：

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

在这里，我们将形状拉伸 10 个单位，设置切片数量，启用居中，并应用扭曲和扭曲偏移。

## 第 4 步：创建 3D 场景

创建 3D 场景并将拉伸添加为子节点：

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## 第 5 步：保存 3D 场景

将生成的 3D 场景保存为 Wavefront OBJ 文件：

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

现在，您已经使用 Aspose.3D for Java 成功执行了线性挤出！

## 结论

恭喜！您已经了解了如何利用 Aspose.3D for Java 执行线性挤出。这个强大的库为您的 3D 建模项目打开了一个充满可能性的世界。

## 常见问题解答

### Q1：Aspose.3D 是否兼容所有 Java 版本？

A1：Aspose.3D 设计用于与 Java 1.6 及更高版本一起使用。

### Q2：我可以将Aspose.3D用于商业项目吗？

A2：是的，Aspose.3D 可用于个人和商业项目。检查许可详细信息[这里](https://purchase.aspose.com/buy).

### Q3：如何获得 Aspose.3D 的支持？

 A3：访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)寻求社区支持或考虑购买[临时执照](https://purchase.aspose.com/temporary-license/)以获得优质支持。

### Q4：Aspose.3D 中还有其他 3D 建模功能吗？

 A4：当然！探索广泛的文档[这里](https://reference.aspose.com/3d/java/)获取功能和示例的完整列表。

### Q5：Aspose.3D 有免费试用版吗？

 A5：是的，您可以免费试用[这里](https://releases.aspose.com/).