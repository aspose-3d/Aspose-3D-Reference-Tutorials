---
date: 2026-01-14
description: 學習如何使用 Aspose.3D for .NET 在 3D 場景中為立方體製作動畫。本指南展示如何建立動畫曲線、綁定關鍵幀以及為 3D
  屬性製作動畫。
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: 如何使用 Aspose.3D for .NET 在 3D 場景中為立方體製作動畫
url: /zh-hant/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 3D 場景中使用 Aspose.3D for .NET 動畫化立方體

## 簡介

如果你正投入 .NET 中的 3D 場景建立與動畫領域，Aspose.3D 是你的首選工具包。在本步驟指南中，我們將探討 **如何動畫化立方體** 物件，透過動畫其屬性、建立動畫曲線以及綁定關鍵影格。完成後，你將擁有一個完整動畫化的立方體，並可匯出至常見的 3D 格式。

## 快速答覆
- **使用的函式庫是什麼？** Aspose.3D for .NET  
- **本教學主要涵蓋哪項任務？** 如何在 3D 場景中動畫化立方體  
- **關鍵步驟？** 匯入命名空間、建立場景、綁定關鍵影格、儲存檔案  
- **需要授權嗎？** 免費試用可用於學習；商業授權則需於正式環境使用  
- **支援的輸出格式？** FBX (ASCII 7500) 以及 Aspose.3D 支援的其他格式  

## 什麼是 Aspose.3D 中的「如何動畫化立方體」？

對立方體進行動畫化是指使用關鍵影格資料，隨時間變更其變換屬性（例如平移、旋轉或縮放）。Aspose.3D 提供簡潔的 API，讓你能直接在場景節點上 **建立動畫曲線**、**綁定關鍵影格**，以及 **動畫化 3D 屬性**。

## 為何使用 Aspose.3D 來動畫化立方體？

- **完整的 .NET 整合** – 支援 .NET Framework、.NET Core 以及 .NET 5/6。  
- **無外部相依性** – 簡單動畫無需 Unity 或其他引擎。  
- **匯出彈性** – 動畫化場景可儲存為 FBX、OBJ、GLTF 等格式，供後續流程使用。

## 先決條件

在開始這段精彩旅程之前，請確保已具備以下先決條件：

- Aspose.3D for .NET：確保已安裝此函式庫。可從 [Aspose.3D 官方網站](https://releases.aspose.com/3d/net/) 下載。

- C# 知識：熟悉 C# 程式語言對於理解與實作範例至關重要。

- 整合開發環境 (IDE)：使用你慣用的 IDE，例如 Visual Studio，來撰寫範例程式。

- 基本 3D 場景概念：掌握基礎的 3D 場景概念，能讓學習過程更順暢。

## 匯入命名空間

在 C# 程式碼中，請確保匯入 Aspose.3D 所需的命名空間。以下為必要的集合：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## 步驟 1：初始化 Scene 物件

建立一個空的場景，用以容納所有節點與動畫。

```csharp
Scene scene = new Scene();
```

## 步驟 2：使用 Polygon Builder 建立 Mesh

我們使用輔助方法 `Common.CreateMeshUsingPolygonBuilder()` 產生一個簡易的立方體 Mesh。

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## 步驟 3：建立立方體節點

將立方體 Mesh 加入場景作為根節點的子節點。節點名稱 **cube1** 之後在綁定關鍵影格時會用到。

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## 步驟 4：尋找 Translation 屬性

要為立方體位置加入動畫，我們需要在節點的 Transform 上找到其 **Translation** 屬性。

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## 步驟 5：建立 Bind Point

`BindPoint` 用於將場景屬性連結至動畫曲線。此處我們綁定 Translation 屬性。

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## 步驟 6：在 X 軸元件上綁定動畫曲線

現在為 **X** 軸建立動畫曲線。此步驟示範 **建立動畫曲線**，並說明如何 **綁定關鍵影格**。

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## 步驟 7：在 Z 軸元件上綁定動畫曲線

同樣地，我們為 **Z** 軸加入動畫，使立方體的運動路徑更具動態感。

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## 步驟 8：儲存 3D 場景

將動畫化的場景匯出為 FBX 檔案。`FBX7500ASCII` 格式受到多數 3D 工具廣泛支援。

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## 步驟 9：顯示成功訊息

向使用者回饋動畫已成功加入的訊息。

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## 常見問題與解決方案

| 問題 | 原因 | 解決方式 |
|------|------|----------|
| 未觀察到移動 | 關鍵影格時間未與播放範圍匹配 | 確保場景的動畫時間軸涵蓋關鍵影格時間（本例為 0‑5 秒）。 |
| 檔案路徑錯誤 | `output` 指向不存在的目錄 | 先建立目錄或使用絕對路徑。 |
| 授權例外 | 生產環境未使用有效授權 | 在建立 `Scene` 前套用 Aspose.3D 授權。 |

## 常見問答

### Q1：在哪裡可以找到 Aspose.3D 文件？

A1：文件可於 [此處](https://reference.aspose.com/3d/net/) 取得。

### Q2：如何下載 Aspose.3D for .NET？

A2：可從 [發行頁面](https://releases.aspose.com/3d/net/) 下載。

### Q3：是否提供免費試用？

A3：是的，您可於 [此處](https://releases.aspose.com/) 取得免費試用。

### Q4：在哪裡可以取得 Aspose.3D 支援？

A4：請前往 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 取得支援。

### Q5：是否能取得臨時授權？

A5：是的，您可於 [此處](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

## 額外問答（AI 優化）

**Q：我可以動畫化其他屬性，例如旋轉或縮放嗎？**  
A：當然可以。使用 `cube1.Transform.FindProperty("Rotation")` 或 `"Scale"`，並以相同方式綁定關鍵影格序列。

**Q：Aspose.3D 是否支援除 Bezier 與 Linear 之外的關鍵影格插值類型？**  
A：是的，亦支援 `Interpolation.Step` 與 `Interpolation.Cubic`，提供更細緻的控制。

**Q：如何在匯出前預覽動畫？**  
A：Aspose.3D 在 API 中提供簡易檢視器；或將匯出的 FBX 載入如 Autodesk FBX Review 等 3D 檢視器。

**Q：是否能同時動畫化多個立方體？**  
A：為每個立方體建立獨立節點，取得各自的屬性，並綁定獨立的關鍵影格序列。

## 結論

恭喜！你剛剛掌握了使用 Aspose.3D for .NET 在 3D 場景中 **動畫化立方體** 的技巧。現在你已了解如何 **建立動畫曲線**、**綁定關鍵影格**，以及 **動畫化 3D 屬性**，讓靜態幾何體活起來。歡迎自行嘗試旋轉、縮放，甚至形變目標，以擴充你的動畫工具箱。

---

**最後更新：** 2026-01-14  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}