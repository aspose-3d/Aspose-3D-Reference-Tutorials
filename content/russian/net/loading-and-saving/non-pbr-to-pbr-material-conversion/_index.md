---
title: Загрузка и сохранение — преобразование материалов из не-PBR в PBR
linktitle: Загрузка и сохранение — преобразование материалов из не-PBR в PBR
second_title: Aspose.3D .NET API
description: Изучите Aspose.3D для .NET — конвертируйте материалы без PBR в PBR без особых усилий. Комплексное руководство и мощный API.
type: docs
weight: 16
url: /ru/net/loading-and-saving/non-pbr-to-pbr-material-conversion/
---
## Введение

Добро пожаловать в это пошаговое руководство по использованию Aspose.3D для .NET для преобразования материалов без PBR (физического рендеринга) в материалы PBR. Aspose.3D — это мощный API, который позволяет разработчикам беспрепятственно работать с форматами 3D-файлов в своих .NET-приложениях.

## Предварительные условия

Прежде чем мы углубимся в руководство, убедитесь, что у вас есть следующие предварительные условия:

-  Aspose.3D for .NET: убедитесь, что у вас установлена библиотека Aspose.3D for .NET. Вы можете найти ссылку для скачивания[здесь](https://releases.aspose.com/3d/net/).

- Базовое понимание C#. В этом руководстве предполагается, что у вас есть фундаментальное понимание программирования на C#.

- IDE (интегрированная среда разработки). Выберите предпочитаемую среду IDE для разработки .NET, например Visual Studio.

## Импортировать пространства имен

В своем коде C# начните с импорта необходимых пространств имен:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Шаг 1. Инициализируйте новую 3D-сцену

Начните с создания новой 3D-сцены, используя следующий код:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// инициализировать новую 3D-сцену
var scene = new Scene();
```

## Шаг 2. Создайте 3D-объект

Далее создайте 3D объект, например коробку:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Шаг 3. Настройка преобразования материалов

Настройте параметры преобразования материалов для преобразования Non-PBR в PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Шаг 4. Сохраните в формате GLTF 2.0.

Сохраните конвертированную сцену в формате GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Повторите эти шаги по мере необходимости для вашего конкретного варианта использования, убедившись, что каждая деталь настроена правильно.

## Заключение

Поздравляем! Вы успешно научились конвертировать материалы Non-PBR в PBR с помощью Aspose.3D для .NET. Этот мощный инструмент открывает безграничные возможности для манипуляций с 3D-графикой в ваших .NET-приложениях.

## Часто задаваемые вопросы

### Вопрос 1: Совместим ли Aspose.3D со всеми форматами 3D-файлов?

О1: Да, Aspose.3D поддерживает широкий спектр форматов 3D-файлов, обеспечивая гибкость в ваших проектах.

### Вопрос 2: Могу ли я использовать Aspose.3D для коммерческих приложений?

 А2: Абсолютно! Aspose.3D — коммерческий продукт, и вы можете его приобрести.[здесь](https://purchase.aspose.com/buy).

### В3: Нужна ли мне временная лицензия для тестирования?

О3: Да, вы можете получить временную лицензию для целей тестирования.[здесь](https://purchase.aspose.com/temporary-license/).

### В4: Где я могу найти поддержку Aspose.3D?

 А4: Посетите[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) за поддержку сообщества и обсуждения.

### В5: Есть ли бесплатная пробная версия?

 A5: Да, вы можете изучить бесплатную пробную версию.[здесь](https://releases.aspose.com/).