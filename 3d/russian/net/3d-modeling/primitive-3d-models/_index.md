---
date: 2026-03-26
description: Узнайте, как создавать 3D‑модели коробки и цилиндра и сохранять сцену
  в формате FBX с помощью Aspose.3D для .NET.
linktitle: Create 3D Box and Cylinder Models with Aspose.3D for .NET
second_title: Aspose.3D .NET API
title: Создайте 3D‑модели коробки и цилиндра с помощью Aspose.3D для .NET
url: /ru/net/3d-modeling/primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Создание 3D‑моделей коробки и цилиндра с помощью Aspose.3D

## Introduction

Добро пожаловать в захватывающий мир 3D‑моделирования с Aspose.3D для .NET! В этом руководстве вы узнаете, **как создавать примитивы 3d‑box**, добавлять цилиндр и экспортировать всю сцену в FBX. Независимо от того, создаёте ли вы быстрый прототип или готовый к производству конвейер активов, эти шаги дадут вам прочную основу для работы с 3D‑геометрией в .NET.

## Quick Answers
- **Что охватывает данное руководство?** Создание 3D‑коробки, 3D‑цилиндра и сохранение сцены в файл FBX.  
- **Какая библиотека требуется?** Aspose.3D для .NET (скачать с официального сайта).  
- **Сколько времени занимает реализация?** Около 10‑15 минут для базовой сцены.  
- **Можно ли настроить размеры?** Да — конструкторы Box и Cylinder принимают параметры размеров.  
- **Нужна ли лицензия для продакшна?** Для сборок, не являющихся пробными, требуется действующая лицензия Aspose.3D.

## What is “create 3d box”?

Создание 3D‑коробки означает генерацию простого куба или прямоугольного параллелепипеда, который может служить строительным блоком для более сложных моделей. В Aspose.3D класс `Box` представляет этот примитив, и его можно добавить в сцену одной строкой кода.

## Why use Aspose.3D for this task?

- **Чистый .NET API:** Нет нативных зависимостей, идеально подходит для проектов на C# и VB.NET.  
- **Широкая поддержка форматов:** Экспорт в FBX, OBJ, STL и многие другие.  
- **Примитивы высокого уровня:** Box, Cylinder, Sphere и др., позволяют сосредоточиться на логике, а не на низкоуровневом построении сетки.  
- **Оптимизировано по производительности:** Эффективно обрабатывает большие сцены.

## Prerequisites

Прежде чем приступить, убедитесь, что у вас есть:

- Aspose.3D для .NET: скачайте и установите библиотеку по [ссылке для загрузки](https://releases.aspose.com/3d/net/).  
- Среда разработки .NET (Visual Studio, Rider или VS Code), совместимая с установленной версией Aspose.3D.

Теперь, когда всё готово, начнём поэтапно создавать сцену.

## Import Namespaces

Начните с импорта необходимых пространств имён для доступа к функционалу Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

С этими пространствами имён вы готовы раскрыть мощь Aspose.3D в вашем .NET‑приложении.

## Step 1: Initialize a Scene Object

```csharp
// Initialize a Scene object
Scene scene = new Scene();
```

Объект `Scene` служит холстом, на котором будут размещаться все 3D‑сущности.

## Step 2: Create a Box Model

```csharp
// Create a Box model
scene.RootNode.CreateChildNode("box", new Box());
```

Эта строка добавляет примитив **3D‑box** в корень вашей сцены. Позже вы можете изменить её ширину, высоту и глубину, передавая параметры конструктору `Box`.

## Step 3: Create a Cylinder Model

```csharp
// Create a Cylinder model
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Цилиндр дополняет коробку и демонстрирует, насколько просто комбинировать разные примитивы.

## Step 4: Save Drawing in FBX Format

```csharp
// Save drawing in the FBX format
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Здесь мы **конвертируем модель в FBX**, сохраняя всю сцену в файл FBX. При желании измените путь и имя файла в соответствии с структурой вашего проекта.

## Step 5: Display Success Message

```csharp
// Display success message
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Дружественное сообщение в консоли подтверждает, что операция **создания 3d‑сцены** завершилась без ошибок.

## Common Issues & Tips

- **Каталог вывода не существует:** Убедитесь, что папка `output` существует, либо используйте `Directory.CreateDirectory()` перед сохранением.  
- **Лицензия не установлена:** В сборке, не являющейся пробной, вызовите `License license = new License(); license.SetLicense("Aspose.3D.lic");` перед созданием `Scene`.  
- **Пользовательские размеры:** Используйте `new Box(width, height, depth)` или `new Cylinder(radius, height)` для задания размеров.

## Conclusion

Поздравляем! Вы успешно создали примитивы **3d‑box** и цилиндра, построили простую сцену и сохранили её в файл FBX с помощью Aspose.3D для .NET. Основы теперь находятся в вашем арсенале, и вы можете изучить [документацию](https://reference.aspose.com/3d/net/) для более продвинутых возможностей, таких как материалы, освещение и анимация.

## Frequently Asked Questions

### Q1: Can I use Aspose.3D for .NET with other programming languages?
**A1:** Aspose.3D в основном поддерживает .NET, но существуют версии для Java и других платформ.

### Q2: Is there a free trial available?
**A2:** Да, вы можете ознакомиться со способностями Aspose.3D с помощью [бесплатной пробной версии](https://releases.aspose.com/).

### Q3: Where can I find support for Aspose.3D for .NET?
**A3:** Посетите [форум Aspose.3D](https://forum.aspose.com/c/3d/18) для поддержки сообщества и обсуждений.

### Q4: How can I obtain a temporary license?
**A4:** Временную лицензию можно получить [здесь](https://purchase.aspose.com/temporary-license/).

### Q5: Are there any sample tutorials available?
**A5:** Да, изучайте дополнительные руководства и примеры в [документации](https://reference.aspose.com/3d/net/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-03-26  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

---