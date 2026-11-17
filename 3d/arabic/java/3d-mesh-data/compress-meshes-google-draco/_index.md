---
date: 2026-11-17
description: كيفية تقليل حجم نموذج 3D عن طريق إنشاء شبكة كرة في Java وضغطها باستخدام
  Google Draco عبر Aspose.3D. تعلم سير العمل الكامل في دقائق.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: كيفية تقليل حجم نموذج 3D – إنشاء شبكة كرة في Java باستخدام Google Draco
og_description: إنشاء شبكة كرة وضغط نموذج 3D باستخدام Java عبر Aspose.3D وGoogle Draco.
  يوضح هذا الدرس كيفية إنشاء كرة، وتصديرها إلى .drc وتحقيق تقليل الحجم حتى 95٪ في
  دقائق.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: إنشاء شبكة كرة وضغط نموذج 3D باستخدام Java وDraco
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: كيفية تقليل حجم نموذج 3D باستخدام شبكة كرة Java وDraco
url: /ar/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تقليل حجم نموذج ثلاثي الأبعاد باستخدام شبكة كرة Java و Draco

## مقدمة

Aspose.3D for Java هي مكتبة تمكّن من إنشاء ومعالجة وتحويل نماذج ثلاثية الأبعاد مباشرةً من كود Java. إذا كنت تبحث عن طريقة سريعة لـ **تقليل حجم النموذج ثلاثي الأبعاد** مع الحفاظ على جودة الهندسة العالية، فقد وجدت المكان المناسب. في هذا الدرس سنستعرض إنشاء شبكة كرة باستخدام **Aspose.3D for Java** ثم ضغط تلك الشبكة باستخدام **Google Draco**. في النهاية ستحصل على ملف `.drc` جاهز للاستخدام أصغر بشكل كبير من الأصلي، مما يجعله مثالياً لعروض الويب، ألعاب الهواتف المحمولة، أو أي تطبيق Java محدود النطاق الترددي.

## إجابات سريعة
- **ما الذي يغطيه هذا الدرس؟** إنشاء شبكة كرة في Java وضغطها باستخدام Google Draco عبر Aspose.3D.  
- **المكتبة الأساسية؟** Aspose.3D for Java (تُستخدم لإنشاء الشبكة وتصدير Draco).  
- **الوقت النموذجي للتنفيذ؟** حوالي 10‑15 دقيقة لإنشاء كرة أساسية.  
- **المتطلب الأساسي؟** بيئة تطوير Java مع ملفات Aspose.3D JAR على مسار الفئة.  
- **النتيجة؟** ملف `.drc` **يقلل حجم النموذج ثلاثي الأبعاد** بنسبة تصل إلى 95 % مقارنةً بشبكة غير مضغوطة.

## كيفية تقليل حجم النموذج ثلاثي الأبعاد؟

حمّل كرتك واضغطها في خطوتين بسيطتين. أولاً، **تنشئ شبكة كرة** باستخدام `new Sphere(1.0, 32, 32)`. ثم تقوم بتصدير المشهد مباشرةً إلى Draco باستخدام `scene.save("sphere.drc", SaveFormat.Draco)`. تتعامل Aspose.3D مع تقليل دقة الهندسة وإزالة التكرار في الرؤوس تلقائيًا، مما ينتج ملفات أصغر عادةً بنسبة 80‑95 % مع الحفاظ على جودة العرض.

الفئة `Sphere` هي مولد الهندسة المدمج في Aspose.3D الذي ينشئ شبكة كرة مُثلثة. تقبل نصف القطر ومعلمات التشعب، مما يتيح لك التحكم في مستوى التفاصيل قبل الضغط.

## ما معنى “تقليل حجم النموذج ثلاثي الأبعاد” في سياق تطوير ثلاثي الأبعاد؟

**تقليل حجم النموذج ثلاثي الأبعاد** يعني تقليل كمية بيانات الهندسة التي تحتاج إلى نقلها أو تخزينها، دون تدهور ملحوظ في جودة العرض. يحقق Draco ذلك عن طريق ترميز مواضع الرؤوس، والاتجاهات، والسمات الأخرى في تنسيق ثنائي مضغوط للغاية. عند الجمع مع Aspose.3D، يبقى سير العمل بالكامل داخل Java، لذا لا تحتاج إلى التعامل مع ملفات ثنائية أصلية.

