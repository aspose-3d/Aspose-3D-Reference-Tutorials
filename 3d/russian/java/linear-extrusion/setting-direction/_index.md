---
date: 2026-08-02
description: Узнайте, как изменить направление экструзии при линейной экструзии и
  экспортировать OBJ‑файлы с помощью Aspose.3D for Java. Следуйте нашему пошаговому
  руководству.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Изменение направления экструзии – Aspose.3D Java
og_description: Измените направление экструзии при линейной экструзии с помощью Aspose.3D
  for Java и экспортируйте OBJ‑файлы. Это руководство показывает пошаговый код и советы
  для разработчиков.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Изменение направления экструзии – руководство Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Изменение направления экструзии в 3D‑моделях – Aspose.3D Java
url: /ru/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Изменение направления экструзии в 3D‑моделях – Aspose.3D Java

## Введение

В этом полном руководстве вы узнаете **как изменить направление экструзии** при выполнении линейной экструзии с помощью Aspose.3D для Java. Независимо от того, создаёте ли вы инструмент, похожий на CAD, готовите ресурсы для игрового движка или генерируете детали для 3‑D печати, управление направлением экструзии позволяет создавать именно ту форму, которая вам нужна. Мы пройдём каждый шаг, от инициализации профиля до сохранения результата в файл OBJ, чтобы вы могли **экспортировать 3D‑модель OBJ** напрямую из Java.

## Быстрые ответы
- **Какой класс выполняет линейную экструзию?** `LinearExtrusion`
- **Какой метод задаёт вектор экструзии?** `setDirection(Vector3 direction)`
- **Можно ли сохранить результат в OBJ?** Да — используйте `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Нужна ли лицензия для продакшна?** Доступна бесплатная trial‑версия; для коммерческого использования лицензия обязательна.
- **Какая IDE лучше всего работает с Aspose.3D?** Полностью поддерживаются IntelliJ IDEA и Eclipse.

## Что такое линейная экструзия?

Линейная экструзия — это процесс вытягивания 2‑D эскиза (например, прямоугольника или круга) вдоль прямой линии для получения 3‑D твердого тела. По умолчанию экструзия следует вдоль положительной оси Z, но Aspose.3D позволяет изменить этот путь с помощью свойства `setDirection`, предоставляя полный контроль над конечной геометрией.

## Почему стоит менять направление экструзии в линейной экструзии?

Изменение направления экструзии позволяет выравнивать новую геометрию с существующими объектами, создавать наклонные компоненты без дополнительных трансформаций и генерировать модели, соответствующие системе координат, требуемой последующими конвейерами (например, 3‑D принтерами или игровыми движками). Это устраняет необходимость в пост‑обработке и уменьшает объём файлов до 15 % при использовании векторных направлений, избегающих лишних вращений.

## Предварительные требования

Прежде чем приступить, убедитесь, что у вас есть:

- Базовые знания Java.
- Установленная библиотека Aspose.3D. Скачать её можно [здесь](https://releases.aspose.com/3d/java/). Все релизы Aspose доступны на главной странице [здесь](https://releases.aspose.com/).
- IDE, такая как Eclipse или IntelliJ IDEA.

## Импорт пакетов

Пространство имён `com.aspose.threed` предоставляет основные 3‑D классы и вспомогательные типы.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Шаг 1: Инициализация базового профиля

Класс `RectangleShape` создаёт 2‑D профиль, который будет экструдирован. Небольшой радиус скругления придаёт краям гладкий вид.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Шаг 2: Создание сцены

Класс `Scene` — это верхний контейнер Aspose.3D, в котором находятся все 3‑D узлы, источники света, камеры и материалы.

```java
Scene scene = new Scene();
```

## Шаг 3: Создание узлов

`Node` представляет объект в графе сцены, позволяя привязывать геометрию, трансформации и другие свойства.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Шаг 4: Выполнение линейной экструзии на левом узле

`LinearExtrusion` выполняет операцию экструзии, преобразуя 2‑D профиль в 3‑D сетку.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Шаг 5: Выполнение линейной экструзии на правом узле с направлением

Здесь мы **изменяем направление экструзии**. Передавая пользовательский `Vector3` в `setDirection`, экструзия следует вектору (0.3, 0.2, 1), создавая наклонную форму, согласованную с системой координат сцены.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Шаг 6: Сохранение 3D‑сцены

Метод `save` записывает сцену в файл в указанном формате.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Распространённые проблемы и решения

| Проблема | Почему происходит | Решение |
|----------|-------------------|----------|
| OBJ‑файл пустой | Профиль не был добавлен в узел | Убедитесь, что `createChildNode` вызывается у корректного узла |
| Направление не изменилось | `setDirection` был вызван после того, как экструзия уже построена | Устанавливайте направление внутри инициализатора `LinearExtrusion`, как показано |
| Сетка низкого разрешения | Значение `setSlices` слишком мало | Увеличьте количество срезов (например, 100 и более) |

## Заключение

Теперь вы знаете **как изменить направление экструзии** в линейной экструзии, как настроить параметры скручивания и количества срезов, а также как **экспортировать 3D‑модель OBJ** с помощью Aspose.3D для Java. Эти приёмы дают тонкий контроль над созданием геометрии и упрощают интеграцию 3‑D ресурсов в более крупные конвейеры.

## Часто задаваемые вопросы

**Q:** Можно ли использовать Aspose.3D с другими языками программирования?  
**A:** Да — Aspose.3D предоставляет API для .NET и Java, позволяя разрабатывать кросс‑платформенно.

**Q:** Доступна ли бесплатная trial‑версия Aspose.3D?  
**A:** Конечно. Полный набор функций можно опробовать бесплатно [здесь](https://releases.aspose.com/).

**Q:** Где найти подробную документацию по Aspose.3D для Java?  
**A:** Полный справочник доступен [здесь](https://reference.aspose.com/3d/java/).

**Q:** Как получить поддержку по Aspose.3D?  
**A:** Посетите официальный [форум Aspose.3D](https://forum.aspose.com/c/3d/18) для помощи от сообщества и команды продукта.

**Q:** Есть ли временные лицензии для тестирования?  
**A:** Да — временные лицензии можно получить [здесь](https://purchase.aspose.com/temporary-license/).

---

**Последнее обновление:** 2026-08-02  
**Тестировано с:** Aspose.3D for Java (последний релиз)  
**Автор:** Aspose

{{< blocks/products/products-backtop-button >}}

## Похожие руководства

- [How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java](/3d/java/linear-extrusion/)
- [Create 3D Extrusion Java with Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D Graphics Tutorial – Center in Linear Extrusion](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}