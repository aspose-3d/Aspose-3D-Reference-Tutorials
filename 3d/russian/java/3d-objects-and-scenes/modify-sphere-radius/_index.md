---
date: 2025-11-30
description: Узнайте, как использовать Aspose в Java для изменения радиуса 3‑D сферы.
  Это пошаговое руководство охватывает библиотеку Aspose.3D Java, как установить радиус,
  добавить сферу в сцену и записать файл OBJ на Java.
language: ru
linktitle: 'How to Use Aspose: Modify 3D Sphere Radius in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'Как использовать Aspose: изменить радиус 3D‑сферы в Java с помощью Aspose.3D'
url: /java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Как использовать Aspose: изменить радиус 3D‑сферы в Java с помощью Aspose.3D

## Introduction

Если вы ищете **как использовать Aspose** для работы с 3D‑моделями в Java, вы попали по адресу. В этом руководстве мы пройдем каждый шаг, необходимый для изменения размера сферы, добавления её в сцену и, наконец, записи OBJ‑файла с использованием **библиотеки Aspose.3D Java** К концу у вас будет переиспользуемый фрагмент кода, который можно вставить в любое Java‑основанное 3D‑приложение.

## Quick Answers
- **Какова основная цель данного руководства?** Показать, как изменить радиус сферы с помощью Aspose.3D в Java.  
- **Какую библиотеку мы используем?** Библиотеку Aspose.3D Java (полнофункциональная **java 3d library**).  
- **Как установить радиус?** Вызвать `sphere.setRadius(double)` у объекта `Sphere`.  
- **Можно ли экспортировать в OBJ?** Да — используйте `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Нужна ли лицензия?** Бесплатная пробная версия подходит для разработки; для продакшн‑использования требуется лицензия.

## What is Aspose.3D for Java?

Aspose.3D — это **java 3d library**, позволяющая разработчикам создавать, редактировать и конвертировать 3D‑файлы без внешних зависимостей. Она поддерживает популярные форматы, такие как OBJ, FBX, STL и другие, что делает её идеальной для игр, САПР и научных визуализаций.

## Why Use Aspose.3D to Change Sphere Size?

- **Не требуется нативный 3D‑движок** — все операции выполняются над объектной моделью.  
- **Кроссплатформенность** — работает на любой ОС, где установлен Java.  
- **Высокоточная геометрия** — можно задавать точные значения радиуса, а не только приближённое масштабирование.  

## Prerequisites

- Базовые знания программирования на Java.  
- Установленная библиотека Aspose.3D — её можно скачать из [документации Aspose.3D for Java](https://reference.aspose.com/3d/java/).  
- Установленный Java Development Kit (JDK) на вашем компьютере.

## Import Packages

Чтобы начать, импортируйте необходимые классы в ваш Java‑проект:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Step 1: Initialize a Scene

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Здесь мы создаём новую **3D‑сцену**, которая будет содержать всю нашу геометрию.

## Step 2: Initialize a Sphere

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

Объект `Sphere` представляет идеальный примитив‑сферу. На данный момент он использует радиус по умолчанию 1.0.

## Step 3: How to Set Radius of a Sphere

```java
// set radius
sphere.setRadius(10);
```

Эта строка демонстрирует **как задать радиус**. Вы можете заменить `10` любым значением типа `double`, чтобы получить нужный размер.

## Step 4: Add Sphere to the Scene

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Вызов **добавляет сферу в сцену** (или «add sphere to scene») путем создания дочернего узла под корневым узлом.

## Step 5: Write OBJ File Java

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Наконец, мы **записываем OBJ‑файл** в стиле Java, используя `scene.save`. Выходной файл `sphere.obj` можно открыть в любом 3D‑просмотрщике, поддерживающем формат Wavefront OBJ.

## Common Issues and Solutions

| Проблема | Решение |
|----------|---------|
| **Сфера выглядит слишком маленькой в просмотрщике** | Убедитесь, что значение радиуса установлено правильно; помните, что единицы измерения произвольны, если только вы не применяете масштабирующее преобразование. |
| **Экспортированный OBJ не содержит материал** | Aspose.3D записывает только геометрию; добавьте материал к сфере, если нужны текстуры (`sphere.setMaterial(...)`). |
| **Исключение лицензии во время выполнения** | Убедитесь, что у вас загружен временный или постоянный файл лицензии перед созданием `Scene`. |

## Frequently Asked Questions

### Q: Where can I find the documentation for Aspose.3D for Java?

A: Обратитесь к [документации Aspose.3D for Java](https://reference.aspose.com/3d/java/) для получения полной информации и рекомендаций по использованию.

### Q: How do I download Aspose.3D for Java?

A: Скачайте библиотеку со страницы релизов: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### Q: Is there a free trial available for Aspose.3D for Java?

A: Да, изучите возможности с бесплатной пробной версией, посетив [Aspose.3D Free Trial](https://releases.aspose.com/).

### Q: Where can I get support for Aspose.3D for Java?

A: Присоединяйтесь к сообществу Aspose на [форуме поддержки Aspose.3D](https://forum.aspose.com/c/3d/18) для получения помощи и обсуждений.

### Q: How can I obtain a temporary license for Aspose.3D?

A: Получите временную лицензию, посетив [Temporary License](https://purchase.aspose.com/temporary-license/).

### Q: Can I use this code with other 3D formats like STL?

A: Конечно — просто измените перечисление `FileFormat` при вызове `scene.save`, например, `FileFormat.STL`.

## Conclusion

Теперь вы освоили **как использовать Aspose** для изменения радиуса сферы, добавления её в сцену и экспорта результата в OBJ‑файл на Java. Не стесняйтесь экспериментировать с другими примитивами, применять материалы или цепочкой выполнять несколько преобразований для создания более сложных 3D‑моделей.

---

**Последнее обновление:** 2025-11-30  
**Тестировано с:** Aspose.3D for Java 24.11  
**Автор:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}