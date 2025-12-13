---
date: 2025-12-13
description: تعلم كيفية استخدام Aspose 3D Java لتحويل العقد ثلاثية الأبعاد. يوضح هذا
  الدليل كيفية استخدام زوايا أويلر، إضافة دوران ثلاثي الأبعاد وتعيين الترجمة في Java.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – تحويل العقد ثلاثية الأبعاد باستخدام زوايا أويلر
url: /ar/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تحويل العقد ثلاثية الأبعاد باستخدام زوايا أويلر في جافا باستخدام Aspose.3D

## المقدمة

في هذا الدرس ستكتشف **كيفية استخدام aspose 3d java** لتحويل العقد ثلاثية الأبعاد عن طريق تطبيق زوايا أويلر. بنهاية الدليل ستكون قادرًا على إضافة دوران 3d، ضبط الإزاحة java، وإنشاء مشاهد ديناميكية تتفاعل مع البيانات في الوقت الحقيقي.

## إجابات سريعة
- **ما المكتبة التي تتعامل مع التحويلات ثلاثية الأبعاد في جافا؟** Aspose 3D for Java.  
- **أي طريقة تضبط الدوران باستخدام زوايا أويلر؟** `setEulerAngles()` على تحويل العقدة.  
- **كيف أحرك عقدة في الفضاء؟** استخدم `setTranslation()` مع `Vector3`.  
- **هل أحتاج إلى ترخيص للإنتاج؟** نعم، يلزم ترخيص تجاري لـ Aspose 3D.  
- **هل يمكنني التصدير إلى FBX؟** بالتأكيد – `scene.save(..., FileFormat.FBX7500ASCII)` يعمل مباشرةً.

## المتطلبات المسبقة

قبل أن نغوص في الدرس، تأكد من توفر المتطلبات التالية:

- معرفة أساسية ببرمجة جافا.  
- مجموعة تطوير جافا (JDK) مثبتة على جهازك.  
- مكتبة Aspose.3D، التي يمكنك الحصول عليها من [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## استيراد الحزم

ابدأ باستيراد الحزم اللازمة إلى مشروع جافا الخاص بك. تأكد من إضافة مكتبة Aspose.3D بشكل صحيح إلى مسار الفئة (classpath). إذا لم تقم بتنزيلها بعد، يمكنك العثور على رابط التنزيل [here](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – العمل مع زوايا أويلر

### الخطوة 1. تهيئة المشهد والعقدة

أولاً، أنشئ مشهدًا وعقدة ستحمل الهندسة التي تريد تحويلها.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### الخطوة 2. إنشاء شبكة وتحديد الهندسة

بعد ذلك، أنشئ شبكة بسيطة (مكعب في هذه الحالة) وأرفقها بالعقدة.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## إضافة دوران ثلاثي الأبعاد إلى عقدة

### الخطوة 3. ضبط زوايا أويلر والإزاحة

الآن نطبق الدوران باستخدام زوايا أويلر ونحرك العقدة إلى موضع مرئي.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## ضبط الإزاحة Java – تموضع العقدة

خطوة الإزاحة أعلاه توضح **set translation java** عمليًا: تم إزاحة العقدة 20 وحدة على المحور Z حتى يمكنك رؤيتها بعد التصيير.

## الخطوة 4. إضافة العقدة إلى المشهد

أرفق العقدة المحوّلة إلى العقدة الجذرية للمشهد.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## الخطوة 5. حفظ المشهد ثلاثي الأبعاد

أخيرًا، صدّر المشهد إلى ملف FBX (أو أي تنسيق مدعوم آخر).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

تأكد من استبدال `"Your Document Directory"` بالمسار المناسب على جهازك.

## الخاتمة

تهانينا! لقد نجحت في تحويل العقد ثلاثية الأبعاد باستخدام زوايا أويلر في جافا مع **aspose 3d java**. جرّب زوايا وإزاحات مختلفة لإنشاء مشاهد ثلاثية الأبعاد ديناميكية وجذابة.

## الأسئلة المتكررة

### س1: هل يمكنني استخدام Aspose.3D لجافا في المشاريع التجارية؟

ج1: نعم، يمكنك ذلك. زر صفحة [purchase page](https://purchase.aspose.com/buy) للحصول على تفاصيل الترخيص.

### س2: أين يمكنني العثور على دعم Aspose.3D؟

ج2: منتدى [Aspose.3D forum](https://forum.aspose.com/c/3d/18) هو المكان المناسب للحصول على المساعدة والتواصل مع المجتمع.

### س3: هل هناك نسخة تجريبية مجانية متاحة؟

ج3: نعم، يمكنك استكشاف [free trial](https://releases.aspose.com/) لتجربة إمكانيات Aspose.3D.

### س4: كيف يمكنني الحصول على ترخيص مؤقت؟

ج4: يمكنك الحصول على ترخيص مؤقت [here](https://purchase.aspose.com/temporary-license/).

### س5: أين يمكنني العثور على الوثائق؟

ج5: توفر [documentation](https://reference.aspose.com/3d/java/) إرشادات شاملة لاستخدام Aspose.3D لجافا.

## الأسئلة المتكررة

**س: ما الفرق بين زوايا أويلر ودوران الكواتيرنيون؟**  
ج: زوايا أويلر بديهية (الميل، الدوران، الالتفاف) لكنها قد تعاني من قفل الجيمبال، بينما الكواتيرنيونات تتجنب هذه المشكلة وتكون أفضل للتداخلات السلسة.

**س: هل يمكنني ربط عدة تحويلات على نفس العقدة؟**  
ج: نعم. استدعِ `setEulerAngles`، `setTranslation`، و`setScale` بأي ترتيب؛ المكتبة تجمعها في مصفوفة تحويل واحدة.

**س: هل يمكن التصدير إلى صيغ أخرى مثل OBJ أو STL؟**  
ج: بالتأكيد. استبدل `FileFormat.FBX7500ASCII` بـ `FileFormat.OBJ` أو `FileFormat.STL` في استدعاء `scene.save`.

**س: كيف أطبق نفس الدوران على عدة عقد في آن واحد؟**  
ج: أنشئ عقدة أصلية، طبّق الدوران عليها، ثم أضف العقد الفرعية تحتها. جميع الأطفال يرثون التحويل.

**س: هل أحتاج إلى استدعاء أي طرق تنظيف بعد الحفظ؟**  
ج: جامع القمامة في جافا يتعامل مع معظم الموارد، لكن يمكنك استدعاء `scene.dispose()` صراحةً إذا كنت تتعامل مع مشاهد كبيرة في تطبيق طويل التشغيل.

---

**آخر تحديث:** 2025-12-13  
**تم الاختبار مع:** Aspose.3D 23.12 for Java  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}