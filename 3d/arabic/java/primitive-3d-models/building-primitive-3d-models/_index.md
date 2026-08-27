---
date: 2026-06-03
description: تعلم كيفية تصدير المشهد كـ FBX وإنشاء cylinder، box، ونماذج primitive
  أخرى باستخدام Aspose.3D for Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: بناء نماذج Primitive 3D باستخدام Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: تصدير المشهد كـ FBX وبناء cylinder باستخدام Aspose.3D Java
url: /ar/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تصدير المشهد كـ FBX وإنشاء أسطوانة باستخدام Aspose.3D Java

## المقدمة

إذا احتجت إلى **إنشاء أسطوانة ثلاثية الأبعاد** (أو أي شكل أساسي آخر) مباشرةً من كود Java، فإن Aspose.3D يجعل المهمة سهلة. في هذا الدرس سنستعرض سير العمل بالكامل — من إعداد البيئة إلى **تصدير المشهد كـ FBX** — لتتمكن من توليد الهندسة ثلاثية الأبعاد برمجياً فوراً. ستتعرف على كيفية تعامل المكتبة مع الأشكال الأولية، وكيفية تنظيمها في رسم المشهد، وكيفية حفظ النتيجة بصيغة يمكن لـ Unity أو Blender أو أي أداة ثلاثية الأبعاد أخرى قراءتها.

## إجابات سريعة
- **ما المكتبة التي تسمح لي بإنشاء أسطوانة ثلاثية الأبعاد في Java؟** Aspose.3D for Java.  
- **ما الصيغة التي يمكنني تصدير المشهد إليها؟** FBX (ASCII 7500) باستخدام `FileFormat.FBX7500ASCII`.  
- **هل أحتاج إلى ترخيص للتطوير؟** نسخة تجريبية مجانية تكفي للاختبار؛ يلزم ترخيص دائم للإنتاج.  
- **ما هي الأشكال الأولية الرئيسية المدعومة؟** Box, Cylinder, Sphere, Cone، وأكثر من 10 أشكال إضافية.  
- **هل الكود متوافق مع Java 8 وما بعدها؟** نعم، Aspose.3D تستهدف JDK 8+.

## ما هو الشكل الأولي للأسطوانة ثلاثية الأبعاد؟

الشكل الأولي للأسطوانة هو شكل هندسي أساسي يُعرّف بنصف القطر والارتفاع. في العديد من خطوط أنابيب 3D يُستخدم ككتلة بناء لنماذج أكثر تعقيدًا مثل الأنابيب، العجلات، أو الأعمدة المعمارية. توفر Aspose.3D فئة `Cylinder` جاهزة، لذا لا تحتاج إلى حساب الرؤوس يدويًا.

## لماذا نستخدم Aspose.3D لـ Java؟

توفر Aspose.3D لـ Java محركًا ثلاثيًا بحتًا بلغة Java يزيل الحاجة إلى المكتبات الأصلية، مما يجعله مثاليًا للتطوير عبر الأنظمة. يدعم مجموعة واسعة من صيغ الاستيراد والتصدير، يقدم رسم مشهد قوي لتنظيم هرمي، ويتضمن أشكالًا أولية مدمجة تسمح بإنشاء الهندسة بأقل قدر من الكود. هذه الميزات معًا تُسرّع التطوير وتقلل من عبء الصيانة.

- **محرك ثلاثي الأبعاد كامل الميزات** – يدعم استيراد/تصدير **أكثر من 30** صيغة شائعة (FBX, OBJ, STL, GLTF, 3DS، إلخ).  
- **واجهة برمجة تطبيقات Java صافية** – لا توجد تبعيات أصلية، مثالية للمشاريع متعددة المنصات.  
- **رسم مشهد قوي** – يتيح لك تنظيم الكائنات بشكل هرمي، مما يجعل إدارة المشاهد الكبيرة سهلة.  
- **ترخيص سهل** – ابدأ بنسخة تجريبية مجانية، ثم ارتقِ إلى ترخيص دائم عند الإطلاق.

## المتطلبات المسبقة

