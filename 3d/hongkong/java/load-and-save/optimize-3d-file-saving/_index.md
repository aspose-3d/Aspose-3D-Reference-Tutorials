---
date: 2025-12-21
description: 學習如何在 Java 中使用 Aspose.3D SaveOptions 保存 3D 檔案 – 優化效能、啟用美化列印、客製化 HTML5
  輸出等。
linktitle: Save 3D File Java – Optimize 3D Saving with Aspose.3D SaveOptions
second_title: Aspose.3D Java API
title: 儲存 3D 檔案 Java – 使用 Aspose.3D SaveOptions 優化 3D 儲存
url: /zh-hant/java/load-and-save/optimize-3d-file-saving/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 保存 3D 檔案 Java – 使用 Aspose.3D SaveOptions 優化 3D 儲存

## 介紹

如果您需要快速且高效地 **save 3d file java** 專案，Aspose.3D for Java 提供了一套強大的選項讓您微調輸出。本文將逐步說明最實用的 `SaveOptions` 設定、如何提升效能，並示範實務情境，例如美化 GLTF 檔案或產生自包含的 HTML5 觀賞器。

## 快速回答
- **主要的儲存類別是什麼？** `Scene.save()` 搭配特定的 `*SaveOptions` 子類別。  
- **哪個選項可以讓 GLTF 檔案易於閱讀？** `GltfSaveOptions.setPrettyPrint(true)`。  
- **我可以在 GLTF 匯出時嵌入資產嗎？** 可以 – 使用 `GltfSaveOptions.setEmbedAssets(true)`。  
- **如何關閉 HTML5 匯出的 UI？** 設定 `Html5SaveOptions.setShowUI(false)`。  
- **正式環境需要授權嗎？** 商業授權是非評估使用的必要條件。

## 前置條件

在開始教學前，請先確保具備以下前置條件：

- Aspose.3D for Java：確保已將 Aspose.3D 套件整合至您的 Java 專案。您可以在此處下載 [here](https://releases.aspose.com/3d/java/)。  
- Java 開發環境：在您的機器上已安裝可正常運作的 Java 開發環境。  
- 文件目錄：建立一個用來儲存 3D 檔案的資料夾，並記下其路徑以備後續使用。

## 匯入套件

在您的 Java 專案中，匯入使用 Aspose.3D 所需的套件。這包括 `Scene` 類別以及各種 `SaveOptions` 類別。以下為基本範例：

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## 如何使用 Aspose.3D SaveOptions 儲存 3D 檔案 Java

以下將說明最常見的 `SaveOptions` 設定。每段程式碼後皆附有簡短說明，讓您了解 **為何** 需要此設定。

### 步驟 1：GLTF SaveOption 的美化輸出

`prettyPrintInGltfSaveOption` 方法可產生帶有縮排 JSON 內容的 GLTF 檔案，方便人工閱讀。

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Initialize 3D scene
    Scene scene = new Scene(new Sphere());
    
    // Initialize GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Enable pretty print for better readability
    opt.setPrettyPrint(true);
    
    // Save 3D Scene
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

### 步驟 2：HTML5 SaveOption

`html5SaveOption` 方法示範如何將 3D 場景儲存為 HTML5 檔案，並提供自訂選項。

```java
public static void html5SaveOption() throws IOException {
    // Initialize a scene
    Scene scene = new Scene();
    
    // Create a child node with a cylinder
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    // Set properties for the child node
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Add a light to the scene
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Initialize HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Customize options (e.g., turn off grid and user interface)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Save the scene as an HTML5 file
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

接下來以相同方式說明其他 `SaveOptions` 方法，例如 `colladaSaveOption`、`discreet3DSSaveOption`、`fbxSaveOption`、`objSaveOption`、`STLSaveOption`、`U3DSaveOption`、`glTFSaveOptions` 與 `drcSaveOptions`。每個範例皆遵循相同模式：建立場景、設定對應的 `*SaveOptions` 物件，最後呼叫 `scene.save()`。

## 常見陷阱與技巧

- **嵌入資產** – 需要單一自包含檔案時，務必在 `GltfSaveOptions` 上呼叫 `setEmbedAssets(true)`。  
- **效能** – 大型場景建議先降低網格複雜度或使用 Draco 壓縮 (`DracoSaveOptions`) 後再儲存。  
- **檔案系統處理** – 匯出 OBJ 時，可透過 `setFileSystem(new DummyFileSystem())` 控制材質檔案的產生，避免產生不必要的副檔案。  
- **UI 元素** – HTML5 匯出預設會帶有 UI，使用 `setShowUI(false)` 可產生純淨的觀賞器。

## 結論

透過本完整教學，您已學會如何使用 Aspose.3D 的 `SaveOptions` 高效地 **save 3d file java**。無論是需要美化的 GLTF、輕量的 HTML5 觀賞器，或是高度壓縮的 Draco 輸出，這些選項都能讓您全方位掌控 3D 圖形工作流程。

## 常見問答

### Q1: 如何在 glTF 檔案中嵌入資產？

A1: 在 `GltfSaveOptions` 類別中使用 `setEmbedAssets(true)` 方法即可。

### Q2: `DracoSaveOptions` 中的 `setPositionBits` 方法有何用途？

A2: `setPositionBits` 用於設定 Draco 壓縮演算法中位置座標的量化位元數。

### Q3: 能否在 U3D 檔案中匯出法線資料？

A3: 可以，於 `U3dSaveOptions` 類別中設定 `setExportNormals(true)` 即可。

### Q4: 如何在 OBJ 匯出時避免產生材質檔案？

A4: 在 `ObjSaveOptions` 類別中使用 `setFileSystem(new DummyFileSystem())` 方法即可捨棄材質檔案。

### Q5: 有沒有辦法將 OBJ 的相依檔案儲存至本機目錄？

A5: 可以，於 `ObjSaveOptions` 中使用 `setFileSystem(new LocalFileSystem(MyDir))` 方法將相依檔案儲存至本機目錄。

## Frequently Asked Questions

**Q: 可以在無頭（headless）伺服器環境使用這些 SaveOptions 嗎？**  
A: 當然可以。所有 `SaveOptions` 都不依賴 UI，適合後端處理流程。

**Q: Aspose.3D 是否支援儲存為新版 glTF 2.0 規格？**  
A: 支援。使用 `GltfSaveOptions(FileFormat.GLTF2)` 即可針對 glTF 2.0 格式。

**Q: 如何在匯出 OBJ 時控制細節層級？**  
A: 可在儲存前先簡化網格，或使用 `ObjSaveOptions` 調整頂點精度。

**Q: 有沒有方法在不寫入磁碟的情況下預覽儲存的檔案？**  
A: 可以將內容儲存至 `ByteArrayOutputStream`，再將位元串流傳送至檢視器或客戶端。

**Q: 正式環境使用需要什麼授權？**  
A: 任何非評估用途皆需商業 Aspose.3D 授權。

---

**最後更新：** 2025-12-21  
**測試環境：** Aspose.3D for Java 24.12（撰寫時最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}