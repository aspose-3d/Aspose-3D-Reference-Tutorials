---
title: Пользовательские параметры сохранения
linktitle: Пользовательские параметры сохранения
second_title: Aspose.3D .NET API
description: Откройте для себя возможности Aspose.3D для .NET. Узнайте, как настроить сохранение 3D-сцены, с помощью пошаговых руководств по форматам Collada, USD, 3DS, FBX, OBJ, STL, U3D, glTF, DRC и RVM.
weight: 21
url: /ru/net/loading-and-saving/custom-save-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Пользовательские параметры сохранения

## Введение

Добро пожаловать в мир Aspose.3D для .NET! Если вы хотите расширить свои возможности в области 3D-разработки, вы попали по адресу. В этом уроке мы углубимся в функции загрузки и сохранения, уделив особое внимание пользовательским параметрам сохранения. Aspose.3D для .NET — это мощная библиотека, которая позволяет разработчикам эффективно манипулировать и сохранять 3D-сцены.

## Предварительные условия

Прежде чем мы начнем изучать захватывающие возможности Aspose.3D, убедитесь, что у вас есть следующие предварительные условия:

- Базовое понимание разработки на C# и .NET.
-  Установлена библиотека Aspose.3D для .NET. Вы можете скачать его с сайта[страница выпуска](https://releases.aspose.com/3d/net/).
- Среда разработки, настроенная с помощью Visual Studio или любой другой предпочтительной среды разработки C#.

## Импортировать пространства имен

Для начала импортируем необходимые пространства имен:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

Теперь, когда мы подготовили почву, давайте разобьем руководство на несколько этапов.

## Шаг 1. Вариант сохранения коллады

Начнем с Collada, популярного формата 3D-файлов. Выполните следующие действия, чтобы настроить параметры сохранения Collada:

### 1. Настройка каталога:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Инициализируйте параметры сохранения Collada:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. Настройте параметры:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## Шаг 2. Возможность дискретного сохранения в 3DS.

Теперь давайте рассмотрим Discreet 3DS и возможности его настройки:

### 1. Настройка каталога:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Инициализируйте параметры сохранения 3DS:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. Настройте параметры:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // Дополнительные возможности конфигурации...
   ```

Продолжайте этот пошаговый подход для параметров сохранения FBX, OBJ, STL, U3D, glTF и DRC, настраивая каждый из них в соответствии с вашими требованиями.

## Шаг 3. Параметры сохранения glTF

Теперь давайте сосредоточимся на glTF — формате, широко используемом в веб-приложениях и мобильных приложениях. Настройте параметры сохранения glTF, выполнив следующие действия:

### 1. Инициализируйте объект сцены:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. Установите параметры сохранения glTF:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. Сохраните файл glTF:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

Следуйте аналогичной структуре для других вариантов сохранения, таких как DRC и RVM.

## Заключение

Поздравляем! Вы успешно изучили пользовательские параметры сохранения в Aspose.3D для .NET. Эта мощная библиотека предоставляет множество возможностей для настройки процесса сохранения 3D-сцены.

## Часто задаваемые вопросы

### Вопрос 1: Могу ли я использовать Aspose.3D для .NET с другими платформами .NET?

О1: Да, Aspose.3D совместим с различными платформами .NET, что обеспечивает гибкость вашей среды разработки.

### Вопрос 2: Существуют ли какие-либо варианты лицензирования для Aspose.3D?

 О2: Да, вы можете изучить варианты лицензирования.[здесь](https://purchase.aspose.com/buy).

### Вопрос 3. Где я могу найти поддержку запросов, связанных с Aspose.3D?

 A3: Вы можете обратиться за поддержкой на[Форум Aspose.3D](https://forum.aspose.com/c/3d/18).

### В4: Есть ли бесплатная пробная версия?

 О4: Да, вы можете получить доступ к бесплатной пробной версии.[здесь](https://releases.aspose.com/).

### В5: Как я могу получить временную лицензию на Aspose.3D?

 A5: Получите временную лицензию[здесь](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
