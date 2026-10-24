---
date: 2026-10-24
description: تعلم كيفية تصدير ملفات OBJ وتغيير اتجاه المستوى في Java باستخدام Aspose.3D.
  يوضح هذا الدليل خطوة بخطوة إنشاء مستوى مائل وتصدير نموذج 3D بصيغة OBJ.
keywords:
- how to export obj
- create sloped plane
- export 3d model obj
- adjust plane orientation
lastmod: 2026-10-24
linktitle: كيفية تصدير OBJ وتغيير اتجاه المستوى في Java
og_description: تعلم كيفية تصدير OBJ وتغيير اتجاه المستوى في Java مع Aspose.3D. اتبع
  هذا الدليل لإنشاء مستوى مائل وتصدير نموذج 3D بصيغة OBJ بكفاءة.
og_image_alt: 'Tutorial: export OBJ and adjust plane orientation in Java with Aspose.3D'
og_title: كيفية تصدير OBJ وتغيير اتجاه المستوى في Java
schemas:
- author: Aspose
  dateModified: '2026-10-24'
  description: Learn how to export OBJ files and change plane orientation in Java
    using Aspose.3D. This step‑by‑step guide shows creating a sloped plane and exporting
    a 3D model OBJ.
  headline: How to export OBJ and change plane orientation in Java
  type: TechArticle
