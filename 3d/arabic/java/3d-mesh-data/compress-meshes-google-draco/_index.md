---
date: 2026-04-29
description: تعلم كيفية تقليل حجم نموذج ثلاثي الأبعاد عن طريق إنشاء شبكة كرة في جافا
  وضغطها باستخدام Google Draco عبر Aspose.3D – أمر أساسي لتصدير Aspose 3D.
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: كيفية إنشاء شبكة كروية في جافا – ضغط الشبكات ثلاثية الأبعاد باستخدام جوجل
  دراكو
second_title: Aspose.3D Java API
title: 'تقليل حجم النموذج ثلاثي الأبعاد: إنشاء شبكة كرة في جافا باستخدام دراكو'
url: /ar/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تقليل حجم النموذج ثلاثي الأبعاد: إنشاء شبكة كرة في Java باستخدام Draco

## مقدمة

إذا كنت تبحث عن طريقة سريعة **لتقليل حجم النموذج ثلاثي الأبعاد** مع الحفاظ على جودة الهندسة العالية، فقد وصلت إلى المكان الصحيح. في هذا الدرس سنستعرض إنشاء شبكة كرة باستخدام **Aspose.3D for Java** ثم ضغط تلك الشبكة باستخدام **Google Draco**. في النهاية ستحصل على ملف `.drc` جاهز للاستخدام أصغر بكثير من الأصل، مما يجعله مثالياً لعروض الويب، الألعاب المحمولة، أو أي تطبيق Java يواجه قيود عرض النطاق الترددي.

## إجابات سريعة
- **ما الذي يغطيه هذا الدرس؟** إنشاء شبكة كرة في Java وضغطها باستخدام Google Draco عبر Aspose.3D.  
- **المكتبة الأساسية؟** Aspose.3D for Java (تُستخدم لإنشاء الشبكة وتصدير Draco).  
- **الوقت التقريبي للتنفيذ؟** حوالي 10‑15 دقيقة لإنشاء كرة أساسية.  
- **المتطلب الأساسي؟** بيئة تطوير Java مع ملفات Aspose.3D JAR في مسار الفئة.  
- **النتيجة؟** ملف `.drc` **يقلل حجم النموذج ثلاثي الأبعاد** حتى 90 % مقارنةً بشبكة غير مضغوطة.

## ما هو “تقليل حجم النموذج ثلاثي الأبعاد” في سياق تطوير 3D؟

تقليل حجم النموذج ثلاثي الأبعاد يعني تقليل كمية بيانات الهندسة التي تحتاج إلى النقل أو التخزين، دون إحداث تدهور ملحوظ في الجودة البصرية. يحقق Draco ذلك عبر ترميز مواضع الرؤوس، والاتجاهات، والسمات الأخرى في صيغة ثنائية مضغوطة للغاية. عند الجمع مع Aspose.3D، يبقى سير العمل بالكامل داخل Java، دون الحاجة إلى التعامل مع مكتبات أصلية.

## لماذا تستخدم ضغط شبكة Google Draco مع Aspose.3D؟

- **تقليل حجم هائل:** يمكن لـ Draco خفض بيانات الشبكة حتى 90 % مقارنةً بصيغ مثل OBJ أو STL.  
- **فك تشفير سريع في وقت التشغيل:** محركات مثل Unity و Unreal و three.js تفك ضغط Draco أصلاً، مما يسرّع أوقات التحميل.  
- **تكامل سلس مع Java:** Aspose.3D يَجْهَز مكتبة Draco الأصلية، مما يتيح لك البقاء في بيئة Java.  
- **تصدير Aspose 3D موحد:** نفس الـ API الذي تستخدمه لإنشاء الهندسة يتعامل أيضاً مع التصدير، مما يبسط خط الأنابيب.

## المتطلبات المسبقة

