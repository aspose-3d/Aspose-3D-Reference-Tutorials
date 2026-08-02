---
date: 2026-08-02
description: 了解如何在線性擠出中更改擠出方向，並使用 Aspose.3D for Java 匯出 OBJ 檔案。請依照我們的逐步指南操作。
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: 更改擠出方向 – Aspose.3D Java
og_description: 使用 Aspose.3D for Java 在線性擠出中更改擠出方向並匯出 OBJ 檔案。本指南提供逐步程式碼示例與開發人員提示。
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: 更改擠出方向 – Aspose.3D Java 教程
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: 更改擠出方向 – 3D 模型 – Aspose.3D Java
url: /zh-hant/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 更改 3D 模型的擠出方向 – Aspose.3D Java

## 介紹

在本完整教學中，您將學會 **如何更改擠出方向**，在使用 Aspose.3D for Java 進行線性擠出時。無論您是在打造類 CAD 工具、為遊戲引擎準備資產，或是產生 3‑D 列印零件，控制擠出方向都能讓您精確打造所需形狀。我們將逐步說明，從初始化輪廓到將結果儲存為 OBJ 檔案，讓您也能 **匯出 3D 模型 OBJ** 檔案直接從 Java 執行。

## 快速解答
- **哪個類別執行線性擠出？** `LinearExtrusion`
- **哪個方法設定擠出向量？** `setDirection(Vector3 direction)`
- **結果可以儲存為 OBJ 嗎？** 可以——使用 `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **商業使用是否需要授權？** 提供免費試用版；商業使用必須購買授權。
- **哪個 IDE 最適合搭配 Aspose.3D？** 完全支援 IntelliJ IDEA 與 Eclipse。

## 什麼是線性擠出？

線性擠出是將 2‑D 草圖（例如矩形或圓形）沿直線延伸，以產生 3‑D 實體的過程。預設情況下，擠出沿正 Z 軸方向，但 Aspose.3D 允許您透過 `setDirection` 屬性變更路徑，完整掌控最終幾何形狀。

## 為什麼要在線性擠出中更改擠出方向？

更改擠出方向可讓新幾何與既有物件對齊、直接產生傾斜元件而無需額外變換，並生成符合下游管線（如 3‑D 列印機或遊戲引擎）座標系統的模型。這可省去後處理步驟，並在使用避免不必要旋轉的方向向量時，將檔案大小減少最高 15 %。

## 前置條件

- 具備 Java 基礎知識。
- 已安裝 Aspose.3D 程式庫。您可從 [here](https://releases.aspose.com/3d/java/) 下載。亦可在主頁 [here](https://releases.aspose.com/) 瀏覽所有 Aspose 版本。
- 使用 Eclipse 或 IntelliJ IDEA 等 IDE。

## 匯入套件

`com.aspose.threed` 命名空間提供核心 3‑D 類別與實用型別。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 步驟 1：初始化基礎輪廓

`RectangleShape` 類別建立將被擠出的 2‑D 輪廓。小幅圓角半徑可使邊緣更平滑。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 步驟 2：建立場景

`Scene` 類別是 Aspose.3D 的最高層容器，負責保存所有 3‑D 節點、光源、相機與材質。

```java
Scene scene = new Scene();
```

## 步驟 3：建立節點

`Node` 代表場景圖中的一個物件，允許您附加幾何、變換與其他屬性。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 步驟 4：在左側節點執行線性擠出

`LinearExtrusion` 執行擠出操作，將 2‑D 輪廓轉換為 3‑D 網格。

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 步驟 5：在右側節點以方向執行線性擠出

此處我們 **更改擠出方向**。透過將自訂 `Vector3` 傳入 `setDirection`，擠出會沿向量 (0.3, 0.2, 1) 方向進行，產生與場景座標系統對齊的斜面形狀。

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 步驟 6：儲存 3D 場景

`save` 方法會將場景寫入指定格式的檔案。

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常見問題與解決方案

| 問題 | 發生原因 | 解決方法 |
|------|----------|----------|
| OBJ 檔案顯示為空 | 輪廓未加入到節點 | 確保在有效節點上呼叫 `createChildNode` |
| 方向似乎未變更 | `setDirection` 在擠出已建構完成後才被呼叫 | 如示範，於 `LinearExtrusion` 初始化時設定方向 |
| 網格解析度低 | `setSlices` 設定值過低 | 提高切片數量（例如 100 以上） |

## 結論

您現在已掌握 **如何更改線性擠出的擠出方向**、如何調整扭轉與切片設定，以及如何使用 Aspose.3D for Java **匯出 3D 模型 OBJ** 檔案。這些技巧讓您對幾何建立擁有精細控制，並能輕鬆將 3‑D 資產整合至更大的工作流程中。

## 常見問答

**Q:** 我可以在其他程式語言中使用 Aspose.3D 嗎？  
**A:** 可以——Aspose.3D 提供 .NET 與 Java 的 API，支援跨平台開發。

**Q:** Aspose.3D 有免費試用版嗎？  
**A:** 當然可以。您可於此處 [here](https://releases.aspose.com/) 取得完整功能的免費試用。

**Q:** 哪裡可以找到 Aspose.3D for Java 的詳細文件？  
**A:** 完整參考文件可於此處 [here](https://reference.aspose.com/3d/java/) 取得。

**Q:** 我要如何取得 Aspose.3D 的支援？  
**A:** 請前往官方 [Aspose.3D forum](https://forum.aspose.com/c/3d/18) 向社群與產品團隊尋求協助。

**Q:** 是否提供測試用的臨時授權？  
**A:** 有——可於此處 [here](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

---

**最後更新：** 2026-08-02  
**測試環境：** Aspose.3D for Java (latest release)  
**作者：** Aspose

{{< blocks/products/products-backtop-button >}}

## 相關教學

- [如何擠出形狀 - 使用 Java 進行線性擠出建立 3D 模型](/3d/java/linear-extrusion/)
- [使用 Aspose.3D 在 Java 中建立 3D 擠出](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D 圖形教學 – 線性擠出中的中心控制](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}