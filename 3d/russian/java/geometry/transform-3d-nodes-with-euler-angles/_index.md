---
date: 2025-12-13
description: Узнайте, как использовать Aspose 3D Java для преобразования 3D‑узлов.
  Это руководство показывает, как применять углы Эйлера, добавлять 3D‑вращение и задавать
  трансляцию в Java.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Преобразование 3D‑узлов с помощью углов Эйлера
url: /ru/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Преобразование 3D‑узлов с помощью углов Эйлера в Java с использованием Aspose.3D

## Введение

В этом руководстве вы узнаете **how to use aspose 3d java** о том, как преобразовать 3D‑узлы, применяя углы Эйлера. К концу руководства вы сможете добавить вращение 3d, задать translation java и создавать динамические сцены, реагирующие на данные в реальном времени.

## Быстрые ответы
- **Какая библиотека обрабатывает 3D‑преобразования в Java?** Aspose 3D for Java.  
- **Какой метод задает вращение с использованием углов Эйлера?** `setEulerAngles()` on the node’s transform.  
- **Как переместить узел в пространстве?** Use `setTranslation()` with a `Vector3`.  
- **Нужна ли лицензия для продакшна?** Yes, a commercial Aspose 3D license is required.  
- **Можно ли экспортировать в FBX?** Absolutely – `scene.save(..., FileFormat.FBX7500ASCII)` works out of the box.

## Предварительные требования

Прежде чем погрузиться в руководство, убедитесь, что у вас есть следующие предварительные требования:

- Базовые знания программирования на Java.  
- Установленный Java Development Kit (JDK) на вашем компьютере.  
- Библиотека Aspose.3D, которую можно получить из [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## Импорт пакетов

Начните с импорта необходимых пакетов в ваш Java‑проект. Убедитесь, что библиотека Aspose.3D правильно добавлена в classpath. Если вы ещё не загрузили её, вы можете найти ссылку для загрузки [здесь](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Работа с углами Эйлера

### Шаг 1. Инициализация сцены и узла

Сначала создайте сцену и узел, который будет содержать геометрию, которую вы хотите преобразовать.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Шаг 2. Создание сетки и задание геометрии

Затем создайте простую сетку (в данном случае куб) и привяжите её к узлу.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Добавление 3D‑вращения к узлу

### Шаг 3. Задание углов Эйлера и трансляции

Теперь применяем вращение с помощью углов Эйлера и также перемещаем узел в видимую позицию.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Set Translation Java – Позиционирование узла

Шаг трансляции выше демонстрирует **set translation java** на практике: узел смещён на 20 единиц вдоль оси Z, чтобы его было видно после рендеринга.

## Шаг 4. Добавление узла в сцену

Присоедините преобразованный узел к корневому узлу сцены.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Шаг 5. Сохранение 3D‑сцены

Наконец, экспортируйте сцену в файл FBX (или любой другой поддерживаемый формат).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Убедитесь, что заменили `"Your Document Directory"` на соответствующий путь на вашем компьютере.

## Заключение

Поздравляем! Вы успешно преобразовали 3D‑узлы, используя углы Эйлера в Java с **aspose 3d java**. Экспериментируйте с различными углами и трансляциями, чтобы создавать динамичные и захватывающие 3D‑сцены.

## Часто задаваемые вопросы

**Q: В чём разница между углами Эйлера и вращением кватернионов?**  
A: Углы Эйлера интуитивны (pitch, yaw, roll), но могут страдать от блокировки кардана, тогда как кватернионы избегают этой проблемы и лучше подходят для плавных интерполяций.

**Q: Можно ли последовательно применять несколько преобразований к одному узлу?**  
A: Да. Вызывайте `setEulerAngles`, `setTranslation` и `setScale` в любом порядке; библиотека объединяет их в одну матрицу преобразования.

**Q: Можно ли экспортировать в другие форматы, такие как OBJ или STL?**  
A: Абсолютно. Замените `FileFormat.FBX7500ASCII` на `FileFormat.OBJ` или `FileFormat.STL` в вызове `scene.save`.

**Q: Как применить одинаковое вращение к нескольким узлам одновременно?**  
A: Создайте родительский узел, примените вращение к нему и добавьте дочерние узлы. Все дочерние узлы наследуют трансформацию.

**Q: Нужно ли вызывать какие‑либо методы очистки после сохранения?**  
A: Сборщик мусора Java освобождает большинство ресурсов, но при работе с большими сценами в длительно работающем приложении можно явно вызвать `scene.dispose()`.

---

**Последнее обновление:** 2025-12-13  
**Тестировано с:** Aspose.3D 23.12 for Java  
**Автор:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}