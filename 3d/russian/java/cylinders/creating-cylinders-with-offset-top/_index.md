---
date: 2026-04-08
description: Узнайте, как создать цилиндр со смещённой верхней частью в Aspose.3D
  для Java, добавить дочерний узел Java, установить смещение верхней части, сгенерировать
  3D‑модель и экспортировать OBJ, используя временную лицензию Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Временная лицензия Aspose – Создать цилиндр со смещённым верхом (Java)
second_title: Aspose.3D Java API
title: Временная лицензия Aspose – Создать цилиндр со смещённым верхом (Java)
url: /ru/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Temporary License – Создание цилиндра со смещённым верхом (Java)

## Введение

If you’re looking to **create cylinder** objects with a custom offset top in a Java‑based 3D scene, Aspose.3D makes the process straightforward. In this tutorial we’ll walk through every step—from setting up the scene to exporting the final model as an OBJ file—so you can integrate offset‑top cylinders into your applications with confidence. By the end of the guide you’ll also understand how an **aspose temporary license** lets you evaluate these features without a full purchase.

## Быстрые ответы
- **Какая библиотека используется?** Aspose.3D for Java  
- **Можно ли сместить верх цилиндра?** Да, using `setOffsetTop`  
- **Как добавить дочерний узел в Java?** Call `createChildNode` on the root node  
- **В какой формат можно экспортировать?** Wavefront OBJ (`java export obj`)  
- **Нужна ли лицензия для тестирования?** An **aspose temporary license** is available for evaluation  

## Что такое Aspose Temporary License?

An **aspose temporary license** is a short‑term, free evaluation key that unlocks the full feature set of Aspose.3D for Java during development and testing. It removes evaluation watermarks and allows you to generate 3D model files, such as OBJ, STL, or FBX, exactly as a paid license would.

## Почему использовать Aspose.3D for Java?

- **High‑level API:** No need to manage low‑level mesh data.  
- **Cross‑platform:** Works on any JVM‑compatible environment.  
- **Built‑in exporters:** Directly save to OBJ, STL, FBX, and more.  
- **Extensible:** Easily add child nodes, apply transformations, and integrate with other Java libraries.  

## Необходимые условия

- **Java Development Kit (JDK)** – a compatible version installed.  
- **Aspose.3D for Java library** – download the latest JAR from the official site [here](https://releases.aspose.com/3d/java/).  
- An IDE of your choice (Eclipse, IntelliJ IDEA, NetBeans, etc.).  

## Импорт пакетов

First, import the classes we’ll need. Place these statements at the top of your Java file:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Пошаговое руководство

### Шаг 1: Создание Java 3D сцены

A **java 3d scene** acts as the container for all 3D objects.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Шаг 2: Инициализация цилиндра со смещённым верхом

Here we answer **how to create cylinder** with a custom offset. The constructor defines radius, height, slices, stacks, and whether the cylinder is closed. After that, we shift the top using `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Шаг 3: Добавление дочернего узла Java – Присоединение первого цилиндра

We create a child node under the scene’s root node and move the cylinder to a desired location.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Шаг 4: Инициализация второго цилиндра (без смещения)

For comparison, we add a regular cylinder without an offset.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Шаг 5: Добавление дочернего узла Java – Присоединение второго цилиндра

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Шаг 6: Java Export OBJ – Сохранение сцены в OBJ

Finally, we **java export obj** the whole scene (both cylinders) as a Wavefront OBJ file, which is widely supported by 3D tools.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

When you run the program, you’ll find `CustomizedOffsetTopCylinder.obj` in the specified directory, ready to be opened in Blender, Maya, or any other OBJ‑compatible viewer.

## Как генерировать 3D‑модель и экспортировать OBJ в Java

The combination of `Scene.save(..., FileFormat.WAVEFRONTOBJ)` and the **aspose temporary license** lets you **generate 3d model** files quickly, without needing external converters. This is especially handy during prototyping or when sharing assets with designers.

## Примеры из реального мира

- **Architectural visualisation:** Offset‑top cylinders model columns that taper toward the ceiling.  
- **Mechanical parts:** Create pistons or gear housings where the top surface is intentionally shifted.  
- **Game assets:** Produce varied pillar shapes on the fly, reducing the need for hand‑crafted meshes.  

## Распространённые проблемы и решения

| Проблема | Причина | Решение |
|----------|---------|----------|
| **OBJ файл пустой** | Scene not saved correctly or wrong path. | Verify the output directory exists and you have write permissions. |
| **Смещение не применено** | Using an older Aspose.3D version. | Update to the latest library where `setOffsetTop` is supported. |
| **Дочерний узел не виден** | Transformation not applied. | Ensure you call `getTransform().setTranslation` after creating the child node. |

## Часто задаваемые вопросы

**Q: Совместим ли Aspose.3D с различными Java IDE?**  
A: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other IDEs.

**Q: Могу ли я применять текстуры к созданным 3D объектам?**  
A: Absolutely! Use the `Material` class to assign textures and surface properties.

**Q: Есть ли варианты лицензирования Aspose.3D?**  
A: Various licensing models are available; you can explore them [here](https://purchase.aspose.com/buy).

**Q: Как получить помощь или поделиться опытом?**  
A: Join the Aspose.3D community forum [here](https://forum.aspose.com/c/3d/18) for support and discussion.

**Q: Доступна ли временная лицензия для тестирования?**  
A: Yes, an **aspose temporary license** can be obtained for evaluation [here](https://purchase.aspose.com/temporary-license/).

---

**Последнее обновление:** 2026-04-08  
**Тестировано с:** Aspose.3D for Java 24.12 (latest)  
**Автор:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}