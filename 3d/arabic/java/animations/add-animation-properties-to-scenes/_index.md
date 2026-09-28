---
date: 2026-09-28
description: تعلم كيفية تحريك المشاهد ثلاثية الأبعاد في Java باستخدام Aspose.3D، إضافة
  خصائص التحريك، إنشاء keyframes، وتصدير ملفات FBX المتحركة باستخدام تقنيات linear
  interpolation ثلاثية الأبعاد.
keywords:
- how to animate 3d
- linear interpolation 3d
- export animated fbx
- create keyframe animation
- add animation properties
lastmod: 2026-09-28
linktitle: كيفية تحريك المشاهد ثلاثية الأبعاد في Java باستخدام Aspose.3D
og_description: تعلم كيفية تحريك المشاهد ثلاثية الأبعاد في Java باستخدام Aspose.3D.
  يوضح هذا الدليل خطوة بخطوة إضافة خصائص التحريك، إنشاء keyframes، وتصدير ملفات FBX
  المتحركة.
og_image_alt: Developer guide showing how to animate 3D scenes in Java with Aspose.3D
og_title: كيفية تحريك المشاهد ثلاثية الأبعاد في Java – دليل Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-09-28'
  description: Learn how to animate 3D scenes in Java using Aspose.3D, add animation
    properties, create keyframes, and export animated FBX files with linear interpolation
    3d techniques.
  headline: How to animate 3D scenes in Java with Aspose.3D
  type: TechArticle
