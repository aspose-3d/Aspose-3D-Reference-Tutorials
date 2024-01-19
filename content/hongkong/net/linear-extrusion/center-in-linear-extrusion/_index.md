---
title: 線性擠壓中心
linktitle: 線性擠壓中心
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 建模世界。集中線性擠壓技術，創造令人驚嘆的設計，並釋放您的創造力。
type: docs
weight: 10
url: /zh-hant/net/linear-extrusion/center-in-linear-extrusion/
---
## 介紹

歡迎閱讀這份關於使用 Aspose.3D for .NET 掌握線性擠出的綜合指南。如果您希望提高 3D 建模技能並創建令人驚嘆的擠壓件，那麼您來對地方了。在本教程中，我們將深入研究線性擠出技術，特別關注居中方面，將您的設計提升到一個全新的水平。

## 先決條件

在我們踏上這趟令人興奮的旅程之前，請確保您具備以下先決條件：

- 對 C# 程式語言有基本了解。
- Visual Studio 安裝在您的電腦上。
-  Aspose.3D for .NET 函式庫，您可以從[Aspose.3D .NET 文檔](https://reference.aspose.com/3d/net/).
- 確保您有權訪問[Aspose.3D .NET 文檔](https://reference.aspose.com/3d/net/)供整個教學參考。

## 導入命名空間

首先，讓我們導入必要的命名空間。這些將為我們的 3D 建模傑作奠定基礎。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 第 1 步：初始化基本設定檔

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 第 2 步：建立 3D 場景

```csharp
Scene scene = new Scene();
```

## 第三步：建立左右節點

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## 第四步：對左節點進行線性擠壓

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## 步驟 5：設定參考地平面

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## 第6步：對右側節點進行線性擠壓

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## 步驟 7：設定參考地平面（右節點）

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## 第 8 步：儲存 3D 場景

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 結論

恭喜！您已經成功掌握了使用 Aspose.3D for .NET 進行居中線性擠出的藝術。請隨意嘗試不同的參數並探索該技術提供的巨大可能性。

## 常見問題解答

### Q1：我可以將 Aspose.3D for .NET 與其他程式語言一起使用嗎？

A1：Aspose.3D主要支援.NET語言，例如C#和VB.NET。

### Q2：在哪裡可以找到 Aspose.3D 相關查詢的支援？

 A2：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)專門的支援和討論。

### 問題 3：Aspose.3D for .NET 是否有免費試用版？

 A3：是的，您可以免費試用[這裡](https://releases.aspose.com/).

### Q4：如何取得 Aspose.3D for .NET 的臨時授權？

A4：您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).

### Q5: 在哪裡可以購買 Aspose.3D for .NET 授權？

 A5：購買您的許可證[這裡](https://purchase.aspose.com/buy).