- description: Learn how to export OBJ files and change plane orientation in Java
    using Aspose.3D. This step‑by‑step guide shows creating a sloped plane and exporting
    a 3D model OBJ.
  name: How to export OBJ and change plane orientation in Java
  steps:
  - name: set document directory path
    text: Define where the exported OBJ file will be saved. ` Replace `"Your Document
      Directory"` with the absolute path on your machine (e.g., `C:/3DOutputs/`).
  - name: initialize the scene – create 3D scene
    text: Create a fresh `Scene` object that will hold all geometry. `
  - name: initialize the plane – how to modify plane
    text: Instantiate a `Plane` object that we will later orient. `
  - name: set vector – how to set plane up
    text: Define a custom up‑vector for the plane. This is the core of **change plane
      orientation**. The vector `(1, 1, 3)` tilts the plane away from the default
      XY‑plane, giving you a sloped surface you can later **export OBJ**.
  - name: complete the plane orientation and export
    text: After this call, you’ll find `ChangePlaneOrientation.obj` in the directory
      you specified, ready for any **Aspose.3D export OBJ** workflow. Aspose.3D supports
      over 30 output formats—including OBJ, FBX, STL, and more—so you can switch formats
      with a single enum change.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D provides APIs for Java, .NET, and other platforms, each
      offering the same feature set.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Certainly! You can explore the features of Aspose.3D by accessing the
      free trial [here](https://releases.aspose.com/).
    question: Is a free trial available for Aspose.3D?
  - answer: For any queries or assistance, visit our [support forum](https://forum.aspose.com/c/3d/18).
    question: Where can I find support for Aspose.3D?
  - answer: To purchase Aspose.3D, visit our [buy page](https://purchase.aspose.com/buy).
    question: How can I purchase Aspose.3D?
  - answer: Yes, if you need a temporary license, you can obtain one [here](https://purchase.aspose.com/temporary-license/).
    question: Is there a temporary license option?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export obj
- Aspose.3D
- Java 3D
- plane orientation
- 3D modeling
title: كيفية تصدير OBJ وتغيير اتجاه المستوى في Java
url: /ar/java/3d-scenes-and-models/change-plane-orientation/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تصدير OBJ وتغيير اتجاه المستوى في Java

## مقدمة

في هذا الدرس ستتعلم **كيفية تصدير OBJ** وتغيير اتجاه المستوى في Java باستخدام Aspose.3D API. تعديل متجه الارتفاع (up‑vector) للمستوى يمنحك تحكمًا دقيقًا في وضع الكائنات داخل سير عمل **إنشاء مشهد ثلاثي الأبعاد** — وهو مثالي للألعاب والمحاكاة والمرئيات المعمارية حيث تكون الدقة في التحديد مهمة. تتوفر Aspose.3D Java API من صفحة التحميل الرئيسية لـ Aspose [هنا](https://releases.aspose.com/).

## إجابات سريعة
- **ماذا يعني “export OBJ”؟** يعني تحويل مشهد ثلاثي الأبعاد إلى تنسيق Wavefront OBJ، وهو نوع ملف شبكة مدعوم عالميًا.  
- **لماذا تعديل اتجاه المستوى؟** تغيير متجه الارتفاع للمستوى يتيح لك محاذاة الهندسة بالضبط حيث تحتاجها في المشهد.  
- **هل أحتاج إلى ترخيص لتشغيل الكود؟** النسخة التجريبية المجانية تكفي للتطوير؛ يلزم ترخيص تجاري للإنتاج.  
- **ما نسخة Java المدعومة؟** Aspose.3D يعمل مع Java 8 وما فوق.  
- **هل يمكنني تصدير صيغ أخرى؟** نعم — API يدعم أيضًا FBX و STL وغيرها.

## ما هو “change plane orientation”؟

تغيير اتجاه المستوى يعني تعديل متجه الارتفاع للمستوى بحيث يميل المستوى بعيدًا عن المستوى XY الافتراضي، مما يتيح لك إنشاء أسطح مائلة مثل المنحدرات أو الأسقف أو مستويات مرجعية مخصصة. هذه العملية تؤثر مباشرةً على كيفية وضع الهندسة قبل **تصدير OBJ**.

## لماذا تعديل اتجاه المستوى؟

تعديل اتجاه المستوى يتيح لك محاذاة الكائنات مع محاور مخصصة، محاكاة الأسطح المائلة، وضمان أن شبكة OBJ المصدرة تعكس النية البصرية لتصميمك. استخدام متجه ارتفاع مخصص يحسن دقة التحديد ويقلل بشكل كبير من وقت التحرير بعد التصدير للمطورين.

## المتطلبات المسبقة

- فهم أساسي لبرمجة Java.  
- تثبيت Aspose.3D for Java — قم بتنزيله [هنا](https://releases.aspose.com/3d/java/).  
- بيئة تطوير Java IDE أو أداة بناء (مثل IntelliJ IDEA أو Maven أو Gradle) جاهزة للبرمجة.

## استيراد الحزم

تمنحك الاستيرادات التالية الوصول إلى الفئات الأساسية في Aspose.3D.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Plane;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;

import java.io.IOException;
```

تمثل الفئة `Plane` مستوىً هندسيًا يمكن وضعه وتوجيهه في الفضاء ثلاثي الأبعاد.  
تعرّف الفئة `Vector3` متجهًا ثلاثي الأبعاد يُستخدم للاتجاهات والمواقع.  
الفئة `Scene` هي حاوية تحتفظ بجميع الكائنات ثلاثية الأبعاد، والإضاءة، والكاميرات في النموذج.  
تحدد التعداد `FileFormat` تنسيق الملف الناتج لحفظ المشهد.

## دليل خطوة بخطوة

### الخطوة 1: تعيين مسار دليل المستند  
حدد المكان الذي سيتم حفظ ملف OBJ المصدّر فيه.

````java
String MyDir = "Your Document Directory";
````

استبدل `"Your Document Directory"` بالمسار المطلق على جهازك (مثال: `C:/3DOutputs/`).

### الخطوة 2: تهيئة المشهد – إنشاء مشهد ثلاثي الأبعاد  
أنشئ كائن `Scene` جديد سيحتوي على جميع الهندسة.

````java
Scene scene = new Scene();
````

### الخطوة 3: تهيئة المستوى – كيفية تعديل المستوى  
أنشئ كائن `Plane` سنقوم بتوجيهه لاحقًا.

````java
Plane plane = new Plane();
````

### الخطوة 4: تعيين المتجه – كيفية تعيين اتجاه المستوى  
حدد متجه ارتفاع مخصص للمستوى. هذا هو جوهر **change plane orientation**.  
المتجه `(1, 1, 3)` يميل المستوى بعيدًا عن المستوى XY الافتراضي، مما يمنحك سطحًا مائلًا يمكنك لاحقًا **تصدير OBJ**.

### الخطوة 5: إكمال توجيه المستوى وتصديره  

```java
// ExStart:ChangePlaneOrientation
try {
    plane.setUp(new Vector3(1, 1, 3));
    
    scene.getRootNode().createChildNode(plane);
    
    scene.save(MyDir + "ChangePlaneOrientation.obj", FileFormat.WAVEFRONTOBJ);
} catch (IOException e) {
    e.printStackTrace();
}
// ExEnd:ChangePlaneOrientation
```

بعد هذا الاستدعاء، ستجد `ChangePlaneOrientation.obj` في الدليل الذي حددته، جاهزًا لأي سير عمل **Aspose.3D export OBJ**. يدعم Aspose.3D أكثر من 30 تنسيق إخراج — بما في ذلك OBJ و FBX و STL وغيرها — لذا يمكنك تغيير الصيغ بتغيير واحد في التعداد.

## المشكلات الشائعة والحلول

| المشكلة | سبب حدوثها | الحل |
|-------|----------------|-----|
| **خطأ ملف غير موجود** عند الحفظ | `MyDir` غير موجود أو يفتقر إلى صلاحية الكتابة | أنشئ المجلد مسبقًا أو استخدم مسارًا مطلقًا مع الصلاحيات المناسبة. |
| المستوى يظهر مسطحًا في العارض | المتجه متوازي مع متجه الارتفاع الافتراضي | اختر متجهًا غير موازٍ (مثال: `(1, 0, 1)`) لرؤية ميل واضح. |
| ملف OBJ يُحمَّل بدون القوام | لم يتم إضافة القوام إلى المشهد | أرفق مادة/قوام إلى الهندسة قبل التصدير إذا لزم الأمر. |

## الأسئلة المتكررة

**س: هل يمكنني استخدام Aspose.3D for Java مع لغات برمجة أخرى؟**  
ج: نعم، Aspose.3D يوفر واجهات برمجة التطبيقات للـ Java و .NET وغيرها من المنصات، كل منها يقدم نفس مجموعة الميزات.

**س: هل تتوفر نسخة تجريبية مجانية لـ Aspose.3D؟**  
ج: بالتأكيد! يمكنك استكشاف ميزات Aspose.3D عبر الوصول إلى النسخة التجريبية المجانية [هنا](https://releases.aspose.com/).

**س: أين يمكنني العثور على الدعم لـ Aspose.3D؟**  
ج: لأي استفسارات أو مساعدة، زر [منتدى الدعم](https://forum.aspose.com/c/3d/18).

**س: كيف يمكنني شراء Aspose.3D؟**  
ج: لشراء Aspose.3D، زر [صفحة الشراء](https://purchase.aspose.com/buy).

**س: هل هناك خيار ترخيص مؤقت؟**  
ج: نعم، إذا كنت تحتاج إلى ترخيص مؤقت، يمكنك الحصول عليه [هنا](https://purchase.aspose.com/temporary-license/).

**س: هل يمكنني تصدير المشهد إلى صيغ أخرى غير OBJ؟**  
ج: بالطبع. طريقة `Scene.save` تدعم FBX و STL والعديد من الصيغ الأخرى — فقط غيّر تعداد `FileFormat`.

## الخلاصة

من خلال تعيين متجه ارتفاع مخصص، يمكنك تغيير اتجاه المستوى لإنشاء هندسة مائلة ثم تصدير النتيجة كملف OBJ ببضع أسطر من الشيفرة فقط. يضمن هذا النهج أن نماذجك ثلاثية الأبعاد تحتفظ بالميل المقصود وتكون جاهزة للأنابيب اللاحقة مثل محركات الألعاب، أدوات CAD، أو عارضات الويب.

---

**Last Updated:** 2026-10-24  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## دروس ذات صلة

- [تصدير نموذج إلى FBX باستخدام الكواترنيونات في Java باستخدام Aspose.3D](/3d/java/geometry/transform-3d-nodes-with-quaternions/)
- [تعلم تصدير ملفات PLY في Java باستخدام Aspose.3D – كيفية تصدير ply](/3d/java/point-clouds/ply-export-point-clouds-java/)
- [حفظ المشاهد ثلاثية الأبعاد في Java باستخدام Aspose.3D – تحويل ملفات 3D بكفاءة](/3d/java/load-and-save/save-3d-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}