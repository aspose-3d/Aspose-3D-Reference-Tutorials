---
title: تطبيق Twist في النتوء الخطي باستخدام Aspose.3D لـ Java
linktitle: تطبيق Twist في النتوء الخطي باستخدام Aspose.3D لـ Java
second_title: Aspose.3D جافا API
description: تعرف على كيفية إضافة لمسة إلى نماذجك ثلاثية الأبعاد باستخدام Aspose.3D لـ Java. اتبع دليلنا خطوة بخطوة للحصول على تأثيرات البثق الخطي المحسنة.
weight: 14
url: /ar/java/linear-extrusion/applying-twist/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تطبيق Twist في النتوء الخطي باستخدام Aspose.3D لـ Java

## مقدمة

مرحبًا بك في هذا البرنامج التعليمي خطوة بخطوة حول تطبيق الالتواء في البثق الخطي باستخدام Aspose.3D لـ Java. Aspose.3D هي مكتبة Java قوية تمكن المطورين من العمل مع تنسيقات الملفات ثلاثية الأبعاد، وتوفر وظائف قوية لإنشاء مشاهد ثلاثية الأبعاد ومعالجتها وعرضها. في هذا البرنامج التعليمي، سنستكشف كيفية تطبيق تأثير ملتوي أثناء عملية البثق الخطي لتحسين نماذجك ثلاثية الأبعاد.

## المتطلبات الأساسية

قبل الغوص في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

- بيئة تطوير Java: تأكد من تثبيت Java على نظامك.
-  مكتبة Aspose.3D: قم بتنزيل وتثبيت مكتبة Aspose.3D لـ Java من[رابط التحميل](https://releases.aspose.com/3d/java/).
-  التوثيق: راجع[وثائق Aspose.3D](https://reference.aspose.com/3d/java/) للحصول على إرشادات شاملة.

## حزم الاستيراد

قبل البدء في عملية البرمجة، قم باستيراد الحزم الضرورية إلى مشروع Java الخاص بك. فيما يلي مثال لكيفية القيام بذلك:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## الخطوة 1: قم بتعيين دليل المستندات

ابدأ بتعيين دليل المستند حيث سيتم حفظ المشهد ثلاثي الأبعاد الخاص بك.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## الخطوة 2: تهيئة ملف التعريف الأساسي

قم بتهيئة ملف التعريف الأساسي المراد قذفه. في هذا المثال، نستخدم شكلاً مستطيلاً بنصف قطر مستدير.

```java
// ExStart: تهيئة الملف الشخصي الأساسي
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd: تهيئة الملف الشخصي الأساسي
```

## الخطوة 3: إنشاء مشهد

قم بإنشاء مشهد ثلاثي الأبعاد لاستضافة العقد المبثوقة.

```java
// ExStart: إنشاء مشهد
Scene scene = new Scene();
// ExEnd:CreateScene
```

## الخطوة 4: إنشاء العقد

قم بإنشاء العقد اليمنى واليسرى داخل المشهد. ضبط ترجمة العقدة اليسرى.

```java
// ExStart:إنشاء العقد
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## الخطوة 5: تنفيذ البثق الخطي مع الالتواء

إجراء قذف خطي على كل من العقد اليسرى واليمنى، مع تطبيق خصائص الالتواء والشرائح.

```java
// ExStart: LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd: LinearExtrusionWithTwist
```

## الخطوة 6: حفظ المشهد ثلاثي الأبعاد

احفظ المشهد ثلاثي الأبعاد بتنسيق ملف Wavefront OBJ.

```java
// ExStart: Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:Save3DScene
```

## خاتمة

تهانينا! لقد نجحت في تطبيق الالتواء في البثق الخطي باستخدام Aspose.3D لـ Java. قدم هذا البرنامج التعليمي دليلاً تفصيليًا خطوة بخطوة لمساعدتك في تحسين قدراتك على تصميم النماذج ثلاثية الأبعاد.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ Java للعمل مع تنسيقات الملفات ثلاثية الأبعاد الأخرى؟

ج1: نعم، يدعم Aspose.3D العديد من تنسيقات الملفات ثلاثية الأبعاد، مما يسمح لك باستيراد أنواع ملفات متنوعة وتصديرها ومعالجتها.

### س2: أين يمكنني العثور على دعم لـ Aspose.3D لـ Java؟

 ج2: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع والمناقشات.

### س3: هل تتوفر نسخة تجريبية مجانية من Aspose.3D لـ Java؟

 ج3: نعم، يمكنك الوصول إلى الإصدار التجريبي المجاني من[هنا](https://releases.aspose.com/).

### س4: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D لـ Java؟

 ج4: احصل على ترخيص مؤقت من[صفحة الترخيص المؤقتة](https://purchase.aspose.com/temporary-license/).

### س5: أين يمكنني شراء Aspose.3D لـ Java؟

 A5: قم بشراء Aspose.3D لـ Java من[صفحة الشراء](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
