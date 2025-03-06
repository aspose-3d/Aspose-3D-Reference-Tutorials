---
title: 連接四元數
linktitle: 連接四元數
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 場景中四元數操作的強大功能。學習逐步連接四元數以實現身臨其境的轉換。
weight: 11
url: /zh-hant/net/geometry-and-hierarchy/concatenate-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 連接四元數

## 介紹

歡迎來到這個關於使用 Aspose.3D for .NET 在 3D 場景中連接四元數的綜合教學！如果您是開發人員或 3D 愛好者，希望提高四元數操作技能，那麼您來對地方了。本教學將逐步引導您完成整個過程，確保順利的學習體驗。

## 先決條件

在深入學習本教程之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET 函式庫：從下列位置下載並安裝該函式庫：[阿斯普斯網站](https://releases.aspose.com/3d/net/).
- 開發環境：確保您有一個有效的 .NET 開發環境。

## 導入命名空間

在您的 .NET 專案中，包含必要的命名空間以利用 Aspose.3D 的強大功能：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
```

## 第 1 步：建立場景

首先使用 Aspose.3D 函式庫建立 3D 場景。該場景將作為四元數操作的畫布。

```csharp
Scene scene = new Scene();
```

## 第 2 步：定義四元數

定義三個四元數，`q1`, `q2`， 和`q3`，每個代表一個特定的旋轉。

```csharp
Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
Quaternion q3 = q1.Concat(q2);
```

## 第 3 步：建立圓柱體

創建三個圓柱體，每個圓柱體代表一個四元數。根據定義的四元數設定旋轉和平移屬性。

```csharp
Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.Transform.Rotation = q1;
cylinder.Transform.Translation = new Vector3(-5, 2, 0);

//對 q2 和 q3 重複
```

## 第 4 步：儲存到文件

將場景儲存到文件，指定輸出格式和檔案名稱。

```csharp
var output = "Your Output Directory" + "test_out.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

## 步驟5：顯示成功訊息

連接四元數並儲存檔案後，列印成功訊息以及檔案路徑。

```csharp
Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);
```

## 結論

恭喜！您已成功學習如何使用 Aspose.3D for .NET 在 3D 場景中連接四元數。嘗試不同的四元數組合，以在您的專案中實現獨特的轉換。

## 常見問題解答

### Q1：3D圖形中的四元數是什麼？

A1：四元數是用來表示 3D 空間中的旋轉的數學實體，與其他旋轉表示相比具有優勢。

### Q2：我可以將 Aspose.3D for .NET 與其他 .NET 函式庫一起使用嗎？

A2：是的，Aspose.3D for .NET 旨在與其他 .NET 程式庫無縫協作。

### 問題 3：Aspose.3D for .NET 是否有免費試用版？

A3：是的，您可以免費試用[這裡](https://releases.aspose.com/).

### 問題 4：如何獲得 Aspose.3D for .NET 支援？

 A4：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持和討論。

### Q5：我可以使用 Aspose.3D for .NET 的臨時授權嗎？

 A5：是的，您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
