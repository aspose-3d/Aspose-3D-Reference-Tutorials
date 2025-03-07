---
title: 使用 Aspose.3D for Java 控制線性拉伸的中心
linktitle: 使用 Aspose.3D for Java 控制線性拉伸的中心
second_title: Aspose.3D Java API
description: 使用 Aspose.3D 探索 Java 中的 3D 圖形世界。輕鬆控制線性擠壓的中心。
weight: 11
url: /zh-hant/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D for Java 控制線性拉伸的中心

## 介紹

在 3D 圖形和 Java 程式設計領域，控制線性擠出的中心對於在專案中實現所需效果起著至關重要的作用。 Aspose.3D for Java 提供了一個強大的工具包來無縫處理此類任務。在本教程中，我們將深入研究使用 Aspose.3D for Java 控制線性擠出中心的過程，分解每個步驟以確保順利、全面地理解。

## 先決條件

在我們開始本教程之旅之前，請確保您具備以下先決條件：

1. Java 開發環境：確保您的電腦上設定有 Java 開發環境。

2.  Aspose.3D for Java：下載並安裝 Aspose.3D 函式庫。您可以找到該庫及其文檔[這裡](https://reference.aspose.com/3d/java/).

3. 文件目錄：建立一個目錄來儲存您的 Java 文件。我們將其稱為“您的文檔目錄”。

## 導入包

在您的 Java 開發環境中，匯入 Aspose.3D 所需的套件。這確保您的程式碼可以存取該庫提供的功能。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 第 1 步：設定基本設定檔

初始化要拉伸的基礎輪廓。在此範例中，我們將使用圓角半徑為 0.3 的矩形。

```java
//文檔目錄的路徑。
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 第 2 步：建立 3D 場景

透過創建場景來建立 3D 世界的基礎。

```java
Scene scene = new Scene();
```

## 第三步：建立左右節點

在場景中建立左右節點。這些節點可作為 3D 物件的畫布。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 第 4 步：具有中心屬性的線性拉伸

對左側節點進行不居中的線性擠壓，切片數設定為3。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## 步驟 5：設定參考地平面

透過向左側節點添加地平面來增強視覺表示。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## 步驟6：具有中心屬性的線性拉伸（右節點）

在右側節點上執行線性拉伸，這次使拉伸居中，並再次將切片數設為 3。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## 步驟 7：設定參考地平面（右節點）

與左節點類似，為右節點新增地平面以供參考。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## 第 8 步：儲存 3D 場景

以 Wavefront OBJ 格式儲存 3D 場景。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 結論

使用 Aspose.3D for Java 控制線性擠壓中心為 3D 圖形開發帶來了令人興奮的可能性。透過遵循本逐步指南，您已經了解如何操作 center 屬性，從而使您能夠在 Java 專案中實現所需的視覺效果。

## 常見問題解答

### Q1：我可以在商業專案中使用Aspose.3D for Java嗎？

 A1：是的，Aspose.3D for Java 可以用於商業用途。有關許可詳細信息，請訪問[這裡](https://purchase.aspose.com/buy).

### Q2: 有免費試用嗎？

A2：是的，您可以探索 Aspose.3D for Java 的免費試用版[這裡](https://releases.aspose.com/).

### Q3：在哪裡可以找到 Aspose.3D for Java 的支援？

A3：Aspose.3D 社群論壇是個尋求支持和分享經驗的好地方。訪問論壇[這裡](https://forum.aspose.com/c/3d/18).

### Q4：測試需要臨時許可證嗎？

A4：是的，如果您需要臨時許可證用於測試目的，您可以獲得一個[這裡](https://purchase.aspose.com/temporary-license/).

### Q5：在哪裡可以找到文件？

A5：Aspose.3D for Java 的文件可用[這裡](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