## لماذا نستخدم ضغط شبكة Google Draco مع Aspose.3D؟

يقدم Google Draco مع Aspose.3D خط أنابيب فعال يضغط ملفات الشبكة بشكل كبير مع الحفاظ على سهولة دمجها في مشاريع Java. تتولى المكتبة جميع عمليات الترميز منخفضة المستوى، مما يسمح للمطورين بالتركيز على إنشاء الهندسة دون الحاجة للتعامل مع ملفات Draco الأصلية، مما ينتج عنه تطوير أسرع وأصول أصغر للويب والهواتف المحمولة.

- **تقليل حجم هائل:** يمكن لـ Draco تقليل بيانات الشبكة بنسبة تصل إلى 95 % للنماذج النموذجية، تحويل ملف OBJ بحجم 5 ميغابايت إلى `.drc` بحجم 0.3 ميغابايت.  
- **فك تشفير سريع أثناء التشغيل:** تقوم محركات مثل Unity و Unreal و three.js بفك تشفير Draco أصليًا، مما يؤدي إلى أوقات تحميل أسرع.  
- **تكامل سلس مع Java:** تقوم Aspose.3D بتجريد مكتبة Draco الأصلية، مما يتيح لك البقاء في بيئة Java.  
- **تصدير Aspose 3D شامل:** نفس الـ API الذي تستخدمه لإنشاء الهندسة يتعامل أيضًا مع التصدير، مما يبسط خط الأنابيب.  

تدعم Aspose.3D **أكثر من 50 تنسيق إدخال وإخراج** — بما في ذلك OBJ و FBX و STL و GLTF والعديد غيرها — ويمكنها معالجة نماذج مئات الصفحات دون تحميل الملف بالكامل إلى الذاكرة.

## المتطلبات المسبقة

- **مجموعة تطوير Java (JDK)** – الإصدار 8 أو أحدث.  
- **Aspose.3D for Java** – قم بتحميل أحدث ملفات JAR من **[صفحة إصدارات Aspose 3D Java](https://releases.aspose.com/3d/java/)**.  
- **إلمام أساسي بـ Google Draco** – ستستخدم غلاف Aspose.3D، لذا لا يلزم إعداد Draco الأصلي.

## استيراد الحزم

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## دليل خطوة بخطوة

### الخطوة 1: إعداد المشروع

أنشئ مشروع Java جديد (أي بيئة تطوير متكاملة تعمل) وأضف جميع ملفات Aspose.3D JAR إلى مسار الفئة. احتفظ بملفات المصدر في حزمة مثل `com.example.draco` للوضوح.

### الخطوة 2: كيفية إنشاء شبكة كرة في Java

الفئة `Sphere` هي مولد الهندسة المدمج في Aspose.3D الذي ينشئ شبكة كرة مُثلثة.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **نصيحة احترافية:** الفئة `Sphere` تُنشئ شبكة مُثلثة بنصف قطر افتراضي قدره 1.0. يمكنك تمرير نصف قطر مخصص، أو تشعب، أو معلمات مادة إذا كنت بحاجة إلى مستوى تفاصيل مختلف قبل الضغط.

### الخطوة 3: تصدير الشبكة إلى تنسيق Draco

الفئة `Scene` تمثل مشهدًا ثلاثي الأبعاد كاملًا يمكن أن يحتوي على شبكات، وإضاءات، وكاميرات. الفئة `DracoCompressionOptions` تتيح لك تخصيص إعدادات ضغط Draco مثل الكميّة ومستوى الضغط. بعد إضافة الكرة إلى كائن `Scene`، استدعِ `scene.save("sphere.drc", SaveFormat.Draco)`. تقوم Aspose.3D تلقائيًا باختيار إعدادات الضغط المثالية، ولكن يمكنك ضبطها بدقة عن طريق تعديل `DracoCompressionOptions` إذا كنت بحاجة إلى أصغر ملف ممكن. `DracoCompressionOptions` تتيح لك

### الخطوة 4: التحقق من الإخراج

الفئة `DRACOLoader` هي أداة في three.js تقوم بتحميل ملفات `.drc` المضغوطة بـ Draco وتحويلها إلى هندسة متوافقة مع WebGL. افتح ملف `.drc` المُولد باستخدام عارض Draco (مثل three.js `DRACOLoader`) للتأكد من أن الهندسة تُعرض بشكل صحيح. ستلاحظ انخفاضًا كبيرًا في حجم الملف — غالبًا ما يكون بمقدار عشرة أضعاف أو أكثر.

## حالات الاستخدام الشائعة

| السيناريو | لماذا تقليل حجم النموذج؟ | كيف يساعد هذا الدرس |
|----------|-----------------------|--------------------------|
| مُكوّنات المنتجات على الويب | تحميل الصفحات أسرع على الاتصالات البطيئة | ملفات `.drc` المضغوطة بـ Draco تُحمَّل في ثوانٍ |
| تطبيقات AR/VR المحمولة | استهلاك ذاكرة أقل على الأجهزة | شبكات أصغر تحافظ على استجابة التطبيق |
| مشاهد سحابية مُصدَّرة | تقليل تكاليف النطاق الترددي | تصدير بنقرة واحدة من Aspose.3D إلى Draco |

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| **`NoClassDefFoundError` لفئات Draco** | ملفات Aspose.3D JAR غير موجودة في مسار الفئة | تحقق من تضمين *جميع* ملفات Aspose.3D JAR وأن الإصدار يتطابق مع الوثائق. |
| **ملف الإخراج فارغ** | `MyDir` يشير إلى مجلد غير موجود | أنشئ المجلد برمجيًا (`Files.createDirectories(Paths.get(MyDir))`) قبل كتابة الملف. |
| **الشبكة المضغوطة تبدو مشوهة** | استخدام مستوى ضغط منخفض أو تشعب غير كافٍ | تحول إلى `DracoCompressionLevel.OPTIMAL` وزد تشعب الكرة (مثال: `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` يختار أعلى جودة ضغط لإخراج Draco. |

## الأسئلة المتكررة

**س: هل Aspose.3D متوافق مع صيغ ملفات ثلاثية الأبعاد المختلفة؟**  
ج: نعم، تدعم Aspose.3D صيغ OBJ و FBX و STL و GLTF والعديد غيرها، مما يجعلها خيارًا متعدد الاستخدامات لخطوط **تصدير Aspose 3d**.

**س: هل يمكنني استخدام Google Draco للضغط في لغات برمجة أخرى؟**  
ج: بالتأكيد. يقدم Draco مكتبات أصلية لـ C++ و Python و JavaScript. يركز هذا الدرس على Java، لكن المفاهيم تنطبق عبر اللغات.

**س: أين يمكنني العثور على وثائق Aspose.3D إضافية؟**  
ج: زر **[توثيق Aspose.3D Java](https://reference.aspose.com/3d/java/)** للحصول على مراجع API كاملة والمزيد من الأمثلة.

**س: كيف أحصل على ترخيص مؤقت لـ Aspose.3D؟**  
ج: استكشف خيارات الترخيص المؤقت على **[صفحة الترخيص المؤقت لـ Aspose](https://purchase.aspose.com/temporary-license/)**.

**س: هل هناك منتدى مجتمع لدعم Aspose.3D؟**  
ج: نعم، انضم إلى النقاش في **[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18)**.

## الخلاصة

في هذا الدليل أظهرنا كيفية **تقليل حجم النموذج ثلاثي الأبعاد** عن طريق إنشاء شبكة كرة في Java ثم ضغطها باستخدام Google Draco عبر Aspose.3D. باتباع هذه الخطوات المختصرة يمكنك تقليل حجم ملفات الشبكة بشكل كبير، تحسين أوقات التحميل، والحفاظ على تطبيقات Java ثلاثية الأبعاد سريعة الاستجابة وصديقة للنطاق الترددي.

---

**آخر تحديث:** 2026-11-17  
**تم الاختبار مع:** Aspose.3D for Java 24.12 (latest)  
**المؤلف:** Aspose

## دروس ذات صلة

- [تقليل حجم ملف 3D – ضغط المشاهد باستخدام Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [إنشاء سحابة نقاط Draco من كرات باستخدام Aspose.3D for Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [تعلم كيفية مثلثية الشبكات لتحسين العرض في Java باستخدام Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}