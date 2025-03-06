---
title: Рендеринг сцены в кубическую карту с шестью гранями
linktitle: Рендеринг сцены в кубическую карту с шестью гранями
second_title: Aspose.3D .NET API
description: Создавайте потрясающие кубические карты с помощью Aspose.3D для .NET. Следуйте нашему пошаговому руководству по рендерингу 3D-сцен в увлекательные шестигранные кубические карты.
weight: 14
url: /ru/net/rendering/render-scene-cubemap/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Рендеринг сцены в кубическую карту с шестью гранями

## Введение
Добро пожаловать в это пошаговое руководство по рендерингу сцены в кубическую карту с шестью гранями с использованием Aspose.3D для .NET. В этом уроке мы покажем вам процесс создания потрясающей кубической карты путем рендеринга 3D-сцены. Aspose.3D — это мощный API .NET, который упрощает манипулирование трехмерной графикой, и с помощью этого руководства вы сможете использовать его возможности для создания увлекательных кубических карт.
## Предварительные условия
Прежде чем мы углубимся в руководство, убедитесь, что у вас есть следующие предварительные условия:
- Практические знания разработки на C# и .NET.
-  Aspose.3D для .NET установлен. Вы можете скачать его[здесь](https://releases.aspose.com/3d/net/).
- Файл 3D-сцены в формате GLB (например, «VirtualCity.glb») для рендеринга.
## Импортировать пространства имен
Начните с импорта необходимых пространств имен для Aspose.3D в ваш код C#:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Шаг 1: Загрузите сцену
Загрузите файл 3D-сцены, используя следующий код:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Шаг 2. Создайте камеру и освещение
Создайте камеру и два источника света для освещения сцены:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Шаг 3. Создайте средство рендеринга и цель рендеринга
Создайте средство рендеринга и цель рендеринга карты куба с текстурой глубины:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Шаг 4. Сохраните грани кубической карты
Сохраните каждую грань кубической карты на диск с указанными именами файлов:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Заключение
Поздравляем! Вы успешно преобразовали 3D-сцену в кубическую карту с помощью Aspose.3D для .NET. Изучите дополнительные возможности настройки и улучшите свои проекты 3D-графики с помощью этого мощного API.
## Часто задаваемые вопросы
### Вопрос: Могу ли я использовать Aspose.3D для .NET с другими форматами 3D-файлов?
Да, Aspose.3D поддерживает различные форматы 3D-файлов, обеспечивая гибкость в ваших проектах.
### Вопрос: Как я могу получить поддержку Aspose.3D?
 Посетить[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) за поддержку сообщества и обсуждения.
### Вопрос: Доступна ли бесплатная пробная версия?
 Да, вы можете получить доступ к бесплатной пробной версии[здесь](https://releases.aspose.com/).
### Вопрос: Могу ли я визуализировать сцены с анимацией с помощью Aspose.3D?
Абсолютно! Aspose.3D поддерживает рендеринг анимированных 3D-сцен.
### Вопрос: Где я могу найти подробную документацию?
 Обратитесь к[Документация Aspose.3D](https://reference.aspose.com/3d/net/) для более подробной информации.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
