---
title: تحويل العقد ثلاثية الأبعاد بزوايا أويلر في Java باستخدام Aspose.3D
linktitle: تحويل العقد ثلاثية الأبعاد بزوايا أويلر في Java باستخدام Aspose.3D
second_title: Aspose.3D جافا API
description: استكشف عالم التحولات ثلاثية الأبعاد في Java باستخدام Aspose.3D. اتبع دليلنا خطوة بخطوة لإضافة زوايا أويلر الديناميكية إلى العقد ثلاثية الأبعاد.
weight: 19
url: /ar/java/geometry/transform-3d-nodes-with-euler-angles/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تحويل العقد ثلاثية الأبعاد بزوايا أويلر في Java باستخدام Aspose.3D

## مقدمة

مرحبًا بك في هذا البرنامج التعليمي خطوة بخطوة حول تحويل العقد ثلاثية الأبعاد بزوايا أويلر في Java باستخدام Aspose.3D. في هذا الدليل، سوف نتعمق في عملية إضافة التحويلات إلى عقدة ثلاثية الأبعاد، باستخدام زوايا أويلر لتحقيق التموضع والتوجيه الديناميكي.

## المتطلبات الأساسية

قبل أن نتعمق في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

- المعرفة الأساسية ببرمجة جافا.
- تم تثبيت Java Development Kit (JDK) على جهازك.
-  مكتبة Aspose.3D والتي يمكنك الحصول عليها من[Aspose.3D وثائق جافا](https://reference.aspose.com/3d/java/).

## حزم الاستيراد

 ابدأ باستيراد الحزم الضرورية إلى مشروع Java الخاص بك. تأكد من إضافة مكتبة Aspose.3D بشكل صحيح إلى مسار الفصل الدراسي الخاص بك. إذا لم تقم بتنزيله بعد، يمكنك العثور على رابط التنزيل[هنا](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## الخطوة 1. تهيئة المشهد والعقدة

```java
// ExStart:AddTransformationToNodeByEulerAngles
// تهيئة كائن المشهد
Scene scene = new Scene();

// تهيئة كائن فئة العقدة
Node cubeNode = new Node("cube");
```

## الخطوة 2. إنشاء شبكة وتعيين الهندسة

```java
// استدعاء الفئة المشتركة لإنشاء شبكة باستخدام طريقة إنشاء المضلع لتعيين مثيل الشبكة
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// نقطة العقدة إلى هندسة الشبكة
cubeNode.setEntity(mesh);
```

## الخطوة 3. ضبط زوايا أويلر والترجمة

```java
// زوايا أويلر
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// تعيين الترجمة
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## الخطوة 4. أضف عقدة إلى المشهد

```java
// إضافة مكعب إلى مكان الحادث
scene.getRootNode().getChildNodes().add(cubeNode);
```

## الخطوة 5. احفظ المشهد ثلاثي الأبعاد

```java
// المسار إلى دليل المستندات.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// حفظ المشهد ثلاثي الأبعاد بتنسيقات الملفات المدعومة
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

تأكد من استبدال "دليل المستندات الخاص بك" بالمسار المناسب على جهازك.

## خاتمة

تهانينا! لقد نجحت في تحويل العقد ثلاثية الأبعاد باستخدام زوايا Euler في Java باستخدام Aspose.3D. قم بتجربة زوايا وترجمات مختلفة لإنشاء مشاهد ثلاثية الأبعاد ديناميكية وجذابة.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ Java في المشاريع التجارية؟

 ج1: نعم يمكنك ذلك. قم بزيارة[صفحة الشراء](https://purchase.aspose.com/buy) للحصول على تفاصيل الترخيص.

### س2: أين يمكنني العثور على الدعم لـ Aspose.3D؟

 ج2: ال[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) هو المكان المناسب لطلب المساعدة والتواصل مع المجتمع.

### س3: هل هناك نسخة تجريبية مجانية متاحة؟

 ج3: نعم، يمكنك استكشاف[تجربة مجانية](https://releases.aspose.com/) لتجربة قدرات Aspose.3D.

### س4: كيف يمكنني الحصول على ترخيص مؤقت؟

 ج4: يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).

### س5: أين يمكنني العثور على الوثائق؟

 ج5: ال[توثيق](https://reference.aspose.com/3d/java/) يوفر إرشادات شاملة حول استخدام Aspose.3D لـ Java.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
