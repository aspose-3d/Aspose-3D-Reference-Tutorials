---
date: 2026-05-24
description: تعلم كيفية استخراج الشكل باستخدام Aspose.3D for Java. يغطي هذا الدرس
  في نمذجة 3D باستخدام Java تقنية Linear Extrusion، والتحكم بالمركز (center control)،
  والاتجاه (direction)، والشرائح (slices)، والالتواء (twist) والمزيد!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: إنشاء نماذج ثلاثية الأبعاد باستخدام Linear Extrusion في Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: كيفية استخراج الشكل - إنشاء نماذج ثلاثية الأبعاد باستخدام Linear Extrusion
  في Java
url: /ar/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية استخراج الشكل – إنشاء نماذج ثلاثية الأبعاد باستخدام البثق الخطي في جافا

إذا كنت تتساءل **كيفية استخراج الشكل** في تطبيق جافا، فأنت في المكان الصحيح. في هذا الدرس سنستعرض ميزات البثق الخطي في Aspose.3D لجافا، موضحين لك كيفية تحويل ملفات تعريف 2‑D بسيطة إلى نماذج 3‑D متكاملة. سواء كنت تبني عارضًا بأسلوب CAD، أو خط أنابيب أصول ألعاب، أو مجرد تجربة مع الهندسة، سيمكنك إتقان البثق الخطي من إنشاء أشكال معقدة ببضع أسطر من الشيفرة فقط.

## إجابات سريعة
- **ما هو البثق الخطي؟** تحويل رسم تخطيطي 2‑D إلى صلب 3‑D بتمديده على طول اتجاه.  
- **أي مكتبة تساعدك؟** Aspose.3D لجافا توفر API سهل الاستخدام لمهام البثق.  
- **هل أحتاج إلى ترخيص؟** نسخة تجريبية مجانية كافية للتعلم؛ الترخيص التجاري مطلوب للإنتاج.  
- **ما نسخة جافا المطلوبة؟** جافا 8 أو أعلى.  
- **هل يمكنني تطبيق الالتواء أو الإزاحة؟** نعم – يدعم API زاوية الالتواء وإزاحة الالتواء مباشرةً.  

## ما هو “كيفية استخراج الشكل” في جافا؟
عملية `Extrusion` هي الميزة الأساسية في Aspose.3D التي تحول الحد المسطح إلى شبكة حجمية. ببساطة، تزود المكتبة بملف تعريف 2‑D (مثل مستطيل أو مضلع مخصص)، تحدد المسافة التي تريد سحبه بها، وتقوم المكتبة بإنشاء الهندسة ثلاثية الأبعاد لك.

## لماذا تستخدم Aspose.3D لجافا؟
Aspose.3D يدعم **أكثر من 50 تنسيقًا** للإدخال والإخراج – بما في ذلك OBJ و STL و FBX و GLTF – ويمكنه توليد شبكات تصل إلى **10 000 قمة لكل بثق** دون الحاجة إلى تحميل المشهد بالكامل في الذاكرة. محركه متعدد المنصات يعمل على Windows و Linux و macOS، ويقدم نتائج متسقة سواء كنت على محطة عمل سطح مكتب أو خادم CI بدون واجهة.

## المتطلبات المسبقة
- جافا 8 أو أحدث مثبتة على جهاز التطوير.  
- Maven أو Gradle لإدارة التبعيات.  
- ملف ترخيص Aspose.3D لجافا (اختياري للتجربة).  

## كيف يعمل البثق الخطي؟
يقوم البثق الخطي بإنشاء صلب ثلاثي الأبعاد عن طريق مسح ملف تعريف 2‑D على طول خط مستقيم. أولاً، يقوم المحرك بتثليث الملف التعريفي، ثم يكرره عند كل شريحة على محور البثق، وأخيرًا يربط الشرائح معًا لتكوين شبكة محكمة. هذه العملية تحسب تلقائيًا المتجهات العادية وإحداثيات UV، بحيث يمكنك عرض النتيجة دون معالجة هندسية إضافية.

