---
date: 2026-01-27
description: Изучите 3D‑моделирование на Java, создавая цилиндры со скошенным основанием
  с помощью Aspose.3D for Java. Этот учебник для начинающих по 3D показывает, как
  установить Aspose 3D, применить трансформацию сдвига и экспортировать OBJ‑файл в
  Java.
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Java 3D моделирование – Скошенные нижние цилиндры с Aspose.3D
url: /ru/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D моделирование – Скошенные нижние цилиндры с Aspose.3D

## Введение

Добро пожаловать в этот **java 3d modeling** урок! В этом пошаговом руководстве мы покажем, как создать цилиндр со скошенным основанием, используя библиотеку Aspose.3D для Java. Независимо от того, следуете ли вы **beginner 3d tutorial** или хотите добавить пользовательскую трансформацию сдвига к существующей модели, вы увидите, как настроить сцену, применить сдвиг и, наконец, **export OBJ file java** для использования в других инструментах.

## Быстрые ответы
- **Какая библиотека используется?** Aspose.3D for Java  
- **Можно ли установить Aspose 3D через Maven?** Yes – add the Aspose.3D dependency to your `pom.xml`  
- **Требуется ли лицензия для разработки?** A temporary license is sufficient for testing; a full license is needed for production  
- **Какой формат файла демонстрируется?** Wavefront OBJ (`.obj`)  
- **Сколько времени занимает выполнение примера?** Under a second on a typical workstation  

## Предварительные требования

- Java Development Kit (JDK) установлен на вашей системе.  
- **Install Aspose 3D** – скачайте библиотеку с официального сайта [here](https://releases.aspose.com/3d/java/).  
- IDE или система сборки (Maven/Gradle) для управления зависимостью Aspose.3D.  

## Импорт пакетов

Сначала импортируйте классы, которые нам понадобятся для сцены, геометрии и работы с файлами.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Шаг 1: Создание сцены

Сцена — это контейнер для всех 3‑D объектов. Мы начнём с создания пустой сцены.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Шаг 2: Создание цилиндра 1 – Как сдвинуть цилиндр

Теперь мы создадим первый цилиндр и **применим трансформацию сдвига** к его основанию. Это демонстрирует **how to shear cylinder** геометрию напрямую через API.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Шаг 3: Создание цилиндра 2 – Стандартный цилиндр (без сдвига)

Для сравнения мы добавим второй цилиндр, у которого **нет** скошенного основания.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Шаг 4: Сохранение сцены – Экспорт OBJ файла Java

Наконец, мы экспортируем сцену в файл Wavefront OBJ, демонстрируя использование **export obj file java**.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Почему это важно для Java 3D моделирования

Добавление сдвига к примитиву позволяет создавать более органические формы без обращения к внешним инструментам моделирования. Эта техника полезна для:

- Архитектурных визуализаций, где требуются наклонные основания.  
- Игровых ассетов, которым нужны пользовательские контуры при сохранении лёгкой геометрии.  
- Быстрого прототипирования, когда необходимо программно корректировать размеры.  

## Распространённые проблемы и решения

| Проблема | Решение |
|----------|---------|
| **Сдвиг выглядит слишком экстремальным** | Отрегулируйте значения `Vector2`; они представляют коэффициент сдвига (диапазон 0‑1). |
| **Файл OBJ не открывается в просмотрщике** | Убедитесь, что целевая директория существует и у вас есть права записи. |
| **Исключение лицензии во время выполнения** | Примените временную или постоянную лицензию перед созданием сцены (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Часто задаваемые вопросы

**Q: Можно ли использовать Aspose.3D для Java с другими Java 3D библиотеками?**  
A: Aspose.3D разработан для независимой работы. Хотя вы можете интегрировать его с другими библиотеками, он уже предоставляет полнофункциональный API для большинства 3‑D задач.

**Q: Подходит ли Aspose.3D для начинающих в 3D моделировании?**  
A: Абсолютно. API прост в использовании, и этот **beginner 3d tutorial** демонстрирует основные концепции с минимальным количеством кода.

**Q: Где я могу найти дополнительную поддержку для Aspose.3D для Java?**  
A: Посетите [Aspose.3D forum](https://forum.aspose.com/c/3d/18) для помощи от сообщества и официальных ответов.

**Q: Как получить временную лицензию для Aspose.3D?**  
A: Вы можете получить временную лицензию [здесь](https://purchase.aspose.com/temporary-license/).

**Q: Где купить полную лицензию Aspose.3D для Java?**  
A: Варианты покупки доступны [здесь](https://purchase.aspose.com/buy).

---

**Последнее обновление:** 2026-01-27  
**Тестировано с:** Aspose.3D 24.11 for Java  
**Автор:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
