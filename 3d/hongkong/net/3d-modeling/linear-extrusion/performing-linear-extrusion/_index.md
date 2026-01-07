---
date: 2026-01-07
description: 學習如何使用 Aspose.3D for .NET 對 2D 剖面進行線性拉伸，並匯出 3D OBJ 模型。本線性拉伸教學將一步一步指導您。
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: 如何使用 Aspose.3D for .NET 進行線性擠出
url: /zh-hant/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用 Aspose.3D for .NET 進行 Linear Extrude

## 介紹

歡迎閱讀我們的 **linear extrusion tutorial**！在本指南中，您將學會如何將 2‑D 剖面進行 linear extrude，並將其轉換為完整的 3‑D 物件，使用 Aspose.3D for .NET。無論您是構建類 CAD 應用程式，或只是需要 **export 3d model obj** 檔案以供後續處理，此逐步說明將讓您有信心在專案中加入強大的幾何創建功能。

## 快速解答
- **什麼是 linear extrusion？** 將 2‑D 形狀沿直線路徑延伸，以建立 3‑D 實體。  
- **我們使用哪個函式庫？** Aspose.3D for .NET。  
- **我需要授權嗎？** 測試時可使用臨時授權；正式環境需購買完整授權。  
- **可以匯出為 OBJ 嗎？** 可以 – 最終場景會儲存為 Wavefront OBJ 檔案。  
- **程式碼行數多少？** 少於 30 行 C# 加上說明性註解。

## 什麼是 Linear Extrusion？

Linear extrusion 會將平面剖面（例如矩形或圓形）沿直線掃描，亦可加入扭轉、縮放或偏移。最終產生的實體可供渲染、編輯，或匯出至其他 3‑D 工具使用。

## 為何使用 Aspose.3D 進行 Linear Extrusion？

* **Zero‑dependency：** 無需外部 CAD 核心。  
* **Full .NET support：** 支援 .NET Framework、.NET Core 以及 .NET 5/6+。  
* **Export flexibility：** 可直接儲存為 OBJ、STL、FBX 等多種格式。  
* **Rich API：** 只需少數屬性即可控制 slices、twist 與 offsets。

## 前置條件

1. **已安裝 Aspose.3D** – 從 [here](https://releases.aspose.com/3d/net/) 下載。  
2. **文件存取** – 依照設定指南於 [here](https://reference.aspose.com/3d/net/) 參考。  
3. 具備 .NET 開發環境（Visual Studio、VS Code 或 Rider），並已參考所需命名空間。

## 匯入命名空間

加入必要的命名空間，即可啟用 Aspose.3D 功能：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

這些命名空間讓您可以使用 `Scene`、`LinearExtrusion`、`RectangleShape` 以及 `Vector3` 等工具類別。

## 執行 Linear Extrusion

以下為完整工作流程。每一步皆以簡明文字說明，緊接著對應的程式碼區塊，讓您不必猜測程式碼的作用。

### 步驟 1：初始化基礎剖面

首先，建立將要被擠出的 2‑D 形狀。本例使用帶有小圓角半徑的矩形。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*為何重要：* 剖面決定最終 3‑D 物件的橫截面。調整 `RoundingRadius`、寬度或高度即可得到不同的輪廓。

### 步驟 2：套用 Linear Extrusion

現在，我們沿 Z 軸將剖面掃描 10 個單位，設定 100 個 slices 以提升平滑度，將幾何置中，並加入完整 360° 的扭轉與偏移。

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*專業提示：* 可調整 `Slices` 以在效能與視覺品質間取得平衡，並嘗試 `Twist` 產生螺旋效果。

### 步驟 3：建立 Scene

`Scene` 為所有 3‑D 實體的容器——可視為畫布。

```csharp
Scene scene = new Scene();
```

### 步驟 4：將 Extrusion 加入 Scene

將擠出的幾何加入場景的根節點，使其成為可渲染層級的一部份。

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### 步驟 5：儲存 3‑D 模型

最後，將場景匯出為廣受支援的 OBJ 檔案。此步驟展示了 Aspose.3D 的 **export 3d model obj** 功能。

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

當您在任何 3‑D 檢視器中開啟產生的 `LinearExtrusion.obj`，即會看到一個扭轉的矩形棱柱——正如程式碼所描述的那樣。

## 常見問題與技巧

| 問題 | 為何發生 | 解決方式 |
|------|----------|----------|
| **剖面未顯示** | 忘記將擠出物件加入場景。 | 確保已呼叫 `CreateChildNode`。 |
| **扭轉看起來平坦** | `Slices` 太低，導致幾何粗糙。 | 將 `Slices` 增加（例如 200）以獲得更平滑的扭轉。 |
| **匯出失敗** | 輸出資料夾不存在或缺乏寫入權限。 | 使用 `RunExamples.GetOutputFilePath` 或手動建立目錄。 |
| **意外的縮放** | `Center` 設為 `false` 會移動幾何位置。 | 除非需要偏移，否則將 `Center = true`。 |

## 常見問答

### Q1：Aspose.3D 適合初學者嗎？

A1：絕對適合！Aspose.3D 提供友善的 API，本教學一步步帶您了解 linear extrusion 的基礎。

### Q2：我可以在商業專案中使用 Aspose.3D 嗎？

A2：可以，Aspose.3D 提供個人與商業兩種授權方案。詳情請參閱 [here](https://purchase.aspose.com/buy)。

### Q3：如何取得測試用的臨時授權？

A3：請前往 [this link](https://purchase.aspose.com/temporary-license/) 取得測試用的臨時授權。

### Q4：在哪裡可以找到社群支援？

A4：加入 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 與活躍的社群互動並尋求協助。

### Q5：是否提供免費試用？

A5：當然！前往 [here](https://releases.aspose.com/) 下載免費試用版，親自體驗 Aspose.3D 的功能。

**最後更新：** 2026-01-07  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## 目標關鍵字：

**主要關鍵字（最高優先）：**  
how to linear extrude

**次要關鍵字（支援）：**  
export 3d model obj, linear extrusion tutorial

**關鍵字整合策略：**
1. 主要關鍵字：使用 3-5 次（標題、meta、第一段落、H2 標題、正文）  
2. 次要關鍵字：各使用 1-2 次（標題、正文）  
3. 所有關鍵字必須自然整合——以可讀性為優先  
4. 若關鍵字不自然，請使用語意相近的變體或略過