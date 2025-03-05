---
title: استخدام الإزاحة الملتوية في البثق الخطي باستخدام Aspose.3D لـ Java
linktitle: استخدام الإزاحة الملتوية في البثق الخطي باستخدام Aspose.3D لـ Java
second_title: Aspose.3D جافا API
description: عزز مهاراتك في النمذجة ثلاثية الأبعاد باستخدام Aspose.3D لـ Java. تعلم كيفية استخدام Twist Offset في Linear Extrusion في هذا البرنامج التعليمي الشامل.

type: docs
weight: 15
url: /ar/java/linear-extrusion/using-twist-offset/
---
## مقدمة

في العالم الديناميكي للرسومات ثلاثية الأبعاد، يعد إتقان فن البثق الخطي بمثابة تغيير جذري لقواعد اللعبة. باستخدام Aspose.3D for Java، يمكنك رفع مهاراتك في النمذجة ثلاثية الأبعاد من خلال دمج ميزة Twist Offset في عملية البثق الخطي. سيرشدك هذا البرنامج التعليمي خلال خطوات استخدام Twist Offset في Linear Extrusion باستخدام Aspose.3D لـ Java، مما يوفر لك الأدوات اللازمة لإنشاء مشاهد ثلاثية الأبعاد مذهلة.

## المتطلبات الأساسية

قبل الغوص في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

- بيئة جافا: تأكد من إعداد بيئة تطوير جافا على نظامك.
-  Aspose.3D لـ Java: قم بتنزيل وتثبيت مكتبة Aspose.3D من[رابط التحميل](https://releases.aspose.com/3d/java/).
-  التوثيق: تعرف على[Aspose.3D لوثائق جافا](https://reference.aspose.com/3d/java/).

## حزم الاستيراد

في مشروع Java الخاص بك، قم باستيراد الحزم اللازمة لبدء استخدام Aspose.3D لـ Java. تأكد من تضمين المكتبات المطلوبة للتكامل السلس.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## الخطوة 1: إعداد البيئة

ابدأ بإعداد بيئة تطوير Java الخاصة بك والتأكد من تثبيت Aspose.3D for Java بشكل صحيح.

## الخطوة 2: تهيئة ملف التعريف الأساسي

قم بإنشاء ملف تعريف أساسي للبثق، في هذه الحالة، شكل مستطيل بنصف قطر تقريب يبلغ 0.3.

```java
// المسار إلى دليل المستندات.
String MyDir = "Your Document Directory";
// قم بتهيئة ملف التعريف الأساسي المراد قذفه
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## الخطوة 3: إنشاء مشهد ثلاثي الأبعاد

أنشئ مشهدًا ثلاثي الأبعاد لإيواء الأشياء المبثوقة.

```java
// إنشاء مشهد
Scene scene = new Scene();
```

## الخطوة 4: إنشاء العقد

قم بإنشاء العقد داخل المشهد لتمثيل كيانات مختلفة.

```java
// إنشاء العقدة اليسرى
Node left = scene.getRootNode().createChildNode();
// إنشاء العقدة الصحيحة
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## الخطوة 5: إجراء البثق الخطي

الاستفادة من النتوء الخطي على العقدتين اليسرى واليمنى بخصائص مختلفة.

```java
// إجراء قذف خطي على العقدة اليسرى باستخدام خاصية الالتواء والشرائح
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// إجراء قذف خطي على العقدة اليمنى باستخدام خاصية الالتواء والإزاحة والشرائح
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## الخطوة 6: احفظ المشهد ثلاثي الأبعاد

احفظ المشهد ثلاثي الأبعاد الذي تم إنشاؤه حديثًا بتنسيق الملف المحدد.

```java
// حفظ مشهد ثلاثي الأبعاد
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## خاتمة

تهانينا! لقد نجحت في تنفيذ Twist Offset في Linear Extrusion باستخدام Aspose.3D لـ Java. تفتح هذه الميزة القوية عالمًا من الإمكانيات لمساعيك في تصميم النماذج ثلاثية الأبعاد، مما يسمح لك بإنشاء مشاهد معقدة وآسرة.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ Java في المشاريع غير التجارية؟

 ج1: نعم، يمكن استخدام Aspose.3D for Java في المشاريع التجارية وغير التجارية. افحص ال[خيارات الترخيص](https://purchase.aspose.com/buy) لمزيد من التفاصيل.

### س2: أين يمكنني العثور على دعم لـ Aspose.3D لـ Java؟

 ج2: قم بزيارة[Aspose.3D لمنتدى جافا](https://forum.aspose.com/c/3d/18) للحصول على المساعدة والتواصل مع المجتمع.

### س3: هل تتوفر نسخة تجريبية مجانية من Aspose.3D لـ Java؟

 ج3: نعم، يمكنك استكشاف نسخة تجريبية مجانية من[صفحة الإصدارات](https://releases.aspose.com/).

### س4: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D لـ Java؟

 ج4: احصل على ترخيص مؤقت لمشروعك من خلال زيارة[هذا الرابط](https://purchase.aspose.com/temporary-license/).

### س5: هل هناك أمثلة ودروس إضافية متاحة؟

 ج5: نعم، راجع[توثيق](https://reference.aspose.com/3d/java/) لمزيد من الأمثلة والبرامج التعليمية المتعمقة.