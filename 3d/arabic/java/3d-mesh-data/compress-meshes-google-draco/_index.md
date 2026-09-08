---
date: 2026-09-08
description: كيفية تقليل حجم نموذج ثلاثي الأبعاد عن طريق إنشاء شبكة كرة في Java وضغطها
  باستخدام Google Draco عبر Aspose.3D. تعلّم سير العمل الكامل في دقائق.
keywords:
- how to reduce 3d model size
- aspose 3d java
- draco mesh compression
- java sphere mesh
- 3d model optimization
lastmod: 2026-09-08
linktitle: كيفية تقليل حجم نموذج ثلاثي الأبعاد – إنشاء شبكة كرة في Java باستخدام Google
  Draco
og_description: كيفية تقليل حجم نموذج ثلاثي الأبعاد عن طريق إنشاء شبكة كرة في Java
  وضغطها باستخدام Google Draco عبر Aspose.3D. احصل على ملف .drc أصغر بنسبة تصل إلى
  95٪ في دقائق.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: كيفية تقليل حجم نموذج ثلاثي الأبعاد باستخدام شبكة كرة Java وDraco
schemas:
- author: Aspose
  dateModified: '2026-09-08'
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
title: كيفية تقليل حجم نموذج ثلاثي الأبعاد باستخدام شبكة كرة Java وDraco
url: /ar/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تقليل حجم نموذج ثلاثي الأبعاد باستخدام شبكة كرة جافا و Draco

## مقدمة

إذا كنت تبحث عن طريقة سريعة **لتقليل حجم نموذج ثلاثي الأبعاد** مع الاستمرار في تقديم هندسة عالية الجودة، فقد وصلت إلى المكان الصحيح. في هذا الدرس سنستعرض إنشاء شبكة كرة باستخدام **Aspose.3D for Java** ثم ضغط تلك الشبكة باستخدام **Google Draco**. في النهاية ستحصل على ملف `.drc` جاهز للاستخدام أصغر بشكل كبير من الأصلي، مما يجعله مثالياً للمشاهدات على الويب، ألعاب الهواتف المحمولة، أو أي تطبيق جافا يواجه قيوداً في عرض النطاق الترددي.

## إجابات سريعة

- **ما الذي يغطيه هذا الدرس؟** إنشاء شبكة كرة في جافا وضغطها باستخدام Google Draco عبر Aspose.3D.  
- **المكتبة الأساسية؟** Aspose.3D for Java (يُستخدم لإنشاء الشبكة وتصدير Draco).  
- **الوقت النموذجي للتنفيذ؟** حوالي 10‑15 دقيقة لإنشاء كرة أساسية.  
- **المتطلب الأساسي؟** بيئة تطوير جافا مع ملفات JAR الخاصة بـ Aspose.3D على مسار الفئات.  
- **النتيجة؟** ملف `.drc` **يقلل حجم نموذج ثلاثي الأبعاد** بنسبة تصل إلى 95 % مقارنةً بشبكة غير مضغوطة.

## كيف تقلل حجم نموذج ثلاثي الأبعاد؟

تولد فئة `Sphere` هندسة كرة مُثلثية استناداً إلى نصف القطر ومعلمات التشابك المحددة. قم بتحميل كرتك باستخدام `new Sphere(1.0, 32, 32)` وصدرها مباشرة إلى Draco باستخدام `scene.save("sphere.drc", SaveFormat.Draco)`. طريقة `scene.save` تكتب المشهد الحالي إلى ملف بالتنسيق المحدد. تتعامل Aspose.3D مع التحويل داخلياً، لذا تتجنب خطوات الترميز اليدوي. يقوم مُصدّر Draco تلقائياً بتطبيق تقليل دقة الهندسة وإزالة التكرار في الرؤوس، مما ينتج ملفات أصغر بنسبة غالباً 80‑95 % مع الحفاظ على الدقة البصرية.

## ما هو “تقليل حجم نموذج ثلاثي الأبعاد” في سياق تطوير ثلاثي الأبعاد؟

