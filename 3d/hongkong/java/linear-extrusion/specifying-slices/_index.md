---
date: 2026-05-24
description: 了解如何使用 Aspose.3D for Java 透過切片建立 3D 拉伸。本分步指南涵蓋線性拉伸、設定圓角半徑，以及匯出 OBJ。
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: 使用切片建立 3D 拉伸 – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: 使用切片建立 3D 拉伸 – Aspose.3D for Java
url: /zh-hant/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用切片建立 3D 拉伸 – Aspose.3D for Java

## 介紹

如果您需要 **建立 3d 拉伸** 物件，使其外觀平滑且精確，控制切片數量是關鍵。在本教學中，我們將說明如何在使用 Aspose.3D for Java 執行線性拉伸時指定切片。您將了解為何切片數量重要、如何設定圓角半徑，以及如何將結果匯出為 OBJ 檔案，以便在任何 3‑D 流程中使用。

## 快速解答
- **“slices” 控制什麼？** 用於近似拉伸表面的中間橫截面數量。  
- **哪個方法設定切片數量？** `LinearExtrusion.setSlices(int)`  
- **我可以更改輪廓的圓角半徑嗎？** 是的，透過 `RectangleShape.setRoundingRadius(double)`  
- **此範例使用的檔案格式是什麼？** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **執行程式碼是否需要授權？** 免費試用可用於評估；商業授權則需於正式環境使用。

`LinearExtrusion.setSlices(int)` 設定拉伸將產生的中間切片數量。  
`RectangleShape.setRoundingRadius(double)` 定義矩形輪廓的角半徑。

## 如何使用 Java 及切片建立 3D 拉伸？

載入您的 2‑D 輪廓，選擇切片數量，設定圓角半徑，然後呼叫 `save` —— 整個工作流程只需幾行程式碼。Aspose.3D for Java 會自動處理幾何體建立、切片插值與 OBJ 匯出，讓您專注於視覺品質，而不必關心底層網格計算。

## 什麼是帶切片的線性拉伸？

帶切片的線性拉伸會將平面 2‑D 形狀沿直線掃掠，產生可設定數量的中間橫截面，從而形成 3‑D 實體。切片數量直接影響曲線邊緣（例如圓角）的平滑程度。

## 為何使用 Aspose.3D for Java 來建立 3D 拉伸？

Aspose.3D 提供對每個拉伸參數的 **完整程式控制**，支援 **超過 50 種輸入與輸出格式**（包括 OBJ、FBX、STL 與 GLTF），且能在不將整個檔案載入記憶體的情況下處理 **上百頁的模型**。它可在任何支援 Java 的平台上執行，無需原生 DLL，並保證在 Windows、Linux 與 macOS 上產生確定性的結果。

## 前置條件

1. **Java Development Kit** – 已安裝 JDK 8 或更新版本。  
2. **Aspose.3D for Java** – 從官方網站下載程式庫 [here](https://releases.aspose.com/3d/java/)。  
3. 您慣用的 IDE 或文字編輯器。

## 匯入套件

將 Aspose.3D 命名空間加入您的專案，以便存取 3‑D 建模類別。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 步驟指南

### 步驟 1：設定場景並定義輪廓

`RectangleShape` 是用於定義 2‑D 矩形輪廓的類別。  
首先，我們建立一個 `RectangleShape`，並給予 **圓角半徑** 使角落平滑。  
`Scene` 是所有節點與幾何體的根容器。  
接著，我們初始化一個新的 `Scene` 以容納所有幾何體。

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### 步驟 2：為每個拉伸建立子節點物件

`Node` 代表場景圖中的一個元素，可容納幾何體與變換。  
每個幾何體都位於 `Node` 之下。此處我們產生兩個同層節點 —— 一個用於低切片拉伸，另一個用於高切片拉伸 —— 並將左側節點稍微向旁邊移動，以便於比較結果。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 步驟 3：執行線性拉伸並設定切片

`LinearExtrusion` 是透過線性掃掠輪廓來建立實體的類別。  
`LinearExtrusion` 為 Aspose.3D 用於沿直線拉伸 2‑D 輪廓以產生實體的類別。使用 **匿名內部類別** 我們呼叫 `setSlices` 以控制平滑度。左側節點僅使用 2 個切片（粗糙），右側節點則使用 10 個切片（平滑）。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### 步驟 4：匯出 OBJ – 儲存場景

最後，我們將場景寫入 Wavefront OBJ 檔案，這是一種被廣泛支援的 3‑D 編輯器與遊戲引擎格式。此範例展示了 Aspose.3D 的 **export OBJ Java** 功能。

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常見問題與解決方案

| 問題 | 為何發生 | 解決方案 |
|------|----------|----------|
| **拉伸呈平面** | 切片數量設定為 1 或 0 | 確保 `setSlices` 的值 ≥ 2。 |
| **圓角看起來鋸齒狀** | 相對於切片數，圓角半徑過小 | 增加半徑或切片數以獲得更平滑的曲線。 |
| **儲存時找不到檔案** | `MyDir` 指向不存在的資料夾 | 事先建立目錄或使用絕對路徑。 |

## 常見問答

**問：如何下載 Aspose.3D for Java？**  
答：您可以從 [here](https://releases.aspose.com/3d/java/) 下載程式庫。

**問：在哪裡可以找到 Aspose.3D 的文件？**  
答：請參考文件 [here](https://reference.aspose.com/3d/java/)。

**問：是否提供免費試用？**  
答：是的，您可於 [here](https://releases.aspose.com/) 探索免費試用。

**問：如何取得 Aspose.3D 的支援？**  
答：請前往支援論壇 [here](https://forum.aspose.com/c/3d/18)。

**問：我可以購買臨時授權嗎？**  
答：是的，可於 [here](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

---

**最後更新：** 2026-05-24  
**測試環境：** Aspose.3D for Java 24.11（撰寫時最新）  
**作者：** Aspose

## 相關教學

- [使用 Aspose.3D 建立 3D 拉伸 Java](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [如何在 Aspose.3D for Java 中設定線性拉伸方向](/3d/java/linear-extrusion/setting-direction/)
- [使用扭轉在 Aspose.3D for Java 中建立 3D 場景](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}