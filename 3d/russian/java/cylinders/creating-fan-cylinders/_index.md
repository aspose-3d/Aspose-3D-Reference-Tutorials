---
date: 2026-08-02
description: Узнайте, как создать cylinder fan shape в Java с Aspose.3D. Это руководство
  охватывает java 3D modeling и техники сохранения obj file в Java.
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
lastmod: 2026-08-02
linktitle: Как создать cylinder fan shape с помощью Aspose.3D для Java
og_description: Создайте cylinder fan shape с использованием Aspose.3D для Java и
  экспортируйте OBJ file java. Следуйте пошаговым инструкциям, чтобы моделировать,
  настраивать и сохранять ваш 3D fan cylinder.
og_image_alt: 'Tutorial: create cylinder fan shape in Java with Aspose.3D'
og_title: Создайте cylinder fan shape с Aspose.3D для Java – Быстрое руководство
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to create cylinder fan shape in Java with Aspose.3D. This
    guide covers java 3d modeling and save obj file java techniques.
  headline: How to create cylinder fan shape using Aspose.3D for Java
  type: TechArticle
- questions:
  - answer: Yes, Aspose.3D can coexist with libraries like Java 3D or jMonkeyEngine,
      allowing you to integrate custom geometry into larger pipelines.
    question: Is Aspose.3D compatible with other Java 3D libraries?
  - answer: Absolutely. You can apply materials, textures, and lighting by accessing
      the node’s `Material` and `Light` collections.
    question: Can I further customize the appearance of the fan cylinder?
  - answer: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community
      help and official responses.
    question: Where can I get additional support?
  - answer: Yes, you can explore Aspose.3D with a [free trial](https://releases.aspose.com/)
      before purchasing.
    question: Is there a free trial available?
  - answer: Acquire one [here](https://purchase.aspose.com/temporary-license/) to
      unlock full functionality during development.
    question: How do I obtain a temporary license for testing?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- create cylinder fan shape
- Aspose.3D
- Java 3D modeling
- export OBJ
- 3D geometry
title: Как создать cylinder fan shape с помощью Aspose.3D для Java
url: /ru/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Как создать форму цилиндра‑вентилятора с помощью Aspose.3D для Java

## Введение

Готовы освоить **создание формы цилиндра‑вентилятора** в среде Java? В этом руководстве мы пройдем каждый шаг — от настройки сцены до экспорта файла Wavefront OBJ — используя Aspose.3D. Независимо от того, создаете ли вы игровой объект, прототип CAD или просто экспериментируете с 3D‑геометрией, вы увидите, насколько простым может быть 3D‑моделирование на Java с этой мощной библиотекой.

## Быстрые ответы
- **Какова основная цель?** Создать настраиваемый цилиндр‑вентилятор и сохранить его в виде OBJ‑файла.  
- **Какая библиотека используется?** Aspose.3D для Java.  
- **Нужна ли лицензия?** Бесплатная пробная версия подходит для разработки; коммерческая лицензия требуется для продакшна.  
- **Какие предпосылки?** Установленный JDK и добавленный пакет Aspose.3D Java в ваш проект.  
- **Можно ли экспортировать в другие форматы?** Да — Aspose.3D поддерживает множество форматов; в этом примере используется Wavefront OBJ.

## Что такое цилиндр‑вентилятор?

Цилиндр‑вентилятор — это сегмент цилиндра, у которого удалена часть круглого основания, образуя открытый «вентиляторный» сектор. Он определяется радиусом, высотой и углом раскрытия, что делает его идеальным для визуализации срезов, панелей приборов или пользовательских механических деталей.  

На практике это обычный цилиндр с вырезанным клином — идеально подходит для представления частичных вращений или визуализаций в стиле срезов в инженерных панелях.

## Почему стоит использовать Aspose.3D для 3D‑моделирования на Java?

Aspose.3D для Java предоставляет высокоуровневый объектно‑ориентированный API, который абстрагирует низкоуровневую математику, поддерживает **более 50 форматов ввода и вывода** и может обрабатывать модели в сотни страниц без загрузки всего файла в память, что ускоряет разработку 3D‑приложений. Библиотека также автоматически обрабатывает **экспорт OBJ‑файлов на Java**, позволяя сосредоточиться на геометрии, а не на особенностях форматов файлов.

## Предпосылки

Прежде чем приступить, убедитесь, что у вас есть:

- **Java Development Kit (JDK)** — скачайте его [здесь](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D для Java** — получите последнюю JAR‑библиотеку по [ссылке загрузки](https://releases.aspose.com/3d/java/).  

Добавьте JAR‑файл Aspose.3D в classpath вашего проекта.

## Импорт пакетов

Начните с импорта необходимых классов. Это даст вам доступ к 3D‑сцене, примитивам геометрии и вспомогательным методам.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Шаг 1: Создание сцены

Класс `Scene` — контейнер Aspose.3D, который хранит все 3D‑объекты, источники света и камеры. Представьте его как виртуальную сцену, где размещаются все элементы вашей модели.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Шаг 2: Создание цилиндра‑вентилятора (как создать цилиндр)

Класс `Cylinder` представляет цилиндрическую сетку, которую можно настроить с помощью радиуса, высоты, тесселяции и угла раскрытия вентилятора. Регулируя `setThetaLength`, вы контролируете, какая часть цилиндра будет удалена.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Совет:** Изменяйте `setThetaLength`, чтобы задать угол раскрытия. 270° создаёт трёхчетвертный вентилятор; 180° даст полусиллиндр.

## Шаг 3: Позиционирование цилиндра‑вентилятора

Класс `Node` — элемент графа сцены, который хранит геометрию и её трансформацию. Перемещение узла переводит цилиндр‑вентилятор в нужное место в системе координат (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Шаг 4: Создание обычного цилиндра (сравнение 3D‑моделирования на Java)

Чтобы продемонстрировать гибкость Aspose.3D, мы также создаём обычный цилиндр без вентилятора. Это сравнение «лицом к лицу» помогает увидеть влияние параметра `ThetaLength`.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Шаг 5: Сохранение сцены (сохранение OBJ‑файла на Java)

Метод `Scene.save` записывает всю сцену в файл. При передаче `FileFormat.WAVEFRONTOBJ` Aspose.3D генерирует стандартный OBJ‑файл, который можно открыть в Blender, Maya, Unity и многих других 3D‑инструментах.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Примечание:** Замените `"Your Document Directory"` на абсолютный или относительный путь, где у вас есть права записи.

## Как сохранить OBJ‑файл в Java с помощью Aspose 3D

Чтобы экспортировать сцену, вызовите `scene.save("output.obj", FileFormat.WAVEFRONTOBJ);` — Aspose.3D запишет геометрию, материалы и ссылки на текстуры в стандартный Wavefront OBJ‑файл, который откроет любой крупный 3D‑редактор.

## Распространённые проблемы и решения

| Проблема | Причина | Решение |
|----------|---------|---------|
| OBJ‑файл пустой | Сцена не сохранена или указан неверный путь | Проверьте, что каталог вывода существует и имеет права записи. |
| Угол раскрытия вентилятора выглядит неверно | Неправильное значение `ThetaLength` | Используйте `MathUtils.toRadian(degrees)`, чтобы задать точный угол. |
| Ошибки компиляции | Отсутствует JAR‑файл Aspose.3D в classpath | Добавьте JAR в папку `libs` проекта и включите его в путь сборки. |

## Часто задаваемые вопросы

**В: Совместима ли Aspose.3D с другими Java‑библиотеками 3D?**  
О: Да, Aspose.3D может сосуществовать с библиотеками вроде Java 3D или jMonkeyEngine, позволяя интегрировать пользовательскую геометрию в более крупные конвейеры.

**В: Можно ли дальше настраивать внешний вид цилиндра‑вентилятора?**  
О: Абсолютно. Вы можете применять материалы, текстуры и освещение, получая доступ к коллекциям `Material` и `Light` узла.

**В: Где получить дополнительную поддержку?**  
О: Посетите [форум Aspose.3D](https://forum.aspose.com/c/3d/18) для помощи сообщества и официальных ответов.

**В: Есть ли бесплатная пробная версия?**  
О: Да, вы можете опробовать Aspose.3D с помощью [бесплатной пробной версии](https://releases.aspose.com/) перед покупкой.

**В: Как получить временную лицензию для тестирования?**  
О: Приобретите её [здесь](https://purchase.aspose.com/temporary-license/), чтобы разблокировать полный функционал во время разработки.

---

**Последнее обновление:** 2026-08-02  
**Тестировано с:** Aspose.3D 24.11 for Java  
**Автор:** Aspose

## Похожие руководства

- [How to Create Cylinder Models with Aspose.3D for Java](/3d/java/cylinders/)
- [Aspose Temporary License – Create Cylinder with Offset Top (Java)](/3d/java/cylinders/creating-cylinders-with-offset-top/)
- [How to Change Plane Orientation and Export OBJ in Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}