**تقليل حجم نموذج ثلاثي الأبعاد** يعني تقليل كمية بيانات الهندسة التي تحتاج إلى النقل أو التخزين، دون تدهور ملحوظ في جودة الصورة. يحقق Draco ذلك عن طريق ترميز مواضع الرؤوس، والاتجاهات، والسمات الأخرى في تنسيق ثنائي مضغوط للغاية. عند الجمع مع Aspose.3D، يبقى سير العمل بالكامل داخل جافا، لذا لا تحتاج إلى التعامل مع الثنائيات الأصلية.

## لماذا نستخدم ضغط شبكة Google Draco مع Aspose.3D؟

يوفر Google Draco مع Aspose.3D خط أنابيب فعال يقلص ملفات الشبكة بشكل كبير مع الحفاظ على سهولة دمجها في مشاريع جافا. تتعامل المكتبة مع جميع عمليات الترميز منخفضة المستوى، لذا يمكن للمطورين التركيز على إنشاء الهندسة دون التعامل مع الثنائيات الأصلية لـ Draco، مما ينتج تطويراً أسرع وأصولاً أصغر للويب والهواتف المحمولة.

- **تقليل حجم هائل:** يمكن لـ Draco تقليل بيانات الشبكة بنسبة تصل إلى 95 % للنماذج النموذجية، مما يحول ملف OBJ بحجم 5 MB إلى `.drc` بحجم 0.3 MB.  
- **فك تشفير سريع أثناء التشغيل:** المحركات مثل Unity و Unreal و three.js تقوم بفك تشفير Draco أصلاً، مما يؤدي إلى أوقات تحميل أسرع.  
- **تكامل سلس مع جافا:** Aspose.3D ي抽象 مكتبة Draco الأصلية، مما يسمح لك بالبقاء في بيئة جافا.  
- **تصدير Aspose 3D شامل:** نفس الـ API الذي تستخدمه لإنشاء الهندسة يتعامل أيضاً مع التصدير، مما يبسط خط الأنابيب.

## المتطلبات المسبقة

