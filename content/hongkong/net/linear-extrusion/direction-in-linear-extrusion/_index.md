---
title: 線性擠出方向
linktitle: 線性擠出方向
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 開啟 3D 建模世界。學習方向線性擠壓、提高創造力並輕鬆製作沉浸式應用程式。
type: docs
weight: 11
url: /zh-hant/net/linear-extrusion/direction-in-linear-extrusion/
---
## 介紹

在軟體開發的動態世界中，創建沉浸式 3D 模型是一項不可或缺的技能。 Aspose.3D for .NET 為開發人員提供了一組強大的工具，以在其應用程式中發揮 3D 建模的潛力。在本教程中，我們將深入研究線性擠出的有趣世界，並探索「線性擠出方向」功能的細微差別。

## 先決條件

在我們踏上這趟令人興奮的旅程之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET：從以下位置下載並安裝該程式庫[Aspose.3D .NET 文檔](https://reference.aspose.com/3d/net/).

- 開發環境：確保您已設定有效的 .NET 開發環境。

## 導入命名空間

在您的 .NET 專案中，匯入必要的命名空間以存取 Aspose.3D 的功能。將以下行加入程式碼的開頭：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 第 1 步：初始化基本設定檔

首先初始化要拉伸的基礎輪廓。在此範例中，我們建立一個圓角半徑為 0.3 的矩形。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 第 2 步：建立 3D 場景

透過創建場景為您的 3D 傑作奠定基礎。

```csharp
Scene scene = new Scene();
```

## 第三步：建立節點

在場景中產生節點來表示 3D 環境的不同元件。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## 第四步：無方向線性擠壓

使用以下命令對左側節點執行線性擠壓`Twist`和`Slices`特性。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## 步驟5：帶方向的線性擠壓

透過結合擴展擠出能力`Direction`屬性在右節點。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## 第 6 步：儲存 3D 場景

透過儲存 3D 場景來保留您的創作。代替`"Your Output Directory"`與所需的目錄。

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

恭喜！您已經使用 Aspose.3D for .NET 成功實現了線性擠出，並探索了傳統方法和定向方法。

## 結論

在本教程中，我們使用 Aspose.3D for .NET 瀏覽了 3D 建模的迷人領域。線性擠壓，無論有沒有方向，都為尋求創建視覺上令人驚嘆的應用程式的開發人員提供了無限的可能性。借助 Aspose.3D，3D 建模的力量觸手可及。

## 常見問題解答

### Q1：如何取得 Aspose.3D for .NET 的臨時授權？

 A1：參觀[申請臨時許可證](https://purchase.aspose.com/temporary-license/)獲得臨時許可證。

### Q2：在哪裡可以找到對 Aspose.3D 的支援？

 A2：加入[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)尋求協助並與社區建立聯繫。

### Q3：有免費試用嗎？

 A3：是的，透過免費試用探索這些功能[Aspose.3D 發布](https://releases.aspose.com/).

### Q4：如何購買 Aspose.3D for .NET？

 A4：導航至[Aspose 購買頁面](https://purchase.aspose.com/buy)了解許可選項和購買詳細資訊。

### Q5：在哪裡可以找到 Aspose.3D for .NET 的詳細文件？

 A5：參考綜合[Aspose.3D .NET 文檔](https://reference.aspose.com/3d/net/)以獲得深入的資訊。