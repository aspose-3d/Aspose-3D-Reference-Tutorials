---
title: 使用 Aspose.3D SaveOptions 优化 Java 中的 3D 文件保存
linktitle: 使用 Aspose.3D SaveOptions 优化 Java 中的 3D 文件保存
second_title: Aspose.3D Java API
description: 了解如何使用 Aspose.3D SaveOptions 优化 Java 中的 3D 文件保存。轻松增强性能并自定义输出。
weight: 16
url: /zh/java/load-and-save/optimize-3d-file-saving/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D SaveOptions 优化 Java 中的 3D 文件保存

## 介绍

Aspose.3D 是一个功能丰富的 Java 库，使开发人员能够无缝地使用 3D 模型。在保存 3D 文件时，SaveOptions 类提供了大量设置来根据您的要求微调输出。在本教程中，我们将探讨各种保存选项以及如何利用它们来优化流程。

## 先决条件

在我们深入学习本教程之前，请确保您具备以下先决条件：

-  Aspose.3D for Java：确保您已将 Aspose.3D 库集成到您的 Java 项目中。你可以下载它[这里](https://releases.aspose.com/3d/java/).

- Java 开发环境：在您的计算机上设置一个功能性的 Java 开发环境。

- 文档目录：创建一个要保存 3D 文件的目录，并记下其路径以供以后使用。

## 导入包

在您的 Java 项目中，导入使用 Aspose.3D 所需的包。这包括`Scene`类和各种 SaveOptions 类。下面是一个基本示例：

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

现在，让我们将每个示例分解为多个步骤来演示不同 SaveOptions 的用法。

## 第 1 步：在 GLTF SaveOption 中漂亮打印

这`prettyPrintInGltfSaveOption`方法允许您生成具有缩进 JSON 内容的 GLTF 文件，以方便人类阅读。

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    //初始化3D场景
    Scene scene = new Scene(new Sphere());
    
    //初始化 GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    //启用漂亮的打印以获得更好的可读性
    opt.setPrettyPrint(true);
    
    //保存 3D 场景
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## 第 2 步：HTML5 保存选项

这`html5SaveOption`方法演示如何将 3D 场景保存为 HTML5 文件，包括自定义选项。

```java
public static void html5SaveOption() throws IOException {
    //初始化场景
    Scene scene = new Scene();
    
    //创建一个带有圆柱体的子节点
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //设置子节点的属性
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    //向场景添加灯光
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    //初始化 HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    //自定义选项（例如，关闭网格和用户界面）
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    //将场景另存为 HTML5 文件
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

继续对其他 SaveOptions 方法进行类似的细分，例如`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions`， 和`drcSaveOptions`.

## 结论

通过学习这个综合教程，您已经了解了如何使用 Aspose.3D SaveOptions 优化 Java 中的 3D 文件保存。无论您是对漂亮打印的 GLTF 文件感兴趣还是对自定义 HTML5 输出感兴趣，Aspose.3D 都能为您提供增强 3D 图形工作流程的工具。

## 常见问题解答

### Q1：如何将资源嵌入到 glTF 文件中？

 A1：要嵌入资产，请使用`setEmbedAssets(true)`方法中的`GltfSaveOptions`班级。

### Q2：这样做的目的是什么？`setPositionBits` method in `DracoSaveOptions`?

 A2: 的`setPositionBits`方法设置 Draco 压缩算法中位置的量化位。

### Q3：我可以导出U3D文件中的普通数据吗？

 A3: 是的，您可以通过设置导出正常数据`setExportNormals(true)`在里面`U3dSaveOptions`班级。

### Q4：如何放弃 OBJ 导出中保存的材质文件？

A4：利用`setFileSystem(new DummyFileSystem())`方法中的`ObjSaveOptions`类丢弃材质文件。

### Q5：有没有办法将依赖项保存到 OBJ 文件中的本地目录？

 A5：是的，使用`setFileSystem(new LocalFileSystem(MyDir))`方法中的`ObjSaveOptions`类在本地保存依赖项。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
