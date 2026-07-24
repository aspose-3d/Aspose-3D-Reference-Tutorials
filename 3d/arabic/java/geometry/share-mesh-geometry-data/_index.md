---
date: 2026-05-19
description: تعلم كيفية تحويل mesh إلى FBX مع تعيين لون المادة ومشاركة بيانات هندسة
  mesh في Java 3D باستخدام Aspose.3D.
keywords:
- convert mesh to fbx
- how to export fbx
- how to set material
- export mesh to fbx
- aspose 3d tutorial
linktitle: تحويل Mesh إلى FBX وتعيين لون المادة في Java 3D
schemas:
- author: Aspose
  dateModified: '2026-05-19'
  description: Learn how to convert mesh to FBX while setting material color and sharing
    mesh geometry data in Java 3D using Aspose.3D.
  headline: Convert Mesh to FBX and Set Material Color in Java 3D
  type: TechArticle
- questions:
  - answer: Yes, the shared mesh can be animated via skeletal rigs or morph targets
      while each node retains its own material.
    question: Can I reuse the same mesh for animated characters?
  - answer: Absolutely, Aspose.3D writes full UV data, so textures map correctly in
      downstream tools.
    question: Does the FBX export preserve UV coordinates?
  - answer: The library can stream meshes exceeding 2 GB without loading the entire
      file into memory, making it suitable for large scenes.
    question: What is the maximum file size Aspose.3D can handle?
  - answer: Pass a different `FileFormat` enum value, such as `FileFormat.FBX201400ASCII`,
      to `scene.save`.
    question: How do I change the FBX version?
  - answer: Yes, you can create a new `Scene`, add the desired nodes, and then save
      that scene to FBX.
    question: Is it possible to export only a subset of nodes?
  type: FAQPage
second_title: Aspose.3D Java API
title: تحويل Mesh إلى FBX وتعيين لون المادة في Java 3D
url: /ar/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تحويل الشبكة إلى FBX وتعيين لون المادة في Java 3D

## المقدمة

إذا كنت تبني تطبيقًا ثلاثي الأبعاد يعتمد على Java، فستحتاج غالبًا إلى إعادة استخدام نفس الهندسة عبر عدة كائنات مع إعطاء كل نسخة مظهرًا فريدًا. في هذا الدرس ستتعلم **how to convert mesh to FBX**, مشاركة هندسة الشبكة الأساسية بين عدة عقد, و**set a different material color for each node**. في النهاية ستحصل على مشهد FBX جاهز للتصدير يمكنك إدراجه في أي محرك أو عارض.

## إجابات سريعة
- **ما هو الهدف الرئيسي؟** تحويل الشبكة إلى FBX، مشاركة هندسة الشبكة، وتعيين لون مادة مميز لكل عقدة.  
- **ما المكتبة المطلوبة؟** Aspose.3D for Java.  
- **كيف يمكنني تصدير النتيجة؟** احفظ المشهد كملف FBX باستخدام `FileFormat.FBX7400ASCII`.  
- **هل أحتاج إلى ترخيص؟** يلزم ترخيص مؤقت أو كامل للاستخدام في الإنتاج.  
- **ما نسخة Java التي تعمل؟** أي بيئة Java 8+.

## ما هو **convert mesh to FBX**؟

تحويل الشبكة إلى FBX يعني أخذ كائن شبكة موجود في الذاكرة وكتابته إلى تنسيق ملف FBX، وهو معيار فعلي مدعوم من Maya وBlender وUnity والعديد من أدوات 3D الأخرى. تقوم Aspose.3D بالعمل الشاق، لذا كل ما عليك هو استدعاء `scene.save(...)` مع `FileFormat` المناسب.

## لماذا مشاركة بيانات هندسة الشبكة؟

مشاركة الهندسة تقلل من استهلاك الذاكرة وتسرع عملية العرض لأن مخازن الرؤوس الأساسية تُخزن مرة واحدة فقط. هذه التقنية مثالية للمشاهد التي تحتوي على العديد من الكائنات المكررة—مثل الغابات، الحشود، أو الهندسة المعمارية المعيارية—حيث يختلف كل نسخة فقط في التحويل أو المادة.

## المتطلبات المسبقة

