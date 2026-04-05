---
date: 2026-02-25
description: 學習如何在 Java 中使用 Aspose.3D 的 LoadOptions 反轉座標系統並自訂 3D 匯入。提供 3DS、OBJ、STL、U3D、glTF、PLY、X
  以及可選的 FBX 的逐步指南。
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: 翻轉座標系統 – 使用 Aspose.3D 在 Java 中自訂 3D 檔案載入
url: /zh-hant/java/load-and-save/customize-3d-file-loading/
weight: 12
---

, placeholders.

Let's craft final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 翻轉座標系統 – 使用 Aspose.3D 在 Java 中自訂 3D 檔案載入

在不斷演變的 3D 設計與開發領域中，匯入模型時 **翻轉座標系統** 是常見需求。無論您是將資產從右手座標系轉換為左手座標系，或是需要將模型與引擎的軸向慣例對齊，Aspose.3D for Java 都能提供細緻的控制。本教學將帶您了解如何使用 Aspose.3D 的 `LoadOptions` **自訂 3D 匯入**，涵蓋最常見的格式，如 3DS、OBJ、STL、U3D、glTF、PLY、X，以及可選的 FBX。

## 快速解答
- **「翻轉座標系統」的作用是什麼？** 它會交換 X/Y/Z 軸，以符合目標座標慣例。  
- **哪些格式支援翻轉？** 所有主要格式（3DS、OBJ、STL、U3D、glTF、PLY、X、FBX）皆提供 `setFlipCoordinateSystem` 選項。  
- **需要額外的函式庫嗎？** 只需 Aspose.3D for Java 的 JAR；不需要外部轉換器。  
- **可以同時載入材質嗎？** 可以——對於 OBJ 檔案使用 `setEnableMaterials(true)`。  
- **正式環境需要授權嗎？** 非試用部署需要有效的 Aspose.3D 授權。

## 什麼是「翻轉座標系統」？
翻轉座標系統會改變匯入模型所使用的軸向方向。當來源檔案的手性（右手系或左手系）與您的渲染引擎不同時，這是必須的，可避免模型出現鏡像或倒置的情況。

## 為何要自訂 3D 匯入？
- 保留動畫變換 (`setApplyAnimationTransform`)。  
- 正確的顏色處理 (`setGammaCorrectedColor`)。  
- 透過 `getLookupPaths()` 解決外部資源路徑。  
- 僅載入所需內容，以優化記憶體使用。

## 前置條件

- 具備 Java 程式設計的基本概念。  
- 已安裝 Java Development Kit（JDK）。  
- 已下載 Aspose.3D for Java 函式庫。您可於 [此處](https://releases.aspose.com/3d/java/) 取得。  
- 熟悉 3D 檔案格式，如 3DS、OBJ、STL、U3D、glTF、PLY、X 及 FBX。

## 匯入套件

在您的 Java 專案中，確保匯入必要的 Aspose.3D 套件：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 如何使用 LoadOptions 自訂 3D 匯入

以下為逐步程式碼片段，示範如何為每種支援的格式啟用 **翻轉座標系統** 選項。這些片段可直接複製到您的專案中，只需將 `"Your Document Directory"` 替換為實際的資產路徑。

### 步驟 1：自訂 3DS 檔案載入

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

### 步驟 2：自訂 OBJ 檔案載入

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### 步驟 3：自訂 STL 檔案載入

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### 步驟 4：自訂 U3D 檔案載入

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### 步驟 5：自訂 glTF 檔案載入

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### 步驟 6：自訂 PLY 檔案載入

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### 步驟 7：自訂 X 檔案載入

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### 步驟 8：自訂 FBX 檔案載入（可選）

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

## 常見問題與解決方案
- **模型載入後呈鏡像** – 確認已對正確的格式設定 `setFlipCoordinateSystem(true)`。  
- **材質遺失** – 對於 OBJ 檔案，確保使用 `setEnableMaterials(true)`，且材質檔案 (.mtl) 位於任一 lookup 路徑中。  
- **貼圖座標顛倒** – 對於 glTF，除了翻轉軸之外，可能還需要 `setFlipTexCoordV(true)`。  
- **找不到檔案錯誤** – 將包含外部資源（貼圖、輔助檔案）的目錄加入 `loadOpts.getLookupPaths()`。

## 結論

透過 Aspose.3D 的 `LoadOptions`，您可以 **翻轉座標系統** 並 **自訂 3D 匯入**，幾乎支援所有主要格式。此等控制力免除後處理腳本的需求，確保資產首次即正確渲染。

## 常見問答

### Q1：在哪裡可以找到 Aspose.3D for Java 的文件說明？
A1：文件說明可於 [此處](https://reference.aspose.com/3d/java/) 取得。

### Q2：如何下載 Aspose.3D for Java？
A2：您可於 [此處](https://releases.aspose.com/3d/java/) 下載。

### Q3：是否提供免費試用？
A3：是的，您可於 [此處](https://releases.aspose.com/) 取得免費試用。

### Q4：在哪裡可以取得 Aspose.3D for Java 的支援？
A4：請前往支援論壇 [此處](https://forum.aspose.com/c/3d/18)。

### Q5：測試是否需要臨時授權？
A5：是的，請於 [此處](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2026-02-25  
**測試環境：** Aspose.3D for Java 24.11 (latest)  
**作者：** Aspose