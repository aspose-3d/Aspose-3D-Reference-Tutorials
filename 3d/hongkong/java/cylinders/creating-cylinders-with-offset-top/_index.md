---
date: 2026-04-08
description: 學習如何在 Aspose.3D for Java 中建立具有偏移頂部的圓柱體、加入子節點 Java、設定偏移頂部、生成 3D 模型，並使用
  Aspose 臨時授權匯出 OBJ。
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Aspose 臨時授權 – 建立帶偏移頂部的圓柱 (Java)
second_title: Aspose.3D Java API
title: Aspose 臨時授權 – 建立頂部偏移的圓柱體 (Java)
url: /zh-hant/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose 臨時授權 – 建立具有偏移頂部的圓柱 (Java)

## 介紹

如果您想在基於 Java 的 3D 場景中 **create cylinder** 物件並設定自訂的偏移頂部，Aspose.3D 讓這個過程變得簡單直觀。在本教學中，我們將逐步說明從場景設定到將最終模型匯出為 OBJ 檔案的每個步驟，讓您能自信地將偏移頂部的圓柱整合到應用程式中。完成本指南後，您也會了解 **aspose temporary license** 如何讓您在不購買完整授權的情況下評估這些功能。

## 快速解答
- **使用的函式庫是什麼？** Aspose.3D for Java  
- **可以偏移圓柱的頂部嗎？** 可以，使用 `setOffsetTop`  
- **如何在 Java 中新增子節點？** 在根節點上呼叫 `createChildNode`  
- **可以匯出成哪種格式？** Wavefront OBJ (`java export obj`)  
- **測試時需要授權嗎？** 可使用 **aspose temporary license** 進行評估  

## 什麼是 Aspose 臨時授權？

**aspose temporary license** 是一種短期、免費的評估金鑰，於開發與測試期間解鎖 Aspose.3D for Java 的完整功能。它會移除評估水印，並允許您產生 3D 模型檔案（如 OBJ、STL、FBX），效果與正式授權相同。

## 為何使用 Aspose.3D for Java？

- **High‑level API：** 無需管理低階網格資料。  
- **Cross‑platform：** 可在任何相容 JVM 的環境執行。  
- **Built‑in exporters：** 直接儲存為 OBJ、STL、FBX 等格式。  
- **Extensible：** 輕鬆新增子節點、套用變換，並與其他 Java 函式庫整合。  

## 前置條件

在開始之前，請確保您已具備：

- **Java Development Kit (JDK)** – 已安裝相容版本。  
- **Aspose.3D for Java library** – 從官方網站 [here](https://releases.aspose.com/3d/java/) 下載最新 JAR。  
- 您偏好的 IDE（Eclipse、IntelliJ IDEA、NetBeans 等）。  

## 匯入套件

首先，匯入我們需要的類別。將以下敘述放在 Java 檔案的最上方：

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## 步驟指南

### 步驟 1：建立 Java 3D 場景

一個 **java 3d scene** 充當所有 3D 物件的容器。

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### 步驟 2：初始化具有偏移頂部的圓柱

此處說明 **how to create cylinder** 並設定自訂偏移。建構子定義半徑、高度、切片數、堆疊數，以及圓柱是否封閉。之後，我們使用 `setOffsetTop` 來移動頂部。

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### 步驟 3：新增子節點 Java – 附加第一個圓柱

我們在場景的根節點下建立子節點，並將圓柱移動到指定位置。

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### 步驟 4：初始化第二個圓柱（無偏移）

為了作比較，我們加入一個沒有偏移的普通圓柱。

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### 步驟 5：新增子節點 Java – 附加第二個圓柱

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### 步驟 6：Java 匯出 OBJ – 將場景儲存為 OBJ

最後，我們 **java export obj** 整個場景（兩個圓柱）為 Wavefront OBJ 檔案，該格式被廣泛的 3D 工具支援。

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

執行程式後，您會在指定目錄中找到 `CustomizedOffsetTopCylinder.obj`，即可在 Blender、Maya 或其他支援 OBJ 的檢視器中開啟。

## 如何在 Java 中產生 3D 模型並匯出 OBJ

結合 `Scene.save(..., FileFormat.WAVEFRONTOBJ)` 與 **aspose temporary license**，您可以快速 **generate 3d model** 檔案，無需外部轉換工具。這在原型開發或與設計師共享資產時特別方便。

## 真實案例

- **Architectural visualisation：** 偏移頂部的圓柱可用於建模向天花板收斂的柱子。  
- **Mechanical parts：** 可建立活塞或齒輪外殼，頂部表面特意偏移。  
- **Game assets：** 即時產生多樣化的柱形資產，減少手工製作網格的需求。  

## 常見問題與解決方案

| 問題 | 原因 | 解決方法 |
|-------|--------|-----|
| **OBJ 檔案為空** | 場景未正確儲存或路徑錯誤。 | 確認輸出目錄存在且您具有寫入權限。 |
| **Offset not applied** | 使用較舊的 Aspose.3D 版本。 | 更新至支援 `setOffsetTop` 的最新函式庫。 |
| **Child node not visible** | Transformation not applied。 | 在建立子節點後，確保呼叫 `getTransform().setTranslation`。 |

## 常見問答

**Q: Aspose.3D 是否相容於不同的 Java IDE？**  
A: 是的，它可無縫運作於 Eclipse、IntelliJ IDEA、NetBeans 以及其他 IDE。

**Q: 我可以為建立的 3D 物件套用材質嗎？**  
A: 當然可以！使用 `Material` 類別來指派紋理與表面屬性。

**Q: Aspose.3D 有哪些授權方案？**  
A: 提供多種授權模式，您可於 [here](https://purchase.aspose.com/buy) 了解詳情。

**Q: 如何取得協助或分享使用經驗？**  
A: 可前往 Aspose.3D 社群論壇 [here](https://forum.aspose.com/c/3d/18) 取得支援與討論。

**Q: 是否提供測試用的臨時授權？**  
A: 有的，您可在 [here](https://purchase.aspose.com/temporary-license/) 取得 **aspose temporary license** 以供評估。

---

**最後更新：** 2026-04-08  
**測試版本：** Aspose.3D for Java 24.12 (latest)  
**作者：** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}