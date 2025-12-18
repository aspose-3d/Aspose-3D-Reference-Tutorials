---
date: 2025-12-18
description: 學習如何在 Aspose.3D for Java 中使用線性擠出添加地面平面並設定中心屬性，並提供逐步程式碼範例。
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 如何在 Aspose.3D for Java 的線性擠出中添加地面平面與控制中心
url: /zh-hant/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Aspose.3D for Java 中控制線性擠出中心

## 簡介

當您在 Java 中構建 3D 場景時，能夠 **加入地面平面** 並在 **設定線性擠出的中心屬性** 時保持精確，往往會決定原型是平淡無奇還是視覺上精緻。在本教學中，我們將完整說明如何透過 Aspose.3D for Java 控制擠出中心並加入地面平面。您將了解此操作的重要性、設定方式，並取得一段可直接執行的程式碼範例，方便您套用到自己的專案中。

## 快速答覆
- **「加入地面平面」的作用是什麼？** 它會建立一個薄薄的參考幾何體，協助您觀察擠出物相對於世界座標軸的位置。  
- **如何設定線性擠出的中心？** 在 `LinearExtrusion` 物件上使用 `setCenter(boolean)` 方法。  
- **執行範例是否需要授權？** 測試時可使用臨時授權；正式上線則需正式授權。  
- **儲存使用哪種檔案格式？** 範例會儲存為 Wavefront OBJ（`.obj`）。  
- **需要哪個版本的 Java？** Java 8 或以上即可。

## 什麼是 3D 場景中的「加入地面平面」？

加入地面平面指的是在 X‑Z 平面上插入一個薄薄的矩形幾何體（通常是一個厚度極小的盒子）。它充當視覺上的地板，讓您更容易判斷其他物件的高度與對齊情況，特別是在測試擠出中心時。

## 為什麼要在線性擠出上設定中心屬性？

預設情況下，線性擠出會從輪廓的原點開始。設定中心屬性 (`setCenter(true)`) 會將輪廓移動，使擠出物以原點為中心，這對於對稱設計或需要在多個物件間保持一致對齊時非常有用。

## 先決條件

在開始本教學之前，請確保您已具備以下條件：

1. **Java 開發環境** – 確認您的機器已安裝並設定好 Java 開發環境。  
2. **Aspose.3D for Java** – 下載並安裝 Aspose.3D 程式庫。您可以在[此處](https://reference.aspose.com/3d/java/)找到程式庫與文件。  
3. **文件目錄** – 建立一個目錄用來存放您的 Java 檔案。此目錄暫稱為「Your Document Directory」。

## 匯入套件

在您的 Java 開發環境中，匯入 Aspose.3D 所需的套件，以確保程式碼能使用程式庫提供的功能。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步驟 1：設定基礎輪廓

初始化要進行擠出的基礎輪廓。本例使用半徑為 0.3 的矩形形狀。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 步驟 2：建立 3D 場景

建立 3D 世界的基礎——場景物件。

```java
Scene scene = new Scene();
```

## 步驟 3：建立左側與右側節點

在場景中建立左、右兩個節點，作為放置 3D 物件的畫布。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步驟 4：左側節點的線性擠出與中心屬性

在左側節點執行 **不置中** 的線性擠出，並將切片數設定為 3。請注意 `setCenter(false)` 呼叫——此處將 **中心屬性** 設為 *false*。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## 步驟 5：為左側節點加入參考用地面平面

透過 **加入地面平面** 來增強視覺效果。這個薄盒子充當地板，讓您清楚看到擠出的高度。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## 步驟 6：右側節點的線性擠出與中心屬性

現在在右側節點執行線性擠出，這次 **將擠出置中**。`setCenter(true)` 呼叫示範如何將 **中心屬性** 設為 *true*。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## 步驟 7：為右側節點加入參考用地面平面

與左側相同，為右側節點加入地面平面，以保持視覺上的一致基準。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## 步驟 8：儲存 3D 場景

將 3D 場景以 Wavefront OBJ 格式儲存，方便在任何標準 3D 檢視器中開啟。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常見問題與解決方案

| 問題 | 為什麼會發生 | 解決方式 |
|------|--------------|----------|
| 地面平面未顯示 | 盒子厚度對於檢視器的比例太小。 | 增加厚度（`Box` 的第一個參數）或在檢視器中拉遠視角。 |
| 擠出位置偏移 | `setCenter` 的值未如預期設定。 | 再次確認傳入 `setCenter` 的布林值。 |
| 檔案未儲存 | 目錄路徑錯誤或缺少寫入權限。 | 確認 `MyDir` 指向一個已存在且具有寫入權限的資料夾。 |

## 常見問答

**Q1: 我可以在商業專案中使用 Aspose.3D for Java 嗎？**  
A1: 可以，Aspose.3D for Java 可用於商業用途。授權細節請參閱[此處](https://purchase.aspose.com/buy)。

**Q2: 有免費試用版嗎？**  
A2: 有，您可以在[此處](https://releases.aspose.com/)取得 Aspose.3D for Java 的免費試用版。

**Q3: 我可以在哪裡取得 Aspose.3D for Java 的支援？**  
A3: Aspose.3D 社群論壇是尋求支援與分享經驗的好地方。請前往論壇[此處](https://forum.aspose.com/c/3d/18)。

**Q4: 測試時需要臨時授權嗎？**  
A4: 需要，若您需要臨時授權以進行測試，可在[此處](https://purchase.aspose.com/temporary-license/)取得。

**Q5: 文件在哪裡可以找到？**  
A5: Aspose.3D for Java 的文件可在[此處](https://reference.aspose.com/3d/java/)取得。

## 結論

在 Aspose.3D for Java 中同時 **控制線性擠出的中心** 與 **加入地面平面**，為 3D 圖形開發開啟了許多可能性。依照上述步驟，您現在已掌握可重複使用的模式，能建立置中的擠出、視覺參考平面，並將結果匯出為 OBJ。歡迎自行嘗試不同的輪廓、切片數與變換，以符合您專案的需求。

---

**最後更新：** 2025-12-18  
**測試環境：** Aspose.3D 24.11 for Java（撰寫時的最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}