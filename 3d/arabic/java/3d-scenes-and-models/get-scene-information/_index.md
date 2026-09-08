---
date: 2026-09-08
description: تعلم كيفية تعريف units وتصدير scene إلى FBX في Java باستخدام Aspose.3D.
  يوضح هذا الدليل خطوة بخطوة ضبط application name، measurement units، واسترجاع 3D
  scene information.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: كيفية حفظ FBX واسترجاع 3D Scene Info في Java
og_description: تعلم كيفية تعريف units وتصدير scene إلى FBX في Java مع Aspose.3D.
  يغطي الدليل ضبط application name، measurement units، واسترجاع 3D scene info في بضع
  خطوات.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: كيفية تعريف units وتصدير scene إلى FBX في Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: كيفية تعريف units وتصدير scene إلى FBX في Java
url: /ar/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تعريف الوحدات وتصدير المشهد إلى FBX في Java

## مقدمة

إذا كنت تبحث عن دليل واضح وعملي حول **كيفية تعريف الوحدات** و**تصدير مشهد إلى FBX** مع استخراج بيانات تعريفية مفيدة من مشاهدك ثلاثية الأبعاد، فقد وجدت المكان المناسب. في هذا البرنامج التعليمي سنستعرض كل خطوة باستخدام مكتبة **Aspose.3D for Java**: من إنشاء المشهد، **تعيين اسم التطبيق**، **تعريف وحدات القياس**، وحتى **تصدير المشهد إلى FBX**. في النهاية ستحصل على ملف FBX جاهز للاستخدام يحمل معلومات الأصول التي تحتاجها لسلاسل المعالجة اللاحقة.

## إجابات سريعة
- **ما هو الهدف الأساسي؟** تصدير مشهد إلى FBX يحتوي على معلومات أصول مخصصة.  
- **ما المكتبة المستخدمة؟** Aspose.3D for Java.  
- **هل أحتاج إلى ترخيص؟** نسخة تجريبية مجانية تكفي للتطوير؛ الترخيص التجاري مطلوب للإنتاج.  
- **هل يمكنني تغيير وحدات القياس؟** نعم – استخدم `setUnitName` و `setUnitScaleFactor`.  
- **أين يتم حفظ الناتج؟** إلى المسار الذي تحدده في `scene.save(...)`.  

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من أن لديك:

- فهم قوي لأساسيات لغة Java.  
- **Aspose.3D for Java** تم تنزيله وإضافته إلى مشروعك (يمكنك الحصول عليه من الصفحة الرسمية) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- بيئة التطوير المتكاملة المفضلة لديك للـ Java (IntelliJ IDEA، Eclipse، NetBeans، إلخ) مُكوَّنة بشكل صحيح.

## استيراد الحزم

في ملف مصدر Java الخاص بك، استورد فئات Aspose.3D التي توفر معالجة المشاهد ودعم صيغ الملفات.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **نصيحة احترافية:** حافظ على قائمة الاستيراد بأقل قدر لتجنب الاعتمادات غير الضرورية وتحسين أوقات التجميع.

## ما هي عملية حفظ ملف FBX؟

لحفظ مشهد كملف FBX، تقوم بإنشاء كائن `Scene`، وتعيين أي بيانات تعريفية للأصول المطلوبة، وتعريف وحدة القياس، ثم تستدعي `scene.save(path, FileFormat.FBX7500ASCII)`. هذه السلسلة تكتب الهندسة والمواد والبيانات التعريفية إلى ملف FBX بصيغة ASCII يمكن فحصه أو استيراده بواسطة الأدوات اللاحقة.

### الخطوة 1: تهيئة مشهد ثلاثي الأبعاد

فئة `Scene` هي الحاوية العليا في Aspose.3D التي تمثل مشهدًا ثلاثيًا كاملاً، بما في ذلك الهندسة، والإضاءة، والكاميرات، والبيانات التعريفية. أولاً، أنشئ كائن `Scene` فارغ. سيكون هذا الحاوية لجميع الهندسة والإضاءة والكاميرات وبيانات تعريف الأصول.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### كيفية تعيين اسم التطبيق في Java

كائن `AssetInfo` يخزن البيانات التعريفية مثل اسم التطبيق، والبائع، والإصدار للمشهد. إضافة بيانات تعريف مخصصة تساعد الأدوات اللاحقة على تحديد مصدر الملف. استخدم كائن `AssetInfo` **لتعيين اسم التطبيق** (والبائع) قبل حفظ الملف.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **لماذا هذا مهم:** العديد من سلاسل المعالجة تقوم بفلترة أو وضع علامات على الأصول بناءً على التطبيق الأصلي، مما يجعل هذه الخطوة أساسية للمشاريع الكبيرة.

### الخطوة 3: تعريف وحدات القياس

