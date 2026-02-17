---
date: 2026-01-27
description: 學習如何在 Java 中建立球體網格，並使用 Google Draco 及 Aspose.3D 壓縮 3D 網格檔案。一步一步的指南，助您高效開發
  3D。
linktitle: How to Create Sphere Mesh in Java – Compress 3D Meshes with Google Draco
second_title: Aspose.3D Java API
title: 在 Java 中如何建立球體網格 – 使用 Google Draco 壓縮 3D 網格
url: /zh-hant/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Java 中建立球體網格 – 使用 Google Draco 壓縮 3D 網格

## 介紹

如果你正在尋找 **如何在 Java 中建立球體** 網格，同時保持檔案尺寸極小，你來對地方了。在本教學中，我們將示範如何結合 **Aspose.3D** 與 **Google Draco** 來 **有效壓縮 3D 網格** 資料。完成後，你將得到一個已使用 Draco 壓縮的 `.drc` 球體網格檔案，載入速度更快，且在任何基於 Java 的 3D 應用程式中佔用的頻寬也大幅降低。

## 快速回答
- **本教學涵蓋什麼內容？** 在 Java 中建立球體網格，並使用 Google Draco 透過 Aspose.3D 進行壓縮。  
- **主要使用的函式庫？** Aspose.3D for Java。  
- **一般實作時間？** 基本球體大約需要 10‑15 分鐘。  
- **關鍵前置條件？** 已安裝 Java 開發環境，且 Aspose.3D JAR 已加入 classpath。  
- **最終成果？** 包含壓縮球體網格的 `.drc` 檔案。

## 在 3D 開發中，「如何建立球體」是什麼意思？

建立球體網格是指產生一組頂點、邊與面，以近似完美球形。Aspose.3D 的 `Sphere` 類別負責此繁重工作，為你提供乾淨的三角化網格，之後可進一步處理或壓縮。

## 為什麼要在 Aspose.3D 中使用 Google Draco 網格壓縮？

- **極大尺寸縮減：** 與未壓縮格式相比，Draco 可將網格資料縮小最高 90 %。  
- **快速執行時解碼：** 現代引擎如 Unity 與 three.js 原生支援 Draco 解碼，載入時間更快。  
- **無縫 Java 整合：** Aspose.3D 封裝了原生 Draco 函式庫，讓你全程留在 Java 生態系，無需處理原生二進位檔。

## 前置條件

在開始之前，請確保你已具備：

- **Java Development Kit (JDK)** – 已安裝 8 版或更新版本，且已正確設定。  
- **Aspose.3D for Java** – 從官方頁面[此處](https://releases.aspose.com/3d/java/)下載最新 JAR。  
- **Google Draco 基礎** – 了解 Draco 為幾何壓縮函式庫，我們將使用 Aspose.3D 的封裝來完成主要工作。

## 匯入套件

在 Java 原始檔中匯入建立網格與 Draco 壓縮所需的類別。

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

建立一個新的 Java 專案（使用你慣用的 IDE），並將 Aspose.3D JAR 加入專案的 classpath。將原始碼放在乾淨的套件中，例如 `com.example.draco`。

### 步驟 2：如何在 Java 中建立球體網格

接下來，我們產生一個簡單的球體模型，作為要壓縮的網格。

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **小技巧：** `Sphere` 類別會自動建立預設半徑為 1.0 的三角化網格。若需求不同，可自行調整半徑、細分程度與材質。

### 步驟 3：如何使用 Google Draco 壓縮網格

球體建立完成後，我們透過 Aspose.3D 的 `DracoSaveOptions` 來執行 Draco 壓縮。將壓縮等級設為 `OPTIMAL` 可在保留品質的同時取得最佳尺寸縮減。

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

### 步驟 4：儲存壓縮後的網格

最後，將壓縮後的位元組陣列寫入 `.drc` 檔案。此檔案可直接串流給客戶端或作為日後使用的儲存檔。

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

你可以將相同步驟套用於其他 3D 物件——立方體、客製模型或匯入的場景，只要更換幾何建立的呼叫即可。

## 常見問題與解決方案

| 問題 | 原因 | 解決方式 |
|------|------|----------|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D JAR 未加入 classpath | 確認所有 Aspose.3D JAR 已正確包含，且版本符合文件說明。 |
| **輸出檔案為空** | `MyDir` 指向不存在的資料夾 | 確認目錄已存在，或在寫入檔案前以程式碼自行建立。 |
| **壓縮後的網格變形** | 使用過低的壓縮等級 | 改為 `DracoCompressionLevel.OPTIMAL`，或在壓縮前提升網格細分度。 |

## 常見問答

**Q: Aspose.3D 是否支援多種 3D 檔案格式？**  
A: 是，Aspose.3D 支援包括 OBJ、FBX、STL、GLTF 等多種格式，適用於各種工作流程。

**Q: 我可以在其他程式語言中使用 Google Draco 進行壓縮嗎？**  
A: 當然可以。Draco 提供 C++、Python、JavaScript 等原生函式庫。本教學聚焦於 Java，但概念可跨語言套用。

**Q: 我在哪裡可以找到更多 Aspose.3D 文件？**  
A: 請造訪 [Aspose.3D Java 文件](https://reference.aspose.com/3d/java/) 取得完整 API 參考與範例。

**Q: 如何取得 Aspose.3D 的臨時授權？**  
A: 前往[此處](https://purchase.aspose.com/temporary-license/)了解臨時授權方案。

**Q: 有 Aspose.3D 的社群論壇嗎？**  
A: 有，請至 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 參與討論與支援。

## 結論

本教學示範了 **如何在 Java 中建立球體** 網格，並透過 Aspose.3D 使用 Google Draco **壓縮 3D 網格** 資料。依循這些步驟，你可以大幅減少網格檔案大小、提升載入速度，讓 Java 為基礎的 3D 應用程式保持流暢。

---

**最後更新：** 2026-01-27  
**測試環境：** Aspose.3D for Java 24.12（最新）  
**作者：** Aspose  

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
