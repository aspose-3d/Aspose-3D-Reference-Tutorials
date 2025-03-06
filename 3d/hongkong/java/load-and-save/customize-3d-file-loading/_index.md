---
title: 使用 Aspose.3D LoadOptions 在 Java 中自訂 3D 檔案加載
linktitle: 使用 Aspose.3D LoadOptions 在 Java 中自訂 3D 檔案加載
second_title: Aspose.3D Java API
description: 使用 Aspose.3D 可自訂的 LoadOptions 增強 Java 中的 3D 檔案載入。了解 3DS、OBJ、STL、U3D、glTF、PLY、X 和可選 FBX 的逐步自訂。
weight: 12
url: /zh-hant/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D LoadOptions 在 Java 中自訂 3D 檔案加載

## 介紹

在不斷發展的 3D 設計和開發領域，高效處理 3D 檔案格式至關重要。 Aspose.3D for Java 提供了強大的解決方案來自訂載入各種 3D 檔案格式。本教學將引導您完成使用 Aspose.3D 的 LoadOptions 在 Java 中自訂 3D 檔案載入的過程。

## 先決條件

在深入定製過程之前，請確保您具備以下條件：

- 對 Java 程式設計有基本的了解。
- 安裝了 Java 開發工具包 (JDK)。
- 下載 Aspose.3D for Java 函式庫。您可以獲得它[這裡](https://releases.aspose.com/3d/java/).
- 熟悉 3D 檔案格式，例如 3DS、OBJ、STL、U3D、glTF、PLY、X 和 FBX。

## 導入包

在您的 Java 專案中，請確保匯入必要的 Aspose.3D 套件：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 自訂 3D 檔案加載

### 第 1 步：自訂 3DS 檔案加載

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

### 步驟2：自訂OBJ檔案加載

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### 第 3 步：自訂 STL 檔案加載

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### 第 4 步：自訂 U3D 檔案加載

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### 步驟5：自訂glTF檔案加載

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### 步驟6：自訂PLY檔案加載

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### 步驟7：自訂X檔案加載

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### 第 8 步：自訂 FBX 檔案載入（可選）

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

## 結論

使用 Aspose.3D 的 LoadOptions 在 Java 中自訂 3D 檔案加載，使開發人員能夠根據特定要求自訂匯入過程。無論是調整動畫變換、翻轉座標系或處理外部依賴性，Aspose.3D 都提供了無縫整合所需的靈活性。

## 常見問題解答

### Q1：在哪裡可以找到 Aspose.3D for Java 文件？

 A1：文檔可用[這裡](https://reference.aspose.com/3d/java/).

### Q2: 如何下載 Aspose.3D for Java？

 A2：可以下載[這裡](https://releases.aspose.com/3d/java/).

### Q3：有免費試用嗎？

 A3：是的，您可以免費試用[這裡](https://releases.aspose.com/).

### 問題 4：在哪裡可以獲得 Aspose.3D for Java 的支援？

A4：造訪支援論壇[這裡](https://forum.aspose.com/c/3d/18).

### Q5：測試需要臨時許可證嗎？

 A5：是的，獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
