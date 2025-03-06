---
title: 自訂載入選項
linktitle: 自訂載入選項
second_title: Aspose.3D .NET API
description: 探索 Aspose.3D for .NET 無縫 3D 模型載入和保存的終極解決方案。
weight: 15
url: /zh-hant/net/loading-and-saving/custom-load-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 自訂載入選項

## 介紹

歡迎來到 Aspose.3D for .NET 的世界——一個強大的程式庫，使開發人員能夠無縫地處理 3D 檔案。在本教程中，我們將深入研究載入和保存 3D 模型的複雜性，重點關注自訂載入選項。無論您是經驗豐富的開發人員還是新手，本指南都將逐步引導您完成整個過程，確保您充分利用 Aspose.3D for .NET 的全部潛力。

## 先決條件

在我們開始這趟旅程之前，請確保您具備以下先決條件：

-  Aspose.3D for .NET：確保您已安裝該程式庫。你可以下載它[這裡](https://releases.aspose.com/3d/net/).

- 文檔目錄：建立一個目錄來儲存 3D 模型檔案。

現在您已經掌握了必需的知識，讓我們深入了解 3D 模型操作的令人興奮的世界！

## 導入命名空間

首先，讓我們導入必要的名稱空間。這將為我們進入 Aspose.3D 領域奠定基礎。

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## 載入和儲存 - 自訂載入選項

### 第 1 步：載入 Discreet3DS 文件

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //設定自訂選項
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //使用載入選項載入文件
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### 步驟2：載入OBJ文件

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //設定自訂選項
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //使用載入選項載入文件
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### 第3步：載入STL文件

```csharp
private static void STLLoadOption()
{
    //文檔目錄的路徑。
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //設定自訂選項
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //使用載入選項載入文件
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### 第4步：載入U3D文件

```csharp
private static void U3DLoadOption()
{
    //文檔目錄的路徑。
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //設定自訂選項
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //使用載入選項載入文件
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### 第5步：載入glTF文件

```csharp
private static void glTFLoadOptions()
{
    //文檔目錄的路徑。
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //設定自訂選項
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### 第6步：載入PLY文件

```csharp
private static void PlyLoadOptions()
{
    //文檔目錄的路徑。
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //設定自訂選項
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### 第7步：載入FBX文件

```csharp
private static void FBXLoadOptions()
{
    //文檔目錄的路徑。
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //設定自訂選項
    scene.Open("test.FBX", opt);

    //FBX 檔案中 GlobalSettings 中定義的輸出屬性
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## 結論

恭喜！您已成功瀏覽使用 Aspose.3D for .NET 載入和儲存 3D 模型的複雜世界。本教學涵蓋了各種文件格式及其自訂載入選項，讓您輕鬆操作 3D 資源。

## 常見問題解答

### Q1：Aspose.3D for .NET適合初學者嗎？

A1：當然！ Aspose.3D for .NET 提供了使用者友善的介面，使各個層級的開發人員都可以使用它。

### Q2：我可以將Aspose.3D用於商業項目嗎？

A2：是的，Aspose.3D for .NET 附帶商業許可證，允許您在專案中使用它。

### Q3：支援的文件格式有限制嗎？

 A3：Aspose.3D for .NET 支援多種流行的 3D 檔案格式，包括 OBJ、STL、FBX 等。請參閱[文件](https://reference.aspose.com/3d/net/)以獲得完整的清單。

### Q4：有試用版嗎？

A4：是的，您可以透過下載 Aspose.3D for .NET 來探索 Aspose.3D for .NET 的功能[免費試用](https://releases.aspose.com/).

### Q5：在哪裡可以尋求 Aspose.3D for .NET 支援？

 A5：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區的支持和幫助。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
