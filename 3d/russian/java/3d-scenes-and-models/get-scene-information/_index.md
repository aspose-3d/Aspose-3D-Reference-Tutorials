---
date: 2026-09-08
description: Узнайте, как определить единицы измерения и экспортировать сцену в FBX
  на Java с помощью Aspose.3D. Это пошаговое руководство показывает, как задать имя
  приложения, единицы измерения и получить информацию о 3D‑сцене.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Как сохранить FBX и получить информацию о 3D‑сцене на Java
og_description: Узнайте, как определить единицы измерения и экспортировать сцену в
  FBX на Java с Aspose.3D. Руководство охватывает настройку имени приложения, единиц
  измерения и получение информации о 3D‑сцене за несколько шагов.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Как определить единицы измерения и экспортировать сцену в FBX на Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Как определить единицы измерения и экспортировать сцену в FBX на Java
url: /ru/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Как определить единицы измерения и экспортировать сцену в FBX на Java

## Введение

Если вы ищете понятное, практическое руководство по **определению единиц измерения** и **экспорту сцены в FBX**, одновременно извлекая полезные метаданные из ваших 3D‑сцен, вы попали по адресу. В этом уроке мы пройдем каждый шаг, используя библиотеку **Aspose.3D for Java**: от создания сцены, **установки имени приложения**, **определения единиц измерения**, до окончательного **экспорта сцены в FBX**. К концу вы получите готовый FBX‑файл, содержащий информацию об объекте, необходимую для последующих конвейеров.

## Быстрые ответы
- **Какова основная цель?** Экспортировать сцену в FBX, содержащую пользовательскую информацию об объекте.  
- **Какая библиотека используется?** Aspose.3D for Java.  
- **Нужна ли лицензия?** Бесплатная пробная версия подходит для разработки; для продакшна требуется коммерческая лицензия.  
- **Можно ли изменить единицы измерения?** Да — используйте `setUnitName` и `setUnitScaleFactor`.  
- **Куда сохраняется результат?** По пути, указанному в `scene.save(...)`.  

## Предварительные требования

Прежде чем начать, убедитесь, что у вас есть:

- Твердое понимание базового синтаксиса Java.  
- **Aspose.3D for Java** скачан и добавлен в ваш проект (можно получить на официальной) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Ваш любимый Java‑IDE (IntelliJ IDEA, Eclipse, NetBeans и т.д.) правильно настроен.

## Импорт пакетов

В вашем Java‑файле импортируйте классы Aspose.3D, предоставляющие работу со сценами и поддержку форматов файлов.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Держите список импортов минимальным, чтобы избежать лишних зависимостей и ускорить компиляцию.

## Как происходит сохранение FBX‑файла?

Чтобы сохранить сцену как FBX‑файл, вы создаёте `Scene`, задаёте нужные метаданные объекта, определяете единицу измерения и вызываете `scene.save(path, FileFormat.FBX7500ASCII)`. Эта последовательность записывает геометрию, материалы и метаданные в ASCII‑FBX, который можно просмотреть или импортировать в последующие инструменты.

### Шаг 1: инициализация 3D‑сцены

Класс `Scene` — это верхний контейнер Aspose.3D, представляющий всю 3D‑сцену, включая геометрию, источники света, камеры и метаданные. Сначала создайте пустой объект `Scene`. Он будет контейнером для всей геометрии, света, камер и метаданных объекта.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Как задать имя приложения в Java

Объект `AssetInfo` хранит метаданные, такие как имя приложения, поставщик и версия сцены. Добавление пользовательских метаданных помогает downstream‑инструментам определить источник файла. Используйте объект `AssetInfo`, чтобы **задать имя приложения** (и поставщика) перед сохранением файла.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Why this matters:** Многие конвейеры фильтруют или помечают объекты на основе исходного приложения, поэтому этот шаг критически важен для крупных проектов.

### Шаг 3: определение единиц измерения

