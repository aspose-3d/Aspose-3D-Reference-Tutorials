---
date: 2026-02-22
description: 學習如何在直線擠出中設定方向，並使用 Aspose.3D for Java 匯出 3D 模型 OBJ。請跟隨我們的逐步指南。
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 如何在 Aspose.3D for Java 中設定線性擠出方向
url: /zh-hant/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D for Java 中設定線性擠出方向

## 簡介

在本完整教學中，您將了解在使用 Aspose.3D for Java 進行線性擠出時，**如何設定方向**。無論您是構建類 CAD 工具或為遊戲引擎產生幾何體，控制擠出方向都能讓您精確打造所需形狀。我們將一步步說明，從初始化輪廓到將結果儲存為 OBJ 檔案，讓您也能直接從 Java **匯出 3d model obj** 檔案。

## 快速答案
- **什麼是線性擠出的主要類別？** `LinearExtrusion`
- **哪個方法定義擠出方向？** `setDirection(Vector3 direction)`
- **我可以將結果匯出為 OBJ 嗎？** Yes, using `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **開發是否需要授權？** A free trial is available; a license is required for production.
- **哪個 Java IDE 最適合？** IntelliJ IDEA or Eclipse are both fully supported.

## 什麼是線性擠出？

線性擠出是將 2‑D 輪廓（例如矩形或圓形）沿直線延伸，產生 3‑D 實體。預設情況下，擠出沿正 Z 軸方向，但 Aspose.3D 可透過 `setDirection` 屬性變更此路徑。

## 為什麼要在線性擠出中設定方向？

- 使幾何體與場景中已有物件對齊。
- 在不需額外變換步驟的情況下建立斜角或傾斜的零件。
- 匯出必須符合特定座標系統的模型（例如 3‑D 列印或遊戲引擎）。

## 先決條件

在開始之前，請確保您已具備：

- 基本的 Java 知識。
- 已安裝 Aspose.3D 程式庫。您可從 [此處](https://releases.aspose.com/3d/java/) 下載。
- 如 Eclipse 或 IntelliJ IDEA 等開發環境。

## 匯入套件

首先，匯入提供核心 3‑D 類別與實用型別的命名空間。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步驟 1：初始化基礎輪廓

建立將要被擠出的形狀。本範例使用帶有小圓角半徑的 `RectangleShape`，使邊緣呈現平滑外觀。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 步驟 2：建立場景

`Scene` 物件作為所有 3‑D 節點、光源、相機與材質的容器。

```java
Scene scene = new Scene();
```

## 步驟 3：建立節點

在場景根節點下新增兩個子節點——左側擠出與右側擠出各一個。右側節點會平移，以避免兩個物件重疊。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步驟 4：在左側節點執行線性擠出

在左側節點使用預設 Z 軸方向擠出輪廓。我們同時加入完整 360° 的扭轉，並提升切片數量以獲得更平滑的網格。

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 步驟 5：在右側節點以自訂方向執行線性擠出

這裡我們 **設定方向**。透過將自訂的 `Vector3` 傳入 `setDirection`，擠出會沿向量 (0.3, 0.2, 1) 方向，產生斜斜的形狀。

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 步驟 6：儲存 3D 場景

最後，將場景匯出為 Wavefront OBJ 格式。此步驟示範如何 **save obj file java** 專案，並讓您能在任何 3‑D 檢視器中輕鬆檢視結果。

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常見問題與解決方案

| 問題 | 發生原因 | 解決方式 |
|-------|----------------|-----|
| OBJ 檔案顯示為空 | 輪廓未被加入到節點 | 確保在有效的節點上呼叫 `createChildNode` |
| 方向似乎未變更 | `setDirection` 在擠出已建立之後才被呼叫 | 如範例所示，在 `LinearExtrusion` 初始化時設定方向 |
| 網格解析度低 | `setSlices` 值過低 | 提升切片數量（例如 100 以上） |

## 結論

您現在已了解如何在 **設定方向** 的線性擠出、如何調整扭轉與切片設定，以及如何使用 Aspose.3D for Java **匯出 3d model obj** 檔案。這些技巧讓您對幾何體的建立擁有精細的控制，並能輕鬆將 3‑D 資產整合至更大的工作流程中。

## 常見問答

### Q1：我可以將 Aspose.3D 與其他程式語言一起使用嗎？

A1：Aspose.3D 支援多種程式語言，包括 .NET 與 Java。

### Q2：Aspose.3D 是否提供免費試用？

A2：是的，您可透過免費試用 [此處](https://releases.aspose.com/) 了解 Aspose.3D 的功能。

### Q3：在哪裡可以找到 Aspose.3D for Java 的詳細文件？

A3：完整文件可於 [此處](https://reference.aspose.com/3d/java/) 取得。

### Q4：如何取得 Aspose.3D 的支援？

A4：請前往 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 獲得協助或詢問。

### Q5：Aspose.3D 是否提供臨時授權？

A5：是的，您可於 [此處](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2026-02-22  
**測試環境：** Aspose.3D for Java（最新版本）  
**作者：** Aspose