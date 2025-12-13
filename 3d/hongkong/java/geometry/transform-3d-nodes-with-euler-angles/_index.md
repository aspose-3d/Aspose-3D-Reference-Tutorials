---
date: 2025-12-13
description: 學習如何使用 Aspose 3D Java 轉換 3D 節點。本指南示範如何使用歐拉角、加入 3D 旋轉以及設定平移（Java）。
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – 使用歐拉角轉換 3D 節點
url: /zh-hant/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D 在 Java 中以歐拉角轉換 3D 節點

## 簡介

在本教學中，您將會了解 **如何使用 aspose 3d java** 透過歐拉角來轉換 3D 節點。完成本指南後，您將能夠加入 3D 旋轉、設定 translation java，並建立可即時回應資料的動態場景。

## 快速回答
- **哪個函式庫負責 Java 中的 3D 變換？** Aspose 3D for Java。  
- **哪個方法使用歐拉角設定旋轉？** `setEulerAngles()` 於節點的 transform。  
- **如何在空間中移動節點？** 使用 `setTranslation()` 搭配 `Vector3`。  
- **生產環境是否需要授權？** 需要，必須購買商業版 Aspose 3D 授權。  
- **可以匯出為 FBX 嗎？** 當然可以 – `scene.save(..., FileFormat.FBX7500ASCII)` 直接支援。

## 先決條件

在開始教學之前，請確保您已具備以下條件：

- 基本的 Java 程式設計知識。  
- 已在電腦上安裝 Java Development Kit (JDK)。  
- Aspose.3D 函式庫，可從 [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/) 取得。

## 匯入套件

先將必要的套件匯入您的 Java 專案。請確保已正確將 Aspose.3D 函式庫加入 classpath。若尚未下載，可在此取得下載連結 [here](https://releases.aspose.com/3d/java/)。

```java
import com.aspose.threed.*;
```

## aspose 3d java – 使用歐拉角

### 步驟 1. 初始化場景與節點

首先，建立一個場景與一個將承載您欲轉換之幾何體的節點。

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### 步驟 2. 建立 Mesh 並設定幾何體

接著，產生一個簡單的 mesh（此例為立方體），並將其附加至節點上。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## 為節點新增 3D 旋轉

### 步驟 3. 設定歐拉角與平移

現在，我們使用歐拉角套用旋轉，同時將節點移動至可見位置。

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## 設定 Translation Java – 定位節點

上述平移步驟示範了 **set translation java** 的實作：節點沿 Z 軸平移 20 單位，以便在渲染後能看見它。

## 步驟 4. 將節點加入場景

將已轉換的節點附加至場景的根節點。

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## 步驟 5. 儲存 3D 場景

最後，將場景匯出為 FBX 檔（或其他支援的格式）。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

請務必將 `"Your Document Directory"` 替換為您機器上相應的路徑。

## 結論

恭喜！您已成功使用 **aspose 3d java** 於 Java 中以歐拉角轉換 3D 節點。可嘗試不同的角度與平移，打造動態且具吸引力的 3D 場景。

## 常見問題

### Q1: 可以在商業專案中使用 Aspose.3D for Java 嗎？

A1: 可以。請前往 [purchase page](https://purchase.aspose.com/buy) 了解授權細節。

### Q2: 哪裡可以取得 Aspose.3D 的支援？

A2: 請至 [Aspose.3D forum](https://forum.aspose.com/c/3d/18) 尋求協助並與社群交流。

### Q3: 有免費試用版嗎？

A3: 有，您可前往 [free trial](https://releases.aspose.com/) 體驗 Aspose.3D 的功能。

### Q4: 如何取得臨時授權？

A4: 可在此取得臨時授權 [here](https://purchase.aspose.com/temporary-license/)。

### Q5: 哪裡可以找到文件說明？

A5: 請參考 [documentation](https://reference.aspose.com/3d/java/) 獲得完整使用指南。

## 常見問答

**Q: Euler 角與四元數旋轉有何差異？**  
A: Euler 角直觀（俯仰、偏航、滾轉），但可能遭遇萬向鎖；四元數則避免此問題，且更適合平滑插值。

**Q: 可以在同一節點上串接多個變換嗎？**  
A: 可以。依序呼叫 `setEulerAngles`、`setTranslation`、`setScale`，函式庫會將它們合成為單一變換矩陣。

**Q: 能否匯出為 OBJ 或 STL 等其他格式？**  
A: 完全可以。只要在 `scene.save` 呼叫中將 `FileFormat.FBX7500ASCII` 改為 `FileFormat.OBJ` 或 `FileFormat.STL` 即可。

**Q: 如何一次對多個節點套用相同的旋轉？**  
A: 建立一個父節點，將旋轉套用於父節點，然後將子節點加入其下，所有子節點皆會繼承此變換。

**Q: 儲存後需要呼叫清理方法嗎？**  
A: Java 的垃圾回收機制會處理大部分資源，但若在長時間執行的應用程式中處理大型場景，可明確呼叫 `scene.dispose()` 釋放資源。

---

**最後更新日期：** 2025-12-13  
**測試環境：** Aspose.3D 23.12 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}