## ما هي المعلمات الرئيسية للبثق الخطي؟
يمكن تخصيص البثق الخطي بعدة معلمات. **المركز** يحدد نقطة الارتكاز للملف التعريفي قبل البثق. **الاتجاه** يحدد محور البثق، ويكون افتراضيًا على محور Z الموجب. **الشرائح** تتحكم في عدد المقاطع العرضية المتوسطة، مما يؤثر على السلاسة للأشكال الملتوية أو المخروطية. **زاوية الالتواء** تدور الملف التعريفي تدريجيًا من البداية إلى النهاية، بينما **إزاحة الالتواء** تضيف إزاحة خطية على المحور، مما يتيح أشكالًا حلزونية.

- **المركز** – نقطة الارتكاز التي يتم حولها وضع الملف التعريفي قبل البثق.  
- **الاتجاه** – متجه يحدد محور البثق؛ الافتراضي هو محور Z الموجب.  
- **الشرائح** – عدد المقاطع العرضية المتوسطة؛ كلما زاد عدد الشرائح زادت السلاسة للبتقات الملتوية أو المخروطية.  
- **زاوية الالتواء** – مقدار الدوران الكلي المطبق على الملف التعريفي من البداية إلى النهاية، بالدرجات.  
- **إزاحة الالتواء** – إزاحة خطية تحرك الملف التعريفي على طول محور البثق أثناء الالتواء، مما يتيح أشكالًا حلزونية.

## تنفيذ البثق الخطي في Aspose.3D لجافا

حمّل ملفك التعريفي، اضبط المعلمات، ودع الـ API يولد الشبكة. الخطوات التالية توضح سير العمل النموذجي.

### الخطوة 1: تعريف الملف الشخصي ثنائي الأبعاد
أنشئ `Polygon` أو `Polyline` يمثل الشكل الذي تريد بُثقَه.  
*`Polygon` يمثل شكلًا مغلقًا يُعرّف بالرؤوس، بينما `Polyline` هو سلسلة مفتوحة من المقاطع الخطية.*  
هل أنت مستعد للبدء؟ [قم بتنفيذ البثق الخطي الآن](./performing-linear-extrusion/)  
للحصول على درس تفصيلي، راجع [تنفيذ البثق الخطي في Aspose.3D لجافا](./performing-linear-extrusion/).

### الخطوة 2: تكوين خيارات البثق
حدد المركز، الاتجاه، الشرائح، الالتواء، وإزاحة الالتواء على كائن `Extrusion`.  
*فئة `Extrusion` تحزم جميع المعلمات اللازمة لتوليد شبكة 3‑D من ملف تعريف 2‑D.*  
جرب التحكم بالمركز عمليًا: [التحكم بالمركز في البثق الخطي](./controlling-center/)  
اقرأ المزيد عن التحكم بالمركز: [التحكم بالمركز في البثق الخطي باستخدام Aspose.3D لجافا](./controlling-center/)

### الخطوة 3: إضافة البثق إلى المشهد
أنشئ كائن `Scene`، أرفق شبكة البثق، وصدرها إلى التنسيق المطلوب.  
*`Scene` هو الحاوية التي تحتفظ بجميع الكائنات ثلاثية الأبعاد وتتعامل مع تصديرها إلى صيغ ملفات مختلفة.*  
هل أنت مستعد لتحديد الاتجاه؟ [استكشف الآن](./setting-direction/)  
تعرف على المزيد حول الاتجاه: [تحديد الاتجاه في البثق الخطي باستخدام Aspose.3D لجافا](./setting-direction/)

### الخطوة 4: تصدير أو عرض
استخدم `Scene.save()` لكتابة النموذج إلى OBJ أو STL أو أي تنسيق مدعوم.  
*`Scene.save()` يكتب المشهد بالكامل إلى الصيغة المحددة، مع تطبيق أي معالجة لاحقة ضرورية.*  
ابدأ بتحديد الشرائح: [تعرف على المزيد](./specifying-slices/)  
دليل مفصل: [تحديد الشرائح في البثق الخطي باستخدام Aspose.3D لجافا](./specifying-slices/)

## كيف تطبق الالتواء على البثق؟
قم بتطبيق الالتواء عن طريق ضبط خاصية `twistAngle` في خيارات البثق. يدور المحرك كل شريحة بنسبة متناسبة، محدثًا تأثيرًا حلزونيًا. بتعديل الزاوية يمكنك إنتاج أي شيء من الالتواء الخفيف إلى دوامات كاملة 360°، مفيد للعناصر الزخرفية أو النوابض الوظيفية.  
هل تريد إضافة الالتواء الآن؟ [طبق الالتواء الآن](./applying-twist/)  
مثال كامل: [تطبيق الالتواء في البثق الخطي باستخدام Aspose.3D لجافا](./applying-twist/)

