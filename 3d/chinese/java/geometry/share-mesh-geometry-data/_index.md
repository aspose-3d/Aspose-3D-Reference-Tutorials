---
date: 2025-12-12
description: 学习如何在使用 Aspose.3D 的 Java 3D 中共享网格几何数据并将场景保存为 FBX 时设置材质颜色。
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: 在 Java 3D 中使用 Aspose.3D 设置材质颜色并共享网格几何数据
url: /zh/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 设置材质颜色并在 Java 3D 中共享网格几何数据（使用 Aspose.3D）

## 介绍

踏上使用 Aspose.3D 进行 Java 3D 开发的旅程，将为您打开创建惊艳可视化和沉浸式体验的无限可能。在本教程中，我们将指导您 **如何共享网格** 几何数据，并展示 **如何为每个网格实例设置材质颜色** 的完整步骤。请仔细按照每一步操作，最终您将能够在多个节点之间无缝交换网格数据，同时控制颜色并导出为 FBX。

## 快速回答
- **主要目标是什么？** 为每个节点设置材质颜色并共享网格几何数据。  
- **需要哪个库？** Aspose.3D for Java。  
- **如何导出结果？** 将场景保存为 FBX 文件（FBX7400ASCII）。  
- **是否需要许可证？** 生产环境需要临时或正式许可证。  
- **支持哪些 Java 版本？** 任意 Java 8 及以上环境。

## 前置条件

在开始教程之前，请确保您已具备以下条件：

- **Java 开发环境**：确保系统已安装并配置好 Java 开发环境。  
- **Aspose.3D 库**：下载并安装 Aspose.3D 库。您可以在此处获取库 [here](https://releases.aspose.com/3d/java/)。

## 导入包

在 Java 项目中导入必要的包，以便使用 Aspose.3D 提供的功能。

```java
import com.aspose.threed.*;
```

## 步骤 1：初始化场景对象（initialize scene java）

让我们通过初始化场景对象来开启本次操作。该对象将作为我们 3D 魔法展开的画布。

```java
// Initialize scene object
Scene scene = new Scene();
```

## 步骤 2：定义颜色向量

在此步骤中，我们定义一个颜色向量数组，用于为场景中的不同元素指定颜色。

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## 步骤 3：使用多边形构建器创建 3D 网格（create 3d mesh java）

利用 Common 类通过多边形构建器方法创建网格。该网格将作为我们 3D 元素的基础。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## 如何为每个节点设置材质颜色？

遍历颜色向量，创建立方体节点，并设置材质、**设置材质颜色**以及平移等属性。这是控制每个网格实例视觉外观的核心步骤。

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

指定目录和文件名，以受支持的文件格式（本例为 FBX7400ASCII）保存 3D 场景。此步骤还演示了 **将网格转换为 FBX** 的过程。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## 结论

恭喜！您已经成功 **设置材质颜色**，在多个节点之间共享网格几何数据，并使用 Aspose.3D for Java 将结果导出为 FBX 文件。这为创建视觉惊艳且交互式的 3D 应用程序提供了无限可能。

## 常见问题

### Q1: 我可以在其他 Java 框架中使用 Aspose.3D 吗？

A1: 可以，Aspose.3D 设计为能够无缝兼容各种 Java 框架。

### Q2: Aspose.3D 有哪些授权选项？

A2: 您可以在此处查看授权选项 [here](https://purchase.aspose.com/buy)。

### Q3: 如何获取 Aspose.3D 的技术支持？

A3: 请访问 Aspose.3D [forum](https://forum.aspose.com/c/3d/18) 获取支持和讨论。

### Q4: 是否提供免费试用？

A4: 可以，免费试用请前往 [here](https://releases.aspose.com/)。

### Q5: 如何获取 Aspose.3D 的临时许可证？

A5: 您可以在此获取临时许可证 [here](https://purchase.aspose.com/temporary-license/)。

## 其他常见问题

**Q: 我可以将场景导出为除 FBX 之外的其他格式吗？**  
A: 可以，Aspose.3D 支持 OBJ、STL、3MF 等格式，只需在 `save` 调用中更改 `FileFormat` 枚举即可。

**Q: 场景创建后，我需要更改材质怎么办？**  
A: 获取对应节点，修改其 `LambertMaterial`（例如 `setDiffuseColor`），然后重新保存场景。

**Q: 该库能高效处理大型网格吗？**  
A: Aspose.3D 使用了优化的数据结构；但对于极大型网格，建议使用流式处理或拆分场景。

**Q: 是否可以为颜色变化添加动画？**  
A: 可以，使用 `AnimationController` API 对材质属性进行动画处理。

---

**最后更新：** 2025-12-12  
**测试环境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}