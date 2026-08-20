---
date: 2026-06-03
description: 了解如何將場景匯出為 FBX，並使用 Aspose.3D for Java 建立 3D 圓柱體、盒子及其他基礎模型。
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: 使用 Aspose.3D for Java 建立基礎 3D 模型
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: 將場景匯出為 FBX 並使用 Aspose.3D Java 建立圓柱體
url: /zh-hant/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 匯出場景為 FBX 並使用 Aspose.3D Java 建立圓柱

## 介紹

如果你曾經需要直接從 Java 程式碼 **建立 3D 圓柱**（或任何其他基本形狀），Aspose.3D 讓這項工作變得輕鬆無痛。在本教學中，我們將逐步說明完整工作流程——從環境設定到 **匯出場景為 FBX**——讓你能立即以程式方式產生 3D 幾何。你將看到函式庫如何處理基元、如何在場景圖中組織它們，以及如何將結果儲存為 Unity、Blender 或其他 3D 工具皆能讀取的格式。

## 快速解答
- **什麼函式庫可以讓我在 Java 中建立 3D 圓柱？** Aspose.3D for Java.  
- **我可以將場景匯出為哪種格式？** FBX (ASCII 7500) 使用 `FileFormat.FBX7500ASCII`.  
- **開發時需要授權嗎？** 免費試用可用於測試；正式上線需購買永久授權。  
- **支援的主要基元有哪些？** Box、Cylinder、Sphere、Cone，以及超過 10 種其他形狀。  
- **程式碼是否相容於 Java 8 及以上版本？** 是，Aspose.3D 以 JDK 8+ 為目標。  

## 什麼是 3D 圓柱基元？

圓柱基元是一種以半徑與高度定義的基本幾何形狀。在許多 3D 工作流程中，它是管道、車輪或建築柱等更複雜模型的組件。Aspose.3D 提供即用的 `Cylinder` 類別，讓你無需手動計算頂點。

## 為什麼要使用 Aspose.3D for Java？

Aspose.3D for Java 提供完整的純 Java 3D 引擎，免除本機函式庫的需求，讓跨平台開發變得理想。它支援多種匯入與匯出格式，提供穩健的場景圖以進行階層式組織，且內建基元讓你以最少程式碼建立幾何。這些功能共同加速開發並降低維護負擔。

- **功能完整的 3D 引擎** – 支援 **30 多** 種流行格式的匯入/匯出（FBX、OBJ、STL、GLTF、3DS 等）。  
- **純 Java API** – 無本機相依，適合跨平台專案。  
- **穩健的場景圖** – 讓你以階層方式組織物件，便於管理大型場景。  
- **授權簡易** – 可先使用免費試用，正式上線時升級為永久授權。  

## 前置條件

在深入程式碼之前，請確保你已具備以下條件：

1. **Java Development Kit (JDK)** – 已在機器上安裝 JDK 8 或更新版本。  
2. **Aspose.3D for Java 函式庫** – 從 [download page](https://releases.aspose.com/3d/java/) 下載並安裝。  

## 匯入套件

首先匯入核心的 Aspose.3D 命名空間，即可取得 `Scene`、`Box`、`Cylinder` 以及檔案格式常數的存取權。

```java
import com.aspose.threed.*;
```

現在函式庫已被引用，讓我們建立一個場景並加入一些基元幾何。

## 如何匯出場景為 FBX 並建立 3D 基元？

載入新的 `Scene` 物件，加入基元節點（Box、Cylinder 等），然後使用 FBX7500ASCII 格式呼叫 `save`。只需幾行程式碼，即可取得完整的 FBX 檔案，能在任何主流 3D 編輯器中開啟，實現與遊戲引擎、渲染管線或 AR/VR 應用的無縫整合。

### 步驟 1：初始化 Scene 物件

`Scene` 類別是 Aspose.3D 的最高層容器，用於在記憶體中保存所有節點、光源、相機與材質。

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### 步驟 2：建立 3D 方塊模型

`Box` 類別代表長方體，適合用來測試座標系統。將它作為場景根節點的子節點加入，即會位於原點。

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### 步驟 3：建立 3D 圓柱模型

`Cylinder` 類別是 Aspose.3D 內建的圓柱基元。它預設尺寸為（半徑 = 1，高度 = 2），但可透過建構子自訂。

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### 步驟 4：以 FBX 格式儲存圖形

組裝完場景後，將其匯出讓其他工具（例如 Unity、Blender）能讀取。我們使用 `FBX7500ASCII` 格式，該格式支援廣泛且可讀性高。

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## 常見問題與解決方案

| 問題 | 為何發生 | 解決方法 |
|-------|----------------|-----|
| **儲存時找不到檔案** | `myDir` 指向不存在的資料夾 | 確認目錄存在，或使用 `new File(myDir).mkdirs();` 建立。 |
| **匯出後場景為空** | 在呼叫 `save` 前未加入任何節點 | 確認已執行 `createChildNode` 呼叫（可用 `scene.getRootNode().getChildCount()` 進行除錯）。 |
| **授權例外** | 生產環境中未使用有效授權 | 使用 `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` 申請臨時或永久授權。 |

## 常見問與答

**Q: 我可以將 Aspose.3D for Java 與其他程式語言一起使用嗎？**  
A: Aspose.3D 主要支援 Java，但亦提供 .NET 與 C++ 版本。

**Q: Aspose.3D 適合用於複雜的 3D 建模任務嗎？**  
A: 絕對適合。它提供完整功能集——包括網格操作、材質指派與動畫——適用於簡單基元與複雜模型。

**Q: 我可以在哪裡取得更多協助與支援？**  
A: 前往 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 取得社群支援與討論。

**Q: 我可以在購買前試用 Aspose.3D 嗎？**  
A: 可以，你可以在做出購買決策前探索 [free trial](https://releases.aspose.com/)。

**Q: 我該如何取得 Aspose.3D 的臨時授權？**  
A: 你可以透過網站取得 [temporary license](https://purchase.aspose.com/temporary-license/)。

## 結論

現在你已學會如何 **匯出場景為 FBX**，以及如何使用 Aspose.3D for Java **建立 3D 圓柱**、方塊與其他基元模型。隨意嘗試其他基元，如 Sphere、Cone 或 Torus，並探索材質指派，使模型呈現真實外觀。熟悉後，你即可將產生的 FBX 檔案整合至遊戲引擎、AR/VR 管線或任何後續的 3D 工作流程。

---

**Last Updated:** 2026-06-03  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose

## 相關教學

- [如何將場景匯出為 FBX 並在 Java 中取得 3D 場景資訊](/3d/java/3d-scenes-and-models/get-scene-information/)
- [如何匯出 FBX 並在 Java 中建立節點層級結構](/3d/java/geometry/build-node-hierarchies/)
- [如何使用 Aspose.3D for Java 建立圓柱模型](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}