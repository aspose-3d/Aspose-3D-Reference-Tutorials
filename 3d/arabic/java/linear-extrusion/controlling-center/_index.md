---
title: مركز التحكم في النتوء الخطي باستخدام Aspose.3D لـ Java
linktitle: مركز التحكم في النتوء الخطي باستخدام Aspose.3D لـ Java
second_title: Aspose.3D جافا API
description: استكشف عالم الرسومات ثلاثية الأبعاد في Java باستخدام Aspose.3D. السيطرة على المركز في قذف خطي دون عناء.
weight: 11
url: /ar/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# مركز التحكم في النتوء الخطي باستخدام Aspose.3D لـ Java

## مقدمة

في عالم الرسومات ثلاثية الأبعاد وبرمجة Java، يلعب التحكم في المركز في البثق الخطي دورًا حاسمًا في تحقيق التأثيرات المطلوبة في مشاريعك. يوفر Aspose.3D for Java مجموعة أدوات قوية للتعامل مع مثل هذه المهام بسلاسة. في هذا البرنامج التعليمي، سنتعمق في عملية التحكم في المركز في البثق الخطي باستخدام Aspose.3D لـ Java، مع تفصيل كل خطوة لضمان فهم سلس وشامل.

## المتطلبات الأساسية

قبل أن نبدأ هذه الرحلة التعليمية، تأكد من توفر المتطلبات الأساسية التالية:

1. بيئة تطوير Java: تأكد من إعداد بيئة تطوير Java على جهازك.

2.  Aspose.3D لـ Java: قم بتنزيل وتثبيت مكتبة Aspose.3D. يمكنك العثور على المكتبة ووثائقها[هنا](https://reference.aspose.com/3d/java/).

3. دليل المستندات: قم بإنشاء دليل لتخزين مستندات Java الخاصة بك. دعنا نسميه "دليل المستندات الخاص بك".

## حزم الاستيراد

في بيئة تطوير Java الخاصة بك، قم باستيراد الحزم اللازمة لـ Aspose.3D. وهذا يضمن أن الكود الخاص بك لديه حق الوصول إلى الوظائف التي توفرها المكتبة.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## الخطوة 1: إعداد ملف التعريف الأساسي

قم بتهيئة ملف التعريف الأساسي المراد قذفه. في هذا المثال، سنستخدم شكلًا مستطيلًا بنصف قطر دائري قدره 0.3.

```java
// المسار إلى دليل المستندات.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## الخطوة 2: إنشاء مشهد ثلاثي الأبعاد

قم ببناء أساس عالمك ثلاثي الأبعاد من خلال إنشاء مشهد.

```java
Scene scene = new Scene();
```

## الخطوة 3: إنشاء العقد اليسرى واليمنى

أنشئ العقد اليسرى واليمنى داخل المشهد الخاص بك. تعمل هذه العقد بمثابة لوحة قماشية للكائنات ثلاثية الأبعاد الخاصة بك.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## الخطوة 4: البثق الخطي مع خاصية المركز

إجراء قذف خطي على العقدة اليسرى دون توسيط، وتعيين عدد الشرائح إلى 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## الخطوة 5: تعيين الطائرة الأرضية كمرجع

قم بتعزيز التمثيل المرئي عن طريق إضافة مستوى أرضي إلى العقدة اليسرى.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## الخطوة 6: النتوء الخطي مع خاصية المركز (العقدة اليمنى)

إجراء قذف خطي على العقدة اليمنى، وهذه المرة توسيط البثق، ومرة أخرى قم بتعيين عدد الشرائح إلى 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## الخطوة 7: تعيين المستوى الأرضي كمرجع (العقدة اليمنى)

على غرار العقدة اليسرى، أضف مستوى أرضيًا إلى العقدة اليمنى كمرجع.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## الخطوة 8: احفظ المشهد ثلاثي الأبعاد

احفظ مشهدك ثلاثي الأبعاد بتنسيق Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## خاتمة

إن التحكم في المركز في البثق الخطي باستخدام Aspose.3D لـ Java يفتح إمكانيات مثيرة في تطوير الرسومات ثلاثية الأبعاد. باتباع هذا الدليل التفصيلي، تعلمت كيفية التعامل مع خاصية المركز، مما يسمح لك بتحقيق التأثيرات المرئية المطلوبة في مشاريع Java الخاصة بك.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ Java في المشاريع التجارية؟

 A1: نعم، Aspose.3D for Java متاح للاستخدام التجاري. للحصول على تفاصيل الترخيص، قم بزيارة[هنا](https://purchase.aspose.com/buy).

### س2: هل هناك نسخة تجريبية مجانية متاحة؟

 ج2: نعم، يمكنك استكشاف النسخة التجريبية المجانية من Aspose.3D لـ Java[هنا](https://releases.aspose.com/).

### س3: أين يمكنني العثور على دعم لـ Aspose.3D لـ Java؟

 ج3: يعد منتدى مجتمع Aspose.3D مكانًا رائعًا للحصول على الدعم ومشاركة تجاربك. زيارة المنتدى[هنا](https://forum.aspose.com/c/3d/18).

### س4: هل أحتاج إلى ترخيص مؤقت للاختبار؟

ج4: نعم، إذا كنت بحاجة إلى ترخيص مؤقت لأغراض الاختبار، فيمكنك الحصول عليه[هنا](https://purchase.aspose.com/temporary-license/).

### س5: أين يمكنني العثور على الوثائق؟

 ج5: تتوفر وثائق Aspose.3D لـ Java[هنا](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