- **Java Development Kit (JDK)** – الإصدار 8 أو أحدث.  
- **Aspose.3D for Java** – قم بتنزيل أحدث ملفات JAR من **[صفحة إصدارات Aspose 3D Java](https://releases.aspose.com/3d/java/)**.  
- **Basic familiarity with Google Draco** – ستستخدم غلاف Aspose.3D، لذا لا يلزم إعداد Draco الأصلي.

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

أنشئ مشروع جافا جديد (أي بيئة تطوير متكاملة تعمل) وأضف جميع ملفات JAR الخاصة بـ Aspose.3D إلى مسار الفئات. احتفظ بملفات المصدر في حزمة مثل `com.example.draco` للوضوح.

### الخطوة 2: كيفية إنشاء شبكة كرة في جافا

فئة `Sphere` هي مولّد الهندسة المدمج في Aspose.3D الذي ينتج شبكة مثلثية مع نصف قطر وإعداد تشابك قابلين للتكوين.  

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

> **نصيحة احترافية:** فئة `Sphere` تولد شبكة مثلثية بنصف قطر افتراضي 1.0. يمكنك تمرير نصف قطر مخصص، أو إعداد تشابك، أو معلمات مادة إذا كنت بحاجة إلى مستوى تفاصيل مختلف قبل الضغط.

### الخطوة 3: تصدير الشبكة إلى تنسيق Draco

بعد إضافة الكرة إلى كائن `Scene`، استدعِ `scene.save("sphere.drc", SaveFormat.Draco)`. تقوم Aspose.3D تلقائياً باختيار إعدادات الضغط المثلى، ولكن يمكنك ضبطها بدقة عن طريق تعديل `DracoCompressionOptions` إذا كنت بحاجة إلى أصغر ملف ممكن. يتيح لك `DracoCompressionOptions` تخصيص إعدادات ضغط Draco مثل التكميم ومستوى الضغط.

### الخطوة 4: التحقق من النتيجة

افتح ملف `.drc` المُولد باستخدام عارض Draco (مثلاً `DRACOLoader` في three.js) للتأكد من أن الهندسة تُعرض بشكل صحيح. ستلاحظ تقليلاً كبيراً في حجم الملف—غالباً ما يكون بمقدار عشرة أضعاف أو أكثر.

## حالات الاستخدام الشائعة

| السيناريو | لماذا تقليل حجم النموذج؟ | كيف يساعد هذا الدرس |
|----------|-----------------------|--------------------------|
| مُكوّنات المنتجات على الويب | تحميل صفحات أسرع على اتصالات بطيئة | ملفات `.drc` المضغوطة بـ Draco تُحمَّل في ثوانٍ |
| تطبيقات AR/VR على الهواتف المحمولة | استهلاك ذاكرة أقل على الأجهزة | الشبكات الأصغر تحافظ على استجابة التطبيق |
| المشاهد المُعالجة سحابياً | تقليل تكاليف عرض النطاق الترددي | تصدير بنقرة واحدة من Aspose.3D إلى Draco |

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | ملفات JAR الخاصة بـ Aspose.3D غير موجودة في مسار الفئات | تحقق من أن *جميع* ملفات JAR الخاصة بـ Aspose.3D مضمنة وأن الإصدار يتطابق مع الوثائق. |
| **Output file is empty** | `MyDir` يشير إلى مجلد غير موجود | أنشئ المجلد برمجياً (`Files.createDirectories(Paths.get(MyDir))`) قبل كتابة الملف. |
| **Compressed mesh looks distorted** | استخدام مستوى ضغط منخفض أو تشابك غير كافٍ | قم بالتحويل إلى `DracoCompressionLevel.OPTIMAL` وزد تشابك الكرة (مثلاً `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` يختار أعلى جودة ضغط لإخراج Draco. |

## الأسئلة المتكررة

**Q: هل Aspose.3D متوافق مع صيغ ملفات ثلاثية الأبعاد المختلفة؟**  
A: نعم، يدعم Aspose.3D صيغ OBJ و FBX و STL و GLTF والعديد غيرها، مما يجعله خياراً مرناً لأنابيب **Aspose 3d export**.

**Q: هل يمكنني استخدام Google Draco للضغط في لغات برمجة أخرى؟**  
A: بالتأكيد. يوفر Draco مكتبات أصلية لـ C++ و Python و JavaScript. يركز هذا الدرس على جافا، لكن المفاهيم تنطبق على جميع اللغات.

**Q: أين يمكنني العثور على وثائق Aspose.3D إضافية؟**  
A: زر **[توثيق Aspose.3D Java](https://reference.aspose.com/3d/java/)** للحصول على مراجع API كاملة ومزيد من الأمثلة.

**Q: كيف أحصل على ترخيص مؤقت لـ Aspose.3D؟**  
A: استكشف خيارات الترخيص المؤقت على **[صفحة الترخيص المؤقت لـ Aspose](https://purchase.aspose.com/temporary-license/)**.

**Q: هل هناك منتدى مجتمع لدعم Aspose.3D؟**  
A: نعم، انضم إلى النقاش في **[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18)**.

## الخلاصة

في هذا الدليل أظهرنا كيفية **تقليل حجم نموذج ثلاثي الأبعاد** عن طريق إنشاء شبكة كرة في جافا ثم ضغطها باستخدام Google Draco عبر Aspose.3D. باتباع هذه الخطوات المختصرة يمكنك تقليل ملفات الشبكة بشكل كبير، تحسين أوقات التحميل، والحفاظ على تطبيقاتك ثلاثية الأبعاد القائمة على جافا سريعة الاستجابة وصديقة للعرض الترددي.

---

**آخر تحديث:** 2026-09-08  
**تم الاختبار مع:** Aspose.3D for Java 24.12 (latest)  
**المؤلف:** Aspose

## الدروس ذات الصلة

- [تقليل حجم ملف 3D – ضغط المشاهد باستخدام Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [إنشاء سحابة نقاط Draco من كرات باستخدام Aspose.3D for Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [تعلم كيفية مثلثية الشبكات لتحسين العرض في جافا باستخدام Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}