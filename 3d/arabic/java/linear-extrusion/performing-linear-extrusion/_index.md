---
date: 2025-12-18
description: تعلم كيفية بَرْنِ الشكل في Java باستخدام Aspose.3D، وإنشاء مشهد ثلاثي
  الأبعاد، وتصدير ملفات Wavefront OBJ بسهولة.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: كيفية استخراج الشكل في جافا باستخدام Aspose.3D (استخراج خطي)
url: /ar/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إجراء البثق الخطي في Aspose.3D للـ Java

## مقدمة

مرحبًا بك في هذا الدرس الشامل حول **how to extrude shape** في Aspose.3D للـ Java! إذا كنت ترغب في تحسين مهاراتك في نمذجة 3D باستخدام Java، فأنت في المكان الصحيح. سنرشدك خلال إنشاء مشهد 3D، إجراء البثق الخطي، وتصدير النتيجة كملف Wavefront OBJ — كل ذلك بأمثلة شفرة واضحة خطوة بخطوة.

## إجابات سريعة
- **ما هو البثق الخطي؟** تمديد ملف ثنائي الأبعاد على طول مسار مستقيم لإنشاء جسم ثلاثي الأبعاد.  
- **ما المكتبة التي تتعامل مع ذلك في Java؟** Aspose.3D للـ Java.  
- **هل يمكنني التصدير إلى OBJ؟** نعم، باستخدام ميزة تصدير Wavefront OBJ.  
- **هل أحتاج إلى ترخيص للتطوير؟** النسخة التجريبية المجانية تكفي للاختبار؛ الترخيص مطلوب للإنتاج.  
- **ما نسخة Java المطلوبة؟** Java 1.6 أو أحدث.

## ما هو “how to extrude shape”؟
البثق الخطي هو تقنية أساسية في **3d modeling java** تحول ملفًا مسطحًا — مثل المستطيل — إلى جسم حجمي عن طريق سحبه على مسافة محددة. تُستخدم هذه الطريقة على نطاق واسع لإنشاء قطع ميكانيكية، عناصر معمارية، ونماذج زخرفية.

## لماذا نستخدم Aspose.3D للبثق الخطي؟
- **تحكم كامل** في الهندسة (الشرائح، الالتواء، الإزاحة).  
- **تكامل سلس** مع مشاريع Java — بدون تبعيات أصلية.  
- **مصدِّرات مدمجة** للأنساق الشائعة، بما في ذلك Wavefront OBJ، مما يجعل من السهل **generate 3d model** للملفات في خطوط المعالجة اللاحقة.

## المتطلبات المسبقة

قبل الغوص في الدرس، تأكد من أن لديك المتطلبات المسبقة التالية جاهزة:

1. **بيئة تطوير Java** — JDK (1.6 أو أحدث) وIDE المفضلة لديك.  
2. **مكتبة Aspose.3D** — قم بتنزيل وتثبيت المكتبة من الموقع الرسمي **[هنا](https://releases.aspose.com/3d/java/)**.

## استيراد الحزم

بعد إعداد بيئة التطوير الخاصة بك وتثبيت مكتبة Aspose.3D، استورد الحزمة اللازمة:

```java
import com.aspose.threed.*;
```

### الخطوة 1: تعيين دليل المستند

حدد المجلد الذي سيتم حفظ الملفات المولدة فيه:

```java
String MyDir = "Your Document Directory";
```

> هذا يضمن أن عملية **generate 3d model** تكتب ملف OBJ إلى موقع معروف.

### الخطوة 2: تهيئة الشكل الأساسي

أنشئ مستطيلًا سيعمل كملف بروفايل للبثق:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

يمكنك تعديل نصف قطر التقويس للحصول على زوايا مستديرة أو ضبطه إلى `0` للحصول على مستطيل مثالي.

### الخطوة 3: إجراء البثق الخطي

الآن نقوم ببثق المستطيل على طول محور Z، إضافة شرائح، تمكين التمركز، وتطبيق الالتواء مع إزاحة:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **طول البثق** — `10` وحدات.  
- **الشرائح** — `100` للحصول على هندسة ناعمة.  
- **الالتواء** — `360°` يخلق دورة كاملة.  
- **إزاحة الالتواء** — تنقل أصل الالتواء إلى `(10, 0, 0)`.

### الخطوة 4: إنشاء مشهد 3D

أنشئ حاوية مشهد وأضف البثق كعقدة فرعية. هذه الخطوة **creates 3d scene** التي يمكنها احتواء عدة كائنات:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### الخطوة 5: حفظ مشهد 3D

صدّر المشهد إلى ملف Wavefront OBJ. هذا يوضح قدرات **wavefront obj export** و **save 3d obj**:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

بعد تشغيل الشفرة، ستجد `LinearExtrusion.obj` في الدليل الذي حددته، جاهزًا للفتح في أي عارض 3D أو لمعالجة إضافية.

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| ملف OBJ فارغ | مسار دليل الإخراج غير صحيح أو غير قابل للكتابة | تحقق من أن `MyDir` يشير إلى مجلد موجود مع أذونات كتابة. |
| لم يتم تطبيق الالتواء | `setCenter(true)` محذوف | تأكد من تمكين التمركز أو اضبط قيم `setTwistOffset`. |
| خطأ تجميع في `LinearExtrusion` | استخدام نسخة أقدم من Aspose.3D | قم بالتحديث إلى أحدث إصدار من Aspose.3D. |

## الأسئلة المتكررة

**س: هل Aspose.3D متوافق مع جميع إصدارات Java؟**  
ج: Aspose.3D يعمل مع Java 1.6 وما بعدها.

**س: هل يمكنني استخدام Aspose.3D للمشاريع التجارية؟**  
ج: نعم، يُسمح بالاستخدام التجاري مع ترخيص صالح. يمكنك الحصول على واحد **[هنا](https://purchase.aspose.com/buy)**.

**س: أين يمكنني الحصول على الدعم إذا واجهت مشاكل؟**  
ج: زر **[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18)** للحصول على مساعدة المجتمع أو اشترِ **[ترخيصًا مؤقتًا](https://purchase.aspose.com/temporary-license/)** للحصول على دعم مميز.

**س: ما هي الميزات الأخرى لنمذجة 3D التي يوفرها Aspose.3D؟**  
ج: تشمل المكتبة تعديل الشبكات، عمليات بوليانية، تخطيط القوام، وأكثر. راجع القائمة الكاملة **[هنا](https://reference.aspose.com/3d/java/)**.

**س: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج: نعم، يمكنك تنزيل نسخة تجريبية **[هنا](https://releases.aspose.com/)**.

## الخلاصة

لقد تعلمت الآن **how to extrude shape** باستخدام Aspose.3D للـ Java، أنشأت مشهد 3D، وصَدَّرت النتيجة كملف Wavefront OBJ. تفتح هذه التقنية الباب أمام مجموعة واسعة من مشاريع **3d modeling java** — من الأجزاء البسيطة إلى التجميعات المعقدة. استكشف ميزات إضافية مثل العمليات البوليانية أو تخطيط القوام لإثراء نماذجك أكثر.

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## الكلمات المفتاحية المستهدفة:

**الكلمة المفتاحية الأساسية (أعلى أولوية):**  
how to extr shape

**الكلمات المفتاحية الثانوية (داعمة):**  
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj