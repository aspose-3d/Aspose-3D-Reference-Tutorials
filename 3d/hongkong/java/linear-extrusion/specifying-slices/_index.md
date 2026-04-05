---
date: 2026-02-22
description: 學習如何使用 Aspose.3D for Java 建立帶切片的 3D 擠出。本一步一步的指南涵蓋線性擠出、設定圓角半徑以及匯出 OBJ。
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: 建立含切片的 3D 拉伸 – Aspose.3D for Java
url: /zh-hant/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用切片建立 3D 拉伸 – Aspose.3D for Java

## Introduction

如果您需要 **建立 3D 拉伸** 物件，讓外觀平滑且精確，控制切片數量是關鍵。在本教學中，我們將說明如何在使用 Aspose.3D for Java 進行線性拉伸時指定切片。您將了解為什麼切片數量重要、如何設定圓角半徑，以及如何將結果匯出為 OBJ 檔案，以便在任何 3D 流程中使用。

## Quick Answers
- **「slices」控制什麼？** 用於近似拉伸表面的中間橫截面數量。  
- **哪個方法設定切片數量？** `LinearExtrusion.setSlices(int)`  
- **我可以變更輪廓的圓角半徑嗎？** 可以，透過 `RectangleShape.setRoundingRadius(double)`  
- **此範例使用的檔案格式是什麼？** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **執行程式碼需要授權嗎？** 免費試用版可用於評估；正式上線需購買商業授權。

## 什麼是帶切片的線性拉伸？

線性拉伸會將 2‑D 輪廓（例如矩形）沿直線拉伸，形成 3‑D 實體。透過指定 **slices**，您告訴 Aspose.3D 產生多少個中間步驟，直接影響曲線邊緣（如圓角矩形）的平滑程度。

## 為什麼使用 Aspose.3D for Java 來建立 3D 拉伸？

* **完整控制** – 您可以以程式方式調整切片數量、圓角半徑與匯出格式。  
* **跨平台** – 可在任何支援 Java 的環境執行，無需原生相依性。  
* **匯出彈性** – 可直接儲存為 OBJ、FBX、STL 等多種格式。

## 先決條件

1. **Java Development Kit** – 已安裝 JDK 8 或更新版本。  
2. **Aspose.3D for Java** – 從官方網站下載程式庫，點此 [here](https://releases.aspose.com/3d/java/)。  
3. 任意您喜好的 IDE 或文字編輯器。

## 匯入套件

將 Aspose.3D 命名空間加入您的專案，以便存取 3‑D 建模類別。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 逐步指南

### 步驟 1：設定場景並定義輪廓

首先，我們建立一個 `RectangleShape`，並設定 **rounding radius** 使角落平滑。接著，我們初始化一個新的 `Scene`，用來容納所有幾何體。

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### 步驟 2：為每個拉伸 **建立子節點** 物件

每個幾何體都屬於一個 `Node`。此處我們產生兩個同層節點——一個用於低切片拉伸，另一個用於高切片拉伸——並將左側節點稍微向旁邊移動，以便於比較結果。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 步驟 3：執行線性拉伸並 **設定切片**

現在我們實際 **建立 3D 拉伸** 物件。`LinearExtrusion` 建構子接受輪廓與拉伸深度。透過 **anonymous inner class** 呼叫 `setSlices` 以控制平滑度。左側節點僅使用 2 個切片（粗糙），右側節點使用 10 個切片（平滑）。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### 步驟 4：**匯出 OBJ** – 儲存場景

最後，我們將場景寫入 Wavefront OBJ 檔案，這是一種被廣泛支援的 3‑D 編輯器與遊戲引擎格式。此示範了 Aspose.3D 的 **export obj java** 功能。

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常見問題與解決方案

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **拉伸呈平面** | 切片數量設定為 1 或 0 | 確保 `setSlices` 的參數值 ≥ 2。 |
| **圓角看起來鋸齒狀** | 相對於切片數量，圓角半徑過小 | 增加半徑或切片數量，以獲得更平滑的曲線。 |
| **儲存時找不到檔案** | `MyDir` 指向不存在的資料夾 | 事先建立該目錄，或使用絕對路徑。 |

## 常見問答

**Q: 如何下載 Aspose.3D for Java？**  
A: 您可以在此處下載程式庫 [here](https://releases.aspose.com/3d/java/).

**Q: 在哪裡可以找到 Aspose.3D 的文件？**  
A: 請參考文件 [here](https://reference.aspose.com/3d/java/).

**Q: 是否提供免費試用？**  
A: 有，您可以在此處探索免費試用 [here](https://releases.aspose.com/).

**Q: 如何取得 Aspose.3D 的支援？**  
A: 前往支援論壇 [here](https://forum.aspose.com/c/3d/18).

**Q: 可以購買臨時授權嗎？**  
A: 可以，臨時授權可在此取得 [here](https://purchase.aspose.com/temporary-license/).

---

**最後更新：** 2026-02-22  
**測試環境：** Aspose.3D for Java 24.11（撰寫時的最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}