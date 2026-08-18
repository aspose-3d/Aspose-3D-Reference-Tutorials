---
date: 2026-06-03
description: Узнайте, как экспортировать сцену в FBX и создавать 3D cylinder, box
  и другие primitive модели с использованием Aspose.3D for Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Создание Primitive 3D моделей с Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Экспортировать сцену в FBX и создать cylinder с Aspose.3D Java
url: /ru/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Экспорт сцены в FBX и построение цилиндра с Aspose.3D Java

## Введение

Если вам когда‑нибудь нужно было **создать 3D цилиндр** (или любую другую базовую форму) напрямую из кода Java, Aspose.3D делает эту задачу простой. В этом руководстве мы пройдём весь процесс — от настройки окружения до **экспорта сцены в FBX** — чтобы вы могли сразу начать программно генерировать 3D геометрию. Вы увидите, как библиотека работает с примитивами, как организовать их в графе сцены и как сохранить результат в формате, который могут читать Unity, Blender или любой другой 3D‑инструмент.

## Быстрые ответы
- **Какая библиотека позволяет создать 3D цилиндр в Java?** Aspose.3D for Java.  
- **В какой формат можно экспортировать сцену?** FBX (ASCII 7500) с использованием `FileFormat.FBX7500ASCII`.  
- **Нужна ли лицензия для разработки?** Бесплатная пробная версия подходит для тестирования; для продакшна требуется постоянная лицензия.  
- **Какие основные примитивы поддерживаются?** Box, Cylinder, Sphere, Cone и более 10 дополнительных фигур.  
- **Совместим ли код с Java 8 и новее?** Да, Aspose.3D ориентирован на JDK 8+.

## Что такое примитив 3D цилиндра?

Примитив цилиндра — это базовая геометрическая форма, определяемая радиусом и высотой. Во многих 3D‑конвейерах он служит строительным блоком для более сложных моделей, таких как трубы, колёса или архитектурные колонны. Aspose.3D предоставляет готовый класс `Cylinder`, поэтому вам не нужно вручную рассчитывать вершины.

## Почему использовать Aspose.3D для Java?

Aspose.3D for Java предлагает комплексный, полностью Java‑based 3D‑движок, который устраняет необходимость в нативных библиотеках, делая его идеальным для кросс‑платформенной разработки. Он поддерживает широкий спектр форматов импорта и экспорта, предоставляет надёжный граф сцены для иерархической организации и включает встроенные примитивы, позволяющие создавать геометрию с минимальным количеством кода. Эти возможности ускоряют разработку и снижают затраты на обслуживание.

- **Полнофункциональный 3D‑движок** — поддерживает импорт/экспорт **более 30** популярных форматов (FBX, OBJ, STL, GLTF, 3DS и др.).  
- **Чистый Java API** — без нативных зависимостей, идеально подходит для кросс‑платформенных проектов.  
- **Надёжный граф сцены** — позволяет организовывать объекты иерархически, упрощая управление большими сценами.  
- **Простая лицензия** — начните с бесплатной пробной версии, затем перейдите на постоянную лицензию при запуске.

## Требования

Прежде чем погрузиться в код, убедитесь, что у вас есть:

1. **Java Development Kit (JDK)** — установлен JDK 8 или новее.  
2. **Библиотека Aspose.3D for Java** — скачайте и установите её со [страницы загрузки](https://releases.aspose.com/3d/java/).  

## Импорт пакетов

Начните с импорта основного пространства имён Aspose.3D. Это даст вам доступ к `Scene`, `Box`, `Cylinder` и константам форматов файлов.

```java
import com.aspose.threed.*;
```

Теперь, когда библиотека подключена, создадим сцену и добавим примитивную геометрию.

## Как экспортировать сцену в FBX и создать 3D примитивы?

Создайте новый объект `Scene`, добавьте узлы‑примитивы (Box, Cylinder и др.), а затем вызовите `save` с форматом FBX7500ASCII. Всего в несколько строк вы получите полностью функциональный FBX‑файл, который можно открыть в любом крупном 3D‑редакторе, обеспечивая бесшовную интеграцию с игровыми движками, конвейерами рендеринга или AR/VR‑приложениями.

### Шаг 1: Инициализация объекта Scene

Класс `Scene` — это верхний контейнер Aspose.3D, который хранит в памяти все узлы, источники света, камеры и материалы.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Шаг 2: Создание 3D модели коробки

Класс `Box` представляет прямоугольный параллелепипед и полезен для тестирования системы координат. Добавление его в качестве дочернего узла корня сцены размещает его в начале координат.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Шаг 3: Создание 3D модели цилиндра

Класс `Cylinder` — встроенный примитив цилиндра в Aspose.3D. Он имеет размеры по умолчанию (radius = 1, height = 2), но вы можете изменить их через конструктор.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Шаг 4: Сохранение рисунка в формате FBX

После сборки сцены экспортируйте её, чтобы другие инструменты (например, Unity, Blender) могли её прочитать. Мы используем формат `FBX7500ASCII`, который широко поддерживается и читаем человеком.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Распространённые проблемы и решения

| Проблема | Почему происходит | Решение |
|----------|-------------------|---------|
| **File not found** при сохранении | `myDir` указывает на несуществующую папку | Убедитесь, что каталог существует, или создайте его с помощью `new File(myDir).mkdirs();` |
| **Empty scene** после экспорта | Перед вызовом `save` не были добавлены узлы | Проверьте, что вызовы `createChildNode` выполнены (отладьте с помощью `scene.getRootNode().getChildCount()` ) |
| **License exception** | Запуск без действующей лицензии в продакшн‑среде | Примените временную или постоянную лицензию, используя `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Часто задаваемые вопросы

**Q: Можно ли использовать Aspose.3D for Java с другими языками программирования?**  
A: Aspose.3D в основном поддерживает Java, но также доступны версии для .NET и C++.

**Q: Подходит ли Aspose.3D для сложных задач 3D‑моделирования?**  
A: Абсолютно. Он предоставляет полный набор функций — включая работу с мешами, назначение материалов и анимацию — что делает его пригодным как для простых примитивов, так и для сложных моделей.

**Q: Где можно найти дополнительную помощь и поддержку?**  
A: Посетите [форум Aspose.3D](https://forum.aspose.com/c/3d/18) для поддержки сообщества и обсуждений.

**Q: Можно ли попробовать Aspose.3D перед покупкой?**  
A: Да, вы можете ознакомиться с [бесплатной пробной версией](https://releases.aspose.com/) перед принятием решения о покупке.

**Q: Как получить временную лицензию для Aspose.3D?**  
A: Вы можете получить [временную лицензию](https://purchase.aspose.com/temporary-license/) для Aspose.3D через веб‑сайт.

## Заключение

Теперь вы знаете, как **экспортировать сцену в FBX** и как **создавать 3D цилиндр**, коробку и другие примитивные модели с помощью Aspose.3D for Java. Не стесняйтесь экспериментировать с дополнительными примитивами, такими как Sphere, Cone или Torus, и изучать назначение материалов, чтобы придать моделям реалистичный вид. Как только вы освоитесь, вы сможете интегрировать сгенерированные FBX‑файлы в игровые движки, AR/VR‑конвейеры или любой последующий 3D‑рабочий процесс.

---

**Последнее обновление:** 2026-06-03  
**Тестировано с:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Автор:** Aspose

## Связанные руководства

- [Как экспортировать сцену в FBX и получить информацию о 3D сцене в Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Как экспортировать FBX и построить иерархию узлов в Java](/3d/java/geometry/build-node-hierarchies/)
- [Как создать модели цилиндров с Aspose.3D for Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}