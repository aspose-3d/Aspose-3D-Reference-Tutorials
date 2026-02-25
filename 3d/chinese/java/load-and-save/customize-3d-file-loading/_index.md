---
date: 2026-02-25
description: 学习如何在 Java 中使用 Aspose.3D LoadOptions 翻转坐标系并自定义 3D 导入。针对 3DS、OBJ、STL、U3D、glTF、PLY、X
  以及可选的 FBX 的一步步指南。
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: 翻转坐标系 – 在 Java 中使用 Aspose.3D 自定义 3D 文件加载
url: /zh/java/load-and-save/customize-3d-file-loading/
weight: 12
---

 translate to Chinese: "最后更新：" etc. But maybe keep as is? The instruction: translate all text content naturally to Chinese. So translate those.

But need to keep URLs unchanged.

Also note "Aspose.3D for Java" is a product name; keep as is.

Let's craft.

Be careful with markdown formatting: headings (#). Keep same number of #.

Let's produce final.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Flip Coordinate System – Customize 3D File Loading in Java with Aspose.3D

在不断演进的 3D 设计与开发领域，**翻转坐标系**在导入模型时是常见需求。无论是将资产从右手坐标系转换为左手坐标系，还是需要使模型与引擎的轴约定保持一致，Aspose.3D for Java 都能提供细粒度的控制。本教程将演示如何使用 Aspose.3D 的 `LoadOptions` **自定义 3D 导入**，涵盖最流行的格式，如 3DS、OBJ、STL、U3D、glTF、PLY、X，以及可选的 FBX。

## 快速回答
- **“翻转坐标系”到底做了什么？** 它会交换 X/Y/Z 轴，以匹配目标坐标约定。  
- **哪些格式支持翻转？** 所有主流格式（3DS、OBJ、STL、U3D、glTF、PLY、X、FBX）均提供 `setFlipCoordinateSystem` 选项。  
- **需要额外的库吗？** 只需 Aspose.3D for Java 的 JAR；不需要外部转换器。  
- **可以同时加载材质吗？** 可以——对 OBJ 文件使用 `setEnableMaterials(true)`。  
- **生产环境需要许可证吗？** 非试用部署必须使用有效的 Aspose.3D 许可证。

## 什么是 “翻转坐标系”？
翻转坐标系会改变导入模型所使用的轴方向。当源文件的手性（右手坐标系或左手坐标系）与渲染引擎不同，若不进行翻转，模型会出现镜像或倒置的情况。

## 为什么要自定义 3D 导入？
自定义导入可以让您：
- 保留动画变换（`setApplyAnimationTransform`）。  
- 正确处理颜色（`setGammaCorrectedColor`）。  
- 通过 `getLookupPaths()` 解析外部资源路径。  
- 通过仅加载所需内容来优化内存使用。

## 前置条件

- 具备 Java 编程基础。  
- 已安装 Java Development Kit (JDK)。  
- 已下载 Aspose.3D for Java 库。您可以在 [此处](https://releases.aspose.com/3d/java/) 获取。  
- 熟悉 3DS、OBJ、STL、U3D、glTF、PLY、X、FBX 等 3D 文件格式。

## 导入包

在 Java 项目中，确保导入必要的 Aspose.3D 包：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 如何使用 LoadOptions 自定义 3D 导入

下面提供逐步代码片段，演示如何为每种受支持的格式启用 **翻转坐标系** 选项。将这些片段复制到项目中即可，只需将 `"Your Document Directory"` 替换为实际的资产路径。

### 步骤 1：自定义 3DS 文件加载

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

### 步骤 2：自定义 OBJ 文件加载

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### 步骤 3：自定义 STL 文件加载

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### 步骤 4：自定义 U3D 文件加载

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### 步骤 5：自定义 glTF 文件加载

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### 步骤 6：自定义 PLY 文件加载

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### 步骤 7：自定义 X 文件加载

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### 步骤 8：自定义 FBX 文件加载（可选）

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

## 常见问题与解决方案
- **模型加载后出现镜像** – 确认已为对应格式设置 `setFlipCoordinateSystem(true)`。  
- **材质缺失** – 对 OBJ 文件，确保 `setEnableMaterials(true)` 并且材质文件 (.mtl) 位于某个 lookup 路径下。  
- **纹理坐标上下颠倒** – 对 glTF，可能需要在翻转轴的同时使用 `setFlipTexCoordV(true)`。  
- **文件未找到错误** – 将包含外部资源（纹理、辅助文件）的目录加入 `loadOpts.getLookupPaths()`。

## 结论

通过利用 Aspose.3D 的 `LoadOptions`，您可以 **翻转坐标系** 并 **自定义 3D 导入**，几乎覆盖所有主流格式。这种控制力消除了后处理脚本的需求，确保资产首次加载即能正确渲染。

## 常见问答

### Q1: 在哪里可以找到 Aspose.3D for Java 文档？
A1: 文档可在 [此处](https://reference.aspose.com/3d/java/) 查看。

### Q2: 如何下载 Aspose.3D for Java？
A2: 您可以在 [此处](https://releases.aspose.com/3d/java/) 下载。

### Q3: 是否提供免费试用？
A3: 是的，免费试用可在 [此处](https://releases.aspose.com/) 获取。

### Q4: 在哪里可以获得 Aspose.3D for Java 的支持？
A4: 请访问支持论坛 [此处](https://forum.aspose.com/c/3d/18)。

### Q5: 测试时需要临时许可证吗？
A5: 需要，临时许可证可在 [此处](https://purchase.aspose.com/temporary-license/) 获取。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最后更新：** 2026-02-25  
**测试环境：** Aspose.3D for Java 24.11（最新）  
**作者：** Aspose