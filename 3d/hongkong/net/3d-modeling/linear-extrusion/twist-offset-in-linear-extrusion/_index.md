---
date: 2026-03-23
description: 學習如何在 Aspose.3D for .NET 中於線性擠出加入扭轉，並了解如何在 asp.net 3D 建模項目中使用擠出功能。
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: 如何使用 Aspose.3D for .NET 在線性擠出中加入扭轉
url: /zh-hant/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用 Aspose.3D for .NET 在線性擠出中加入扭轉

## 簡介

如果您正在尋找一個清晰、逐步的指南，說明 **如何在線性擠出中加入扭轉**，您來對地方了。在本教學中，我們將使用 Aspose.3D for .NET 完整示範整個過程，向您展示 **如何使用擠出** 來建立動態的 3D 形狀，這些形狀非常適合 *asp.net 3d modeling* 場景。完成後，您將擁有一個可直接執行的範例，展示扭轉偏移、切片數量，以及將結果保存為 OBJ 檔案。

## 快速解答
- **「twist offset」是什麼作用？** 它會沿著擠出軸線移動扭轉的起始點。  
- **執行範例是否需要授權？** 測試時可使用臨時授權；正式上線則需完整授權。  
- **支援哪些 .NET 版本？** .NET Framework 4.5 以上、.NET Core 3.1 以上、.NET 5/6 以上。  
- **可以變更切片數量嗎？** 可以——調整 `Slices` 屬性即可控制網格平滑度。  
- **輸出格式只能是 OBJ 嗎？** 不是，Aspose.3D 支援多種格式；此處使用 OBJ 只是為了簡化示範。

## 什麼是線性拉伸中的扭轉偏移？

扭轉偏移定義了一個平移位移，會套用於扭轉操作。與其在擠出起點直接旋轉，幾何體會從指定的偏移向量開始旋轉，讓您對最終形狀擁有更多藝術性的控制。

## 為什麼選擇 Aspose.3D for .NET？

- **Full‑featured API** – 處理輪廓、變換以及各種檔案格式。  
- **Cross‑platform** – 可在 Windows、Linux、macOS 上使用 .NET Core 執行。  
- **Performance‑optimized** – 產生乾淨的網格，無需手動計算。  
- **Excellent documentation** – 豐富的範例可加速開發。

## 前提條件

在開始之前，請確保您已具備：

- Aspose.3D for .NET Library：從 [release page](https://releases.aspose.com/3d/net/) 下載並安裝。  
- 開發環境：Visual Studio、Rider，或任何支援 C# 的 IDE。

## 匯入命名空間

首先，匯入用於存取核心 3D 類別的命名空間。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

這些語句使 `Scene`、`LinearExtrusion`、`Vector3` 和其他基本類型在您的程式碼中可用。

## 逐步指南

### 步驟 1：初始化基礎輪廓

我們從一個簡單的矩形輪廓開始，並為其添加一個較小的圓角半徑，使邊緣不會過於銳利。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### 步驟 2：建立場景

`Scene` 用作所有節點、燈光、攝影機和幾何體的容器。

```csharp
Scene scene = new Scene();
```

### 步驟 3：建立節點

在場景根節點中添加兩個子節點——一個用於普通拉伸，另一個用於扭曲拉伸。左側節點沿著 X 軸偏移，以實現視覺上的分離。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### 步驟 4：左側節點上的線性拉伸（無扭曲偏移）

這裡我們示範一個基本的拉伸，進行完整的 360° 扭曲，並進行 100 次切片以獲得平滑效果。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### 步驟 5：在右側節點上套用扭轉偏移的線性拉伸

現在我們應用扭轉偏移量 `(3, 0, 0)`。這會將扭轉的起始點沿著 X 軸移動三個單位，從而創建一個明顯偏移的螺旋線。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### 步驟 6：儲存 3D 場景

最後，我們將場景儲存為 OBJ 檔案。請根據您的環境變更輸出路徑。

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 常見問題及解決方案

| 問題 | 原因 | 解決方法 |
|-------|----------------|-----|
| **Twist appears flat** | `Slices` 設定過低，導致網格粗糙。 | 增加 `Slices`（例如 200）以獲得更平滑的旋轉。 |
| **Object is off‑center** | `TwistOffset` 使用世界座標；節點可能已被平移。 | 以節點的本地變換為基礎套用偏移，或相應調整節點的平移。 |
| **File not saved** | 輸出路徑不正確或缺少寫入權限。 | 確認目錄存在且應用程式具備寫入權限。 |
| **License exception** | 在非試用版建置中未載入有效授權。 | 在建立場景前載入臨時或永久授權。 |

## 常見問題解答

### 問題1：我可以使用 Aspose.3D for .NET 和其他程式語言嗎？

回答1： Aspose.3D 主要支援 .NET 語言，但 Aspose 也提供了 Java 等其他平台的類似函式庫。

### 問題2：如何取得 Aspose.3D for .NET 的臨時授權？

回答2: 前往 [this link](https://purchase.aspose.com/temporary-license/) 取得測試用的臨時授權。

### 問題3：Aspose.3D for .NET 有社群論壇嗎？

回答3: 當然！請加入 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 與其他開發者交流並尋求協助。

### 問題4：是否有其他範例和文件？

回答4: 請參考 [documentation](https://reference.aspose.com/3d/net/) 獲取完整的教學與範例。

### 問題5：哪裡可以購買 Aspose.3D for .NET？

回答5: 前往 [this link](https://purchase.aspose.com/buy) 購買，解鎖 Aspose.3D 的全部功能。

### 問題6：我可以將模型匯出為 OBJ 以外的格式嗎？

回答6: 可以——Aspose.3D 支援 FBX、STL、3MF 等多種格式。只需在 `Save` 呼叫中更改 `FileFormat` 列舉值即可。

### 問題7：「如何加入扭曲」與常規旋轉有何不同？

回答7: 扭轉會在擠出長度上逐漸旋轉輪廓，而普通旋轉則一次性套用固定角度。偏移則在旋轉開始前先進行平移位移。

---

**上次更新：** 2026-03-23
**測試版本：** Aspose.3D for .NET（最新版本）
**作者：** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}