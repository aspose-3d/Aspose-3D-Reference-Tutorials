---
date: 2026-02-09
description: تعلم كيفية إنشاء مشهد ثلاثي الأبعاد في جافا، وتطبيق مواد PBR واقعية باستخدام
  Aspose.3D، وحفظ نموذج STL ثلاثي الأبعاد لتصوير الكائنات ثلاثية الأبعاد في جافا.
linktitle: Create 3D Scene Java – Apply PBR Materials with Aspose.3D
second_title: Aspose.3D Java API
title: 'إنشاء مشهد ثلاثي الأبعاد بجافا: تطبيق مواد PBR باستخدام Aspose.3D'
url: /ar/java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إنشاء مشهد ثلاثي الأبعاد Java – تطبيق مواد PBR باستخدام Aspose.3D

## Introduction

في هذا الدرس العملي ستتعلم **كيفية إنشاء مشهد ثلاثي الأبعاد في Java** وإثرائه بمواد التظليل الفيزيائي (PBR) باستخدام مكتبة Aspose.3D. بحلول نهاية الدليل ستكون قادرًا على عرض أسطح واقعية و**حفظ نموذج 3D بصيغة STL** للاستخدام لاحقًا في أي خط أنابيب ثلاثي الأبعاد.

## Quick Answers
- **ماذا يعني “create 3d scene java”؟** إنه عملية بناء كائن Scene يحتوي على الهندسة والإضاءة والكاميرات في تطبيق Java.  
- **أي مكتبة تتعامل مع مواد PBR؟** توفر Aspose.3D فئة `PbrMaterial` جاهزة.  
- **هل يمكنني تصدير النتيجة بصيغة STL؟** نعم – تدعم طريقة `Scene.save` صيغة STL (ASCII وbinary).  
- **هل أحتاج إلى ترخيص للإنتاج؟** يتطلب الاستخدام التجاري ترخيص دائم لـ Aspose.3D؛ ترخيص مؤقت يكفي للاختبار.  
- **ما نسخة Java المطلوبة؟** أي بيئة تشغيل Java 8+ مدعومة.

## How to create 3d scene java with Aspose.3D

كيفية إنشاء مشهد ثلاثي الأبعاد Java باستخدام Aspose.3D

قبل أن نغوص في الشيفرة، دعونا نوضح لماذا بناء مشهد ثلاثي الأبعاد برمجيًا ذو قيمة. سواء كنت تُعد أصولًا لمحرك ألعاب، أو تُولّد نماذج للطباعة ثلاثية الأبعاد، أو تُنشئ تصورات منتجات لموقع تجارة إلكترونية، فإن التحكم الكامل في الهندسة، والمواد، وصيغ التصدير يتيح لك أتمتة خطوط عمل قابلة للتكرار والحفاظ على كل شيء تحت التحكم بالإصدارات.

### Why this matters

* **الاتساق** – تُطبق نفس معلمات المادة في كل مرة، مما يلغي الحاجة إلى تعديل يدوي في محرر ثلاثي الأبعاد.  
* **الأتمتة** – يمكنك إنشاء العشرات من التغييرات (ألوان مختلفة، مستويات الخشونة، أو الأحجام) باستخدام حلقة بسيطة.  
* **متعدد المنصات** – يمكن لأي أداة لاحقة استخدام ملف STL، من Blender إلى برامج تقطيع الطابعات ثلاثية الأبعاد.

## What is a 3D scene in Java?

ما هو المشهد ثلاثي الأبعاد في Java؟

*المشهد* هو الحاوية التي تحتفظ بجميع الكائنات (العُقد)، والهندسة، والمواد، والإضاءة، والكاميرات. فكر فيه كأنه مسرح افتراضي تضع عليه نماذجك ثلاثية الأبعاد. توفر فئة `Scene` في Aspose.3D طريقة نظيفة كائنية لتكوين هذا المسرح برمجيًا.

## Why use PBR materials for rendering 3D objects in Java?

لماذا نستخدم مواد PBR لتصيير الكائنات ثلاثية الأبعاد في Java؟

تقنية PBR (Physically Based Rendering) تحاكي تفاعل الضوء في العالم الحقيقي باستخدام عوامل مثل المعدن والخشونة. النتيجة مظهر أكثر إقناعًا عبر ظروف إضاءة مختلفة، وهو أمر ذو قيمة خاصة لتصور المنتجات، الألعاب، أو تجارب AR/VR.

## Prerequisites

المتطلبات المسبقة

