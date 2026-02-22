---
date: 2026-02-22
description: تعلم كيفية تعيين الاتجاه في البثق الخطي وتصدير نموذج 3D بصيغة OBJ باستخدام
  Aspose.3D للغة Java. اتبع دليلنا خطوة بخطوة.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: كيفية تعيين الاتجاه في البثق الخطي باستخدام Aspose.3D للـ Java
url: /ar/java/linear-extrusion/setting-direction/
weight: 12
---

.

But ensure not to translate dates or product names.

Now produce final content.

Make sure to keep code block placeholders unchanged.

Let's craft final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تعيين الاتجاه في البثق الخطي باستخدام Aspose.3D للـ Java

## المقدمة

في هذا الدرس الشامل ستكتشف **كيفية تعيين الاتجاه** عند تنفيذ بثق خطي باستخدام Aspose.3D للـ Java. سواءً كنت تبني أداة شبيهة بـ CAD أو تولد هندسة لمحرك ألعاب، فإن التحكم في اتجاه البثق يتيح لك إنشاء الشكل الدقيق الذي تحتاجه. سنستعرض كل خطوة، من تهيئة الملف التعريفي إلى حفظ النتيجة كملف OBJ، بحيث يمكنك أيضًا **تصدير ملفات نموذج 3d obj** مباشرةً من Java.

## إجابات سريعة
- **ما هو الصنف الأساسي للبثق الخطي؟** `LinearExtrusion`
- **ما هي الطريقة التي تحدد اتجاه البثق؟** `setDirection(Vector3 direction)`
- **هل يمكنني تصدير النتيجة كملف OBJ؟** نعم، باستخدام `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **هل أحتاج إلى ترخيص للتطوير؟** نسخة تجريبية مجانية متاحة؛ الترخيص مطلوب للإنتاج.
- **ما هو بيئة التطوير المتكاملة (IDE) الأفضل للـ Java؟** IntelliJ IDEA أو Eclipse مدعومان بالكامل.

## ما هو البثق الخطي؟

البثق الخطي يأخذ ملفًا تعريفًا ثنائي الأبعاد (مثل مستطيل أو دائرة) ويمده على طول خط مستقيم لإنشاء صلب ثلاثي الأبعاد. بشكل افتراضي يتبع البثق المحور Z الموجب، لكن Aspose.3D يتيح لك تغيير هذا المسار باستخدام خاصية `setDirection`.

## لماذا تعيين الاتجاه في البثق الخطي؟

تعيين اتجاه مخصص يكون مفيدًا عندما:
- محاذاة الهندسة مع كائنات موجودة في المشهد.
- إنشاء أجزاء مائلة أو مائلة دون خطوات تحويل إضافية.
- تصدير نماذج يجب أن تتطابق مع نظام إحداثيات محدد (مثل الطباعة ثلاثية الأبعاد أو محركات الألعاب).

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من أن لديك:

- معرفة أساسية بـ Java.
- مكتبة Aspose.3D مثبتة. يمكنك تنزيلها من [هنا](https://releases.aspose.com/3d/java/).
- بيئة تطوير مثل Eclipse أو IntelliJ IDEA.

## استيراد الحزم

أولاً، استورد المساحات التي توفر الأصناف الأساسية ثلاثية الأبعاد وأنواع الأدوات المساعدة.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## الخطوة 1: تهيئة الملف الأساسي

أنشئ الشكل الذي سيتم بثقه. في هذا المثال نستخدم `RectangleShape` مع نصف قطر تقويس صغير لإعطاء الحواف مظهرًا ناعمًا.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## الخطوة 2: إنشاء مشهد

كائن `Scene` يعمل كحاوية لجميع العقد ثلاثية الأبعاد، الأضواء، الكاميرات، والمواد.

```java
Scene scene = new Scene();
```

## الخطوة 3: إنشاء العقد

أضف عقدتين فرعيتين إلى جذر المشهد—واحدة للبثق الأيسر والأخرى للبثق الأيمن. تُترجم العقدة اليمنى بحيث لا يتداخل الكائنان.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## الخطوة 4: تنفيذ البثق الخطي على العقدة اليسرى

بثق الملف التعريفي على العقدة اليسرى باستخدام اتجاه محور Z الافتراضي. نضيف أيضًا دورانًا كاملاً 360° ونزيد عدد الشرائح للحصول على شبكة أكثر سلاسة.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## الخطوة 5: تنفيذ البثق الخطي على العقدة اليمنى مع الاتجاه

هنا ن **نعين الاتجاه**. بتمرير `Vector3` مخصص إلى `setDirection`، يتبع البثق المتجه (0.3, 0.2, 1)، مما ينتج شكلًا مائلًا.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## الخطوة 6: حفظ المشهد ثلاثي الأبعاد

أخيرًا، صدّر المشهد إلى صيغة Wavefront OBJ. تُظهر هذه الخطوة كيفية **حفظ ملف obj java** وتسهّل عرض النتيجة في أي عارض ثلاثي الأبعاد.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## المشكلات الشائعة والحلول

| المشكلة | سبب حدوثها | الحل |
|---------|------------|------|
| ملف OBJ يظهر فارغًا | لم يتم إضافة الملف التعريفي إلى عقدة | تأكد من استدعاء `createChildNode` على عقدة صالحة |
| الاتجاه يبدو غير متغير | `setDirection` تم استدعاؤه بعد إنشاء البثق بالفعل | قم بتعيين الاتجاه داخل مُهيئ `LinearExtrusion` كما هو موضح |
| شبكة منخفضة الدقة | قيمة `setSlices` منخفضة جدًا | زيادة عدد الشرائح (مثلاً 100 أو أكثر) |

## الخلاصة

أنت الآن تعرف **كيفية تعيين الاتجاه** في البثق الخطي، وكيفية تعديل إعدادات الالتواء والشرائح، وكيفية **تصدير ملفات نموذج 3d obj** باستخدام Aspose.3D للـ Java. تمنحك هذه التقنيات تحكمًا دقيقًا في إنشاء الهندسة وتسهّل دمج الأصول ثلاثية الأبعاد في خطوط أنابيب أكبر.

## الأسئلة المتكررة

### س1: هل يمكنني استخدام Aspose.3D مع لغات برمجة أخرى؟

A1: Aspose.3D يدعم لغات برمجة متعددة، بما في ذلك .NET و Java.

### س2: هل هناك نسخة تجريبية مجانية متاحة لـ Aspose.3D؟

A2: نعم، يمكنك استكشاف ميزات Aspose.3D عبر نسخة تجريبية مجانية [هنا](https://releases.aspose.com/).

### س3: أين يمكنني العثور على الوثائق التفصيلية لـ Aspose.3D للـ Java؟

A3: الوثائق الشاملة متاحة [هنا](https://reference.aspose.com/3d/java/).

### س4: كيف يمكنني الحصول على الدعم لـ Aspose.3D؟

A4: قم بزيارة [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لأي مساعدة أو استفسارات.

### س5: هل تتوفر تراخيص مؤقتة لـ Aspose.3D؟

A5: نعم، يمكنك الحصول على ترخيص مؤقت [هنا](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**آخر تحديث:** 2026-02-22  
**تم الاختبار مع:** Aspose.3D للـ Java (أحدث إصدار)  
**المؤلف:** Aspose