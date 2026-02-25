---
date: 2026-02-25
description: Узнайте, как изменить систему координат и настроить импорт 3D с помощью
  Aspose.3D LoadOptions в Java. Пошаговое руководство для 3DS, OBJ, STL, U3D, glTF,
  PLY, X и, при необходимости, FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Перевернуть систему координат – Настройте загрузку 3D‑файлов в Java с Aspose.3D
url: /ru/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Переворот системы координат – Настройка загрузки 3D‑файлов в Java с Aspose.3D

В постоянно меняющемся мире 3D‑дизайна и разработки **переворот системы координат** при импорте моделей является распространённым требованием. Независимо от того, конвертируете ли вы ресурсы из правосторонней в левостороннюю систему или нужно согласовать модели с конвенциями осей вашего движка, Aspose.3D for Java предоставляет тонкий контроль. В этом руководстве мы покажем, как **настроить импорт 3D** с помощью `LoadOptions` Aspose.3D, охватывая самые популярные форматы, такие как 3DS, OBJ, STL, U3D, glTF, PLY, X и дополнительный FBX.

## Быстрые ответы
- **Что делает «переворот системы координат»?** Он меняет местами оси X/Y/Z, чтобы соответствовать целевой системе координат.  
- **Какие форматы поддерживают переворот?** Все основные форматы (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) предоставляют параметр `setFlipCoordinateSystem`.  
- **Нужны ли дополнительные библиотеки?** Только JAR‑файл Aspose.3D for Java; внешние конвертеры не требуются.  
- **Можно ли загружать материалы одновременно?** Да — используйте `setEnableMaterials(true)` для файлов OBJ.  
- **Требуется ли лицензия для продакшн?** Для не‑тестовых развертываний необходима действующая лицензия Aspose.3D.

## Что такое «переворот системы координат»?
Переворот системы координат меняет ориентацию осей, используемых импортируемой моделью. Это необходимо, когда исходный файл использует другую «руку» (правостороннюю vs. левостороннюю), чем ваш движок рендеринга, предотвращая отображение моделей в виде зеркального отражения или инверсии.

## Зачем настраивать импорт 3D?
- Сохранить трансформации анимации (`setApplyAnimationTransform`).  
- Корректно обрабатывать цвета (`setGammaCorrectedColor`).  
- Разрешать пути к внешним ресурсам с помощью `getLookupPaths()`.  
- Оптимизировать использование памяти, загружая только необходимое.

## Предварительные требования

- Базовые знания программирования на Java.  
- Установленный Java Development Kit (JDK).  
- Скачанная библиотека Aspose.3D for Java. Вы можете получить её [здесь](https://releases.aspose.com/3d/java/).  
- Знание 3D‑форматов файлов, таких как 3DS, OBJ, STL, U3D, glTF, PLY, X и FBX.

## Импорт пакетов

В вашем Java‑проекте убедитесь, что импортированы необходимые пакеты Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Как настроить импорт 3D с помощью LoadOptions

Ниже представлены пошаговые фрагменты кода, демонстрирующие, как включить опцию **переворота системы координат** для каждого поддерживаемого формата. Фрагменты готовы к копированию в ваш проект; просто замените `"Your Document Directory"` на реальный путь к вашим ресурсам.

### Шаг 1: Настройка загрузки файлов 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Шаг 2: Настройка загрузки файлов OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Шаг 3: Настройка загрузки файлов STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Шаг 4: Настройка загрузки файлов U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Шаг 5: Настройка загрузки файлов glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Шаг 6: Настройка загрузки файлов PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Шаг 7: Настройка загрузки файлов X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Шаг 8: Настройка загрузки файлов FBX (необязательно)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Распространённые проблемы и решения
- **Модель выглядит зеркально после загрузки** — Убедитесь, что `setFlipCoordinateSystem(true)` установлен для нужного формата.  
- **Отсутствуют материалы** — Для файлов OBJ убедитесь, что включён `setEnableMaterials(true)` и файлы материалов (.mtl) находятся в одном из путей поиска.  
- **Текстурные координаты перевёрнуты** — Для glTF может потребоваться `setFlipTexCoordV(true)` в дополнение к перевороту осей.  
- **Ошибки «файл не найден»** — Добавьте каталог, содержащий внешние ресурсы (текстуры, вспомогательные файлы), в `loadOpts.getLookupPaths()`.

## Заключение

Используя `LoadOptions` Aspose.3D, вы можете **перевернуть систему координат** и **настроить импорт 3D** практически для всех основных форматов. Такой уровень контроля устраняет необходимость в скриптах пост‑обработки и гарантирует корректный рендеринг ваших ресурсов с первого раза.

## Часто задаваемые вопросы

### Вопрос 1: Где найти документацию Aspose.3D for Java?
A1: Документация доступна [здесь](https://reference.aspose.com/3d/java/).

### Вопрос 2: Как скачать Aspose.3D for Java?
A2: Вы можете скачать её [здесь](https://releases.aspose.com/3d/java/).

### Вопрос 3: Есть ли бесплатная пробная версия?
A3: Да, бесплатную пробную версию можно получить [здесь](https://releases.aspose.com/).

### Вопрос 4: Где получить поддержку по Aspose.3D for Java?
A4: Посетите форум поддержки [здесь](https://forum.aspose.com/c/3d/18).

### Вопрос 5: Нужна ли временная лицензия для тестирования?
A5: Да, временную лицензию можно получить [здесь](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Последнее обновление:** 2026-02-25  
**Тестировано с:** Aspose.3D for Java 24.11 (latest)  
**Автор:** Aspose