---
date: 2025-12-19
description: 學習如何使用 Aspose.3D for Java 在線性擠出中運用扭轉偏移來建立 3D 場景並匯出 3D OBJ。
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: 使用扭轉偏移建立 3D 場景 – Aspose.3D Java
url: /zh-hant/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Twist Offset 建立 3d 場景 – Aspose.3D for Java

## 簡介

在充滿活力的 3D 圖形世界中，學習如何 **create 3d scene** 搭配線性擠出是一個改變遊戲規則的技巧。使用 Aspose.3D for Java，您可以透過將 Twist Offset 功能加入線性擠出流程，提升您的 3D 建模技能。本教學將指導您如何在 Aspose.3D for Java 中於線性擠出使用 Twist Offset，提供您建立驚豔 3D 場景的工具。

## 快速解答
- **Twist Offset 有什麼作用？** 它會沿著擠出路徑移動扭轉的起始點，讓您對幾何形狀有更大的控制。  
- **哪種檔案格式用於匯出？** 此範例將模型儲存為 Wavefront OBJ（`.obj`）。  
- **開發時需要授權嗎？** 免費試用版可用於測試；正式上線則需商業授權。  
- **需要哪個 Java 版本？** Java 8 或更新版本。  
- **可以更改切片數量嗎？** 可以 – `setSlices` 方法可定義扭轉的平滑度。

## 先決條件

在深入本教學之前，請確保已具備以下先決條件：

- Java 環境：確保您的系統已設置 Java 開發環境。  
- Aspose.3D for Java：從[下載連結](https://releases.aspose.com/3d/java/)下載並安裝 Aspose.3D 程式庫。  
- 文件說明：熟悉[Aspose.3D for Java 文件說明](https://reference.aspose.com/3d/java/)。

## 匯入套件

在您的 Java 專案中，匯入必要的套件以開始使用 Aspose.3D for Java。確保包含所需的程式庫以順利整合。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 步驟 1：設定環境

首先設定您的 Java 開發環境，並確保已正確安裝 Aspose.3D for Java。

## 步驟 2：初始化基礎輪廓

建立擠出的基礎輪廓，此例使用半徑為 0.3 的 `RectangleShape`。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 步驟 3：建立 3D 場景

建立一個 3D 場景以容納您的擠出物件。

```java
// Create a scene
Scene scene = new Scene();
```

## 步驟 4：建立節點

在場景中產生節點以代表不同的實體。

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步驟 5：執行線性擠出

對左右節點使用線性擠出，並設定各種屬性。

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## 步驟 6：儲存 3D 場景

使用指定的檔案格式儲存您新建立的 3D 場景。

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 如何儲存 3d 模型並匯出 3d obj

`scene.save` 在前一步的呼叫 **saves the 3d model** 為 OBJ 檔案，這是一種廣受支援的 **export 3d obj** 格式。您可以透過調整 `FileFormat` 列舉來變更檔名或選擇其他支援的格式（例如 STL、FBX）。

## 結論

恭喜！您已成功在 Aspose.3D for Java 中於線性擠出實作 Twist Offset。此強大功能為您的 3D 建模開啟無限可能，讓您能夠 **create 3d scene** 具備精細扭轉與偏移，並 **save 3d model** 為可供後續流程使用的格式。

## 常見問題

### Q1: 我可以在非商業專案中使用 Aspose.3D for Java 嗎？

A1: 可以，Aspose.3D for Java 可用於商業與非商業專案。請參閱[授權選項](https://purchase.aspose.com/buy)了解更多細節。

### Q2: 我可以在哪裡取得 Aspose.3D for Java 的支援？

A2: 前往[Aspose.3D for Java 論壇](https://forum.aspose.com/c/3d/18)取得協助並與社群互動。

### Q3: 是否提供 Aspose.3D for Java 的免費試用版？

A3: 可以，您可從[發佈頁面](https://releases.aspose.com/)下載免費試用版。

### Q4: 如何取得 Aspose.3D for Java 的臨時授權？

A4: 前往[此連結](https://purchase.aspose.com/temporary-license/)為您的專案取得臨時授權。

### Q5: 是否有其他範例與教學可供參考？

A5: 有，請參考[文件說明](https://reference.aspose.com/3d/java/)以取得更多範例與深入教學。

## 常見問答

**Q: 此教學是否屬於 Aspose 3d 教學系列的一部份？**  
A: 是 – 這是一個官方 **aspose 3d tutorial**，示範了函式庫的特定功能。

**Q: 我可以使用除矩形外的其他形狀嗎？**  
A: 當然可以。任何 `IProfile` 實作（例如 `CircleShape`、自訂 `PolygonShape`）皆可進行擠出。

**Q: 如果省略 `setTwistOffset` 會發生什麼？**  
A: 擠出將從輪廓的原點開始扭轉，產生對稱的扭轉效果。

**Q: 如何提升扭轉的平滑度？**  
A: 提高傳遞給 `setSlices` 的數值；較高的切片數會產生更平滑的幾何形狀。

**Q: 除了 OBJ，還能匯出哪些其他檔案格式？**  
A: Aspose.3D 透過 `FileFormat` 列舉支援 STL、FBX、GLTF、3MF 等多種格式。

---

**最後更新：** 2025-12-19  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## TARGET KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**  
create 3d scene  

**Secondary Keywords (SUPPORTING):**  
save 3d model, export 3d obj, aspose 3d tutorial