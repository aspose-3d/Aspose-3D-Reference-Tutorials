---
date: 2025-11-29
description: 了解如何 **在 Java 中建立 3D 場景**，以及在 Aspose.3D for Java 中使用類 XPath 的查詢 **按類型選取物件**。
language: zh-hant
linktitle: Create 3D Scene Java – Apply XPath‑Like Queries with Aspose.3D
second_title: Aspose.3D Java API
title: 建立 3D 場景（Java） – 使用 Aspose.3D 進行類 XPath 查詢
url: /java/3d-objects-and-scenes/xpath-like-object-queries/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 建立 3D 場景 Java – 使用 XPath‑Like 查詢與 Aspose.3D

## 介紹  

如果您需要 **create 3d scene java** 應用程式來操作複雜的物件層級，Aspose.3D for Java 為您提供一種乾淨、類 XPath 的方式，精準定位所需的項目。在本教學中，我們將示範如何建立簡易場景、加入層級節點，並使用 XPath‑like 查詢來 **select objects by type**（例如相機或燈光），不論它們位於樹狀結構的哪個位置。完成後，您將能僅透過一行表達式就完成查詢、篩選與取得 3‑D 實體。

## 快速答覆
- **我可以查詢什麼？** 任何節點或實體（Camera、Light、Mesh 等）於 Scene 中。  
- **如何依類型 select objects by type？** 使用類 XPath 表達式，例如 `//*[(@Type='Camera')]`。  
- **開發是否需要授權？** 免費試用可用於測試；正式上線需購買授權。  
- **支援哪個 Java 版本？** Java 8 及以上版本。  
- **在哪裡下載 Aspose.3D？** 請前往先決條件中提供的官方下載頁面。

## 先決條件  

開始之前，請確保您已具備：

- 已在 **您的**機器上安裝 Java Development Kit (JDK)。  
- 已下載並設定 Aspose.3D for Java 函式庫。您可以在 **[此處](https://releases.aspose.com/3d/java/)** 取得下載連結。  
- 具備基本的 Java 程式設計知識。  

## 匯入套件  

首先，匯入您將使用的 Aspose.3D 類別。此步驟會讓函式庫在專案中可用。

```java
import com.aspose.threed.*;

import java.util.ArrayList;
import java.util.List;
```

## 什麼是 Aspose.3D 中的 XPath‑like 查詢？  

Aspose.3D 實作了 XPath 語法的子集，可對場景圖 (scene graph) 進行查詢。表達式的目標不是 XML 節點，而是 **A3DObject** 實例（節點、相機、燈光、網格等）。這讓您能寫出如「所有相機」或「名稱為 ‘light’ 的物件」等具表現力的過濾條件，而不必手動遍歷層級。

## 為何使用 XPath‑like 查詢來 **select objects by type**？  

- **速度：** 一行程式碼即可取代數十個 `if` 判斷與迴圈。  
- **可讀性：** 查詢語句如同自然語言般易懂。  
- **彈性：** 只需修改過濾條件，即可改變查詢結果，無需觸碰遍歷程式碼。

## 步驟說明  

### 步驟 1：建立測試用的 Scene  

我們先建立一個空的 Scene，作為層級的容器。

```java
// ExStart:CreateScene
Scene s = new Scene();
// ExEnd:CreateScene
```

### 步驟 2：建構節點層級  

接著，在根節點下加入幾個子節點。部分節點會包含 **Camera** 或 **Light** 實體，稍後將對它們進行查詢。

```java
// ExStart:CreateHierarchy
Node a = s.getRootNode().createChildNode("a");
a.createChildNode("a1");
a.createChildNode("a2");
s.getRootNode().createChildNode("b");
Node c = s.getRootNode().createChildNode("c");
c.createChildNode("c1").addEntity(new Camera("cam"));
c.createChildNode("c2").addEntity(new Light("light"));
// ExEnd:CreateHierarchy
```

### 步驟 3：套用 XPath‑Like 查詢  

現在進入重點——使用 XPath 風格的字串來 **select objects by type** 或依名稱查詢。

```java
// ExStart:XPathLikeObjectQueries
// Select objects that have type Camera or name is 'light' regardless of their location.
List<Object> objects = s.getRootNode().selectObjects("//*[(@Type = 'Camera') or (@Name = 'light')]");

// Select a single camera object under the child nodes of the node named 'c' under the root node
A3DObject c1 = (A3DObject) s.getRootNode().selectSingleObject("/c/*/<Camera>");

// Select the node named 'a1' under the root node, even if 'a1' is not a directly child node
A3DObject obj = (A3DObject) s.getRootNode().selectSingleObject("a1");

// Select the node itself, as '/' is selected directly on the root node
obj = (A3DObject) s.getRootNode().selectSingleObject("/");
// ExEnd:XPathLikeObjectQueries
```

**關鍵表達式說明**

- `//*[(@Type = 'Camera') or (@Name = 'light')]` – 找出場景中所有 **type** 屬性等於 `Camera` **或** **name** 屬性等於 `light` 的物件。這是 **select objects by type** 的典型範例。  
- `/c/*/<Camera>` – 從根節點開始，前往節點 `c`，再到任意子節點 (`*`)，最後選取 `<Camera>` 實體。  
- `a1` – 簡寫形式，搜尋整個樹中名稱為 `a1` 的節點。  
- `/` – 回傳根節點本身。  

### 常見問題與技巧  

- **大小寫敏感：** 屬性名稱 (`@Type`、`@Name`) 必須符合大小寫。  
- **實體 vs. 節點：** 只有在需要取得底層實體時才使用 `<Camera>` 語法，若僅需節點本身則不必。  
- **效能考量：** 對於極大型的場景，建議縮小搜尋範圍（例如從特定子樹開始），以提升查詢速度。  

## 結論  

現在您已掌握如何利用 XPath‑like 查詢，在 **create 3d scene java** 程式中高效 **select objects by type**。此方法可從簡易示範擴展至生產等級的 3‑D 應用，讓您在不撰寫冗長程式碼的前提下，對場景遍歷擁有精細的控制。

## 常見問答  

**Q: 在哪裡可以找到 Aspose.3D for Java 的文件？**  
A: 文件可於 **[此處](https://reference.aspose.com/3d/java/)** 取得。  

**Q: 如何下載 Aspose.3D for Java？**  
A: 請前往 **[此處](https://releases.aspose.com/3d/java/)** 下載。  

**Q: 有提供免費試用嗎？**  
A: 有，您可在 **[此處](https://releases.aspose.com/)** 取得免費試用版。  

**Q: 在哪裡可以取得 Aspose.3D for Java 的技術支援？**  
A: 請造訪支援論壇 **[此處](https://forum.aspose.com/c/3d/18)**。  

**Q: 需要臨時授權嗎？**  
A: 可於 **[此處](https://purchase.aspose.com/temporary-license/)** 取得臨時授權。  

**Q: 能否查詢自訂的使用者屬性？**  
A: 可以，您可在 XPath 表達式中加入自行新增的 `@` 屬性以進行查詢。  

**Q: 查詢引擎能否用於動畫場景？**  
A: 能——查詢作用於靜態層級；動畫是附加在同一節點上，故亦會被納入結果。  

---

**最後更新：** 2025-11-29  
**測試環境：** Aspose.3D for Java 24.11  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}