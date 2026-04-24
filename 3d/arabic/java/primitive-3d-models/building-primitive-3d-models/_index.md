---
date: 2026-03-13
description: تعلم كيفية إنشاء أسطوانات وصناديق ونماذج أولية أخرى ثلاثية الأبعاد باستخدام
  Aspose.3D للغة Java وحفظ المشهد بصيغة FBX.
linktitle: Building Primitive 3D Models with Aspose.3D for Java
second_title: Aspose.3D Java API
title: كيفية إنشاء أسطوانة ثلاثية الأبعاد ونماذج ثلاثية الأبعاد بدائية أخرى باستخدام
  Aspose.3D للـ Java
url: /ar/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# بناء نماذج ثلاثية الأبعاد بدائية باستخدام Aspose.3D للـ Java

## مقدمة

## إجابات سريعة
- **ما المكتبة التي تسمح لي بإنشاء أسطوانة ثلاثية الأبعاد في Java؟** Aspose.3D for Java.
- **ما الصيغة التي يمكنني تصدير المشهد إليها؟** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.
- **هل أحتاج إلى ترخيص للتطوير؟** A free trial works for testing; a permanent license is required for production.
- **ما هي الأشكال البدائية الرئيسية المدعومة؟** Box, Cylinder, Sphere, Cone, and more.
- **هل الكود متوافق مع Java 8 وما بعده؟** Yes, Aspose.3D targets JDK 8+.

## ما هو الشكل البدائي الأسطوانة ثلاثية الأبعاد؟

الأسطوانة البدائية هي شكل هندسي أساسي يُعرّف بنصف القطر والارتفاع. في العديد من خطوط أنابيب 3D تُستخدم ككتلة بناء لنماذج أكثر تعقيدًا مثل الأنابيب، العجلات، أو أعمدة العمارة. توفر Aspose.3D فئة `Cylinder` جاهزة، لذا لا تحتاج إلى حساب الرؤوس يدويًا.

## لماذا تستخدم Aspose.3D للـ Java؟

- **محرك ثلاثي الأبعاد كامل المميزات** – يدعم الاستيراد/التصدير للعديد من الصيغ الشائعة (FBX, OBJ, STL, إلخ).
- **واجهة برمجة تطبيقات Java صافية** – لا توجد تبعيات أصلية، مثالية للمشاريع متعددة المنصات.
- **رسم بياني للمشهد قوي** – يتيح لك تنظيم الكائنات هرمياً.
- **ترخيص سهل** – ابدأ بتجربة مجانية، ثم ارتقِ إلى ترخيص دائم.

## المتطلبات المسبقة

قبل الغوص في الكود، تأكد من أن لديك:

1. **مجموعة تطوير Java (JDK)** – JDK 8 أو أحدث مثبت على جهازك.  
2. **مكتبة Aspose.3D للـ Java** – قم بتنزيلها وتثبيتها من [صفحة التحميل](https://releases.aspose.com/3d/java/).  

## استيراد الحزم

ابدأ باستيراد مساحة الاسم الأساسية لـ Aspose.3D. هذا يمنحك الوصول إلى `Scene`, `Box`, `Cylinder`, وثوابت صيغ الملفات.

```java
import com.aspose.threed.*;
```

الآن بعد ربط المكتبة، لننشئ مشهدًا ونضيف بعض الهندسة البدائية.

## كيفية إنشاء أسطوانة ثلاثية الأبعاد وغيرها من الأشكال البدائية في المشهد

### الخطوة 1: تهيئة كائن المشهد

أولاً، نحتاج إلى حاوية `Scene` ستحتوي على جميع عقد 3D الخاصة بنا.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### الخطوة 2: بناء نموذج صندوق ثلاثي الأبعاد

الشكل البدائي الصندوق مفيد لاختبار نظام الإحداثيات. هنا نضيفه كطفل لعقدة الجذر في المشهد.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### الخطوة 3: إنشاء نموذج أسطوانة ثلاثية الأبعاد

الآن نقوم فعليًا **بإنشاء أسطوانة ثلاثية الأبعاد**. فئة `Cylinder` تأتي بأبعاد افتراضية معقولة، لكن يمكنك تخصيص نصف القطر والارتفاع عبر المُنشئ إذا لزم الأمر.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### الخطوة 4: حفظ الرسم بصيغة FBX

بعد تجميع المشهد، صدّره حتى تتمكن الأدوات الأخرى (مثل Unity, Blender) من قراءته. نستخدم صيغة `FBX7500ASCII`، وهي مدعومة على نطاق واسع.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## المشكلات الشائعة والحلول

| المشكلة | سبب حدوثها | الحل |
|-------|----------------|-----|
| **الملف غير موجود** عند الحفظ | `myDir` يشير إلى مجلد غير موجود | تأكد من وجود المجلد أو أنشئه باستخدام `new File(myDir).mkdirs();` |
| **مشهد فارغ** بعد التصدير | لم يتم إضافة أي عقد قبل استدعاء `save` | تحقق من تنفيذ استدعاءات `createChildNode` (قم بالتصحيح باستخدام `scene.getRootNode().getChildCount()` ) |
| **استثناء الترخيص** | التشغيل بدون ترخيص صالح في بيئة الإنتاج | تطبيق ترخيص مؤقت أو دائم باستخدام `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## الأسئلة المتكررة

**س: هل يمكنني استخدام Aspose.3D للـ Java مع لغات برمجة أخرى؟**  
ج: Aspose.3D يدعم أساساً Java، لكن هناك إصدارات متاحة للغات أخرى مثل .NET.

**س: هل Aspose.3D مناسب لمهام النمذجة ثلاثية الأبعاد المعقدة؟**  
ج: بالتأكيد! Aspose.3D يوفر مجموعة شاملة من الميزات، مما يجعله مناسباً لكل من المهام البسيطة والمعقدة في النمذجة ثلاثية الأبعاد.

**س: أين يمكنني العثور على مساعدة ودعم إضافيين؟**  
ج: زر [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على دعم المجتمع والنقاشات.

**س: هل يمكنني تجربة Aspose.3D قبل الشراء؟**  
ج: نعم، يمكنك استكشاف [نسخة تجريبية مجانية](https://releases.aspose.com/) قبل اتخاذ قرار الشراء.

**س: كيف أحصل على ترخيص مؤقت لـ Aspose.3D؟**  
ج: يمكنك الحصول على [ترخيص مؤقت](https://purchase.aspose.com/temporary-license/) لـ Aspose.3D عبر الموقع الإلكتروني.

## الخلاصة

لقد تعلمت الآن كيفية **إنشاء أسطوانة ثلاثية الأبعاد**، صندوق، وغيرها من النماذج البدائية باستخدام Aspose.3D للـ Java، وكيفية **حفظ المشهد كملف FBX** للاستخدام لاحقًا. لا تتردد في تجربة أشكال بدائية أخرى (Sphere, Cone, إلخ) واستكشاف تعيين المواد لإضفاء مظهر واقعي على نماذجك.

---

**آخر تحديث:** 2026-03-13  
**تم الاختبار مع:** Aspose.3D للـ Java 24.11 (أحدث نسخة وقت الكتابة)  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}