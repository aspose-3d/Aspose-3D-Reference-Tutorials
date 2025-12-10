---
date: 2025-12-10
description: 學習如何在 Java 中使用 Aspose.3D 進行 3D 物件的平移。掌握幾何變換、節點平移以及全域變換。
linktitle: How to Translate 3D in Java with Aspose.3D
second_title: Aspose.3D Java API
title: 如何在 Java 中使用 Aspose.3D 進行 3D 平移
url: /zh-hant/java/geometry/expose-geometric-transformations/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Java 3D 中使用 Aspose.3D 暴露幾何變換

## 介紹

在動態變化的 Java 3D 程式開發領域，掌握幾何變換是一項關鍵技能。在本教學中，**您將學會如何使用 Aspose.3D 在 Java 中平移 3D 物件**，這是一個簡化 3D 建模的強大函式庫。我們將逐步說明如何初始化節點、套用幾何平移，並評估全域變換，讓您即時看到效果。

## 快速回答
- **主要目標是什麼？** 學習如何在 Java 中使用 Aspose.3D 平移 3D 物件。  
- **使用哪個函式庫？** Aspose.3D for Java。  
- **需要授權嗎？** 測試階段需要臨時授權；正式上線則需正式授權。  
- **程式碼行數多少？** 少於 20 行即可完成平移並取得結果。  
- **可以在任何作業系統上執行嗎？** 可以，只要安裝相容的 JDK 即可。

## 如何在 Java 中平移 3D 物件
了解每一步驟後，您可以輕鬆在任何專案中複製此流程。以下是一個簡潔的逐步指南，直接貼到 IDE 即可使用。

## 前置條件

在開始使用 Aspose.3D 進行幾何變換之前，請先確保具備以下條件：

1. **Java Development Kit (JDK)：** Aspose.3D for Java 需要相容的 JDK。您可於[此處](https://www.oracle.com/java/technologies/javase-downloads.html)下載最新 JDK。  
2. **Aspose.3D 函式庫：** 前往[發佈頁面](https://releases.aspose.com/3d/java/)下載 Aspose.3D 函式庫，並將其整合至您的 Java 專案。

## 匯入套件

取得 Aspose.3D 函式庫後，匯入必要的套件以開啟 3D 幾何變換之旅。將以下程式碼加入您的 Java 檔案：

```java
import com.aspose.threed.Node;
import com.aspose.threed.Vector3;
```

## 步驟 1：初始化 Node

我們的 3D 世界從 `Node` 開始。於 Java 程式碼中建立新的 `Node` 物件：

```java
// ExStart: Step 1 - Initialize Node
Node n = new Node();
// ExEnd: Step 1
```

## 步驟 2：幾何平移

接下來，為節點套用幾何平移。此步驟會將節點在 3D 空間中移動。使用以下程式碼設定幾何平移：

```java
// ExStart: Step 2 - Geometric Translation
n.getTransform().setGeometricTranslation(new Vector3(10, 0, 0));
// ExEnd: Step 2
```

## 步驟 3：評估全域變換

為了觀察幾何變換的效果，讓我們評估節點的全域變換。此步驟會輸出變換矩陣，包含幾何變換資訊：

```java
// ExStart: Step 3 - Evaluate Global Transform
System.out.println(n.evaluateGlobalTransform(true));
System.out.println(n.evaluateGlobalTransform(false));
// ExEnd: Step 3
```

恭喜！您已成功在 Java 3D 中使用 Aspose.3D 暴露幾何變換。

## 結論

在本教學中，我們帶您了解如何在 Java 3D 中使用 Aspose.3D 進行幾何變換。透過初始化節點、套用幾何平移與評估全域變換，您已掌握 3D 程式開發的基礎，未來可進一步構建更複雜的場景、動畫或結合物理模擬。

## 常見問題

### Q1: Aspose.3D 是否相容所有 Java 開發環境？

A1: Aspose.3D 可無縫整合至任何支援 JDK 的 Java 開發環境。

### Q2: 我可以在哪裡找到 Aspose.3D 的完整文件說明？

A2: 請參考[文件說明](https://reference.aspose.com/3d/java/)，獲取 Aspose.3D 功能的詳細資訊。

### Q3: 購買前我可以先試用 Aspose.3D for Java 嗎？

A3: 可以，您可透過[免費試用](https://releases.aspose.com/)先行體驗。

### Q4: 若有 Aspose.3D 相關問題，我該如何取得支援？

A4: 請前往[Aspose.3D 社群支援論壇](https://forum.aspose.com/c/3d/18)尋求協助。

### Q5: 測試 Aspose.3D 時需要臨時授權嗎？

A5: 請取得[臨時授權](https://purchase.aspose.com/temporary-license/)，以供測試使用。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2025-12-10  
**測試環境：** Aspose.3D Java 24.11（撰寫時最新版本）  
**作者：** Aspose  

---