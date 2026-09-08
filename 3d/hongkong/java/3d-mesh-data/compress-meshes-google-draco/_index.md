---
date: 2026-09-08
description: 透過在 Java 中生成球形網格並使用 Google Draco（透過 Aspose.3D）壓縮，學習如何在短時間內減少 3D 模型大小。
keywords:
- how to reduce 3d model size
- aspose 3d java
- draco mesh compression
- java sphere mesh
- 3d model optimization
lastmod: 2026-09-08
linktitle: 如何減少 3D 模型大小 – 使用 Google Draco 在 Java 中建立球形網格
og_description: 透過在 Java 中建立球形網格並使用 Google Draco（搭配 Aspose.3D）壓縮，快速將 .drc 檔案縮小至原始大小的
  95%。
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: 如何使用 Java 球形網格和 Draco 減少 3D 模型大小
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: 如何使用 Java 球形網格和 Draco 減少 3D 模型大小
url: /zh-hant/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用 Java 球體網格與 Draco 減少 3D 模型大小

## 介紹

如果您正在尋找一種快速的方式來 **減少 3D 模型大小** 同時仍能提供高品質的幾何體，您已經來對地方了。在本教學中，我們將示範如何使用 **Aspose.3D for Java** 產生球體網格，然後使用 **Google Draco** 進行壓縮。完成後，您將得到一個可直接使用的 `.drc` 檔案，其大小遠小於原始檔案，非常適合網頁檢視器、行動遊戲或任何頻寬受限的 Java 應用程式。

## 快速答覆
- **本教學涵蓋什麼內容？** 使用 Java 建立球體網格，並透過 Aspose.3D 使用 Google Draco 進行壓縮。  
- **主要使用的函式庫？** Aspose.3D for Java（用於網格建立與 Draco 匯出）。  
- **一般實作時間？** 基本球體大約需要 10‑15 分鐘。  
- **主要前置條件？** 具備 Aspose.3D JAR 位於 classpath 的 Java 開發環境。  
- **結果？** 一個 `.drc` 檔案，可 **減少 3D 模型大小** 高達 95 %，相較於未壓縮的網格。

## 如何減少 3D 模型大小？

`Sphere` 類別根據給定的半徑與細分參數產生三角化的球體幾何。使用 `new Sphere(1.0, 32, 32)` 建立球體，然後透過 `scene.save("sphere.drc", SaveFormat.Draco)` 直接匯出為 Draco。`scene.save` 方法會將目前的場景寫入指定格式的檔案。Aspose.3D 於內部處理轉換，讓您免除手動編碼步驟。Draco 匯出器會自動套用幾何量化與頂點去重，產生的檔案通常可縮小 80‑95 %，同時保留視覺品質。

## 在 3D 開發中「減少 3D 模型大小」是什麼意思？

**減少 3D 模型大小** 意指在不明顯降低視覺品質的前提下，縮減需要傳輸或儲存的幾何資料量。Draco 透過將頂點位置、法線及其他屬性編碼為高度緊湊的二進位格式來達成此目的。結合 Aspose.3D 後，整個工作流程皆在 Java 內部完成，無需處理原生二進位檔案。

## 為什麼在 Aspose.3D 中使用 Google Draco 網格壓縮？

Google Draco 結合 Aspose.3D 提供高效的管線，能大幅縮減網格檔案大小，同時保持在 Java 專案中易於整合。此函式庫處理所有低階編碼，讓開發者專注於幾何建立，而不必面對原生 Draco 二進位檔，從而加快開發速度並為網頁與行動裝置提供更小的資產。

- **巨大的尺寸縮減：** Draco 可將典型模型的網格資料縮減最高 95 %，例如將 5 MB 的 OBJ 轉為 0.3 MB 的 `.drc`。  
- **快速的執行時解碼：** Unity、Unreal 與 three.js 等引擎原生支援 Draco 解碼，縮短載入時間。  
- **無縫的 Java 整合：** Aspose.3D 抽象化原生 Draco 函式庫，讓您保持在 Java 生態系統中。  
- **一站式 Aspose 3D 匯出：** 同一套 API 可同時建立幾何與匯出，簡化工作流程。

## 前置條件

- **Java Development Kit (JDK)** – 8 版或更新版本。  
- **Aspose.3D for Java** – 從 **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)** 下載最新的 JAR。  
- **具備 Google Draco 的基本概念** – 您將使用 Aspose.3D 的封裝，無需自行設定原生 Draco。

