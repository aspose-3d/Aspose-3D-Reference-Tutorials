---
date: 2026-03-23
description: 學習如何使用 Aspose.3D for .NET 創建帶扭轉的擠出。本逐步指南涵蓋線性擠出扭轉技術。
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: 如何在直線擠出中製作扭轉擠出
url: /zh-hant/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在線性擠出中創建帶扭轉的擠出

## 簡介

如果您正在開發需要吸睛 3D 視覺效果的 .NET 應用程式，您很快會發現 **如何創建擠出** 是一項基本技能。Aspose.3D for .NET 提供乾淨且高效能的 API，能將簡單的 2‑D 輪廓轉換為精緻的 3‑D 模型——尤其在加入扭轉時更是如此。在本教學中，我們將逐步說明從設定場景到儲存最終 OBJ 檔的每個步驟，讓您親眼見證線性擠出扭轉的威力。

## 快速答覆
- **主要的擠出類別是什麼？** `LinearExtrusion`
- **哪個屬性會加入旋轉？** `Twist`
- **多少切片能產生平滑的結果？** 大約 100 個切片（視需要調整）
- **我可以使用其他形狀嗎？** 可以，任何 `IProfile`（例如圓形、多邊形或自訂曲線）
- **範例使用的檔案格式是什麼？** Wavefront OBJ（`.obj`）

## 先決條件

在開始之前，請確保您已具備以下條件：

- 已安裝 Aspose.3D for .NET。如尚未下載，請點擊 **[此處](https://releases.aspose.com/3d/net/)** 取得。
- 可正常使用的 .NET 開發環境（Visual Studio、VS Code 或任何您偏好的 IDE）。
- 具備 C# 語法與物件導向概念的基本認識。

## 匯入命名空間

在任何 .NET 專案中，正確使用命名空間至關重要。首先匯入必要的命名空間，以有效利用 Aspose.3D 的功能。以下是示範程式碼片段：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 逐步指南

### 步驟 1：初始化基礎輪廓

我們先定義要擠出的形狀。本例使用帶有小圓角半徑的矩形，以讓邊緣呈現微妙的曲線。

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### 步驟 2：建立 3D 場景

`Scene` 物件充當所有 3‑D 實體的畫布。可將其視為擠出的舞台。

```csharp
// Create a scene 
Scene scene = new Scene();
```

### 步驟 3：新增左側與右側節點

節點允許您以階層方式組織物件。我們將建立兩個同層節點——一個用於直線擠出，另一個用於帶扭轉的版本。

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### 步驟 4：在左側節點執行帶扭轉的線性擠出

`Twist` 屬性控制在擠出過程中輪廓的旋轉量。設定為 **0** 即為傳統的直線擠出。

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### 步驟 5：在右側節點執行帶扭轉的線性擠出

現在將同一輪廓套用 90 度的扭轉。這清楚展示了 **線性擠出扭轉** 效果。

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### 步驟 6：儲存 3D 場景

最後，將場景匯出為任何 3‑D 檢視器都能開啟的格式。範例使用 Wavefront OBJ，但 Aspose.3D 亦支援許多其他格式。

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 為什麼使用帶扭轉的線性擠出？

- **快速原型製作：** 將 2‑D 草圖轉換為 3‑D 零件，無需手動建模。
- **設計彈性：** 調整 `Twist` 值即可產生螺旋、螺旋肋或裝飾特徵。
- **效能友好：** `Slices` 參數讓您在視覺精細度與執行速度之間取得平衡。

## 常見問題與技巧

- **切片過多：** 雖然 100 個切片看起來平滑，但過高的數值可能會減慢渲染速度。若效能成問題，請測試較低的切片數。
- **負值扭轉：** 負的 `Twist` 會向相反方向旋轉，適用於鏡像設計。
- **檔案路徑：** 確保輸出目錄已存在且具有寫入權限，否則 `scene.Save` 會拋出例外。

## 結論

在本教學中，我們示範了如何使用 Aspose.3D for .NET 以帶扭轉的方式 **創建擠出**。透過調整 `Twist` 與 `Slices` 屬性，您可以產生各式形狀，從簡單的扭轉棒到複雜的螺旋結構，只需幾行程式碼。

## 常見問題

**Q: 我可以將帶扭轉的線性擠出套用到其他形狀嗎？**  
A: 當然可以！任何實作 `IProfile` 的類別——例如 `CircleShape`、`PolygonShape` 或自訂樣條曲線——都能以扭轉方式進行擠出。

**Q: `Twist` 屬性實際上代表什麼？**  
A: 它指定在整個擠出長度上，輪廓所旋轉的總角度（以度為單位）。

**Q: 增加切片數會影響記憶體使用量嗎？**  
A: 會的，更多的切片會產生更多的頂點與面，會佔用額外記憶體，且在低階裝置上可能影響效能。

**Q: 我可以將線性擠出與其他 Aspose.3D 功能結合使用嗎？**  
A: 完全可以。擠出後您可以套用材質、貼圖，甚至執行布林運算，以打造更豐富的模型。

**Q: 我該去哪裡取得協助或與其他開發者討論想法？**  
A: 加入 Aspose.3D 社群 **[Aspose Forum](https://forum.aspose.com/c/3d/18)**，獲取支援、範例與討論。

**最後更新：** 2026-03-23  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}