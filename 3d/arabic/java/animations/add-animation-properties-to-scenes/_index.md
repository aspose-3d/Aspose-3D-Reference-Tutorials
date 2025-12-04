---
date: 2025-12-04
description: تعلم **كيفية تحريك المشاهد ثلاثية الأبعاد** في Java باستخدام Aspose.3D.
  يوضح لك هذا الدليل خطوة بخطوة كيفية إضافة خصائص التحريك، وإنشاء الإطارات المفتاحية،
  وتصدير النتيجة.
language: ar
linktitle: How to Animate 3D Scenes in Java – Add Animation Properties with Aspose.3D
  Tutorial
second_title: Aspose.3D Java API
title: كيفية تحريك المشاهد ثلاثية الأبعاد في جافا – إضافة خصائص التحريك باستخدام دليل
  Aspose.3D
url: /java/animations/add-animation-properties-to-scenes/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تحريك المشاهد ثلاثية الأبعاد في Java – إضافة خصائص التحريك باستخدام Aspose.3D

## المقدمة

إذا كنت تبحث عن دليل واضح وتطبيقي حول **كيفية تحريك كائنات ثلاثية الأبعاد** في تطبيق Java، فقد وصلت إلى المكان المناسب. في هذا البرنامج التعليمي سنستعرض كل خطوة مطلوبة لإضافة خصائص التحريك إلى مشهد ثلاثي الأبعاد باستخدام مكتبة Aspose.3D—من إنشاء المشهد والشبكة إلى تعريف الإطارات المفتاحية وأخيرًا تصدير الملف المتحرك. في النهاية ستحصل على ملف FBX يعمل يمكنك تحميله في أي عارض ثلاثي الأبعاد حديث أو محرك ألعاب.

## إجابات سريعة
- **ما المكتبة المستخدمة؟** Aspose.3D for Java  
- **هل يمكنني التصدير إلى FBX؟** نعم، يحفظ البرنامج التعليمي المشهد كـ FBX7500ASCII.  
- **هل أحتاج إلى ترخيص للتطوير؟** نسخة تجريبية مجانية تكفي للاختبار؛ الترخيص التجاري مطلوب للإنتاج.  
- **ما نسخة Java المطلوبة؟** Java 8 أو أعلى.  
- **هل التحريك خطي أم منحني؟** كلاهما—يمكن للإطارات المفتاحية استخدام تقاطع BEZIER أو LINEAR.

## ما هو “كيفية تحريك ثلاثي الأبعاد” في Java؟

تحريك الكائنات ثلاثية الأبعاد يعني تغيير خصائص التحويل الخاصة بها (الموقع، الدوران، المقياس) مع مرور الوقت. توفر Aspose.3D واجهة برمجة تطبيقات عالية المستوى تتيح لك إنشاء **نقاط ربط**، إرفاق **سلاسل إطارات مفتاحية**، والتحكم في التقاطع، كل ذلك دون الحاجة لكتابة محرك تحريك مخصص.

## لماذا نستخدم Aspose.3D للتحريك؟

- **دعم صيغ متعددة** – تصدير إلى FBX، OBJ، 3MF، وأكثر.  
- **بدون تبعيات أصلية** – جافا صافية، مثالية لأنابيب المعالجة على الخادم.  
- **خيارات تقاطع غنية** – منحنيات BEZIER، LINEAR، وSTEP.  
- **رسم مشهد كامل** – العقد، الشبكات، المواد، والتحريك كلها متاحة عبر واجهة برمجة تطبيقات واحدة.

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من وجود ما يلي:

