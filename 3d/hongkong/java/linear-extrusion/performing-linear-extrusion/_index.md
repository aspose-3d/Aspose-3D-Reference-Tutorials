---
date: 2025-12-18
description: 學習如何在 Java 中使用 Aspose.3D 擠出形狀，建立 3D 場景，並輕鬆匯出 Wavefront OBJ 檔案。
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: 如何在 Java 中使用 Aspose.3D 進行線性擠出形狀
url: /zh-hant/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Aspose.3D for Java 中執行線性擠出

## 簡介

歡迎閱讀本完整教學，了解如何在 Aspose.3D for Java 中 **how to extrude shape**！如果您想使用 Java 提升 3D 建模技巧，這裡正是起點。我們將一步步示範如何建立 3D 場景、執行線性擠出，並將結果匯出為 Wavefront OBJ 檔案，並提供清晰的程式碼範例。

## 快速回答
- **什麼是線性擠出？** 將 2D 剖面沿直線路徑延伸，以產生 3D 實體。  
- **哪個程式庫在 Java 中處理此功能？** Aspose.3D for Java。  
- **我可以匯出為 OBJ 嗎？** 可以，使用 Wavefront OBJ 匯出功能。  
- **開發是否需要授權？** 免費試用可用於測試；正式環境需購買授權。  
- **需要哪個 Java 版本？** Java 1.6 或更新版本。

## 什麼是「how to extrude shape」？

線性擠出是 **3d modeling java** 中的基本技術，可將平面剖面（例如矩形）透過沿一定距離拉伸，轉換為體積物件。此方法廣泛應用於機械零件、建築構件及裝飾模型的製作。

## 為什麼在線性擠出時使用 Aspose.3D？

- **完整控制** 幾何形狀（切片、扭轉、偏移）。  
- **無縫整合** 與 Java 專案——無需本機相依性。  
- **內建匯出器** 支援常見格式，包括 Wavefront OBJ，讓 **generate 3d model** 檔案的下游流程更為簡便。

## 先決條件

在開始本教學之前，請確保已具備以下先決條件：

1. **Java 開發環境** – JDK（1.6 或更新）以及您慣用的 IDE。  
2. **Aspose.3D 程式庫** – 從官方網站 **[here](https://releases.aspose.com/3d/java/)** 下載並安裝。

## 匯入套件

設定好開發環境並安裝 Aspose.3D 程式庫後，匯入必要的套件：

```java
import com.aspose.threed.*;
```

### 步驟 1：設定文件目錄

定義產生檔案的儲存資料夾：

```java
String MyDir = "Your Document Directory";
```

> 這可確保 **generate 3d model** 操作將 OBJ 檔寫入已知位置。

### 步驟 2：初始化基礎形狀

建立一個矩形作為擠出剖面：

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

您可以調整圓角半徑以取得圓角，或將其設為 `0` 以得到完整的矩形。

### 步驟 3：執行線性擠出

現在我們沿 Z 軸對矩形進行擠出，加入切片、啟用置中，並以偏移量套用扭轉：

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **擠出長度** – `10` 單位。  
- **切片數** – `100`，以獲得平滑幾何。  
- **扭轉** – `360°` 產生完整旋轉。  
- **扭轉偏移** – 將扭轉原點移至 `(10, 0, 0)`。

### 步驟 4：建立 3D 場景

建立場景容器，並將擠出物件作為子節點加入。此步驟 **creates 3d scene** 可容納多個物件：

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### 步驟 5：儲存 3D 場景

將場景匯出為 Wavefront OBJ 檔案，示範 **wavefront obj export** 與 **save 3d obj** 功能：

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

執行程式碼後，您會在先前指定的目錄中找到 `LinearExtrusion.obj`，可在任何 3D 檢視器中開啟或進一步處理。

## 常見問題與解決方案

| 問題 | 原因 | 解決方案 |
|-------|--------|-----|
| OBJ 檔案為空 | 輸出目錄路徑不正確或不可寫入 | 確認 `MyDir` 指向已存在且具寫入權限的資料夾。 |
| 扭轉未套用 | 缺少 `setCenter(true)` | 確保已啟用置中，或調整 `setTwistOffset` 的數值。 |
| 編譯 `LinearExtrusion` 時出錯 | 使用較舊的 Aspose.3D 版本 | 更新至最新的 Aspose.3D 版本。 |

## 常見問答

**Q: Aspose.3D 是否相容所有 Java 版本？**  
A: Aspose.3D 支援 Java 1.6 及以上版本。

**Q: 我可以在商業專案中使用 Aspose.3D 嗎？**  
A: 可以，持有效授權即可商業使用。您可於 **[here](https://purchase.aspose.com/buy)** 取得授權。

**Q: 若遇到問題，我該向何處尋求支援？**  
A: 前往 **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** 取得社群協助，或購買 **[temporary license](https://purchase.aspose.com/temporary-license/)** 以獲得高階支援。

**Q: Aspose.3D 還提供哪些 3D 建模功能？**  
A: 程式庫包含網格操作、布林運算、貼圖映射等功能。完整清單請見 **[here](https://reference.aspose.com/3d/java/)**。

**Q: 是否提供免費試用？**  
A: 有，您可於 **[here](https://releases.aspose.com/)** 下載試用版。

## 結論

您現在已學會使用 Aspose.3D for Java **how to extrude shape**，建立 3D 場景，並將結果匯出為 Wavefront OBJ 檔案。此技術為各種 **3d modeling java** 專案開啟可能性，無論是簡單零件或複雜組件。可進一步探索布林運算或貼圖映射等功能，以豐富模型內容。

---

**最後更新：** 2025-12-18  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## 目標關鍵字：

**Primary Keyword (HIGHEST PRIORITY):**
how to extrude shape

**Secondary Keywords (SUPPORTING):**
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj