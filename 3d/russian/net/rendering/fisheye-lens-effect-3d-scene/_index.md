---
title: Применение эффекта линзы «рыбий глаз» с помощью Aspose.3D для .NET
linktitle: Применение эффекта линзы «рыбий глаз» к 3D-сцене
second_title: Aspose.3D .NET API
description: Улучшите свои 3D-сцены с помощью Aspose.3D для .NET! Узнайте, как шаг за шагом применить очаровательный эффект линзы «рыбий глаз». Скачать сейчас!
weight: 12
url: /ru/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Применение эффекта линзы «рыбий глаз» с помощью Aspose.3D для .NET

## Введение
Вы хотите повысить визуальную привлекательность своих 3D-сцен? Погрузитесь в увлекательный мир эффектов объектива «рыбий глаз» с Aspose.3D для .NET. В этом уроке вы шаг за шагом узнаете, как применить эффект линзы «рыбий глаз» к вашим 3D-сценам, придав им уникальную и захватывающую перспективу.
## Предварительные условия
Прежде чем мы начнем, убедитесь, что у вас есть следующие предварительные условия:
-  Aspose.3D для .NET: убедитесь, что у вас установлена библиотека Aspose.3D для .NET. Если нет, то вы можете скачать его[здесь](https://releases.aspose.com/3d/net/).
-  Пример 3D-сцены. Мы будем работать с примером файла 3D-сцены (VirtualCity.glb). Вы можете использовать свою собственную сцену или загрузить образец с сайта[Документация Aspose.3D](https://reference.aspose.com/3d/net/).
## Импортировать пространства имен
В свой проект .NET включите необходимые пространства имен для доступа к функциям Aspose.3D. Добавьте следующие пространства имен в начало вашего кода:
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
## Шаг 1. Загрузите 3D-сцену
Загрузите файл 3D-сцены в свой проект, используя следующий код:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Шаг 2. Настройте камеру и освещение
Создайте камеру и освещение, чтобы улучшить визуальные аспекты вашей сцены. При необходимости настройте такие параметры, как NearPlane, FarPlane и RotationMode:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Шаг 3. Создайте средство рендеринга и цели рендеринга
Настройте средство рендеринга и создайте цели рендеринга для карты куба и 2D-текстуры:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Шаг 4. Примените эффект линзы «рыбий глаз»
Выполните постобработку эффекта линзы «рыбий глаз» на визуализированной карте куба:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Заключение
Поздравляем! Вы успешно применили эффект линзы «рыбий глаз» к своей 3D-сцене с помощью Aspose.3D для .NET. Экспериментируйте с различными сценами и параметрами, чтобы раскрыть свой творческий потенциал.
## Часто задаваемые вопросы
### Могу ли я применить эффект «рыбий глаз» к любой 3D-сцене?
Да, вы можете применить эффект «рыбий глаз» к любой 3D-сцене. Для достижения оптимальных результатов убедитесь, что сцена правильно загружена и освещена.
### Каково значение настройки поля зрения (fov) на 360 градусов?
Поле обзора в 360 градусов обеспечивает полную сферическую проекцию, создавая потрясающий эффект «рыбиго глаза».
### Как настроить освещение в 3D-сцене?
Вы можете настроить свойства источников света, такие как положение, тип и цвет, для достижения желаемых световых эффектов.
### Существует ли ограничение на размер обрабатываемой 3D-сцены?
Размер 3D-сцены в первую очередь ограничен системными ресурсами. Убедитесь, что ваше оборудование может справиться с размером вашей сцены.
### Могу ли я использовать другой выходной формат вместо PNG для получения эффекта «рыбий глаз»?
Да, вы можете изменить код, чтобы сохранить выходные данные в разных форматах изображений в зависимости от ваших требований.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
