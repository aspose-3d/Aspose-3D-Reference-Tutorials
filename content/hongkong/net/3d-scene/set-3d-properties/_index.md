---
title: 在 3D 場景中設定三維屬性
linktitle: 在 3D 場景中設定三維屬性
second_title: Aspose.3D .NET API
description: 探索設定 3D 屬性的 Aspose.3D for .NET 教學。透過程式碼範例逐步學習。提升您的 3D 場景操作技能。
type: docs
weight: 14
url: /zh-hant/net/3d-scene/set-3d-properties/
---
## 介紹

創建迷人的三維場景通常需要能夠操縱各種屬性，為您的項目添加深度和真實感。 Aspose.3D for .NET 提供了強大的工具集來實現此目的，讓您可以輕鬆地在 3D 場景中設定和修改三維屬性。在本教程中，我們將逐步探索該過程，增強您對如何有效利用 Aspose.3D for .NET 的理解。

## 先決條件

在深入學習本教程之前，請確保您符合以下先決條件：

-  Aspose.3D for .NET：請確定您已在 .NET 專案中安裝了該程式庫。你可以下載它[這裡](https://releases.aspose.com/3d/net/).

- 文件目錄：建立一個目錄來儲存您的 3D 文件。

現在您已經掌握了重點，讓我們探索使用 Aspose.3D for .NET 在 3D 場景中設定三維屬性的過程。

## 導入命名空間

首先，將必要的命名空間匯入到您的專案中。這些命名空間提供了在 Aspose.3D for .NET 中處理三維屬性所需的類別和方法。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 第 1 步：載入 3D 場景

首先載入 3D 場景。在此範例中，我們使用帶有嵌入紋理的 FBX 檔案。

```csharp
//ExStart：載入3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd：載入3DScene
```

## 第 2 步：存取材料屬性

存取載入的 3D 場景的材質屬性以操縱其特性。

```csharp
//ExStart：存取材料屬性
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//結束：存取材料屬性
```

## 第 3 步：列出所有屬性

使用 foreach 迴圈或序數 for 迴圈列出材質的所有屬性。

```csharp
//ExStart：列出所有屬性
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//或使用序數 for 迴圈
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//結束：列出所有屬性
```

## 步驟 4：按名稱取得和修改屬性

按名稱檢索和修改特定屬性。

```csharp
//ExStart：GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//按名稱修改屬性值
props["Diffuse"] = new Vector3(1, 0, 1);
//結束：GetModifyPropertyByName
```

## 步驟5：按名稱取得屬性實例

按名稱檢索屬性實例以進行進一步操作。

```csharp
//ExStart：GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//結束：按名稱取得屬性實例
```

## 第6步：遍歷Property的屬性

自從`Property`繼承自`A3DObject`，可以遍歷一個屬性的屬性。

```csharp
//ExStart：TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//以及一些僅在 FBX 檔案中定義的屬性：
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//可以遍歷財產的財產
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//結束：TraverseProperty屬性
```

## 結論

恭喜！現在您已經掌握了使用 Aspose.3D for .NET 在 3D 場景中設定三維屬性的藝術。嘗試不同的屬性和值，讓您的 3D 專案栩栩如生。

## 常見問題解答

### Q1：我可以將 Aspose.3D for .NET 與其他 3D 檔案格式一起使用嗎？

A1：是的，Aspose.3D 支援各種 3D 檔案格式，包括 FBX、STL 等等。

### Q2：如何取得 Aspose.3D for .NET 的臨時授權？

 A2：參觀[這裡](https://purchase.aspose.com/temporary-license/)獲得臨時許可證。

### Q3：有 Aspose.3D 用戶的社群論壇嗎？

 A3：是的，您可以在以下位置找到支持和討論：[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18).

### Q4：在哪裡可以找到 Aspose.3D for .NET 的詳細文件？

 A4：請參閱[文件](https://reference.aspose.com/3d/net/)進行全面指導。

### Q5：我可以在購買前免費試用 Aspose.3D for .NET 嗎？

 A5：當然！下載[免費試用版](https://releases.aspose.com/)來探索它的特點。
