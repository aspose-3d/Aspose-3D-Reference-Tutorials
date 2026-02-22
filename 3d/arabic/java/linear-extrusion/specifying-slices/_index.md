---
date: 2026-02-22
description: تعلم كيفية إنشاء بروز ثلاثي الأبعاد مع شرائح باستخدام Aspose.3D للغة
  Java. يغطي هذا الدليل خطوة بخطوة البروز الخطي، ضبط نصف قطر التقويس، وتصدير OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: إنشاء بروز ثلاثي الأبعاد باستخدام الشرائح – Aspose.3D للـ Java
url: /ar/java/linear-extrusion/specifying-slices/
weight: 13
---

Make sure not to translate code identifiers like `LinearExtrusion.setSlices(int)` etc.

Also not translate URLs.

Now produce final content.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إنشاء بثق ثلاثي الأبعاد مع الشرائح – Aspose.3D للـ Java

## المقدمة

إذا كنت بحاجة إلى **إنشاء كائنات بثق ثلاثي الأبعاد** تبدو ناعمة ودقيقة، فإن التحكم في عدد الشرائح هو المفتاح. في هذا الدرس سنستعرض كيفية تحديد الشرائح أثناء تنفيذ بثق خطي باستخدام Aspose.3D للـ Java. ستتعرف على سبب أهمية عدد الشرائح، وكيفية ضبط نصف قطر التقريب، وكيفية تصدير النتيجة كملف OBJ يمكن استخدامه في أي خط أنابيب ثلاثي الأبعاد.

## إجابات سريعة
- **ماذا تتحكم “الشرائح”؟** عدد المقاطع العرضية المتوسطة المستخدمة لتقريب سطح البثق.  
- **أي طريقة تحدد عدد الشرائح؟** `LinearExtrusion.setSlices(int)`  
- **هل يمكنني تغيير نصف قطر التقريب للملف التعريفي؟** نعم، عبر `RectangleShape.setRoundingRadius(double)`  
- **ما هو تنسيق الملف المستخدم في هذا المثال؟** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **هل أحتاج إلى ترخيص لتشغيل الكود؟** النسخة التجريبية المجانية تكفي للتقييم؛ الترخيص التجاري مطلوب للإنتاج.

## ما هو البثق الخطي مع الشرائح؟

البثق الخطي يأخذ ملفًا تعريفياً ثنائي الأبعاد (مثل المستطيل) ويمده على طول خط مستقيم لتكوين صلب ثلاثي الأبعاد. من خلال تحديد **الشرائح**، تخبر Aspose.3D بعدد الخطوات المتوسطة التي يجب توليدها، وهو ما يؤثر مباشرةً على سلاسة الحواف المنحنية مثل المستطيل المدور.

## لماذا نستخدم Aspose.3D للـ Java لإنشاء بثق ثلاثي الأبعاد؟

* **تحكم كامل** – يمكنك تعديل عدد الشرائح، نصف قطر التقريب، وتنسيق التصدير برمجيًا.  
* **متعدد المنصات** – يعمل على أي بيئة تدعم Java دون تبعيات أصلية.  
* **مرونة التصدير** – حفظ مباشر إلى OBJ، FBX، STL، والعديد من الصيغ الأخرى.

## المتطلبات المسبقة

1. **مجموعة تطوير Java** – JDK 8 أو أعلى مثبتة.  
2. **Aspose.3D للـ Java** – حمّل المكتبة من الموقع الرسمي [هنا](https://releases.aspose.com/3d/java/).  
3. بيئة تطوير متكاملة (IDE) أو محرر نصوص تفضله.

## استيراد الحزم

أضف مساحة أسماء Aspose.3D إلى مشروعك لتتمكن من الوصول إلى فئات النمذجة ثلاثية الأبعاد.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## دليل خطوة بخطوة

### الخطوة 1: إعداد المشهد وتعريف الملف التعريفي

أولاً نقوم بإنشاء `RectangleShape` ونمنحه **نصف قطر تقريبي** لتكون الزوايا ناعمة. ثم نُنشئ كائن `Scene` جديد سيحمل جميع الهندسات.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### الخطوة 2: **إنشاء كائنات عقد فرعية** لكل بثق

كل قطعة هندسية تعيش تحت `Node`. هنا نقوم بإنشاء عقدتين شقيتين – واحدة للبثق منخفض الشرائح وأخرى للبثق عالي الشرائح – وننقل العقدة اليسرى قليلاً إلى الجانب لتسهيل المقارنة بين النتائج.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### الخطوة 3: تنفيذ البثق الخطي و**تحديد الشرائح**

الآن نقوم فعليًا **بإنشاء كائنات بثق ثلاثي الأبعاد**. يأخذ مُنشئ `LinearExtrusion` الملف التعريفي وعمق البثق. باستخدام **فئة داخلية مجهولة** نستدعي `setSlices` للتحكم في السلاسة. العقدة اليسرى تحصل على 2 شريحة فقط (خشن)، بينما العقدة اليمنى تحصل على 10 شرائح (ناعم).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### الخطوة 4: **تصدير OBJ** – حفظ المشهد

أخيرًا نكتب المشهد إلى ملف Wavefront OBJ، وهو تنسيق مدعوم على نطاق واسع من قبل محررات ثلاثية الأبعاد ومحركات الألعاب. يوضح هذا **قدرة تصدير obj java** في Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|------|
| **يظهر البثق مسطحًا** | تم ضبط عدد الشرائح إلى 1 أو 0 | تأكد من استدعاء `setSlices` بقيمة ≥ 2. |
| **الزوايا المدورة تبدو متعرجة** | نصف قطر التقريب صغير جدًا مقارنةً بعدد الشرائح | زد إما نصف القطر أو عدد الشرائح للحصول على منحنيات أكثر سلاسة. |
| **الملف غير موجود عند الحفظ** | `MyDir` يشير إلى مجلد غير موجود | أنشئ المجلد مسبقًا أو استخدم مسارًا مطلقًا. |

## الأسئلة المتكررة

**س: كيف يمكنني تحميل Aspose.3D للـ Java؟**  
ج: يمكنك تحميل المكتبة [هنا](https://releases.aspose.com/3d/java/).

**س: أين يمكنني العثور على وثائق Aspose.3D؟**  
ج: راجع الوثائق [هنا](https://reference.aspose.com/3d/java/).

**س: هل هناك نسخة تجريبية مجانية؟**  
ج: نعم، يمكنك تجربة النسخة التجريبية المجانية [هنا](https://releases.aspose.com/).

**س: كيف يمكنني الحصول على دعم لـ Aspose.3D؟**  
ج: زر منتدى الدعم [هنا](https://forum.aspose.com/c/3d/18).

**س: هل يمكنني شراء ترخيص مؤقت؟**  
ج: نعم، يمكن الحصول على ترخيص مؤقت [هنا](https://purchase.aspose.com/temporary-license/).

---

**آخر تحديث:** 2026-02-22  
**تم الاختبار مع:** Aspose.3D للـ Java 24.11 (أحدث نسخة وقت كتابة الدليل)  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}