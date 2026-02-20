---
date: 2026-02-20
description: 學習使用 Aspose.3D 的 Java 3D 圖形教學，掌握線性擠出時中心的控制，包括如何設定圓角半徑以及儲存 OBJ 檔案（Java）。
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Java 3D 圖形教學 – 線性擠出中的中心
url: /zh-hant/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D 圖形教學 – 線性擠出之中心

## 簡介

如果你在 Java 中構建 3D 可視化，精通擠出技術是必須的。這個 **java 3d graphics tutorial** 會指導你如何使用 Aspose.3D for Java 控制線性擠出的中心，讓你無需額外數學即可建立精確、對稱的模型。完成本指南後，你將了解 `center` 屬性的重要性、如何 **set rounding radius**，以及如何 **save OBJ file java** 相容的輸出。

## 快速問答
- **center 屬性有什麼作用？** 它決定擠出是否以輪廓原點為中心對稱。  
- **執行程式碼是否需要授權？** 測試時可使用臨時授權；正式環境需購買完整授權。  
- **結果使用哪種檔案格式？** 場景會儲存為 Wavefront OBJ 檔案。  
- **可以更改切片數量嗎？** 可以，於 `LinearExtrusion` 物件上使用 `setSlices(int)`。  
- **Aspose.3D 是否相容於 Java 8 以上？** 當然，支援所有現代 Java 版本。

## 什麼是 java 3d graphics tutorial？

一個 **java 3d graphics tutorial** 逐步說明如何使用 Java 函式庫來建立、操作與渲染三維物件。本例聚焦於 Aspose.3D 的擠出 API，將 2‑D 輪廓轉換為完整的 3‑D 網格。

## 為什麼選擇 Aspose.3D for Java？

- **High‑level API** – 無需編寫低階網格計算。  
- **Cross‑format support** – 可匯出為 OBJ、FBX、STL 等多種格式。  
- **Performance‑optimized** – 高效處理大型場景。  
- **Rich documentation** – 包含以下範例。

## 先決條件

1. **Java Development Environment** – 已安裝 JDK 8 或更新版本。  
2. **Aspose.3D for Java** – 下載函式庫與文件說明 [here](https://reference.aspose.com/3d/java/)。  
3. **Document Directory** – 在電腦上建立資料夾以儲存產生的檔案，我們稱之為 **「Your Document Directory」**。

## 匯入套件

在 Java IDE 中匯入所需的 Aspose.3D 類別。這樣編譯器即可使用擠出與場景建構功能。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 逐步指南

### 步驟 1：設定基礎輪廓

首先，建立將要被擠出的 2‑D 形狀。此處使用矩形，並 **set rounding radius** 為 0.3，以平滑角落。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### 步驟 2：建立 3D 場景

`Scene` 物件作為所有 3‑D 節點、光源與相機的容器。

```java
Scene scene = new Scene();
```

### 步驟 3：加入左側與右側節點

我們會將兩個獨立節點並排放置，以便比較有無中心化的擠出效果。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 步驟 4：線性擠出 – 無中心 (左側節點)

在左側節點建立擠出，關閉中心化，並將網格切片數限制為三，以產生低多邊形預覽。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### 步驟 5：加入參考用地面平面 (左側節點)

薄盒子作為視覺地板，協助觀察擠出的方向。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### 步驟 6：線性擠出 – 置中 (右側節點)

現在重複擠出，這次啟用 `center`。幾何形狀將以輪廓原點為中心對稱。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### 步驟 7：加入參考用地面平面 (右側節點)

右側使用相同的地面平面，讓比較更清晰。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### 步驟 8：儲存 3D 場景

最後，將整個場景匯出為 Wavefront OBJ 檔案——此格式可在大多數 3‑D 編輯器中直接使用。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 常見問題與解決方案

| 問題 | 發生原因 | 解決方法 |
|------|----------|----------|
| **擠出顯示偏移** | `setCenter(false)` 會使輪廓固定在角落。 | 使用 `setCenter(true)` 以取得對稱結果。 |
| **OBJ 檔案為空** | 輸出目錄路徑不正確或缺少寫入權限。 | 確認 `MyDir` 指向已存在的資料夾且應用程式具有寫入權限。 |
| **圓角看起來銳利** | 相對於矩形尺寸，圓角半徑過小。 | 增大半徑值（例如 `setRoundingRadius(0.5)`）。 |

## 常見問答

### Q1：我可以在商業專案中使用 Aspose.3D for Java 嗎？

A1：可以，Aspose.3D for Java 可用於商業用途。授權細節請參閱 [here](https://purchase.aspose.com/buy)。

### Q2：是否提供免費試用？

A2：可以，您可於 [here](https://releases.aspose.com/) 取得 Aspose.3D for Java 的免費試用。

### Q3：在哪裡可以取得 Aspose.3D for Java 的支援？

A3：Aspose.3D 社群論壇是尋求支援與分享經驗的好地方。請前往論壇 [here](https://forum.aspose.com/c/3d/18)。

### Q4：測試是否需要臨時授權？

A4：是的，若測試需要臨時授權，可於 [here](https://purchase.aspose.com/temporary-license/) 取得。

### Q5：文件說明在哪裡？

A5：Aspose.3D for Java 的文件說明可在 [here](https://reference.aspose.com/3d/java/) 取得。

## 結論

完成此 **java 3d graphics tutorial** 後，你已掌握如何控制線性擠出的中心、調整圓角半徑，並使用 Aspose.3D **save OBJ file java** 輸出。這些技巧讓你對網格對稱性有精細的控制，對於遊戲資產、CAD 原型與科學可視化皆相當重要。歡迎嘗試不同的輪廓、切片數量與匯出格式，以擴充你的 3‑D 工具箱。

---

**最後更新：** 2026-02-20  
**測試環境：** Aspose.3D for Java 24.11  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}