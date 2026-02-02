---
date: 2026-02-02
description: تعلم كيفية إنشاء أشكال مروحة أسطوانية في Java باستخدام Aspose.3D. يغطي
  هذا الدليل نمذجة 3D في Java وتقنيات حفظ ملف OBJ في Java.
linktitle: How to Create Cylinder Fan Shapes Using Aspose.3D for Java
second_title: Aspose.3D Java API
title: كيفية إنشاء أشكال مروحة أسطوانية باستخدام Aspose.3D للغة Java
url: /ar/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية إنشاء أشكال أسطوانة مروحة باستخدام Aspose.3D للـ Java

## المقدمة

هل أنت مستعد لإتقان **كيفية إنشاء أسطوانة** بأشكال مروحة في بيئة Java؟ في هذا الدرس سنستعرض كل خطوة — من إعداد المشهد إلى تصدير ملف Wavefront OBJ — باستخدام Aspose.3D. سواءً كنت تبني عنصرًا للعبة، نموذجًا أوليًا في CAD، أو مجرد تجربة مع الهندسة ثلاثية الأبعاد، سترى مدى سهولة نمذجة 3D في Java باستخدام هذه المكتبة القوية.

## إجابات سريعة
- **ما هو الهدف الأساسي؟** إنشاء أسطوانة على شكل مروحة قابلة للتخصيص وحفظها كملف OBJ.  
- **ما المكتبة المستخدمة؟** Aspose.3D للـ Java.  
- **هل أحتاج إلى ترخيص؟** النسخة التجريبية المجانية تكفي للتطوير؛ يتطلب الإنتاج ترخيصًا تجاريًا.  
- **ما المتطلبات المسبقة؟** تثبيت JDK وإضافة حزمة Aspose.3D للـ Java إلى مشروعك.  
- **هل يمكنني تصدير صيغ أخرى؟** نعم — يدعم Aspose.3D صيغًا متعددة؛ هذا المثال يستخدم Wavefront OBJ.

## ما هي أسطوانة المروحة؟

أسطوانة المروحة هي أسطوانة ذات سطح جزئي حيث يتم حذف قطاع من القاعدة الدائرية، مما يخلق فتحة على شكل “مروحة”. هذه الهندسة مفيدة لتصوير الشرائح، اللوحات، أو الأجزاء الميكانيكية المخصصة.

## لماذا نستخدم Aspose.3D لنمذجة 3D في Java؟

يوفر Aspose.3D واجهة برمجة تطبيقات نظيفة وموجهة للكائنات تُجرد الرياضيات منخفضة المستوى للرسومات ثلاثية الأبعاد. يمكنك التركيز على التصميم بدلاً من تفاصيل صيغ الملفات، وتتعامل المكتبة تلقائيًا مع عمليات **java save obj file**.

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من أن لديك:

- **Java Development Kit (JDK)** – قم بتنزيله [هنا](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D للـ Java** – احصل على أحدث ملف JAR من [رابط التحميل](https://releases.aspose.com/3d/java/).  

أضف ملف JAR الخاص بـ Aspose.3D إلى مسار الفئة (classpath) في مشروعك.

## استيراد الحزم

ابدأ باستيراد الفئات الضرورية. سيمنحك ذلك الوصول إلى مشهد 3D، الأشكال الهندسية الأولية، وطرق المساعدة.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## الخطوة 1: إنشاء مشهد

أولاً، نقوم بإنشاء كائن `Scene` جديد. فكر في المشهد كحاوية تحتوي على جميع كائنات 3D، الأضواء، والكاميرات.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## الخطوة 2: إنشاء أسطوانة مروحة (كيفية إنشاء أسطوانة)

الآن نقوم بإنشاء أسطوانة المروحة نفسها. تحدد معلمات المُنشئ نصف القطر، الارتفاع، التشعب، وما إذا كان سيتم توليد الهندسة على شكل مروحة.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **نصيحة احترافية:** عدل `setThetaLength` لتغيير زاوية الفتحة. 270° تُنشئ مروحة ثلاثة أرباع؛ 180° ستعطي نصف أسطوانة.

## الخطوة 3: وضع أسطوانة المروحة

بعد ذلك، نضيف أسطوانة المروحة إلى المشهد وننقلها إلى موقع مناسب. إحداثيات الإزاحة تكون بالترتيب (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## الخطوة 4: إنشاء أسطوانة غير مروحة (مقارنة نمذجة 3D في Java)

لتوضيح مرونة Aspose.3D، نقوم أيضًا بإنشاء أسطوانة عادية بدون فتحة مروحة.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## الخطوة 5: حفظ المشهد (java save obj file)

أخيرًا، نقوم بتصدير المشهد بالكامل إلى ملف Wavefront OBJ. هذه الصيغة مدعومة على نطاق واسع من قبل معظم محررات 3D ومحركات الألعاب.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **ملاحظة:** استبدل `"Your Document Directory"` بمسار مطلق أو نسبي حيث لديك صلاحية كتابة.

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| ملف OBJ فارغ | لم يتم حفظ المشهد أو المسار غير صحيح | تحقق من وجود دليل الإخراج وأن لديك صلاحية كتابة. |
| فتحة المروحة تبدو غير صحيحة | قيمة `ThetaLength` غير صحيحة | استخدم `MathUtils.toRadian(degrees)` لتعيين الزاوية الدقيقة التي تحتاجها. |
| أخطاء تجميع | عدم وجود ملف JAR الخاص بـ Aspose.3D في مسار الفئة | أضف ملف JAR إلى مجلد `libs` في مشروعك وضمنه في مسار البناء. |

## الأسئلة المتكررة

**س: هل Aspose.3D متوافق مع مكتبات Java 3D الأخرى؟**  
ج: نعم، يمكن لـ Aspose.3D التعايش مع مكتبات مثل Java 3D أو jMonkeyج الهندسة المخصصة في خطوط أنابيب أكبر.

**س: هل يمكنني تخصيص مظهر أسطوانة المروحة بشكل أكبر؟**  
ج: بالتأكيد. يمكنك تطبيق المواد، القوام، والإضاءة عبر الوصول إلى مجموعات `Material` و `Light` الخاصة بالعقدة.

**س: أين يمكنني الحصول على دعم إضافي؟**  
ج: زر [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة المجتمع والردود الرسمية.

**س: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج: نعم، يمكنك است عبر [نسخة تجريبية مجانية](https://releases.aspose.com/) قبل الشراء.

**س: كيف أحصل على ترخيص مؤقت للاختبار؟**  
ج: احصل على واحد [هنا](https://purchase.aspose.com/temporary-license/) لفتح جميع الوظائف أثناء التطوير.

---

**آخر تحديث:** 2026-02-02  
**تم الاختبار مع:** Aspose.3D 24.11 للـ Java  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}