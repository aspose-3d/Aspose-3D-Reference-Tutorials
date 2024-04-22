---
title: Направление линейной экструзии
linktitle: Направление линейной экструзии
second_title: Aspose.3D .NET API
description: Откройте для себя мир 3D-моделирования с помощью Aspose.3D для .NET. Изучите направление линейной экструзии, развивайте творческий подход и с легкостью создавайте иммерсивные приложения.
type: docs
weight: 11
url: /ru/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---
## Введение

В динамичном мире разработки программного обеспечения создание иммерсивных 3D-моделей является незаменимым навыком. Aspose.3D для .NET предоставляет разработчикам надежный набор инструментов для использования потенциала 3D-моделирования в своих приложениях. В этом уроке мы углубимся в интригующий мир линейной экструзии и исследуем нюансы функции «Направление линейной экструзии».

## Предварительные условия

Прежде чем мы отправимся в это увлекательное путешествие, убедитесь, что у вас есть следующие предпосылки:

-  Aspose.3D для .NET: Загрузите и установите библиотеку с сайта[Документация Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- Среда разработки: убедитесь, что у вас настроена работающая среда разработки .NET.

## Импортировать пространства имен

В свой проект .NET импортируйте необходимые пространства имен для доступа к функциям Aspose.3D. Добавьте следующие строки в начало вашего кода:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Шаг 1. Инициализируйте базовый профиль

Начните с инициализации базового профиля, который будет выдавливаться. В этом примере мы создаем прямоугольную форму с радиусом закругления 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Шаг 2. Создайте 3D-сцену

Создайте основу для своего 3D-шедевра, создав сцену.

```csharp
Scene scene = new Scene();
```

## Шаг 3: Создайте узлы

Создавайте узлы внутри сцены для представления различных компонентов вашей 3D-среды.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Шаг 4: Линейная экструзия без направления

 Выполните линейное вытягивание левого узла, используя`Twist` и`Slices` характеристики.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Шаг 5: Линейная экструзия с указанием направления

 Расширьте возможности экструзии, включив`Direction` свойство в правом узле.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Шаг 6: Сохраните 3D-сцену

 Сохраните свое творение, сохранив 3D-сцену. Заменять`"Your Output Directory"` с желаемым каталогом.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Поздравляем! Вы успешно реализовали линейную экструзию с помощью Aspose.3D для .NET, изучив как традиционный, так и направленный подходы.

## Заключение

В этом уроке мы прошли через увлекательную область 3D-моделирования с использованием Aspose.3D для .NET. Линейное выдавливание с направлением и без него открывает безграничные возможности для разработчиков, стремящихся создавать визуально ошеломляющие приложения. С Aspose.3D возможности 3D-моделирования у вас под рукой.

## Часто задаваемые вопросы

### Вопрос 1: Как я могу получить временную лицензию на Aspose.3D для .NET?

 А1: Посетите[Aspose Временная лицензия](https://purchase.aspose.com/temporary-license/) получить временную лицензию.

### В2: Где я могу найти поддержку Aspose.3D?

 А2: Присоединяйтесь к[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) искать помощи и общаться с сообществом.

### В3: Есть ли бесплатная пробная версия?

 О3: Да, изучите функции, воспользовавшись бесплатной пробной версией на сайте[Релизы Aspose.3D](https://releases.aspose.com/).

### Вопрос 4: Как мне приобрести Aspose.3D для .NET?

 A4: Перейдите к[Aspose Страница покупки](https://purchase.aspose.com/buy) для получения информации о вариантах лицензирования и деталях приобретения.

### Вопрос 5: Где я могу найти подробную документацию по Aspose.3D для .NET?

 A5: обратитесь к подробному[Документация Aspose.3D .NET](https://reference.aspose.com/3d/net/) для более подробной информации.