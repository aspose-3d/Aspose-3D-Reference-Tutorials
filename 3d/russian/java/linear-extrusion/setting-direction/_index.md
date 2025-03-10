---
title: Установка направления линейной экструзии с помощью Aspose.3D для Java
linktitle: Установка направления линейной экструзии с помощью Aspose.3D для Java
second_title: Aspose.3D Java API
description: Освойте линейную экструзию с помощью Aspose.3D для Java! Следуйте нашему руководству по бесшовному 3D-программированию. Загрузите сейчас и получите захватывающие впечатления.
weight: 12
url: /ru/java/linear-extrusion/setting-direction/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Установка направления линейной экструзии с помощью Aspose.3D для Java

## Введение

Добро пожаловать в наше пошаговое руководство по настройке направления линейной экструзии с использованием Aspose.3D для Java. Aspose.3D — это мощная библиотека Java, которая позволяет разработчикам беспрепятственно работать с 3D-файлами и сценами. В этом уроке мы сосредоточимся на конкретной задаче задания направления линейной экструзии, что повысит ваши навыки в 3D-программировании.

## Предварительные условия

Прежде чем мы углубимся в руководство, убедитесь, что у вас есть следующие предварительные условия:

- Базовые знания языка программирования Java.
-  Установлена библиотека Aspose.3D. Вы можете скачать его с[здесь](https://releases.aspose.com/3d/java/).
- Интегрированная среда разработки (IDE) для Java, например Eclipse или IntelliJ.

## Импортировать пакеты

Убедитесь, что вы импортировали необходимые пакеты для запуска проекта:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Шаг 1. Инициализируйте базовый профиль

 Начните с инициализации базового профиля, который будет выдавливаться. В этом примере мы используем`RectangleShape` с радиусом округления 0,3:

```java
// Путь к каталогу документов.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Шаг 2: Создайте сцену

Затем создайте 3D-сцену, содержащую выдавленные объекты:

```java
Scene scene = new Scene();
```

## Шаг 3: Создайте узлы

Создайте левый и правый узлы внутри сцены:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Шаг 4. Выполните линейное выдавливание на левом узле

 Выполните линейное вытягивание левого узла, используя`LinearExtrusion`класс с указанными параметрами, такими как скручивание и срезы:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Шаг 5. Выполните линейное выдавливание на правом узле с указанием направления.

 Выполните линейное вытягивание правого узла, введя`setDirection` свойство для определения направления выдавливания:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Шаг 6: Сохраните 3D-сцену

Сохраните 3D-сцену в нужный формат файла. В этом примере мы сохраняем его как файл Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Заключение

Поздравляем! Вы успешно научились задавать направление линейной экструзии с помощью Aspose.3D для Java. Это руководство расширяет ваши навыки 3D-программирования и открывает новые возможности для творческих проектов.

## Часто задаваемые вопросы

### Вопрос 1: Могу ли я использовать Aspose.3D с другими языками программирования?

О1: Aspose.3D поддерживает различные языки программирования, включая .NET и Java.

### В2. Доступна ли бесплатная пробная версия Aspose.3D?

 О2: Да, вы можете изучить возможности Aspose.3D с помощью бесплатной пробной версии.[здесь](https://releases.aspose.com/).

### Вопрос 3: Где я могу найти подробную документацию по Aspose.3D для Java?

 A3: доступна полная документация.[здесь](https://reference.aspose.com/3d/java/).

### В4: Как я могу получить поддержку Aspose.3D?

 А4: Посетите[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) для любой помощи или вопросов.

### В5: Доступны ли временные лицензии для Aspose.3D?

 О5: Да, вы можете получить временную лицензию.[здесь](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
