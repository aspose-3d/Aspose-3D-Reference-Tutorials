---
date: 2025-12-12
description: تعلم كيفية تعيين لون المادة أثناء مشاركة بيانات هندسة الشبكة وحفظ المشهد
  بصيغة FBX في Java 3D باستخدام Aspose.3D.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: تعيين لون المادة ومشاركة بيانات هندسة الشبكة في Java 3D باستخدام Aspose.3D
url: /ar/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تعيين لون المادة ومشاركة بيانات هندسة الشبكة في Java 3D باستخدام Aspose.3D

## مقدمة

الشروع في رحلة إلى عالم Java 3D مع Aspose.3D يفتح أمامك عالماً من الإمكانيات لإنشاء تصورات مذهلة وتجارب غامرة. في هذا الدرس، سنرشدك إلى **كيفية مشاركة بيانات الشبكة** في Java 3D باستخدام Aspose.3D، وسنوضح لك بالضبط **كيفية تعيين لون المادة** لكل نسخة من الشبكة. اتبع كل خطوة بعناية، وفي النهاية ستتمكن من تبادل بيانات الشبكة بسلاسة بين عدة عقد مع التحكم في الألوان وتصديرها إلى FBX.

## إجابات سريعة
- **ما هو الهدف الرئيسي؟** تعيين لون المادة لكل عقدة ومشاركة بيانات هندسة الشبكة.  
- **ما المكتبة المطلوبة؟** Aspose.3D for Java.  
- **كيف يمكنني تصدير النتيجة؟** حفظ المشهد كملف FBX (FBX7400ASCII).  
- **هل أحتاج إلى ترخيص؟** يلزم ترخيص مؤقت أو كامل للاستخدام في الإنتاج.  
- **ما نسخة Java التي تعمل؟** أي بيئة Java 8+.

## المتطلبات المسبقة

قبل أن نغوص في الدرس، تأكد من توفر المتطلبات المسبقة التالية:

- بيئة تطوير Java: تأكد من إعداد بيئة تطوير Java على نظامك.  
- مكتبة Aspose.3D: قم بتحميل وتثبيت مكتبة Aspose.3D. يمكنك العثور على المكتبة [هنا](https://releases.aspose.com/3d/java/).

## استيراد الحزم

ابدأ باستيراد الحزم الضرورية إلى مشروع Java الخاص بك. هذه الخطوة حاسمة للوصول إلى الوظائف التي توفرها مكتبة Aspose.3D.

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

في هذه الخطوة، نعرّف مصفوفة من متجهات اللون التي ستُطبق على عناصر مختلفة في مشهدنا ثلاثي الأبعاد.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## الخطوة 3: إنشاء شبكة 3D في Java باستخدام Polygon Builder (create 3d mesh java)

استخدم الفئة Common لإنشاء شبكة باستخدام طريقة polygon builder. ستكون هذه الشبكة أساس عناصرنا ثلاثية الأبعاد.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## كيف يمكن تعيين لون المادة لكل عقدة؟

قم بالتكرار عبر متجهات اللون، أنشئ عقد مكعب، واضبط الخصائص مثل المادة، **set material color**، والانتقال. هذا هو جوهر التحكم في المظهر البصري لكل نسخة من الشبكة.

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

## الخاتمة

تهانينا! لقد نجحت في **set material color**، ومشاركة بيانات هندسة الشبكة بين عدة عقد، وتصدير النتيجة كملف FBX باستخدام Aspose.3D for Java. يفتح هذا أمامك إمكانيات لا حصر لها لإنشاء تطبيقات ثلاثية الأبعاد بصرية مذهلة وتفاعلية.

## الأسئلة المتكررة

### Q1: هل يمكنني استخدام Aspose.3D مع أطر Java أخرى؟

A1: نعم، تم تصميم Aspose.3D للعمل بسلاسة مع مختلف أطر Java.

### Q2: هل هناك خيارات ترخيص متاحة لـ Aspose.3D؟

A2: نعم، يمكنك استكشاف خيارات الترخيص [هنا](https://purchase.aspose.com/buy).

### Q3: كيف يمكنني الحصول على الدعم لـ Aspose.3D؟

A3: قم بزيارة منتدى Aspose.3D [هنا](https://forum.aspose.com/c/3d/18) للحصول على الدعم والمناقشات.

### Q4: هل هناك نسخة تجريبية مجانية متاحة؟

A4: نعم، يمكنك الحصول على نسخة تجريبية مجانية [هنا](https://releases.aspose.com/).

### Q5: كيف أحصل على ترخيص مؤقت لـ Aspose.3D؟

A5: يمكنك الحصول على ترخيص مؤقت [هنا](https://purchase.aspose.com/temporary-license/).

## أسئلة شائعة إضافية

**س: هل يمكنني تصدير المشهد إلى تنسيقات أخرى غير FBX؟**  
ج: نعم، يدعم Aspose.3D تنسيقات OBJ، STL، 3MF، وأكثر. فقط غيّر تعداد `FileFormat` في استدعاء `save`.

**س: ماذا لو احتجت لتغيير المادة بعد إنشاء المشهد؟**  
ج: استرجع العقدة، عدّل `LambertMaterial` (مثلًا `setDiffuseColor`)، ثم أعد حفظ المشهد.

**س: هل تتعامل المكتبة مع الشبكات الكبيرة بكفاءة؟**  
ج: يستخدم Aspose.3D هياكل بيانات مُحسّنة؛ ومع ذلك، بالنسبة للشبكات الكبيرة جدًا، يُنصح باستخدام البث أو تقسيم المشهد.

**س: هل هناك طريقة لتحريك تغيير اللون؟**  
ج: نعم، يمكنك تحريك خصائص المادة باستخدام واجهة برمجة التطبيقات `AnimationController`.

---

**آخر تحديث:** 2025-12-12  
**تم الاختبار مع:** Aspose.3D 24.11 for Java  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}