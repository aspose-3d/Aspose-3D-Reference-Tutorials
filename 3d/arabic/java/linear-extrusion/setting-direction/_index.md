---
date: 2026-08-02
description: تعلم كيفية تغيير اتجاه البثق في البثق الخطي وتصدير ملفات OBJ باستخدام
  Aspose.3D للغة Java. اتبع دليلنا خطوة بخطوة.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: تغيير اتجاه البثق – Aspose.3D Java
og_description: تغيير اتجاه البثق في البثق الخطي باستخدام Aspose.3D للغة Java وتصدير
  ملفات OBJ. يوضح هذا الدليل الكود خطوة بخطوة ونصائح للمطورين.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: تغيير اتجاه البثق – دليل Aspose.3D Java
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
title: تغيير اتجاه البثق في نماذج 3D – Aspose.3D Java
url: /ar/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تغيير اتجاه البثق في نماذج ثلاثية الأبعاد – Aspose.3D Java

## مقدمة

في هذا الدرس الشامل ستكتشف **كيفية تغيير اتجاه البثق** عند إجراء بثق خطي باستخدام Aspose.3D للغة Java. سواءً كنت تبني أداة شبيهة بـ CAD، أو تُعد أصولًا لمحرك ألعاب، أو تُنشئ أجزاءً للطباعة ثلاثية الأبعاد، فإن التحكم في اتجاه البثق يتيح لك إنشاء الشكل الدقيق الذي تحتاجه. سنستعرض كل خطوة، من تهيئة الملف إلى حفظ النتيجة كملف OBJ، بحيث يمكنك أيضًا **تصدير ملفات نموذج ثلاثي الأبعاد OBJ** مباشرةً من Java.

