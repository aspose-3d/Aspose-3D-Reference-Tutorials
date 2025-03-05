---
title: Настройте загрузку 3D-файлов в Java с помощью Aspose.3D LoadOptions
linktitle: Настройте загрузку 3D-файлов в Java с помощью Aspose.3D LoadOptions
second_title: Aspose.3D Java API
description: Улучшите загрузку 3D-файлов на Java с помощью настраиваемых параметров LoadOptions Aspose.3D. Изучите пошаговую настройку 3DS, OBJ, STL, U3D, glTF, PLY, X и дополнительного FBX.
type: docs
weight: 12
url: /ru/java/load-and-save/customize-3d-file-loading/
---
## Введение

В постоянно развивающемся мире 3D-проектирования и разработки решающее значение имеет эффективная обработка форматов 3D-файлов. Aspose.3D for Java предоставляет мощное решение для настройки загрузки различных форматов 3D-файлов. Это руководство проведет вас через процесс настройки загрузки 3D-файлов в Java с помощью LoadOptions Aspose.3D.

## Предварительные условия

Прежде чем приступить к процессу настройки, убедитесь, что у вас есть следующее:

- Базовое понимание программирования на Java.
- Установлен пакет разработки Java (JDK).
-  Скачана библиотека Aspose.3D для Java. Вы можете получить его[здесь](https://releases.aspose.com/3d/java/).
- Знакомство с форматами 3D-файлов, такими как 3DS, OBJ, STL, U3D, glTF, PLY, X и FBX.

## Импортировать пакеты

В вашем проекте Java обязательно импортируйте необходимые пакеты Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Настройте загрузку 3D-файлов

### Шаг 1. Настройте загрузку файлов 3DS

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

### Шаг 2. Настройте загрузку файла OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Шаг 3. Настройте загрузку файла STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Шаг 4. Настройте загрузку файлов U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Шаг 5. Настройте загрузку файла glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Шаг 6. Настройте загрузку файла PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Шаг 7. Настройте загрузку X-файла

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Шаг 8. Настройте загрузку файлов FBX (необязательно)

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

## Заключение

Настройка загрузки 3D-файлов в Java с помощью LoadOptions Aspose.3D позволяет разработчикам адаптировать процесс импорта к конкретным требованиям. Будь то настройка преобразований анимации, переворачивание систем координат или обработка внешних зависимостей, Aspose.3D обеспечивает гибкость, необходимую для плавной интеграции.

## Часто задаваемые вопросы

### Вопрос 1: Где я могу найти документацию Aspose.3D для Java?

 A1: документация доступна[здесь](https://reference.aspose.com/3d/java/).

### Вопрос 2: Как загрузить Aspose.3D для Java?

 A2: Вы можете скачать его[здесь](https://releases.aspose.com/3d/java/).

### В3: Есть ли бесплатная пробная версия?

 О3: Да, вы можете получить доступ к бесплатной пробной версии.[здесь](https://releases.aspose.com/).

### Вопрос 4: Где я могу получить поддержку Aspose.3D для Java?

 A4: Посетите форум поддержки.[здесь](https://forum.aspose.com/c/3d/18).

### В5: Нужна ли мне временная лицензия для тестирования?

 A5: Да, получите временную лицензию[здесь](https://purchase.aspose.com/temporary-license/).