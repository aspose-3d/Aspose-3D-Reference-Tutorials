---
title: Индивидуальный нижний цилиндр сдвига
linktitle: Индивидуальный нижний цилиндр сдвига
second_title: Aspose.3D .NET API
description: Научитесь создавать индивидуальные цилиндры со сдвиговым дном с помощью Aspose.3D для .NET с помощью нашего подробного пошагового руководства. Совершенствуйте свои навыки 3D-моделирования уже сегодня!
weight: 12
url: /ru/net/3d-modeling/working-with-cylinder/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Индивидуальный нижний цилиндр сдвига

## Введение
Добро пожаловать в наше подробное руководство по созданию индивидуального цилиндра с помощью Aspose.3D для .NET. Если вы хотите улучшить свои навыки 3D-моделирования и добавить уникальные функции в свои проекты, вы попали по адресу. В этом уроке мы шаг за шагом проведем вас через этот процесс, используя четкие объяснения и фрагменты кода.
## Предварительные условия
Прежде чем мы углубимся в руководство, убедитесь, что у вас есть следующее:
- Базовое понимание программирования на C# и .NET.
-  Установлена библиотека Aspose.3D для .NET. Вы можете скачать его[здесь](https://releases.aspose.com/3d/net/).
- Среда разработки, настроенная для программирования .NET.
## Импортировать пространства имен
В своем коде C# начните с импорта необходимых пространств имен:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Шаг 1: Создайте сцену
Начните с создания 3D-сцены с помощью Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Шаг 2: Создайте цилиндр 1
Создайте первый цилиндр и установите его свойства:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Шаг 3. Настройка сдвигающегося днища для цилиндра 1
Примените настроенную нижнюю часть сдвига к первому цилиндру:
```csharp
//Сдвиг 47,5 градусов в плоскости xy (ось z)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Установите для GenerateFanCylinder значение true.
cylinder1.GenerateFanCylinder = true;
// Установить тетадлину
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Установить OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## Шаг 4. Добавьте в сцену цилиндр 1.
Добавьте в сцену первый цилиндр и задайте его перевод:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Шаг 5: Создайте цилиндр 2
Создайте второй цилиндр с аналогичными свойствами:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Шаг 6: Добавьте в сцену цилиндр 2
Добавьте в сцену второй цилиндр без настроенных параметров:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Шаг 7: Сохраните сцену
Сохраните сцену как файл Wavefront OBJ в каталоге документов:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Заключение
Поздравляем! Вы успешно создали индивидуальный цилиндр со сдвиговым дном, используя Aspose.3D для .NET. Цель этого руководства — предоставить пошаговое руководство для пользователей с разным уровнем знаний в области 3D-моделирования и программирования.
## Часто задаваемые вопросы
### Подходит ли Aspose.3D для .NET новичкам?
Абсолютно! Aspose.3D для .NET предлагает удобный интерфейс, что делает его доступным как для новичков, так и для опытных разработчиков.
### Могу ли я применять разные углы сдвига к цилиндрам?
Да, вы можете настроить дно сдвига для каждого цилиндра индивидуально, что позволит вам добиться уникальных эффектов.
### Доступна ли пробная версия?
 Да, вы можете изучить бесплатную пробную версию[здесь](https://releases.aspose.com/).
### Где я могу найти дополнительную поддержку?
 Посетить[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) за поддержку сообщества и обсуждения.
### Как получить временную лицензию?
 Получите временную лицензию[здесь](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
