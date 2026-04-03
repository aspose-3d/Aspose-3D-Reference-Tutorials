---
date: 2026-04-03
description: 學習如何在 Java 中使用 Aspose.3D 建立圓柱形風扇形狀。本指南涵蓋 Java 3D 建模及保存 OBJ 檔案的 Java 技術。
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
linktitle: 如何使用 Aspose.3D for Java 建立圓柱形風扇形狀
second_title: Aspose.3D Java API
title: 如何使用 Aspose.3D for Java 建立圓柱形風扇形狀
url: /zh-hant/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用 Aspose.3D for Java 建立圓柱風扇形狀

## 介紹

準備好在 Java 環境中精通 **如何建立圓柱風扇形狀** 嗎？在本教學中，我們將逐步說明從設定場景到匯出 Wavefront OBJ 檔案的每個步驟，全部使用 Aspose.3D。無論您是製作遊戲資產、CAD 原型，或僅僅在嘗試 3D 幾何，您都會看到使用這個強大函式庫進行 Java 3D 建模是多麼簡單。

## 快速答案
- **主要目標是什麼？** 建立可自訂的風扇形圓柱並將其儲存為 OBJ 檔案。  
- **使用哪個函式庫？** Aspose.3D for Java。  
- **需要授權嗎？** 免費試用可用於開發；商業授權則需於正式環境使用。  
- **前置條件是什麼？** 已安裝 JDK 並將 Aspose.3D Java 套件加入專案。  
- **可以匯出其他格式嗎？** 可以——Aspose.3D 支援多種格式；本範例使用 Wavefront OBJ。

## 什麼是風扇圓柱？

風扇圓柱是一種部分表面的圓柱，其圓形底部的某個扇形被省略，形成「風扇」開口。此幾何形狀適用於可視化切片、儀表板或自訂機械零件。

## 為什麼使用 Aspose.3D 進行 Java 3D 建模？

Aspose.3D 提供乾淨、物件導向的 API，將 3D 圖形的低階數學抽象化。您可以專注於設計，而不必處理檔案格式的細節，且函式庫會自動處理 **save obj file java** 的操作。

## 前置條件

在開始之前，請確保您已具備：

- **Java Development Kit (JDK)** – 前往 [此處](https://www.oracle.com/java/technologies/javase-downloads.html) 下載。  
- **Aspose.3D for Java** – 從 [下載連結](https://releases.aspose.com/3d/java/) 取得最新的 JAR。  

將 Aspose.3D JAR 加入專案的 classpath。

## 匯入套件

首先匯入必要的類別。這樣即可存取 3D 場景、幾何基元與實用方法。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步驟 1：建立場景

首先，我們實例化一個新的 `Scene`。可以將場景視為容納所有 3D 物件、光源與相機的容器。

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## 步驟 2：建立風扇圓柱（如何建立圓柱）

現在我們建立風扇圓柱本身。建構子參數定義半徑、高度、細分程度，以及幾何是否以風扇方式產生。

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **專業提示：** 調整 `setThetaLength` 以改變開口角度。270° 會產生三分之四的風扇；180° 則會得到半圓柱。

## 步驟 3：定位風扇圓柱

接著，我們將風扇圓柱加入場景並移動到合適的位置。平移座標的順序為 (X, Y, Z)。

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## 步驟 4：建立非風扇圓柱（Java 3D 建模比較）

為了說明 Aspose.3D 的彈性，我們同時建立一個沒有風扇開口的普通圓柱。

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## 步驟 5：儲存場景（Java 儲存 OBJ 檔案）

最後，我們將整個場景匯出為 Wavefront OBJ 檔案。此格式被大多數 3D 編輯器與遊戲引擎廣泛支援。

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **注意：** 將 `"Your Document Directory"` 替換為您具有寫入權限的絕對或相對路徑。

## 如何在 Java 使用 Aspose 3D 儲存 OBJ 檔案

Aspose.3D 的 `Scene.save` 方法會自動處理 **aspose 3d export obj** 的過程。您只需指定目標檔名以及 `FileFormat.WAVEFRONTOBJ` 列舉值，如前一步所示。

## 常見問題與解決方案

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| OBJ 檔案為空 | 場景未儲存或路徑不正確 | 確認輸出目錄存在且具有寫入權限。 |
| 風扇開口不正確 | `ThetaLength` 值錯誤 | 使用 `MathUtils.toRadian(degrees)` 設定所需的精確角度。 |
| 編譯錯誤 | classpath 中缺少 Aspose.3D JAR | 將 JAR 加入專案的 `libs` 資料夾，並在建置路徑中包含它。 |

## 常見問答

**Q: Aspose.3D 是否相容於其他 Java 3D 函式庫？**  
A: 是的，Aspose.3D 可與 Java 3D 或 jMonkeyEngine 等函式庫共存，讓您能將自訂幾何整合至更大的工作流程。

**Q: 我可以進一步自訂風扇圓柱的外觀嗎？**  
A: 當然可以。您可以透過存取節點的 `Material` 與 `Light` 集合來套用材質、紋理與光源。

**Q: 我可以在哪裡取得額外支援？**  
A: 前往 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 獲得社群協助與官方回應。

**Q: 是否提供免費試用？**  
A: 有的，您可以在購買前透過 [免費試用](https://releases.aspose.com/) 來體驗 Aspose.3D。

**Q: 如何取得測試用的臨時授權？**  
A: 前往 [此處](https://purchase.aspose.com/temporary-license/) 取得，以在開發期間解鎖完整功能。

---

**最後更新：** 2026-04-03  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}