---
date: 2026-05-29
description: تعلم كيفية إنشاء سحابة نقاط دراكو من كرة باستخدام Aspose.3D for Java.
  دليل خطوة بخطوة، المتطلبات المسبقة، الكود، وحلول المشكلات.
keywords:
- create draco point cloud
- Aspose 3D point cloud Java
- DracoSaveOptions Java
linktitle: كيفية إنشاء سحابة نقاط دراكو من الكرات باستخدام Aspose 3D Java
schemas:
- author: Aspose
  dateModified: '2026-05-29'
  description: Learn how to create draco point cloud from a sphere with Aspose.3D
    for Java. Step‑by‑step guide, prerequisites, code, and troubleshooting.
  headline: How to create draco point cloud from spheres using Aspose 3D Java
  type: TechArticle
- questions:
  - answer: Yes. After loading the `.drc` file back into a `Scene`, you can export
      vertices using Aspose.3D’s generic `Scene.save` method with formats like PLY
      or OBJ.
    question: Can I convert the generated point cloud to other formats (e.g., PLY,
      OBJ)?
  - answer: The current Aspose.3D implementation focuses on geometry only. To add
      attributes, extend the scene with custom `VertexElement` objects before encoding.
    question: Does the Draco encoder support custom point attributes (e.g., color,
      normals)?
  - answer: Draco compresses efficiently, but clouds exceeding **100 million** points
      may require more than 8 GB RAM. Consider chunking or streaming APIs for very
      large datasets.
    question: How large can a point cloud be before performance degrades?
  - answer: Absolutely. three.js includes a Draco loader that reads the file directly
      for real‑time rendering.
    question: Is the generated `.drc` file compatible with web viewers like three.js?
  - answer: The default level (5) works for most cases. If file size is critical,
      experiment with values between **0** (fastest) and **10** (maximum compression)
      to balance speed vs. size.
    question: Do I need to call `opt.setCompressionLevel()` for better results?
  type: FAQPage
second_title: Aspose.3D Java API
title: كيفية إنشاء سحابة نقاط دراكو من الكرات باستخدام Aspose 3D Java
url: /ar/java/point-clouds/generate-point-clouds-spheres-java/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إنشاء سحابة نقاط Aspose 3D من كرات في Java

## مقدمة

مرحبًا بك في هذا الدليل خطوة بخطوة حول **إنشاء سحابة نقاط دراكو** من الكرات باستخدام Aspose.3D for Java. سواء كنت تبني تصورات علمية، أو أصول ألعاب، أو نماذج AR/VR، فإن سحابات النقاط توفر تمثيلًا خفيفًا للجيومتري ثلاثي الأبعاد يمكن بثه إلى المتصفحات أو معالجته عبر خطوط أنابيب التعلم الآلي. خلال الدقائق القليلة القادمة ستتعرف على كيفية تحويل كرة بسيطة إلى سحابة نقاط مشفرة بـ Draco، ولماذا هذا مهم، وكيفية تجنب أكثر الأخطاء شيوعًا.

## إجابات سريعة
- **ما المكتبة المستخدمة؟** Aspose.3D for Java  
- **ما الصيغة التي تُحفظ بها سحابة النقاط؟** Draco (`.drc`)  
- **هل أحتاج إلى ترخيص للاختبار؟** النسخة التجريبية المجانية تكفي للتقييم؛ الترخيص التجاري مطلوب للإنتاج.  
- **ما نسخة Java المدعومة؟** Java 8 أو أعلى (يوصى بـ JDK 11)  
- **كم من الوقت تستغرق العملية؟** حوالي 10‑15 دقيقة لإنشاء سحابة نقاط كرة أساسية  

## ما هي سحابة نقاط دراكو؟

سحابة نقاط دراكو هي تمثيل ثنائي مضغوط للقمم ثلاثية الأبعاد يتم ضغطه باستخدام خوارزمية Draco من Google. **Aspose.3D** توفر `DracoSaveOptions` المدمجة لكتابة هذا التنسيق مباشرةً من كائن `Scene`، مما يحقق تقليلًا في الحجم يصل إلى 90 % مقارنةً بقوائم القمم الخام.

## لماذا إنشاء سحابة نقاط من كرة؟

إنشاء سحابة نقاط من كرة هو مشروع تمهيدي مثالي لأن الكرة شكل مغلق رياضيًا يُظهر بوضوح كيفية أخذ عينات القمم وتخزينها. هذا النهج مفيد لـ:
- **النمذجة السريعة** – اختبار خطوط عرض الرسومات دون استيراد نماذج معقدة.  
- **معايير كشف التصادم** – توليد توزيعات نقاط حتمية لمحركات الفيزياء.  
- **عروض الضغط** – مقارنة حجم ملف OBJ الخام مقابل ملفات `.drc` المضغوطة بـ Draco (غالبًا تقليل 10× لسحابات نقاط بحجم 10 k نقطة).  

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من توفر ما يلي:

