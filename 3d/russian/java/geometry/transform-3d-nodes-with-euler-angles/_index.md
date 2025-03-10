---
title: Преобразование 3D-узлов с помощью углов Эйлера в Java с помощью Aspose.3D
linktitle: Преобразование 3D-узлов с помощью углов Эйлера в Java с помощью Aspose.3D
second_title: Aspose.3D Java API
description: Исследуйте мир 3D-преобразований в Java с помощью Aspose.3D. Следуйте нашему пошаговому руководству, чтобы добавить динамические углы Эйлера к вашим 3D-узлам.
weight: 19
url: /ru/java/geometry/transform-3d-nodes-with-euler-angles/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Преобразование 3D-узлов с помощью углов Эйлера в Java с помощью Aspose.3D

## Введение

Добро пожаловать в это пошаговое руководство по преобразованию 3D-узлов с помощью углов Эйлера в Java с использованием Aspose.3D. В этом руководстве мы углубимся в процесс добавления преобразований к 3D-узлу, используя углы Эйлера для достижения динамического позиционирования и ориентации.

## Предварительные условия

Прежде чем мы углубимся в руководство, убедитесь, что у вас есть следующие предварительные условия:

- Базовые знания Java-программирования.
- На вашем компьютере установлен Java Development Kit (JDK).
-  Библиотека Aspose.3D, которую вы можете получить по адресу[Документация Aspose.3D Java](https://reference.aspose.com/3d/java/).

## Импортировать пакеты

 Начните с импорта необходимых пакетов в ваш Java-проект. Убедитесь, что библиотека Aspose.3D правильно добавлена в ваш путь к классам. Если вы еще не скачали его, вы можете найти ссылку для скачивания.[здесь](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## Шаг 1. Инициализируйте сцену и узел

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Инициализировать объект сцены
Scene scene = new Scene();

// Инициализировать объект класса Node
Node cubeNode = new Node("cube");
```

## Шаг 2. Создайте сетку и задайте геометрию

```java
// Вызов общего класса создает сетку, используя метод построения полигонов, чтобы установить экземпляр сетки.
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Наведите узел на геометрию сетки.
cubeNode.setEntity(mesh);
```

## Шаг 3. Установите углы Эйлера и перевод

```java
// углы Эйлера
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Установить перевод
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Шаг 4. Добавьте узел в сцену

```java
// Добавляем куб в сцену
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Шаг 5. Сохраните 3D-сцену

```java
// Путь к каталогу документов.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Сохранение 3D-сцены в поддерживаемых форматах файлов.
scene.save(MyDir, FileFormat.FBX7500ASCII);
// Эксенд: аддтрансформатионтонодебиеулеранглес
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Обязательно замените «Каталог ваших документов» соответствующим путем на вашем компьютере.

## Заключение

Поздравляем! Вы успешно преобразовали 3D-узлы с использованием углов Эйлера в Java с помощью Aspose.3D. Экспериментируйте с разными углами и перемещениями, чтобы создавать динамичные и захватывающие 3D-сцены.

## Часто задаваемые вопросы

### Вопрос 1: Могу ли я использовать Aspose.3D для Java в коммерческих проектах?

 А1: Да, вы можете. Посетить[страница покупки](https://purchase.aspose.com/buy) для получения подробной информации о лицензировании.

### В2: Где я могу найти поддержку Aspose.3D?

 А2:[Форум Aspose.3D](https://forum.aspose.com/c/3d/18) это место, где можно обратиться за помощью и пообщаться с сообществом.

### В3: Есть ли бесплатная пробная версия?

 A3: Да, вы можете изучить[бесплатная пробная версия](https://releases.aspose.com/) чтобы испытать возможности Aspose.3D.

### В4: Как я могу получить временную лицензию?

 A4: Вы можете получить временную лицензию[здесь](https://purchase.aspose.com/temporary-license/).

### В5: Где я могу найти документацию?

 A5:[документация](https://reference.aspose.com/3d/java/) предоставляет подробное руководство по использованию Aspose.3D для Java.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
