---
title: تحويل العقد ثلاثية الأبعاد مع Quaternions في Java باستخدام Aspose.3D
linktitle: تحويل العقد ثلاثية الأبعاد مع Quaternions في Java باستخدام Aspose.3D
second_title: Aspose.3D جافا API
description: قم بتحسين تطبيقات Java الخاصة بك باستخدام Aspose.3D لإجراء تحويلات ثلاثية الأبعاد قوية. تعلم كيفية تحويل العقد باستخدام الكواترنيونات في هذا الدليل التفصيلي خطوة بخطوة.
type: docs
weight: 20
url: /ar/java/geometry/transform-3d-nodes-with-quaternions/
---
## مقدمة

مرحبًا بك في هذا الدليل التفصيلي خطوة بخطوة حول تحويل العقد ثلاثية الأبعاد ذات الكواترنيونات في Java باستخدام Aspose.3D. إذا كنت تتطلع إلى تحسين تطبيق Java لديك من خلال تحويلات ثلاثية الأبعاد قوية، فهذا البرنامج التعليمي مناسب لك. يوفر Aspose.3D for Java مجموعة قوية من الميزات للعمل مع الرسومات ثلاثية الأبعاد، وفي هذا البرنامج التعليمي، سنركز على تحويل العقد ثلاثية الأبعاد باستخدام الكواترنيونات.

## المتطلبات الأساسية

قبل أن نتعمق في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

- المعرفة الأساسية ببرمجة جافا.
- تم تثبيت Aspose.3D لـ Java. يمكنك تنزيله[هنا](https://releases.aspose.com/3d/java/).
- تم إعداد دليل المستندات لحفظ المشاهد ثلاثية الأبعاد.

## حزم الاستيراد

في هذا القسم، سنقوم باستيراد الحزم اللازمة للبدء في التحويلات ثلاثية الأبعاد باستخدام Aspose.3D.

```java
import com.aspose.threed.*;
```

## الخطوة 1: تهيئة كائن المشهد

للبدء، قم بإنشاء كائن مشهد سيكون بمثابة حاوية للعناصر ثلاثية الأبعاد الخاصة بك.

```java
Scene scene = new Scene();
```

## الخطوة 2: تهيئة كائن فئة العقدة

الآن، قم بإنشاء كائن فئة العقدة، في هذه الحالة، يمثل مكعبًا.

```java
Node cubeNode = new Node("cube");
```

## الخطوة 3: إنشاء شبكة باستخدام Polygon Builder

استخدم الفئة المشتركة لإنشاء شبكة باستخدام طريقة إنشاء المضلعات.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## الخطوة 4: تعيين هندسة الشبكة

قم بتعيين الشبكة التي تم إنشاؤها إلى عقدة المكعب.

```java
cubeNode.setEntity(mesh);
```

## الخطوة 5: ضبط التدوير مع Quaternion

قم بتطبيق التدوير على عقدة المكعب باستخدام الكواترنيونات.

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## الخطوة 6: تعيين الترجمة

حدد الترجمة لعقدة المكعب.

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## الخطوة 7: إضافة المكعب إلى المشهد

قم بتضمين عقدة المكعب في المشهد.

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## الخطوة 8: حفظ المشهد ثلاثي الأبعاد

احفظ المشهد ثلاثي الأبعاد بتنسيق ملف مدعوم، على سبيل المثال، FBX7500ASCII.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## خاتمة

تهانينا! لقد تعلمت بنجاح كيفية تحويل العقد ثلاثية الأبعاد باستخدام الكواترنيونات في Java باستخدام Aspose.3D. قم بتجربة التحولات المختلفة لإضفاء الحيوية على تطبيقاتك ثلاثية الأبعاد.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ Java مجانًا؟

ج1: يقدم Aspose.3D for Java نسخة تجريبية مجانية. يمكن ان تجدها[هنا](https://releases.aspose.com/).

### س2: أين يمكنني العثور على الوثائق الخاصة بـ Aspose.3D لـ Java؟

 ج2: الوثائق متاحة[هنا](https://reference.aspose.com/3d/java/).

### س3: كيف يمكنني الحصول على دعم Aspose.3D لـ Java؟

 ج3: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للدعم.

### س4: هل التراخيص المؤقتة متاحة؟

 ج4: نعم، يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).

### س5: أين يمكنني شراء Aspose.3D لـ Java؟

 ج5: يمكنك شرائه[هنا](https://purchase.aspose.com/buy).