- **Java Development Kit (JDK)** – الإصدار 8 أو أحدث.  
- **Aspose.3D for Java** – حمّل أحدث ملفات JAR من الصفحة الرسمية [هنا](https://releases.aspose.com/3d/java/).  
- **إلمام أساسي بـ Google Draco** – ستستخدم غلاف Aspose.3D، لذا لا تحتاج إلى إعداد Draco أصلي.

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

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **نصيحة احترافية:** فئة `Sphere` تُنشئ شبكة مثلثية بنصف قطر افتراضي قدره 1.0. يمكنك تمرير نصف قطر مخصص، أو عدد تقطيعات، أو معلمات مادة إذا كنت بحاجة إلى مستوى تفاصيل مختلف قبل الضغط.

### الخطوة 3: كيفية ضغط الشبكة باستخدام Google Draco

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

تحديد مستوى الضغط إلى `OPTIMAL` يمنح أكبر تقليل في الحجم مع الحفاظ على الدقة البصرية، مما يساعدك مباشرةً على **تقليل حجم النموذج ثلاثي الأبعاد**.

### الخطوة 4: حفظ الشبكة المضغوطة

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

يمكن بث الملف الناتج `SphereMeshtoDRC_Out.drc` إلى العملاء، تخزينه في CDN، أو تحميله مباشرةً بواسطة أي محرك يدعم Draco.

## حالات الاستخدام الشائعة

| السيناريو | لماذا تقليل حجم النموذج؟ | كيف يساعد هذا الدرس |
|----------|-----------------------|--------------------------|
| مُكوّنات المنتجات على الويب | تحميل صفحات أسرع على الاتصالات البطيئة | ملفات `.drc` المضغوطة بـ Draco تُحمَّل خلال ثوانٍ |
| تطبيقات AR/VR المحمولة | استهلاك ذاكرة أقل على الأجهزة | الشبكات الأصغر تحافظ على استجابة التطبيق |
| مشاهد مُعالجة سحابيًا | تقليل تكاليف النطاق العريض | تصدير بنقرة واحدة من Aspose.3D إلى Draco |

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | ملفات Aspose.3D JAR غير موجودة في مسار الفئة | تأكد من تضمين *جميع* ملفات Aspose.3D JAR وأن الإصدار يتطابق مع الوثائق. |
| **Output file is empty** | المتغير `MyDir` يشير إلى مجلد غير موجود | أنشئ الدليل برمجياً (`Files.createDirectories(Paths.get(MyDir))`) قبل كتابة الملف. |
| **Compressed mesh looks distorted** | استخدام مستوى ضغط منخفض أو تقطيعات غير كافية | انتقل إلى `DracoCompressionLevel.OPTIMAL` وزد تقطيعات الكرة (مثلاً `new Sphere(1.0, 64, 64)`). |

## الأسئلة المتكررة

**س: هل Aspose.3D متوافق مع صيغ ملفات 3D المختلفة؟**  
ج: نعم، يدعم Aspose.3D صيغ OBJ، FBX، STL، GLTF، والعديد غيرها، مما يجعله خيارًا مرنًا لسلاسل **تصدير Aspose 3D**.

**س: هل يمكنني استخدام Google Draco للضغط في لغات برمجة أخرى؟**  
ج: بالتأكيد. يوفر Draco مكتبات أصلية لـ C++، Python، و JavaScript. يركز هذا الدرس على Java، لكن المفاهيم قابلة للتطبيق عبر اللغات.

**س: أين يمكنني العثور على وثائق إضافية لـ Aspose.3D؟**  
ج: زر [وثائق Aspose.3D Java](https://reference.aspose.com/3d/java/) للحصول على مراجع API كاملة ومزيد من الأمثلة.

**س: كيف أحصل على ترخيص مؤقت لـ Aspose.3D؟**  
ج: استكشف خيارات الترخيص المؤقت [هنا](https://purchase.aspose.com/temporary-license/).

**س: هل هناك منتدى مجتمع لدعم Aspose.3D؟**  
ج: نعم، انضم إلى النقاش في [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18).

## الخاتمة

في هذا الدليل أظهرنا كيفية **تقليل حجم النموذج ثلاثي الأبعاد** بإنشاء شبكة كرة في Java ثم ضغطها باستخدام Google Draco عبر Aspose.3D. باتباع هذه الخطوات المختصرة يمكنك تقليل ملفات الشبكة بشكل كبير، تحسين أوقات التحميل، والحفاظ على استجابة تطبيقات Java ثلاثية الأبعاد وصديقة للنطاق الترددي.

---

**Last Updated:** 2026-04-29  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}