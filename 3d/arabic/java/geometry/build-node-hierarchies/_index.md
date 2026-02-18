---
date: 2026-02-09
description: تعلم كيفية تصدير FBX وإضافة شبكة إلى العقدة أثناء إنشاء عقد فرعية في
  جافا باستخدام Aspose.3D.
linktitle: Build Node Hierarchies in 3D Scenes with Java and Aspose.3D
second_title: Aspose.3D Java API
title: كيفية تصدير FBX وبناء هياكل العقد في جافا
url: /ar/java/geometry/build-node-hierarchies/
weight: 16
---

Now produce final content with all translations.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تصدير FBX وبناء هياكل العقد في Java باستخدام Aspose.3D

## المقدمة

إذا كنت تبحث عن دليل واضح خطوة بخطوة حول **how to export FBX** من تطبيق Java، فأنت في المكان المناسب. في هذا البرنامج التعليمي سنوضح لك كيفية بناء هياكل العقد، **add mesh to node**، وأخيرًا حفظ المشهد كملف FBX باستخدام Aspose.3D Java API. سواءً كنت تنشئ نموذجًا أوليًا بسيطًا أو محركًا ثلاثي الأبعاد جاهزًا للإنتاج، ستمنحك هذه التقنيات تحكمًا كاملًا في مخطط المشهد.

## إجابات سريعة
- **What is the primary purpose of this tutorial?** توضيح كيفية تصدير FBX بعد بناء هياكل العقد.  
- **Which library is used?** Aspose.3D for Java.  
- **Do I need a license?** نسخة تجريبية مجانية تكفي للتطوير؛ يلزم الحصول على ترخيص تجاري للإنتاج.  
- **What file format is produced?** FBX (ASCII 7500).  
- **Can I customize node transformations?** نعم – الترجمة، الدوران، والتحجيم مدعومة جميعًا.

## ما هو “how to export FBX” في سياق Aspose.3D؟

تصدير FBX يعني تحويل مخطط المشهد الموجود في الذاكرة والذي تبنيه باستخدام Aspose.3D إلى ملف FBX يمكن فتحه في أدوات ثلاثية الأبعاد شائعة مثل Blender أو Maya أو Unity. تتولى الـ API الجزء الأكبر من العمل، مما يتيح لك التركيز على إنشاء المشهد.

## لماذا بناء هياكل العقد قبل التصدير؟

تتيح لك هياكل العقد المنظمة جيدًا تطبيق التحولات مرة واحدة على العقدة الأم، مما يؤثر تلقائيًا على جميع العقد التابعة لها. هذا يقلل من تكرار الشيفرة ويعكس علاقات الكائنات في العالم الحقيقي (مثلاً هيكل سيارة مع العجلات كعقد فرعية).

## المتطلبات المسبقة

قبل الغوص في التفاصيل، تأكد من وجود ما يلي:

1. **Java Development Environment** – JDK 8+ وبيئة تطوير متكاملة أو أداة بناء حسب اختيارك.  
2. **Aspose.3D for Java Library** – قم بتنزيل وتثبيت المكتبة من [صفحة التحميل](https://releases.aspose.com/3d/java/).  
3. **Document Directory** – مجلد على جهازك حيث سيتم حفظ ملف FBX المُنشأ.

## استيراد الحزم

ابدأ باستيراد الفئات الضرورية من Aspose.3D:

```java
import com.aspose.threed.*;

```

## الخطوة 1: تهيئة كائن المشهد

```java
// Initialize scene object
Scene scene = new Scene();
```

## الخطوة 2: إنشاء عقد فرعية وإضافة شبكة إلى العقدة

في هذه الخطوة نوضح **how to create child nodes** و **add mesh to node**.

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Use your mesh creation method
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## الخطوة 3: تطبيق الدوران على العقدة العليا

تدوير العقدة الأم يدور تلقائيًا جميع العقد التابعة لها، وهو ميزة أساسية للمشاهد الهرمية.

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## الخطوة 4: حفظ المشهد ثلاثي الأبعاد – How to Export FBX

الآن ن **save scene as FBX**، مُكملين سير عمل “how to export FBX”.

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

### النتيجة المتوقعة
تشغيل الشيفرة ينشئ ملفًا باسم **NodeHierarchy.fbx** في الدليل المحدد. افتحه في أي عارض يدعم FBX لرؤية مكعبين موضعين إلى اليسار واليمين من محور مركزي، جميعهما يدور معًا.

## المشكلات الشائعة والحلول

| المشكلة | سبب حدوثها | الحل |
|-------|----------------|-----|
| **File not found** error when saving | مسار `MyDir` غير صحيح أو يفتقد الفاصل النهائي | تأكد من وجود الدليل وانتهائه بفاصل ملف (`/` أو `\\`). |
| **Mesh not visible** after export | كيان الشبكة غير مُعيّن أو الترجمة تحركه خارج نطاق الرؤية | تحقق من `cube1.setEntity(mesh)` وتفقد قيم الترجمة. |
| **Rotation looks wrong** | استخدام الراديان بدلاً من الدرجات بشكل غير صحيح | `Quaternion.fromEulerAngle` يتوقع راديان؛ عدّل القيم وفقًا لذلك. |

## الأسئلة المتكررة

**س: هل Aspose.3D for Java مناسب للمبتدئين؟**  
ج: بالطبع! تم تصميم الـ API بنهج نظيف وموجه كائنًا يجعل تعلمه سهلًا، حتى لو كنت جديدًا في برمجة ثلاثية الأبعاد.

**س: هل يمكنني استخدام Aspose.3D for Java في المشاريع التجارية؟**  
ج: نعم، يمكنك ذلك. زر [صفحة الشراء](https://purchase.aspose.com/buy) للحصول على تفاصيل الترخيص.

**س: كيف يمكنني الحصول على الدعم لـ Aspose.3D for Java؟**  
ج: انضم إلى [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة من المجتمع وفريق دعم Aspose.

**س: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج: بالتأكيد! استكشف الميزات عبر [الإصدار التجريبي المجاني](https://releases.aspose.com/) قبل اتخاذ القرار.

**س: أين يمكنني العثور على الوثائق؟**  
ج: راجع [الوثائق](https://reference.aspose.com/3d/java/) للحصول على معلومات مفصلة حول Aspose.3D for Java.

## الخاتمة

إتقان **how to export FBX**، بناء هياكل العقد، و **add mesh to node** هي خطوات أساسية نحو إنشاء تطبيقات ثلاثية الأبعاد متقدمة في Java. مع Aspose.3D تحصل على حل قوي وصديق للترخيص يُجرد التفاصيل منخفضة المستوى مع منحك تحكمًا كاملًا في مخطط المشهد. جرّب شبكات مختلفة، وتحولات، وصيغ تصدير لاكتشاف إمكانيات إضافية.

**آخر تحديث:** 2026-02-09  
**تم الاختبار مع:** Aspose.3D for Java 24.11  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}