---
date: 2026-03-26
description: 學習如何使用 Aspose.3D for .NET 建立圓柱體並匯出 OBJ 檔案。本初學者友善指南涵蓋 3D 場景設定與 OBJ 匯出。
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: 如何建立具有剪切底部的圓柱體 – Aspose.3D for .NET
url: /zh-hant/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D for .NET 中建立帶剪切底面的圓柱體

## 介紹
如果你想了解 **如何建立圓柱體** 物件，並在 .NET 環境中使用自訂的剪切底面，恭喜你來對地方了。在本教學中，我們將逐步說明從設定 3‑D 場景到將最終模型匯出為 OBJ 檔案的每個步驟，讓你能夠利用 **Aspose.3D for .NET** 提升 *初學者 3D 建模* 技能。

## 快速解答
- **開始 3D 模型的主要類別是什麼？** `Scene` creates the root container for all geometry.  
- **哪個方法可將模型匯出為 OBJ？** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **測試是否需要授權？** A free trial is available — see the trial link in the FAQ.  
- **我可以更改剪切角度嗎？** Yes, modify `ShearBottom` with a `Vector2` value.  
- **這適合初學者嗎？** Absolutely; the API abstracts low‑level mesh handling.

## 什麼是 3D 場景？
*3D 場景* 是一個階層式容器，用於保存所有幾何實體、光源、相機和變換。在 Aspose.3D 中，`Scene` 類別提供了一種簡潔的方式來組織並稍後匯出你的模型。

## 為什麼要匯出 OBJ？
OBJ 是一種廣受支援的文字格式，許多 3‑D 應用程式（如 Blender、Maya、Unity）皆可匯入。將模型匯出為 OBJ 可讓你在 .NET 之外分享或進一步編輯圓柱體模型。

## 前置條件
- 具備 C# 與 .NET 開發的基本知識。  
- **Aspose.3D for .NET** 已安裝 – 你可以在 **[此處](https://releases.aspose.com/3d/net/)** 下載。  
- 已安裝 .NET IDE（Visual Studio、Rider 或 VS Code）以便編寫程式碼。

## 匯入命名空間
首先，將所需的命名空間引入作用域，以便 API 類型能被辨識。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 步驟 1：建立 3D 場景
`Scene` 物件充當模型階層的根節點。

```csharp
Scene scene = new Scene();
```

## 步驟 2：建立圓柱體 1
我們產生第一個圓柱體，半徑為 2，高度為 10，且具有 20 個徑向分段。

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 步驟 3：自訂圓柱體 1 的剪切底面
套用剪切變換，啟用扇形圓柱體產生，並調整其他屬性以達到所需形狀。

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 步驟 4：將圓柱體 1 加入場景
使用平移變換將第一個圓柱體放置在合適的位置。

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 步驟 5：建立圓柱體 2
第二個圓柱體使用相同的基礎尺寸建立，但不套用自訂剪切——非常適合並排比較。

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 步驟 6：將圓柱體 2 加入場景
我們只需將第二個圓柱體附加到場景圖中。

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 步驟 7：將場景匯出為 OBJ 檔案
最後，我們將整個場景儲存為 OBJ 檔案，以便能在任何標準的 3‑D 檢視器中開啟。

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## 常見問題與解決方案
| 問題 | 發生原因 | 解決方式 |
|-------|----------------|-----|
| **OBJ 檔案為空** | 場景未附加任何幾何體。 | 確保兩個圓柱體皆已加入 `scene.RootNode`。 |
| **剪切顯示異常** | `ShearBottom` 需要角度的正切值。 | 使用 `Math.Tan(angleInRadians)` 或提供的 `0.83`（約 47.5°）。 |
| **檔案路徑錯誤** | 目錄無效或不存在。 | 使用 `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`。 |

## 常見問答
### Aspose.3D for .NET 適合初學者嗎？
絕對適合！Aspose.3D for .NET 提供高階 API，將 3‑D 建模中繁重的數學運算抽象化，使任何技能層級的開發者都能輕鬆上手。

### 我可以對圓柱體套用不同的剪切角度嗎？
可以，每個 `Cylinder` 實例都有自己的 `ShearBottom` 屬性，因而能為每個物件指定不同的角度。

### 有提供試用版嗎？
有，你可以在 **[此處](https://releases.aspose.com/)** 探索免費試用版。

### 我可以在哪裡取得其他支援？
前往 **[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)** 獲取社群協助、程式碼範例與討論。

### 我該如何取得臨時授權？
在 **[此處](https://purchase.aspose.com/temporary-license/)** 取得臨時授權。

**其他問答**

**Q: 如何將模型匯出為其他格式，例如 STL？**  
A: 在 `scene.Save` 呼叫中，將 `FileFormat.WavefrontOBJ` 替換為 `FileFormat.STL`。

**Q: 建立圓柱體後，我可以為其加入動畫嗎？**  
A: 可以，你可以使用 Aspose.3D 提供的 `Animation` 類別，為節點變換加入關鍵影格動畫。

**Q: API 是否支援 .NET Core？**  
A: 此函式庫完全相容於 .NET Core、.NET 5+ 以及 .NET 6+。

---

**最後更新：** 2026-03-26  
**測試環境：** Aspose.3D for .NET（最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}