نظام الوحدات يحدد مقياس العالم الحقيقي للمشهد؛ تسمح لك Aspose.3D بتحديد اسم الوحدة وعامل مقياس بالنسبة إلى الأمتار. في هذا المثال نستخدم وحدة مصرية قديمة تسمى “pole” مع عامل مقياس مخصص.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **نصيحة:** اضبط `unitScaleFactor` لتتناسب مع الحجم الحقيقي لنماذجك؛ 1.0 تمثل تطابق 1‑إلى‑1 مع الوحدة المختارة.

### الخطوة 4: تصدير المشهد إلى FBX

الآن بعد إرفاق معلومات الأصول، نقوم بحفظ المشهد كملف FBX. خيار `FileFormat.FBX7500ASCII` ينتج ملف FBX بصيغة ASCII قابلة للقراءة من قبل الإنسان، وهو مفيد للتصحيح.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **تذكر:** استبدل `"Your Document Directory"` بمسار مطلق أو مسار نسبي إلى دليل عمل مشروعك.

## لماذا تصدير المشهد إلى FBX باستخدام Aspose.3D؟

تدعم Aspose.3D **أكثر من 50 صيغة إدخال وإخراج** ويمكنها معالجة مشاهد مئات الصفحات دون تحميل الملف بالكامل إلى الذاكرة، مما يمنحك سيطرة كاملة على الملف المُصدَّر — البيانات التعريفية، الوحدات، والهندسة — دون الحاجة إلى تطبيق تأليف ثلاثي الأبعاد ثقيل. هذا يجعل توليد الأصول تلقائيًا، والمعالجة الدفعية، والتحويلات على الخادم سريعة وموثوقة.

## حالات الاستخدام الشائعة

- **خطوط أنابيب أصول الألعاب** – تضمين معلومات المنشئ مباشرة في ملفات FBX لتتبع الإصدارات.  
- **التصوير المعماري** – تخزين وحدات خاصة بالمشروع لتجنب أخطاء التحجيم عند الاستيراد إلى محركات العرض.  
- **التقارير الآلية** – إنشاء ملفات FBX في الوقت الفعلي مع بيانات تعريفية يمكن للأدوات التحليلية اللاحقة قراءتها.  
- **خدمات 3D السحابية** – إنشاء وتصدير المشاهد برمجيًا دون واجهة مستخدم، مثالي لمنصات SaaS.

## استكشاف الأخطاء وإصلاحها والنصائح

| المشكلة | الحل |
|-------|----------|
| **File not found after save** | تحقق من أن `MyDir` يشير إلى مجلد موجود وأن تطبيقك يملك أذونات الكتابة. |
| **Units appear incorrect in external viewer** | تحقق مرة أخرى من `unitScaleFactor`؛ بعض العارضات تتوقع الأمتار كوحدة أساسية. |
| **Asset metadata missing** | تأكد من استدعاء `scene.getAssetInfo()` **قبل** الحفظ؛ التغييرات التي تتم بعد `save()` لن تُحفظ. |
| **Performance bottleneck on large scenes** | استخدم `scene.optimize()` قبل الحفظ لتقليل استهلاك الذاكرة. |
| **ASCII FBX is too large** | التحول إلى FBX ثنائي باستخدام `FileFormat.FBX7500` (انظر الأسئلة المتكررة). |

## الأسئلة المتكررة

**س: كيف أغير صيغة الإخراج إلى FBX ثنائي؟**  
ج: استبدل `FileFormat.FBX7500ASCII` بـ `FileFormat.FBX7500` عند استدعاء `scene.save(...)`.

**س: هل يمكنني إضافة بيانات تعريف مخصصة من قبل المستخدم تتجاوز حقول الأصول المدمجة؟**  
ج: نعم، استخدم `scene.getUserData().add("Key", "Value")` لتضمين أزواج مفتاح‑قيمة إضافية.

**س: هل تدعم Aspose.3D صيغ تصدير أخرى مثل OBJ أو GLTF؟**  
ج: نعم. فقط غيّر قيمة تعداد `FileFormat` إلى `OBJ` أو `GLTF2` حسب الحاجة.

**س: ما نسخة Java المطلوبة؟**  
ج: تدعم Aspose.3D for Java Java 8 وما بعدها.

**س: هل يمكن تحميل ملف FBX موجود، تعديل معلومات الأصول الخاصة به، ثم إعادة حفظه؟**  
ج: بالتأكيد. حمّل الملف باستخدام `new Scene("input.fbx")`، عدّل `scene.getAssetInfo()`، ثم احفظ.

---
**آخر تحديث:** 2026-09-08  
**تم الاختبار مع:** Aspose.3D for Java 24.11  
**المؤلف:** Aspose

## دروس ذات صلة

- [تقليل حجم ملفات 3D – ضغط المشاهد باستخدام Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [كيفية تعيين لون vector3 في Java: تغيير اللون المنتشر وإدارة خصائص 3D في مشاهد Java باستخدام Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}