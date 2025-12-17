---
date: 2025-12-09
description: 學習如何使用 Aspose 在 Java 中創建帶有斜切底部的自訂圓柱體，完美適用於 Java 3D 建模並將場景保存為 OBJ。
language: zh-hant
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 如何使用 Aspose：在 Java 中建立底部斜切的圓柱體
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用 Aspose：在 Java 中建立底部斜切的圓柱體

## 簡介

在本實作教學中，您將了解 **如何使用 Aspose** 來建立底部斜切的圓柱體——此技術常用於 *java 3d modeling* 專案。我們會逐步說明，從設定場景到將最終模型儲存為 OBJ 檔案。完成後，您將擁有可直接嵌入任何基於 Java 的 3D 應用程式的可重用程式碼片段。

## 快速解答
- **什麼是「shear bottom」？** 它會在 XY 平面上以指定角度傾斜圓柱體的底部。  
- **哪個函式庫負責 3D 數學運算？** Aspose.3D for Java 提供 `Cylinder` 與 `Vector2` 類別。  
- **執行範例是否需要授權？** 臨時授權可用於評估；正式環境需使用完整授權。  
- **我可以將模型匯出為其他格式嗎？** 可以——使用 `scene.save(..., FileFormat.WAVEFRONTOBJ)` 取得 OBJ 檔案。  
- **需要哪個 Java 版本？** JDK 8 或更新版本即可。

## 在 3D 建模情境下，「如何使用 aspose」是什麼意思？

Aspose.3D for Java 是一高階 API，抽象化 3D 幾何、檔案格式與變換的複雜性。您不必處理低階的頂點緩衝區，只需呼叫直觀的方法，例如 `new Cylinder(...)`，讓 Aspose 代為完成繁重的工作。

## 為什麼在 Java 3D 建模中使用 Aspose？

- **快速開發：** 只需少量程式碼即可建立複雜形狀。  
- **廣泛格式支援：** 可匯出至 OBJ、STL、FBX 等多種格式。  
- **跨平台：** 在任何支援 Java 的作業系統上皆可執行。  
- **一致的 API：** 相同程式碼可用於桌面、伺服器或 Android 環境。

## 前置條件

在開始之前，請確保您已具備以下條件：

- **Java Development Kit (JDK) 8+** 已安裝並在 IDE 中設定。  
- **Aspose.3D for Java** 函式庫已加入專案 classpath。您可從官方網站 [here](https://releases.aspose.com/3d/java/) 下載。  
- **臨時或完整授權**（試用時可選）。

## 匯入套件

首先，匯入必要的 Aspose.3D 類別與 Java 工具類別：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步驟 1：建立場景

*場景* 是容納所有 3D 物件、光源與相機的容器。可將其視為放置圓柱體的舞台。

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## 步驟 2：建立圓柱體 1（底部斜切）

現在建立第一個圓柱體，並對其底部套用斜切變換。`setShearBottom` 方法接受一個 `Vector2`，其中 X 分量代表沿 X 軸的斜切係數，Y 分量代表沿 Y 軸的斜切係數。

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

> **專業提示：** 斜切係數 `0.83` 大約對應 47.5°；可調整此數值以取得所需的精確角度。

## 步驟 3：建立圓柱體 2（標準）

為了作比較，我們會加入第二個未套用斜切的圓柱體。這可讓您在匯出的 OBJ 檔案中直接看到視覺差異。

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## 步驟 4：儲存場景（如何將場景另存為 OBJ）

最後，我們將場景寫入磁碟。`FileFormat.WAVEFRONTOBJ` 常數告訴 Aspose 輸出 OBJ 檔案，該格式被 Blender、Maya 等多數 3D 編輯器廣泛支援。

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **注意：** 請將 `"Your Document Directory"` 替換為適合您環境的絕對或相對路徑。

## 常見問題與解決方案

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| **圓柱體顯示平坦** | 斜切係數不正確（超出 0‑1 範圍） | 使用介於 0 與 1 之間的值；在預覽時逐步調整。 |
| **OBJ 檔案無法在檢視器中載入** | 缺少材質定義 | 為每個節點加入簡單材質，或匯出為 STL 以僅測試幾何體。 |
| **執行時出現 LicenseException** | 沒有有效的授權檔案 | 將 `Aspose.3D.lic` 放置於專案根目錄，或使用 `License` 類別以程式方式載入。 |

## 常見問與答

### Q1: 我可以將 Aspose.3D for Java 與其他 Java 3D 函式庫一起使用嗎？
**A:** Aspose.3D for Java 設計為獨立運作。雖然您可以與其他函式庫整合，但它本身已提供大多數 3D 建模任務所需的完整功能。

### Q2: Aspose.3D 適合 3D 建模新手嗎？
**A:** 適合。Aspose.3D 提供友善的 API，抽象化低階細節，讓新手與有經驗的開發者皆能輕鬆使用。

### Q3: 我可以在哪裡取得 Aspose.3D for Java 的額外支援？
**A:** 前往 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 獲取社群支援、教學與討論。

### Q4: 如何取得 Aspose.3D 的臨時授權？
**A:** 您可在此處取得臨時授權 [here](https://purchase.aspose.com/temporary-license/)。

### Q5: 我可以購買 Aspose.3D for Java 嗎？
**A:** 可以，您可於此處購買 Aspose.3D for Java [here](https://purchase.aspose.com/buy)。

## 結論

我們已示範 **如何使用 Aspose** 建立兩個圓柱體——一個底部斜切、另一個為標準形狀，並將結果儲存為 OBJ 檔案。此技術是構建更複雜 3D 模型（如自訂零件、建築構件或遊戲資產）的基礎。歡迎自行嘗試不同的斜切係數、半徑與高度，以符合您的專案需求。

---

**最後更新：** 2025-12-09  
**測試環境：** Aspose.3D for Java 24.11（撰寫時的最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}