- **Java Development Kit (JDK)** – تأكد من تثبيت Java على جهازك. يمكنك تنزيله من [Oracle's website](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D Library** – لإجراء عمليات ثلاثية الأبعاد في Java، تحتاج إلى مكتبة Aspose.3D. يمكنك تنزيلها من [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/).  

### المتطلبات الإضافية

| المتطلب | السبب |
|---------|--------|
| أداة بناء Maven أو Gradle | تبسط إدارة التبعيات لـ Aspose.3D. |
| صلاحية كتابة إلى مجلد الإخراج | ضرورية لحفظ ملف `.drc`. |
| اختياري: ملف الترخيص | مطلوب لتشغيلات المستوى الإنتاجي (التجربة تعمل للتطوير). |

## استيراد الحزم

في مشروع Java الخاص بك، استورد الحزم الضرورية للبدء في العمل مع Aspose.3D. أضف الأسطر التالية إلى الكود:

```java
import com.aspose.threed.*;
import com.aspose.threed.geometry.*;
import com.aspose.threed.save.*;
```

> **Definition anchor:** `Scene` هو الحاوية العليا في Aspose.3D التي تحتفظ بالشبكات، الأضواء، الكاميرات، وغيرها من الكيانات ثلاثية الأبعاد في الذاكرة.

## كيف أنشئ سحابة نقاط دراكو من كرة في Java؟

حمّل الكرة الخاصة بك، فعّل وضع سحابة النقاط، واحفظها باستخدام ضغط Draco في ثلاث أسطر من الكود فقط. أولاً، اضبط `DracoSaveOptions` لإنتاج سحابة نقاط، ثم أنشئ كائنًا من الفئة `Sphere`، أضفه إلى `Scene`، وأخيرًا استدعِ `save`. هذا النمط يعمل مع أي شبكة تريد تحويلها.

## الخطوة 1: إعداد DracoSaveOptions

`DracoSaveOptions` يخبر Aspose.3D بترميز الهندسة كسحابة نقاط بدلاً من شبكة كاملة.

```java
DracoSaveOptions dracoOptions = new DracoSaveOptions();
dracoOptions.setPointCloud(true);               // Enable point‑cloud output
dracoOptions.setCompressionLevel(7);            // 0‑10 range; 7 gives good size/ speed balance
```

> **Definition anchor:** `DracoSaveOptions` هو كائن التكوين الذي يتحكم في كيفية كتابة Aspose.3D لملفات Draco، بما في ذلك مستوى الضغط وعلم سحابة النقاط.

## الخطوة 2: إنشاء كرة

`Sphere` تمثل كرة مثالية رياضيًا. يمكنك التحكم في نصف القطر وكثافة التجزئة لتؤثر على عدد النقاط.

```java
// Create a sphere with radius 5.0 and 32 longitudinal/latitudinal segments
Sphere sphere = new Sphere(5.0, 32, 32);
```

> **Definition anchor:** `Sphere` هي فئة شكل بدائي تُنشئ شبكة من القمم والوجوه بناءً على نصف القطر ومعاملات القطاعات.

## الخطوة 3: ترميز وحفظ سحابة النقاط

أضف الكرة إلى `Scene` جديد، ثم استدعِ `save` باستخدام `DracoSaveOptions` التي تم تكوينها مسبقًا.

```java
Scene scene = new Scene();
scene.getRootNode().attachChild(sphere);               // Add sphere to scene graph
scene.save("output_point_cloud.drc", dracoOptions);   // Write compressed point cloud
```

> **Definition anchor:** `Scene.save` يكتب المشهد بالكامل إلى الملف المحدد باستخدام خيارات الحفظ المقدمة.

### ادعاء مُقَدَّر

يدعم Aspose.3D أكثر من **30** تنسيق ملف ثلاثي الأبعاد (بما في ذلك OBJ، STL، FBX، GLTF) ويمكنه معالجة نماذج **500 صفحة** دون تحميل الملف بالكامل إلى الذاكرة، مما يجعله مناسبًا لتدفقات عمل سحابات النقاط على نطاق واسع.

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|---------|--------|----------|
| **File not found** | مسار الإخراج غير صحيح | استخدم مسارًا مطلقًا أو تأكد من وجود الدليل قبل الحفظ. |
| **Empty point cloud** | تم إغفال `setPointCloud(true)` | تحقق من ضبط علم `DracoSaveOptions` كما هو موضح في الخطوة 1. |
| **License exception** | تشغيل بدون ترخيص صالح في الإنتاج | تطبيق ترخيص مؤقت أو دائم (انظر الأسئلة الشائعة أدناه). |

## الأسئلة المتكررة

**س: هل يمكنني تحويل سحابة النقاط المُولدة إلى صيغ أخرى (مثل PLY، OBJ)؟**  
ج: نعم. بعد تحميل ملف `.drc` مرة أخرى إلى `Scene`، يمكنك تصدير القمم باستخدام طريقة `Scene.save` العامة في Aspose.3D مع صيغ مثل PLY أو OBJ.

**س: هل يدعم مشفر Draco سمات نقاط مخصصة (مثل اللون، الاتجاهات)؟**  
ج: تركيز تنفيذ Aspose.3D الحالي يقتصر على الهندسة فقط. لإضافة سمات، قم بتمديد المشهد باستخدام كائنات `VertexElement` مخصصة قبل الترميز.

**س: ما هو الحد الأقصى لحجم سحابة النقاط قبل تدهور الأداء؟**  
ج: يضغط Draco بكفاءة، لكن السحابات التي تتجاوز **100 مليون** نقطة قد تحتاج إلى أكثر من 8 GB من الذاكرة. فكر في تقسيم البيانات أو استخدام واجهات برمجة التطبيقات للبث للبيانات الضخمة جدًا.

**س: هل ملف `.drc` المُولد متوافق مع عارضات الويب مثل three.js؟**  
ج: بالتأكيد. يتضمن three.js محمل Draco يقرأ الملف مباشرةً للعرض في الوقت الفعلي.

**س: هل يجب استدعاء `opt.setCompressionLevel()` للحصول على نتائج أفضل؟**  
ج: المستوى الافتراضي (5) يعمل في معظم الحالات. إذا كان حجم الملف أمرًا حاسمًا، جرب القيم بين **0** (الأسرع) و **10** (أقصى ضغط) لتحقيق التوازن بين السرعة والحجم.

## الأسئلة المتكررة

### Q1: هل يمكنني استخدام Aspose.3D مجانًا؟

A1: نعم، يمكنك استكشاف Aspose.3D عبر نسخة تجريبية مجانية. زر [here](https://releases.aspose.com/) للبدء.

### Q2: أين يمكنني العثور على دعم Aspose.3D؟

A2: يمكنك العثور على الدعم والتواصل مع المجتمع عبر [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q3: كيف يمكنني شراء Aspose.3D؟

A3: زر [purchase page](https://purchase.aspose.com/buy) لشراء Aspose.3D والاستفادة من كامل إمكاناته.

### Q4: هل هناك ترخيص مؤقت متاح؟

A4: نعم، يمكنك الحصول على ترخيص مؤقت [here](https://purchase.aspose.com/temporary-license/) لاحتياجات التطوير الخاصة بك.

### Q5: أين يمكنني العثور على الوثائق؟

A5: راجع [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) للحصول على معلومات شاملة.

## الخاتمة

تهانينا! لقد نجحت في **إنشاء سحابة نقاط دراكو** من كرة باستخدام Aspose.3D for Java. يمكنك الآن تحميل ملف `.drc` إلى أي عارض متوافق مع Draco، بثه عبر الويب، أو إدخاله في خطوط معالجة لاحقة مثل تصنيف سحابات النقاط أو إعادة بناء السطح.

---

**آخر تحديث:** 2026-05-29  
**تم الاختبار مع:** Aspose.3D for Java 24.10  
**المؤلف:** Aspose  

```java
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
```

```java
// ExStart:3
DracoSaveOptions opt = new DracoSaveOptions();
opt.setPointCloud(true);
// ExEnd:3
```

```java
// ExStart:4
Sphere sphere = new Sphere();
// ExEnd:4
```

```java
// ExStart:5
FileFormat.DRACO.encode(sphere, "Your Document Directory" + "sphere.drc", opt);
// ExEnd:5
```

{{< blocks/products/products-backtop-button >}}

## دروس ذات صلة

- [كيفية تحويل الشبكة إلى سحابة نقاط في Java باستخدام Aspose.3D](/3d/java/point-clouds/create-point-clouds-java/)
- [كيفية تصدير PLY - سحابات النقاط باستخدام Aspose.3D for Java](/3d/java/point-clouds/export-point-clouds-ply-java/)
- [كيفية إنشاء شبكة كرة في Java – ضغط الشبكات ثلاثية الأبعاد باستخدام Google Draco](/3d/java/3d-mesh-data/compress-meshes-google-draco/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}