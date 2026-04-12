---
date: 2026-04-12
description: 學習如何使用 Aspose.3D for .NET 將 PBR 材質套用於盒子、建立 PBR 材質，並以基於物理的渲染匯出 STL ASCII
  檔案。
keywords:
- how to apply pbr
- create pbr material
- export stl ascii
- physically based rendering
- create box mesh
linktitle: 將 PBR 材質套用至盒子
second_title: Aspose.3D .NET API
title: 如何將 PBR 材質套用到盒子上
url: /zh-hant/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何將 PBR 材質套用到盒子上

## 介紹

歡迎來到令人著迷的 3D 圖形世界！在本步驟教學中，**您將學習如何將 pbr** 材質套用到盒子上，使用 Aspose.3D for .NET。我們將逐步說明如何建立 PBR 材質、將其加入網格，最後**匯出 STL ASCII**，讓您能在任何後續工作流程中使用此模型。無論您是構建遊戲原型、產品可視化，或是 3D 列印的快速原型，掌握此工作流程即可在 .NET 應用程式中開啟逼真、基於物理的渲染 (PBR) 大門。

## 快速解答
- **主要目標是什麼？** 將 PBR 材質套用到盒子並匯出為 STL ASCII。  
- **使用哪個函式庫？** Aspose.3D for .NET (how to use aspose)。  
- **需要授權嗎？** 是的，生產環境需要臨時或完整授權。  
- **支援的輸出格式？** STL ASCII (export stl ascii) 以及其他多種 3D 格式。  
- **需要多久時間？** 基本實作大約需要 10‑15 分鐘。

## 什麼是 PBR 材質？

Physically Based Rendering (PBR) 是一種著色模型，模擬光線與真實世界表面的互動。透過調整金屬度與粗糙度等屬性，您可以在不手動調校複雜著色器的情況下，達到高度寫實的效果。

## 為什麼要使用 Physically Based Rendering (PBR)？

- **寫實性：** 材質對光線的反應符合真實物理。  
- **一致性：** 相同的材質在任何光照環境下都能正確呈現。  
- **效能：** 現代 GPU 已針對 PBR 計算進行最佳化，讓您免費獲得效能提升。

## 前置條件

在深入程式碼之前，請確保您已具備以下條件：

### 下載與安裝 Aspose.3D for .NET

前往 [Aspose.3D for .NET 文件](https://reference.aspose.com/3d/net/) 取得下載與安裝函式庫的詳細說明。

### 取得授權

為了發揮 Aspose.3D 的全部功能，請取得有效授權。您可以在[此處](https://purchase.aspose.com/temporary-license/)取得臨時授權，或在[此處](https://purchase.aspose.com/buy)購買完整授權。

## 匯入命名空間

首先，請確保匯入必要的命名空間，以利用 Aspose.3D for .NET 的功能：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 步驟說明

### 步驟 1：初始化場景

首先建立一個空的 3D 場景。此容器將容納您之後加入的所有幾何、材質與光源。

```csharp
Scene scene = new Scene();
```

### 步驟 2：建立 PBR 材質

現在我們**建立 pbr 材質**，為盒子賦予寫實外觀。`PbrMaterial` 類別提供了實作基於物理渲染所需的全部參數。

```csharp
PbrMaterial mat = new PbrMaterial();
```

### 步驟 3：設定材質屬性

微調材質屬性。在此範例中，我們將表面設定為接近金屬且相當粗糙——非常適合刷紋金屬盒子。

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

### 步驟 4：建立盒子網格

產生簡單的盒子幾何。這就是**建立盒子網格**的步驟，也是主要關鍵字所指的內容。

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

### 步驟 5：將 PBR 材質套用到盒子上

將先前設定好的**add pbr material** 指派給剛建立的盒子節點。

```csharp
boxNode.Material = mat;
```

### 步驟 6：匯出 STL ASCII（如何匯出 STL）

最後，**export stl ascii**，讓模型能在任何標準 3D 檢視器或切片軟體中開啟。使用 `FileFormat.STLASCII` 可確保檔案為人類可讀的格式。

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

## 常見陷阱與技巧
- **未找到授權檔案：** 確保在任何 Aspose 呼叫*之前*載入授權檔案；否則函式庫會以評估模式運行。  
- **檔案路徑錯誤：** 使用 `Path.Combine` 以避免在不同作業系統上缺少路徑分隔符。  
- **粗糙度與金屬度平衡：** 兩者同時設定過高會使表面看起來平坦；請在 `0.5‑0.9` 之間嘗試，以取得平衡外觀。  
- **效能提示：** 若需將相同材質套用至多個網格，請重複使用單一 `PbrMaterial` 實例；可減少記憶體開銷。

## 常見問與答

**Q1：Aspose.3D 是否相容其他 3D 檔案格式？**  
A1：是的，Aspose.3D 支援多種 3D 檔案格式，確保您的專案具備彈性。

**Q2：我可以在商業應用中使用 Aspose.3D 嗎？**  
A2：當然可以！Aspose.3D 提供商業授權，讓您能無縫整合至生產軟體中。

**Q3：是否提供試用版？**  
A3：是的，您可透過下載免費試用版[此處](https://releases.aspose.com/)來探索 Aspose.3D 的功能。

**Q4：在哪裡可以找到社群支援與討論？**  
A4：加入 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 以獲得支援與討論。

**Q5：如何取得 Aspose.3D 的臨時授權？**  
A5：您可在[此處](https://purchase.aspose.com/temporary-license/)取得臨時授權以供評估使用。

## 結論

使用 Aspose.3D for .NET 進入 3D 圖形領域，為您開啟無盡的創意可能性。憑藉直觀的 API 與強大的功能，打造視覺震撼的場景成為開發者的愉快體驗。既然您已了解**如何將 pbr** 材質套用到盒子並**匯出 STL ASCII**，不妨將盒子換成更複雜的網格，或嘗試使用貼圖，以觀察光照即時的反應。

---

**最後更新：** 2026-04-12  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}