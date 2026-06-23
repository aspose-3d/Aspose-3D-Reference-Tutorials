---
date: 2026-06-23
description: تعرف على كيفية إنشاء عقد فرعية، إضافة شبكة إلى العقدة، وتصدير FBX باستخدام
  إمكانيات java 3d scene graph في Aspose.3D Java API.
keywords:
- java 3d scene graph
- how to export fbx
- add mesh to node
- how to create child nodes
- save scene as fbx
- convert scene to fbx
linktitle: بناء هياكل العقد في المشاهد ثلاثية الأبعاد باستخدام Java و Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-06-23'
  description: Learn how to create child nodes, add mesh to node, and export FBX using
    the java 3d scene graph capabilities of Aspose.3D Java API.
  headline: 'java 3d scene graph: Create Child Nodes and Export FBX in Java with Aspose.3D'
  type: TechArticle
- description: Learn how to create child nodes, add mesh to node, and export FBX using
    the java 3d scene graph capabilities of Aspose.3D Java API.
  name: 'java 3d scene graph: Create Child Nodes and Export FBX in Java with Aspose.3D'
  steps:
  - name: '**Java Development Environment** – JDK 8+ and an IDE or build tool of your
      choice.'
    text: '**Java Development Environment** – JDK 8+ and an IDE or build tool of your
      choice.'
  - name: '**Aspose.3D for Java Library** – Download and install the library from
      the [download page](https://releases.aspose.com/3d/java/).'
    text: '**Aspose.3D for Java Library** – Download and install the library from
      the [download page](https://releases.aspose.com/3d/java/).'
  - name: '**Document Directory** – A folder on your machine where the generated FBX
      file will be saved.'
    text: '**Document Directory** – A folder on your machine where the generated FBX
      file will be saved.'
  type: HowTo
- questions:
  - answer: Absolutely! The API is designed with a clean, object‑oriented approach
      that makes it easy to learn, even if you’re new to 3D programming.
    question: Is Aspose.3D for Java suitable for beginners?
  - answer: Yes, you can. Visit the [purchase page](https://purchase.aspose.com/buy)
      for licensing details.
    question: Can I use Aspose.3D for Java for commercial projects?
  - answer: Join the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) to get assistance
      from the community and Aspose support team.
    question: How can I get support for Aspose.3D for Java?
  - answer: Certainly! Explore the features with the [free trial](https://releases.aspose.com/)
      before making a commitment.
    question: Is there a free trial available?
  - answer: Refer to the [documentation](https://reference.aspose.com/3d/java/) for
      detailed information on Aspose.3D for Java.
    question: Where can I find the documentation?
  type: FAQPage
second_title: Aspose.3D Java API
title: 'java 3d scene graph: إنشاء عقد فرعية وتصدير FBX في Java باستخدام Aspose.3D'
url: /ar/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}

## الدروس ذات الصلة

- [Create Mesh Aspose Java – Transform 3D Nodes with Euler Angles](/3d/java/geometry/transform-3d-nodes-with-euler-angles/)
- [Create 3D Scene Java - Apply PBR Materials with Aspose.3D](/3d/java/geometry/apply-pbr-materials-to-objects/)
- [How to Export Scene to FBX and Retrieve 3D Scene Info in Java](/3d/java/3d-scenes-and-models/get-scene-information/)


{{< /blocks/products/pf/tutorial-page-section >}}  
{{< blocks/products/pf/tutorial-page-section >}}  

# كيفية تصدير FBX وبناء هياكل العقد في Java باستخدام Aspose.3D  

## المقدمة  

إذا كنت تبحث عن دليل واضح خطوة بخطوة حول **إنشاء عقد فرعية**، **إضافة شبكة إلى عقدة**، و**كيفية تصدير FBX** من تطبيق Java، فأنت في المكان الصحيح. في هذا الدرس سنستعرض بناء **رسم مشهد 3D في Java**، ربط الشبكات، تطبيق التحولات، وأخيرًا حفظ المشهد كملف FBX باستخدام Aspose.3D Java API. سواء كنت تصمم نموذجًا تجريبيًا بسيطًا أو تطور محرك 3D جاهز للإنتاج، فإن إتقان هذه المفاهيم يمنحك تحكمًا كاملًا في هيكلية المشهد وتدفق عملية التصدير.  

## إجابات سريعة  
- **ما هو الهدف الأساسي من هذا الدرس؟** توضيح كيفية **إنشاء عقد فرعية**، ربط الشبكات، و**تصدير FBX** بعد بناء هيكلية العقد.  
- **ما المكتبة المستخدمة؟** Aspose.3D for Java.  
- **هل أحتاج إلى ترخيص؟** النسخة التجريبية المجانية تكفي للتطوير؛ الترخيص التجاري مطلوب للإنتاج.  
- **ما صيغة الملف الناتج؟** FBX (ASCII 7500).  
- **هل يمكن تخصيص تحولات العقد؟** نعم – يدعم الترجمة، الدوران، والتحجيم.  

## ما هو رسم مشهد 3D في Java؟  

**رسم مشهد 3D في Java** هو بنية بيانات هرمية تمثل الكائنات (`Node`s) وعلاقاتها في عالم ثلاثي الأبعاد. من خلال تنظيم الكائنات كأزواج أب‑ابن، يمكنك تطبيق تحول واحد على الأصل وينتقل إلى جميع الفروع، مما يبسط الرسوم المتحركة وإدارة المشهد.  

## لماذا نبني هياكل العقد قبل التصدير؟  

هيكلية منظمة جيدًا تقلل من تكرار الشيفرة، تبسط الرسوم المتحركة، وتعكس العلاقات الواقعية. عندما تقوم لاحقًا **بتحويل المشهد إلى FBX** (أو أي صيغة أخرى)، تُحافظ الهيكلية على علاقات الأب‑ابن، مما يسمح للأدوات مثل Blender، Maya، أو Unity بفهمها بدقة كما صممتها.  

## الفوائد الكمية لـ Aspose.3D  

يدعم Aspose.3D **أكثر من 30 صيغة استيراد وتصدير** – بما فيها FBX، OBJ، STL، 3DS، وCollada – ويمكنه معالجة **مشاهد مئات الصفحات** دون تحميل الملف بالكامل إلى الذاكرة. المكتبة تعرض الشبكات بسرعة تصل إلى **60 إطارًا في الثانية** على الأجهزة العادية، مما يتيح معاينة فورية أثناء التطوير.  

## حالات الاستخدام الشائعة لهياكل العقد  

| حالة الاستخدام | لماذا تساعد الهيكلية | النتيجة المتوقعة |
|----------|----------------------|-----------------|
| **تجميعات ميكانيكية** (مثل ذراع روبوت) | دوران العقدة الأساسية يحرك جميع الأجزاء المرفقة | رسوم متحركة سهلة للآليات المعقدة |
| **هياكل الشخصيات** | عظام الهيكل هي عقد فرعية للجذر | تحولات وضعية متسقة |
| **تنظيم المشهد** | تجميع العناصر الثابتة تحت عقدة “props” | إدارة مشهد أنظف وتصدير انتقائي |
| **تبديل مستوى التفاصيل (LOD)** | عقدة الأصل تتحكم في إظهار/إخفاء الشبكات الفرعية | تحسين العرض لأجهزة مختلفة |

## المتطلبات المسبقة  

1. **بيئة تطوير Java** – JDK 8+ وأي IDE أو أداة بناء تفضلها.  
2. **مكتبة Aspose.3D for Java** – حمّل وثبت المكتبة من [صفحة التحميل](https://releases.aspose.com/3d/java/).  
3. **دليل المستندات** – مجلد على جهازك سيُحفظ فيه ملف FBX المُولد.  

## استيراد الحزم  

مساحة الاسم `com.aspose.threed` توفر جميع الفئات التي تحتاجها لإنشاء المشهد، معالجة العقد، وتصدير الملفات. استورد الحزم التالية قبل البدء:  

```java
import com.aspose.threed.*;
```  

## الخطوة 1: تهيئة كائن المشهد  

فئة `Scene` هي الحاوية العليا التي تحتفظ بالهرمية ثلاثية الأبعاد بالكامل. إنشاء نسخة من `Scene` يخصص عقدة الجذر ويجهز الهياكل الداخلية للشبكات، الأضواء، والكاميرات.  

```java
// Initialize scene object
Scene scene = new Scene();
```  

## الخطوة 2: إنشاء عقد فرعية وإضافة شبكة إلى العقدة  

في هذه الخطوة نوضح **كيفية إنشاء عقد فرعية** و**إضافة شبكة إلى عقدة**. فئة `Node` تمثل عنصرًا واحدًا في الهرمية، بينما فئة `Mesh` تخزن بيانات الهندسة مثل الرؤوس والوجوه.  

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

## الخطوة 3: تطبيق دوران على العقدة العليا  

دوران العقدة الأصلية يدور تلقائيًا جميع أبنائها، وهو ميزة أساسية للمشاهد الهرمية. استخدم فئة `Quaternion` لتعريف الدوران بالراديان للحصول على استيفاء سلس.  

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```  

## الخطوة 4: حفظ المشهد ثلاثي الأبعاد – كيفية تصدير FBX  

الآن **نحفظ المشهد كملف FBX**، مكملين سير عمل “كيفية تصدير FBX”. طريقة `Scene.save` تقبل مسار الملف وتعداد `FileFormat`، مما يتيح لك اختيار بين FBX 2013، FBX 2014، أو أحدث صيغة ASCII 7500.  
تعداد `FileFormat` يدرج صيغ التصدير المدعومة مثل FBX2013، FBX2014، وASCII 7500.  

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```  

### النتيجة المتوقعة  

تشغيل الشيفرة ينشئ ملفًا باسم **NodeHierarchy.fbx** في الدليل المحدد. افتحه في أي عارض يدعم FBX لتشاهد مكعبين موضعين إلى اليسار واليمين من محور مركزي، يدوران معًا.  

## المشكلات الشائعة والحلول  

| المشكلة | السبب | الحل |
|-------|--------|-----|
| **خطأ “الملف غير موجود”** عند الحفظ | مسار `MyDir` غير صحيح أو يفتقد الفاصل النهائي | تأكد من وجود المجلد وانتهائه بفاصل ملف (`/` أو `\\`). |
| **الشبكة غير مرئية** بعد التصدير | لم يتم تعيين كيان الشبكة أو الترجمة نقلها خارج نطاق الرؤية | تحقق من `cube1.setEntity(mesh)` وتأكد من قيم الترجمة. |
| **الدوران غير صحيح** | استخدام راديان بدلاً من درجات أو العكس | `Quaternion.fromEulerAngle` يتوقع راديان؛ عدّل القيم وفقًا لذلك. |

## نصائح استكشاف الأخطاء وإصلاحها  

- **تحقق من الدليل**: استخدم `new File(MyDir).mkdirs();` قبل `scene.save` إذا كان المجلد قد لا يكون موجودًا.  
- **افحص رسم المشهد**: استدعِ `scene.getRootNode().getChildren().size()` لتؤكد إضافة العقد الفرعية.  
- **تحقق من توافق نسخة FBX**: بعض الأدوات القديمة تدعم فقط FBX 2013؛ يمكنك تغيير الصيغة إلى `FileFormat.FBX2013` إذا لزم الأمر.  

## الأسئلة المتكررة  

**س: هل Aspose.3D for Java مناسب للمبتدئين؟**  
ج: بالتأكيد! تم تصميم الـ API بنهج كائني واضح يجعل تعلمه سهلًا حتى إذا كنت جديدًا على برمجة 3D.  

**س: هل يمكنني استخدام Aspose.3D for Java في مشاريع تجارية؟**  
ج: نعم. زر [صفحة الشراء](https://purchase.aspose.com/buy) للحصول على تفاصيل الترخيص.  

**س: كيف أحصل على دعم لـ Aspose.3D for Java؟**  
ج: انضم إلى [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة من المجتمع وفريق الدعم.  

**س: هل تتوفر نسخة تجريبية مجانية؟**  
ج: بالطبع! استكشف الميزات عبر [التجربة المجانية](https://releases.aspose.com/) قبل اتخاذ قرار.  

**س: أين يمكنني العثور على الوثائق؟**  
ج: راجع [الوثائق](https://reference.aspose.com/3d/java/) للحصول على معلومات مفصلة حول Aspose.3D for Java.  

## الخاتمة  

إتقان **إنشاء عقد فرعية**، **إضافة شبكة إلى عقدة**، و**كيفية تصدير FBX** خطوات أساسية لبناء تطبيقات 3D متقدمة في Java. مع Aspose.3D تحصل على حل قوي ومرن يخفف التفاصيل منخفضة المستوى مع إتاحة التحكم الكامل في رسم المشهد ثلاثي الأبعاد. جرّب شبكات مختلفة، تحولات، وصيغ تصدير لاكتشاف إمكانيات إضافية.  

---  

**آخر تحديث:** 2026-06-23  
**تم الاختبار مع:** Aspose.3D for Java 24.11  
**المؤلف:** Aspose  

{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-container >}}