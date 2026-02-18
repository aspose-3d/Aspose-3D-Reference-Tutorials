---
date: 2026-02-17
description: 学习如何在 Java 3D 中使用 Aspose.3D 将网格转换为 FBX，同时设置材质颜色并共享网格几何数据。
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: 将网格转换为 FBX 并在 Java 3D 中设置材质颜色
url: /zh/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Java 3D 中将网格转换为 FBX 并设置材质颜色

## 介绍

如果您正在构建基于 Java 的 3D 应用程序，通常需要在多个对象之间复用相同的几何体，同时为每个实例赋予独特的外观。在本教程中，您将学习**如何将网格转换为 FBX**，在多个节点之间共享底层网格几何体，并**为每个节点设置不同的材质颜色**。完成后，您将拥有一个可直接导出的 FBX 场景，可放入任何引擎或查看器中。

## 快速回答
- **主要目标是什么？** 将网格转换为 FBX，共享网格几何体，并为每个节点设置不同的材质颜色。  
- **需要哪个库？** Aspose.3D for Java。  
- **如何导出结果？** 使用 `FileFormat.FBX7400ASCII` 将场景保存为 FBX 文件。  
- **是否需要许可证？** 生产使用时需要临时或完整许可证。  
- **哪个 Java 版本可用？** 任意 Java 8 及以上环境。

## 什么是 **convert mesh to FBX**？

`convert mesh to fbx` 是指将内存中创建或操作的网格对象写入 FBX 文件格式的过程，FBX 被 Maya、Blender、Unity 等 3D 工具广泛支持。Aspose.3D 负责繁重的工作，您只需使用适当的 `FileFormat` 调用 `scene.save(...)` 即可。

## 为什么要共享网格几何数据？

共享几何体可以减少内存消耗并加快渲染，因为底层顶点缓冲区只存储一次。该技术非常适用于包含大量重复对象的场景——比如森林、人群或模块化建筑——其中每个实例仅在变换或材质上有所不同。

## 先决条件

在开始教程之前，请确保已具备以下先决条件：

- **Java 开发环境** – 任意带有 Java 8 或更高版本的 IDE 或命令行环境。  
- **Aspose.3D 库** – 从官方网站下载最新的 JAR 包：[here](https://releases.aspose.com/3d/java/)。

## 导入包

首先在 Java 项目中导入必要的包。此步骤对于访问 Aspose.3D 库提供的功能至关重要。

```java
import com.aspose.threed.*;
```

## 步骤 1：初始化场景对象（initialize scene java）

让我们通过初始化场景对象来开始此过程。它将作为我们 3D 魔法展开的画布。

```java
// Initialize scene object
Scene scene = new Scene();
```

## 步骤 2：定义颜色向量

在此步骤中，我们定义一个颜色向量数组，用于应用于 3D 场景的不同元素。

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## 步骤 3：使用多边形构建器创建 3D 网格 Java（create 3d mesh java）

利用 Common 类通过多边形构建器方法创建网格。该网格将作为我们 3D 元素的基础。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## 如何为每个节点设置材质颜色？

遍历颜色向量，创建立方体节点，并设置材质、**set material color** 和平移等属性。这是控制每个网格实例视觉外观的核心。

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## 步骤 5：保存 3D 场景（save scene fbx，convert mesh to fbx）

指定用于保存 3D 场景的目录和文件名，使用受支持的文件格式，此处为 FBX7400ASCII。此步骤还演示了 **convert mesh to FBX**。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## 常见陷阱与技巧

- **路径问题** – 在追加文件名之前，确保目录路径以文件分隔符 (`/` 或 `\\`) 结尾。  
- **许可证初始化** – 如果在调用 `scene.save` 之前忘记设置 Aspose.3D 许可证，库将以试用模式运行，可能会嵌入水印。  
- **材质覆盖** – 为多个节点重复使用同一个 `LambertMaterial` 实例会导致所有节点共享相同颜色。始终在每次迭代中创建新的材质，如上所示。  
- **大型网格** – 对于拥有数百万顶点的网格，考虑使用带索引多边形的 `MeshBuilder`，以保持 FBX 文件大小在可控范围。

## 其他常见问题

**Q1: 我可以将 Aspose.3D 与其他 Java 框架一起使用吗？**  
A1: 可以，Aspose.3D 旨在与各种 Java 框架无缝配合。

**Q2: Aspose.3D 有哪些授权选项？**  
A2: 有，您可以在此处查看授权选项 [here](https://purchase.aspose.com/buy)。

**Q3: 如何获取 Aspose.3D 的支持？**  
A3: 请访问 Aspose.3D [forum](https://forum.aspose.com/c/3d/18) 获取支持和讨论。

**Q4: 是否提供免费试用？**  
A4: 有，您可以在此获取免费试用 [here](https://releases.aspose.com/)。

**Q5: 如何获取 Aspose.3D 的临时许可证？**  
A5: 您可以在此获取临时许可证 [here](https://purchase.aspose.com/temporary-license/)。

## 结论

恭喜！您已成功**将网格转换为 FBX**，在多个节点之间共享网格几何数据，并使用 Aspose.3D for Java 为每个节点设置了独立的材质颜色。此工作流为您提供了轻量级、可复用的网格架构，可导出到任何兼容 FBX 的管线中。

---

**最后更新：** 2026-02-17  
**测试环境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}