---
title: Указание срезов при линейном выдавливании с помощью Aspose.3D для Java
linktitle: Указание срезов при линейном выдавливании с помощью Aspose.3D для Java
second_title: Aspose.3D Java API
description: Научитесь задавать фрагменты при линейной экструзии с помощью Aspose.3D для Java. Совершенствуйте свои навыки 3D-моделирования с помощью этого пошагового руководства.
weight: 13
url: /ru/java/linear-extrusion/specifying-slices/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Указание срезов при линейном выдавливании с помощью Aspose.3D для Java

## Введение

Создание сложных 3D-моделей часто требует большего, чем просто творческий подход; это требует глубокого понимания инструментов, имеющихся в вашем распоряжении. Aspose.3D для Java меняет правила игры в этом отношении. В этом уроке мы сосредоточимся на конкретном аспекте — указании срезов при линейной экструзии.

## Предварительные условия

Прежде чем приступить к изучению руководства, убедитесь, что у вас есть следующие предварительные условия:

1. Среда Java: убедитесь, что в вашей системе настроена среда разработки Java.
2.  Aspose.3D для Java: Загрузите и установите библиотеку Aspose.3D. Вы можете найти необходимые пакеты[здесь](https://releases.aspose.com/3d/java/).

## Импортировать пакеты

В свой проект Java импортируйте библиотеку Aspose.3D. Это крайне важно для доступа к функциям, с которыми мы будем работать. Добавьте в свой код следующий оператор импорта:

```java
import com.aspose.threed.*;

import java.io.IOException;
```

Теперь давайте разобьем пример на несколько этапов.

## Шаг 1: Настройте сцену

Инициализируйте базовый профиль для выдавливания, в данном случае`RectangleShape` с заданным радиусом скругления. Создайте 3D-сцену для работы.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## Шаг 2: Создайте узлы

Создайте левый и правый узлы внутри сцены. Отрегулируйте перевод левого узла для пространственных изменений.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Шаг 3: Линейная экструзия срезами

Выполните линейное выдавливание на обоих узлах, указав количество срезов для каждого. Вот где происходит волшебство.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## Шаг 4: Сохраните сцену

Сохраните 3D-сцену в нужном формате, в данном случае в файле Wavefront OBJ.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Заключение

Поздравляем! Вы успешно научились задавать фрагменты при линейном вытягивании с помощью Aspose.3D для Java. Этот навык открывает новые возможности в вашем путешествии по 3D-моделированию.

## Часто задаваемые вопросы

### Вопрос 1: Как загрузить Aspose.3D для Java?

 A1: Вы можете скачать библиотеку[здесь](https://releases.aspose.com/3d/java/).

### Вопрос 2: Где я могу найти документацию для Aspose.3D?

 A2: обратитесь к документации[здесь](https://reference.aspose.com/3d/java/).

### В3: Есть ли бесплатная пробная версия?

 О3: Да, вы можете воспользоваться бесплатной пробной версией.[здесь](https://releases.aspose.com/).

### В4: Как я могу получить поддержку Aspose.3D?

 A4: Посетите форум поддержки.[здесь](https://forum.aspose.com/c/3d/18).

### В5: Могу ли я приобрести временную лицензию?

 О5: Да, временную лицензию можно получить.[здесь](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
