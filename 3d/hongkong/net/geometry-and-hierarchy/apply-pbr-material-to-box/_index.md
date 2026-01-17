---
date: 2026-01-17
description: 學習如何使用 Aspose.3D for .NET 將 PBR 材質套用到盒子上、建立 PBR 材質，並以實體渲染方式匯出 STL ASCII
  檔案。
linktitle: Applying PBR Material to Box
second_title: Aspose.3D .NET API
title: 如何將 PBR 材質套用到盒子上
url: /zh-hant/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何將 PBR 材質套用到盒子

## 介紹

歡迎來到 3D 圖形的奇妙世界！在本步驟教學中，您將學會 **如何將 pbr** 材質套用到盒子，使用 Aspose.3D for .NET。我們會一步步說明如何建立 PBR 材質、將其加入網格，最後 **匯出 STL ASCII**，讓您能在任何後續工作流程中使用此模型。無論是開發遊戲原型或產品視覺化，掌握此工作流程都能為您的 .NET 應用程式開啟寫實、基於物理的渲染 (PBR) 大門。

## 快速答覆
- **主要目標是什麼？** 將 PBR 材質套用到盒子並匯出為 STL ASCII。  
- **使用哪個函式庫？** Aspose.3D for .NET（如何使用 aspose）。  
- **需要授權嗎？** 需要，生產環境必須使用臨時或正式授權。  
- **支援的輸出格式？** STL ASCII（export stl ascii）以及其他多種 3D 格式。  
- **需要多久時間？** 基本實作大約 10‑15 分鐘即可完成。

## 什麼是 PBR 材質？
Physically Based Rendering (PBR) 是一種著色模型，模擬光線與真實世界表面的交互。透過調整金屬度 (metallic) 與粗糙度 (roughness) 等屬性，您可以在不必手動調校複雜著色器的情況下，達到高度寫實的效果。

## 為什麼使用基於物理的渲染 (PBR)？
- **寫實度：** 材質對光線的回應符合真實物理。  
- **一致性：** 同一材質在任何光照環境下都能正確呈現。  
- **效能：** 現代 GPU 已針對 PBR 計算做最佳化，讓您免費獲得效能提升。

## 前置條件

在進入程式碼之前，請先確保您已具備以下項目：

### 下載並安裝 Aspose.3D for .NET
請參考 [Aspose.3D for .NET documentation](https://reference.aspose.com/3d/net/) 取得下載與安裝說明。

### 取得授權
為解鎖 Aspose.3D 的全部功能，請取得有效授權。您可以在 [此處](https://purchase.aspose.com/temporary-license/) 取得臨時授權，或在 [此處](https://purchase.aspose.com/buy) 購買正式授權。

## 匯入命名空間
首先，請匯入必要的命名空間，以便使用 Aspose.3D for .NET 的功能：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 步驟 1：初始化 Scene
使用以下程式碼片段建立 3D 場景：

```csharp
Scene scene = new Scene();
```

## 步驟 2：建立 PBR 材質
現在我們 **create pbr material**，為盒子賦予寫實外觀：

```csharp
PbrMaterial mat = new PbrMaterial();
```

## 步驟 3：設定材質屬性
微調材質屬性，使其接近金屬且相當粗糙——非常適合刷金屬盒子：

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## 步驟 4：建立盒子
產生一個將套用 PBR 材質的盒子：

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## 步驟 5：將 PBR 材質套用到盒子
將先前配置好的 **add pbr material** 指派給剛建立的盒子節點：

```csharp
boxNode.Material = mat;
```

## 步驟 6：將 3D Scene 儲存為 STL ASCII
最後，**export stl ascii**，讓模型能在任何標準 3D 檢視器或切片軟體中開啟：

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

恭喜！您已成功使用 Aspose.3D for .NET 在 3D 場景中將 PBR 材質套用到盒子。

## 常見問題與技巧
- **找不到授權檔案：** 請確保在任何 Aspose 呼叫之前先載入授權檔案，否則函式庫會以評估模式執行。  
- **檔案路徑錯誤：** 使用 `Path.Combine` 可避免在不同作業系統上遺失路徑分隔符。  
- **粗糙度 vs. 金屬度：** 兩者同時設定過高會使表面看起來平坦；建議在 0.5‑0.9 之間調整，以取得平衡效果。

## 結論
使用 Aspose.3D for .NET 進入 3D 圖形領域，為您開啟無限創意可能性。憑藉直觀的 API 與強大的功能，打造視覺驚豔的場景將變得輕鬆愉快。接下來，您可以嘗試將盒子換成更複雜的網格，或實驗不同的 PBR 紋理，觀察光照的變化。

## 常見問答

**Q1: Aspose.3D 是否相容其他 3D 檔案格式？**  
A1: 是的，Aspose.3D 支援多種 3D 檔案格式，確保您在專案中的彈性。

**Q2: 我可以將 Aspose.3D 用於商業應用嗎？**  
A2: 當然！Aspose.3D 提供商業授權，讓您無縫整合至應用程式中。

**Q3: 有提供試用版嗎？**  
A3: 有，您可在此下載免費試用版 [here](https://releases.aspose.com/) 以探索 Aspose.3D 的功能。

**Q4: 哪裡可以找到社群支援與討論？**  
A4: 加入 Aspose.3D 社群於 [Aspose.3D Forums](https://forum.aspose.com/c/3d/18) 取得支援與討論。

**Q5: 如何取得 Aspose.3D 的臨時授權？**  
A5: 您可在此取得臨時授權 [here](https://purchase.aspose.com/temporary-license/) 以供評估使用。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2026-01-17  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

---