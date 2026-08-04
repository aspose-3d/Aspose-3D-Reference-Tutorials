---
date: 2026-04-08
description: تعلم كيفية إنشاء أسطوانة ذات قمة مُزاحة في Aspose.3D للغة Java، إضافة
  عقدة فرعية Java، ضبط القمة المُزاحة، إنشاء نموذج ثلاثي الأبعاد، وتصدير ملف OBJ باستخدام
  ترخيص مؤقت من Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: رخصة Aspose المؤقتة – إنشاء أسطوانة مع قمة مُزاحة (Java)
second_title: Aspose.3D Java API
title: رخصة Aspose المؤقتة – إنشاء أسطوانة مع قمة مُزاحة (جافا)
url: /ar/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# رخصة Aspose المؤقتة – إنشاء أسطوانة مع قمة مائلة (Java)

## مقدمة

إذا كنت تبحث عن **إنشاء أسطوانة** مع قمة مائلة مخصصة في مشهد ثلاثي الأبعاد يعتمد على Java، فإن Aspose.3D يجعل العملية بسيطة. في هذا البرنامج التعليمي سنستعرض كل خطوة — من إعداد المشهد إلى تصدير النموذج النهائي كملف OBJ — حتى تتمكن من دمج الأسطوانات ذات القمة المائلة في تطبيقاتك بثقة. بنهاية الدليل ستفهم أيضًا كيف تسمح لك **رخصة Aspose المؤقتة** بتقييم هذه الميزات دون الحاجة إلى شراء كامل.

## إجابات سريعة
- **ما المكتبة المستخدمة؟** Aspose.3D for Java  
- **هل يمكنني إزاحة قمة الأسطوانة؟** نعم، باستخدام `setOffsetTop`  
- **كيف أضيف عقدة فرعية في Java؟** استدعِ `createChildNode` على العقدة الجذرية  
- **ما الصيغة التي يمكنني التصدير إليها؟** Wavefront OBJ (`java export obj`)  
- **هل أحتاج إلى رخصة للاختبار؟** **رخصة Aspose المؤقتة** متاحة للتقييم  

## ما هي رخصة Aspose المؤقتة؟

**رخصة Aspose المؤقتة** هي مفتاح تقييم قصير‑الأمد ومجاني يفتح مجموعة الميزات الكاملة لـ Aspose.3D for Java أثناء التطوير والاختبار. تُزيل العلامات المائية التجريبية وتسمح لك بإنشاء ملفات نماذج ثلاثية الأبعاد، مثل OBJ أو STL أو FBX، تمامًا كما تفعل الرخصة المدفوعة.

## لماذا تستخدم Aspose.3D للـ Java؟

- **API عالي المستوى:** لا حاجة لإدارة بيانات الشبكة منخفضة المستوى.  
- **متعدد المنصات:** يعمل على أي بيئة متوافقة مع JVM.  
- **مصدرات مدمجة:** حفظ مباشرة إلى OBJ، STL، FBX، وأكثر.  
- **قابل للتوسيع:** يمكن بسهولة إضافة عقد فرعية، تطبيق التحويلات، والدمج مع مكتبات Java الأخرى.  

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من وجود ما يلي:

