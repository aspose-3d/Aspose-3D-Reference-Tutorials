---
title: Сохранение 3D-сетей в пользовательском двоичном формате
linktitle: Сохранение 3D-сетей в пользовательском двоичном формате
second_title: Aspose.3D .NET API
description: Исследуйте мир 3D с помощью Aspose.3D для .NET. Научитесь сохранять сетки в пользовательском двоичном формате.
weight: 13
url: /ru/net/3d-scene/save-3d-meshes-binary-format/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Сохранение 3D-сетей в пользовательском двоичном формате

## Введение

Добро пожаловать в мир Aspose.3D для .NET, мощной библиотеки, которая позволяет разработчикам легко работать с 3D-файлами. В этом уроке мы углубимся в процесс сохранения 3D-сеток в пользовательском двоичном формате с использованием Aspose.3D для .NET. В этом руководстве предполагается, что у вас есть базовые знания C# и вы знакомы с библиотекой Aspose.3D.

## Предварительные условия

Прежде чем мы перейдем к руководству, убедитесь, что у вас есть следующее:

-  Aspose.3D для .NET: убедитесь, что у вас установлена библиотека Aspose.3D. Вы можете скачать его с[здесь](https://releases.aspose.com/3d/net/).

- Среда разработки: настройте предпочитаемую среду разработки C#, например Visual Studio.

- Входной 3D-файл: у вас есть 3D-файл (например, test.fbx), который вы хотите преобразовать в собственный двоичный формат.

## Импортировать пространства имен

В свой код C# включите необходимые пространства имен для доступа к функциям Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## Шаг 1. Загрузите 3D-файл

Загрузите свой 3D-файл с помощью Aspose.3D. В этом примере мы загружаем файл с именем «test.fbx»:

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Шаг 2. Определите собственный двоичный формат

Определите структуру пользовательского двоичного формата, в котором вы хотите сохранить свои 3D-сетки. В примере используется структура с MeshBlock, Vertex и Triangle в качестве компонентов.

```csharp
// Расположение памяти вершины
// позиция с плавающей запятой[3];
// float[3] нормально;
// поплавок[3] УФ;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Шаг 3: Откройте файл для записи

Откройте для записи бинарный файл, в котором будут сохранены конвертированные 3D-сетки:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Шаг 4. Перебор узлов и объектов

Посетите каждый узел 3D-сцены и преобразуйте объекты сетки в собственный двоичный формат. Игнорируйте источники света, камеры и другие объекты, не являющиеся сетками:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (продолжить обработку)
    }
    return true;
});
```

## Шаг 5: Преобразование и запись контрольных точек и треугольников

Для каждого объекта сетки преобразуйте контрольные точки в мировое пространство и записывайте их в двоичный файл вместе с индексами треугольников:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//Расположение памяти сетки:
// float[16] Transform_matrix;
// ИНТ vertices_count;
// интервал index_count;
// вершины[vertices_count] вершин;
// индексы ushort[indices_count];


//написать преобразование
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//написать количество вершин/индексов
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//писать вершины и индексы
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Заключение

В этом уроке мы рассмотрели процесс сохранения 3D-сеток в пользовательском двоичном формате с использованием Aspose.3D для .NET. Эта мощная библиотека предоставляет разработчикам инструменты, необходимые для беспрепятственного управления 3D-файлами. Экспериментируйте с различными форматами и настройками, чтобы раскрыть весь потенциал Aspose.3D в своих проектах.

## Часто задаваемые вопросы

### Вопрос 1: Могу ли я использовать Aspose.3D для .NET с другими языками программирования?

О1: Aspose.3D в основном поддерживает языки .NET, но вы можете изучить варианты совместимости для других языков.

### Вопрос 2. Где я могу найти дополнительные примеры и ресурсы?

 А2:[Форум Aspose.3D](https://forum.aspose.com/c/3d/18)— отличное место, где можно найти поддержку, примеры и пообщаться с сообществом.

### В3: Доступна ли пробная версия для Aspose.3D?

 О3: Да, вы можете получить бесплатную пробную версию на сайте[здесь](https://releases.aspose.com/).

### В4: Как получить временную лицензию на Aspose.3D?

 А4: Посетите[эта ссылка](https://purchase.aspose.com/temporary-license/) получить временную лицензию для целей тестирования.

### Вопрос 5: Могу ли я приобрести Aspose.3D для .NET?

 О5: Да, вы можете купить Aspose.3D на сайте[страница покупки](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
