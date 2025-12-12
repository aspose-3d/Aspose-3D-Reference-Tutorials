---
date: 2025-12-12
description: 學習如何在共享網格幾何資料的同時設定材質顏色，並使用 Aspose.3D 在 Java 3D 中將場景另存為 FBX。
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: 在 Java 3D 中使用 Aspose.3D 設定材質顏色與共享網格幾何資料
url: /zh-hant/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 設定材質顏色並在 Java 3D 中共享網格幾何資料，使用 Aspose.3D

## 介紹

踏入使用 Aspose.3D 的 Java 3D 世界，您將開啟創建驚豔視覺化與沉浸式體驗的無限可能。在本教學中，我們將指導您 **如何在 Java 3D 中共享網格** 幾何資料，並示範 **如何為每個網格實例設定材質顏色**。請仔細遵循每一步，完成後您將能在多個節點之間無縫交換網格資料，同時控制顏色並匯出為 FBX。

## 快速答覆
- **主要目標是什麼？** 為每個節點設定材質顏色並共享網格幾何資料。  
- **需要哪個函式庫？** Aspose.3D for Java。  
- **如何匯出結果？** 將場景儲存為 FBX 檔案（FBX7400ASCII）。  
- **是否需要授權？** 生產環境需使用臨時或正式授權。  
- **支援哪個 Java 版本？** 任意 Java 8 以上環境。

## 前置條件

在開始教學之前，請確保您已具備以下前置條件：

- Java 開發環境：確保系統已設定 Java 開發環境。  
- Aspose.3D 函式庫：下載並安裝 Aspose.3D 函式庫。您可以在[此處](https://releases.aspose.com/3d/java/)取得。

## 匯入套件

首先在 Java 專案中匯入必要的套件。此步驟對於存取 Aspose.3D 函式庫提供的功能至關重要。

```java
import com.aspose.threed.*;
```

## 步驟 1：初始化 Scene 物件（initialize scene java）

讓我們從初始化 Scene 物件開始。此物件將作為我們 3D 魔法展開的畫布。

```java
// Initialize scene object
Scene scene = new Scene();
```

## 步驟 2：定義顏色向量

在此步驟中，我們定義一組顏色向量陣列，將套用於 3D 場景的不同元素。

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## 步驟 3：使用 Polygon Builder 建立 3D Mesh（create 3d mesh java）

使用 Common 類別透過 polygon builder 方法建立 Mesh。此 Mesh 將作為我們 3D 元素的基礎。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## 如何為每個節點設定材質顏色？

遍歷顏色向量，建立立方體節點，並設定屬性，如材質、**設定材質顏色**以及平移。這是控制每個 Mesh 實例視覺外觀的核心。

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## 步驟 5：儲存 3D 場景（save scene fbx, convert mesh to fbx）

指定目錄與檔名，以支援的檔案格式（此例為 FBX7400ASCII）儲存 3D 場景。此步驟亦示範 **將 Mesh 轉換為 FBX**。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## 結論

恭喜！您已成功 **設定材質顏色**、在多個節點之間共享網格幾何資料，並使用 Aspose.3D for Java 將結果匯出為 FBX 檔案。這為創建視覺驚豔且具互動性的 3D 應用程式開啟了無限可能。

## 常見問題

### Q1：我可以將 Aspose.3D 與其他 Java 框架一起使用嗎？

A1：可以，Aspose.3D 設計上能與各種 Java 框架無縫協作。

### Q2：Aspose.3D 有哪些授權方案可供選擇？

A2：有，您可在[此處](https://purchase.aspose.com/buy)了解授權方案。

### Q3：如何取得 Aspose.3D 的支援？

A3：請前往 Aspose.3D [論壇](https://forum.aspose.com/c/3d/18)取得支援與討論。

### Q4：是否提供免費試用？

A4：有，您可在[此處](https://releases.aspose.com/)取得免費試用。

### Q5：如何取得 Aspose.3D 的臨時授權？

A5：您可在[此處](https://purchase.aspose.com/temporary-license/)取得臨時授權。

## 其他常見問題

**問：我可以將場景匯出為除 FBX 之外的其他格式嗎？**  
答：可以，Aspose.3D 支援 OBJ、STL、3MF 等格式。只需在 `save` 呼叫中更改 `FileFormat` 列舉即可。

**問：如果場景建立後需要變更材質該怎麼辦？**  
答：取得節點，修改其 `LambertMaterial`（例如 `setDiffuseColor`），然後重新儲存場景。

**問：此函式庫能有效處理大型 Mesh 嗎？**  
答：Aspose.3D 使用最佳化資料結構；但對於極大型 Mesh，建議使用串流或將場景拆分。

**問：有沒有方法為顏色變化加入動畫？**  
答：可以，使用 `AnimationController` API 為材質屬性加入動畫。

---

**最後更新：** 2025-12-12  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}