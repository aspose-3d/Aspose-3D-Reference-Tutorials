---
title: Центр линейной экструзии
linktitle: Центр линейной экструзии
second_title: Aspose.3D .NET API
description: Исследуйте мир 3D-моделирования с помощью Aspose.3D для .NET. Сосредоточьте методы линейной экструзии, создавайте потрясающие дизайны и раскрывайте свой творческий потенциал.
weight: 10
url: /ru/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Центр линейной экструзии

## Введение

Добро пожаловать в это подробное руководство по освоению линейной экструзии с использованием Aspose.3D для .NET. Если вы хотите улучшить свои навыки 3D-моделирования и создавать потрясающие выдавливания, вы попали по адресу. В этом уроке мы углубимся в технику линейной экструзии, уделив особое внимание аспекту центрирования, чтобы вывести ваши проекты на совершенно новый уровень.

## Предварительные условия

Прежде чем мы отправимся в это увлекательное путешествие, убедитесь, что у вас есть следующие предпосылки:

- Базовое понимание языка программирования C#.
- Visual Studio установлена на вашем компьютере.
-  Библиотека Aspose.3D для .NET, которую можно загрузить с сайта[Документация Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  Убедитесь, что у вас есть доступ к[Документация Aspose.3D .NET](https://reference.aspose.com/3d/net/) для справки на протяжении всего руководства.

## Импортировать пространства имен

Для начала давайте импортируем необходимые пространства имен. Они заложат основу для нашего шедевра 3D-моделирования.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Шаг 1. Инициализируйте базовый профиль

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Шаг 2. Создайте 3D-сцену

```csharp
Scene scene = new Scene();
```

## Шаг 3. Создайте левый и правый узлы

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Шаг 4. Выполните линейное выдавливание на левом узле

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Шаг 5. Установите базовую плоскость для справки

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Шаг 6. Выполните линейное выдавливание на правом узле

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Шаг 7. Установите базовую плоскость для справки (правый узел)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Шаг 8: Сохраните 3D-сцену

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Заключение

Поздравляем! Вы успешно освоили искусство линейной экструзии с центрированием, используя Aspose.3D для .NET. Не стесняйтесь экспериментировать с различными параметрами и исследовать огромные возможности, которые предлагает этот метод.

## Часто задаваемые вопросы

### Вопрос 1: Могу ли я использовать Aspose.3D для .NET с другими языками программирования?

A1: Aspose.3D в первую очередь поддерживает языки .NET, такие как C# и VB.NET.

### Вопрос 2. Где я могу найти поддержку запросов, связанных с Aspose.3D?

 A2: Посетите[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) за целенаправленную поддержку и обсуждения.

### Вопрос 3: Существует ли бесплатная пробная версия Aspose.3D для .NET?

 О3: Да, вы можете получить доступ к бесплатной пробной версии.[здесь](https://releases.aspose.com/).

### Вопрос 4: Как я могу получить временную лицензию на Aspose.3D для .NET?

 A4: Вы можете приобрести временную лицензию.[здесь](https://purchase.aspose.com/temporary-license/).

### Вопрос 5: Где я могу приобрести лицензию Aspose.3D для .NET?

 A5: Купите лицензию[здесь](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