## 匯入套件

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## 步驟說明

### 步驟 1：設定專案

建立一個新的 Java 專案（任何 IDE 都可），並將所有 Aspose.3D JAR 加入 classpath。為了清晰起見，建議將來源檔案放在如 `com.example.draco` 的套件下。

### 步驟 2：在 Java 中建立球體網格

`Sphere` 類別是 Aspose.3D 內建的幾何產生器，可產生可設定半徑與細分程度的三角化網格。  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **專業提示：** `Sphere` 類別會以預設半徑 1.0 產生三角化網格。若在壓縮前需要不同的細節層級，您可以傳入自訂的半徑、細分或材質參數。

### 步驟 3：將網格匯出為 Draco 格式

將球體加入 `Scene` 物件後，呼叫 `scene.save("sphere.drc", SaveFormat.Draco)`。Aspose.3D 會自動選擇最佳壓縮設定，但若需要最小檔案，可透過調整 `DracoCompressionOptions` 進行微調。`DracoCompressionOptions` 允許您自訂 Draco 的壓縮設定，例如量化與壓縮等級。

### 步驟 4：驗證輸出

使用 Draco 檢視器（例如 three.js 的 `DRACOLoader`）開啟產生的 `.drc` 檔案，以確認幾何正確渲染。您會發現檔案大小大幅縮減，通常可減少至原來的十分之一甚至更少。

## 常見使用情境

| 情境 | 為何要減少模型大小？ | 本教學如何協助 |
|----------|-----------------------|--------------------------|
| 基於網頁的產品配置器 | 在慢速連線下加快頁面載入 | Draco 壓縮的 `.drc` 檔案可在數秒內載入 |
| 行動 AR/VR 應用程式 | 降低裝置記憶體佔用 | 較小的網格讓應用保持回應 |
| 雲端渲染場景 | 降低頻寬成本 | 一鍵從 Aspose.3D 匯出至 Draco |

## 常見問題與解決方案

| 問題 | 原因 | 解決方式 |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D JAR 未加入 classpath | 確認已包含 *所有* Aspose.3D JAR 檔案，且版本與文件說明相符。 |
| **Output file is empty** | `MyDir` 指向不存在的資料夾 | 在寫入檔案前，以程式方式建立目錄 (`Files.createDirectories(Paths.get(MyDir))`)。 |
| **Compressed mesh looks distorted** | 使用過低的壓縮等級或細分不足 | 改用 `DracoCompressionLevel.OPTIMAL`，並提升球體的細分程度（例如 `new Sphere(1.0, 64, 64)`）。`DracoCompressionLevel.OPTIMAL` 會為 Draco 輸出選擇最高的壓縮品質。 |

## 常見問答

**Q: Aspose.3D 是否相容於不同的 3D 檔案格式？**  
A: 是的，Aspose.3D 支援 OBJ、FBX、STL、GLTF 等多種格式，是 **Aspose 3D 匯出** 工作流程的多功能選擇。

**Q: 我可以在其他程式語言中使用 Google Draco 進行壓縮嗎？**  
A: 當然可以。Draco 提供 C++、Python 與 JavaScript 的原生函式庫。本教學以 Java 為例，但概念可跨語言應用。

**Q: 我在哪裡可以找到更多 Aspose.3D 文件？**  
A: 請前往 **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** 取得完整的 API 參考與更多範例。

**Q: 如何取得 Aspose.3D 的臨時授權？**  
A: 可在 **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)** 探索臨時授權方案。

**Q: 有 Aspose.3D 的社群論壇嗎？**  
A: 有，請加入 **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)** 參與討論。

## 結論

本指南示範了如何透過在 Java 中建立球體網格，並使用 Aspose.3D 透過 Google Draco 進行壓縮，以 **減少 3D 模型大小**。依照這些簡潔步驟，您可以大幅縮小網格檔案、提升載入速度，並讓基於 Java 的 3D 應用保持回應迅速且節省頻寬。

---

**Last Updated:** 2026-09-08  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

## 相關教學

- [Reduce 3D File Size – Compress Scenes with Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Generate a Draco point cloud from spheres using Aspose.3D for Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Learn How to Triangulate Meshes for Optimized Rendering in Java Using Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}