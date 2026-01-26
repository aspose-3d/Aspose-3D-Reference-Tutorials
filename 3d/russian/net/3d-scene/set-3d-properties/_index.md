---
date: 2026-01-17
description: Узнайте, как перечислять свойства материалов, изменять диффузный цвет
  и модифицировать атрибуты 3D‑материалов с помощью Aspose.3D для .NET. Включены пошаговые
  примеры кода.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Список свойств материалов в 3D‑сценах с Aspose.3D
url: /ru/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Список свойств материалов в 3D‑сценах с Aspose.3D

## Introduction

Если вам нужно **list material properties** 3D‑модели и затем подправить такие параметры, как диффузный цвет, вы попали по адресу. Aspose.3D for .NET предоставляет чистый объектно‑ориентированный API, позволяющий инспектировать, получать и изменять атрибуты материалов, не выходя из кода C#. В этом руководстве мы пройдем процесс загрузки сцены, перечисления её свойств материалов и изменения значений, например диффузного компонента — чтобы вы могли задать моделям именно тот вид, который нужен.

## Quick Answers
- **What is the primary goal?** Список свойств материалов и их изменение (например, цвет диффузного отражения).  
- **Which library is required?** Aspose.3D for .NET.  
- **Do I need a license?** Требуется временная или полная лицензия для использования в продакшене.  
- **Supported file formats?** FBX, OBJ, STL, STL‑ASCII, 3MF и другие.  
- **Typical implementation time?** Около 10‑15 минут для базового скрипта перечисления свойств.

## What is **list material properties**?
Перечисление свойств материалов означает итерацию по `PropertyCollection` материала для чтения каждого имени свойства и его текущего значения. Это полезно для отладки, визуального осмотра или создания UI‑элементов, позволяющих пользователям менять настройки материала во время выполнения.

## Why use Aspose.3D to **access material properties**?
- **No external converters** – работа напрямую с нативными объектами .NET.  
- **Rich property model** – поддерживает пользовательские FBX‑специфические атрибуты в дополнение к стандартным PBR‑значениям.  
- **Cross‑platform** – работает на .NET Framework, .NET Core и .NET 5/6+.

## Prerequisites

- Aspose.3D for .NET установлен в вашем проекте. Скачайте его [здесь](https://releases.aspose.com/3d/net/).
- Папка на диске для хранения ваших 3‑D исходных файлов (например, файл FBX с встроенными текстурами).

Теперь, когда основы готовы, давайте перейдём к коду.

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
Если нужно изменить спекулярный, эмиссивный или амбиентный цвет, просто замените `"Diffuse"` на `"Specular"` или `"Ambient"` в присваивании `props["..."]` выше. Применяются те же структуры `Vector3` или `Vector4`.

## Common Pitfalls & Tips
- **Property name case‑sensitivity** – ключи свойств Aspose.3D чувствительны к регистру; используйте точное имя, отображаемое в выводе списка.  
- **Missing property** – не все материалы раскрывают каждый PBR‑атрибут. Проверьте `props.ContainsKey("Specular")` перед доступом.  
- **Saving changes** – после изменения свойств вызовите `scene.Save("output.fbx");` для сохранения изменений.

## Conclusion

Теперь вы знаете, как **list material properties**, **retrieve a property by name** и **change the diffuse color** (или любой другой атрибут материала) с помощью Aspose.3D for .NET. Экспериментируйте с различными типами свойств, чтобы точно настроить внешний вид ваших 3‑D активов.

## FAQ's

### Q1: Can I use Aspose.3D for .NET with other 3D file formats?

A1: Да, Aspose.3D поддерживает различные 3D‑форматы файлов, включая FBX, STL и многие другие.

### Q2: How can I obtain a temporary license for Aspose.3D for .NET?

A2: Посетите [здесь](https://purchase.aspose.com/temporary-license/) для получения временной лицензии.

### Q3: Is there a community forum for Aspose.3D users?

A3: Да, поддержка и обсуждения доступны на [форуме Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Where can I find detailed documentation for Aspose.3D for .NET?

A4: Обратитесь к [documentation](https://reference.aspose.com/3d/net/) для полного руководства.

### Q5: Can I try Aspose.3D for .NET for free before purchasing?

A5: Конечно! Скачайте [free trial version](https://releases.aspose.com/) для ознакомления с возможностями.

## Frequently Asked Questions

**Q: What does the `Vector3(1, 0, 1)` represent?**  
A: Он задаёт диффузный цвет магентой (red = 1, green = 0, blue = 1) в линейном цветовом пространстве.

**Q: Do I need to call `scene.Save` after changing properties?**  
A: Да, сохранение сцены записывает ваши изменения на диск; иначе изменения остаются только в памяти.

**Q: Can I enumerate custom FBX attributes?**  
A: Абсолютно. `PropertyCollection` будет включать любые пользовательские атрибуты, к которым можно обратиться через `GetProperty("customName")`.

**Q: Is there a way to batch‑update multiple materials?**  
A: Пройдитесь по `scene.RootNode.ChildNodes` и повторите шаги изменения свойств для каждого материала.

**Q: Does Aspose.3D support .NET 6?**  
A: Да, библиотека полностью совместима с .NET 6 и более новыми версиями.

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}