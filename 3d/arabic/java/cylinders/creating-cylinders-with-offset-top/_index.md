---
date: 2026-02-07
description: تعلم كيفية إنشاء نماذج أسطوانية ذات قمم مائلة في Aspose.3D للغة Java،
  إضافة خطوات عقدة فرعية في Java، وتصدير ملفات OBJ لنماذج 3D بسهولة.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: كيفية إنشاء أسطوانة ذات قمة مائلة في Aspose.3D للـ Java
url: /ar/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية إنشاء أسطوانة ذات قمة مُزاحة في Aspose.3D للغة Java

## المقدمة

إذا كنت تبحث عن **how to create cylinder** بأجسام ذات قمة مُزاحة مخصصة في مشهد ثلاثي الأبعاد مبني على Java، فإن Aspose.3D يجعل العملية مباشرة. في هذا الدرس سنمرّ بكل خطوة — من إعداد المشهد إلى تصدير النموذج النهائي كملف OBJ — حتى تتمكن من دمج الأسطوانات ذات القمة المُزاحة في تطبيقاتك بثقة. في نهاية الدليل ستتمكن من إتقان إنشاء أشكال أسطوانية بإزاحات مخصصة في بضع أسطر من الشيفرة فقط.

## إجابات سريعة
- **ما المكتبة المستخدمة؟** Aspose.3D for Java  
- **هل يمكنني إزاحة قمة الأسطوانة؟** نعم، باستخدام `setOffsetTop`  
- **كيف يمكنني إضافة عقدة فرعية في Java؟** استدعِ `createChildNode` على العقدة الجذرية  
- **ما الصيغة التي يمكنني التصدير إليها؟** Wavefront OBJ (`export 3d model obj`)  
- **هل أحتاج إلى ترخيص للاختبار؟** رخصة مؤقتة متاحة للتقييم  

## ما هو “how to create cylinder” مع قمة مُزاحة؟

إنشاء أسطوانة ذات قمة مُزاحة يعني أن الوجه الدائري العلوي يتم إزاحته بالنسبة للقاعدة، مما يتيح لك نمذجة أشكال مخروطية أو غير متماثلة دون تعديل القمم يدويًا. توفر Aspose.3D مُنشئًا مخصصًا وخصائص `OffsetTop` لتحقيق ذلك في بضع أسطر من الشيفرة فقط.

## لماذا نستخدم Aspose.3D للغة Java؟

- **واجهة برمجة تطبيقات عالية المستوى:** لا حاجة لإدارة بيانات الشبكة منخفضة المستوى.  
- **متعدد المنصات:** يعمل على أي بيئة متوافقة مع JVM.  
- **مصدرات مدمجة:** حفظ مباشرة إلى OBJ، STL، FBX، وأكثر.  
- **قابل للتوسيع:** يمكن بسهولة إضافة عقد فرعية، تطبيق التحويلات، والدمج مع مكتبات Java الأخرى.  

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من وجود ما يلي:

