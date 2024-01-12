---
title: Загрузка и сохранение — использование CancellationToken
linktitle: Загрузка и сохранение — использование CancellationToken
second_title: Aspose.3D .NET API
description: Исследуйте беспрепятственный мир 3D-моделирования с помощью Aspose.3D для .NET. Научитесь эффективно загружать и сохранять 3D-документы с помощью CancellationToken.
type: docs
weight: 10
url: /ru/net/loading-and-saving/cancellation-token/
---
## Введение

Добро пожаловать в наше подробное руководство по использованию Aspose.3D для .NET для улучшения ваших проектов 3D-моделирования и рендеринга. Aspose.3D — это мощная библиотека, которая позволяет .NET-разработчикам беспрепятственно работать с 3D-файлами. В этом руководстве мы углубимся в аспекты загрузки и сохранения, уделив особое внимание использованию CancellationToken для эффективного управления асинхронными задачами.

## Предварительные условия

Прежде чем мы отправимся в это путешествие, убедитесь, что у вас есть следующие предварительные условия:

-  Aspose.3D для .NET: Загрузите и установите библиотеку с сайта[здесь](https://releases.aspose.com/3d/net/).
- Среда .NET: убедитесь, что у вас настроена совместимая среда разработки .NET.
- Базовое понимание C#: рекомендуется знание языка программирования C#.

## Импортировать пространства имен

Для начала убедитесь, что вы включили в свой проект необходимые пространства имен. Эти пространства имен обеспечат доступ к функциям, необходимым для манипулирования 3D-файлами.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Загрузка и сохранение — использование CancellationToken

### Шаг 1. Создайте источник CancellationTokenSource.

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Здесь мы создаем экземпляр CancellationTokenSource, важнейшего компонента для управления отменой в асинхронных операциях.

### Шаг 2. Инициализируйте 3D-сцену

```csharp
Scene scene = new Scene();
```

Создайте экземпляр класса Scene. Это будет основой для вашего 3D-моделирования.

### Шаг 3. Установите тайм-аут CancellationToken

```csharp
cts.CancelAfter(1000);
```

 Установите тайм-аут отмены с помощью`CancelAfter` метод. В этом примере тайм-аут установлен на 1000 миллисекунд (1 секунду).

### Шаг 4: Откройте 3D-документ

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 Попытайтесь открыть 3D-документ в течение указанного периода времени.`cts.Token` Параметр гарантирует, что операцию можно отменить, если она превысит установленный таймаут.

### Шаг 5. Обработка исключения импорта

В случае ImportException обработайте его корректно, проверив, не было ли оно вызвано OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## Заключение

Поздравляем! Вы успешно прошли процесс использования Aspose.3D для .NET с CancellationToken для управления загрузкой 3D-документов. Этот метод обеспечивает эффективные и своевременные операции импорта, повышая общую производительность ваших 3D-приложений.

## Часто задаваемые вопросы

### Вопрос 1: Совместим ли Aspose.3D со всеми форматами 3D-файлов?

 A1: Aspose.3D поддерживает широкий спектр форматов 3D-файлов, включая FBX, STL, OBJ и другие. Обратитесь к[документация](https://reference.aspose.com/3d/net/) для полного списка.

### В2: Как я могу получить временную лицензию на Aspose.3D?

 A2: Получите временную лицензию, посетив[эта ссылка](https://purchase.aspose.com/temporary-license/).

### В3: Где я могу найти поддержку Aspose.3D?

 A3: Присоединяйтесь к обсуждению сообщества на[Форум Aspose.3D](https://forum.aspose.com/c/3d/18).

### Вопрос 4: Могу ли я бесплатно попробовать Aspose.3D перед покупкой?

 A4: Да, изучите функции, воспользовавшись бесплатной пробной версией.[здесь](https://releases.aspose.com/).

### Вопрос 5: Какая последняя версия Aspose.3D для .NET?

 A5: Будьте в курсе последних событий, проверяя[страница загрузки](https://releases.aspose.com/3d/net/) для последнего выпуска.