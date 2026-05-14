---
date: 2026-05-14
description: تعلم كيفية تصدير STL في Java عن طريق إنشاء مشهد ثلاثي الأبعاد، وتطبيق
  مواد PBR واقعية باستخدام Aspose.3D، وحفظ النموذج للعرض.
keywords:
- how to export stl
- Aspose 3D PBR materials
- Java 3D scene creation
linktitle: كيفية تصدير STL في Java – إنشاء مشهد ثلاثي الأبعاد باستخدام Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-05-14'
  description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  headline: How to Export STL in Java – Create 3D Scene with Aspose.3D
  type: TechArticle
- description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  name: How to Export STL in Java – Create 3D Scene with Aspose.3D
  steps:
  - name: '**Java Development Environment** – JDK 8 or newer installed.'
    text: '**Java Development Environment** – JDK 8 or newer installed.'
  - name: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
    text: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
  - name: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
    text: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
  - name: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
    text: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
  type: HowTo
- questions:
  - answer: It’s the process of building a `Scene` object that holds geometry, lights,
      and cameras in a Java application.
    question: What does “create 3d scene java” mean?
  - answer: Aspose.3D provides a ready‑made `PbrMaterial` class.
    question: Which library handles PBR materials?
  - answer: Yes – the `Scene.save` method supports STL (ASCII and binary).
    question: Can I export the result as STL?
  - answer: A permanent Aspose.3D license is required for commercial use; a temporary
      license works for testing.
    question: Do I need a license for production?
  - answer: Any Java 8+ runtime is supported.
    question: What Java version is required?
  type: FAQPage
second_title: Aspose.3D Java API
title: كيفية تصدير STL في Java – إنشاء مشهد ثلاثي الأبعاد باستخدام Aspose.3D
url: /ar/java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تصدير STL في Java – إنشاء مشهد 3D باستخدام Aspose.3D

## مقدمة

في هذا الدرس العملي ستتعلم **كيفية تصدير STL** من تطبيق Java من خلال بناء مشهد 3D كامل، وتطبيق مواد Physically Based Rendering (PBR)، وحفظ النتيجة باستخدام Aspose.3D. سواءً كنت تستهدف الطباعة ثلاثية الأبعاد، أو خطوط أنابيب محركات الألعاب، أو تصور المنتجات، فإن الخطوات أدناه توفر لك سير عمل قابل للتكرار ومتحكم فيه بالإصدار يعمل على أي بيئة تشغيل Java 8+.

## إجابات سريعة
- **ماذا يعني “create 3d scene java”؟** إنه عملية بناء كائن `Scene` الذي يحتوي على الهندسة والإضاءة والكاميرات في تطبيق Java.  
- **أي مكتبة تتعامل مع مواد PBR؟** توفر Aspose.3D فئة `PbrMaterial` جاهزة.  
- **هل يمكنني تصدير النتيجة كـ STL؟** نعم – تدعم طريقة `Scene.save` صيغة STL (ASCII وbinary).  
- **هل أحتاج إلى ترخيص للإنتاج؟** يتطلب الاستخدام التجاري ترخيص دائم لـ Aspose.3D؛ الترخيص المؤقت يكفي للاختبار.  
- **ما نسخة Java المطلوبة؟** أي بيئة تشغيل Java 8+ مدعومة.

## كيفية إنشاء مشهد 3d java باستخدام Aspose.3D

`Scene` هي الفئة الحاوية الرئيسية التي تمثل وثيقة 3D. قم بتحميل وتكوين وحفظ المشهد ببضع أسطر من الشيفرة فقط. أولاً، تنشئ كائن `Scene`، ثم تُرفق الهندسة و`PbrMaterial`، وأخيرًا تستدعي `Scene.save` بصيغة STL. يتيح لك هذا التدفق الشامل أتمتة إنشاء الأصول دون الحاجة إلى فتح محرر 3D.

## ما هو مشهد 3D في Java؟

*المشهد* هو الحاوية التي تحتفظ بجميع الكائنات (العقد)، والهندسة الخاصة بها، والمواد، والإضاءة، والكاميرات. فكر فيه كمنصة افتراضية تضع عليها نماذجك ثلاثية الأبعاد. توفر فئة `Scene` في Aspose.3D طريقة نظيفة كائنية‑التوجه لبناء هذه المنصة برمجيًا.

## لماذا نستخدم مواد PBR لتصيير كائنات 3D في Java؟

PBR (Physically Based Rendering) تحاكي تفاعل الضوء في العالم الحقيقي باستخدام معلمات المعدن والخشونة. النتيجة هي مادة تبدو متسقة تحت أي ظروف إضاءة، وهو أمر أساسي لتصور المنتجات الواقعي، والواقع المعزز/الواقع الافتراضي، ومحركات الألعاب الحديثة. من خلال التحكم في المعدن، والخشونة، والالوبيد، وخرائط العادي، يمكنك تحقيق مجموعة واسعة من تشطيبات السطح — من المعدن المصقول إلى البلاستيك غير اللامع — دون تعديل الشادرات يدويًا.

## المتطلبات المسبقة

