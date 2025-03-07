---
title: 使用 CancellationToken
linktitle: 使用 CancellationToken
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 建模的無縫世界。了解使用 CancellationToken 高效載入和儲存 3D 文件。
weight: 10
url: /zh-hant/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 CancellationToken

## 介紹

歡迎閱讀我們關於利用 Aspose.3D for .NET 來增強您的 3D 建模和渲染專案的綜合指南。 Aspose.3D 是一個功能強大的程式庫，可讓 .NET 開發人員無縫地處理 3D 檔案。在本教程中，我們將深入研究載入和儲存方面，特別關注如何使用 CancellationToken 來有效管理非同步任務。

## 先決條件

在我們開始這趟旅程之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET：從以下位置下載並安裝該程式庫[這裡](https://releases.aspose.com/3d/net/).
- .NET 環境：確保您設定了相容的 .NET 開發環境。
- 對 C# 的基本了解：建議熟悉 C# 程式語言。

## 導入命名空間

首先，請確保您的專案中包含必要的命名空間。這些命名空間將提供對 3D 檔案操作所需功能的存取。

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## 載入與儲存 - 使用 CancellationToken

### 第 1 步：建立 CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

在這裡，我們實例化一個 CancellationTokenSource，它是管理非同步操作中取消的關鍵元件。

### 第 2 步：初始化 3D 場景

```csharp
Scene scene = new Scene();
```

建立 Scene 類別的實例。這將成為您進行 3D 建模活動的畫布。

### 步驟 3： 設定 CancellationToken 逾時

```csharp
cts.CancelAfter(1000);
```

使用以下命令設定取消逾時`CancelAfter`方法。在此範例中，超時設定為 1000 毫秒（1 秒）。

### 第 4 步：開啟 3D 文檔

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

嘗試在指定的時間範圍內開啟 3D 文件。這`cts.Token`參數確保如果超過設定的超時時間可以取消操作。

### 步驟5：處理導入異常

如果出現 ImportException，請透過檢查它是否是由 OperationCanceledException 引起的來優雅地處理它。

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## 結論

恭喜！您已成功完成使用 Aspose.3D for .NET 和 CancellationToken 來管理 3D 文件載入的過程。此技術可確保高效、及時的導入操作，從而增強 3D 應用程式的整體效能。

## 常見問題解答

### Q1：Aspose.3D 是否相容於所有 3D 檔案格式？

 A1：Aspose.3D 支援多種 3D 檔案格式，包括 FBX、STL、OBJ 等。請參閱[文件](https://reference.aspose.com/3d/net/)取得完整清單。

### Q2：如何取得 Aspose.3D 的臨時授權？

 A2：透過訪問獲得臨時許可證[這個連結](https://purchase.aspose.com/temporary-license/).

### Q3：哪裡可以找到對 Aspose.3D 的支援？

A3：加入社區討論[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18).

### Q4：購買前可以免費試用Aspose.3D嗎？

 A4：是的，可以透過免費試用來探索功能[這裡](https://releases.aspose.com/).

### Q5：Aspose.3D for .NET 的最新版本是什麼？

 A5：查看最新信息[下載頁面](https://releases.aspose.com/3d/net/)取得最新版本。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
