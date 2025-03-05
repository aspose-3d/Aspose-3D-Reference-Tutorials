---
title: 使用 Aspose.3D 透過變換矩陣變換 3D 節點
linktitle: 使用 Aspose.3D 在 Java 中透過變換矩陣變換 3D 節點
second_title: Aspose.3D Java API
description: 使用 Aspose.3D 探索 Java 中的 3D 圖形世界。學習使用變換矩陣輕鬆變換節點。
type: docs
weight: 21
url: /zh-hant/java/geometry/transform-3d-nodes-with-matrices/
---
## 介紹

歡迎閱讀本逐步指南，了解如何使用 Aspose.3D 在 Java 中透過變換矩陣變換 3D 節點。如果您是一位希望提高 3D 圖形和建模技能的 Java 開發人員，那麼您來對地方了。在本教程中，我們將深入探討在 Aspose.3D 框架內將轉換應用於 3D 節點的過程。

## 先決條件

在我們開始之前，請確保您符合以下先決條件：

- Java 程式設計的基礎知識。
-  Aspose.3D 庫已安裝。您可以從以下位置下載：[這裡](https://releases.aspose.com/3d/java/).
- 用於 Java 開發的工作整合開發環境 (IDE)。

## 導入包

在您的 Java 專案中，從 Aspose.3D 匯入必要的套件。確保您的專案配置正確以使用 Aspose.3D 庫。這是一個範例導入語句：

```java
import com.aspose.threed.*;

```

## 變換 3D 節點

### 第 1 步：初始化場景對象

首先初始化場景對象，該物件充當 3D 元素的容器。

```java
Scene scene = new Scene();
```

### 第2步：初始化節點類別對象

建立一個 Node 類別對象，例如一個立方體，它將進行轉換。

```java
Node cubeNode = new Node("cube");
```

### 第 3 步：使用多邊形生成器建立網格

利用 Common 類別使用多邊形生成器方法建立網格。這將設定立方體的網格實例。

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### 第 4 步：將節點指向網格幾何體

將建立的網格指派給立方體節點。

```java
cubeNode.setEntity(mesh);
```

### 第5步：設定自訂翻譯矩陣

將自訂平移矩陣套用到立方體節點。此範例設定用於平移的變換矩陣。

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### 第 6 步：將立方體加入場景中

將立方體節點包含在場景的根節點中。

```java
scene.getRootNode().addChildNode(cubeNode);
```

### 第 7 步：儲存 3D 場景

指定以支援的檔案格式（例如 FBX）儲存 3D 場景的目錄和檔案名稱。

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## 結論

恭喜！您已經成功學習如何在 Java 中使用 Aspose.3D 轉換 3D 節點。嘗試不同的矩陣並探索 3D 圖形的無限可能性。

## 常見問題解答

### Q1：我可以對單一 3D 節點套用多個變換嗎？

A1：是的，您可以連接多個變換矩陣以進行複雜的變換。

### Q2：如何在Aspose.3D中旋轉3D物件？

A2：在變換矩陣中使用適當的旋轉矩陣來實現所需的旋轉。

### Q3：我可以創建的 3D 場景的大小有限制嗎？

A3：3D 場景的大小可能會受到系統資源的限制，但 Aspose.3D 是為了提高效率而設計的。

### Q4：在哪裡可以找到更多範例和文件？

 A4：訪問[Aspose.3D 文檔](https://reference.aspose.com/3d/java/)了解更多範例和詳細資訊。

### Q5：如何取得Aspose.3D的臨時授權？

 A5：您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).