- **مجموعة تطوير Java (JDK)** – نسخة متوافقة مثبتة.  
- **مكتبة Aspose.3D للـ Java** – حمّل أحدث JAR من الموقع الرسمي [here](https://releases.aspose.com/3d/java/).  
- بيئة تطوير متكاملة (IDE) من اختيارك (Eclipse، IntelliJ IDEA، NetBeans، إلخ).  

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

### الخطوة 1: إنشاء مشهد Java 3D

يعمل **مشهد Java 3D** كحاوية لجميع الكائنات ثلاثية الأبعاد.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### الخطوة 2: تهيئة أسطوانة مع قمة مائلة

هنا نجيب على **كيفية إنشاء أسطوانة** مع إزاحة مخصصة. يحدد المُنشئ نصف القطر والارتفاع والشرائح والطبقات وما إذا كانت الأسطوانة مغلقة. بعد ذلك، نقوم بتحريك القمة باستخدام `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### الخطوة 3: إضافة عقدة فرعية Java – إرفاق الأسطوانة الأولى

ننشئ عقدة فرعية تحت العقدة الجذرية للمشهد وننقل الأسطوانة إلى الموقع المطلوب.

```java
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

### الخطوة 5: إضافة عقدة فرعية Java – إرفاق الأسطوانة الثانية

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### الخطوة 6: تصدير Java إلى OBJ – حفظ المشهد كملف OBJ

أخيرًا، نقوم **java export obj** للمشهد بالكامل (كلا الأسطوانتين) كملف Wavefront OBJ، وهو مدعوم على نطاق واسع من قبل أدوات 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

عند تشغيل البرنامج، ستجد الملف `CustomizedOffsetTopCylinder.obj` في الدليل المحدد، جاهزًا للفتح في Blender أو Maya أو أي عارض OBJ آخر.

## كيفية إنشاء نموذج ثلاثي الأبعاد وتصدير OBJ في Java

يجمع استخدام `Scene.save(..., FileFormat.WAVEFRONTOBJ)` مع **رخصة Aspose المؤقتة** لتتيح لك **إنشاء نموذج ثلاثي الأبعاد** بسرعة، دون الحاجة إلى محولات خارجية. هذا مفيد بشكل خاص أثناء النمذجة الأولية أو عند مشاركة الأصول مع المصممين.

## حالات الاستخدام الواقعية

- **التصوير المعماري:** أسطوانات ذات قمة مائلة تمثل أعمدة تتناقص نحو السقف.  
- **الأجزاء الميكانيكية:** إنشاء مكابس أو حاويات تروس حيث يتم إزاحة السطح العلوي عمدًا.  
- **أصول الألعاب:** إنتاج أشكال أعمدة متنوعة بسرعة، مما يقلل الحاجة إلى نماذج يدوية الصنع.  

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| **ملف OBJ فارغ** | لم يتم حفظ المشهد بشكل صحيح أو المسار غير صحيح. | تحقق من وجود دليل الإخراج وأن لديك أذونات كتابة. |
| **لم يتم تطبيق الإزاحة** | استخدام نسخة قديمة من Aspose.3D. | قم بتحديث المكتبة إلى أحدث نسخة تدعم `setOffsetTop`. |
| **العقدة الفرعية غير مرئية** | لم يتم تطبيق التحويل. | تأكد من استدعاء `getTransform().setTranslation` بعد إنشاء العقدة الفرعية. |

## الأسئلة المتكررة

**س: هل Aspose.3D متوافق مع بيئات تطوير Java المختلفة؟**  
**ج:** نعم، يعمل بسلاسة مع Eclipse، IntelliJ IDEA، NetBeans، وغيرها من بيئات التطوير.

**س: هل يمكنني تطبيق القوام على الكائنات ثلاثية الأبعاد التي تم إنشاؤها؟**  
**ج:** بالتأكيد! استخدم الفئة `Material` لتعيين القوام وخصائص السطح.

**س: هل هناك خيارات ترخيص لـ Aspose.3D؟**  
**ج:** تتوفر نماذج ترخيص مختلفة؛ يمكنك استكشافها [here](https://purchase.aspose.com/buy).

**س: كيف يمكنني الحصول على مساعدة أو مشاركة التجارب؟**  
**ج:** انضم إلى منتدى مجتمع Aspose.3D [here](https://forum.aspose.com/c/3d/18) للحصول على الدعم والنقاش.

**س: هل تتوفر رخصة مؤقتة للاختبار؟**  
**ج:** نعم، يمكن الحصول على **رخصة Aspose المؤقتة** للتقييم [here](https://purchase.aspose.com/temporary-license/).

---

**آخر تحديث:** 2026-04-08  
**تم الاختبار مع:** Aspose.3D for Java 24.12 (latest)  
**المؤلف:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}