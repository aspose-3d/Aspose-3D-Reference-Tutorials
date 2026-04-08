---
date: 2026-04-08
description: 学习如何在 Aspose.3D for Java 中创建带有顶部偏移的圆柱体，添加子节点 Java，设置顶部偏移，生成 3D 模型，并使用
  Aspose 临时许可证导出 OBJ。
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Aspose 临时许可证 – 创建具有偏移顶部的圆柱体（Java）
second_title: Aspose.3D Java API
title: Aspose 临时许可证 – 创建带偏移顶部的圆柱体（Java）
url: /zh/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose 临时许可证 – 创建带偏移顶部的圆柱体 (Java)

## 介绍

如果您希望在基于 Java 的 3D 场景中 **创建圆柱体** 并自定义顶部偏移，Aspose.3D 能让此过程变得简单直观。在本教程中，我们将逐步演示从场景搭建到将最终模型导出为 OBJ 文件的全部步骤，帮助您自信地将带偏移顶部的圆柱体集成到应用程序中。教程结束时，您还将了解 **aspose 临时许可证** 如何让您在无需完整购买的情况下评估这些功能。

## 快速答疑
- **使用的库是什么？** Aspose.3D for Java  
- **可以偏移圆柱体的顶部吗？** 可以，使用 `setOffsetTop`  
- **如何在 Java 中添加子节点？** 在根节点上调用 `createChildNode`  
- **可以导出为哪种格式？** Wavefront OBJ（`java export obj`）  
- **测试时需要许可证吗？** 可使用 **aspose 临时许可证** 进行评估  

## 什么是 Aspose 临时许可证？

**aspose 临时许可证** 是一种短期、免费的评估密钥，可在开发和测试期间解锁 Aspose.3D for Java 的全部功能。它会移除评估水印，并允许您生成 3D 模型文件（如 OBJ、STL 或 FBX），效果与付费许可证完全相同。

## 为什么选择 Aspose.3D for Java？

- **高级 API：** 无需管理底层网格数据。  
- **跨平台：** 兼容任何 JVM 环境。  
- **内置导出器：** 可直接保存为 OBJ、STL、FBX 等格式。  
- **可扩展：** 轻松添加子节点、应用变换，并与其他 Java 库集成。  

## 前置条件

在开始之前，请确保您已具备：

- **Java Development Kit (JDK)** – 已安装兼容版本。  
- **Aspose.3D for Java 库** – 从官方站点 [here](https://releases.aspose.com/3d/java/) 下载最新 JAR 包。  
- 您喜欢的 IDE（Eclipse、IntelliJ IDEA、NetBeans 等）。  

## 导入包

首先，导入我们需要的类。将以下语句放在 Java 文件的顶部：

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## 步骤指南

### 步骤 1：创建 Java 3D 场景

**java 3d scene** 充当所有 3D 对象的容器。

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### 步骤 2：初始化带偏移顶部的圆柱体

这里演示 **如何创建圆柱体** 并自定义顶部偏移。构造函数用于定义半径、高度、切片、堆叠以及圆柱体是否封闭。随后使用 `setOffsetTop` 移动顶部。

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### 步骤 3：添加子节点 Java – 附加第一个圆柱体

在场景的根节点下创建子节点，并将圆柱体移动到指定位置。

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### 步骤 4：初始化第二个圆柱体（无偏移）

为了对比，我们再添加一个没有偏移的普通圆柱体。

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### 步骤 5：添加子节点 Java – 附加第二个圆柱体

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### 步骤 6：Java 导出 OBJ – 将场景保存为 OBJ

最后，我们 **java export obj** 整个场景（包括两个圆柱体）为 Wavefront OBJ 文件，该格式被广泛的 3D 工具支持。

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

运行程序后，您将在指定目录中找到 `CustomizedOffsetTopCylinder.obj`，即可在 Blender、Maya 或任何其他 OBJ 兼容的查看器中打开。

## 如何在 Java 中生成 3D 模型并导出 OBJ

使用 `Scene.save(..., FileFormat.WAVEFRONTOBJ)` 结合 **aspose 临时许可证**，您可以快速 **生成 3d model** 文件，无需外部转换器。这在原型开发或与设计师共享资产时尤为便利。

## 实际应用场景

- **建筑可视化：** 偏移顶部的圆柱体可模拟向天花板收缩的柱子。  
- **机械零件：** 创建活塞或齿轮外壳等顶部表面需特意偏移的部件。  
- **游戏资产：** 动态生成多样化的柱形结构，减少手工建模工作量。

## 常见问题及解决方案

| 问题 | 原因 | 解决办法 |
|-------|--------|-----|
| **OBJ 文件为空** | 场景未正确保存或路径错误。 | 确认输出目录存在且具有写入权限。 |
| **未应用偏移** | 使用了旧版 Aspose.3D。 | 更新至支持 `setOffsetTop` 的最新库。 |
| **子节点不可见** | 变换未生效。 | 在创建子节点后调用 `getTransform().setTranslation`。 |

## 常见问答

**问：Aspose.3D 是否兼容不同的 Java IDE？**  
答：是的，能够无缝工作于 Eclipse、IntelliJ IDEA、NetBeans 等 IDE。

**问：我可以为创建的 3D 对象应用纹理吗？**  
答：当然！使用 `Material` 类即可分配纹理和表面属性。

**问：Aspose.3D 有哪些授权选项？**  
答：提供多种授权模式，您可以在 [here](https://purchase.aspose.com/buy) 了解详情。

**问：我该如何获取帮助或分享使用经验？**  
答：加入 Aspose.3D 社区论坛 [here](https://forum.aspose.com/c/3d/18) 获取支持和交流。

**问：是否提供用于测试的临时许可证？**  
答：是的，您可以在 [here](https://purchase.aspose.com/temporary-license/) 获取 **aspose 临时许可证** 进行评估。

---

**最后更新：** 2026-04-08  
**测试环境：** Aspose.3D for Java 24.12（最新）  
**作者：** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}