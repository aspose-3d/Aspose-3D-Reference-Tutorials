---
title: تحديد الاتجاه في النتوء الخطي باستخدام Aspose.3D لـ Java
linktitle: تحديد الاتجاه في النتوء الخطي باستخدام Aspose.3D لـ Java
second_title: Aspose.3D جافا API
description: إتقان البثق الخطي باستخدام Aspose.3D لـ Java! اتبع دليلنا لبرمجة ثلاثية الأبعاد سلسة. قم بالتنزيل الآن لتجربة آسرة.
type: docs
weight: 12
url: /ar/java/linear-extrusion/setting-direction/
---
## مقدمة

مرحبًا بك في دليلنا خطوة بخطوة حول تحديد الاتجاه في البثق الخطي باستخدام Aspose.3D لـ Java. Aspose.3D هي مكتبة Java قوية تتيح للمطورين العمل بسلاسة مع الملفات والمشاهد ثلاثية الأبعاد. في هذا البرنامج التعليمي، سنركز على المهمة المحددة المتمثلة في تحديد الاتجاه في البثق الخطي، مما يعزز كفاءتك في البرمجة ثلاثية الأبعاد.

## المتطلبات الأساسية

قبل أن نتعمق في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

- المعرفة الأساسية بلغة البرمجة جافا.
-  تم تثبيت مكتبة Aspose.3D. يمكنك تنزيله من[هنا](https://releases.aspose.com/3d/java/).
- بيئة تطوير متكاملة (IDE) لـ Java، مثل Eclipse أو IntelliJ.

## حزم الاستيراد

تأكد من استيراد الحزم اللازمة لبدء مشروعك:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## الخطوة 1: تهيئة ملف التعريف الأساسي

 ابدأ بتهيئة ملف التعريف الأساسي المراد قذفه. في هذا المثال نستخدم أ`RectangleShape` بنصف قطر تقريب 0.3:

```java
// المسار إلى دليل المستندات.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## الخطوة 2: إنشاء مشهد

بعد ذلك، قم بإنشاء مشهد ثلاثي الأبعاد لاحتواء الكائنات المبثوقة:

```java
Scene scene = new Scene();
```

## الخطوة 3: إنشاء العقد

قم بإنشاء العقد اليسرى واليمنى داخل المشهد:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## الخطوة 4: إجراء البثق الخطي على العقدة اليسرى

 إجراء قذف خطي على العقدة اليسرى باستخدام`LinearExtrusion`فئة ذات معلمات محددة مثل الالتواء والشرائح:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## الخطوة 5: إجراء البثق الخطي على العقدة اليمنى بالاتجاه

 إجراء قذف خطي على العقدة اليمنى، وإدخال`setDirection` خاصية تحديد اتجاه البثق:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## الخطوة 6: حفظ المشهد ثلاثي الأبعاد

احفظ المشهد ثلاثي الأبعاد بتنسيق الملف المطلوب. في هذا المثال، نقوم بحفظه كملف Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## خاتمة

تهانينا! لقد تعلمت بنجاح كيفية ضبط الاتجاه في البثق الخطي باستخدام Aspose.3D لـ Java. يعزز هذا البرنامج التعليمي مهاراتك في البرمجة ثلاثية الأبعاد ويفتح لك إمكانيات جديدة للمشاريع الإبداعية.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D مع لغات البرمجة الأخرى؟

ج1: يدعم Aspose.3D العديد من لغات البرمجة، بما في ذلك .NET وJava.

### س2. هل هناك نسخة تجريبية مجانية متاحة لـ Aspose.3D؟

 ج2: نعم، يمكنك استكشاف ميزات Aspose.3D من خلال النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).

### س3: أين يمكنني العثور على الوثائق التفصيلية لـ Aspose.3D لـ Java؟

 ج3: الوثائق الشاملة متاحة[هنا](https://reference.aspose.com/3d/java/).

### س4: كيف يمكنني الحصول على الدعم لـ Aspose.3D؟

 ج4: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لأية مساعدة أو استفسار.

### س5: هل التراخيص المؤقتة متاحة لـ Aspose.3D؟

 ج5: نعم، يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).