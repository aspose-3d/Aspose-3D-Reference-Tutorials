---
date: 2026-02-17
description: تعلم كيفية تحويل الشبكة إلى FBX مع ضبط لون المادة ومشاركة بيانات هندسة
  الشبكة في Java 3D باستخدام Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: تحويل الشبكة إلى FBX وتعيين لون المادة في Java 3D
url: /ar/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تحويل Mesh إلى FBX وتعيين لون المادة في Java 3D

## المقدمة

إذا كنت تبني تطبيقًا ثلاثي الأبعاد مبنيًا على Java، فستحتاج غالبًا إلى إعادة استخدام نفس الهندسة عبر كائنات متعددة مع إعطاء كل نسخة مظهرًا فريدًا. في هذا الدرس ستتعلم **كيفية تحويل mesh إلى FBX**، مشاركة هندسة الـ mesh الأساسية بين عدة عقد، و**تعيين لون مادة مختلف لكل عقدة**. في النهاية ستحصل على مشهد FBX جاهز للتصدير يمكنك إدراجه في أي محرك أو عارض.

## إجابات سريعة
- **ما هو الهدف الرئيسي؟** تحويل mesh إلى FBX، مشاركة هندسة الـ mesh، وتعيين لون مادة مميز لكل عقدة.  
- **ما المكتبة المطلوبة؟** Aspose.3D for Java.  
- **كيف يمكنني تصدير النتيجة؟** احفظ المشهد كملف FBX باستخدام `FileFormat.FBX7400ASCII`.  
- **هل أحتاج إلى ترخيص؟** يلزم الحصول على ترخيص مؤقت أو كامل للاستخدام في الإنتاج.  
- **ما نسخة Java التي تعمل؟** أي بيئة Java 8+.

## ما هو **convert mesh to FBX**؟

`convert mesh to fbx` هي العملية التي يتم فيها أخذ كائن mesh تم إنشاؤه أو تعديلُه في الذاكرة وكتابته إلى تنسيق ملف FBX، الذي يدعمه على نطاق واسع أدوات 3D مثل Maya وBlender وUnity. تقوم Aspose.3D بالتعامل مع الجزء الصعب، لذا كل ما عليك هو استدعاء `scene.save(...)` مع الـ `FileFormat` المناسب.

## لماذا مشاركة بيانات هندسة الـ mesh؟

مشاركة الهندسة تقلل من استهلاك الذاكرة وتسرّع عملية العرض لأن مخازن الرؤوس الأساسية تُخزن مرة واحدة فقط. هذه التقنية مثالية للمشاهد التي تحتوي على الكثير من الكائنات المكررة—مثل الغابات، الحشود، أو الهندسة المعيارية—حيث يختلف كل نسخة فقط في التحويل أو المادة.

## المتطلبات المسبقة

قبل أن نغوص في الدرس، تأكد من توفر المتطلبات التالية:

