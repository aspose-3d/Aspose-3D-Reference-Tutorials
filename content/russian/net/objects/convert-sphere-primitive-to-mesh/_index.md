---
title: Преобразование примитива сферы в сетку
linktitle: Преобразование примитива сферы в сетку
second_title: Aspose.3D .NET API
description: Изучите Aspose.3D для .NET и легко преобразуйте сферическую сетку в треугольную сетку с настраиваемым расположением памяти. Следуйте нашему пошаговому руководству для бесшовной интеграции.
type: docs
weight: 16
url: /ru/net/objects/convert-sphere-primitive-to-mesh/
---
## Введение
Вы хотите использовать возможности Aspose.3D для .NET для преобразования сферической сетки в треугольную сетку с настраиваемым расположением памяти? Это пошаговое руководство проведет вас через весь процесс, благодаря чему его смогут легко выполнить даже новички. К концу этого руководства вы получите четкое представление о том, как добиться этого с помощью Aspose.3D для .NET.
## Предварительные условия
Прежде чем приступить к изучению руководства, убедитесь, что у вас есть следующие предварительные условия:
- Базовые знания .NET-программирования.
- Установлена библиотека Aspose.3D для .NET. Вы можете скачать его с сайта[Страница загрузки Aspose.3D для .NET](https://releases.aspose.com/3d/net/).
- Знание языка программирования C#.
## Импортировать пространства имен
В вашем проекте C# обязательно импортируйте необходимые пространства имен для использования функциональности Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Шаг 1: Инициализация объекта сцены
```csharp
// Инициализировать объект сцены
Scene scene = new Scene();
```
## Шаг 2. Инициализация объекта класса узла
```csharp
// Инициализировать объект класса Node
Node cubeNode = new Node("sphere");
```
## Шаг 3. Преобразование сферической сетки в типизированную TriMesh
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Шаг 4. Получите данные вершин в индивидуальной структуре
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Шаг 5. Получите 32-битные и 16-битные индексы
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Шаг 6. Запись данных вершин и индексов в поток памяти
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Шаг 7: Наведите узел на геометрию сетки
```csharp
cubeNode.Entity = sphere;
```
## Шаг 8: Добавьте узел в сцену
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Шаг 9: Сохраните 3D-сцену
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Шаг 10: Отображение результатов
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## Пример исходного кода MyVertex
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## Заключение
Поздравляем! Вы успешно преобразовали сферическую сетку в треугольную сетку с пользовательским расположением памяти с помощью Aspose.3D для .NET. Эта мощная библиотека обеспечивает удобный способ манипулирования трехмерными объектами в ваших приложениях .NET.
## Часто задаваемые вопросы
### Вопрос: Могу ли я использовать Aspose.3D для .NET с другими платформами .NET?
О: Да, Aspose.3D for .NET совместим с различными платформами .NET.
### Вопрос: Где я могу найти подробную документацию по Aspose.3D для .NET?
 О: Обратитесь к[Документация Aspose.3D для .NET](https://reference.aspose.com/3d/net/) для более подробной информации.
### Вопрос: Как я могу получить временную лицензию на Aspose.3D для .NET?
 Визит[эта ссылка](https://purchase.aspose.com/temporary-license/) получить временную лицензию.
### Вопрос: Существуют ли какие-либо примеры проектов для Aspose.3D для .NET?
 О: Изучите документацию Aspose.3D for .NET и[Репозиторий GitHub](https://github.com/aspose-3d/Aspose.3D-for-.NET) для образцовых проектов.
### Вопрос: Существует ли активное сообщество поддержки Aspose.3D для .NET?
 О: Да, присоединяйтесь[Форум Aspose.3D для .NET](https://forum.aspose.com/c/3d/18) чтобы получить помощь от сообщества.