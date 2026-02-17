---
date: 2026-01-27
description: 學習 Java 3D 建模，透過使用 Aspose.3D for Java 來建立底部剪切的圓柱體。本初學者 3D 教學示範如何安裝 Aspose
  3D、套用剪切變換，並匯出 OBJ 檔案（Java）。
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Java 3D 建模 – 使用 Aspose.3D 的斜切底部圓柱體
url: /zh-hant/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D 建模 – 斜切底部圓柱與 Aspose.3D

## 簡介

歡迎閱讀本 **java 3d modeling** 教學！在本步驟說明中，我們將示範如何使用 Aspose.3D for Java 建立一個底部被斜切的圓柱。無論您是跟隨 **beginner 3d tutorial**，或是想為現有模型加入自訂的斜切變換，都能清楚看到如何設定場景、套用斜切，最後 **export OBJ file java** 以供其他工具使用。

## 快速答覆
- **使用的函式庫是什麼？** Aspose.3D for Java  
- **我可以透過 Maven 安裝 Aspose 3D 嗎？** 是 – 將 Aspose.3D 相依性加入 `pom.xml`  
- **開發是否需要授權？** 測試時使用臨時授權即可；正式環境則需完整授權  
- **示範使用哪種檔案格式？** Wavefront OBJ（`.obj`）  
- **範例執行需要多久？** 在一般工作站上不到一秒  

## 先決條件

在開始之前，請確保您已具備以下項目：

- 已在系統上安裝 Java Development Kit（JDK）。  
- **安裝 Aspose 3D** – 從官方網站[此處](https://releases.aspose.com/3d/java/)下載函式庫。  
- 具備 IDE 或建置工具（Maven/Gradle）以管理 Aspose.3D 相依性。  

## 匯入套件

首先，匯入我們在場景、幾何與檔案處理上需要的類別。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步驟 1：建立場景

場景是所有 3‑D 物件的容器。我們將先建立一個空的場景。

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## 步驟 2：建立 Cylinder 1 – 如何斜切圓柱

現在我們建立第一個圓柱，並對其底部 **套用 shear transformation**。此範例示範如何直接透過 API **how to shear cylinder** 幾何。

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## 步驟 3：建立 Cylinder 2 – 標準圓柱（無斜切）

為了作比較，我們會加入第二個 **未** 斜切底部的圓柱。

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## 步驟 4：儲存場景 – Export OBJ File Java

最後，我們將場景匯出為 Wavefront OBJ 檔案，示範 **export obj file java** 的使用方式。

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## 為何此技巧對 Java 3D 建模重要

對基元加入斜切可讓您在不使用外部建模工具的情況下，創造更具有機感的形狀。此技巧適用於：

- 需要斜坡底座的建築視覺化。  
- 在保持幾何輕量的前提下，需要自訂外形的遊戲資產。  
- 需要以程式方式微調尺寸的快速原型製作。  

## 常見問題與解決方案

| 問題 | 解決方案 |
|------|----------|
| **斜切過於極端** | 調整 `Vector2` 的數值；它代表斜切係數（0‑1 範圍）。 |
| **OBJ 檔案無法在檢視器中開啟** | 確認目標目錄是否存在且您具有寫入權限。 |
| **執行時授權例外** | 在建立場景前套用臨時或永久授權 (`License license = new License(); license.setLicense("Aspose.3D.lic");`)。 |

## 常見問答

**Q: 我可以將 Aspose.3D for Java 與其他 Java 3D 函式庫一起使用嗎？**  
A: Aspose.3D 設計為獨立運作。雖然您可以與其他函式庫整合，但它已提供大多數 3‑D 任務所需的完整 API。

**Q: Aspose.3D 適合 3D 建模初學者嗎？**  
A: 絕對適合。API 簡潔易懂，且本 **beginner 3d tutorial** 以最少的程式碼示範核心概念。

**Q: 我可以在哪裡取得 Aspose.3D for Java 的其他支援？**  
A: 前往 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 獲得社群協助與官方回覆。

**Q: 我要如何取得 Aspose.3D 的臨時授權？**  
A: 您可在[此處](https://purchase.aspose.com/temporary-license/)取得臨時授權。

**Q: 我該從哪裡購買完整的 Aspose.3D for Java 授權？**  
A: 購買選項請參考[此處](https://purchase.aspose.com/buy)。

---

**最後更新：** 2026-01-27  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