- **بيئة تطوير Java** – أي IDE أو إعداد سطر أوامر مع Java 8 أو أحدث.  
- **مكتبة Aspose.3D** – قم بتحميل أحدث JAR من الموقع الرسمي: [here](https://releases.aspose.com/3d/java/).

## استيراد الحزم

ابدأ باستيراد الحزم اللازمة إلى مشروع Java الخاص بك. هذه الخطوة حاسمة للوصول إلى الوظائف التي توفرها مكتبة Aspose.3D.

```java
import com.aspose.threed.*;
```

## الخطوة 1: تهيئة كائن المشهد (initialize scene java)

لنبدأ العملية بتهيئة كائن المشهد. سيعمل هذا كقماش حيث ستظهر سحرنا ثلاثي الأبعاد.

```java
// Initialize scene object
Scene scene = new Scene();
```

## الخطوة 2: تعريف متجهات اللون

في هذه الخطوة، نقوم بتعريف مصفوفة من متجهات اللون التي ستُطبق على عناصر مختلفة في مشهدنا ثلاثي الأبعاد.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## الخطوة 3: إنشاء Mesh ثلاثي الأبعاد في Java باستخدام Polygon Builder (create 3d mesh java)

استخدم الفئة Common لإنشاء mesh باستخدام طريقة polygon builder. سيكون هذا الـ mesh أساسًا لعناصرنا ثلاثية الأبعاد.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## كيف يتم تعيين لون المادة لكل عقدة؟

قم بالتكرار عبر متجهات اللون، أنشئ عقد مكعب، واضبط الخصائص مثل المادة، **set material color**، والترجمة. هذا هو جوهر التحكم في المظهر البصري لكل نسخة من الـ mesh.

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

حدد الدليل واسم الملف لحفظ المشهد ثلاثي الأبعاد بالتنسيق المدعوم، في هذه الحالة FBX7400ASCII. تُظهر هذه الخطوة أيضًا **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## المشكلات الشائعة والنصائح

- **مشكلات المسار** – تأكد من أن مسار الدليل ينتهي بفاصل ملف (`/` أو `\\`) قبل إلحاق اسم الملف.  
- **تهيئة الترخيص** – إذا نسيت ضبط ترخيص Aspose.3D قبل استدعاء `scene.save`، ستعمل المكتبة في وضع التجربة وقد تُضيف علامة مائية.  
- **استبدال المادة** – إعادة استخدام نفس كائن `LambertMaterial` لعدة عقد سيؤدي إلى مشاركة جميع العقد لنفس اللون. احرص دائمًا على إنشاء مادة جديدة في كل تكرار، كما هو موضح أعلاه.  
- **Meshes الكبيرة** – بالنسبة للـ meshes التي تحتوي على ملايين الرؤوس، فكر في استخدام `MeshBuilder` مع مضلعات مفهرسة للحفاظ على حجم ملف FBX ضمن نطاق معقول.

## الأسئلة المتكررة

**س: هل يمكنني تصدير المشهد إلى صيغ أخرى غير FBX؟**  
ج: نعم، تدعم Aspose.3D صيغ OBJ وSTL و3MF وGLTF وغيرها. فقط استبدل تعداد `FileFormat` في استدعاء `save`.

**س: ماذا لو احتجت لتغيير المادة بعد إنشاء المشهد؟**  
ج: استرجع العقدة، عدل `LambertMaterial` الخاصة بها (مثلاً `setDiffuseColor`)، ثم أعد حفظ المشهد.

**س: هل تتعامل المكتبة مع الـ meshes الكبيرة بكفاءة؟**  
ج: تستخدم Aspose.3D هياكل بيانات مُحسّنة؛ ومع ذلك، بالنسبة للـ meshes الضخمة جدًا فكر في البث أو تقسيم المشهد.

**س: هل هناك طريقة لتحريك تغيير اللون؟**  
ج: نعم، يمكنك تحريك خصائص المادة باستخدام API `AnimationController`.

## أسئلة متكررة إضافية

**س1: هل يمكنني استخدام Aspose.3D مع أطر Java أخرى؟**  
ج1: نعم، تم تصميم Aspose.3D للعمل بسلاسة مع مختلف أطر Java.

**س2: هل هناك خيارات ترخيص متاحة لـ Aspose.3D؟**  
ج2: نعم، يمكنك استكشاف خيارات الترخيص [here](https://purchase.aspose.com/buy).

**س3: كيف يمكنني الحصول على دعم لـ Aspose.3D؟**  
ج3: زر منتدى Aspose.3D [forum](https://forum.aspose.com/c/3d/18) للحصول على الدعم والنقاشات.

**س4: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج4: نعم، يمكنك الحصول على نسخة تجريبية مجانية [here](https://releases.aspose.com/).

**س5: كيف أحصل على ترخيص مؤقت لـ Aspose.3D؟**  
ج5: يمكنك الحصول على ترخيص مؤقت [here](https://purchase.aspose.com/temporary-license/).

## الخلاصة

تهانينا! لقد نجحت في **تحويل mesh إلى FBX**، مشاركة بيانات هندسة الـ mesh بين عدة عقد، وتعيين ألوان مادة فردية باستخدام Aspose.3D for Java. يمنحك هذا سير العمل بنية mesh خفيفة الوزن وقابلة لإعادة الاستخدام يمكن تصديرها إلى أي خط أنابيب متوافق مع FBX.

---

**آخر تحديث:** 2026-02-17  
**تم الاختبار مع:** Aspose.3D 24.11 for Java  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}