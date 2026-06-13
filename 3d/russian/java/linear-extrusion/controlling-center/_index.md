---
date: 2026-06-13
description: Изучите учебник по графике java 3d, посвященный управлению центром в
  линейной экструзии с Aspose.3D, включая настройку радиуса скругления и сохранение
  OBJ‑файла java.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Управление центром в линейной экструзии с Aspose.3D для Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: Создание 3D Mesh Java – Центр в линейной экструзии
url: /ru/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Создать 3D Mesh Java – Центр в линейной экструзии

## Введение

Если вы создаёте 3‑D визуализации в Java, освоение техник экструзии является обязательным. Этот **java 3d graphics tutorial** показывает, как **create 3d mesh java** объекты, контролируя центр линейной экструзии с помощью Aspose.3D for Java. К концу этого руководства вы поймёте, почему свойство `center` имеет значение, как **set rounding radius**, и как **save obj file java**‑совместный вывод. Вы также увидите, как **export 3d model obj** для использования в любом крупном 3‑D редакторе.

## Быстрые ответы

- **Что делает свойство center?** Оно определяет, будет ли экструзия симметричной относительно начала профиля.  
- **Нужна ли лицензия для запуска кода?** Временная лицензия работает для тестирования; полная лицензия требуется для продакшн.  
- **Какой формат файла используется для результата?** Сцена сохраняется в виде файла Wavefront OBJ.  
- **Можно ли изменить количество срезов?** Да, используйте `setSlices(int)` у объекта `LinearExtrusion`.  
- **Совместим ли Aspose.3D с Java 8+?** Абсолютно — он поддерживает все современные версии Java.

## Что такое java 3d graphics tutorial?

**java 3d graphics tutorial** — это пошаговое руководство, которое учит использовать Java‑библиотеки для создания, манипулирования и рендеринга трёхмерных объектов. В этом руководстве вы научитесь **create 3d mesh java** путем преобразования 2‑D профиля в полноценную 3‑D модель, управлять её центральным выравниванием, скруглять углы экструзии и в конце экспортировать результат в файл OBJ, который может прочитать любая 3‑D программа.

## Почему использовать Aspose.3D for Java?

Aspose.3D for Java предоставляет высокоуровневый API, который устраняет необходимость ручных вычислений сетки, позволяя сосредоточиться на дизайне, а не на низкоуровневой геометрии. Он поддерживает **50+ input and output formats** — включая OBJ, FBX, STL и GLTF — поэтому вы можете **export 3d model obj** или любой другой формат одним вызовом метода. Библиотека обрабатывает сцены из сотен страниц без загрузки всего файла в память, обеспечивая **до 3× более быструю производительность** по сравнению с чистыми OpenGL‑конвейерами на типичном серверном оборудовании.

## Требования

Перед тем как приступить, убедитесь, что у вас есть:

1. **Java Development Environment** – JDK 8 или новее установлен.  
2. **Aspose.3D for Java** – Скачайте библиотеку и документацию [здесь](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Создайте папку на вашем компьютере для хранения сгенерированных файлов; будем называть её **«Your Document Directory»**.

## Импорт пакетов

В вашей Java‑IDE импортируйте необходимые классы Aspose.3D. Это предоставляет компилятору доступ к функциям экструзии и построения сцены.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Пошаговое руководство

### Шаг 1: Настройка базового профиля

Сначала создайте 2‑D форму, которая будет экструзироваться. Здесь мы используем прямоугольник и **set rounding radius** до 0.3, что сглаживает углы и демонстрирует, как **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Шаг 2: Создание 3D сцены

**Scene** — это контейнер верхнего уровня, который содержит все 3‑D объекты, источники света и камеры.

```java
Scene scene = new Scene();
```

### Шаг 3: Добавление левых и правых узлов

**Node** представляет трансформируемый объект в графе сцены, позволяя задавать позицию и иерархию.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Шаг 4: Линейная экструзия – без центра (левый узел)

**LinearExtrusion** преобразует 2‑D профиль в 3‑D сетку, перемещая его вдоль прямой линии.  
**setCenter(boolean)** переключает, будет ли экструзия центрирована относительно начала профиля.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Шаг 5: Добавление плоскости пола для ориентира (левый узел)

Тонкий короб служит визуальным полом, помогая увидеть ориентацию экструзии.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Шаг 6: Линейная экструзия – центрирована (правый узел)

Теперь повторите экструзию, включив `center`. Геометрия будет симметричной относительно начала профиля, давая вам идеально сбалансированный результат **create 3d mesh java**.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Шаг 7: Добавление плоскости пола для ориентира (правый узел)

Та же плоскость пола для правой стороны, чтобы сравнение было очевидным.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Шаг 8: Сохранение 3D сцены

Наконец, экспортируйте всю сцену в файл Wavefront OBJ — формат, который легко использовать в большинстве 3‑D редакторов. Метод `save` автоматически преобразует сетку в спецификацию OBJ, позволяя вам **save obj file java** без дополнительной постобработки.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Распространённые проблемы и решения

| Проблема | Почему происходит | Решение |
|----------|-------------------|---------|
| **Экструзия смещена** | `setCenter(false)` оставляет профиль привязанным к его углу. | Используйте `setCenter(true)` для симметричных результатов. |
| **Файл OBJ пустой** | Путь к выходному каталогу неверен или отсутствуют права записи. | Убедитесь, что `MyDir` указывает на существующую папку и приложение имеет права записи. |
| **Скруглённые углы выглядят острыми** | Радиус скругления слишком мал относительно размера прямоугольника. | Увеличьте значение радиуса (например, `setRoundingRadius(0.5)`). |

## Часто задаваемые вопросы

### Q1: Могу ли я использовать Aspose.3D for Java в коммерческих проектах?

A1: Да, Aspose.3D for Java доступен для коммерческого использования. Подробности о лицензировании см. [здесь](https://purchase.aspose.com/buy).

### Q2: Доступна ли бесплатная пробная версия?

A2: Да, вы можете опробовать бесплатную пробную версию Aspose.3D for Java [здесь](https://releases.aspose.com/).

### Q3: Где я могу найти поддержку Aspose.3D for Java?

A3: Форум сообщества Aspose.3D — отличное место для получения поддержки и обмена опытом. Посетите форум [здесь](https://forum.aspose.com/c/3d/18).

### Q4: Нужна ли временная лицензия для тестирования?

A4: Да, если вам нужна временная лицензия для тестирования, её можно получить [здесь](https://purchase.aspose.com/temporary-license/).

### Q5: Где я могу найти документацию?

A5: Документация Aspose.3D for Java доступна [здесь](https://reference.aspose.com/3d/java/).

## Заключение

Пройдя этот **java 3d graphics tutorial**, вы теперь знаете, как создавать объекты **create 3d mesh java**, управлять центром линейной экструзии, регулировать радиус скругления и получать вывод **save obj file java** с помощью Aspose.3D. Эти техники дают вам точный контроль над симметрией сетки, что важно для игровых ассетов, прототипов CAD и научных визуализаций. Не стесняйтесь экспериментировать с различными профилями, количеством срезов и форматами экспорта, чтобы расширить ваш 3‑D набор инструментов.

---

**Последнее обновление:** 2026-06-13  
**Тестировано с:** Aspose.3D for Java 24.11  
**Автор:** Aspose

## Связанные руководства

- [Создать 3D Extrusion Java с Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Как задать направление в линейной экструзии с Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Создать 3D сцену с кручением в линейной экструзии — Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}