---
date: 2026-05-24
description: Узнайте, как создать 3D-выдавливание с помощью срезов, используя Aspose.3D
  for Java. Это пошаговое руководство охватывает линейное выдавливание, установку
  радиуса скругления и экспорт OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Создание 3D-выдавливания с помощью срезов – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Создание 3D-выдавливания с помощью срезов – Aspose.3D for Java
url: /ru/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Создать 3D экструдирование с срезами – Aspose.3D for Java

## Введение

Если вам нужно **создать 3d экструдирование** объектов, которые выглядят гладко и точно, контроль количества срезов является ключевым. В этом руководстве мы пройдемся по тому, как задавать срезы при выполнении линейного экструдирования с помощью Aspose.3D for Java. Вы увидите, почему количество срезов важно, как установить радиус скругления и как экспортировать результат в файл OBJ, который можно использовать в любой 3‑D конвейер.

## Быстрые ответы
- **Что контролируют «срезы»?** Количество промежуточных поперечных сечений, используемых для аппроксимации поверхности экструдирования.  
- **Какой метод задает количество срезов?** `LinearExtrusion.setSlices(int)`  
- **Можно ли изменить радиус скругления профиля?** Да, через `RectangleShape.setRoundingRadius(double)`  
- **Какой формат файла используется в этом примере?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Нужна ли лицензия для запуска кода?** Бесплатная пробная версия подходит для оценки; коммерческая лицензия требуется для продакшна.

`LinearExtrusion.setSlices(int)` задает, сколько промежуточных срезов будет генерировать экструдирование.  
`RectangleShape.setRoundingRadius(double)` определяет радиус скругления углов прямоугольного профиля.

## Как создать 3d экструдирование java с срезами?

Загрузите ваш 2‑D профиль, выберите количество срезов, задайте радиус скругления и вызовите `save` — весь процесс помещается в несколько строк. Aspose.3D for Java автоматически обрабатывает создание геометрии, интерполяцию срезов и экспорт в OBJ, позволяя сосредоточиться на визуальном качестве, а не на низкоуровневых расчётах сетки.

## Что такое линейное экструдирование с срезами?

Линейное экструдирование с срезами превращает плоскую 2‑D форму в 3‑D объект, вытягивая её вдоль прямой линии и генерируя настраиваемое количество промежуточных поперечных сечений. Количество срезов напрямую влияет на плавность отображения изогнутых краев, таких как скруглённые углы.

## Почему использовать Aspose.3D for Java для создания 3d экструдирования?

Aspose.3D предоставляет **полный программный контроль** над каждым параметром экструдирования, поддерживает **более 50 форматов ввода и вывода** (включая OBJ, FBX, STL и GLTF) и может обрабатывать **многосотенные модели** без загрузки всего файла в память. Он работает на любой платформе с поддержкой Java, не требует нативных DLL и гарантирует детерминированные результаты на Windows, Linux и macOS.

## Предварительные требования

1. **Java Development Kit** – установлен JDK 8 или выше.  
2. **Aspose.3D for Java** – Скачайте библиотеку с официального сайта [здесь](https://releases.aspose.com/3d/java/).  
3. Любая IDE или текстовый редактор по вашему выбору.

## Импорт пакетов

Добавьте пространство имён Aspose.3D в ваш проект, чтобы иметь доступ к классам 3‑D моделирования.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Пошаговое руководство

### Шаг 1: Настройка сцены и определение профиля

`RectangleShape` — класс, определяющий 2‑D профиль прямоугольника.  
Сначала мы создаём `RectangleShape` и задаём ему **радиус скругления**, чтобы углы были гладкими.  
`Scene` — корневой контейнер для всех узлов и геометрии.  
Затем мы инициализируем новый `Scene`, который будет содержать всю геометрию.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Шаг 2: Создание дочерних узлов для каждого экструдирования

`Node` представляет элемент в графе сцены, который может содержать геометрию и трансформации.  
Каждый кусок геометрии находится под `Node`. Здесь мы создаём два соседних узла — один для экструдирования с небольшим количеством срезов, другой для экструдирования с большим количеством срезов — и немного сдвигаем левый узел в сторону, чтобы результаты было легко сравнить.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Шаг 3: Выполнение линейного экструдирования и установка срезов

`LinearExtrusion` — класс, создающий твёрдое тело путём линейного вытягивания профиля.  
`LinearExtrusion` — класс Aspose.3D, генерирующий твёрдое тело, экструдируя 2‑D профиль вдоль прямой линии. С помощью **анонимного внутреннего класса** мы вызываем `setSlices`, чтобы контролировать плавность. Левый узел получает только 2 среза (грубый), а правый узел — 10 срезов (плавный).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Шаг 4: Экспорт OBJ – сохранение сцены

Наконец, мы сохраняем сцену в файл Wavefront OBJ, формат, широко поддерживаемый 3‑D редакторами и игровыми движками. Это демонстрирует возможность **экспорта OBJ в Java** в Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Распространённые проблемы и решения

| Проблема | Почему происходит | Решение |
|----------|-------------------|--------|
| **Экструдирование выглядит плоским** | Количество срезов установлено в 1 или 0 | Убедитесь, что `setSlices` вызывается со значением ≥ 2. |
| **Скруглённые углы выглядят зазубренными** | Радиус скругления слишком мал относительно количества срезов | Увеличьте либо радиус, либо количество срезов для более плавных кривых. |
| **Файл не найден при сохранении** | `MyDir` указывает на несуществующую папку | Создайте каталог заранее или используйте абсолютный путь. |

## Часто задаваемые вопросы

**В: Как я могу скачать Aspose.3D for Java?**  
О: Вы можете скачать библиотеку [здесь](https://releases.aspose.com/3d/java/).

**В: Где я могу найти документацию по Aspose.3D?**  
О: Обратитесь к документации [здесь](https://reference.aspose.com/3d/java/).

**В: Доступна ли бесплатная пробная версия?**  
О: Да, вы можете ознакомиться с бесплатной пробной версией [здесь](https://releases.aspose.com/).

**В: Как я могу получить поддержку по Aspose.3D?**  
О: Посетите форум поддержки [здесь](https://forum.aspose.com/c/3d/18).

**В: Можно ли приобрести временную лицензию?**  
О: Да, временную лицензию можно получить [здесь](https://purchase.aspose.com/temporary-license/).

---

**Последнее обновление:** 2026-05-24  
**Тестировано с:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Автор:** Aspose

## Связанные руководства

- [Создать 3D экструдирование Java с Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Как задать направление в линейном экструдировании с Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Создать 3D сцену с круткой в линейном экструдировании – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}