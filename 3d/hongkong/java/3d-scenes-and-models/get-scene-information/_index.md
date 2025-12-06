---
date: 2025-12-06
description: 了解如何使用 Aspose.3D for Java 儲存 FBX 檔案並擷取場景資訊。本步驟指南涵蓋設定應用程式名稱、定義測量單位，以及將場景匯出為
  FBX。
language: zh-hant
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: 如何在 Java 中儲存 FBX 並取得 3D 場景資訊
url: /java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Java 中儲存 FBX 並取得 3D 場景資訊

## 介紹

如果您在尋找一個清晰、實作導向的指南，說明 **如何儲存 fbx** 檔案同時從 3D 場景中提取有用的中繼資料，您來對地方了。在本教學中，我們將使用 **Aspose.3D Java** 函式庫逐步說明：從建立場景、**設定應用程式名稱**、**定義測量單位**，到最後 **匯出場景為 FBX**。完成後，您將擁有一個可直接使用的 FBX 檔案，內含您在後續流程中需要的資產資訊。

## 快速回答
- **主要目標是什麼？** 儲存包含自訂資產資訊的 FBX 檔案。  
- **使用哪個函式庫？** Aspose.3D for Java。  
- **需要授權嗎？** 開發階段可使用免費試用版；正式上線需購買商業授權。  
- **可以變更測量單位嗎？** 可以 – 使用 `setUnitName` 與 `setUnitScaleFactor`。  
- **輸出檔案儲存在哪裡？** 儲存於您於 `scene.save(...)` 指定的路徑。

## 前置條件

在開始之前，請確保您已具備：

- 對核心 Java 語法有扎實的了解。  
- **Aspose.3D for Java** 已下載並加入專案（可從官方 [Aspose 3D 下載頁面](https://releases.aspose.com/3d/java/) 取得）。  
- 您喜愛的 Java IDE（IntelliJ IDEA、Eclipse、NetBeans 等）已正確設定。

## 匯入套件

在您的 Java 原始檔中，匯入提供場景處理與檔案格式支援的 Aspose.3D 類別。

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **專業提示：** 保持 import 清單最小化，以避免不必要的相依性並提升編譯速度。

## 儲存 FBX 檔案的流程是什麼？

以下是一個簡潔的逐步說明，展示 **如何將資產資訊加入場景**，再 **將場景匯出為 FBX**。

### 步驟 1：初始化 3D 場景

首先，建立一個空的 `Scene` 物件。它將作為所有幾何、光源、相機以及資產中繼資料的容器。

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### 步驟 2：設定應用程式與供應商資訊

加入自訂中繼資料有助於下游工具辨識檔案來源。此處我們使用 `AssetInfo` 物件 **設定應用程式名稱** 與供應商。

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **為何重要：** 許多流水線會根據來源應用程式過濾或標記資產，對於大型專案此步驟相當必要。

### 步驟 3：定義測量單位

Aspose.3D 允許您指定場景使用的單位系統。在此範例中，我們使用古埃及單位「pole」並設定自訂比例因子。

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **提示：** 調整 `unitScaleFactor` 以符合模型的實際尺寸；1.0 代表與所選單位的 1:1 映射。

### 步驟 4：匯出場景為 FBX

現在資產資訊已附加，我們將場景儲存為 FBX 檔案。`FileFormat.FBX7500ASCII` 選項會產生可讀的 ASCII FBX，對除錯相當方便。

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **請記得：** 將 `"Your Document Directory"` 替換為絕對路徑或相對於專案工作目錄的路徑。

### 步驟 5：印出成功訊息

簡單的主控台輸出可確認操作成功，並告知檔案寫入位置。

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## 常見使用情境

- **遊戲資產流水線** – 直接在 FBX 檔案中嵌入創作者資訊，以便版本追蹤。  
- **建築可視化** – 儲存專案特定的單位，避免匯入渲染引擎時出現縮放錯誤。  
- **自動化報告** – 即時產生帶有中繼資料的 FBX 檔案，供下游分析工具讀取。

## 故障排除與技巧

| 問題 | 解決方案 |
|-------|----------|
| **儲存後找不到檔案** | 確認 `MyDir` 指向已存在的資料夾，且應用程式具備寫入權限。 |
| **外部檢視器顯示單位不正確** | 再次檢查 `unitScaleFactor`；某些檢視器預設以公尺為基礎單位。 |
| **資產中繼資料遺失** | 確保在儲存前呼叫 `scene.getAssetInfo()` **之前**；在 `save()` 之後的變更不會被保留。 |

## 常見問答

### Q1：Aspose.3D 是否相容所有 Java IDE？

A1：是的，Aspose.3D 設計上能無縫支援所有主要的 Java IDE。

### Q2：我可以在商業專案中使用 Aspose.3D 嗎？

A2：當然可以。Aspose.3D 提供商業授權，確保開發者符合授權需求。

### Q3：在哪裡可以取得 Aspose.3D 的額外支援？

A3：如有任何問題或需要協助，請前往 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)。

### Q4：Aspose.3D 有提供免費試用嗎？

A4：是的，您可於此處取得免費試用版以探索功能 [here](https://releases.aspose.com/)。

### Q5：如何取得 Aspose.3D 的臨時授權？

A5：可於此處取得測試用的臨時授權 [here](https://purchase.aspose.com/temporary-license/)。

## 常見問題

**問：如何將輸出格式改為二進位 FBX？**  
答：在呼叫 `scene.save(...)` 時，將 `FileFormat.FBX7500ASCII` 替換為 `FileFormat.FBX7500`。

**問：我能在內建資產欄位之外加入自訂使用者定義的中繼資料嗎？**  
答：可以，使用 `scene.getUserData().add("Key", "Value")` 來嵌入額外的鍵值對。

**問：Aspose.3D 是否支援其他匯出格式，例如 OBJ 或 GLTF？**  
答：支援，只要將 `FileFormat` 列舉改為 `OBJ` 或 `GLTF2` 即可。

**問：需要哪個版本的 Java？**  
答：Aspose.3D for Java 支援 Java 8 及以上版本。

**問：能否載入現有的 FBX，修改其資產資訊後再儲存？**  
答：當然可以。使用 `new Scene("input.fbx")` 載入檔案，修改 `scene.getAssetInfo()`，最後儲存。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2025-12-06  
**測試環境：** Aspose.3D for Java 24.11  
**作者：** Aspose