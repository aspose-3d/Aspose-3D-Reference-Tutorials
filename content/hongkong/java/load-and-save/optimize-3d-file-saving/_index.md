---
title: 使用 Aspose.3D SaveOptions 優化 Java 中的 3D 檔案保存
linktitle: 使用 Aspose.3D SaveOptions 優化 Java 中的 3D 檔案保存
second_title: Aspose.3D Java API
description: 了解如何使用 Aspose.3D SaveOptions 優化 Java 中的 3D 檔案保存。輕鬆增強效能並自訂輸出。
type: docs
weight: 16
url: /zh-hant/java/load-and-save/optimize-3d-file-saving/
---
## 介紹

Aspose.3D 是一個功能豐富的 Java 函式庫，可讓開發人員無縫地使用 3D 模型。在儲存 3D 檔案時，SaveOptions 類別提供了大量設定來根據您的要求微調輸出。在本教程中，我們將探討各種保存選項以及如何利用它們來優化流程。

## 先決條件

在我們深入學習本教程之前，請確保您具備以下先決條件：

-  Aspose.3D for Java：確保您已將 Aspose.3D 函式庫整合到您的 Java 專案中。你可以下載它[這裡](https://releases.aspose.com/3d/java/).

- Java 開發環境：在您的電腦上設定一個功能性的 Java 開發環境。

- 文件目錄：建立一個要儲存 3D 檔案的目錄，並記下其路徑以供以後使用。

## 導入包

在您的 Java 專案中，匯入使用 Aspose.3D 所需的套件。這包括`Scene`類和各種 SaveOptions 類。下面是一個基本範例：

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

現在，讓我們將每個範例分解為多個步驟來示範不同 SaveOptions 的用法。

## 第 1 步：在 GLTF SaveOption 中漂亮列印

這`prettyPrintInGltfSaveOption`方法可讓您產生具有縮排 JSON 內容的 GLTF 文件，以方便人類閱讀。

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    //初始化3D場景
    Scene scene = new Scene(new Sphere());
    
    //初始化 GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    //啟用漂亮的列印以獲得更好的可讀性
    opt.setPrettyPrint(true);
    
    //儲存 3D 場景
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## 第 2 步：HTML5 儲存選項

這`html5SaveOption`方法示範如何將 3D 場景儲存為 HTML5 文件，包括自訂選項。

```java
public static void html5SaveOption() throws IOException {
    //初始化場景
    Scene scene = new Scene();
    
    //建立一個帶有圓柱體的子節點
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //設定子節點的屬性
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    //在場景中添加燈光
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    //初始化 HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    //自訂選項（例如，關閉網格和使用者介面）
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    //將場景另存為 HTML5 文件
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

繼續對其他 SaveOptions 方法進行類似的細分，例如`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions`， 和`drcSaveOptions`.

## 結論

透過學習這個綜合教程，您已經了解如何使用 Aspose.3D SaveOptions 優化 Java 中的 3D 檔案保存。無論您是對漂亮列印的 GLTF 檔案感興趣還是對自訂 HTML5 輸出感興趣，Aspose.3D 都能為您提供增強 3D 圖形工作流程的工具。

## 常見問題解答

### Q1：如何將資源嵌入 glTF 檔案中？

 A1：要嵌入資產，請使用`setEmbedAssets(true)`方法中的`GltfSaveOptions`班級。

### Q2：這樣做的目的是什麼？`setPositionBits` method in `DracoSaveOptions`?

 A2: 的`setPositionBits`方法設定 Draco 壓縮演算法中位置的量化位。

### Q3：我可以匯出U3D檔案中的普通資料嗎？

 A3: 是的，您可以透過設定匯出正常數據`setExportNormals(true)`在裡面`U3dSaveOptions`班級。

### Q4：如何放棄 OBJ 匯出中儲存的材質檔案？

A4：利用`setFileSystem(new DummyFileSystem())`方法中的`ObjSaveOptions`類丟棄材質文件。

### Q5：有沒有辦法將依賴項儲存到 OBJ 檔案中的本機目錄？

 A5：是的，使用`setFileSystem(new LocalFileSystem(MyDir))`方法中的`ObjSaveOptions`類別在本地保存依賴項。