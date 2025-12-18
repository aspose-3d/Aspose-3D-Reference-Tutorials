---
date: 2025-12-18
description: 學習如何使用 Aspose.3D for Java 建立 3D 場景並儲存 OBJ 檔案。請跟隨我們的逐步指南了解線性擠出方向。
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 建立 3D 場景 – 設定 擠出方向 Aspose.3D Java
url: /zh-hant/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 建立 3D 場景 – 設定拉伸方向 Aspose.3D Java

## 簡介

在本教學中，您將學習 **如何建立 3d 場景** 物件，並使用 Aspose.3D for Java 控制拉伸方向。無論是建構建築視覺化、產品原型或遊戲資產，掌握線性拉伸都能讓您快速建模複雜形狀。我們將逐步說明，從在 Java 中加入節點到 **匯出 3d 模型 obj** 檔案，讓您即時看到結果。

## 快速解答
- **「建立 3d 場景」是什麼意思？** 代表初始化一個 Aspose.3D `Scene` 物件，用來容納所有幾何、光源與相機。  
- **如何設定拉伸方向？** 在 `LinearExtrusion` 實例上使用 `setDirection(Vector3)` 方法。  
- **應該使用哪種格式匯出？** OBJ 格式 (`FileFormat.WAVEFRONTOBJ`) 在 3‑D 工作流程中支援度最高。  
- **使用 Aspose.3D 是否需要授權？** 開發階段可使用免費試用版；正式上線需購買商業授權。  
- **可以在 Java 中加入更多節點嗎？** 可以——使用 `scene.getRootNode().createChildNode()` 依需求新增任意物件。

## 「建立 3d 場景」工作流程是什麼？

**建立 3d 場景**流程從一個空的 `Scene` 物件開始，加入幾何（例如拉伸輪廓），透過變換定位，最後將場景儲存為 OBJ 等檔案格式。此模式是使用 Aspose.3D 建置大多數 3‑D 應用程式的核心。

## 為什麼要設定拉伸方向？

設定拉伸方向可讓您在拉伸過程中傾斜、旋轉或斜切形狀，從而在不需額外後處理的情況下掌控最終幾何形狀。此功能特別適用於：

- 建立錐形柱或客製化管線。  
- 在機械零件中對齊非標準軸向的拉伸。  
- 為視覺特效產生藝術形狀。

## 前置條件

在開始之前，請確保您已具備：

- 基本的 Java 知識。  
- 已安裝 Aspose.3D 程式庫——可從 [此處](https://releases.aspose.com/3d/java/) 下載。  
- 如 Eclipse 或 IntelliJ IDEA 等開發環境。

## 匯入套件

首先，匯入所需的 Aspose.3D 類別：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步驟 1：初始化基礎輪廓

建立將被拉伸的 2‑D 輪廓。此範例使用圓角矩形：

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **專業提示：** 調整圓角半徑即可控制矩形落在拉伸前的銳利或平滑程度。

## 步驟 2：建立場景

現在我們 **建立 3d 場景**，作為物件的容器：

```java
Scene scene = new Scene();
```

## 步驟 3：在 Java 中加入節點 – 定位物件

我們將在場景根節點下加入兩個子節點（左、右），並將左側節點稍微向側邊移動：

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步驟 4：如何拉伸 – 左節點（預設方向）

在左節點上使用預設 Z 軸方向拉伸輪廓，並設定完整 360° 扭轉與較高的切片數以提升平滑度：

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 步驟 5：如何設定方向 – 右節點

此處我們 **設定方向**，提供自訂的 `Vector3`，使拉伸傾斜至向量 (0.3, 0.2, 1)：

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 步驟 6：儲存 OBJ 檔案 – 匯出 3D 模型

最後，我們 **儲存 obj 檔案**，以便在任何 3‑D 檢視器中檢視結果：

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

開啟產生的 OBJ 檔案時，您會看到兩個拉伸的矩形：一個使用預設方向，另一個則依設定的向量傾斜。

## 常見問題與解決方案

| 問題 | 原因 | 解決方法 |
|------|------|----------|
| OBJ 檔案為空 | 場景未儲存或路徑錯誤 | 確認 `MyDir` 指向可寫入的資料夾，且檔名以 `.obj` 結尾。 |
| 拉伸外觀扁平 | `setSlices` 設定過低 | 增加 `setSlices`（例如 200）以取得更平滑的幾何。 |
| 方向未變化 | 向量未正規化 | 使用正規化的 `Vector3`，或調整數值以符合預期的傾斜角度。 |

## 常見問題

### Q1：我可以在其他程式語言中使用 Aspose.3D 嗎？
A1：Aspose.3D 支援多種語言，包括 .NET 與 Java。

### Q2：Aspose.3D 有提供免費試用嗎？
A2：有，您可於此處取得免費試用版 [here](https://releases.aspose.com/)。

### Q3：哪裡可以找到 Aspose.3D for Java 的詳細文件？
A3：完整文件可於此處取得 [here](https://reference.aspose.com/3d/java/)。

### Q4：如何取得 Aspose.3D 的支援？
A4：請前往 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 尋求協助或提出問題。

### Q5：Aspose.3D 是否提供臨時授權？
A5：有，您可於此處取得臨時授權 [here](https://purchase.aspose.comtemporary-license/)。

---

**最後更新：** 2025-12-18  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}