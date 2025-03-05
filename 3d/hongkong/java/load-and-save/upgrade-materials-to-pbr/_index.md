---
title: 使用 Aspose.3D 將 3D 材質升級為 PBR，以增強 Java 中的真實感
linktitle: 使用 Aspose.3D 將 3D 材質升級為 PBR，以增強 Java 中的真實感
second_title: Aspose.3D Java API
description: 使用 Aspose.3D 在 Java 中輕鬆將 3D 材質升級為 PBR。增強真實感，呈現迷人的視覺效果。
type: docs
weight: 13
url: /zh-hant/java/load-and-save/upgrade-materials-to-pbr/
---
## 介紹

將 3D 材質升級到 PBR 是在 Java 應用程式中實現逼真視覺效果的變革性一步。 Aspose.3D 簡化了這個過程，讓您可以從傳統材質無縫過渡到 PBR 材質。在本教程中，我們將探討必要的先決條件、導入包，並將每個範例分解為詳細的步驟。

## 先決條件

在深入學習本教程之前，請確保您具備以下先決條件：

1.  Aspose.3D for Java：從下列位置下載並安裝 Aspose.3D 函式庫：[發布頁面](https://releases.aspose.com/3d/java/).

2. Java 開發環境：確保您的電腦上設定了 Java 開發環境。

3. 文件目錄：為您的 3D 文件建立專用目錄。

## 導入包

若要開始升級過程，請將所需的套件匯入您的 Java 專案。使用以下程式碼片段作為指導：

```java
import com.aspose.threed.*;
```

確保包含所有必需的 Aspose.3D 套件以無縫地利用其功能。

## 第 1 步：初始化新的 3D 場景

首先使用以下程式碼初始化一個新的 3D 場景：

```java
// ExStart:初始化場景
String MyDir = "Your Document Directory";
Scene s = new Scene();
//擴充結束：初始化場景
```

## 第 2 步：使用 PhongMaterial 建立一個盒子

建立一個 3D 框並為其指定 PhongMaterial：

```java
// ExStart：CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd：CreateBoxWithMaterial
```

## 步驟 3：儲存為 GLTF 2.0 格式

將場景儲存為 GLTF 2.0 格式，在此過程中將 PhongMaterial 轉換為 PBRMaterial：

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

嚴格按照這些步驟將 3D 材質無縫升級到 PBR，從而增強 Java 應用程式的真實感。

## 結論

總而言之，Aspose.3D for Java 使您能夠透過將材質升級為 PBR 來提升 3D 圖形的視覺吸引力。採用這項技術可以增強真實感，並透過視覺上令人驚嘆的 Java 應用程式吸引您的觀眾。

## 常見問題解答

### Q1：Aspose.3D是否相容於Eclipse以外的Java開發環境？

A1：是的，Aspose.3D相容於各種Java開發環境。

### Q2：我可以將Aspose.3D用於商業項目嗎？

 A2：是的，您可以將 Aspose.3D 用於個人和商業專案。參觀[購買頁面](https://purchase.aspose.com/buy)了解許可詳細資訊。

### Q3：有免費試用嗎？

A3：是的，您可以免費試用[這裡](https://releases.aspose.com/).

### Q4：哪裡可以找到對 Aspose.3D 的支援？

A4：探索[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持。

### Q5：如何取得Aspose.3D的臨時授權？

 A5：參觀[這個連結](https://purchase.aspose.com/temporary-license/)取得臨時許可證資訊。