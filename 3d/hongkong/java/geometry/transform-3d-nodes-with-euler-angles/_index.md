---
date: 2026-02-20
description: 學習如何使用 Aspose Java 建立網格，並使用歐拉角轉換 3D 節點、加入 3D 旋轉以及設定 Java 平移。
linktitle: Create Mesh Aspose Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: 建立 Mesh Aspose Java – 以歐拉角轉換 3D 節點
url: /zh-hant/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D 於 Java 中以歐拉角轉換 3D 節點

## 簡介

在本教學中，你將學習如何 **create mesh aspose java** 並透過套用歐拉角來轉換 3D 節點。完成本指南後，你將能夠加入 3D 旋轉、設定 translation java，並建立能即時回應資料的動態場景。

## 快速解答
- **什麼程式庫負責 Java 中的 3D 變換？** Aspose 3D for Java。  
- **哪個方法使用歐拉角設定旋轉？** `setEulerAngles()` 於節點的 transform。  
- **如何在空間中移動節點？** 使用帶有 `Vector3` 的 `setTranslation()`。  
- **生產環境是否需要授權？** 是，需要商業版 Aspose 3D 授權。  
- **可以匯出為 FBX 嗎？** 當然可以 – `scene.save(..., FileFormat.FBX7500ASCII)` 直接可用。

## 先決條件

在深入教學之前，請確保已具備以下先決條件：

- 具備 Java 程式設計的基本知識。  
- 在你的機器上已安裝 Java Development Kit (JDK)。  
- Aspose.3D 程式庫，可從 [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/) 取得。

## 匯入套件

先將必要的套件匯入你的 Java 專案。確保 Aspose.3D 程式庫已正確加入 classpath。若尚未下載，可在此取得下載連結 [here](https://releases.aspose.com/3d/java/)。

```java
import com.aspose.threed.*;
```

## 建立 Mesh Aspose Java

任何 3D 工作流程的第一步都是 **create mesh aspose java** —— 即建立稍後將被轉換的幾何資料。在本範例中，我們將使用 Aspose 的輔助方法產生一個簡單的立方體 Mesh，並將其附加到節點上。

### aspose 3d java – 使用歐拉角

#### 步驟 1. 初始化 Scene 與 Node

首先，建立一個 scene 與一個將容納欲轉換幾何體的 node。

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

#### 步驟 2. 建立 Mesh 並設定 Geometry

接著，產生一個簡單的 Mesh（此例為立方體），並將其附加到 node。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## 為節點加入 3D 旋轉

#### 步驟 3. 設定 Euler Angles 與 Translation

現在，我們使用歐拉角套用旋轉，同時將節點移動到可見位置。

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## 設定 Translation Java – 定位節點

上述的 translation 步驟示範了 **set translation java** 的實作：節點沿 Z 軸平移 20 單位，以便在渲染後能看見它。

## 步驟 4. 將節點加入 Scene

將已轉換的節點附加到 scene 的根節點。

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## 步驟 5. 儲存 3D Scene

最後，將 scene 匯出為 FBX 檔（或任何其他支援的格式）。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

請務必將 `"Your Document Directory"` 替換為你機器上相應的路徑。

## 為何使用 Euler Angles 搭配 Aspose 3D？

Euler Angles 提供直觀的旋轉概念——俯仰、偏航與滾轉——非常適合快速原型開發或需要向最終使用者提供旋轉控制的情境。Aspose 3D 會抽象底層矩陣運算，讓你專注於視覺結果，而非數學細節。

## 常見使用情境

- **即時資料視覺化：** 根據感測器輸入旋轉模型。  
- **遊戲式相機裝置：** 套用 yaw‑pitch‑roll 以模擬相機。  
- **產品配置器：** 讓客戶使用簡單滑桿旋轉 3D 產品模型。

## 故障排除與技巧

- **萬向節鎖死：** 若旋轉時出現意外卡頓，請考慮改用基於四元數的旋轉 (`setRotationQuaternion()`)。  
- **單位一致性：** Aspose 3D 使用你提供的相同單位；請確保 translation 數值與模型比例一致。  
- **效能：** 對於大型場景，儲存後呼叫 `scene.dispose()` 以釋放本機資源。

## 常見問答

**Q: Euler Angles 與 quaternion rotation 有何差異？**  
A: Euler Angles 直觀（俯仰、偏航、滾轉），但可能遭遇萬向節鎖死；四元數則避免此問題，且更適合平滑插值。

**Q: 可以在同一節點上串接多個變換嗎？**  
A: 可以。依任意順序呼叫 `setEulerAngles`、`setTranslation` 與 `setScale`；程式庫會將它們合成為單一變換矩陣。

**Q: 能否匯出為 OBJ 或 STL 等其他格式？**  
A: 完全可以。只需在 `scene.save` 呼叫中將 `FileFormat.FBX7500ASCII` 替換為 `FileFormat.OBJ` 或 `FileFormat.STL`。

**Q: 如何一次對多個節點套用相同的旋轉？**  
A: 建立一個父節點，將旋轉套用於父節點，然後將子節點加入其下。所有子節點皆會繼承此變換。

**Q: 儲存後需要呼叫任何清理方法嗎？**  
A: Java 的垃圾回收器會處理大部分資源，但若在長時間執行的應用程式中處理大型場景，建議明確呼叫 `scene.dispose()`。

## 結論

恭喜！你已成功 **created mesh aspose java**，並使用 Aspose 3D 在 Java 中以歐拉角轉換 3D 節點。可嘗試不同的角度、平移，甚至四元數旋轉，打造動態且引人入勝的 3D 體驗。

---

**最後更新：** 2026-02-20  
**測試環境：** Aspose.3D 23.12 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}