---
date: 2025-12-19
description: تعلم كيفية إنشاء مشهد ثلاثي الأبعاد وتصدير ملف OBJ ثلاثي الأبعاد باستخدام
  إزاحة الالتواء في البثق الخطي مع Aspose.3D للغة Java.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: إنشاء مشهد ثلاثي الأبعاد مع إزاحة الالتواء – Aspose.3D Java
url: /ar/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إنشاء مشهد ثلاثي الأبعاد مع Twist Offset – Aspose.3D for Java

## Introduction

في عالم الرسومات ثلاثية الأبعاد الديناميكي، تعلم كيفية **create 3d scene** مع البثق الخطي يُغيّر قواعد اللعبة. باستخدام Aspose.3D for Java، يمكنك رفع مستوى مهاراتك في النمذجة ثلاثية الأبعاد من خلال دمج ميزة Twist Offset في عملية البثق الخطي. سيوجهك هذا الدليل خلال خطوات استخدام Twist Offset في البثق الخطي باستخدام Aspose.3D for Java، موفرًا لك الأدوات لإنشاء مشاهد ثلاثية الأبعاد مذهلة.

## Quick Answers
- **What does Twist Offset do?** إنه يغيّر بداية الالتواء على طول مسار البثق، مما يمنحك مزيدًا من التحكم في الهندسة.  
- **Which file format is used for export?** المثال يحفظ النموذج كملف Wavefront OBJ (`.obj`).  
- **Do I need a license for development?** نسخة تجريبية مجانية تكفي للاختبار؛ يلزم الحصول على ترخيص تجاري للإنتاج.  
- **What Java version is required?** Java 8 أو أحدث.  
- **Can I change the number of slices?** نعم – تُحدد طريقة `setSlices` سلاسة الالتواء.

## Prerequisites

قبل الغوص في الدليل، تأكد من توفر المتطلبات التالية:

- **Java Environment:** تأكد من إعداد بيئة تطوير Java على نظامك.  
- **Aspose.3D for Java:** قم بتنزيل وتثبيت مكتبة Aspose.3D من [download link](https://releases.aspose.com/3d/java/).  
- **Documentation:** تعرّف على [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  

## Import Packages

في مشروع Java الخاص بك، استورد الحزم الضرورية لبدء استخدام Aspose.3D for Java. تأكد من تضمين المكتبات المطلوبة لتكامل سلس.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Step 1: Set Up the Environment

ابدأ بإعداد بيئة تطوير Java الخاصة بك والتأكد من تثبيت Aspose.3D for Java بشكل صحيح.

## Step 2: Initialize the Base Profile

أنشئ ملفًا أساسيًا للبثق، في هذه الحالة، `RectangleShape` بنصف قطر تقويمي قدره 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 3: Create a 3D Scene

أنشئ مشهدًا ثلاثيًا الأبعاد لاستضافة الكائنات المبعثرة.

```java
// Create a scene
Scene scene = new Scene();
```

## Step 4: Create Nodes

أنشئ عقد داخل المشهد لتمثيل كيانات مختلفة.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 5: Perform Linear Extrusion

استخدم البثق الخطي على كل من العقد اليسرى واليمنى مع خصائص مختلفة.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Step 6: Save the 3D Scene

احفظ المشهد الثلاثي الأبعاد الذي أنشأته حديثًا بالتنسيق المحدد.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## How to save 3d model and export 3d obj

استدعاء `scene.save` في الخطوة السابقة **يحفظ 3d model** كملف OBJ، وهو تنسيق **export 3d obj** مدعوم على نطاق واسع. يمكنك تغيير اسم الملف أو اختيار تنسيق مدعوم آخر (مثل STL، FBX) عن طريق تعديل تعداد `FileFormat`.

## Conclusion

تهانينا! لقد نفذت بنجاح Twist Offset في البثق الخطي باستخدام Aspose.3D for Java. تفتح هذه الميزة القوية عالمًا من الإمكانيات لمشاريع النمذجة ثلاثية الأبعاد الخاصة بك، مما يتيح لك **create 3d scene** بلفات وإزاحات معقدة، ثم **save 3d model** بتنسيق جاهز للأنابيب اللاحقة.

## FAQ's

### Q1: هل يمكنني استخدام Aspose.3D for Java في المشاريع غير التجارية؟

A1: نعم، يمكن استخدام Aspose.3D for Java في المشاريع التجارية وغير التجارية. راجع [licensing options](https://purchase.aspose.com/buy) للمزيد من التفاصيل.

### Q2: أين يمكنني العثور على الدعم لـ Aspose.3D for Java؟

A2: قم بزيارة [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18) للحصول على المساعدة والتواصل مع المجتمع.

### Q3: هل تتوفر نسخة تجريبية مجانية لـ Aspose.3D for Java؟

A3: نعم، يمكنك تجربة نسخة تجريبية مجانية من [releases page](https://releases.aspose.com/).

### Q4: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D for Java؟

A4: احصل على ترخيص مؤقت لمشروعك بزيارة [this link](https://purchase.aspose.com/temporary-license/).

### Q5: هل هناك أمثلة ودروس إضافية متاحة؟

A5: نعم، راجع [documentation](https://reference.aspose.com/3d/java/) لمزيد من الأمثلة والدروس المتعمقة.

## Frequently Asked Questions

**Q: هل هذا الدليل جزء من سلسلة دروس Aspose 3d؟**  
A: نعم – إنه **aspose 3d tutorial** رسمي يوضح ميزة محددة في المكتبة.

**Q: هل يمكنني استخدام شكل مختلف بدلاً من المستطيل؟**  
A: بالطبع. يمكن بث أي تنفيذ لـ `IProfile` (مثل `CircleShape` أو `PolygonShape` مخصص).

**Q: ماذا يحدث إذا تجاهلت `setTwistOffset`؟**  
A: سيبدأ البثق بالالتواء من أصل الملف، مما ينتج عنه التواء متماثل.

**Q: كيف يمكنني زيادة سلاسة الالتواء؟**  
A: زد القيمة الممررة إلى `setSlices`؛ عدد أكبر من الشرائح ينتج هندسة أكثر سلاسة.

**Q: ما هي صيغ الملفات الأخرى التي يمكن تصديرها بجانب OBJ؟**  
A: يدعم Aspose.3D صيغ STL، FBX، GLTF، 3MF، والعديد غيرها عبر تعداد `FileFormat`.

---

**Last Updated:** 2025-12-19  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## الكلمات المفتاحية المستهدفة:

**الكلمة المفتاحية الأساسية (أعلى أولوية):**  
create 3d scene  

**الكلمات المفتاحية الثانوية (الداعمة):**  
save 3d model, export 3d obj, aspose 3d tutorial