---
date: 2026-01-12
description: 學習如何使用 Aspose.3D for .NET 建立剪切底部圓柱，並匯出 3D 模型 OBJ。跟隨此一步一步的指南，掌握 3D 建模。
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: 如何使用 Aspose.3D for .NET 建立剪切底部圓柱體
url: /zh-hant/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 自訂剪切底部圓柱

## 簡介
歡迎閱讀本完整教學，您將學會如何使用 Aspose.3D for .NET **建立剪切底部圓柱** 模型。無論您是製作遊戲資產、機械零件，或是視覺示範，本教學都會一步步示範如何塑形圓柱底部、套用剪切，最後 **匯出 3D 模型 OBJ** 檔，以供任何後續流程使用。讓我們一起完成每個步驟，讓您在幾分鐘內即可產出自訂幾何形狀。

## 快速回答
- **什麼是剪切底部圓柱？** 底面傾斜（被剪切）而非平坦的圓柱。  
- **使用哪個函式庫？** Aspose.3D for .NET。  
- **如何匯出模型？** 使用 `scene.Save(..., FileFormat.WavefrontOBJ)`。  
- **需要授權嗎？** 有試用版；正式使用需購買商業授權。  
- **需要哪些前置條件？** .NET 開發環境與 Aspose.3D NuGet 套件。

## 什麼是剪切底部圓柱？
剪切底部圓柱是一種標準的圓柱網格，其底面經過剪切變形。此操作讓您能輕鬆建立斜面基座、坡道或自訂連接件，而無需手動編輯頂點。

## 為什麼在此任務中使用 Aspose.3D？
- **完整控制** 幾何參數（半徑、高度、分段）。  
- **內建剪切支援** 透過 `ShearBottom` 屬性，免除低階網格操作。  
- **一鍵匯出** 至常見格式如 OBJ、FBX、STL，讓與其他工具的整合更順暢。

## 前置條件
在開始之前，請確保您已具備：

- 基本的 C# 與 .NET 知識。  
- 已安裝 Aspose.3D for .NET。您可於 **[此處](https://releases.aspose.com/3d/net/)** 下載。  
- 相容 .NET 的 IDE（Visual Studio、Rider 或 VS Code）。

## 匯入命名空間
在您的 C# 檔案中，先匯入必要的命名空間：

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

## 步驟 1：建立場景
首先，實例化一個新的 3‑D 場景，用來容納所有物件。

```csharp
Scene scene = new Scene();
```

## 步驟 2：建立 Cylinder 1
建立我們將以剪切底部自訂的主要圓柱。

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 步驟 3：為 Cylinder 1 自訂剪切底部
套用剪切、啟用扇形生成，並調整其他屬性以取得期望形狀。

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 步驟 4：將 Cylinder 1 加入場景
將自訂的圓柱放入場景，並向右微移，以便同時觀察兩個物件。

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 步驟 5：建立 Cylinder 2
建立第二個純粹的圓柱作為對照。

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 步驟 6：將 Cylinder 2 加入場景
將第二個圓柱加入場景且不套用任何自訂剪切——這有助於說明前述步驟的效果。

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 步驟 7：儲存場景
最後，將整個場景匯出為 OBJ 檔，您即可在 Blender、Maya 或其他 3‑D 檢視器中開啟。

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## 常見問題與技巧
- **剪切值**：`Vector2` 接受 X 與 Y 的剪切因子。`0.83` 約等於 47.5°，您可依需求調整角度。  
- **匯出路徑**：確保指定的資料夾已存在且具寫入權限，否則 `scene.Save` 會拋出例外。  
- **效能**：對於高分段的圓柱，建議減少分段數（範例中的 `20`），以控制 OBJ 檔案大小。

## 常見問答

### Aspose.3D for .NET 適合初學者嗎？
**答**：絕對適合！Aspose.3D for .NET 提供友善的 API，對初學者與有經驗的開發者皆易於上手。

### 我可以對圓柱套用不同的剪切角度嗎？
**答**：可以，您可為每個圓柱分別自訂 `ShearBottom`，以產生獨特效果。

### 是否提供試用版？
**答**：可以，您可於 **[此處](https://releases.aspose.com/)** 取得免費試用版。

### 哪裡可以取得額外支援？
**答**：前往 **[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)** 取得社群支援與討論。

### 如何取得臨時授權？
**答**：於 **[此處](https://purchase.aspose.com/temporary-license/)** 取得臨時授權。

**Additional Q&A**

**Q: 如何將匯出格式改為 FBX？**  
A: 在 `scene.Save` 呼叫中將 `FileFormat.WavefrontOBJ` 替換為 `FileFormat.FBX`。

**Q: 匯出後我可以為圓柱加入動畫嗎？**  
A: OBJ 不支援動畫；若需動畫資料，請使用 FBX 或 GLTF。

**Q: 若需要更大的圓柱半徑該怎麼辦？**  
A: 調整 `Cylinder` 建構式的前兩個參數（例如 `new Cylinder(4, 4, …)`）。

## 結論
您現在已掌握如何使用 Aspose.3D for .NET **建立剪切底部圓柱** 模型並匯出為 OBJ 檔。可自行嘗試不同的剪切值、分段數與匯出格式，以符合專案需求。祝您建模愉快！

---

**最後更新：** 2026-01-12  
**測試環境：** Aspose.3D for .NET 24.11（撰寫時的最新版本）  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}