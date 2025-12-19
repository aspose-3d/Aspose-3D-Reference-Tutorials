---
date: 2025-12-19
description: 學習如何使用 Aspose.3D LoadOptions 自訂 3D 載入 Java。逐步指南涵蓋 3DS、OBJ、STL、U3D、glTF、PLY、X
  以及可選的 FBX 檔案。
linktitle: Customize 3D Loading Java – How to customize 3d loading java with Aspose.3D
  LoadOptions
second_title: Aspose.3D Java API
title: 自訂 3D 載入 Java – 如何使用 Aspose.3D LoadOptions 自訂 3D 載入 Java
url: /zh-hant/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 自訂 3D Loading Java – 如何使用 Aspose.3D LoadOptions 自訂 3D Loading Java

## Introduction

在現代的 3D 應用程式中，**customize 3d loading java** 是確保模型能夠如預期呈現、且不受來源格式限制的關鍵。無論您是在打造遊戲引擎、AR/VR 觀賞器，或是 CAD 轉換工具，能夠掌控 3DS、OBJ、STL、U3D、glTF、PLY、X 甚至 FBX 檔案的匯入方式，都能為您節省大量後處理時間。本教學將逐步說明如何在 Java 中使用 Aspose.3D 彈性的 `LoadOptions` 類別，自訂 3D 檔案的載入行為。

## Quick Answers
- **What does “customize 3d loading java” mean?** 它是指設定 Aspose.3D 的 `LoadOptions`，以控制匯入行為，例如座標系翻轉、材質處理與動畫變換。  
- **Which formats can I customize?** 3DS、OBJ、STL、U3D、glTF、PLY、X 以及可選的 FBX。  
- **Do I need a license to try this?** 需要臨時授權才能完整使用功能；同時也提供免費試用版。  
- **Is any additional data required?** 您可能需要提供外部資源（如貼圖或材質庫）的查找路徑。  
- **Where can I find the latest Aspose.3D for Java version?** 請參閱下方的官方下載頁面。

## What is “customize 3d loading java”?

在 Java 中自訂 3D 載入即是讓您決定 Aspose.3D 引擎如何解讀傳入的檔案。透過調整各種 `*LoadOptions` 類別的屬性，您可以：

* 翻轉座標系以符合您的渲染管線。  
* 為效能關鍵情境啟用或停用材質載入。  
* 套用 gamma 校正、動畫變換，或保留 FBX 檔案的內建全域設定。

## Why use Aspose.3D LoadOptions?

* **Fine‑grained control** – 為每種格式分別調整設定。  
* **Cross‑format consistency** – 在所有支援的檔案類型上套用相同的座標系規則。  
* **Performance optimization** – 在不需要時跳過不必要的資料（例如材質）。

## Prerequisites

在開始之前，請確保您已具備：

- 扎實的 Java 基礎。  
- 已安裝 JDK 8 或更高版本。  
- 從官方網站下載的 Aspose.3D for Java 程式庫 — 您可以在 [此處](https://releases.aspose.com/3d/java/) 取得。  
- 對您將要處理的 3D 檔案格式（3DS、OBJ、STL、U3D、glTF、PLY、X、FBX）有基本了解。

## Import Packages

在您的 Java 專案中，匯入 Aspose.3D 核心類別以及標準 I/O 套件：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Customize 3D File Loading

以下提供每種支援格式的專屬方法。每段程式碼示範最常見的自訂設定，您可依需求調整屬性以符合自己的管線。

### Step 1: Customize 3DS File Loading  

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

*Why this matters:* 啟用 `ApplyAnimationTransform` 可確保任何內嵌的動畫資料遵循目標座標系，而 `GammaCorrectedColor` 則可修正在不同渲染引擎間切換時常見的顏色強度問題。

### Step 2: Customize OBJ File Loading  

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

*Tip:* 若載入的 OBJ 檔案會參照外部的 `.mtl` 材質檔，請將 `EnableMaterials` 設為 `true`，並確保查找路徑指向該資料夾。

### Step 3: Customize STL File Loading  

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

*Pro tip:* STL 檔案僅包含幾何資訊，通常只需要翻轉座標系即可。

### Step 4: Customize U3D File Loading  

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Step 5: Customize glTF File Loading  

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

*Why flip V texture coordinates?* 許多 glTF 匯出工具使用的 UV 原點與傳統 DirectX 管線不同；翻轉 `TexCoordV` 可使貼圖正確對齊。

### Step 6: Customize PLY File Loading  

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Step 7: Customize X File Loading  

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Step 8: Customize FBX File Loading (Optional)  

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

*When to use this:* FBX 檔案常內嵌全域設定（單位、上方向），保留這些設定可確保匯入的場景與原作者的意圖相符。

## Common Issues and Solutions

| Issue | Likely Cause | Fix |
|-------|---------------|-----|
| 貼圖顯示遺失 | 查找路徑未設定或大小寫不符 | 將正確的目錄加入 `loadOpts.getLookupPaths()`，並確認檔名大小寫 |
| 模型顯示顛倒 | 未為該格式啟用 `FlipCoordinateSystem` | 為相關的 `*LoadOptions` 設定 `setFlipCoordinateSystem(true)` |
| 顏色過於淡薄 | 3DS 的 gamma 校正未開啟 | 在 `Discreet3dsLoadOptions` 上呼叫 `setGammaCorrectedColor(true)` |
| FBX 動畫異常 | 全域設定被覆寫 | 使用 `setKeepBuiltinGlobalSettings(true)` |

## Frequently Asked Questions

### Q1: Where can I find the Aspose.3D for Java documentation?  
A1: 文件可於 [此處](https://reference.aspose.com/3d/java/) 取得。

### Q2: How can I download Aspose.3D for Java?  
A2: 您可在 [此處](https://releases.aspose.com/3d/java/) 下載。

### Q3: Is there a free trial available?  
A3: 有，免費試用版可在 [此處](https://releases.aspose.com/) 取得。

### Q4: Where can I get support for Aspose.3D for Java?  
A4: 請前往支援論壇 [此處](https://forum.aspose.com/c/3d/18)。

### Q5: Do I need a temporary license for testing?  
A5: 需要，請於 [此處](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

### Q6: Can I load multiple formats in a single scene?  
A6: 當然可以。為每種格式建立獨立的 `LoadOptions`，然後分別呼叫 `scene.open()`，場景會自動合併幾何體。

### Q7: How do I improve loading performance for large files?  
A7: 停用不必要的功能（例如 STL 的材質載入），並使用 `LookupPaths` 以避免重複 I/O。

### Q8: Is it possible to programmatically change the coordinate system after loading?  
A8: 可以，檔案開啟後可呼叫 `scene.getRootNode().rotate()` 或 `scene.getRootNode().scale()` 進行座標系調整。

---

**Last Updated:** 2025-12-19  
**Tested With:** Aspose.3D for Java 24.11（撰寫時的最新版本）  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}