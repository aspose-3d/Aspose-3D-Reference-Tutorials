---
date: 2026-03-28
description: 學習如何使用 Aspose.3D for .NET 列出材質屬性、變更漫反射顏色，以及修改 3D 材質屬性，並附有逐步程式碼範例。
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

## 簡介

如果你需要 **列出材質屬性** 的 3D 模型，並且想要調整例如漫反射顏色等設定，你來對地方了。Aspose.3D for .NET 為你提供乾淨、物件導向的 API，讓你在 C# 程式碼中即可檢查、取得與修改材質屬性。於本教學中，我們將示範如何載入場景、列舉其材質屬性，並變更例如漫反射成分的值——讓你的模型呈現精確的外觀。

## 快速解答
- **主要目標是什麼？** 列出材質屬性並修改它們（例如漫反射顏色）。  
- **需要哪個函式庫？** Aspose.3D for .NET。  
- **需要授權嗎？** 生產環境使用需臨時或正式授權。  
- **支援的檔案格式？** FBX、OBJ、STL、STL‑ASCII、3MF 等。  
- **典型實作時間？** 基本屬性列舉腳本約需 10‑15 分鐘。

## 什麼是 **列出材質屬性**？

列出材質屬性是指遍歷材質的 `PropertyCollection`，讀取每個屬性名稱及其當前值。這對除錯、視覺檢查，或建立允許使用者在執行時調整材質設定的 UI 控制項非常有用。

## 為什麼使用 Aspose.3D 來 **存取材質屬性**？

- **無需外部轉換器** – 直接使用原生 .NET 物件。  
- **豐富的屬性模型** – 支援自訂 FBX 專屬屬性以及標準 PBR 值。  
- **跨平台** – 支援 .NET Framework、.NET Core 以及 .NET 5/6+。

## 先決條件

- Aspose.3D for .NET 已安裝於你的專案中。請於 [here](https://releases.aspose.com/3d/net/) 下載。  
- 一個磁碟上的資料夾，用來存放你的 3‑D 原始檔案（例如包含內嵌貼圖的 FBX 檔）。

既然已完成基礎設定，讓我們深入程式碼吧。

## 匯入命名空間

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

## 步驟 1：載入 3D 場景

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## 步驟 2：**存取材質屬性** 的第一個節點

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## 步驟 3：**列出材質屬性** – 查看每個名稱/值配對

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

## 步驟 4：**如何變更漫反射** – 修改 Diffuse 屬性

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## 步驟 5：**依名稱取得屬性** – 獲得強型別實例

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## 步驟 6：遍歷屬性的子屬性（進階）

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

## 如何 **變更 3D 材質顏色** 超出漫反射

如果你需要影響高光、環境光或自發光顏色，只需在上述 `props["..."]` 賦值中將 `"Diffuse"` 替換為 `"Specular"` 或 `"Ambient"`。同樣的 `Vector3` 或 `Vector4` 結構皆適用。

## 如何 **在 C# 中更新材質顏色**

改變材質的視覺外觀歸結為在 `PropertyCollection` 中更新相應的屬性。無論你想修改漫反射、高光或任何自訂顏色屬性，步驟皆相同：

1. 依確切名稱（區分大小寫）取得屬性。  
2. 指派新的 `Vector3`（RGB）或 `Vector4`（RGBA）值。  

由於 API 直接操作 C# 物件，你可以在 **update material color C#** 程式碼中更新材質顏色，而不需任何中間檔案或轉換器。這使其非常適合即時編輯器或批次處理流程。

## 常見陷阱與技巧
- **屬性名稱大小寫敏感** – Aspose.3D 的屬性鍵區分大小寫；請使用列舉輸出中顯示的精確名稱。  
- **缺少屬性** – 並非所有材質都公開每個 PBR 屬性。存取前請先檢查 `props.ContainsKey("Specular")`。  
- **儲存變更** – 修改屬性後，呼叫 `scene.Save("output.fbx");` 以永久保存變更。

## 結論

你現在已學會如何 **列出材質屬性**、**依名稱取得屬性**，以及使用 Aspose.3D for .NET **變更漫反射顏色**（或任何其他材質屬性）。嘗試不同的屬性類型以微調 3‑D 資產的外觀，並記得只需一行程式碼即可 **update material color C#**。

## 常見問答

### Q1：我可以在 Aspose.3D for .NET 中使用其他 3D 檔案格式嗎？

A1：是的，Aspose.3D 支援多種 3D 檔案格式，包括 FBX、STL 等等。

### Q2：我該如何取得 Aspose.3D for .NET 的臨時授權？

A2：請前往 [here](https://purchase.aspose.com/temporary-license/) 取得臨時授權。

### Q3：是否有 Aspose.3D 使用者的社群論壇？

A3：是的，你可以在 [Aspose.3D forum](https://forum.aspose.com/c/3d/18) 找到支援與討論。

### Q4：在哪裡可以找到 Aspose.3D for .NET 的詳細文件？

A4：請參考 [documentation](https://reference.aspose.com/3d/net/) 以獲得完整指引。

### Q5：我可以在購買前免費試用 Aspose.3D for .NET 嗎？

A5：當然可以！下載 [free trial version](https://releases.aspose.com/) 以體驗其功能。

## 常見問題

**Q：`Vector3(1, 0, 1)` 代表什麼？**  
A：它將漫反射顏色設定為洋紅色（紅 = 1，綠 = 0，藍 = 1），使用線性色彩空間。

**Q：變更屬性後需要呼叫 `scene.Save` 嗎？**  
A：需要，將場景保存會把修改寫入磁碟；否則變更僅保留在記憶體中。

**Q：我可以列舉自訂的 FBX 屬性嗎？**  
A：當然可以。`PropertyCollection` 會包含所有自訂屬性，你可以透過 `GetProperty("customName")` 取得。

**Q：有沒有方法批次更新多個材質？**  
A：遍歷 `scene.RootNode.ChildNodes`，對每個材質重複屬性修改步驟即可。

**Q：Aspose.3D 支援 .NET 6 嗎？**  
A：支援，該函式庫完全相容於 .NET 6 及更高版本。

---

**最後更新：** 2026-03-28  
**測試環境：** Aspose.3D 24.11 for .NET  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}