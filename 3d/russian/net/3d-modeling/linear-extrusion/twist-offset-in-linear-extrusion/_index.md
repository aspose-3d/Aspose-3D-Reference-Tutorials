---
title: Смещение скручивания при линейной экструзии
linktitle: Смещение скручивания при линейной экструзии
second_title: Aspose.3D .NET API
description: Откройте для себя магию Aspose.3D для .NET с помощью нашего пошагового руководства по смещению скручивания в линейной экструзии. Усовершенствуйте свои 3D-проекты без особых усилий.
weight: 15
url: /ru/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Смещение скручивания при линейной экструзии

## Введение

Добро пожаловать в мир Aspose.3D для .NET, универсальной библиотеки, позволяющей разработчикам с легкостью выполнять 3D-манипуляции. В этом уроке мы углубимся в одну из интригующих функций — «Смещение поворота в линейной экструзии». Если вы готовы улучшить свои навыки 3D-программирования, давайте приступим!

## Предварительные условия

Прежде чем мы отправимся в это увлекательное путешествие, убедитесь, что у вас есть следующие предпосылки:

-  Библиотека Aspose.3D для .NET: загрузите и установите библиотеку из[страница выпуска](https://releases.aspose.com/3d/net/).

- Ваша среда разработки: убедитесь, что ваша среда разработки настроена и готова к работе.

## Импортировать пространства имен

Начните с импорта необходимых пространств имен для доступа к функциям, предоставляемым Aspose.3D для .NET. В вашем коде это может выглядеть так:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Теперь давайте разобьем пример на выполнимые шаги, чтобы освоить смещение поворота в линейной экструзии:

## Шаг 1. Инициализируйте базовый профиль

Начните с создания базового профиля, примером которого является прямоугольник с заданным радиусом скругления.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Шаг 2: Создайте сцену

Создайте 3D-сцену для размещения узлов и фигур.

```csharp
Scene scene = new Scene();
```

## Шаг 3: Создайте узлы

Постройте узлы внутри сцены, как слева, так и справа.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Шаг 4: Линейное выдавливание на левом узле

Выполните линейное вытягивание левого узла, используя свойство скручивания и срезов.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Шаг 5: Линейное выдавливание на правом узле со смещением поворота

На правом узле выполните линейное выдавливание, используя свойства скручивания, смещения скручивания и срезов.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Шаг 6: Сохраните 3D-сцену

Сохраните 3D-сцену в желаемый выходной каталог, указав формат файла WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Поздравляем! Вы успешно реализовали смещение поворота в линейной экструзии, используя Aspose.3D для .NET.

## Заключение

В этом уроке мы рассмотрели мощные возможности Aspose.3D для .NET, уделив особое внимание смещению поворота в линейной экструзии. Благодаря этим новообретенным навыкам вы хорошо подготовлены к тому, чтобы придать динамизм своим 3D-проектам.

## Часто задаваемые вопросы

### Вопрос 1: Могу ли я использовать Aspose.3D для .NET с другими языками программирования?

A1: Aspose.3D в основном поддерживает языки .NET, но Aspose предоставляет аналогичные библиотеки для Java и других платформ.

### Вопрос 2: Как получить временную лицензию на Aspose.3D для .NET?

 А2: Посетите[эта ссылка](https://purchase.aspose.com/temporary-license/)приобрести временную лицензию для целей тестирования.

### Вопрос 3. Существует ли форум сообщества Aspose.3D для .NET?

 А3: Абсолютно! Присоединяйтесь к сообществу по адресу[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) взаимодействовать с другими разработчиками и обращаться за помощью.

### Вопрос 4: Доступны ли дополнительные примеры и документация?

 А4: Исследуйте[документация](https://reference.aspose.com/3d/net/) для обширных руководств и примеров.

### Вопрос 5: Где я могу приобрести Aspose.3D для .NET?

 A5: Отправляйтесь в[эта ссылка](https://purchase.aspose.com/buy) совершить покупку и раскрыть весь потенциал Aspose.3D.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
