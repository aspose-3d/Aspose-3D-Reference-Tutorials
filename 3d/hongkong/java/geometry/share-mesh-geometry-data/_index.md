---
date: 2026-02-17
description: 學習如何在 Java 3D 中使用 Aspose.3D 將網格轉換為 FBX，同時設定材質顏色並共享網格幾何資料。
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: 將網格轉換為 FBX 並在 Java 3D 中設定材質顏色
url: /zh-hant/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 將 Mesh 轉換為 FBX 並在 Java 3D 中設定材質顏色

## 簡介

如果你正在開發基於 Java 的 3D 應用程式，通常需要在多個物件之間重複使用相同的幾何體，同時為每個實例賦予獨特的外觀。在本教學中，你將學會 **如何將 mesh 轉換為 FBX**、在多個節點之間共享底層 mesh 幾何，並 **為每個節點設定不同的材質顏色**。完成後，你將擁有一個可直接匯出的 FBX 場景，能夠放入任何引擎或檢視器中使用。

## 快速答覆
- **主要目標是什麼？** 將 mesh 轉換為 FBX、共享 mesh 幾何，並為每個節點設定不同的材質顏色。  
- **需要哪個函式庫？** Aspose.3D for Java。  
- **如何匯出結果？** 使用 `FileFormat.FBX7400ASCII` 將場景儲存為 FBX 檔案。  
- **是否需要授權？** 生產環境需要臨時或完整授權。  
- **支援哪個 Java 版本？** 任意 Java 8 以上環境。

## 什麼是 **convert mesh to FBX**？

`convert mesh to fbx` 是指將在記憶體中建立或操作的 mesh 物件寫入 FBX 檔案格式的過程。FBX 被 Maya、Blender、Unity 等多種 3D 工具廣泛支援。Aspose.3D 會處理繁重的工作，你只需要呼叫 `scene.save(...)` 並指定正確的 `FileFormat` 即可。

## 為什麼要共享 mesh 幾何資料？

共享幾何可以減少記憶體使用量並加速渲染，因為底層的頂點緩衝區只會儲存一次。此技巧特別適用於包含大量重複物件的場景——例如森林、人群或模組化建築——每個實例僅在變換或材質上有所不同。

## 先決條件

在開始教學之前，請確保已具備以下條件：

- **Java 開發環境** – 任意 IDE 或指令列設定，需支援 Java 8 或更新版本。  
- **Aspose.3D 函式庫** – 從官方網站下載最新 JAR：[here](https://releases.aspose.com/3d/java/)。

## 匯入套件

開始之前先將必要的套件匯入你的 Java 專案。此步驟是存取 Aspose.3D 功能的前提。

```java
import com.aspose.threed.*;
```

## 步驟 1：初始化 Scene 物件（initialize scene java）

先建立一個 Scene 物件，作為我們 3D 魔法展開的畫布。

```java
// Initialize scene object
Scene scene = new Scene();
```

## 步驟 2：定義顏色向量

在此步驟中，我們定義一組顏色向量，稍後會套用到場景中的不同元素上。

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## 步驟 3：使用 Polygon Builder 建立 3D Mesh（create 3d mesh java）

利用 Common 類別的 polygon builder 方法建立 mesh，作為 3D 元素的基礎。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## 如何為每個節點設定材質顏色？

遍歷顏色向量，建立立方體節點，並設定材質、**設定材質顏色**以及平移。這是控制每個 mesh 實例外觀的核心。

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

指定目錄與檔名，將 3D 場景以支援的檔案格式（此處為 FBX7400ASCII）儲存。此步驟同時示範 **convert mesh to FBX**。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## 常見陷阱與技巧

- **路徑問題** – 確保目錄路徑在加入檔名之前以檔案分隔符 (`/` 或 `\\`) 結尾。  
- **授權初始化** – 若在呼叫 `scene.save` 前未設定 Aspose.3D 授權，函式庫將以試用模式運作，可能會嵌入浮水印。  
- **材質覆寫** – 多個節點重複使用相同的 `LambertMaterial` 實例會導致所有節點共用同一顏色。請如上例在每次迭代時建立全新的材質。  
- **大型 Mesh** – 若 Mesh 含有數百萬個頂點，建議使用帶索引多邊形的 `MeshBuilder`，以控制 FBX 檔案大小。

## 其他常見問答

**Q1: 我可以在其他 Java 框架中使用 Aspose.3D 嗎？**  
A1: 可以，Aspose.3D 設計上能與各種 Java 框架無縫整合。

**Q2: Aspose.3D 有哪些授權方案可供選擇？**  
A2: 您可以在此處探索授權方案：[here](https://purchase.aspose.com/buy)。

**Q3: 如何取得 Aspose.3D 的技術支援？**  
A3: 請前往 Aspose.3D [forum](https://forum.aspose.com/c/3d/18) 取得支援與討論。

**Q4: 是否提供免費試用？**  
A4: 有，您可以在此取得免費試用：[here](https://releases.aspose.com/)。

**Q5: 如何取得 Aspose.3D 的臨時授權？**  
A5: 您可以在此取得臨時授權：[here](https://purchase.aspose.com/temporary-license/)。

## 結論

恭喜！你已成功 **將 mesh 轉換為 FBX**、在多個節點之間共享 mesh 幾何資料，並使用 Aspose.3D for Java 為每個節點設定個別的材質顏色。此工作流程為你提供輕量且可重用的 mesh 架構，能夠匯出至任何支援 FBX 的管線。

---

**Last Updated:** 2026-02-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}