## إجابات سريعة
- **ما هو الصنف الذي يقوم بالبثق الخطي؟** `LinearExtrusion`
- **ما هي الطريقة التي تحدد متجه البثق؟** `setDirection(Vector3 direction)`
- **هل يمكن حفظ النتيجة كملف OBJ؟** نعم—استخدم `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **هل يلزم وجود ترخيص للاستخدام في الإنتاج؟** تتوفر نسخة تجريبية مجانية؛ الترخيص إلزامي للاستخدام التجاري.
- **أي بيئة تطوير متكاملة (IDE) تعمل بشكل أفضل مع Aspose.3D؟** IntelliJ IDEA و Eclipse مدعومان بالكامل.

## ما هو البثق الخطي؟

البثق الخطي هو عملية توسيع رسم ثنائي الأبعاد (مثل مستطيل أو دائرة) على طول خط مستقيم لتوليد جسم ثلاثي الأبعاد. بشكل افتراضي يتبع البثق المحور Z الموجب، لكن Aspose.3D يتيح لك تغيير هذا المسار باستخدام خاصية `setDirection`، مما يمنحك سيطرة كاملة على الهندسة النهائية.

## لماذا تغيير اتجاه البثق في البثق الخطي؟

تغيير اتجاه البثق يتيح لك محاذاة الهندسة الجديدة مع الكائنات الموجودة، وإنشاء مكونات مائلة دون تحويلات إضافية، وتوليد نماذج تتطابق مع نظام الإحداثيات المطلوب في خطوط الأنابيب اللاحقة (مثل الطابعات ثلاثية الأبعاد أو محركات الألعاب). هذا يلغي الحاجة إلى خطوات ما بعد المعالجة ويقلل من حجم الملف بنسبة تصل إلى 15 % عند استخدام متجهات اتجاهية تتجنب الدورانات غير الضرورية.

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من وجود:

- معرفة أساسية بـ Java.
- مكتبة Aspose.3D مثبتة. يمكنك تنزيلها من [هنا](https://releases.aspose.com/3d/java/). يمكنك أيضًا تصفح جميع إصدارات Aspose من الصفحة الرئيسية [هنا](https://releases.aspose.com/).
- بيئة تطوير متكاملة مثل Eclipse أو IntelliJ IDEA.

## استيراد الحزم

مساحة الأسماء `com.aspose.threed` توفر الفئات الأساسية ثلاثية الأبعاد وأنواع الأدوات المساعدة.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## الخطوة 1: تهيئة الملف الأساسي

الفئة `RectangleShape` تنشئ الملف الثنائي الأبعاد الذي سيُبثق. يعطي نصف قطر التقويس الصغير الحواف مظهرًا ناعمًا.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## الخطوة 2: إنشاء مشهد

الفئة `Scene` هي الحاوية العليا في Aspose.3D التي تحتفظ بجميع العقد ثلاثية الأبعاد، والإضاءات، والكاميرات، والمواد.

```java
Scene scene = new Scene();
```

## الخطوة 3: إنشاء العقد

العنصر `Node` يمثل كائنًا في رسم المشهد، مما يتيح لك إرفاق الهندسة، والتحويلات، وخصائص أخرى.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## الخطوة 4: تنفيذ البثق الخطي على العقدة اليسرى

`LinearExtrusion` ينفذ عملية البثق، محولًا ملفًا ثنائي الأبعاد إلى شبكة ثلاثية الأبعاد.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## الخطوة 5: تنفيذ البثق الخطي على العقدة اليمنى مع الاتجاه

هنا **نغير اتجاه البثق**. بتمرير `Vector3` مخصص إلى `setDirection`، يتبع البثق المتجه (0.3, 0.2, 1)، منتجًا شكلًا مائلًا يتماشى مع نظام إحداثيات المشهد.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## الخطوة 6: حفظ المشهد ثلاثي الأبعاد

طريقة `save` تكتب المشهد إلى ملف بالتنسيق المحدد.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## المشكلات الشائعة والحلول

| المشكلة | لماذا يحدث | الحل |
|---------|------------|------|
| ملف OBJ يظهر فارغًا | لم يتم إضافة الملف إلى عقدة | تأكد من استدعاء `createChildNode` على عقدة صالحة |
| يبدو أن الاتجاه لم يتغير | تم استدعاء `setDirection` بعد إنشاء البثق | ضع تعيين الاتجاه داخل مُهيئ `LinearExtrusion` كما هو موضح |
| شبكة منخفضة الدقة | قيمة `setSlices` منخفضة جدًا | زد عدد الشرائح (مثلاً 100 أو أكثر) |

## الخلاصة

أنت الآن تعرف **كيفية تغيير اتجاه البثق** في البثق الخطي، وكيفية تعديل إعدادات الالتواء والشرائح، وكيفية **تصدير ملفات نموذج ثلاثي الأبعاد OBJ** باستخدام Aspose.3D للغة Java. تمنحك هذه التقنيات سيطرة دقيقة على إنشاء الهندسة وتسهّل دمج الأصول ثلاثية الأبعاد في خطوط الأنابيب الأكبر.

## الأسئلة المتكررة

**س:** هل يمكنني استخدام Aspose.3D مع لغات برمجة أخرى؟  
**ج:** نعم—توفر Aspose.3D واجهات برمجة تطبيقات لـ .NET و Java، مما يسمح بالتطوير عبر المنصات.

**س:** هل تتوفر نسخة تجريبية مجانية لـ Aspose.3D؟  
**ج:** بالتأكيد. يمكنك استكشاف مجموعة الميزات الكاملة من خلال نسخة تجريبية مجانية [هنا](https://releases.aspose.com/).

**س:** أين يمكنني العثور على وثائق مفصلة لـ Aspose.3D للغة Java؟  
**ج:** المرجع الشامل متاح [هنا](https://reference.aspose.com/3d/java/).

**س:** كيف أحصل على دعم لـ Aspose.3D؟  
**ج:** زر المنتدى الرسمي لـ [Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة من المجتمع وفريق المنتج.

**س:** هل تتوفر تراخيص مؤقتة للاختبار؟  
**ج:** نعم—يمكن الحصول على تراخيص مؤقتة [هنا](https://purchase.aspose.com/temporary-license/).

**آخر تحديث:** 2026-08-02  
**تم الاختبار مع:** Aspose.3D للغة Java (أحدث إصدار)  
**المؤلف:** Aspose

{{< blocks/products/products-backtop-button >}}

## دروس ذات صلة

- [كيفية بثق الشكل - إنشاء نماذج ثلاثية الأبعاد باستخدام البثق الخطي في Java](/3d/java/linear-extrusion/)
- [إنشاء بثق ثلاثي الأبعاد Java باستخدام Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [دورة رسومات Java 3D – المركز في البثق الخطي](/3d/java/linear-extrusion/controlling-center/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}