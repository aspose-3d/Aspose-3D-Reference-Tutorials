---
date: 2026-05-24
description: تعلم كيفية إنشاء استخراج ثلاثي الأبعاد باستخدام الشرائح باستخدام Aspose.3D
  for Java. يغطي هذا الدليل خطوة بخطوة الاستخراج الخطي، تعيين نصف قطر التقريب، وتصدير
  OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: إنشاء استخراج ثلاثي الأبعاد باستخدام الشرائح – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: إنشاء استخراج ثلاثي الأبعاد باستخدام الشرائح – Aspose.3D for Java
url: /ar/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إنشاء استخراج ثلاثي الأبعاد مع الشرائح – Aspose.3D for Java

## المقدمة

إذا كنت بحاجة إلى **إنشاء استخراج ثلاثي الأبعاد** يبدو ناعماً ودقيقاً، فإن التحكم في عدد الشرائح هو المفتاح. في هذا الدرس سنستعرض كيفية تحديد الشرائح أثناء تنفيذ استخراج خطي باستخدام Aspose.3D for Java. سترى لماذا عدد الشرائح مهم، وكيفية ضبط نصف قطر التقريب، وكيفية تصدير النتيجة كملف OBJ يمكن استخدامه في أي خط أنابيب ثلاثي الأبعاد.

## إجابات سريعة
- **ما الذي تتحكم فيه “الشرائح”؟** عدد المقاطع العرضية المتوسطة المستخدمة لتقريب سطح الاستخراج.  
- **أي طريقة تحدد عدد الشرائح؟** `LinearExtrusion.setSlices(int)`  
- **هل يمكنني تغيير نصف قطر التقريب للملف الشخصي؟** نعم، عبر `RectangleShape.setRoundingRadius(double)`  
- **ما هو تنسيق الملف المستخدم في هذا المثال؟** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **هل أحتاج إلى ترخيص لتشغيل الكود؟** النسخة التجريبية المجانية تكفي للتقييم؛ يلزم ترخيص تجاري للإنتاج.

`LinearExtrusion.setSlices(int)` يحدد عدد الشرائح المتوسطة التي سيولدها الاستخراج.  
`RectangleShape.setRoundingRadius(double)` يحدد نصف قطر الزاوية لملف تعريف مستطيل.

## كيفية إنشاء استخراج ثلاثي الأبعاد في Java مع الشرائح؟

حمّل ملف التعريف ثنائي الأبعاد الخاص بك، اختر عدد الشرائح، اضبط نصف قطر التقريب، واستدعِ `save` – يتناسب سير العمل بالكامل مع بضع أسطر. Aspose.3D for Java يتعامل مع إنشاء الهندسة، واستيفاء الشرائح، وتصدير OBJ تلقائيًا، بحيث يمكنك التركيز على جودة العرض بدلاً من حسابات الشبكة منخفضة المستوى.

## ما هو الاستخراج الخطي مع الشرائح؟

يحول الاستخراج الخطي مع الشرائح الشكل الثنائي الأبعاد المسطح إلى صلب ثلاثي الأبعاد عن طريق سحبه على طول خط مستقيم مع توليد عدد قابل للتكوين من المقاطع العرضية المتوسطة. عدد الشرائح يؤثر مباشرة على سلاسة حواف المنحنيات، مثل الزوايا المستديرة، عند العرض.

## لماذا تستخدم Aspose.3D for Java لإنشاء استخراج ثلاثي الأبعاد؟

توفر Aspose.3D **تحكمًا برمجيًا كاملاً** في كل معلمة استخراج، وتدعم **أكثر من 50 تنسيق إدخال وإخراج** (بما في ذلك OBJ و FBX و STL و GLTF)، ويمكنها معالجة **نماذج مئات الصفحات** دون تحميل الملف بالكامل في الذاكرة. تعمل على أي منصة تدعم Java، ولا تتطلب ملفات DLL أصلية، وتضمن نتائج حتمية عبر Windows و Linux و macOS.

## المتطلبات المسبقة

1. **Java Development Kit** – JDK 8 أو أعلى مثبت.  
2. **Aspose.3D for Java** – قم بتنزيل المكتبة من الموقع الرسمي [here](https://releases.aspose.com/3d/java/).  
3. IDE أو محرر نصوص من اختيارك.

## استيراد الحزم

أضف مساحة الأسماء Aspose.3D إلى مشروعك حتى تتمكن من الوصول إلى فئات النمذجة ثلاثية الأبعاد.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## دليل خطوة بخطوة

### الخطوة 1: إعداد المشهد وتعريف الملف الشخصي

`RectangleShape` هي فئة تُعرّف ملف تعريف مستطيل ثنائي الأبعاد.  
أولاً ننشئ `RectangleShape` ونمنحه **نصف قطر التقريب** لجعل الزوايا ناعمة.  
`Scene` هو الحاوية الجذرية لجميع العقد والهندسة.  
ثم نقوم بتهيئة `Scene` جديد سيحتوي على جميع الهندسة.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### الخطوة 2: إنشاء كائنات عقد فرعية لكل استخراج

`Node` يمثل عنصرًا في رسم المشهد يمكنه احتواء الهندسة والتحويلات.  
كل قطعة من الهندسة تعيش تحت `Node`. هنا نقوم بإنشاء عقدتين شقيقتين – واحدة لاستخراج منخفض الشرائح وأخرى لاستخراج عالي الشرائح – ونحرك العقدة اليسرى قليلاً إلى الجانب لتسهيل مقارنة النتائج.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### الخطوة 3: تنفيذ استخراج خطي وتحديد الشرائح

`LinearExtrusion` هي الفئة التي تنشئ صلبًا عن طريق سحب ملف تعريف خطيًا.  
`LinearExtrusion` هي فئة Aspose.3D التي تولد صلبًا باستخراج ملف تعريف ثنائي الأبعاد على طول خط مستقيم. باستخدام **فئة داخلية مجهولة** نستدعي `setSlices` للتحكم في السلاسة. العقدة اليسرى تحصل على 2 شريحة فقط (خشن)، بينما العقدة اليمنى تحصل على 10 شرائح (ناعم).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### الخطوة 4: تصدير OBJ – حفظ المشهد

أخيرًا نكتب المشهد إلى ملف Wavefront OBJ، وهو تنسيق مدعوم على نطاق واسع من قبل محررات 3‑D ومحركات الألعاب. هذا يوضح قدرة **export OBJ Java** في Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## المشكلات الشائعة والحلول

| المشكلة | سبب حدوثه | الحل |
|-------|----------------|-----|
| **يظهر الاستخراج مسطحًا** | تم ضبط عدد الشرائح إلى 1 أو 0 | تأكد من استدعاء `setSlices` بقيمة ≥ 2. |
| **الزوايا المستديرة تبدو متعرجة** | نصف قطر التقريب صغير جدًا مقارنة بعدد الشرائح | زد إما نصف القطر أو عدد الشرائح للحصول على منحنيات أكثر سلاسة. |
| **الملف غير موجود عند الحفظ** | `MyDir` يشير إلى مجلد غير موجود | أنشئ الدليل مسبقًا أو استخدم مسارًا مطلقًا. |

## الأسئلة المتكررة

**س: كيف يمكنني تنزيل Aspose.3D for Java؟**  
ج: يمكنك تنزيل المكتبة [here](https://releases.aspose.com/3d/java/).

**س: أين يمكنني العثور على وثائق Aspose.3D؟**  
ج: راجع الوثائق [here](https://reference.aspose.com/3d/java/).

**س: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج: نعم، يمكنك تجربة النسخة التجريبية [here](https://releases.aspose.com/).

**س: كيف يمكنني الحصول على دعم Aspose.3D؟**  
ج: زر منتدى الدعم [here](https://forum.aspose.com/c/3d/18).

**س: هل يمكنني شراء ترخيص مؤقت؟**  
ج: نعم، يمكن الحصول على ترخيص مؤقت [here](https://purchase.aspose.com/temporary-license/).

---

**آخر تحديث:** 2026-05-24  
**تم الاختبار مع:** Aspose.3D for Java 24.11 (latest at time of writing)  
**المؤلف:** Aspose

## الدروس ذات الصلة

- [إنشاء استخراج ثلاثي الأبعاد Java مع Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [كيفية ضبط الاتجاه في استخراج خطي باستخدام Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [إنشاء مشهد ثلاثي الأبعاد مع التواء في استخراج خطي – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}