- **مجموعة تطوير جافا (JDK)** – نسخة متوافقة مثبتة.  
- **مكتبة Aspose.3D للغة Java** – حمّل أحدث ملف JAR من الموقع الرسمي [هنا](https://releases.aspose.com/3d/java/).  
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

### الخطوة 1: إنشاء مشهد

المشهد يعمل كحاوية لجميع الكائنات ثلاثية الأبعاد.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### الخطوة 2: تهيئة أسطوانة ذات قمة مُزاحة

هنا نجيب على **how to create cylinder** بإزاحة مخصصة. يحدد المُنشئ نصف القطر، الارتفاع، الشرائح، الطبقات، وما إذا كانت الأسطوانة مغلقة. بعد ذلك، نقوم بإزاحة القمة باستخدام `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### الخطوة 3: كيف **add child node Java** – إرفاق الأسطوانة الأولى

نُنشئ عقدة فرعية تحت العقدة الجذرية للمشهد وننقل الأسطوانة إلى الموقع المطلوب.

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

### الخطوة 5: كيف **add child node Java** – إرفاق الأسطوانة الثانية

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### الخطوة 6: كيف **export OBJ** – حفظ المشهد كملف OBJ

أخيرًا، نقوم بتصدير المشهد بالكامل (كلا الأسطوانتين) كملف Wavefront OBJ، وهو مدعوم على نطاق واسع من قبل أدوات 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

عند تشغيل البرنامج، ستجد الملف `CustomizedOffsetTopCylinder.obj` في الدليل المحدد، جاهزًا للفتح في Blender أو Maya أو أي عارض OBJ آخر.

## لماذا هذا مهم – حالات الاستخدام الواقعية

- **التصوير المعماري:** الأسطوانات ذات القمة المُزاحة مثالية لنمذجة الأعمدة التي تتناقص نحو السقف.  
- **الأجزاء الميكانيكية:** إنشاء مكابس أو أغطية تروس حيث يتم إزاحة السطح العلوي عمدًا.  
- **أصول الألعاب:** توليد سريع لأشكال أعمدة متنوعة دون الحاجة إلى إنشاء الشبكات يدويًا.  

## كيفية تصدير OBJ – حفظ المشهد كملف OBJ

تتيح قدرة Aspose 3D على تصدير OBJ مشاركة نماذجك مع أي خط أنابيب ثلاثي الأبعاد تقريبًا. باستخدام الطريقة `scene.save(..., FileFormat.WAVEFRONTOBJ)` يمكنك **how to export obj** مباشرة من Java، مما يلغي الحاجة إلى محولات طرف ثالث.

## كيفية إضافة عقدة فرعية Java – إرفاق الهندسة

إضافة العقد الفرعية هي الطريقة القياسية لتنظيم رسم المشهد. كل استدعاء لـ `createChildNode` يُعيد عقدة يمكن تحويلها بشكل مستقل، وهذا هو السبب في ظهور نمط **add child node java** مرتين في هذا الدرس.

## تصدير نموذج 3D كـ OBJ – باستخدام Aspose 3D Export OBJ

إذا كنت بحاجة لتوزيع نماذجك على المصممين، فإن ميزة **export 3d model obj** توفر تمثيلًا خفيفًا نصيًا يعمل عبر جميع تطبيقات 3D الرئيسية. استدعاء API نفسه المستخدم في الخطوة 6 يوضح سير عمل **aspose 3d export obj**.

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| **ملف OBJ فارغ** | المشهد لم يُحفظ بشكل صحيح أو المسار خاطئ. | تحقق من وجود دليل الإخراج وأن لديك أذونات كتابة. |
| **لم يتم تطبيق الإزاحة** | استخدام نسخة أقدم من Aspose.3D. | قم بالتحديث إلى أحدث مكتبة تدعم `setOffsetTop`. |
| **العقدة الفرعية غير مرئية** | لم يتم تطبيق التحويل. | تأكد من استدعاء `getTransform().setTranslation` بعد إنشاء العقدة الفرعية. |

## الأسئلة المتكررة

**س: هل Aspose.3D متوافق مع بيئات تطوير Java المختلفة؟**  
ج: نعم، يعمل بسلاسة مع Eclipse، IntelliJ IDEA، NetBeans، وغيرها من IDEs.

**س: هل يمكنني تطبيق القوام على الكائنات ثلاثية الأبعاد التي تم إنشاؤها؟**  
ج: بالطبع! استخدم الفئة `Material` لتعيين القوام وخصائص السطح.

**س: هل هناك خيارات ترخيص لـ Aspose.3D؟**  
ج: تتوفر نماذج ترخيص مختلفة؛ يمكنك استكشافها [هنا](https://purchase.aspose.com/buy).

**س: كيف يمكنني الحصول على المساعدة أو مشاركة التجارب؟**  
ج: انضم إلى منتدى مجتمع Aspose.3D [هنا](https://forum.aspose.com/c/3d/18) للحصول على الدعم والنقاش.

**س: هل تتوفر رخصة مؤقتة للاختبار؟**  
ج: نعم، يمكن الحصول على رخصة مؤقتة للتقييم [هنا](https://purchase.aspose.com/temporary-license/).

---

**آخر تحديث:** 2026-02-07  
**تم الاختبار مع:** Aspose.3D for Java 24.12 (latest)  
**المؤلف:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}