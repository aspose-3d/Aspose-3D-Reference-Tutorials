---
date: 2026-01-22
description: 了解如何在 Aspose.3D for .NET 中將變換矩陣套用到節點、將場景轉換為 FBX，並使用一步一步的程式碼套用多重變換。
linktitle: Apply Transformation Matrix to a Node – Aspose.3D for .NET
second_title: Aspose.3D .NET API
title: 將變換矩陣套用於節點 – Aspose.3D for .NET
url: /zh-hant/net/geometry-and-hierarchy/transformation-node-matrix/
weight: 21
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 將變換矩陣套用至節點

## 簡介

在現代 3D 圖形中，**套用變換矩陣**至節點是精確移動、旋轉或縮放物件的基礎。使用 Aspose.3D for .NET，您可以輕鬆**套用變換矩陣**至任何節點場景。本教學將帶您完成整個流程——從建立網格盒到將場景轉換為 FBX——讓您即時看到結果。

## 快速答覆
- **「套用變換矩陣」的作用是什麼？** 它使用 4×4 矩陣修改節點的位置、方向或縮放。  
- **可以匯出成哪種檔案格式？** 您可以**將場景轉換為 FBX**（或其他格式，如 STL、GLTF、OBJ）。  
- **使用 Aspose.3D 是否需要授權？** 可取得暫時授權以供評估；正式環境需購買完整授權。  
- **可以串接多個變換嗎？** 可以——透過矩陣相乘**套用多重變換**。  
- **支援哪些 .NET 版本？** .NET Framework 4.5 以上、.NET Core 3.1 以上、.NET 5/6 及更高版本。

## 什麼是變換矩陣？

變換矩陣是一個 4 × 4 的數值格子，用於編碼平移、旋轉、縮放或上述操作的任意陣指派給節點後，該節點的幾何體會在 3ose.3D 進行節點變換？

- **高階 API** – 無需自行編寫低階數學運算；Aspose 會處理矩陣的建立與套用。  
- **廣泛的格式支援** – 可直接儲存為 FBX、STL、GLTF、OBJ 等。  
- **跨平台** – 可在 Windows、Linux 及 macOS .NET 執行環境上運作。  
- **效能最佳化** – 能有效處理大型場景。

## 先決條件

1. **Aspose.3D for .NET Library** – 前往[此處](https://releases.aspose.com/3d/net/)下載。  
2. **開發環境** – 具備 .NET IDE（如 Visual Studio、Rider 或 VS Code）且建立新的主控台或類別庫專案。  

## 匯入命名空間

首先匯入必要的命名空間，以取得 3D 引擎類別的存取權。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

現在讓我們一步一步分解變換工作流程。

## 如何將變換矩陣套用至節點

### 步驟 1：初始化新場景

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix            
// Initialize scene object
Scene scene = new Scene();

```

建立全新的 `Scene`，為您提供一個乾淨的畫布，可在其上加入幾何體與變換。

### 步驟 2：建立網格盒並附加至場景

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = (new Box()).ToMesh();

// Create a container node for the mesh.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

此處我們使用內建的 `Box` 基元**建立網格盒**，並將其附加到名為 `cubeNode` 的新子節點。此節點將成為我們變換的目標。

### 步驟 3：設定自訂平移矩陣（套用變換矩陣）

```csharp
// Set custom translation matrix
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

`Matrix4` 建構子會定義一個 4 × 4 矩陣。調整其數值即可達成所需的平移、旋轉或縮放。在此範例中，我們將立方體沿 Y 軸平移 20 單位，並加入少量剪切。

> **專業提示：** 若要**套用多重變換**，請在指派給 `TransformMatrix` 前，先將其他矩陣與現有矩陣相乘。

### 步驟 4：儲存場景 – 將場景轉換為 FBX

```csharp
// The path to the documents directory.
var output = "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

本範例選擇 FBX 格式，即**將場景轉換為 FBX**D 會根據檔案副檔名自動選擇陣（即除對角線外全為零）。 |
| 匯出的 FBX 變形 | 確保使用最新的 Aspose.3D 版本，且矩陣符合右手座標系慣例。 |
| 執行時授權例外 | 在呼叫任何 Aspose API 前先套用暫時或完整授權。 |

## 常見問答

### Q1：什麼是 3D 圖形中的變**A：** 它是一種數學表示法，用於編碼平移、旋轉、縮放或將給節點的 `TransformMatrix`。

### Q3：我可以**將場景轉換為 FBX**或其他格式嗎？
**A：** Aspose.3D 支援 FBX、STL、GLTF、OBJ、3MF 等。完整清單請參閱[文件說明](https://reference.aspose.com/3d/net/)。

### Q4：如何取得 Aspose.3D for .NET 的暫時授權？
**A：** 前往[暫時授權頁面](https://purchase.aspose.com/temporary-license/)申請試用授權。

### Q5：在哪裡可以取得 Aspose.3D 的社群支援？
**A：** 加入[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)討論，提出問題並分享經驗。

## 結論

現在您已學會如何使用 Aspose.3D for .NET **套用變換矩陣**至節點、建立網格盒，並**將場景轉換為 FBX**。這些技巧為互動式視覺化、遊戲資產流水線及自動化場景生成等高階 3D 應用開啟了大門。

---

**最後更新：** 2026-01-22  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}