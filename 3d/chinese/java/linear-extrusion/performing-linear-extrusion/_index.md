---
date: 2025-12-18
description: 学习如何在 Java 中使用 Aspose.3D 拉伸形状，创建 3D 场景，并轻松导出 Wavefront OBJ 文件。
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: 如何在 Java 中使用 Aspose.3D 进行线性挤出形状
url: /zh/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Aspose.3D for Java 中执行线性拉伸

## 介绍

## 快速答案
- **线性拉伸是什么？** 将二维轮廓沿直线路径延伸以创建三维实体。  
- **哪个库在 Java 中处理此功能？** Aspose.3D for Java。  
- **我可以导出为 OBJ 吗？** 可以，使用 Wavefront OBJ 导出功能。  
- **开发是否需要许可证？** 免费试用可用于测试；生产环境需要许可证。  
- **需要哪个 Java 版本？** Java 1.6 或更高。

## 什么是 “how to extrude shape”？
线性拉伸是 **3d modeling java** 中的基础技术，它通过沿定义的距离拉伸平面轮廓（例如矩形），将其转换为体积对象。此方法广泛用于创建机械零件、建筑构件和装饰模型。

## 为什么使用 Aspose.3D 进行线性拉伸？
- **完全控制** 几何体（切片、扭转、偏移）。  
- **无缝集成** 到 Java 项目——无需本地依赖。  
- **内置导出器** 支持流行格式，包括 Wavefront OBJ，使得 **generate 3d model** 文件的生成在下游流水线中变得轻松。

## 前置条件

在深入教程之前，请确保已满足以下前置条件：

1. **Java 开发环境** – JDK（1.6 或更新）以及您喜欢的 IDE。  
2. **Aspose.3D 库** – 从官方站点 **[here](https://releases.aspose.com/3d/java/)** 下载并安装库。

## 导入包

在设置好开发环境并安装 Aspose.3D 库后，导入必要的包：

```java
import com.aspose.threed.*;
```

### 步骤 1：设置文档目录

定义生成文件将保存的文件夹：

```java
String MyDir = "Your Document Directory";
```

> 这确保 **generate 3d model** 操作将 OBJ 文件写入已知位置。

### 步骤 2：初始化基础形状

创建一个矩形作为拉伸轮廓：

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

您可以调整圆角半径以获得圆角，或将其设为 `0` 以得到完美的矩形。

### 步骤 3：执行线性拉伸

现在我们沿 Z 轴拉伸矩形，添加切片，启用居中，并使用偏移应用扭转：

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **拉伸长度** – `10` 单位。  
- **切片数** – `100`，以获得平滑几何体。  
- **扭转** – `360°` 产生完整旋转。  
- **扭转偏移** – 将扭转原点移动到 `(10, 0, 0)`。

### 步骤 4：创建 3D 场景

创建一个场景容器并将拉伸体作为子节点添加。此步骤 **creates 3d scene** 可容纳多个对象：

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### 步骤 5：保存 3D 场景

将场景导出为 Wavefront OBJ 文件。这演示了 **wavefront obj export** 和 **save 3d obj** 功能：

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

运行代码后，您将在指定的目录中找到 `LinearExtrusion.obj`，可在任何 3D 查看器中打开或进一步处理。

## 常见问题及解决方案

| 问题 | 原因 | 解决方案 |
|-------|--------|-----|
| OBJ 文件为空 | 输出目录路径不正确或不可写 | 确认 `MyDir` 指向具有写入权限的现有文件夹。 |
| 未应用扭转 | 缺少 `setCenter(true)` | 确保已启用居中，或调整 `setTwistOffset` 的值。 |
| `LinearExtrusion` 编译错误 | 使用了旧版 Aspose.3D | 更新至最新的 Aspose.3D 版本。 |

## 常见问答

**问：Aspose.3D 与所有 Java 版本兼容吗？**  
答：Aspose.3D 支持 Java 1.6 及更高版本。

**问：我可以在商业项目中使用 Aspose.3D 吗？**  
答：可以，拥有有效许可证即可进行商业使用。您可以在 **[here](https://purchase.aspose.com/buy)** 获取。

**问：如果遇到问题，我可以在哪里获得支持？**  
答：访问 **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** 获取社区帮助，或购买 **[temporary license](https://purchase.aspose.com/temporary-license/)** 以获得高级支持。

**问：Aspose.3D 还提供哪些其他 3D 建模功能？**  
答：该库包括网格操作、布尔运算、纹理映射等。完整列表请参见 **[here](https://reference.aspose.com/3d/java/)**。

**问：是否提供免费试用？**  
答：是的，您可以在 **[here](https://releases.aspose.com/)** 下载试用版。

## 结论

您已经学习了使用 Aspose.3D for Java **how to extrude shape**，创建了 3D 场景，并将结果导出为 Wavefront OBJ 文件。此技术为各种 **3d modeling java** 项目打开了大门——从简单零件到复杂装配。探索诸如布尔运算或纹理映射等附加功能，以进一步丰富您的模型。

---

**最后更新：** 2025-12-18  
**测试环境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## 目标关键词：

**主要关键词（最高优先级）：**  
how to extrude shape

**次要关键词（支持）：**  
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj