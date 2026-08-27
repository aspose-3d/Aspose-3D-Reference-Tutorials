---
date: 2026-06-13
description: تعلم درسًا في رسومات 3D بلغة Java حول التحكم في المركز في Linear Extrusion
  باستخدام Aspose.3D، بما في ذلك كيفية ضبط rounding radius وحفظ ملف OBJ بلغة Java.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: التحكم في المركز في Linear Extrusion باستخدام Aspose.3D لـ Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: إنشاء شبكة ثلاثية الأبعاد Java – المركز في Linear Extrusion
url: /ar/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إنشاء شبكة ثلاثية الأبعاد Java – المركز في السحب الخطي

## المقدمة

إذا كنت تبني تصورات ثلاثية الأبعاد في Java، فإن إتقان تقنيات السحب أمر أساسي. يوضح لك هذا **java 3d graphics tutorial** كيفية **create 3d mesh java** الكائنات عن طريق التحكم في مركز السحب الخطي باستخدام Aspose.3D for Java. بحلول نهاية هذا الدليل ستفهم لماذا خاصية `center` مهمة، وكيفية **set rounding radius**، وكيفية **save obj file java**‑compatible output. كما سترى كيفية **export 3d model obj** للاستخدام في أي محرر ثلاثي الأبعاد رئيسي.

## الإجابات السريعة

- **What does the center property do?** يحدد ما إذا كان السحب متماثلًا حول أصل الملف التعريفي.  
- **Do I need a license to run the code?** ترخيص مؤقت يعمل للاختبار؛ يلزم ترخيص كامل للإنتاج.  
- **Which file format is used for the result?** يتم حفظ المشهد كملف Wavefront OBJ.  
- **Can I change the number of slices?** نعم، استخدم `setSlices(int)` على كائن `LinearExtrusion`.  
- **Is Aspose.3D compatible with Java 8+?** بالتأكيد – يدعم جميع إصدارات Java الحديثة.

## ما هو java 3d graphics tutorial؟

إن **java 3d graphics tutorial** هو دليل خطوة بخطوة يعلمك كيفية استخدام مكتبات Java لإنشاء وتعديل وعرض الكائنات ثلاثية الأبعاد. في هذا الدليل ستتعلم **create 3d mesh java** عن طريق تحويل ملف تعريفي ثنائي الأبعاد إلى نموذج ثلاثي الأبعاد كامل، التحكم في محاذاته المركزية، تقويس زوايا السحب، وأخيرًا تصدير النتيجة كملف OBJ يمكن لأي برنامج ثلاثي الأبعاد قراءته.

## لماذا تستخدم Aspose.3D for Java؟

توفر Aspose.3D for Java واجهة برمجة تطبيقات عالية المستوى تُلغي الحاجة إلى حسابات الشبكة اليدوية، مما يتيح لك التركيز على التصميم بدلاً من الهندسة منخفضة المستوى. تدعم **50+ input and output formats** — بما في ذلك OBJ و FBX و STL و GLTF — بحيث يمكنك **export 3d model obj** أو أي تنسيق آخر باستدعاء طريقة واحدة. تعالج المكتبة مشاهد مئات الصفحات دون تحميل الملف بالكامل إلى الذاكرة، مما يقدم **أداء أسرع حتى 3×** مقارنةً بأنابيب OpenGL الخام على عتاد الخادم العادي.

## المتطلبات المسبقة

1. **Java Development Environment** – تثبيت JDK 8 أو أحدث.  
2. **Aspose.3D for Java** – تنزيل المكتبة والوثائق [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – إنشاء مجلد على جهازك لتخزين الملفات المُولدة؛ سنشير إليه باسم **“Your Document Directory.”**

## استيراد الحزم

في بيئة تطوير Java IDE الخاصة بك، استورد فئات Aspose.3D التي تحتاجها. هذا يمنح المترجم إمكانية الوصول إلى ميزات السحب وبناء المشهد.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## دليل خطوة بخطوة

### الخطوة 1: إعداد الملف التعريفي الأساسي

أولاً، أنشئ الشكل الثنائي الأبعاد الذي سيُسحب. هنا نستخدم مستطيلًا و**set rounding radius** إلى 0.3، مما يُنعّم الزوايا ويظهر كيفية **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### الخطوة 2: إنشاء مشهد ثلاثي الأبعاد

**Scene** هو الحاوية العليا التي تحتوي على جميع الكائنات ثلاثية الأبعاد، الأضواء، والكاميرات.

```java
Scene scene = new Scene();
```

### الخطوة 3: إضافة عقد اليسار واليمين

**Node** تمثل كائنًا قابلًا للتحويل في رسم المشهد، مما يسمح بالتموضع والهرمية.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### الخطوة 4: سحب خطي – بدون مركز (عقدة اليسار)

**LinearExtrusion** يحول ملفًا تعريفيًا ثنائي الأبعاد إلى شبكة ثلاثية الأبعاد عن طريق مسحه على طول خط مستقيم.  
**setCenter(boolean)** يبدّل ما إذا كان السحب متمركزًا حول أصل الملف التعريفي.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### الخطوة 5: إضافة سطح أرضي للمرجعية (عقدة اليسار)

صندوق رقيق يعمل كأرضية بصرية، يساعدك على رؤية اتجاه السحب.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### الخطوة 6: سحب خطي – متمركز (عقدة اليمين)

الآن كرر السحب، هذه المرة مفعلاً `center`. ستكون الهندسة متماثلة حول أصل الملف التعريفي، مما يمنحك نتيجة **create 3d mesh java** متوازنة تمامًا.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### الخطوة 7: إضافة سطح أرضي للمرجعية (عقدة اليمين)

نفس السطح الأرضي للجانب الأيمن، لتوضيح المقارنة.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### الخطوة 8: حفظ المشهد ثلاثي الأبعاد

أخيرًا، صدّر المشهد بالكامل إلى ملف Wavefront OBJ – تنسيق قابل للاستخدام بسهولة في معظم محررات 3‑D. تقوم طريقة `save` تلقائيًا بتحويل الشبكة إلى مواصفات OBJ، مما يتيح لك **save obj file java** دون أي معالجة لاحقة إضافية.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## المشكلات الشائعة والحلول

| المشكلة | لماذا يحدث | الحل |
|-------|----------------|-----|
| **Extrusion appears offset** | `setCenter(false)` يترك الملف التعريفي مثبتًا عند زاويته. | استخدم `setCenter(true)` للحصول على نتائج متماثلة. |
| **OBJ file is empty** | مسار دليل الإخراج غير صحيح أو يفتقر إلى أذونات الكتابة. | تحقق من أن `MyDir` يشير إلى مجلد موجود وأن التطبيق يملك صلاحية الكتابة. |
| **Rounded corners look sharp** | نصف قطر التقويس صغير جدًا بالنسبة لحجم المستطيل. | زد قيمة نصف القطر (مثلاً `setRoundingRadius(0.5)`). |

## الأسئلة المتكررة

### س1: هل يمكنني استخدام Aspose.3D for Java في المشاريع التجارية؟

ج1: نعم، Aspose.3D for Java متاح للاستخدام التجاري. للحصول على تفاصيل الترخيص، زر [here](https://purchase.aspose.com/buy).

### س2: هل هناك نسخة تجريبية مجانية متاحة؟

ج2: نعم، يمكنك تجربة نسخة تجريبية مجانية من Aspose.3D for Java [here](https://releases.aspose.com/).

### س3: أين يمكنني العثور على الدعم لـ Aspose.3D for Java؟

ج3: منتدى مجتمع Aspose.3D هو مكان رائع للحصول على الدعم ومشاركة تجاربك. زر المنتدى [here](https://forum.aspose.com/c/3d/18).

### س4: هل أحتاج إلى ترخيص مؤقت للاختبار؟

ج4: نعم، إذا كنت تحتاج إلى ترخيص مؤقت لأغراض الاختبار، يمكنك الحصول عليه [here](https://purchase.aspose.com/temporary-license/).

### س5: أين يمكنني العثور على الوثائق؟

ج5: الوثائق الخاصة بـ Aspose.3D for Java متاحة [here](https://reference.aspose.com/3d/java/).

## الخلاصة

من خلال إكمال هذا **java 3d graphics tutorial**، أصبحت الآن تعرف كيفية **create 3d mesh java** الكائنات، التحكم في مركز السحب الخطي، ضبط نصف قطر التقويس، و**save obj file java** الناتج باستخدام Aspose.3D. تمنحك هذه التقنيات تحكمًا دقيقًا في تماثل الشبكة، وهو أمر حيوي لأصول الألعاب، نماذج CAD، والتصوير العلمي. لا تتردد في تجربة ملفات تعريفية مختلفة، عدد الشرائح، وتنسيقات التصدير لتوسيع صندوق أدواتك ثلاثي الأبعاد.

---

**آخر تحديث:** 2026-06-13  
**تم الاختبار مع:** Aspose.3D for Java 24.11  
**المؤلف:** Aspose

## الدروس ذات الصلة

- [إنشاء سحب ثلاثي الأبعاد Java باستخدام Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [كيفية تعيين الاتجاه في السحب الخطي باستخدام Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [إنشاء مشهد ثلاثي الأبعاد مع التواء في السحب الخطي – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}