Система единиц определяет реальный масштаб сцены; Aspose.3D позволяет задать имя единицы и коэффициент масштабирования относительно метров. В этом примере мы используем древнеегипетскую единицу «pole» с пользовательским коэффициентом масштабирования.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Настройте `unitScaleFactor` в соответствии с реальными размерами ваших моделей; 1.0 представляет 1‑к‑1 соответствие с выбранной единицей.

### Шаг 4: экспорт сцены в FBX

После того как информация об объекте прикреплена, сохраняем сцену как FBX‑файл. Параметр `FileFormat.FBX7500ASCII` создаёт человекочитаемый ASCII‑FBX, удобный для отладки.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Remember:** Замените `"Your Document Directory"` на абсолютный путь или путь, относительный к рабочей директории вашего проекта.

## Почему экспортировать сцену в FBX с Aspose.3D?

Aspose.3D поддерживает **более 50 форматов ввода и вывода** и может обрабатывать сцены сотен страниц без загрузки всего файла в память, предоставляя полный контроль над экспортируемым файлом — метаданные, единицы измерения и геометрию — без необходимости тяжёлого 3D‑редактора. Это делает автоматизированную генерацию ресурсов, пакетную обработку и серверные конвертации быстрыми и надёжными.

## Распространённые сценарии использования

- **Конвейеры игровых активов** — встраивание информации о создателе непосредственно в FBX‑файлы для отслеживания версий.  
- **Архитектурная визуализация** — хранение специфических для проекта единиц, чтобы избежать ошибок масштабирования при импорте в движки рендеринга.  
- **Автоматизированные отчёты** — генерация FBX‑файлов «на лету» с метаданными, которые могут считывать downstream‑аналитические инструменты.  
- **Облачные 3D‑сервисы** — программное создание и экспорт сцен без GUI, идеально для SaaS‑платформ.

## Устранение неполадок и советы

| Проблема | Решение |
|-------|----------|
| **Файл не найден после сохранения** | Убедитесь, что `MyDir` указывает на существующую папку и у вашего приложения есть права записи. |
| **Единицы отображаются некорректно во внешнем просмотрщике** | Проверьте `unitScaleFactor`; некоторые просмотрщики ожидают метры в качестве базовой единицы. |
| **Метаданные объекта отсутствуют** | Убедитесь, что вызываете `scene.getAssetInfo()` **до** сохранения; изменения после `save()` не сохраняются. |
| **Узкое место производительности на больших сценах** | Вызовите `scene.optimize()` перед сохранением, чтобы уменьшить использование памяти. |
| **ASCII FBX слишком велик** | Переключитесь на бинарный FBX, используя `FileFormat.FBX7500` (см. FAQ). |

## Часто задаваемые вопросы

**В: Как изменить формат вывода на бинарный FBX?**  
О: Замените `FileFormat.FBX7500ASCII` на `FileFormat.FBX7500` при вызове `scene.save(...)`.

**В: Можно ли добавить пользовательские метаданные, выходящие за рамки встроенных полей объекта?**  
О: Да, используйте `scene.getUserData().add("Key", "Value")` для встраивания дополнительных пар «ключ‑значение».

**В: Поддерживает ли Aspose.3D другие форматы экспорта, такие как OBJ или GLTF?**  
О: Поддерживает. Просто измените перечисление `FileFormat` на `OBJ` или `GLTF2` по необходимости.

**В: Какая версия Java требуется?**  
О: Aspose.3D for Java поддерживает Java 8 и новее.

**В: Можно ли загрузить существующий FBX, изменить его информацию об объекте и сохранить заново?**  
О: Конечно. Загрузите файл с помощью `new Scene("input.fbx")`, измените `scene.getAssetInfo()`, затем сохраните.

---

**Последнее обновление:** 2026-09-08  
**Тестировано с:** Aspose.3D for Java 24.11  
**Автор:** Aspose

## Связанные уроки

- [Reduce 3D File Size – Compress Scenes with Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [How to set vector3 color java: Change Diffuse Color and Manage 3D Properties in Java Scenes using Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}