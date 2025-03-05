---
title: Захват видовых экранов в 3D-сценах
linktitle: Захват видовых экранов в 3D-сценах
second_title: Aspose.3D .NET API
description: Научитесь захватывать потрясающие 3D-окна просмотра с помощью Aspose.3D для .NET. Пошаговое руководство по гибкому рендерингу сцен.
type: docs
weight: 11
url: /ru/net/rendering/capture-viewport/
---
## Введение

В сфере 3D-графики и визуализации захват видовых экранов является важным навыком, который повышает глубину и детализацию ваших сцен. Aspose.3D для .NET предоставляет надежное решение для рендеринга и управления 3D-сценами. Это руководство проведет вас через процесс захвата видовых экранов в 3D-сценах с помощью Aspose.3D, что позволит вам с легкостью создавать потрясающие визуализации.

## Предварительные условия

Прежде чем приступить к изучению руководства, убедитесь, что у вас есть следующие предварительные условия:

-  Библиотека Aspose.3D для .NET: убедитесь, что у вас установлена библиотека Aspose.3D. Вы можете скачать его с[здесь](https://releases.aspose.com/3d/net/).

## Импортировать пространства имен

Для начала импортируйте необходимые пространства имен в свой проект .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Шаг 1. Загрузите существующую 3D-сцену

Начните с загрузки существующей 3D-сцены в свой проект. Следующий фрагмент кода демонстрирует это:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Шаг 2: Создайте камеру

Затем создайте экземпляр камеры и установите ее положение и цель:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Шаг 3: Добавьте освещение в сцену

Улучшите свою сцену, добавив источник света. В приведенном ниже фрагменте кода показано, как создать точечный источник света:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Шаг 4. Настройте средство рендеринга и цель рендеринга

Настройте рендерер и создайте цель рендеринга для захвата сцены:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (продолжение в следующих шагах)
    }
}
```

## Шаг 5: Определите видовые экраны и рендеринг

Определите области просмотра и визуализируйте сцену для создания выходных изображений:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Шаг 6. Измените видовые экраны и повторите рендеринг

Измените области просмотра и повторите рендеринг сцены, демонстрируя гибкость Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Продолжайте экспериментировать с различными конфигурациями для достижения желаемых визуальных эффектов.

## Заключение

В этом уроке мы рассмотрели процесс захвата областей просмотра в 3D-сценах с использованием Aspose.3D для .NET. Используя его мощные функции, вы можете поднять свои проекты 3D-графики на новую высоту, обеспечив захватывающие визуальные впечатления.

## Часто задаваемые вопросы

### Вопрос 1: Совместим ли Aspose.3D с другими форматами 3D-файлов?

О1: Да, Aspose.3D поддерживает различные форматы 3D-файлов, обеспечивая совместимость с широким спектром инструментов проектирования.

### Вопрос 2: Могу ли я использовать Aspose.3D для разработки игр?

О2: Хотя Aspose.3D в первую очередь предназначен для графики и визуализации, его функциональные возможности могут дополнять определенные аспекты разработки игр.

### Вопрос 3. Где я могу найти дополнительные примеры и документацию?

 A3: Изучите всестороннее[Документация Aspose.3D](https://reference.aspose.com/3d/net/) для получения дополнительных примеров и подробной информации.

### В4: Есть ли бесплатная пробная версия?

 О4: Да, вы можете получить доступ к бесплатной пробной версии.[здесь](https://releases.aspose.com/).

### Вопрос 5: Как я могу обратиться за помощью или принять участие в жизни сообщества?

 A5: Присоединяйтесь к сообществу Aspose.3D на[форум поддержки](https://forum.aspose.com/c/3d/18) за помощь и сотрудничество.