- **بيئة تطوير Java** – أي IDE أو إعداد سطر أوامر مع Java 8 أو أحدث.  
- **مكتبة Aspose.3D** – قم بتنزيل أحدث JAR من الموقع الرسمي: [هنا](https://releases.aspose.com/3d/java/).

## استيراد الحزم

مساحة الاسم `com.aspose.threed` تحتوي على جميع الفئات التي ستحتاجها لبناء المشاهد، الشبكات، والمواد. استورد هذه الحزم في أعلى ملف Java الخاص بك حتى يتمكن المترجم من التعرف على الأنواع.

```java
import com.aspose.threed.*;
```

## الخطوة 1: تهيئة كائن المشهد (initialize scene java)

الفئة `Scene` هي الحاوية العليا في Aspose.3D التي تمثل عالمًا ثلاثي الأبعاد كاملًا. تهيئة `Scene` يمنحك لوحة قماش نظيفة يمكن إضافة الشبكات والإضاءة والكاميرات إليها.

```java
// Initialize scene object
Scene scene = new Scene();
```

## الخطوة 2: تعريف متجهات اللون

`Vector3` تمثل متجهًا ثلاثيًا (X, Y, Z) يُستخدم للمواقع أو الاتجاهات أو الألوان.  
أنشئ مصفوفة من كائنات `Vector3` التي تحمل قيم RGB. سيتم لاحقًا تعيين كل متجه إلى عقدة منفصلة، مما يمنح كل نسخة لونها الخاص.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## الخطوة 3: إنشاء شبكة 3D Java باستخدام Polygon Builder (create 3d mesh java)

الفئة `PolygonBuilder` تتيح لك بناء شبكة عن طريق تعريف الرؤوس والوجوه يدويًا. ستُعاد استخدام هذه الشبكة عبر جميع العقد، مما يوضح كيفية عمل مشاركة الهندسة عمليًا.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## كيفية تعيين لون المادة لكل عقدة؟

`LambertMaterial` هو نوع مادة بسيط يحدد اللون المنتشر لشبكة.  
قم بالتكرار عبر متجهات اللون، أنشئ عقدة مكعب لكل مدخل، عيّن `LambertMaterial` جديد باللون الحالي، وضع العقدة باستخدام مصفوفة تحويل. يضمن هذا النمط أن كل عقدة تعرض لونًا فريدًا مع الاستمرار في الإشارة إلى نفس الشبكة الأساسية.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## الخطوة 5: حفظ المشهد ثلاثي الأبعاد (save scene fbx, convert mesh to fbx)

حدد الدليل واسم الملف لحفظ المشهد ثلاثي الأبعاد بالتنسيق المدعوم، في هذه الحالة FBX7400ASCII. تُظهر هذه الخطوة أيضًا **convert mesh to FBX** عن طريق حفظ المشهد المشترك إلى القرص.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## مشكلات شائعة ونصائح

- **مشكلات المسار** – تأكد من أن مسار الدليل ينتهي بفاصل ملف (`/` أو `\\`) قبل إلحاق اسم الملف.  
- **تهيئة الترخيص** – إذا نسيت ضبط ترخيص Aspose.3D قبل استدعاء `scene.save`, سيعمل المكتبة في وضع التجربة وقد تدرج علامة مائية.  
- **استبدال المادة** – إعادة استخدام نفس مثيل `LambertMaterial` لعدة عقد سيؤدي إلى مشاركة جميع العقد لنفس اللون. احرص دائمًا على إنشاء مادة جديدة لكل تكرار، كما هو موضح أعلاه.  
- **الشبكات الكبيرة** – بالنسبة للشبكات التي تحتوي على ملايين الرؤوس، فكر في استخدام `MeshBuilder` مع مضلعات مفهرسة للحفاظ على حجم ملف FBX قابلًا للإدارة.

## أسئلة شائعة إضافية

**س1: هل يمكنني استخدام Aspose.3D مع أطر Java أخرى؟**  
ج1: نعم، تم تصميم Aspose.3D للعمل بسلاسة مع مختلف أطر Java.

**س2: هل هناك خيارات ترخيص متاحة لـ Aspose.3D؟**  
ج2: نعم، يمكنك استكشاف خيارات الترخيص [هنا](https://purchase.aspose.com/buy).

**س3: كيف يمكنني الحصول على دعم لـ Aspose.3D؟**  
ج3: زر منتدى Aspose.3D [المنتدى](https://forum.aspose.com/c/3d/18) للحصول على الدعم والنقاشات.

**س4: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج4: نعم، يمكنك الحصول على نسخة تجريبية مجانية [هنا](https://releases.aspose.com/).

**س5: كيف أحصل على ترخيص مؤقت لـ Aspose.3D؟**  
ج5: يمكنك الحصول على ترخيص مؤقت [هنا](https://purchase.aspose.com/temporary-license/).

## الأسئلة الشائعة

**س: هل يمكنني إعادة استخدام نفس الشبكة للشخصيات المتحركة؟**  
ج: نعم، يمكن تحريك الشبكة المشتركة عبر هياكل عظام أو أهداف تشويه بينما يحتفظ كل عقدة بمادتها الخاصة.

**س: هل يحافظ تصدير FBX على إحداثيات UV؟**  
ج: بالتأكيد، تقوم Aspose.3D بكتابة بيانات UV كاملة، لذا تُطَبَّق القوام بشكل صحيح في الأدوات اللاحقة.

**س: ما هو الحد الأقصى لحجم الملف الذي يمكن لـ Aspose.3D التعامل معه؟**  
ج: يمكن للمكتبة بث الشبكات التي تتجاوز 2 GB دون تحميل الملف بالكامل إلى الذاكرة، مما يجعلها مناسبة للمشاهد الكبيرة.

**س: كيف أغيّر نسخة FBX؟**  
ج: مرّر قيمة مختلفة من تعداد `FileFormat`، مثل `FileFormat.FBX201400ASCII`، إلى `scene.save`.

**س: هل يمكن تصدير مجموعة فرعية فقط من العقد؟**  
ج: نعم، يمكنك إنشاء `Scene` جديد، إضافة العقد المطلوبة، ثم حفظ هذا المشهد إلى FBX.

## الخاتمة

تهانينا! لقد نجحت في **converted mesh to FBX**, مشاركة بيانات هندسة الشبكة بين عدة عقد، وتعيين ألوان مواد فردية باستخدام Aspose.3D for Java. يمنحك هذا سير العمل بنية شبكة خفيفة الوزن وقابلة لإعادة الاستخدام يمكن تصديرها إلى أي خط أنابيب متوافق مع FBX.

---

**آخر تحديث:** 2026-05-19  
**تم الاختبار مع:** Aspose.3D 24.11 for Java  
**المؤلف:** Aspose  

{{< blocks/products/products-backtop-button >}}

## دروس ذات صلة

- [كيفية تقسيم الشبكة حسب المادة في Java باستخدام Aspose.3D](/3d/java/3d-mesh-data/split-meshes-by-material/)
- [دمج نسيج FBX في Java – تطبيق المواد على كائنات 3D باستخدام Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [كيفية تصدير المشهد إلى FBX واسترجاع معلومات المشهد ثلاثي الأبعاد في Java](/3d/java/3d-scenes-and-models/get-scene-information/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}