## كيف تستخدم إزاحة الالتواء للأشكال اللولبية؟
إزاحة الالتواء تحرك كل شريحة على طول محور البثق أثناء الدوران، مكونةً سلمًا حلزونيًا أو هندسة برغي. الجمع بين زاوية الالتواء وإزاحة إيجابية ينتج منحدرًا حلزونيًا ناعمًا، بينما الإزاحة السالبة يمكن أن تخلق حلزونات هابطة. هذه التقنية مثالية لنمذجة الخيوط، النوابض، أو الشرائط الفنية.  
طور مهاراتك: [تعلم إزاحة الالتواء](./using-twist-offset/)  
دليل شامل: [استخدام إزاحة الالتواء في البثق الخطي باستخدام Aspose.3D لجافا](./using-twist-offset/)

## حالات الاستخدام الشائعة للبثق الخطي
- **الأجزاء الميكانيكية** – توليد البراغي، الأعمدة، والحوامل بسرعة من رسومات بسيطة.  
- **العناصر المعمارية** – بُثق مخططات الأرضيات إلى جدران أو أعمدة لنماذج BIM.  
- **أصول الألعاب** – إنشاء عناصر منخفضة البوليغون مثل الأسوار، الأنابيب، أو السكة الزخرفية مباشرةً من فن 2‑D.  
- **الأدوات التعليمية** – تصور الأسطح الرياضية عن طريق بُثق المنحنيات البارامترية.

## استكشاف المشكلات الشائعة
- **الوجوه المفقودة** – تأكد من أن الملف التعريفي حلقة مغلقة؛ الحدود المفتوحة تُنتج فجوات.  
- **استهلاك الذاكرة المفرط** – قلل عدد `slices` أو فعّل `scene.setMemoryOptimization(true)`.  
- **اتجاه الالتواء غير الصحيح** – الزوايا الموجبة تدور باتجاه عقارب الساعة عند النظر على طول اتجاه البثق؛ استخدم قيمًا سالبة للعكس.  

## الأسئلة المتكررة

**س: هل يمكنني استخدام Aspose.3D لجافا في مشروع تجاري؟**  
ج: نعم، يلزم وجود ترخيص Aspose صالح للاستخدام في الإنتاج، لكن نسخة تجريبية مجانية متاحة للتقييم.

**س: ما إصدارات جافا المدعومة؟**  
ج: تعمل المكتبة مع جافا 8 والإصدارات الأحدث، بما في ذلك جافا 11، 17، و21.

**س: هل أحتاج إلى إدارة الذاكرة للبتقات الكبيرة؟**  
ج: Aspose.3D يدير توليد الشبكات بكفاءة، لكن يمكنك استدعاء `scene.dispose()` عند الانتهاء من المشاهد الكبيرة لتحرير الموارد الأصلية.

**س: هل يمكنني دمج عمليات بُثق متعددة في نموذج واحد؟**  
ج: بالطبع – يمكنك إنشاء عدة كائنات بُثق، وضعها بشكل مستقل، وإضافتها إلى نفس المشهد.

**س: هل هناك مثال شفري لتطبيق الالتواء وإزاحة الالتواء معًا؟**  
ج: نعم، توضح دروس “تطبيق الالتواء” و“استخدام إزاحة الالتواء” كيفية ضبط الخاصيتين على نفس كائن البثق.

---

**آخر تحديث:** 2026-05-24  
**تم الاختبار مع:** Aspose.3D لجافا 24.11  
**المؤلف:** Aspose  

{{< blocks/products/products-backtop-button >}}

## دروس ذات صلة

- [دروس جافا 3D – التحكم بالمركز في البثق الخطي](/3d/java/linear-extrusion/controlling-center/)
- [كيفية ضبط الاتجاه في البثق الخطي باستخدام Aspose.3D لجافا](/3d/java/linear-extrusion/setting-direction/)
- [إنشاء بُثق ثلاثي الأبعاد مع الشرائح – Aspose.3D لجافا](/3d/java/linear-extrusion/specifying-slices/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}