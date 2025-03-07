---
title: Пользовательские параметры загрузки
linktitle: Пользовательские параметры загрузки
second_title: Aspose.3D .NET API
description: Изучите Aspose.3D для .NET — идеальное решение для плавной загрузки и сохранения 3D-моделей.
weight: 15
url: /ru/net/loading-and-saving/custom-load-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Пользовательские параметры загрузки

## Введение

Добро пожаловать в мир Aspose.3D для .NET — мощной библиотеки, которая позволяет разработчикам беспрепятственно работать с 3D-файлами. В этом уроке мы углубимся в тонкости загрузки и сохранения 3D-моделей, уделив особое внимание пользовательским параметрам загрузки. Независимо от того, являетесь ли вы опытным разработчиком или новичком, это руководство шаг за шагом проведет вас через весь процесс, гарантируя, что вы сможете использовать весь потенциал Aspose.3D для .NET.

## Предварительные условия

Прежде чем мы отправимся в это путешествие, убедитесь, что у вас есть следующие предпосылки:

-  Aspose.3D для .NET: убедитесь, что у вас установлена библиотека. Вы можете скачать его[здесь](https://releases.aspose.com/3d/net/).

- Каталог документов: создайте каталог для хранения файлов 3D-моделей.

Теперь, когда у вас есть все необходимое, давайте окунемся в захватывающий мир манипуляций с 3D-моделями!

## Импортировать пространства имен

Прежде всего, давайте импортируем необходимые пространства имен. Это подготовит почву для нашего путешествия в мир Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Загрузка и сохранение — пользовательские параметры загрузки

### Шаг 1. Загрузка файлов Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Установить пользовательские параметры
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Загрузить файл с параметрами загрузки
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Шаг 2. Загрузка файлов OBJ

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Установить пользовательские параметры
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Загрузить файл с параметрами загрузки
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Шаг 3. Загрузка файлов STL

```csharp
private static void STLLoadOption()
{
    // Путь к каталогу документов.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Установить пользовательские параметры
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Загрузить файл с параметрами загрузки
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Шаг 4. Загрузка файлов U3D

```csharp
private static void U3DLoadOption()
{
    // Путь к каталогу документов.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Установить пользовательские параметры
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Загрузить файл с параметрами загрузки
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Шаг 5. Загрузка файлов glTF

```csharp
private static void glTFLoadOptions()
{
    // Путь к каталогу документов.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Установить пользовательские параметры
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Шаг 6: Загрузка файлов PLY

```csharp
private static void PlyLoadOptions()
{
    // Путь к каталогу документов.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Установить пользовательские параметры
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Шаг 7: Загрузка файлов FBX

```csharp
private static void FBXLoadOptions()
{
    // Путь к каталогу документов.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Установить пользовательские параметры
    scene.Open("test.FBX", opt);

    // Свойства вывода, определенные в GlobalSettings в файле FBX.
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Заключение

Поздравляем! Вы успешно справились с запутанным миром загрузки и сохранения 3D-моделей с помощью Aspose.3D для .NET. В этом руководстве рассматриваются различные форматы файлов и их пользовательские параметры загрузки, что позволяет вам с легкостью манипулировать 3D-ресурсами.

## Часто задаваемые вопросы

### Вопрос 1: Подходит ли Aspose.3D для .NET новичкам?

А1: Абсолютно! Aspose.3D for .NET предоставляет удобный интерфейс, что делает его доступным для разработчиков всех уровней.

### В2: Могу ли я использовать Aspose.3D для коммерческих проектов?

О2: Да, Aspose.3D for .NET поставляется с коммерческой лицензией, позволяющей вам использовать его в своих проектах.

### Вопрос 3. Существуют ли какие-либо ограничения на поддерживаемые форматы файлов?

 О3: Aspose.3D for .NET поддерживает широкий спектр популярных форматов 3D-файлов, включая OBJ, STL, FBX и другие. Обратитесь к[документация](https://reference.aspose.com/3d/net/) для получения полного списка.

### В4: Доступна ли пробная версия?

О4: Да, вы можете изучить возможности Aspose.3D для .NET, загрузив[бесплатная пробная версия](https://releases.aspose.com/).

### Вопрос 5: Где я могу получить поддержку Aspose.3D для .NET?

 A5: Посетите[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) за общественную поддержку и помощь.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
