---
date: 2026-02-22
description: Узнайте, как создать 3D‑выдавливание с срезами с помощью Aspose.3D для
  Java. Это пошаговое руководство охватывает линейное выдавливание, установку радиуса
  скругления и экспорт OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Создание 3D‑экструзии со срезами – Aspose.3D для Java
url: /ru/java/linear-extrusion/specifying-slices/
weight: 13
---

 URLs unchanged. Also keep Hugo shortcodes unchanged. Ensure we translate headings and content.

We must not translate code block placeholders; they are not actual code but placeholders. Keep them as is.

We need to translate bullet points, tables, etc.

Let's produce final content.

Be careful: In tables, keep pipes and content; translate Issue, Why it Happens, Fix headings, and entries.

Also translate FAQ questions and answers.

Also translate "Last Updated", "Tested With", "Author". Keep dates.

Let's craft translation.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Создание 3D-экструзии с помощью срезов – Aspose.3D for Java

## Введение

Если вам нужно **создать 3d‑экструзию** объектов, выглядящих гладко и точно, ключевым параметром является количество срезов. В этом руководстве мы пройдемся по тому, как задать количество срезов при выполнении линейной экструзии с Aspose.3D for Java. Вы узнаете, почему количество срезов важно, как установить радиус скругления и как экспортировать результат в файл OBJ, который можно использовать в любой 3D‑конвейер.

## Быстрые ответы
- **Что контролируют «срезы»?** Количество промежуточных поперечных сечений, используемых для аппроксимации поверхности экструзии.  
- **Каким методом задаётся количество срезов?** `LinearExtrusion.setSlices(int)`  
- **Можно ли изменить радиус скругления профиля?** Да, через `RectangleShape.setRoundingRadius(double)`  
- **Какой формат файла используется в этом примере?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Нужна ли лицензия для запуска кода?** Бесплатная пробная версия подходит для оценки; для производства требуется коммерческая лицензия.

## Что такое линейная экструзия с срезами?

Линейная экструзия берёт 2‑D‑профиль (например, прямоугольник) и растягивает его вдоль прямой линии, образуя 3‑D‑твердое тело. Указывая **срезы**, вы сообщаете Aspose.3D, сколько промежуточных шагов сгенерировать, что напрямую влияет на гладкость изогнутых краёв, таких как скруглённый прямоугольник.

## Почему стоит использовать Aspose.3D for Java для создания 3d‑экструзии?

* **Полный контроль** – Вы можете программно регулировать количество срезов, радиус скругления и формат экспорта.  
* **Кросс‑платформенность** – Работает в любой среде с поддержкой Java без нативных зависимостей.  
* **Гибкость экспорта** – Прямой экспорт в OBJ, FBX, STL и многие другие форматы.

## Предварительные требования

1. **Java Development Kit** – установлен JDK 8 или выше.  
2. **Aspose.3D for Java** – Скачайте библиотеку с официального сайта [здесь](https://releases.aspose.com/3d/java/).  
3. Любая IDE или текстовый редактор по вашему выбору.

## Импорт пакетов

Добавьте пространство имён Aspose.3D в ваш проект, чтобы получить доступ к классам 3‑D‑моделирования.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Пошаговое руководство

### Шаг 1: Настройка сцены и определение профиля

Сначала создаём `RectangleShape` и задаём ему **радиус скругления**, чтобы углы были гладкими. Затем инициализируем новый `Scene`, который будет содержать всю геометрию.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Шаг 2: **Создание дочерних узлов** для каждой экструзии

Каждый элемент геометрии находится под `Node`. Здесь мы создаём два соседних узла – один для экструзии с небольшим количеством срезов, другой – с большим количеством – и смещаем левый узел немного в сторону, чтобы результаты было удобно сравнивать.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Шаг 3: Выполнение линейной экструзии и **установка срезов**

Теперь мы действительно **создаём 3d‑экструзию** объектов. Конструктор `LinearExtrusion` принимает профиль и глубину экструзии. С помощью **анонимного внутреннего класса** вызываем `setSlices`, чтобы контролировать гладкость. Левый узел получает только 2 среза (грубая), а правый – 10 срезов (гладкая).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Шаг 4: **Экспорт OBJ** – сохранение сцены

Наконец, сохраняем сцену в файл Wavefront OBJ, формат, широко поддерживаемый 3‑D‑редакторами и игровыми движками. Это демонстрирует возможность **export obj java** в Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Распространённые проблемы и решения

| Проблема | Почему происходит | Решение |
|----------|-------------------|---------|
| **Экструзия выглядит плоской** | Количество срезов установлено в 1 или 0 | Убедитесь, что `setSlices` вызывается со значением ≥ 2. |
| **Скруглённые углы выглядят зубчатыми** | Радиус скругления слишком мал относительно количества срезов | Увеличьте либо радиус, либо количество срезов для более плавных кривых. |
| **Файл не найден при сохранении** | `MyDir` указывает на несуществующую папку | Создайте каталог заранее или используйте абсолютный путь. |

## Часто задаваемые вопросы

**В: Как скачать Aspose.3D for Java?**  
О: Вы можете скачать библиотеку [здесь](https://releases.aspose.com/3d/java/).

**В: Где найти документацию по Aspose.3D?**  
О: Обратитесь к документации [здесь](https://reference.aspose.com/3d/java/).

**В: Есть ли бесплатная пробная версия?**  
О: Да, бесплатную пробную версию можно получить [здесь](https://releases.aspose.com/).

**В: Как получить поддержку по Aspose.3D?**  
О: Посетите форум поддержки [здесь](https://forum.aspose.com/c/3d/18).

**В: Можно ли приобрести временную лицензию?**  
О: Да, временную лицензию можно оформить [здесь](https://purchase.aspose.com/temporary-license/).

---

**Последнее обновление:** 2026-02-22  
**Тестировано с:** Aspose.3D for Java 24.11 (последняя на момент написания)  
**Автор:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}