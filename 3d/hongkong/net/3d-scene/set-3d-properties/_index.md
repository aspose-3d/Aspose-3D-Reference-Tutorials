---
date: 2026-01-17
description: 學習如何使用 Aspose.3D for .NET 列出材質屬性、變更漫反射顏色，並修改 3D 材質屬性。內含逐步程式碼範例。
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: 使用 Aspose.3D 列出 3D 場景中的材質屬性
url: /zh-hant/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 3D 場景中列出 Aspose.3D 的材質屬性

## Introduction

如果您需要**列出 3D 模型的材質屬性**，並且想要調整例如漫反射顏色等項目，您來對地方了。Aspose.3D for .NET 提供乾淨的物件導向 API，讓您在 C# 程式碼中檢視、取得與修改材質屬性。本教學將示範如何載入場景、列舉其材質屬性，並更改如漫反射成分等值，讓您的模型呈現理想外觀。

## Quick Answers
- **主要目標是什麼？** 列出材質屬性並修改它們（例如漫反射顏色）。  
- **需要哪個函式庫？** Aspose.3D for .NET。  
- **需要授權嗎？** 生產環境需使用臨時或正式授權。  
- **支援的檔案格式？** FBX、OBJ、STL、STL‑ASCII、3MF 等。  
- **一般實作時間？** 基本屬性列舉腳本約需 10‑15 分鐘。

## What is **list material properties**?
列出材質屬性是指遍歷材質的 `PropertyCollection`，讀取每個屬性名稱及其當前值。這對除錯、目視檢查，或建立讓使用者在執行時調整材質設定的 UI 控制項非常有用。

## Why use Aspose.3D to **access material properties**?
- **無需外部轉換器** – 直接使用原生 .NET 物件。  
- **豐富的屬性模型** – 除標準 PBR 值外，亦支援自訂的 FBX 專屬屬性。  
- **跨平台** – 可在 .NET Framework、.NET Core 以及 .NET 5/6+ 上執行。  

## Prerequisites

- 在專案中安裝 Aspose.3D for .NET。可於 [此處](https://releases.aspose.com/3d/net/) 下載。  
- 磁碟上用於存放 3‑D 原始檔案的資料夾（例如包含內嵌貼圖的 FBX 檔案）。

現在您已完成基本設定，讓我們深入程式碼吧。

## Import Namespaces

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

## Step 1: Load 3D Scene

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Step 2: **Access material properties** of the first node

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Step 3: **List material properties** – see every name/value pair

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Step 4: **How to change diffuse** – modify the Diffuse property

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Step 5: **Retrieve property by name** – get a strongly‑typed instance

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Step 6: Traverse a property's own properties (advanced)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## How to **change 3d material color** beyond diffuse
如果您需要影響高光、環境光或自發光顏色，只需將上方 `props["..."]` 指派中的 `"Diffuse"` 替換為 `"Specular"` 或 `"Ambient"`。`Vector3` 或 `Vector4` 結構同樣適用。

## Common Pitfalls & Tips
- **屬性名稱大小寫敏感** – Aspose.3D 的屬性鍵區分大小寫，請使用列舉輸出中顯示的完整名稱。  
- **屬性缺失** – 並非所有材質都公開每個 PBR 屬性。存取前請先檢查 `props.ContainsKey("Specular")`。  
- **儲存變更** – 修改屬性後，呼叫 `scene.Save("output.fbx");` 以寫入檔案。

## Conclusion

您現在已學會如何**列出材質屬性**、**依名稱取得屬性**，以及**變更漫反射顏色**（或其他任何材質屬性），使用 Aspose.3D for .NET。可嘗試不同屬性類型，以微調 3‑D 資產的外觀。

## FAQ's

### Q1: 我可以在 .NET 中使用 Aspose.3D 處理其他 3D 檔案格式嗎？

A1: 是的，Aspose.3D 支援多種 3D 檔案格式，包括 FBX、STL 等。

### Q2: 請前往 [此處](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

A2: 

### Q3: 有，您可在 [Aspose.3D 論壇](https://forum.aspose.com/c/3d/18) 找到支援與討論。

A3: 

### Q4: 請參考 [文件](https://reference.aspose.com/3d/net/) 取得完整說明。

A4: 

### Q5: 當然！下載 [免費試用版](https://releases.aspose.com/) 以探索功能。

A5: 

## Frequently Asked Questions

**問：`Vector3(1, 0, 1)` 代表什麼？**  
答：它將漫反射顏色設定為洋紅色（線性色彩空間中紅 = 1，綠 = 0，藍 = 1）。

**問：變更屬性後需要呼叫 `scene.Save` 嗎？**  
答：需要，儲存場景會將修改寫入磁碟；否則變更僅保留在記憶體中。

**問：我可以列舉自訂的 FBX 屬性嗎？**  
答：當然可以。`PropertyCollection` 會包含所有自訂屬性，您可透過 `GetProperty("customName")` 取得。

**問：有沒有辦法批次更新多個材質？**  
答：可遍歷 `scene.RootNode.ChildNodes`，對每個材質重複屬性修改步驟。

**問：Aspose.3D 支援 .NET 6 嗎？**  
答：支援，該函式庫與 .NET 6 及更高版本完全相容。

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}