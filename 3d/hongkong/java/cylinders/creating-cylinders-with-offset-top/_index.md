---
date: 2025-12-05
description: 學習如何在 Aspose.3D for Java 中建立頂部偏移的圓柱模型、加入子節點的 Java 步驟，並輕鬆匯出 3D 模型 OBJ
  檔案。
language: zh-hant
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: 如何在 Aspose.3D for Java 中建立頂部偏移的圓柱體
url: /java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D for Java 中建立具有偏移頂部的圓柱體

## 介紹

如果您想在基於 Java 的 3D 場景中 **建立圓柱體** 並自訂其頂部偏移，Aspose.3D 能讓這個過程變得簡單。在本教學中，我們將一步步說明——從設定場景到將最終模型匯出為 OBJ 檔——讓您能自信地將偏移頂部的圓柱體整合到應用程式中。

## 快速回答
- **使用哪個函式庫？** Aspose.3D for Java  
- **可以偏移圓柱體的頂部嗎？** 可以，使用 `setOffsetTop`  
- **如何在 Java 中新增子節點？** 在根節點上呼叫 `createChildNode`  
- **可以匯出成哪種格式？** Wavefront OBJ（`export 3d model obj`）  
- **測試需要授權嗎？** 可取得臨時授權供評估使用  

## 什麼是「建立圓柱體」且具有偏移頂部？

建立具有偏移頂部的圓柱體，指的是將頂部圓形面相對於底部平面平移，讓您能在不手動操作頂點的情況下建模錐形或非對稱形狀。Aspose.3D 提供專用建構子與 `OffsetTop` 屬性，只需幾行程式碼即可完成。

## 為什麼選擇 Aspose.3D for Java？

- **高階 API：** 無需管理底層網格資料。  
- **跨平台：** 可在任何相容 JVM 的環境執行。  
- **內建匯出器：** 直接儲存為 OBJ、STL、FBX 等格式。  
- **可擴充性：** 輕鬆新增子節點、套用變換，並與其他 Java 函式庫整合。  

## 前置條件

在開始之前，請確保您已具備：

- **Java Development Kit (JDK)** – 已安裝相容版本。  
- **Aspose.3D for Java 函式庫** – 從官方網站下載最新 JAR 檔案 [here](https://releases.aspose.com/3d/java/)。  
- 任一您慣用的 IDE（Eclipse、IntelliJ IDEA、NetBeans 等）。

## 匯入套件

首先，匯入我們將會使用的類別。將以下語句放在 Java 檔案的最上方：

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## 步驟說明

### 步驟 1：建立場景

場景是所有 3D 物件的容器。

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### 步驟 2：以偏移頂部初始化圓柱體

在此我們說明 **如何建立圓柱體** 並自訂偏移。建構子會定義半徑、高度、切片、堆疊以及圓柱體是否封閉。之後，我們使用 `setOffsetTop` 來平移頂部。

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### 步驟 3：如何 **在 Java 中新增子節點** – 附加第一個圓柱體

我們在場景的根節點下建立子節點，並將圓柱體移動到指定位置。

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### 步驟 4：初始化第二個圓柱體（無偏移）

為了作比較，我們加入一個沒有偏移的普通圓柱體。

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### 步驟 5：如何 **在 Java 中新增子節點** – 附加第二個圓柱體

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### 步驟 6：如何 **匯出 3D 模型 OBJ** – 儲存場景

最後，我們將整個場景（兩個圓柱體）匯出為 Wavefront OBJ 檔，該格式被廣泛的 3D 工具支援。

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

執行程式後，您會在指定目錄中看到 `CustomizedOffsetTopCylinder.obj`，即可在 Blender、Maya 或其他支援 OBJ 的檢視器中開啟。

## 常見問題與解決方案

| 問題 | 原因 | 解決方式 |
|------|------|----------|
| **OBJ 檔案為空** | 場景未正確儲存或路徑錯誤。 | 確認輸出目錄存在且具有寫入權限。 |
| **偏移未套用** | 使用了較舊的 Aspose.3D 版本。 | 更新至支援 `setOffsetTop` 的最新函式庫。 |
| **子節點不可見** | 變換未套用。 | 在建立子節點後，確保呼叫 `getTransform().setTranslation`。 |

## 常見問答

**Q: Aspose.3D 是否相容於不同的 Java IDE？**  
A: 是的，能無縫運作於 Eclipse、IntelliJ IDEA、NetBeans 等 IDE。

**Q: 我可以為建立的 3D 物件套用材質嗎？**  
A: 當然可以！使用 `Material` 類別即可指定紋理與表面屬性。

**Q: Aspose.3D 有哪些授權方案？**  
A: 提供多種授權模式，您可於 [here](https://purchase.aspose.com/buy) 了解詳情。

**Q: 如何取得協助或分享使用經驗？**  
A: 歡迎加入 Aspose.3D 社群論壇 [here](https://forum.aspose.com/c/3d/18) 交流與求助。

**Q: 是否提供臨時授權供測試使用？**  
A: 有，您可於 [here](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**最後更新：** 2025-12-05  
**測試環境：** Aspose.3D for Java 24.12（最新）  
**作者：** Aspose