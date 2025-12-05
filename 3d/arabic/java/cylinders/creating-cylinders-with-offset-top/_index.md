---
date: 2025-12-05
description: تعلم كيفية إنشاء نماذج أسطوانية ذات قمم مائلة في Aspose.3D للغة Java،
  إضافة خطوات عقدة فرعية في Java، وتصدير ملفات OBJ لنماذج 3D بسهولة.
language: ar
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: كيفية إنشاء أسطوانة ذات قمة مائلة في Aspose.3D للـ Java
url: /java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية إنشاء أسطوانة مع قمة إزاحة في Aspose.3D للغة Java

## المقدمة

إذا كنت تبحث عن **كيفية إنشاء أسطوانة** مع قمة إزاحة مخصصة في مشهد ثلاثي الأبعاد مبني على Java، فإن Aspose.3D يجعل العملية بسيطة. في هذا البرنامج التعليمي سنستعرض كل خطوة — من إعداد المشهد إلى تصدير النموذج النهائي كملف OBJ — حتى تتمكن من دمج الأسطوانات ذات القمة الإزاحة في تطبيقاتك بثقة.

## إجابات سريعة
- **ما المكتبة المستخدمة؟** Aspose.3D للغة Java  
- **هل يمكن إزاحة قمة الأسطوانة؟** نعم، باستخدام `setOffsetTop`  
- **كيف أضيف عقدة فرعية في Java؟** استدعِ `createChildNode` على العقدة الجذرية  
- **إلى أي صيغة يمكنني التصدير؟** Wavefront OBJ (`export 3d model obj`)  
- **هل أحتاج إلى ترخيص للاختبار؟** ترخيص مؤقت متاح للتقييم  

## ما هو “كيفية إنشاء أسطوانة” مع قمة إزاحة؟

إنشاء أسطوانة مع قمة إزاحة يعني أن الوجه الدائري العلوي يتم إزاحته بالنسبة للقاعدة، مما يتيح لك نمذجة أشكال مخروطة أو غير متماثلة دون تعديل يدوي للرؤوس. توفر Aspose.3D مُنشئًا مخصصًا وخاصية `OffsetTop` لتحقيق ذلك في بضع أسطر من الشيفرة فقط.

## لماذا نستخدم Aspose.3D للغة Java؟

- **API عالي المستوى:** لا حاجة لإدارة بيانات الشبكة منخفضة المستوى.  
- **متعدد المنصات:** يعمل على أي بيئة متوافقة مع JVM.  
- **مصدر تصدير مدمج:** احفظ مباشرةً إلى OBJ، STL، FBX، وأكثر.  
- **قابل للتوسيع:** أضف بسهولة عقدًا فرعية، طبّق التحويلات، ودمج مع مكتبات Java الأخرى.

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من وجود ما يلي:

- **مجموعة تطوير جافا (JDK)** — نسخة متوافقة مثبتة.  
- **مكتبة Aspose.3D للغة Java** — حمّل أحدث ملف JAR من الموقع الرسمي [هنا](https://releases.aspose.com/3d/java/).  
- بيئة تطوير متكاملة من اختيارك (Eclipse، IntelliJ IDEA، NetBeans، إلخ).

## استيراد الحزم

أولاً، استورد الفئات التي سنحتاجها. ضع هذه العبارات في أعلى ملف Java الخاص بك:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## دليل خطوة بخطوة

### الخطوة 1: إنشاء مشهد

المشهد يعمل كحاوية لجميع الكائنات ثلاثية الأبعاد.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### الخطوة 2: تهيئة أسطوانة مع قمة إزاحة

هنا نجيب على **كيفية إنشاء أسطوانة** مع إزاحة مخصصة. يحدد المُنشئ نصف القطر، الارتفاع، الشرائح، المكدسات، وما إذا كانت الأسطوانة مغلقة. بعد ذلك، نُزاح القمة باستخدام `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### الخطوة 3: كيفية **إضافة عقدة فرعية Java** – إرفاق الأسطوانة الأولى

ننشئ عقدة فرعية تحت عقدة الجذر في المشهد ون```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### الخطوة 4: تهيئة أسطوانة ثانية (بدون إزاحة)

للمقارنة، نضيف أسطوانة عادية بدون إزاحة.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### الخطوة 5: كيفية **إضافة عقدة فرعية Java** – إرفاق الأسطوانة الثانية

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

 كيفية **تصدير نموذج 3D بصيغة OBJ** – حفظ المشهد

أخيرًا، نصدر المشهد بالكامل (كلا الأسطوانتين) كملف Wavefront OBJ، وهو مدعوم على نطاق واسع من أدوات 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

عند تشغيل البرنامج، ستجد الملف `CustomizedOffsetTopCylinder.obj` في الدليل المحدد، جاهزًا للفتح في Blender، Maya، أو أي عارض OBJ آخر.

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| **ملف OBJ فارغ** | لم يتم حفظ المشهد بشكل صحيح أو المسار غير صحيح. | تحقق من وجود دليل الإخراج وأن لديك صلاحيات كتابة. |
| **لم تُطبق الإزاحة** | استخدام نسخة قديمة من Aspose.3D. | حدّث إلى أحدث مكتبة تدعم `setOffsetTop`. |
| **العقدة الفرعية غير مرئية** | لم يتم تطبيق التحويل. | تأكد من استدعاء `getTransform().setTranslation` بعد إنشاء العقدة الفرعية. |

## الأسئلة المتكررة

**س: هل Aspose.3D متوافق مع مختلف بيئات تطوير Java؟**  
ج: نعم، يعمل بسلاسة مع Eclipse، IntelliJ IDEA، NetBeans، وغيرها من البيئات.

**س: هل يمكنني تطبيق خامات (textures) على الكائنات ثلاثية الأبعاد المُنشأة؟**  
ج: بالتأكيد! استخدم فئة `Material` لتعيين الخامات وخصائص السطح.

**س: ما هي خيارات الترخيص المتاحة لـ Aspose.3D؟**  
ج: تتوفر نماذج ترخيص متعددة؛ يمكنك استكشافها [هنا](https://purchase.aspose.com/buy).

**س: كيف يمكنني الحصول على المساعدة أو مشاركة التجارب؟**  
ج: انضم إلى منتدى مجتمع Aspose.3D [هنا](https://forum.aspose.com/c/3d/18) للحصول على الدعم والنقاش.

**س: هل يتوفر ترخيص مؤقت للاختبار؟**  
ج: نعم، يمكن الحصول على ترخيص مؤقت للتقييم [هنا](https://purchase.aspose.com/temporary-license/).

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**آخر تحديث:** 2025-12-05  
**تم الاختبار مع:** Aspose.3D للغة Java 24.12 (الأحدث)  
**المؤلف:** Aspose