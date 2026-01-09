---
date: 2026-01-09
description: 學習如何使用 Aspose.3D for .NET 建立 3D 場景並儲存 3D 模型，包括匯出 Wavefront OBJ 以及線性擠出切片。
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: 創建帶有線性擠出切片的 3D 場景
url: /zh-hant/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 建立 3D 場景與線性擠出切片

## 介紹

歡迎來到使用 Aspose.3D for .NET 的 3D 設計世界！在本教學中，您將 **create 3d scene** 物件、套用自訂切片數量的線性擠出，最後 **save 3d model** 為 Wavefront OBJ 檔案。無論您是建立快速原型或是生產級的可視化，以下步驟將向您展示 **how to use Aspose** 直接從 C# 產生高品質幾何體。

## 快速解答
- **What does “create 3d scene” mean?** 它表示建立一個 Scene 物件，用來保存所有 3D 實體（網格、光源、相機）。  
- **Which format is used for export?** 範例匯出為 **Wavefront OBJ** (`export wavefront obj`).  
- **How many slices can I set?** 您可以設定任意整數；示範中顯示 2 與 10 個切片。  
- **Do I need a license?** 生產環境需要臨時或正式授權。  
- **Can I run this on .NET Core?** 可以，Aspose.3D 支援 .NET Framework 與 .NET Core。

## 前置條件

在深入 Aspose.3D 的 3D 設計世界之前，請確保您具備以下前置條件：

- Aspose.3D for .NET Library：確保已安裝 Aspose.3D 函式庫。您可從 [here](https://releases.aspose.com/3d/net/) 下載。
- Integrated Development Environment (IDE)：使用任何相容 .NET 開發的 IDE。
- Basic Understanding of C#：熟悉 C# 程式語言的基礎概念。
- Desire to Explore 3D Design：對打造視覺驚豔的 3D 模型充滿熱情！

## 匯入命名空間

要開始使用 Aspose.3D 進行 3D 設計，您需要匯入必要的命名空間。這可確保程式碼能存取所需的類別與功能。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 如何使用線性擠出建立 3D 場景

以下我們將逐步說明建立場景、套用擠出，並 **save 3d model** 為 OBJ 檔案的每個步驟。說明採對話式語氣，讓您輕鬆跟隨。

### 步驟 1：初始化基礎輪廓

首先，我們定義將被擠出的 2‑D 形狀。本例為帶圓角的矩形。

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### 步驟 2：建立 3D 場景

`Scene` 物件是所有幾何、光源與相機的容器——**creating a 3d scene** 的核心。

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### 步驟 3：建立左側與右側節點

我們在場景根節點下加入兩個子節點。一個使用較低的切片數，另一個使用較高的切片數，以便觀察視覺差異。

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### 步驟 4：對左側節點執行線性擠出

此處我們以 **2 slices** 擠出矩形。較少的切片會產生較粗糙的外觀。

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### 步驟 5：對右側節點執行線性擠出

現在我們以 **10 slices** 擠出相同的輪廓，產生更平滑的表面。

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### 步驟 6：儲存 3D 場景

最後，我們將場景匯出為 Wavefront OBJ 檔案。此示範 **how to save obj** 與 **export wavefront obj** 的使用方式，透過 Aspose.3D。

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## 常見問題與解決方案

| 問題 | 為何發生 | 解決方式 |
|------|----------|----------|
| OBJ 檔案為空 | 輸出路徑不正確或缺少寫入權限。 | 確認目錄存在且應用程式具有寫入權限。 |
| 切片未影響平滑度 | `Slices` 值對於該幾何尺寸而言過低。 | 增加切片數量或調整輪廓尺寸。 |
| 授權例外 | 在非試用版環境下未使用有效授權執行。 | 使用 `License license = new License(); license.SetLicense("Aspose.3D.lic");` 申請臨時或永久授權。 |

## 常見問答

**Q: 我可以將 Aspose.3D for .NET 與其他程式語言一起使用嗎？**  
A: Aspose.3D 主要設計給 .NET 使用，但您可以透過 .NET 綁定探索與 Python 等語言的互操作性選項。

**Q: 我在哪裡可以找到 Aspose.3D for .NET 的詳細文件？**  
A: 請參考文件 [here](https://reference.aspose.com/3d/net/)，了解 Aspose.3D 功能與使用方式的深入資訊。

**Q: Aspose.3D for .NET 有提供免費試用嗎？**  
A: 有，您可在 [here](https://releases.aspose.com/) 取得免費試用，先行探索函式庫功能再決定購買。

**Q: 我要如何取得 Aspose.3D for .NET 的技術支援？**  
A: 前往 Aspose.3D 論壇 [here](https://forum.aspose.com/c/3d/18) 尋求協助並與社群互動。

**Q: 我可以為 Aspose.3D for .NET 使用臨時授權嗎？**  
A: 可以，請在 [here](https://purchase.aspose.com/temporary-license/) 取得臨時授權以供評估使用。

## 結論

恭喜！您已成功學會如何 **create 3d scene**、以自訂切片數量套用線性擠出，並使用 Aspose.3D for .NET **save 3d model** 為 Wavefront OBJ 檔案。這只是您 3D 設計之旅的起點——歡迎嘗試不同的輪廓、切片值與匯出格式，以發揮 **3d modeling c#** 的完整潛力。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2026-01-09  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose