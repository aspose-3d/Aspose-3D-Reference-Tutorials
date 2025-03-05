---
title: Анимация свойств для документа в 3D-сценах
linktitle: Анимация свойств для документа в 3D-сценах
second_title: Aspose.3D .NET API
description: Научитесь анимировать 3D-свойства с помощью Aspose.3D для .NET. Пошаговое руководство по созданию динамичных сцен.
type: docs
weight: 10
url: /ru/net/animation/property-to-document/
---
## Введение

Если вы погружаетесь в область создания 3D-сцен и анимации в .NET, Aspose.3D — ваш идеальный набор инструментов. В этом пошаговом руководстве мы рассмотрим процесс анимации свойств в 3D-сценах с использованием Aspose.3D для .NET. К концу вы будете обладать знаниями, которые помогут вдохнуть жизнь в ваши 3D-проекты.

## Предварительные условия

Прежде чем мы отправимся в это увлекательное путешествие, убедитесь, что у вас есть следующие предпосылки:

-  Aspose.3D для .NET: убедитесь, что у вас установлена библиотека. Вы можете скачать его с сайта[Сайт Aspose.3D](https://releases.aspose.com/3d/net/).

- Знание C#: Знакомство с языком программирования C# необходимо для понимания и реализации примеров.

- Интегрированная среда разработки (IDE): используйте предпочитаемую вами среду IDE, например Visual Studio, для написания кода вместе с примерами.

- Основные концепции 3D-сцен. Понимание основных концепций 3D-сцен сделает ваше обучение более плавным.

## Импортировать пространства имен

Убедитесь, что в вашем коде C# импортированы необходимые пространства имен для Aspose.3D. Вот пример:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Шаг 1. Инициализируйте объект сцены

```csharp
Scene scene = new Scene();
```

## Шаг 2. Создайте сетку с помощью Polygon Builder

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Шаг 3. Создайте узлы куба

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Шаг 4. Найдите свойство перевода

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Шаг 5: Создайте точку привязки

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Шаг 6: Привяжите кривую анимации к X-компоненту

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Шаг 7: Привяжите кривую анимации к Z-компоненту

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Шаг 8: Сохраните 3D-сцену

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Шаг 9: Отображение сообщения об успехе

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Заключение

Поздравляем! Вы только что овладели искусством анимации свойств в 3D-сценах с помощью Aspose.3D для .NET. Теперь дайте волю своему творчеству, вдохнув жизнь в свои 3D-творения.

## Часто задаваемые вопросы

### Вопрос 1: Где я могу найти документацию Aspose.3D?

 A1: документация доступна[здесь](https://reference.aspose.com/3d/net/).

### Вопрос 2: Как загрузить Aspose.3D для .NET?

 A2: Вы можете скачать его с[страница выпуска](https://releases.aspose.com/3d/net/).

### В3: Есть ли бесплатная пробная версия?

 A3: Да, вы можете получить бесплатную пробную версию.[здесь](https://releases.aspose.com/).

### В4: Где я могу получить поддержку Aspose.3D?

 А4: Посетите[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) для поддержки.

### В5: Могу ли я получить временную лицензию?

 О5: Да, вы можете получить временную лицензию.[здесь](https://purchase.aspose.com/temporary-license/).