- معرفة أساسية ببرمجة Java.  
- تثبيت Aspose.3D for Java (حمّلها من [صفحة الإصدارات](https://releases.aspose.com/3d/java/)).  
- بيئة تطوير Java أو أداة بناء (Maven/Gradle) جاهزة لتجميع العينة.

## استيراد الحزم

في مشروع Java الخاص بك، استورد الفئات الأساسية من Aspose.3D وفئة المساعدة `Common` المستخدمة لبناء شبكة بسيطة:

```java
import com.aspose.threed.*;

import examples.geometry.Common;
```

الآن بعد أن أصبحت المساحات الاسمية جاهزة، لنبدأ بناء المشهد.

## الخطوة 1: تهيئة المشهد

```java
// Initialize scene object
Scene scene = new Scene();
```

كائن `Scene` هو الحاوية لجميع العقد، الشبكات، الأضواء، وبيانات التحريك.

## الخطوة 2: إنشاء شبكة باستخدام Polygon Builder

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

تقوم الأداة المساعدة بإنشاء شبكة مكعب أساسية سنقوم بتحريكها لاحقًا.

## الخطوة 3: إنشاء عقدة المكعب مع الإزاحة

```java
// Each cube node has its own translation
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

كل عقدة يمكن أن تمتلك تحويلها الخاص (الإزاحة، الدوران، المقياس). هنا نضيف عقدة فرعية باسم **cube1**.

## الخطوة 4: العثور على خاصية الإزاحة

```java
// Find translation property on node's transform object
Property translation = cube1.getTransform().findProperty("Translation");
```

خاصية `Translation` هي ما سنحركه—نقل المكعب على المحاور X أو Y أو Z.

## الخطوة 5: إنشاء نقطة ربط

```java
// Create a bind point based on the translation property
BindPoint bindPoint = new BindPoint(scene, translation);
```

**نقطة الربط** تربط خاصية (مثل الإزاحة) بمنحنى التحريك.

## الخطوة 6: إنشاء منحنى التحريك للمحور X

```java
// Create the animation curve on the X component of the scale
KeyframeSequence kfs = new KeyframeSequence();

// Add keyframes for X component
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, 20.0f, Interpolation.BEZIER);
kfs.add(5, 30.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the X component
bindPoint.bindKeyframeSequence("X", kfs);
```

يحدد المنحنى ثلاث إطارات مفتاحية: عند الزمن 0، 3، و 5 ثوانٍ. الإطاران الأولان يستخدمان **BEZIER** لحركة سلسة، بينما الأخير يستخدم **LINEAR**.

## الخطوة 7: تكرار للمكوّن Z

```java
// Repeat the process for the Z component
kfs = new KeyframeSequence();
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, -10.0f, Interpolation.BEZIER);
kfs.add(5, 0.0f, Interpolation.LINEAR);

bindPoint.bindKeyframeSequence("Z", kfs);
```

تحريك المحور Z يمنح المكعب مسارًا أكثر ديناميكية في الفضاء ثلاثي الأبعاد.

## الخطوة 8: حفظ المشهد ثلاثي الأبعاد

```java
// Specify the directory for saving the 3D scene
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

يتم حفظ المشهد كملف FBX، يمكنك فتحه في أدوات مثل Blender، Unity، أو Autodesk Maya لمعاينة التحريك.

## المشكلات الشائعة والحلول

| العرض | السبب المحتمل | الحل |
|-------|--------------|------|
| لا يظهر أي حركة | تم إضافة الإطارات المفتاحية للمكوّن الخطأ (مثلاً “Y” بدلًا من “X”) | تحقق من اسم المكوّن في `bindKeyframeSequence`. |
| القفز في التحريك | خلط BEZIER و LINEAR بشكل غير صحيح | حافظ على تقاطع موحد للحصول على حركة أكثر سلاسة، أو اضبط المماس يدويًا. |
| الملف غير محفوظ | مسار الدليل غير صالح | تأكد من أن `MyDir` يشير إلى مجلد موجود قابل للكتابة وينتهي بـ `.fbx`. |

## الأسئلة المتكررة

**س: هل يمكنني استخدام Aspose.3D في مشاريع تجارية؟**  
ج: نعم. اشترِ ترخيصًا تجاريًا من [صفحة الشراء الخاصة بـ Aspose](https://purchase.aspose.com/buy).

**س: هل هناك نسخة تجريبية مجانية؟**  
ج: بالتأكيد. حمّل نسخة تجريبية من [صفحة الإصدارات الخاصة بـ Aspose](https://releases.aspose.com/).

**س: أين يمكنني الحصول على دعم Aspose.3D؟**  
ج: انضم إلى المجتمع في [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة من الموظفين والمستخدمين.

**س: كيف أحصل على ترخيص مؤقت للتقييم؟**  
ج: اطلب [ترخيصًا مؤقتًا](https://purchase.aspose.com/temporary-license/) لتجنب قيود وقت التشغيل أثناء الاختبار.

**س: هل هناك المزيد من البرامج التعليمية المتاحة؟**  
ج: نعم—استكشف الوثائق الكاملة لـ [Aspose.3D](https://reference.aspose.com/3d/java/) للحصول على أمثلة إضافية ومواضيع متقدمة.

## الخاتمة

أنت الآن تعرف **كيفية تحريك كائنات ثلاثية الأبعاد** في Java باستخدام Aspose.3D: إنشاء مشهد، ربط خصائص الإزاحة، تعريف سلاسل الإطارات المفتاحية، وتصدير ملف FBX المتحرك. لا تتردد في تجربة الدوران، المقياس، أو عدة عقد لبناء تحريكات أغنى للألعاب، المحاكاة، أو التصورات.

---

**آخر تحديث:** 2025-12-04  
**تم الاختبار مع:** Aspose.3D for Java 24.12 (الأحدث)  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}