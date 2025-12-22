---
date: 2025-12-22
description: 學習如何在 Java 中使用 Aspose.3D 匯出場景至 glTF，同時將 3D 材質升級為 PBR，以提升真實感。
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: 使用 Aspose.3D 在 Java 中匯出場景為 glTF
url: /zh-hant/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Java 中使用 Aspose.3D 匯出場景為 glTF – 升級材質至 PBR

## 介紹

在本教學中，您將學會如何在 Java 中使用 Aspose.3D **匯出場景為 glTF**，同時將 3D 材質升級為 Physically‑Based Rendering（PBR）。升級至 PBR 能讓模型呈現更真實的外觀，而匯出為廣受支援的 glTF 2.0 格式則可讓您在各種引擎、瀏覽器以及 AR/VR 平台之間共享高品質資產。我們將逐步說明前置條件、匯入必要的套件，並一步步拆解每個範例，讓您能在自己的專案中套用此技術。

## 快速問答
- **「匯出場景為 glTF」是什麼意思？** 它會將 Aspose.3D 場景轉換為 glTF 2.0 檔案格式，保留幾何、材質與層級結構。  
- **為什麼要先升級材質為 PBR？** PBR 材質可直接對應到 glTF 的金屬度‑粗糙度工作流程，提供真實的光照效果，且不需額外的轉換步驟。  
- **執行程式碼需要授權嗎？** 開發階段可使用免費試用版；正式上線則需購買商業授權。  
- **支援哪些 Java IDE？** 任何能編譯 Java 的 IDE 都可（Eclipse、IntelliJ IDEA、VS Code 等）。  
- **可以匯出大型場景嗎？** 可以，Aspose.3D 會有效率地串流資料；只要確保有足夠的堆積記憶體即可處理非常大的模型。

## 什麼是「匯出場景為 glTF」？
將場景匯出為 glTF 意指將整個 3D 場景（包括網格、節點、相機、光源與材質）序列化為 GL Transmission Format（glTF）。glTF 是一種為即時渲染而優化的開放標準格式，非常適合用於網頁、行動裝置與遊戲引擎。

## 為什麼在匯出前先升級材質為 PBR？
PBR（Physically‑Based Rendering）材質使用反照率、金屬度與粗糙度等參數描述光線與表面的交互。glTF 2.0 原生支援 PBR，將 Phong 或自訂材質轉換為 PBR 後，可確保模型在任何支援 glTF 的檢視器中呈現正確的顏色、反射與陰影。

## 前置條件

在開始之前，請確保您已具備以下項目：

1. **Aspose.3D for Java** – 從 [release page](https://releases.aspose.com/3d/java/) 下載。  
2. **Java 開發環境** – JDK 8 或以上版本，並安裝您慣用的 IDE。  
3. **文件目錄** – 您電腦上用來讀寫 3D 檔案的資料夾。

## 匯入套件

將 Aspose.3D 的核心命名空間加入專案：

```java
import com.aspose.threed.*;
```

此單一匯入即可使用 `Scene`、`Box`、`PhongMaterial`、`PbrMaterial`、`GltfSaveOptions` 以及材質轉換 API。

## 步驟 1：初始化新的 3D 場景

建立一個全新的場景，用來容納您的幾何與材質：

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **小技巧：** 在開發期間將 `MyDir` 設為絕對路徑，可避免找不到檔案的錯誤。

## 步驟 2：建立使用 PhongMaterial 的盒子

我們先建立一個使用傳統 Phong 材質的簡易盒子，稍後在匯出時會將其轉換為 PBR 材質：

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **為什麼使用 Phong？** PhongMaterial 設定簡單，且能清楚展示轉換邏輯的運作方式。

## 步驟 3：以 GLTF 2.0 格式儲存（匯出場景為 glTF）

設定 GLTF 儲存選項，讓系統自動將任何 `PhongMaterial` 轉換為 `PbrMaterial`。這即是 **匯出場景為 glTF** 的核心：

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

執行此程式碼後，場景會寫入 `Non_PBRtoPBRMaterial_Out.gltf`。自訂的 `MaterialConverter` 會將 Phong 材質轉換為 PBR 材質，使最終的 glTF 檔案在任何 glTF 檢視器中都能呈現真實的陰影效果。

## 常見問題與解決方案

| 問題 | 解決方案 |
|-------|----------|
| **FileNotFoundException** 發生於儲存時 | 確認 `MyDir` 指向已存在的資料夾，且程式具有寫入權限。 |
| **ClassCastException** 發生於轉換器中 | 確認傳入轉換器的材質確實為 `PhongMaterial`。若混用材質類型，請加入 `instanceof` 檢查。 |
| **匯出後缺少貼圖** | glTF 需要將貼圖單獨提供；如有需要，請在轉換器中加入貼圖處理程式碼。 |

## 常見問答

**Q: Aspose.3D 是否支援除 Eclipse 之外的 Java 開發環境？**  
A: 支援，Aspose.3D 可在任何 Java IDE 中使用，包括 IntelliJ IDEA、NetBeans 與 VS Code。

**Q: 我可以將 Aspose.3D 用於商業專案嗎？**  
A: 可以，Aspose.3D 同時適用於個人與商業專案。詳情請參閱 [purchase page](https://purchase.aspose.com/buy) 的授權說明。

**Q: 有免費試用版嗎？**  
A: 有，您可前往 [here](https://releases.aspose.com/) 取得免費試用。

**Q: 哪裡可以取得 Aspose.3D 的支援？**  
A: 可前往 [Aspose.3D forum](https://forum.aspose.com/c/3d/18) 取得社群支援。

**Q: 如何取得 Aspose.3D 的臨時授權？**  
A: 請造訪 [this link](https://purchase.aspose.com/temporary-license/) 了解臨時授權資訊。

## 結論

依照上述步驟，您現在已掌握如何在 Java 中使用 Aspose.3D **匯出場景為 glTF**，同時自動將 Phong 材質升級為 PBR。此工作流程讓您能建立高品質、基於物理的資產，適用於現代渲染管線、網頁檢視器以及 AR/VR 體驗。您可以嘗試更複雜的幾何、貼圖與光源設定，充分發揮 PBR 與 glTF 的威力。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2025-12-22  
**測試環境：** Aspose.3D 24.12 for Java  
**作者：** Aspose  

---