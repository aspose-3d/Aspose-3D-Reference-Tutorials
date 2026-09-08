---
date: 2026-09-08
description: 了解如何在 Java 中使用 Aspose.3D 定義單位並匯出場景至 FBX。本分步指南說明如何設定應用程式名稱、測量單位，以及取得 3D
  場景資訊。
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: 如何在 Java 中儲存 FBX 並取得 3D 場景資訊
og_description: 了解如何在 Java 中使用 Aspose.3D 定義單位並匯出場景至 FBX。本指南涵蓋設定應用程式名稱、測量單位，以及在幾個步驟內取得
  3D 場景資訊。
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: 如何在 Java 中定義單位並匯出場景至 FBX
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: 如何在 Java 中定義單位並匯出場景至 FBX
url: /zh-hant/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Java 中定義單位並匯出場景為 FBX

## 簡介

如果您正在尋找一個清晰、實作導向的指南，說明 **how to define units** 與 **export a scene to FBX**，同時從 3D 場景中提取有用的中繼資料，您來對地方了。在本教學中，我們將使用 **Aspose.3D for Java** 函式庫逐步說明：從建立場景、**setting the application name**、**defining measurement units**，最後 **exporting the scene to FBX**。完成後，您將擁有一個可直接使用的 FBX 檔案，內含下游流程所需的資產資訊。

## 快速解答
- **主要目標是什麼？** 匯出包含自訂資產資訊的 FBX 場景。  
- **使用哪個函式庫？** Aspose.3D for Java。  
- **我需要授權嗎？** 免費試用版可用於開發；正式環境需要商業授權。  
- **我可以更改測量單位嗎？** 可以 – 使用 `setUnitName` 和 `setUnitScaleFactor`。  
- **輸出會儲存在哪裡？** 儲存在您於 `scene.save(...)` 指定的路徑。  

## 先決條件

在開始之前，請確保您已具備：

- 對核心 Java 語法有扎實的了解。  
- **Aspose.3D for Java** 已下載並加入您的專案（您可從官方取得）[Aspose 3D download page](https://releases.aspose.com/3d/java/)。  
- 您喜愛的 Java IDE（IntelliJ IDEA、Eclipse、NetBeans 等）已正確設定。

## 匯入套件

在您的 Java 原始碼檔案中，匯入提供場景處理與檔案格式支援的 Aspose.3D 類別。

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **小技巧：** 保持匯入清單最小化，以避免不必要的相依性並提升編譯速度。

## 保存 FBX 檔案的流程是什麼？

要將場景儲存為 FBX 檔案，您需要建立 `Scene`、設定所需的資產中繼資料、定義測量單位，然後呼叫 `scene.save(path, FileFormat.FBX7500ASCII)`。此流程會將幾何、材質與中繼資料寫入可供檢查或由下游工具匯入的 ASCII FBX。

### 步驟 1：初始化 3D 場景

`Scene` 類別是 Aspose.3D 的最高層容器，代表整個 3D 場景，包含幾何、光源、相機與中繼資料。首先，建立一個空的 `Scene` 物件。它將作為所有幾何、光源、相機與資產中繼資料的容器。

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### 如何在 Java 中設定應用程式名稱

`AssetInfo` 物件儲存場景的中繼資料，如應用程式名稱、供應商與版本。加入自訂中繼資料有助於下游工具辨識檔案來源。使用 `AssetInfo` 物件在儲存檔案前 **設定應用程式名稱**（以及供應商）。

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **為什麼這很重要：** 許多管線會根據來源應用程式過濾或標記資產，對大型專案而言此步驟相當重要。

### 步驟 3：定義測量單位

單位系統決定場景的實際比例；Aspose.3D 允許您指定單位名稱與相對於公尺的比例因子。在此範例中，我們使用古埃及單位「pole」並設定自訂比例因子。

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **提示：** 調整 `unitScaleFactor` 以符合模型的實際尺寸；1.0 代表與所選單位的 1:1 映射。

### 步驟 4：匯出場景為 FBX

現在已附加資產資訊，我們將場景儲存為 FBX 檔案。`FileFormat.FBX7500ASCII` 選項會產生可供人類閱讀的 ASCII FBX，對除錯非常方便。

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **請記得：** 將 `"Your Document Directory"` 替換為絕對路徑或相對於專案工作目錄的路徑。

## 為何使用 Aspose.3D 匯出場景為 FBX？

Aspose.3D 支援 **超過 50 種輸入與輸出格式**，且能在不將整個檔案載入記憶體的情況下處理上百頁的場景，讓您完整掌控匯出檔案的中繼資料、單位與幾何，無需使用大型 3D 編輯應用程式。這使得自動化資產生成、批次處理與伺服器端轉換快速且可靠。

## 常見使用情境

- **遊戲資產管線** – 直接在 FBX 檔案中嵌入創作者資訊以進行版本追蹤。  
- **建築可視化** – 儲存專案特定單位，以避免匯入渲染引擎時出現比例錯誤。  
- **自動化報告** – 即時產生帶有中繼資料的 FBX 檔案，供下游分析工具讀取。  
- **雲端 3D 服務** – 以程式方式建立與匯出場景，無需 GUI，適合 SaaS 平台。

## 疑難排解與技巧

| 問題 | 解決方案 |
|-------|----------|
| **儲存後找不到檔案** | 確認 `MyDir` 指向已存在的資料夾，且應用程式具備寫入權限。 |
| **外部檢視器中單位顯示不正確** | 再次檢查 `unitScaleFactor`；部分檢視器以公尺作為基礎單位。 |
| **資產中繼資料遺失** | 確保在儲存前呼叫 `scene.getAssetInfo()` **之前**；在 `save()` 之後的變更不會被保留。 |
| **大型場景的效能瓶頸** | 在儲存前使用 `scene.optimize()` 以降低記憶體使用量。 |
| **ASCII FBX 檔案過大** | 改用 `FileFormat.FBX7500` 以切換為二進位 FBX（請參閱 FAQ）。 |

## 常見問題

**Q：如何將輸出格式改為二進位 FBX？**  
A：在呼叫 `scene.save(...)` 時，將 `FileFormat.FBX7500ASCII` 替換為 `FileFormat.FBX7500`。

**Q：我可以在內建資產欄位之外加入自訂使用者定義的中繼資料嗎？**  
A：可以，使用 `scene.getUserData().add("Key", "Value")` 來嵌入額外的鍵值對。

**Q：Aspose.3D 是否支援其他匯出格式，如 OBJ 或 GLTF？**  
A：支援。只需將 `FileFormat` 列舉改為 `OBJ` 或 `GLTF2` 即可。

**Q：需要哪個版本的 Java？**  
A：Aspose.3D for Java 支援 Java 8 及以上版本。

**Q：是否可以載入現有的 FBX，修改其資產資訊後重新儲存？**  
A：當然可以。使用 `new Scene("input.fbx")` 載入檔案，修改 `scene.getAssetInfo()`，然後儲存。

---

**最後更新：** 2026-09-08  
**測試環境：** Aspose.3D for Java 24.11  
**作者：** Aspose

## 相關教學

- [減少 3D 檔案大小 – 使用 Aspose.3D for Java 壓縮場景](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [如何在 Java 中設定 vector3 顏色：變更 Diffuse Color 並管理 3D 屬性 – 使用 Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}