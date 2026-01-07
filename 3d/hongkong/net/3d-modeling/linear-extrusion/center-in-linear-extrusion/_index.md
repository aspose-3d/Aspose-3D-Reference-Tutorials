---
date: 2026-01-07
description: 學習如何在使用 Aspose.3D for .NET 進行線性擠出時加入地面平面，並匯出 Wavefront OBJ 檔案。掌握 3‑D
  建模中的置中與接地技巧。
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: 在線性擠出中加入基準平面與中心
url: /zh-hant/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Linear Extrusion 中加入基準平面與置中

## 簡介

歡迎閱讀本完整指南，學習如何使用 Aspose.3D for .NET 精通線性擠出。如果您想 **加入基準平面** 到模型並 **匯出 Wavefront OBJ** 檔，同時保持擠出體置中，這裡正是您需要的地方。在本教學中，我們將深入探討線性擠出技術，特別聚焦於置中功能，以及基準平面如何協助您更清晰地觀察結果。

## 快速解答
- **「add ground plane」的作用是什麼？** 它提供一個視覺參考，讓您輕鬆看出擠出體在 X‑Z 平面上的位置。  
- **使用哪種格式匯出模型？** 場景會儲存為 Wavefront OBJ 檔 (`FileFormat.WavefrontOBJ`).  
- **執行程式碼是否需要授權？** 開發階段可使用免費試用版，正式上線則需永久授權。  
- **可以更改擠出長度嗎？** 可以 – 修改 `LinearExtrusion` 的第二個參數。  
- **置中是可選的嗎？** 設定 `Center = true` 會將擠出體以輪廓為中心；`false` 則對齊至一側。

## 先決條件

在開始這段激動人心的旅程之前，請確保您已具備以下條件：

- 具備基本的 C# 程式語言知識。  
- 已在電腦上安裝 Visual Studio。  
- Aspose.3D for .NET 程式庫，可從 [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) 下載。  
- 請確保在整個教學過程中能存取 [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/)。

## 匯入命名空間

首先，匯入必要的命名空間。這些命名空間將為我們的 3D 建模作品奠定基礎。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 步驟 1：初始化基礎輪廓

我們先定義一個矩形輪廓作為擠出基礎。`RoundingRadius` 會在角落加入細微的圓角。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 步驟 2：建立 3D 場景

`Scene` 物件充當所有幾何體、光源與相機的容器。

```csharp
Scene scene = new Scene();
```

## 步驟 3：建立左側與右側節點

在根節點下建立兩個同層節點。一個示範 **未** 置中的擠出，另一個示範 **已** 置中的擠出。我們同時將左側節點平移，以免兩個範例重疊。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## 步驟 4：在左側節點執行 Linear Extrusion（不置中）

此處我們在不置中的情況下擠出輪廓。請留意 `Center = false` 旗標。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## 步驟 5：為左側節點加入基準平面作為參考

加入一個薄盒子作為 **基準平面**，讓您清楚看到擠出體在基底上的位置。

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## 步驟 6：在右側節點執行 Linear Extrusion（置中）

現在我們對相同輪廓執行擠出，並啟用置中。幾何體將對稱地位於輪廓原點周圍。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## 步驟 7：為右側節點加入基準平面作為參考

在右側節點加入第二個基準平面，以保持視覺比較的一致性。

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## 步驟 8：匯出 Wavefront OBJ 檔案

最後，我們 **匯出 Wavefront OBJ**，讓結果能在任何標準 3‑D 檢視器中開啟。

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 為什麼要加入基準平面？

加入基準平面可立即提供擠出高度與對齊方式的視覺提示。當需要比較置中與未置中的結果時，這特別有幫助，如本教學所示。

## 常見問題與技巧

- **基準平面未顯示：** 確認平面的厚度（`Box` 建構式中的 `0.01`）足夠小，不會遮蔽擠出體，同時又足夠大以便被渲染。  
- **匯出失敗：** 檢查輸出目錄是否存在且您具有寫入權限。  
- **置中擠出看似偏移：** 再次確認 `Center` 屬性；`true` 會將輪廓置中，`false` 則對齊至一側。

## 常見問答

### Q1：我可以在其他程式語言中使用 Aspose.3D for .NET 嗎？

A1：Aspose.3D 主要支援 .NET 語言，如 C# 與 VB.NET。

### Q2：我可以在哪裡取得 Aspose.3D 相關問題的支援？

A2：請前往 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 取得專屬支援與討論。

### Q3：是否提供 Aspose.3D for .NET 的免費試用？

A3：是的，您可在此取得免費試用版 [here](https://releases.aspose.com/)。

### Q4：如何取得 Aspose.3D for .NET 的臨時授權？

A4：您可在此取得臨時授權 [here](https://purchase.aspose.com/temporary-license/)。

### Q5：在哪裡購買 Aspose.3D for .NET 授權？

A5：請於此處購買授權 [here](https://purchase.aspose.com/buy)。

### Q6：我可以將場景匯出為除 OBJ 之外的其他格式嗎？

A6：可以，Aspose.3D 支援多種格式，如 STL、FBX 與 GLTF。只需在 `Save` 方法中更改 `FileFormat` 列舉值即可。

### Q7：如何變更擠出的切片數量？

A7：在 `LinearExtrusion` 建構式中調整 `Slices` 屬性，以控制網格密度。

---

**最後更新：** 2026-01-07  
**測試環境：** Aspose.3D for .NET 最新版  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}