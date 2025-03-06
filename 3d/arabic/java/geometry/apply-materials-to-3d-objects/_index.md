---
title: قم بتطبيق المواد على الكائنات ثلاثية الأبعاد في Java باستخدام Aspose.3D
linktitle: قم بتطبيق المواد على الكائنات ثلاثية الأبعاد في Java باستخدام Aspose.3D
second_title: Aspose.3D جافا API
description: استكشف عالم الرسومات ثلاثية الأبعاد باستخدام Aspose.3D لـ Java. تعرف على كيفية تطبيق المواد على الكائنات ثلاثية الأبعاد بسلاسة. ارفع مستوى مشاريعك بصور واقعية.
weight: 14
url: /ar/java/geometry/apply-materials-to-3d-objects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# قم بتطبيق المواد على الكائنات ثلاثية الأبعاد في Java باستخدام Aspose.3D

## مقدمة

في العالم الديناميكي للرسومات ثلاثية الأبعاد، يبرز Aspose.3D for Java كأداة قوية لإضفاء الحيوية على مشاريعك. تعمل إضافة المواد إلى الكائنات ثلاثية الأبعاد على تحسين المظهر البصري، مما يجعلها أكثر واقعية. في هذا البرنامج التعليمي، سنرشدك خلال عملية تطبيق المواد على مكعب ثلاثي الأبعاد باستخدام Aspose.3D لـ Java.

## المتطلبات الأساسية

قبل الغوص في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

- تم تثبيت Java Development Kit (JDK) على نظامك.
- تم تنزيل مكتبة Aspose.3D لـ Java وإضافتها إلى مشروعك.
- الإلمام بمفاهيم برمجة Java الأساسية.

## حزم الاستيراد

للبدء، قم باستيراد الحزم الضرورية إلى مشروع Java الخاص بك. أضف الأسطر التالية في بداية الكود الخاص بك:

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## الخطوة 1: تهيئة كائن المشهد

```java
// تهيئة كائن المشهد
Scene scene = new Scene();
```

## الخطوة 2: تهيئة كائن عقدة المكعب

```java
// تهيئة كائن عقدة المكعب
Node cubeNode = new Node("cube");
```

## الخطوة 3: إنشاء شبكة باستخدام Polygon Builder

```java
// استدعاء الفئة المشتركة لإنشاء شبكة باستخدام طريقة إنشاء المضلع لتعيين مثيل الشبكة
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## الخطوة 4: أشر العقدة إلى الشبكة

```java
// نقطة العقدة إلى الشبكة
cubeNode.setEntity(mesh);
```

## الخطوة 5: إضافة المكعب إلى المشهد

```java
// إضافة مكعب إلى مكان الحادث
scene.getRootNode().addChildNode(cubeNode);
```

## الخطوة 6: تهيئة كائن PhongMaterial

```java
// تهيئة كائن PhongMaterial
PhongMaterial mat = new PhongMaterial();
```

## الخطوة 7: تهيئة كائن الملمس

```java
// تهيئة كائن الملمس
Texture diffuse = new Texture();
```

## الخطوة 8: تعيين مسار الملف المحلي للنسيج

```java
// المسار إلى دليل المستندات.
String MyDir = "Your Document Directory";
```

## الخطوة 9: تعيين مسار الملف المحلي للنسيج المضمن

```java
// قم بتعيين مسار الملف المحلي للنسيج المضمن
diffuse.setFileName(MyDir + "surface.dds");
```

## الخطوة 10: تعيين نسيج المادة

```java
// ضبط نسيج المادة
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## الخطوة 11: تضمين بيانات المحتوى الخام في FBX (اختياري)

```java
// قم بتعيين اسم الملف للنسيج المضمن
diffuse.setFileName("embedded-texture.png");
// تعيين المحتوى الثنائي
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## الخطوة 12: تعيين اللون براق

```java
// تعيين لون براق
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## الخطوة 13: ضبط السطوع

```java
// ضبط السطوع
mat.setShininess(100);
```

## الخطوة 14: تعيين الخاصية المادية لكائن المكعب

```java
// قم بتعيين خاصية المادة لكائن المكعب
cubeNode.setMaterial(mat);
```

## الخطوة 15: حفظ المشهد ثلاثي الأبعاد

```java
// قم بتعيين اسم الملف
MyDir = MyDir + "MaterialToCube.fbx";
// حفظ المشهد ثلاثي الأبعاد بتنسيقات الملفات المدعومة
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## خاتمة

تهانينا! لقد نجحت في تطبيق المواد على مكعب ثلاثي الأبعاد باستخدام Aspose.3D لـ Java. يمكن لهذه التقنية البسيطة والقوية أن ترفع مشروعاتك ثلاثية الأبعاد إلى آفاق جديدة، مما يوفر تجربة واقعية ومذهلة بصريًا.

## الأسئلة الشائعة

### س1: هل يمكنني تطبيق مواد متعددة على كائن ثلاثي الأبعاد واحد؟

ج1: نعم، يسمح لك Aspose.3D بتطبيق مواد متعددة على أجزاء مختلفة من كائن ثلاثي الأبعاد لتحسين التخصيص.

### س2: ما هي تنسيقات الملفات التي يدعمها Aspose.3D لحفظ المشاهد؟

 ج2: يدعم Aspose.3D تنسيقات الملفات المختلفة، بما في ذلك FBX وSTL و3DS. الرجوع إلى[توثيق](https://reference.aspose.com/3d/java/) للحصول على القائمة الكاملة.

### س3: هل يتوفر ترخيص مؤقت لـ Aspose.3D لـ Java؟

 ج3: نعم يمكنك الحصول على[ترخيص مؤقت](https://purchase.aspose.com/temporary-license/) لأغراض التقييم.

### س4: أين يمكنني العثور على الدعم لـ Aspose.3D؟

 ج4: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع والمناقشات.

### س5: هل يمكنني تنزيل مكتبة Aspose.3D من رابط محدد؟

 ج5: نعم، استخدم[رابط التحميل](https://releases.aspose.com/3d/java/) للوصول إلى أحدث إصدار من Aspose.3D لـ Java.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
