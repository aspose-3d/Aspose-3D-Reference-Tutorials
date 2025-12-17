---
date: 2025-12-17
description: 學習如何使用 Aspose.3D for Java 以線性擠出扭轉方式建立扭曲的 3D 模型，並匯出 OBJ 檔案。請參考我們的逐步教學。
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 建立扭曲的 3D 模型 – 使用 Aspose.3D for Java 在線性擠出中套用扭轉
url: /zh-hant/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Java 中使用 Aspose.3D 進行線性擠出扭轉

## 介紹

歡迎閱讀本步驟教學，說明如何透過 Aspose.3D for Java 在進行線性擠出時加入扭轉，以 **建立扭曲的 3D 模型**。無論您是製作建築視覺化、遊戲資產或工程原型，僅需幾行程式碼即可為幾何體增添動態的螺旋效果。

## 快速解答
- **「扭轉」在擠出時是什麼意思？** 它會在形狀延伸的同時，使輪廓繞擠出軸旋轉。  
- **哪個 API 類別負責扭轉？** `LinearExtrusion` 提供 `setTwist` 方法。  
- **執行範例是否需要授權？** 評估可使用免費試用版；正式上線需購買商業授權。  
- **可以將結果匯出為 OBJ 嗎？** 可以，使用 `scene.save(..., FileFormat.WAVEFRONTOBJ)`。  
- **需要哪個 Java 版本？** 完全支援 Java 8 及以上版本。

## 前置條件

在開始教學之前，請確保已具備以下條件：

- Java 開發環境：請確認系統已安裝 Java。  
- Aspose.3D 套件：從 [download link](https://releases.aspose.com/3d/java/) 下載並安裝 Aspose.3D for Java。  
- 文件說明：參考 [Aspose.3D documentation](https://reference.aspose.com/3d/java/) 取得完整指引。

## 匯入套件

在開始編寫程式碼之前，先將必要的套件匯入您的 Java 專案。以下為範例：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 設定文件目錄

首先，定義產生的 3D 檔案要儲存的位置。

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## 初始化基礎輪廓

接著，建立將要被擠出的形狀。本例使用帶有小圓角半徑的矩形。

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## 建立場景

`Scene` 物件充當所有 3D 節點的容器。

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## 建立節點

向場景中加入兩個子節點——一個保持直線，另一個將接受扭轉。

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## 線性擠出扭轉

現在對兩個節點執行 **linear extrusion twist**。左側節點使用 0° 扭轉（保持直線），右側節點使用 90° 扭轉，產生螺旋形狀。我們同時設定切片數量，以確保幾何體平滑。

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## 匯出 OBJ 檔案（Java）

最後，將場景儲存為廣受支援的 OBJ 格式。此步驟示範了 Aspose.3D 的 **export OBJ file Java** 功能。

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## 為何重要

建立扭曲的 3D 模型可在不依賴外部建模工具的情況下，產生強大的視覺效果。特別適用於：

- **機械零件** 需要螺旋特徵（例如彈簧、螺絲）。  
- **藝術設計** 中，細微的螺旋可增添視覺趣味。  
- **遊戲資產** 受惠於低多邊形、程序化產生的幾何體。

## 常見問題與技巧

| 問題 | 解決方案 |
|------|----------|
| 扭轉顯示平坦或缺失 | 確認 `setSlices` 設定足夠高（例如 100），以取得平滑旋轉。 |
| OBJ 檔案無法在檢視器開啟 | 檢查輸出路徑 (`MyDir`) 是否正確，且檔案具有寫入權限。 |
| 出現意外的縮放 | 檢查來源輪廓的單位系統；Aspose.3D 預設使用公尺。 |

## 常見問答

**Q: 我可以使用 Aspose.3D for Java 處理其他 3D 檔案格式嗎？**  
A: 可以，Aspose.3D 支援多種格式，如 FBX、STL、3MF 等。

**Q: 在哪裡可以取得 Aspose.3D for Java 的支援？**  
A: 前往 [Aspose.3D forum](https://forum.aspose.com/c/3d/18) 取得社群協助與官方支援。

**Q: 有免費試用版嗎？**  
A: 有，您可從 [here](https://releases.aspose.com/) 下載試用版本。

**Q: 如何取得測試用的臨時授權？**  
A: 前往 [temporary license page](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

**Q: 哪裡可以購買完整授權？**  
A: 請至 [buying page](https://purchase.aspose.com/buy) 購買 Aspose.3D for Java。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2025-12-17  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

---