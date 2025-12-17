---
date: 2025-12-09
description: 学习如何使用 Aspose 在 Java 中创建底部倾斜的自定义圆柱体，完美用于 Java 3D 建模并将场景保存为 OBJ。
language: zh
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 如何使用 Aspose：在 Java 中创建底部倾斜的圆柱体
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用 Aspose：在 Java 中创建底部倾斜的圆柱体

## 介绍

在本实战教程中，您将了解 **如何使用 Aspose** 来构建底部倾斜的圆柱体——这是一种在 *java 3d 建模* 项目中常用的技术。我们将逐步演示从设置场景到将最终模型保存为 OBJ 文件的全部过程。完成后，您将拥有一段可复用的代码片段，可直接嵌入任何基于 Java 的 3D 应用程序中。

## 快速解答
- **“shear bottom” 是什么意思？** 它在 XY 平面上将圆柱体的底部倾斜指定的角度。  
- **哪个库负责 3D 数学计算？** Aspose.3D for Java 提供 `Cylinder` 和 `Vector2` 类。  
- **运行示例是否需要许可证？** 临时许可证可用于评估；生产环境需要正式许可证。  
- **我可以将模型导出为其他格式吗？** 可以——使用 `scene.save(..., FileFormat.WAVEFRONTOBJ)` 可生成 OBJ 文件。  
- **需要哪个 Java 版本？** JDK 8 或更高版本即可。

## 在 3D 建模上下文中，“how to use aspose” 是什么？

Aspose.3D for Java 是一个高级 API，抽象了 3D 几何、文件格式和变换的复杂性。您无需处理底层顶点缓冲区，只需调用直观的方法，如 `new Cylinder(...)`，其余工作由 Aspose 完成。

## 为什么在 Java 3D 建模中使用 Aspose？

- **快速开发：** 只需几行代码即可构建复杂形状。  
- **广泛的格式支持：** 可导出为 OBJ、STL、FBX 等多种格式。  
- **跨平台：** 在任何支持 Java 的操作系统上均可运行。  
- **一致的 API：** 相同的代码可用于桌面、服务器或 Android 环境。

## 前置条件

在开始之前，请确保您已具备以下条件：

- **Java Development Kit (JDK) 8+** 已在 IDE 中安装并配置。  
- **Aspose.3D for Java** 库已添加到项目类路径中。您可以从官方站点 [here](https://releases.aspose.com/3d/java/) 下载。  
- **临时或正式许可证**（试用时可选）。

## 导入包

首先，导入必要的 Aspose.3D 类和 Java 工具类：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步骤 1：创建场景

*场景* 是容纳所有 3D 对象、灯光和相机的容器。可以把它想象成放置圆柱体的舞台。

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## 步骤 2：创建圆柱体 1（底部倾斜）

现在我们创建第一个圆柱体，并对其底部应用剪切变换。`setShearBottom` 方法接受一个 `Vector2`，其中 X 分量表示沿 X 轴的剪切因子，Y 分量表示沿 Y 轴的剪切因子。

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

> **技巧提示：** 剪切因子 `0.83` 大约对应 47.5°；根据需要调整此数值以获得精确角度。

## 步骤 3：创建圆柱体 2（标准）

为了对比，我们将添加第二个未进行剪切的圆柱体。这有助于您在导出的 OBJ 文件中直接看到视觉差异。

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## 步骤 4：保存场景（如何将场景保存为 OBJ）

最后，我们将场景持久化到磁盘。`FileFormat.WAVEFRONTOBJ` 常量指示 Aspose 写入 OBJ 文件，该格式被 Blender、Maya 等 3D 编辑器广泛支持。

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **注意：** 将 `"Your Document Directory"` 替换为适合您环境的绝对或相对路径。

## 常见问题及解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| **圆柱体出现扁平** | 剪切因子不正确（超出 0‑1 范围） | 使用 0 到 1 之间的数值；在预览时逐步调整。 |
| **OBJ 文件在查看器中无法加载** | 缺少材质定义 | 为每个节点添加简单材质，或导出为 STL 进行仅几何测试。 |
| **运行时出现 LicenseException** | 没有有效的许可证文件 | 将 `Aspose.3D.lic` 放置在项目根目录，或使用 `License` 类以编程方式加载。 |

## 常见问答

### 问题 1：我可以将 Aspose.3D for Java 与其他 Java 3D 库一起使用吗？

**答：** Aspose.3D for Java 设计为独立使用。虽然可以与其他库集成，但它本身已提供大多数 3D 建模任务所需的完整功能。

### 问题 2：Aspose.3D 适合 3D 建模初学者吗？

**答：** 是的，Aspose.3D 提供友好的 API，抽象了底层细节，使其对初学者和有经验的开发者都易于使用。

### 问题 3：我在哪里可以找到 Aspose.3D for Java 的额外支持？

**答：** 访问 [Aspose.3D 论坛](https://forum.aspose.com/c/3d/18) 获取社区支持、教程和讨论。

### 问题 4：如何获取 Aspose.3D 的临时许可证？

**答：** 您可以在 [此处](https://purchase.aspose.com/temporary-license/) 获取临时许可证。

### 问题 5：我可以购买 Aspose.3D for Java 吗？

**答：** 是的，您可以在 [此处](https://purchase.aspose.com/buy) 购买 Aspose.3D for Java。

## 结论

我们已经演示了 **如何使用 Aspose** 创建两个圆柱体——一个底部倾斜，一个标准——并将结果保存为 OBJ 文件。该技术是构建更复杂 3D 模型（如定制零件、建筑构件或游戏资产）的基础。欢迎尝试不同的剪切值、半径和高度，以满足您的项目需求。

---

**最后更新：** 2025-12-09  
**测试环境：** Aspose.3D for Java 24.11（撰写时的最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}