1. **مجموعة تطوير جافا (JDK)** – JDK 8 أو أحدث مثبت على جهازك.  
2. **مكتبة Aspose.3D لـ Java** – قم بتنزيلها وتثبيتها من [صفحة التحميل](https://releases.aspose.com/3d/java/).  

## استيراد الحزم

ابدأ باستيراد مساحة أسماء Aspose.3D الأساسية. يتيح لك ذلك الوصول إلى `Scene` و `Box` و `Cylinder` وثوابت صيغ الملفات.

```java
import com.aspose.threed.*;
```

الآن بعد ربط المكتبة، لننشئ مشهدًا ونضيف بعض الهندسة الأولية.

## كيفية تصدير المشهد كـ FBX وإنشاء الأشكال الأولية ثلاثية الأبعاد؟

حمّل كائن `Scene` جديدًا، أضف عقدًا أولية (Box, Cylinder, إلخ)، ثم استدعِ `save` بصيغة FBX7500ASCII. في بضع أسطر ستحصل على ملف FBX كامل الميزات يمكن فتحه في أي محرر ثلاثي الأبعاد رئيسي، مما يتيح دمجه بسلاسة مع محركات الألعاب، خطوط التصيير، أو تطبيقات AR/VR.

### الخطوة 1: تهيئة كائن المشهد

فئة `Scene` هي الحاوية العليا في Aspose.3D التي تحتفظ بجميع العقد، الأضواء، الكاميرات، والمواد في الذاكرة.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### الخطوة 2: بناء نموذج صندوق ثلاثي الأبعاد

فئة `Box` تمثل منشورًا مستطيلاً وتفيد لاختبار نظام الإحداثيات. إضافتها كطفل لعقدة الجذر في المشهد يضعها في الأصل.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### الخطوة 3: إنشاء نموذج أسطوانة ثلاثية الأبعاد

فئة `Cylinder` هي الشكل الأولي المدمج للأسطوانة في Aspose.3D. تأتي بأبعاد افتراضية (نصف القطر = 1، الارتفاع = 2) لكن يمكنك تخصيصها عبر المُنشئ.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### الخطوة 4: حفظ الرسم بصيغة FBX

بعد تجميع المشهد، صدّره حتى تتمكن الأدوات الأخرى (مثل Unity أو Blender) من قراءته. نستخدم صيغة `FBX7500ASCII`، وهي مدعومة على نطاق واسع وقابلة للقراءة البشرية.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|----------------|-----|
| **الملف غير موجود** عند الحفظ | `myDir` يشير إلى مجلد غير موجود | تأكد من وجود المجلد أو أنشئه باستخدام `new File(myDir).mkdirs();` |
| **مشهد فارغ** بعد التصدير | لم تتم إضافة أي عقد قبل استدعاء `save` | تحقق من تنفيذ استدعاءات `createChildNode` (استخدم التصحيح مع `scene.getRootNode().getChildCount()` ) |
| **استثناء الترخيص** | التشغيل بدون ترخيص صالح في بيئة الإنتاج | تطبيق ترخيص مؤقت أو دائم باستخدام `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## الأسئلة المتكررة

**س: هل يمكنني استخدام Aspose.3D لـ Java مع لغات برمجة أخرى؟**  
ج: Aspose.3D تدعم أساسًا Java، لكن هناك إصدارات متاحة لـ .NET و C++ أيضًا.

**س: هل Aspose.3D مناسبة لمهام النمذجة ثلاثية الأبعاد المعقدة؟**  
ج: بالتأكيد. إنها توفر مجموعة شاملة من الميزات — بما في ذلك تعديل الشبكات، تعيين المواد، والرسوم المتحركة — مما يجعلها مناسبة لكل من الأشكال الأولية البسيطة والنماذج المعقدة.

**س: أين يمكنني العثور على مساعدة ودعم إضافيين؟**  
ج: زر [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على دعم المجتمع والنقاشات.

**س: هل يمكنني تجربة Aspose.3D قبل الشراء؟**  
ج: نعم، يمكنك تجربة [نسخة تجريبية مجانية](https://releases.aspose.com/) قبل اتخاذ قرار الشراء.

**س: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D؟**  
ج: يمكنك الحصول على [ترخيص مؤقت](https://purchase.aspose.com/temporary-license/) لـ Aspose.3D عبر الموقع.

## الخلاصة

لقد تعلمت الآن كيفية **تصدير المشهد كـ FBX**، وكيفية **إنشاء أسطوانة ثلاثية الأبعاد**، وصندوق، ونماذج أولية أخرى باستخدام Aspose.3D لـ Java. لا تتردد في تجربة أشكال أولية إضافية مثل Sphere أو Cone أو Torus، واستكشاف تعيين المواد لإضفاء مظهر واقعي على نماذجك. بمجرد أن تشعر بالراحة، يمكنك دمج ملفات FBX التي تم إنشاؤها في محركات الألعاب، خطوط AR/VR، أو أي سير عمل ثلاثي الأبعاد لاحق.

---

**آخر تحديث:** 2026-06-03  
**تم الاختبار مع:** Aspose.3D for Java 24.11 (أحدث نسخة وقت الكتابة)  
**المؤلف:** Aspose

## دروس ذات صلة

- [كيفية تصدير المشهد إلى FBX واسترجاع معلومات المشهد ثلاثي الأبعاد في Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [كيفية تصدير FBX وبناء هياكل العقد في Java](/3d/java/geometry/build-node-hierarchies/)
- [كيفية إنشاء نماذج أسطوانية باستخدام Aspose.3D لـ Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}