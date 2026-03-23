---
date: 2026-03-23
description: 學習如何使用 Aspose.3D for .NET 進行切片的線性擠出，並透過一步一步的程式碼範例建立詳細的 3D 模型。
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: 使用 Aspose.3D for .NET 進行切片線性擠出
url: /zh-hant/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何使用 Aspose.3D for .NET 進行切片線性拉伸

## 簡介

歡迎來到使用 Aspose.3D for .NET 的 3D 設計世界！在本教學中，你將學會 **如何使用切片進行線性拉伸**，這項技術讓你能掌控模型的細節層級。無論你是資深開發者還是剛入門，我們都會一步步帶領你說明每個動作背後的原因，並提供實用技巧讓你立即上手。

## 快速解答
- **什麼是切片線性拉伸？** 這是一種將 2D 剖面延伸成 3D 的方法，同時指定產生多少個中間橫截面（切片）。  
- **為什麼要使用切片？** 更多切片可產生更平滑的曲率；較少切片則可保持網格輕量。  
- **先決條件？** Aspose.3D for .NET、相容 .NET 的 IDE，以及基本的 C# 知識。  
- **典型執行時間？** 範例在現代電腦上執行時間不到一秒。  
- **輸出格式？** 範例會儲存為 Wavefront OBJ，但 Aspose.3D 支援多種格式。

## 什麼是切片線性拉伸？

線性拉伸將 2‑D 形狀（剖面）沿直線拉伸，產生 3‑D 實體。**Slices** 屬性決定在拉伸的起點與終點之間插入多少個中間橫截面，從而影響平滑度與多邊形數量。

## 為什麼在切片線性拉伸中使用切片？

- **控制網格密度：** 微調視覺品質與檔案大小之間的平衡。  
- **最佳化效能：** 實時應用使用較少切片，高解析度渲染則使用較多切片。  
- **創意彈性：** 在不同物件上結合不同的切片數，以突顯設計意圖。

## 先決條件

在開始之前，請確保你已擁有：

- Aspose.3D for .NET Library – 從 [here](https://releases.aspose.com/3d/net/) 下載。  
- 支援 C# 的 IDE（Visual Studio、Rider、VS Code 等）。  
- 基本的 C# 語法與物件導向概念。  
- 對 3‑D 幾何的好奇心與實驗精神！

## 匯入命名空間

首先，匯入能讓你存取 Aspose.3D 核心類別的命名空間。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 逐步指南

### 步驟 1：初始化基礎剖面

我們先建立一個簡單的矩形，並給予小幅圓角半徑，使邊緣不會過於銳利。

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### 步驟 2：建立 3D 場景

`Scene` 充當所有節點、網格、光源與相機的容器。

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### 步驟 3：新增左側與右側節點

我們會在場景根節點下建立兩個同層節點。左側節點使用較低的切片數，右側節點使用較高的切片數，讓你能比較視覺差異。

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### 步驟 4：對左側節點執行線性拉伸（低細節）

此處僅以 **2 個切片** 拉伸矩形，產生較粗糙的網格——適合快速預覽。

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### 步驟 5：對右側節點執行線性拉伸（高細節）

現在使用 **10 個切片**，可得到更平滑的結果。留意幾何體變得更細緻。

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### 步驟 6：儲存 3D 場景

最後，將場景寫入 OBJ 檔案。將 `"Your Output Directory"` 替換為你機器上有效的路徑。

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## 常見問題與解決方案

| 問題 | 發生原因 | 解決方法 |
|------|----------|----------|
| **未產生檔案** | 輸出路徑無效或缺少寫入權限。 | 使用絕對路徑並確保資料夾已存在。 |
| **物件看起來平坦** | `Slices` 設為 1 或 0。 | 將 `Slices` 設為至少 2，以產生可見的拉伸。 |
| **幾何體異常** | 圓角半徑對矩形尺寸而言過大。 | 將 `RoundingRadius` 調整為小於矩形最短邊的一半的值。 |

## 常見問答

**Q: 我可以變更拉伸方向嗎？**  
A: 可以。使用節點的 `Transform` 屬性在儲存前旋轉或平移拉伸後的幾何體。

**Q: Aspose.3D 支援其他拉伸類型嗎？**  
A: 當然支援。除了 `LinearExtrusion`，你還可以使用 `RevolveExtrusion`、`SweepExtrusion` 等。

**Q: 我可以匯出哪些檔案格式？**  
A: Aspose.3D 支援 OBJ、STL、FBX、3MF、Collada 等多種格式。只需更改 `FileFormat` 列舉即可。

**Q: 有辦法以程式方式設定材質嗎？**  
A: 有。建立節點後，將 `Material` 指派給其 `Entity` 集合即可。

**Q: 切片數量如何影響記憶體使用量？**  
A: 更多切片會增加頂點與面數，從而成比例提升記憶體消耗。請使用效能分析找出目標平台的最佳平衡點。

## 原始常見問答

### Q1: 我可以在其他程式語言中使用 Aspose.3D for .NET 嗎？

A1: Aspose.3D 主要設計給 .NET 使用，但你可以透過 .NET 綁定，探索與 Python 等語言的互通性。

### Q2: 哪裡可以找到 Aspose.3D for .NET 的詳細文件？

A2: 請參考文件 [here](https://reference.aspose.com/3d/net/)，了解 Aspose.3D 功能與使用方式的深入資訊。

### Q3: Aspose.3D for .NET 有免費試用版嗎？

A3: 有，你可以在 [here](https://releases.aspose.com/) 取得免費試用，先行體驗函式庫功能再決定是否購買。

### Q4: 我該如何取得 Aspose.3D for .NET 的技術支援？

A4: 前往 Aspose.3D 論壇 [here](https://forum.aspose.com/c/3d/18) 尋求協助，並與社群互動。

### Q5: 我可以使用臨時授權嗎？

A5: 可以，請至 [here](https://purchase.aspose.com/temporary-license/) 取得臨時授權以進行評估。

## 結論

你現在已了解 **如何使用切片進行線性拉伸**，並體驗不同切片數對模型的影響，同時學會如何匯出成果。可嘗試其他剖面、調整 `Slices` 值，或加入材質與光源，打造可投入生產的 3‑D 資產。

---

**最後更新：** 2026-03-23  
**測試環境：** Aspose.3D 24.11 for .NET（撰寫時的最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}