---
date: 2026-01-07
description: Узнайте, как добавить плоскость основания при выполнении линейной экструзии
  с помощью Aspose.3D для .NET и экспортировать файлы Wavefront OBJ. Овладейте техниками
  центрирования и размещения модели на плоскости в 3‑D‑моделировании.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Добавить плоскость основания и центр в линейной экструзии
url: /ru/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Добавление плоскости основания и центрирование при линейной экструзии

## Introduction

Добро пожаловать в это подробное руководство по освоению линейной экструзии с использованием Aspose.3D for .NET. Если вы хотите **добавить плоскость основания** к вашим моделям и **экспортировать файлы Wavefront OBJ**, при этом сохранив экструзию центрированной, вы попали по адресу. В этом уроке мы подробно рассмотрим технику линейной экструзии, сосредоточив внимание на центрировании и том, как плоскость основания помогает лучше визуализировать результат.

## Quick Answers
- **Что даёт “add ground plane”?** Это предоставляет визуальную ссылку, позволяющую легко увидеть, где экструзия располагается на плоскости X‑Z.  
- **В каком формате экспортируется модель?** Сцена сохраняется как файл Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **Нужна ли лицензия для запуска кода?** Бесплатная пробная версия подходит для разработки; для продакшн‑использования требуется постоянная лицензия.  
- **Можно ли изменить длину экструзии?** Да — измените второй параметр `LinearExtrusion`.  
- **Является ли центрирование опциональным?** Установка `Center = true` центрирует экструзию относительно профиля; `false` выравнивает её к одной стороне.

## Prerequisites

Прежде чем начать, убедитесь, что у вас есть следующие предварительные условия:

- Базовое понимание языка программирования C#.  
- Установленная Visual Studio на вашем компьютере.  
- Библиотека Aspose.3D for .NET, которую можно скачать из [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Доступ к [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) для справки в течение всего урока.

## Import Namespaces

Чтобы начать, импортируем необходимые пространства имён. Они станут фундаментом для нашего шедевра 3D‑моделирования.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step 1: Initialize the Base Profile

Мы начинаем с определения прямоугольного профиля, который будет экструдирован. Параметр `RoundingRadius` добавляет лёгкое скругление углов.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Step 2: Create a 3D Scene

Объект `Scene` служит контейнером для всей геометрии, источников света и камер.

```csharp
Scene scene = new Scene();
```

## Step 3: Create Left and Right Nodes

Создаём два дочерних узла под корневым. Один продемонстрирует экструзию **без** центрирования, другой — **с** центрированием. Мы также смещаем левый узел, чтобы два примера не перекрывались.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Step 4: Perform Linear Extrusion on Left Node (No Center)

Здесь мы экструдируем профиль без центрирования. Обратите внимание на флаг `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Step 5: Add Ground Plane for Reference (Left Node)

Добавление тонкого бокса выступает в роли **ground plane**, чтобы вы чётко видели, как экструзия располагается на основе.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Step 6: Perform Linear Extrusion on Right Node (With Center)

Теперь мы экструдируем тот же профиль, но включаем центрирование. Геометрия будет симметрично расположена вокруг начала координат профиля.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Step 7: Add Ground Plane for Reference (Right Node)

Второй ground plane добавляется к правому узлу, чтобы визуальное сравнение оставалось согласованным.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Step 8: Export Wavefront OBJ File

Наконец, мы **export Wavefront OBJ**, чтобы результат можно было открыть в любом стандартном 3‑D‑просмотрщике.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Why Add a Ground Plane?

Добавление плоскости основания даёт мгновенную визуальную подсказку о высоте и выравнивании экструзии. Это особенно полезно, когда нужно сравнить центрированные и нецентрированные результаты, как показано в этом уроке.

## Common Issues & Tips

- **Ground plane not visible:** Убедитесь, что толщина плоскости (`0.01` в конструкторе `Box`) достаточно мала, чтобы не скрывать экструзию, но достаточно велика, чтобы быть отрисованной.  
- **Export fails:** Проверьте, существует ли выходной каталог и есть ли у вас права на запись.  
- **Centered extrusion appears offset:** Дважды проверьте свойство `Center`; `true` центрирует профиль, `false` выравнивает его к одной стороне.

## Frequently Asked Questions

### Q1: Can I use Aspose.3D for .NET with other programming languages?

A1: Aspose.3D primarily supports .NET languages such as C# and VB.NET.

### Q2: Where can I find support for Aspose.3D-related queries?

A2: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for dedicated support and discussions.

### Q3: Is there a free trial available for Aspose.3D for .NET?

A3: Yes, you can access the free trial [here](https://releases.aspose.com/).

### Q4: How can I obtain a temporary license for Aspose.3D for .NET?

A4: You can acquire a temporary license [here](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I purchase the Aspose.3D for .NET license?

A5: Purchase your license [here](https://purchase.aspose.com/buy).

### Q6: Can I export the scene to other formats besides OBJ?

A6: Yes, Aspose.3D supports many formats such as STL, FBX, and GLTF. Simply change the `FileFormat` enum value in the `Save` method.

### Q7: How do I change the extrusion’s number of slices?

A7: Adjust the `Slices` property in the `LinearExtrusion` constructor to control mesh density.

---

**Last Updated:** 2026-01-07  
**Tested With:** Aspose.3D for .NET latest version  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}