1. **بيئة تطوير Java** – JDK 8 أو أحدث مثبت.  
2. **مكتبة Aspose.3D** – قم بتحميل أحدث JAR من [رابط التحميل](https://releases.aspose.com/3d/java/).  
3. **التوثيق** – تعرّف على API عبر [التوثيق الرسمي](https://reference.aspose.com/3d/java/).  
4. **ترخيص مؤقت (اختياري)** – إذا لم يكن لديك ترخيص دائم، احصل على [ترخيص مؤقت](https://purchase.aspose.com/temporary-license/) للاختبار.

## Common use cases

| حالة الاستخدام | كيف يساعد الدرس |
|----------|------------------------|
| **الطباعة ثلاثية الأبعاد** | التصدير إلى STL يتيح لك إرسال النموذج مباشرة إلى برنامج التقطيع. |
| **خط أنابيب أصول الألعاب** | معلمات مادة PBR تتطابق مع توقعات محركات الألعاب الحديثة. |
| **مكوّن المنتج** | أتمتة تغييرات اللون/الإنهاء عن طريق تعديل قيم المعدن/الخشونة. |

## Import Packages

أضف مساحة الاسم الخاصة بـ Aspose.3D إلى ملف المصدر Java الخاص بك:

```java
import com.aspose.threed.*;
```

## Step 1: Initialize a Scene

إنشاء المشهد الذي سيعمل كقماش لهندستك وموادك.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **نصيحة احترافية:** احرص على أن يشير `MyDir` إلى مجلد قابل للكتابة؛ وإلا سيفشل استدعاء `save`.

## Step 2: Initialize a PBR Material

تكوين مادة PBR بقيم معدنية وخشونة تعطي مظهرًا شبه معدني.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **لماذا هذه القيم؟** عامل معدني عالي (≈ 0.9) يجعل السطح يتصرف كالمعدن، بينما الخشونة العالية (≈ 0.9) تضيف انتشارًا خفيفًا، مما يمنع الانعكاس المثالي كالمرآة.

## Step 3: Create a 3D Object and Apply the Material

هنا نولد هندسة صندوق بسيط، نرفعه إلى عقدة الجذر في المشهد، ونُعيّن مادة PBR التي أنشأناها للتو.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **مشكلة شائعة:** نسيان تعيين المادة على العقدة سيترك الكائن بالمظهر الافتراضي (غير PBR).

## Step 4: Save the 3D Scene (STL Export)

تصدير المشهد بالكامل—بما في ذلك الصندوق المُحسّن بـ PBR—إلى ملف STL. STL هو تنسيق مدعوم على نطاق واسع للطباعة ثلاثية الأبعاد وفحوصات بصرية سريعة.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

يمكنك أيضًا اختيار `FileFormat.STLBINARY` إذا كان حجم الملف الأصغر مطلوبًا.

### Troubleshooting tips

| المشكلة | السبب المحتمل | الحل |
|-------|--------------|-----|
| **الملف غير محفوظ** | `MyDir` يشير إلى مجلد غير موجود أو يفتقر إلى صلاحية الكتابة | تحقق من وجود المجلد وأن عملية Java لديها صلاحية الكتابة |
| **المادة تظهر مسطحة** | قيم المعدن/الخشونة مضبوطة على 0 | زيادة `setMetallicFactor` و/أو `setRoughnessFactor` |
| **لا يمكن فتح ملف STL** | علامة تنسيق الملف غير صحيحة (ASCII مقابل Binary) للعارض | استخدم تعداد `FileFormat` المناسب للعارض المستهدف |

## Frequently Asked Questions

**س: هل يمكنني استخدام Aspose.3D للمشاريع التجارية؟**  
ج: نعم. اشترِ ترخيصًا تجاريًا من [صفحة الشراء](https://purchase.aspose.com/buy).

**س: كيف أحصل على الدعم لـ Aspose.3D؟**  
ج: انضم إلى المجتمع على [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة مجانية، أو افتح تذكرة دعم بترخيص صالح.

**س: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج: بالتأكيد. حمّل نسخة تجريبية من [صفحة النسخة التجريبية المجانية](https://releases.aspose.com/).

**س: أين يمكنني العثور على توثيق مفصل لـ Aspose.3D؟**  
ج: جميع مراجع API متاحة في [التوثيق الرسمي](https://reference.aspose.com/3d/java/).

**س: كيف أحصل على ترخيص مؤقت للاختبار؟**  
ج: اطلب واحدًا عبر [رابط الترخيص المؤقت](https://purchase.aspose.com/temporary-license/).

## Conclusion

لقد **أنشأت الآن مشهدًا ثلاثيًا الأبعاد في Java**، وطبقت مادة PBR واقعية، وصدرّت النتيجة كملف STL باستخدام Aspose.3D. يمنحك هذا سير العمل أساسًا قويًا لبناء تصورات أغنى، وإعداد أصول للطباعة ثلاثية الأبعاد، أو إمداد النماذج إلى محركات الألعاب.

---

**Last Updated:** 2026-02-09  
**Tested With:** Aspose.3D 24.12 (latest)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}