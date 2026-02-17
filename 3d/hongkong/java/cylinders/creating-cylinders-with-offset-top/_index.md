---
date: 2026-02-07
description: 學習如何在 Aspose.3D for Java 中建立頂部有偏移的圓柱模型、加入子節點的 Java 步驟，並輕鬆匯出 3D 模型 OBJ
  檔案。
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: 如何在 Aspose.3D for Java 中建立具有偏移頂部的圓柱體
url: /zh-hant/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D for Java 中建立具有偏移頂部的圓柱體

## 簡介

如果您想在基於 Java 的 3D 場景中 **how to create cylinder** 物件並設定自訂的偏移頂部，Aspose.3D 讓這個過程變得簡單直觀。在本教學中，我們將一步步說明——從設定場景到將最終模型匯出為 OBJ 檔案——讓您能自信地將偏移頂部的圓柱體整合到應用程式中。完成本指南後，您只需幾行程式碼即可熟練建立具自訂偏移的圓柱形狀。

## 快速回答
- **使用的函式庫是什麼？** Aspose.3D for Java  
- **我可以偏移圓柱體的頂部嗎？** Yes, using `setOffsetTop`  
- **如何在 Java 中加入子節點？** Call `createChildNode` on the root node  
- **可以匯出成哪種格式？** Wavefront OBJ (`export 3d model obj`)  
- **測試是否需要授權？** A temporary license is available for evaluation  

## 什麼是帶有偏移頂部的「how to create cylinder」？

建立具有偏移頂部的圓柱體表示其頂部圓形面相對於底部有位移，讓您能在不手動操作頂點的情況下建模錐形或非對稱形狀。Aspose.3D 提供專用的建構子與 `OffsetTop` 屬性，只需幾行程式碼即可完成。

## 為什麼使用 Aspose.3D for Java？

- **高階 API：** 無需管理低階網格資料。  
- **跨平台：** 可在任何相容 JVM 的環境執行。  
- **內建匯出器：** 可直接儲存為 OBJ、STL、FBX 等格式。  
- **可擴充性：** 輕鬆加入子節點、套用變換，並與其他 Java 函式庫整合。  

## 先決條件

在開始之前，請確保您已具備：

- **Java Development Kit (JDK)** – 已安裝相容版本。  
- **Aspose.3D for Java 函式庫** – 從官方網站 [here](https://releases.aspose.com/3d/java/) 下載最新的 JAR。  
- 您選擇的 IDE（Eclipse、IntelliJ IDEA、NetBeans 等）。

## 匯入套件

首先，匯入我們需要的類別。將以下語句放在 Java 檔案的最上方：

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## 逐步指南

### 步驟 1：建立場景

場景是所有 3D 物件的容器。

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### 步驟 2：初始化具有偏移頂部的圓柱體

此處說明 **how to create cylinder** 並設定自訂偏移。建構子定義半徑、高度、切片、堆疊以及圓柱是否封閉。之後，我們使用 `setOffsetTop` 來移動頂部。

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### 步驟 3：如何 **add child node Java** – 附加第一個圓柱體

我們在場景的根節點下建立子節點，並將圓柱體移動到所需位置。

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

### 步驟 5：如何 **add child node Java** – 附加第二個圓柱體

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### 步驟 6：如何 **export OBJ** – 將場景儲存為 OBJ

最後，我們將整個場景（兩個圓柱體）匯出為 Wavefront OBJ 檔案，該格式被廣泛的 3D 工具支援。

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

執行程式後，您會在指定目錄中找到 `CustomizedOffsetTopCylinder.obj`，即可在 Blender、Maya 或任何其他支援 OBJ 的檢視器中開啟。

## 為何重要 – 真實案例

- **建築視覺化：** 偏移頂部的圓柱體非常適合建模向天花板收斂的柱子。  
- **機械零件：** 可建立頂面刻意偏移的活塞或齒輪外殼。  
- **遊戲資產：** 快速產生多樣化的柱子形狀，無需手工製作網格。  

## 如何匯出 OBJ – 將場景儲存為 OBJ

Aspose 3D 的 OBJ 匯出功能讓您能將模型分享給幾乎所有 3D 流程。使用 `scene.save(..., FileFormat.WAVEFRONTOBJ)` 方法即可 **how to export obj** 檔案，免除第三方轉換工具的需求。

## 如何在 Java 中加入子節點 – 附加幾何體

加入子節點是組織場景圖的標準方式。每次呼叫 `createChildNode` 都會回傳一個可獨立變換的節點，這也是本教學中出現兩次 **add child node java** 模式的原因。

## 匯出 3D 模型 OBJ – 使用 Aspose 3D 匯出 OBJ

若需將模型分發給設計師，**export 3d model obj** 功能提供輕量、文字式的表示方式，能在所有主流 3D 應用程式間互通。步驟 6 中使用的相同 API 呼叫示範了 **aspose 3d export obj** 工作流程。

## 常見問題與解決方案

| 問題 | 原因 | 解決方法 |
|------|------|----------|
| **OBJ 檔案為空** | 場景未正確儲存或路徑錯誤。 | 請確認輸出目錄存在且您具有寫入權限。 |
| **偏移未套用** | 使用較舊的 Aspose.3D 版本。 | 升級至支援 `setOffsetTop` 的最新函式庫。 |
| **子節點未顯示** | 未套用變換。 | 確保在建立子節點後呼叫 `getTransform().setTranslation`。 |

## 常見問答

**Q: Aspose.3D 是否相容於不同的 Java IDE？**  
A: 是的，它可無縫運作於 Eclipse、IntelliJ IDEA、NetBeans 以及其他 IDE。

**Q: 我可以為建立的 3D 物件套用材質嗎？**  
A: 當然可以！使用 `Material` 類別來指派材質與表面屬性。

**Q: Aspose.3D 有哪些授權方案？**  
A: 有多種授權模式可供選擇，您可於 [here](https://purchase.aspose.com/buy) 了解詳情。

**Q: 我該如何取得協助或分享使用經驗？**  
A: 加入 Aspose.3D 社群論壇 [here](https://forum.aspose.com/c/3d/18) 獲得支援與討論。

**Q: 是否提供測試用的臨時授權？**  
A: 是的，可於 [here](https://purchase.aspose.com/temporary-license/) 取得測試用臨時授權。

---

**最後更新：** 2026-02-07  
**測試環境：** Aspose.3D for Java 24.12（最新）  
**作者：** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}