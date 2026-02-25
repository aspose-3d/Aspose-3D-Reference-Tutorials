---
date: 2026-02-25
description: تعلم كيفية عكس نظام الإحداثيات وتخصيص استيراد ثلاثي الأبعاد باستخدام
  Aspose.3D LoadOptions في Java. دليل خطوة بخطوة لتنسيقات 3DS و OBJ و STL و U3D و glTF
  و PLY و X، و FBX اختياريًا.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: عكس نظام الإحداثيات – تخصيص تحميل ملفات 3D في جافا باستخدام Aspose.3D
url: /ar/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# عكس نظام الإحداثيات – تخصيص تحميل ملفات 3D في Java باستخدام Aspose.3D

في المشهد المتطور باستمرار لتصميم وتطوير ثلاثي الأبعاد، يُعد **عكس نظام الإحداثيات** عند استيراد النماذج مطلبًا شائعًا. سواءً كنت تقوم بتحويل الأصول من نظام يد يميني إلى يد يساري أو تحتاج إلى محاذاة النماذج مع اتفاقيات محاور محركك، توفر لك Aspose.3D for Java تحكمًا دقيقًا. يوضح هذا البرنامج التعليمي كيفية **تخصيص استيراد 3D** باستخدام `LoadOptions` من Aspose.3D، مع تغطية أكثر الصيغ شيوعًا مثل 3DS، OBJ، STL، U3D، glTF، PLY، X، و FBX الاختياري.

## إجابات سريعة
- **ماذا يفعل “عكس نظام الإحداثيات”?** يقوم بتبديل محاور X/Y/Z لتتناسب مع نظام الإحداثيات المستهدف.  
- **أي الصيغ تدعم العكس؟** جميع الصيغ الرئيسية (3DS، OBJ، STL، U3D، glTF، PLY، X، FBX) توفر خيار `setFlipCoordinateSystem`.  
- **هل أحتاج إلى مكتبات إضافية؟** فقط ملف JAR الخاص بـ Aspose.3D for Java؛ لا يلزم أي محولات خارجية.  
- **هل يمكنني تحميل المواد في نفس الوقت؟** نعم—استخدم `setEnableMaterials(true)` لملفات OBJ.  
- **هل يلزم ترخيص للإنتاج؟** يلزم وجود ترخيص صالح لـ Aspose.3D للنشر غير التجريبي.

## ما هو “عكس نظام الإحداثيات”؟
عكس نظام الإحداثيات يغيّر اتجاه المحاور المستخدمة في النموذج المستورد. هذا أمر أساسي عندما يستخدم الملف المصدر نظام يد مختلف (يمين‑يسار) عن محرك العرض الخاص بك، مما يمنع ظهور النماذج معكوسة أو مقلوبة.

## لماذا تخصيص استيراد 3D؟
- الحفاظ على تحويلات الرسوم المتحركة (`setApplyAnimationTransform`).  
- تصحيح معالجة الألوان (`setGammaCorrectedColor`).  
- حل مسارات الموارد الخارجية عبر `getLookupPaths()`.  
- تحسين استخدام الذاكرة بتحميل ما تحتاجه فقط.

## المتطلبات المسبقة

- فهم أساسي لبرمجة Java.  
- تثبيت مجموعة تطوير Java (JDK).  
- مكتبة Aspose.3D for Java تم تحميلها. يمكنك الحصول عليها [هنا](https://releases.aspose.com/3d/java/).  
- الإلمام بصيغ ملفات 3D مثل 3DS، OBJ، STL، U3D، glTF، PLY، X، و FBX.

## استيراد الحزم

في مشروع Java الخاص بك، تأكد من استيراد حزم Aspose.3D اللازمة:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## كيفية تخصيص استيراد 3D باستخدام LoadOptions

فيما يلي مقتطفات شفرة خطوة بخطوة توضح كيفية تمكين خيار **عكس نظام الإحداثيات** لكل صيغة مدعومة. المقتطفات جاهزة للنسخ إلى مشروعك؛ فقط استبدل `"Your Document Directory"` بالمسار الفعلي لأصولك.

### الخطوة 1: تخصيص تحميل ملف 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### الخطوة 2: تخصيص تحميل ملف OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### الخطوة 3: تخصيص تحميل ملف STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### الخطوة 4: تخصيص تحميل ملف U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### الخطوة 5: تخصيص تحميل ملف glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### الخطوة 6: تخصيص تحميل ملف PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### الخطوة 7: تخصيص تحميل ملف X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### الخطوة 8: تخصيص تحميل ملف FBX (اختياري)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## المشكلات الشائعة والحلول
- **النموذج يظهر معكوسًا بعد التحميل** – تأكد من ضبط `setFlipCoordinateSystem(true)` للصيغة الصحيحة.  
- **المواد مفقودة** – لملفات OBJ، تأكد من ضبط `setEnableMaterials(true)` وأن ملفات المواد (.mtl) موجودة في أحد مسارات البحث.  
- **إحداثيات القوام مقلوبة رأسًا على عقب** – لملفات glTF، قد تحتاج إلى `setFlipTexCoordV(true)` بالإضافة إلى عكس المحاور.  
- **أخطاء عدم العثور على الملف** – أضف الدليل الذي يحتوي على الموارد الخارجية (الملمس، الملفات المساعدة) إلى `loadOpts.getLookupPaths()`.

## الخلاصة

باستخدام `LoadOptions` من Aspose.3D، يمكنك **عكس نظام الإحداثيات** و**تخصيص استيراد 3D** تقريبًا لكل صيغة رئيسية. يزيل هذا المستوى من التحكم الحاجة إلى سكريبتات ما بعد المعالجة ويضمن عرض أصولك بشكل صحيح من المرة الأولى.

## الأسئلة المتكررة

### س1: أين يمكنني العثور على وثائق Aspose.3D for Java؟
ج1: الوثائق متاحة [هنا](https://reference.aspose.com/3d/java/).

### س2: كيف يمكنني تحميل Aspose.3D for Java؟
ج2: يمكنك تحميله [هنا](https://releases.aspose.com/3d/java/).

### س3: هل هناك نسخة تجريبية مجانية متاحة؟
ج3: نعم، يمكنك الوصول إلى النسخة التجريبية المجانية [هنا](https://releases.aspose.com/).

### س4: أين يمكنني الحصول على الدعم لـ Aspose.3D for Java؟
ج4: زر منتدى الدعم [هنا](https://forum.aspose.com/c/3d/18).

### س5: هل أحتاج إلى ترخيص مؤقت للاختبار؟
ج5: نعم، احصل على ترخيص مؤقت [هنا](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**آخر تحديث:** 2026-02-25  
**تم الاختبار مع:** Aspose.3D for Java 24.11 (latest)  
**المؤلف:** Aspose