---
title: 使用 Aspose.3D LoadOptions 在 Java 中自定义 3D 文件加载
linktitle: 使用 Aspose.3D LoadOptions 在 Java 中自定义 3D 文件加载
second_title: Aspose.3D Java API
description: 使用 Aspose.3D 可定制的 LoadOptions 增强 Java 中的 3D 文件加载。了解 3DS、OBJ、STL、U3D、glTF、PLY、X 和可选 FBX 的逐步自定义。
weight: 12
url: /zh/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D LoadOptions 在 Java 中自定义 3D 文件加载

## 介绍

在不断发展的 3D 设计和开发领域，高效处理 3D 文件格式至关重要。 Aspose.3D for Java 提供了强大的解决方案来自定义加载各种 3D 文件格式。本教程将指导您完成使用 Aspose.3D 的 LoadOptions 在 Java 中自定义 3D 文件加载的过程。

## 先决条件

在深入定制过程之前，请确保您具备以下条件：

- 对 Java 编程有基本的了解。
- 安装了 Java 开发工具包 (JDK)。
- 下载 Aspose.3D for Java 库。您可以获得它[这里](https://releases.aspose.com/3d/java/).
- 熟悉 3D 文件格式，例如 3DS、OBJ、STL、U3D、glTF、PLY、X 和 FBX。

## 导入包

在您的 Java 项目中，确保导入必要的 Aspose.3D 包：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 自定义 3D 文件加载

### 第 1 步：自定义 3DS 文件加载

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### 第2步：自定义OBJ文件加载

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### 第 3 步：自定义 STL 文件加载

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### 第 4 步：自定义 U3D 文件加载

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### 第5步：自定义glTF文件加载

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### 第6步：自定义PLY文件加载

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### 第7步：自定义X文件加载

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### 第 8 步：自定义 FBX 文件加载（可选）

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## 结论

使用 Aspose.3D 的 LoadOptions 在 Java 中自定义 3D 文件加载，使开发人员能够根据特定要求定制导入过程。无论是调整动画变换、翻转坐标系还是处理外部依赖性，Aspose.3D 都提供了无缝集成所需的灵活性。

## 常见问题解答

### Q1：在哪里可以找到 Aspose.3D for Java 文档？

 A1：文档可用[这里](https://reference.aspose.com/3d/java/).

### Q2: 如何下载 Aspose.3D for Java？

 A2：可以下载[这里](https://releases.aspose.com/3d/java/).

### Q3：有免费试用吗？

 A3：是的，您可以免费试用[这里](https://releases.aspose.com/).

### 问题 4：在哪里可以获得 Aspose.3D for Java 的支持？

A4：访问支持论坛[这里](https://forum.aspose.com/c/3d/18).

### Q5：测试需要临时许可证吗？

 A5：是的，获得临时许可证[这里](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
