---
date: 2026-04-29
description: 學習如何在 Java 中建立球體網格，並使用 Aspose.3D 搭配 Google Draco 進行壓縮，以減少 3D 模型大小——這是
  Aspose 3D 匯出的必備技巧。
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: 如何在 Java 中建立球體網格 – 使用 Google Draco 壓縮 3D 網格
second_title: Aspose.3D Java API
title: 減少 3D 模型大小：使用 Draco 在 Java 中建立球形網格
url: /zh-hant/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 縮減 3D 模型大小：在 Java 中使用 Draco 建立球體網格

## 簡介

如果您正在尋找一種快速的方式來 **縮減 3D 模型大小** 同時仍能提供高品質的幾何體，您已經來對地方了。在本教學中，我們將示範如何使用 **Aspose.3D for Java** 產生球體網格，然後使用 **Google Draco** 壓縮該網格。完成後，您將擁有一個可直接使用的 `.drc` 檔案，其大小遠小於原始檔案，非常適合網頁檢視器、行動遊戲或任何受頻寬限制的 Java 應用程式。

## 快速回答
- **本教學涵蓋什麼？** 在 Java 中建立球體網格，並透過 Aspose.3D 使用 Google Draco 進行壓縮。  
- **主要函式庫？** Aspose.3D for Java（用於網格建立與 Draco 匯出）。  
- **典型實作時間？** 基本球體大約需要 10‑15 分鐘。  
- **關鍵前置條件？** 具備 Aspose.3D JAR 位於 classpath 的 Java 開發環境。  
- **結果？** 一個 `.drc` 檔案，可 **縮減 3D 模型大小** 高達 90 %，相較於未壓縮的網格。

## 在 3D 開發中，「縮減 3D 模型大小」是什麼意思？

縮減 3D 模型大小指的是在不明顯降低視覺品質的前提下，減少需要傳輸或儲存的幾何資料量。Draco 透過將頂點位置、法線及其他屬性編碼為高度緊湊的二進位格式來達成此目的。結合 Aspose.3D 使用時，整個工作流程皆在 Java 內完成，無需處理原生二進位檔案。

## 為什麼在 Aspose.3D 中使用 Google Draco 網格壓縮？

- **大幅度縮減大小：** Draco 可將網格資料縮減至最高 90 %，相較於 OBJ 或 STL 等格式。  
- **快速執行時解碼：** 如 Unity、Unreal 以及 three.js 等引擎可原生解碼 Draco，從而加快載入速度。  
- **無縫 Java 整合：** Aspose.3D 封裝了原生 Draco 函式庫，讓您能留在 Java 生態系統中。  
- **一站式 Aspose 3D 匯出：** 建立幾何體時使用的相同 API 也負責匯出，簡化工作流程。

## 前置條件

- **Java Development Kit (JDK)** – 版本 8 或更新。  
- **Aspose.3D for Java** – 從官方頁面 [here](https://releases.aspose.com/3d/java/) 下載最新的 JAR。  
- **基本了解 Google Draco** – 您將使用 Aspose.3D 的封裝，無需自行設定原生 Draco。

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

## 步驟指南

### 步驟 1：設定專案

建立一個新的 Java 專案（任何 IDE 都可），並將所有 Aspose.3D JAR 加入 classpath。為了清晰起見，將來源檔案放在如 `com.example.draco` 的套件中。

### 步驟 2：在 Java 中建立球體網格

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **小技巧：** `Sphere` 類別會產生預設半徑為 1.0 的三角形網格。若在壓縮前需要不同的細節層級，您可以傳入自訂的半徑、細分或材質參數。

### 步驟 3：使用 Google Draco 壓縮網格

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

將壓縮等級設定為 `OPTIMAL` 可在保留視覺保真度的同時達到最大的尺寸縮減，直接協助您 **縮減 3D 模型大小**。

### 步驟 4：儲存壓縮後的網格

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

產生的 `SphereMeshtoDRC_Out.drc` 可串流給客戶端、儲存在 CDN，或直接由任何相容 Draco 的引擎載入。

## 常見使用情境

| 情境 | 為何縮減模型大小？ | 本教學如何協助 |
|----------|-----------------------|--------------------------|
| 基於網頁的產品配置器 | 在慢速連線下加快頁面載入 | Draco 壓縮的 `.drc` 檔案可在數秒內載入 |
| 行動 AR/VR 應用 | 降低裝置記憶體佔用 | 較小的網格讓應用保持回應 |
| 雲端渲染場景 | 降低頻寬成本 | 一鍵從 Aspose.3D 匯出至 Draco |

## 常見問題與解決方案

| 問題 | 原因 | 解決方案 |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D JAR 未在 classpath 中 | 確認已包含 *所有* Aspose.3D JAR 檔案，且版本符合文件說明。 |
| **輸出檔案為空** | `MyDir` 指向不存在的資料夾 | 在寫入檔案前，以程式方式建立目錄 (`Files.createDirectories(Paths.get(MyDir))`)。 |
| **壓縮後的網格變形** | 使用過低的壓縮等級或細分不足 | 切換至 `DracoCompressionLevel.OPTIMAL`，並提升球體的細分程度（例如 `new Sphere(1.0, 64, 64)`）。 |

## 常見問答

**Q: Aspose.3D 是否相容於不同的 3D 檔案格式？**  
A: 是的，Aspose.3D 支援 OBJ、FBX、STL、GLTF 等多種格式，是 **Aspose 3D export** 管線的多功能選擇。

**Q: 我可以在其他程式語言中使用 Google Draco 進行壓縮嗎？**  
A: 當然可以。Draco 提供 C++、Python 與 JavaScript 的原生函式庫。本教學聚焦於 Java，但概念可跨語言套用。

**Q: 在哪裡可以找到其他 Aspose.3D 文件？**  
A: 請前往 [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) 查看完整 API 參考與更多範例。

**Q: 如何取得 Aspose.3D 的臨時授權？**  
A: 可在 [here](https://purchase.aspose.com/temporary-license/) 探索臨時授權選項。

**Q: 是否有 Aspose.3D 的社群論壇支援？**  
A: 有，請加入 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 參與討論。

## 結論

在本指南中，我們示範了如何透過在 Java 中建立球體網格，並使用 Google Draco 透過 Aspose.3D 進行壓縮，以 **縮減 3D 模型大小**。遵循這些簡潔步驟，即可大幅縮小網格檔案、提升載入速度，並讓您的 Java 為基礎的 3D 應用保持回應迅速且節省頻寬。

---

**最後更新：** 2026-04-29  
**測試環境：** Aspose.3D for Java 24.12 (latest)  
**作者：** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}