- questions:
  - answer: Yes. Purchase a commercial license on the [Aspose purchase page](https://purchase.aspose.com/buy).
    question: Can I use Aspose.3D for commercial projects?
  - answer: Absolutely. Download a trial from the [Aspose releases page](https://releases.aspose.com/).
    question: Is a free trial available?
  - answer: Join the community at the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18)
      for help from staff and other developers.
    question: Where can I get support?
  - answer: Request a [temporary license](https://purchase.aspose.com/temporary-license/)
      to remove runtime restrictions during testing.
    question: How do I obtain a temporary evaluation license?
  - answer: Yes—explore the full [Aspose.3D documentation](https://reference.aspose.com/3d/java/)
      for advanced scenarios such as skeletal animation, morph targets, and custom
      shaders.
    question: Are there more tutorials?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- animate 3d java
- Aspose.3D
- linear interpolation
- FBX export
- Java animation tutorial
title: كيفية تحريك المشاهد ثلاثية الأبعاد في Java باستخدام Aspose.3D
url: /ar/java/animations/add-animation-properties-to-scenes/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تحريك المشاهد ثلاثية الأبعاد في Java باستخدام Aspose.3D

## المقدمة

في هذا الدرس ستتعلم **كيفية تحريك كائنات ثلاثية الأبعاد** في تطبيق Java باستخدام Aspose.3D. سنبدأ بإنشاء مشهد، بناء شبكة بسيطة، ربط خصائص التحريك، تعريف الإطارات الرئيسية مع الاستيفاء الخطي، وأخيرًا تصدير النتيجة كملف FBX متحرك. في النهاية ستحصل على ملف FBX جاهز للاستخدام يعمل في Unity أو Blender أو أي عارض ثلاثي الأبعاد حديث.

## إجابات سريعة
- **ما المكتبة التي تدعم التحريك؟** Aspose.3D for Java، محرك ثلاثي الأبعاد مكتوب بالكامل بلغة Java.  
- **هل يمكنني تصدير النتيجة كملف FBX؟** نعم – العينة تحفظ ملف `FBX7500ASCII` يحتفظ بجميع الإطارات الرئيسية.  
- **هل أحتاج إلى ترخيص مدفوع لتجربة هذا؟** نسخة تجريبية مجانية تكفي للتطوير؛ الترخيص التجاري مطلوب للاستخدام في الإنتاج.  
- **ما نسخة Java المطلوبة؟** Java 8 أو أحدث.  
- **هل الاستيفاء خطي أم منحني؟** كلاهما مدعومان؛ يمكنك اختيار `Interpolation.LINEAR` للحركة الخطية أو `Interpolation.BEZIER` للمنحنيات السلسة.

## ما هو الاستيفاء الخطي ثلاثي الأبعاد؟

الاستيفاء الخطي ثلاثي الأبعاد هو حساب القيم المتوسطة للتحويل بين إطاري مفتاح باستخدام صيغة خطية. في Aspose.3D تختار `Interpolation.LINEAR` عند إضافة إطار مفتاح، وتقوم المحرك تلقائيًا بإنشاء حركة ثابتة السرعة بين الإطارات.

## لماذا نضيف خصائص التحريك إلى المشهد؟

إضافة خصائص التحريك تحول الهندسة الثابتة إلى محتوى ديناميكي يمكن إعادة استخدامه في الألعاب أو المحاكاة أو تصورات المنتجات. باستخدام Aspose.3D يمكنك تحريك العديد من العقد بشكل مستقل، تصدير ملفات FBX متحركة بالكامل، والحفاظ على سير العمل بالكامل بلغة Java دون الحاجة إلى مكتبات DLL أصلية.

## لماذا نستخدم Aspose.3D للتحريك؟

Aspose.3D يدعم **أكثر من 12** صيغة تصدير — بما في ذلك FBX و OBJ و 3MF و STL و GLTF — بحيث يمكنك استهداف أي خط أنابيب. المكتبة تعمل على JVM فقط، مما يلغي الاعتماد على مكونات أصلية. كما توفر ثلاث أوضاع استيفاء (BEZIER، LINEAR، STEP) وواجهة برمجة تطبيقات كاملة لمخطط المشهد تسمح لك بالتعامل مع العقد، الشبكات، المواد، والتحريكات من خلال نموذج كائن موحد.

## المتطلبات المسبقة

- معرفة أساسية ببرمجة Java.  
- تثبيت Aspose.3D for Java – حمّله من [صفحة الإصدارات](https://releases.aspose.com/3d/java/).  
- إعداد Maven أو Gradle لتجميع مشروع العينة.  

## استيراد الحزم

في ملف مصدر Java الخاص بك، استورد مساحات الأسماء الأساسية لـ Aspose.3D والفئة المساعدة `Common` التي تبني شبكة مكعب بسيطة. توفر فئة `Common` طرقًا ثابتة لإنشاء هندسة أساسية مثل مكعب وحدة.

```java
import com.aspose.threed.*;
```

الآن بعد أن أصبحت مساحات الأسماء جاهزة، لنبدأ بناء المشهد.

## الخطوة 1: تهيئة المشهد

الفئة `Scene` هي الحاوية العليا في Aspose.3D التي تحتفظ بجميع العقد، الشبكات، الأضواء، وبيانات التحريك.

```java
// Initialize scene object
Scene scene = new Scene();
```

## الخطوة 2: إنشاء شبكة باستخدام مُنشئ المضلع

الفئة `Mesh` تمثل مجموعة من الرؤوس، الوجوه، والاتجاهات التي تُعرّف كائنًا ثلاثي الأبعاد. في هذه الخطوة يبني المساعد شبكة مكعب أساسية سنقوم بتحريكها لاحقًا.

```java
Mesh mesh = new Mesh();
```

## الخطوة 3: إنشاء عقدة مكعب مع إزاحة

العقدة `Node` هي عنصر في مخطط المشهد يمكنه احتواء شبكة وخصائص تحويلها (الإزاحة، الدوران، المقياس). هنا نرفق شبكة المكعب إلى عقدة جديدة ونضعها في الأصل.

```java
// Each cube node has its own translation
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

## الخطوة 4: العثور على خاصية الإزاحة

نقطة **الربط** (bind point) تربط خاصية معينة — مثل الإزاحة — بمنحنى التحريك. من خلال تحديد نقطة ربط الإزاحة يمكنك تمكين المحرك من تعديل موضع العقدة مع مرور الوقت.

```java
// Find translation property on node's transform object
Property translation = cube1.getTransform().findProperty("Translation");
```

## الخطوة 5: إنشاء منحنى تحريك للمحور X

منحنى التحريك يخزن سلسلة من الإطارات الرئيسية لمكوّن واحد (X أو Y أو Z). المنحنى أدناه يعرّف ثلاثة إطارات رئيسية عند 0 ث، 3 ث، و5 ث. الأولان يستخدمان BEZIER لتسهيل السلاسة، بينما يستخدم الإطار الأخير LINEAR لعرض الاستيفاء الخطي ثلاثي الأبعاد.

```java
// Create an animation node for the scene
AnimationNode animNode = new AnimationNode("TranslationAnimation");

// Create a bind point for the translation property on the cube's transform
BindPoint bp = animNode.createBindPoint(cube1.getTransform(), "Translation");

// Create the animation curve on the X component of the translation
KeyframeSequence kfsX = new KeyframeSequence();

// Add keyframes for X component
kfsX.add(0, 10.0f, Interpolation.BEZIER);
kfsX.add(3, 20.0f, Interpolation.BEZIER);
kfsX.add(5, 30.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the X channel of the bind point
bp.bindKeyframeSequence("X", kfsX);
```

## الخطوة 6: تكرار للمكوّن Z

تحريك المحور Z يضيف عمقًا لحركة المكعب، مما يخلق مسارًا ثلاثيًا أكثر ديناميكية. نفس منطق نقطة الربط والمنحنى يُطبق، لكن بقيم تحرك المكعب للأمام والخلف.

```java
// Repeat the process for the Z component
KeyframeSequence kfsZ = new KeyframeSequence();
kfsZ.add(0, 10.0f, Interpolation.BEZIER);
kfsZ.add(3, -10.0f, Interpolation.BEZIER);
kfsZ.add(5, 0.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the Z channel of the same bind point
bp.bindKeyframeSequence("Z", kfsZ);
```

## كيفية تصدير FBX متحرك

استدعاء `scene.save(...)` مع `FileFormat.FBX7500ASCII` يكتب جميع منحنيات التحريك، نقاط الربط، والإطارات الرئيسية في حاوية FBX واحدة. `FileFormat` هو تعداد يحدد صيغ الإخراج المدعومة، بما في ذلك `FBX7500ASCII`. تأكد من وجود دليل الهدف ولديك صلاحية كتابة؛ وإلا سيُطلق استثناء أثناء عملية الحفظ.

```java
// Specify the directory for saving the 3D scene
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

يمكن فتح الملف المُولد في Blender أو Unity أو Autodesk Maya أو أي عارض يدعم صيغة FBX، مما يتيح لك معاينة التحريك فورًا.

## المشكلات الشائعة والحلول

| العَرَض | السبب المحتمل | الحل |
|---------|--------------|-----|
| لا توجد حركة مرئية | تم إضافة إطارات رئيسية إلى المكوّن الخطأ (مثلاً “Y” بدلًا من “X”) | تحقق من اسم المكوّن في `bindKeyframeSequence`. |
| القفز في التحريك | خلط BEZIER و LINEAR بشكل غير صحيح | حافظ على استيفاء موحد للحصول على حركة أكثر سلاسة، أو اضبط المماس يدويًا. |
| الملف غير محفوظ | مسار الدليل غير صالح | تأكد من أن `MyDir` يشير إلى مجلد موجود قابل للكتابة وينتهي بـ `.fbx`. |

## الأسئلة المتكررة

**س: هل يمكنني استخدام Aspose.3D في مشاريع تجارية؟**  
ج: نعم. اشترِ ترخيصًا تجاريًا من [صفحة الشراء الخاصة بـ Aspose](https://purchase.aspose.com/buy).

**س: هل تتوفر نسخة تجريبية مجانية؟**  
ج: بالطبع. حمّل نسخة تجريبية من [صفحة إصدارات Aspose](https://releases.aspose.com/).

**س: أين يمكنني الحصول على الدعم؟**  
ج: انضم إلى المجتمع في [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة من الموظفين والمطورين الآخرين.

**س: كيف أحصل على ترخيص تقييم مؤقت؟**  
ج: اطلب [ترخيصًا مؤقتًا](https://purchase.aspose.com/temporary-license/) لإزالة قيود وقت التشغيل أثناء الاختبار.

**س: هل هناك المزيد من الدروس؟**  
ج: نعم — استكشف كامل [توثيق Aspose.3D](https://reference.aspose.com/3d/java/) للسيناريوهات المتقدمة مثل التحريك الهيكلي، أهداف التشوه، والظلّات المخصصة.

## الخاتمة

أنت الآن تعرف **كيفية تحريك كائنات ثلاثية الأبعاد** في Java باستخدام Aspose.3D: إنشاء مشهد، ربط خصائص الإزاحة، تعريف سلاسل الإطارات الرئيسية مع الاستيفاء الخطي، وتصدير ملف FBX متحرك. جرّب التحريك بالدوران أو المقياس أو عدة عقد لبناء تحريكات أغنى للألعاب أو المحاكاة أو تصورات المنتجات.

---

**آخر تحديث:** 2026-09-28  
**تم الاختبار مع:** Aspose.3D for Java 24.12 (الأحدث)  
**المؤلف:** Aspose

## دروس ذات صلة

- [إنشاء ملف FBX باستخدام Aspose.3D for Java – درس رسومات ثلاثية الأبعاد](/3d/java/load-and-save/create-empty-3d-document/)
- [حفظ المشاهد ثلاثية الأبعاد في Java باستخدام Aspose.3D – تحويل ملفات 3D بفعالية](/3d/java/load-and-save/save-3d-scenes/)
- [تصدير نموذج إلى FBX باستخدام الكواتيرنيونات في Java باستخدام Aspose.3D](/3d/java/geometry/transform-3d-nodes-with-quaternions/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}