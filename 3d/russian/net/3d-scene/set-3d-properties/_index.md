---
date: 2026-03-28
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

## Введение

Если вам нужно **перечислить свойства материалов** 3D‑модели и затем подправить такие параметры, как диффузный цвет, вы попали в нужное место. Aspose.3D for .NET предоставляет чистый, объектно‑ориентированный API, позволяющий инспектировать, получать и изменять атрибуты материалов, не покидая ваш C#‑код. В этом руководстве мы пройдем процесс загрузки сцены, перечисления её свойств материалов и изменения значений, таких как диффузный компонент, — чтобы вы могли задать моделям именно тот вид, который хотите.

## Быстрые ответы
- **Какова основная цель?** Перечислить свойства материалов и изменить их (например, диффузный цвет).  
- **Какая библиотека требуется?** Aspose.3D for .NET.  
- **Нужна ли лицензия?** Для использования в продакшене требуется временная или полная лицензия.  
- **Поддерживаемые форматы файлов?** FBX, OBJ, STL, STL‑ASCII, 3MF и другие.  
- **Типичное время реализации?** Около 10‑15 минут для базового скрипта перечисления свойств.

## Что такое **list material properties**?
Перечисление свойств материалов означает итерацию по `PropertyCollection` материала для чтения каждого имени свойства и его текущего значения. Это полезно для отладки, визуального осмотра или создания элементов управления UI, позволяющих пользователям изменять настройки материала во время выполнения.

## Почему использовать Aspose.3D для **access material properties**?
- **Нет внешних конвертеров** — работайте напрямую с нативными объектами .NET.  
- **Богатая модель свойств** — поддерживает пользовательские FBX‑специфические атрибуты в дополнение к стандартным PBR‑значениям.  
- **Кросс‑платформенный** — работает на .NET Framework, .NET Core и .NET 5/6+.

## Предварительные требования

- Aspose.3D for .NET установлен в вашем проекте. Скачайте его [здесь](https://releases.aspose.com/3d/net/).
- Папка на диске для хранения ваших 3‑D исходных файлов (например, FBX‑файл с встроенными текстурами).

Теперь, когда основы улажены, давайте погрузимся в код.

## Импорт пространств имён

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

## Шаг 1: Загрузка 3D‑сцены

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Шаг 2: **Access material properties** первого узла

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Шаг 3: **List material properties** — увидеть каждую пару имя/значение

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

## Шаг 4: **How to change diffuse** — изменить свойство Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Шаг 5: **Retrieve property by name** — получить строго типизированный экземпляр

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Шаг 6: Обход собственных свойств свойства (расширенно)

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

## Как **change 3d material color** за пределами диффузного
Если вам нужно изменить зеркальный, окружающий или излучающий цвета, просто замените `"Diffuse"` на `"Specular"` или `"Ambient"` в присваивании `props["..."]` выше. Применяются те же структуры `Vector3` или `Vector4`.

## Как **update material color in C#**
Изменение визуального вида материала сводится к обновлению соответствующего свойства в `PropertyCollection`. Независимо от того, хотите ли вы изменить диффузный, зеркальный или любой пользовательский цветовой атрибут, схема остаётся той же:

1. Получите свойство по его точному имени (чувствительно к регистру).  
2. Присвойте новое значение `Vector3` (RGB) или `Vector4` (RGBA).  

Поскольку API работает напрямую с объектами C#, вы можете **update material color C#** код без каких‑либо промежуточных файлов или конвертеров. Это делает его идеальным для редакторов в реальном времени или конвейеров пакетной обработки.

## Распространённые подводные камни и советы
- **Чувствительность к регистру имени свойства** — ключи свойств Aspose.3D чувствительны к регистру; используйте точное имя, показанное в выводе списка.  
- **Отсутствующее свойство** — не все материалы раскрывают каждый PBR‑атрибут. Проверьте `props.ContainsKey("Specular")` перед доступом.  
- **Сохранение изменений** — после изменения свойств вызовите `scene.Save("output.fbx");`, чтобы сохранить изменения.

## Заключение

Вы теперь знаете, как **перечислить свойства материалов**, **получить свойство по имени** и **изменить диффузный цвет** (или любой другой атрибут материала) с помощью Aspose.3D for .NET. Экспериментируйте с различными типами свойств, чтобы точно настроить внешний вид ваших 3‑D‑активов, и помните, что вы можете **update material color C#** всего одной строкой кода.

## Часто задаваемые вопросы

### Q1: Могу ли я использовать Aspose.3D for .NET с другими 3D‑форматами файлов?
A1: Да, Aspose.3D поддерживает различные 3D‑форматы файлов, включая FBX, STL и многие другие.

### Q2: Как получить временную лицензию для Aspose.3D for .NET?
A2: Перейдите [сюда](https://purchase.aspose.com/temporary-license/), чтобы получить временную лицензию.

### Q3: Есть ли сообщество‑форум для пользователей Aspose.3D?
A3: Да, поддержку и обсуждения можно найти на [форуме Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Где найти подробную документацию по Aspose.3D for .NET?
A4: Обратитесь к [документации](https://reference.aspose.com/3d/net/) для получения полной информации.

### Q5: Можно ли попробовать Aspose.3D for .NET бесплатно перед покупкой?
A5: Конечно! Скачайте [бесплатную пробную версию](https://releases.aspose.com/), чтобы ознакомиться с её возможностями.

## Часто задаваемые вопросы

**В: Что представляет собой `Vector3(1, 0, 1)`?**  
О: Он задаёт диффузный цвет магентой (красный = 1, зелёный = 0, синий = 1) в линейном цветовом пространстве.

**В: Нужно ли вызывать `scene.Save` после изменения свойств?**  
О: Да, сохранение сцены записывает ваши изменения на диск; иначе изменения остаются только в памяти.

**В: Могу ли я перечислить пользовательские атрибуты FBX?**  
О: Конечно. `PropertyCollection` будет включать любые пользовательские атрибуты, к которым можно получить доступ через `GetProperty("customName")`.

**В: Есть ли способ пакетно обновлять несколько материалов?**  
О: Пройдитесь по `scene.RootNode.ChildNodes` и повторите шаги изменения свойств для каждого материала.

**В: Поддерживает ли Aspose.3D .NET 6?**  
О: Да, библиотека полностью совместима с .NET 6 и более новыми версиями.

**Last Updated:** 2026-03-28  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}