1. **بيئة تطوير Java** – تثبيت JDK 8 أو أحدث.  
2. **مكتبة Aspose.3D** – تحميل أحدث JAR من [رابط التحميل](https://releases.aspose.com/3d/java/).  
3. **التوثيق** – تعرّف على API عبر [التوثيق الرسمي](https://reference.aspose.com/3d/java/).  
4. **ترخيص مؤقت (اختياري)** – إذا لم يكن لديك ترخيص دائم، احصل على [ترخيص مؤقت](https://purchase.aspose.com/temporary-license/) للاختبار.

## حالات الاستخدام الشائعة

| حالة الاستخدام | كيف يساعد الدرس |
|----------|------------------------|
| **الطباعة ثلاثية الأبعاد** | يتيح تصدير إلى STL إرسال النموذج مباشرة إلى أداة القطع. |
| **خط أنابيب أصول اللعبة** | تطابق معلمات مادة PBR توقعات محركات الألعاب الحديثة. |
| **مكوّن المنتج** | أتمتة تنوعات اللون/الإنهاء عن طريق ضبط قيم المعدن/الخشونة. |

## استيراد الحزم

يجب استيراد مساحة الأسماء `Aspose.3D` حتى يتمكن المترجم من حل الفئات المستخدمة في الدرس.

```java
import com.aspose.threed.*;
```

## الخطوة 1: تهيئة مشهد

`Scene` هي الحاوية الأساسية لجميع محتوى 3D. إنشاء نسخة جديدة يمنحك لوحة نظيفة يمكنك إضافة الهندسة والإضاءة والكاميرات إليها.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **نصيحة احترافية:** حافظ على أن يشير `MyDir` إلى مجلد قابل للكتابة؛ وإلا سيفشل استدعاء `save`.

## الخطوة 2: تهيئة مادة PBR

`PbrMaterial` تحدد خصائص التصيير القائم على الفيزياء مثل المعدن والخشونة. تُعرّف `PbrMaterial` المعدن، والخشونة، وغيرها من خصائص السطح. ضبط عامل معدني عالي (≈ 0.9) وخشونة 0.9 ينتج مظهر معدن مصقول واقعي.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **لماذا هذه القيم؟** عامل معدني عالي يجعل السطح يتصرف كالمعدن، بينما الخشونة العالية تضيف انتشارًا طفيفًا، مما يمنع الحصول على لمسة مرآة مثالية.

## الخطوة 3: إنشاء كائن 3D وتطبيق المادة

هنا نقوم بإنشاء هندسة صندوق بسيط، وربطه بعقدة الجذر في المشهد، وتعيين `PbrMaterial` التي أنشأناها للتو.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **مشكلة شائعة:** نسيان تعيين المادة على العقدة سيترك الكائن بالمظهر الافتراضي (غير PBR).

## الخطوة 4: حفظ مشهد 3D (تصدير STL)

`Scene.save` يكتب المشهد إلى ملف بالصيغ المحددة. صدّر المشهد بالكامل — بما في ذلك الصندوق المعزز بـ PBR — إلى ملف STL. STL هو صيغة مدعومة على نطاق واسع للطباعة ثلاثية الأبعاد والفحوصات البصرية السريعة.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

`FileFormat.STLBINARY` يحدد إخراج STL ثنائي، وهو أصغر من ASCII. يمكنك أيضًا اختيار `FileFormat.STLASCII` إذا كنت تفضّل ملفًا قابلًا للقراءة البشرية.

## لماذا هذا مهم

تضمن معلمات المادة المتسقة أن كل نموذج مُولد يبدو بنفس الشكل عبر مشاهد مختلفة وإعدادات إضاءة متنوعة. تتيح الأتمتة إنتاج دفعات كبيرة من التنوعات بأقل جهد، بينما يضمن إخراج STL متعدد المنصات التوافق مع أدوات تتراوح من Blender إلى أدوات القطع للطابعات ثلاثية الأبعاد. معًا، تُسرّع هذه الفوائد خطوط تطوير البرمجيات وتقلل الأخطاء اليدوية.

## نصائح استكشاف الأخطاء وإصلاحها

| المشكلة | السبب المحتمل | الحل |
|-------|--------------|-----|
| **الملف غير محفوظ** | `MyDir` يشير إلى مجلد غير موجود أو يفتقر إلى صلاحية الكتابة | تحقق من وجود الدليل وأن عملية Java لديك لديها صلاحية كتابة |
| **المادة تبدو مسطحة** | قيم المعدن/الخشونة مضبوطة على 0 | زيادة `setMetallicFactor` و/أو `setRoughnessFactor` |
| **لا يمكن فتح ملف STL** | علم تنسيق الملف غير صحيح (ASCII مقابل Binary) للعارض | استخدم قيمة `FileFormat` المتطابقة للعارض المستهدف |

## الأسئلة المتكررة

**س:** هل يمكنني استخدام Aspose.3D للمشاريع التجارية؟  
**ج:** نعم. اشترِ ترخيصًا تجاريًا من [صفحة الشراء](https://purchase.aspose.com/buy).

**س:** كيف أحصل على دعم Aspose.3D؟  
**ج:** انضم إلى المجتمع على [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة مجانية، أو افتح تذكرة دعم بترخيص صالح.

**س:** هل هناك نسخة تجريبية مجانية؟  
**ج:** بالتأكيد. حمّل نسخة تجريبية من [صفحة التجربة المجانية](https://releases.aspose.com/).

**س:** أين يمكنني العثور على توثيق مفصل لـ Aspose.3D؟  
**ج:** جميع مراجع API متاحة في [التوثيق الرسمي](https://reference.aspose.com/3d/java/).

**س:** كيف أحصل على ترخيص مؤقت للاختبار؟  
**ج:** اطلب واحدًا عبر [رابط الترخيص المؤقت](https://purchase.aspose.com/temporary-license/).

**Last Updated:** 2026-05-14  
**Tested With:** Aspose.3D 24.12 (latest)  
**Author:** Aspose  

{{< blocks/products/products-backtop-button >}}

## دروس ذات صلة

- [إنشاء مشهد 3D Java باستخدام Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [كيفية تصدير المشهد إلى FBX واسترجاع معلومات مشهد 3D في Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [كيفية تصدير OBJ - تعديل اتجاه المستوى لتحديد موضع المشهد 3D بدقة في Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}