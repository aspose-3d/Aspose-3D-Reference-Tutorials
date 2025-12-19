---
date: 2025-12-19
description: تعلم كيفية تخصيص تحميل 3D في جافا باستخدام Aspose.3D LoadOptions. دليل
  خطوة‑بخطوة يغطي صيغ 3DS وOBJ وSTL وU3D وglTF وPLY وX والملفات الاختيارية FBX.
linktitle: Customize 3D Loading Java – How to customize 3d loading java with Aspose.3D
  LoadOptions
second_title: Aspose.3D Java API
title: تخصيص تحميل 3D في جافا – كيفية تخصيص تحميل 3D في جافا باستخدام Aspose.3D LoadOptions
url: /ar/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تخصيص تحميل 3D في Java – كيفية تخصيص تحميل 3D في Java باستخدام Aspose.3D LoadOptions

## المقدمة

في تطبيقات 3D الحديثة، **customize 3d loading java** أمر أساسي لضمان ظهور النماذج بالضبط كما هو مقصود، بغض النظر عن تنسيق المصدر. سواءً كنت تبني محرك ألعاب، أو عارض AR/VR، أو أداة تحويل CAD، فإن القدرة على التحكم في طريقة استيراد ملفات 3DS و OBJ و STL و U3D و glTF و PLY و X وحتى ملفات FBX يمكن أن توفر لك ساعات من المعالجة اللاحقة. يشرح هذا الدليل كل خطوة من خطوات تخصيص تحميل ملفات 3D في Java باستخدام فئات `LoadOptions` المرنة في Aspose.3D.

## إجابات سريعة
- **ماذا يعني “customize 3d loading java”؟** يعني ذلك تكوين `LoadOptions` الخاصة بـ Aspose.3D للتحكم في سلوك الاستيراد مثل عكس نظام الإحداثيات، معالجة المواد، وتحويلات الرسوم المتحركة.  
- **ما هي الصيغ التي يمكنني تخصيصها؟** 3DS، OBJ، STL، U3D، glTF، PLY، X، واختياريًا FBX.  
- **هل أحتاج إلى ترخيص لتجربة ذلك؟** يلزم الحصول على ترخيص مؤقت للوظائف الكاملة؛ كما يتوفر نسخة تجريبية مجانية.  
- **هل هناك بيانات إضافية مطلوبة؟** قد تحتاج إلى توفير مسارات البحث للموارد الخارجية مثل القوام أو مكتبات المواد.  
- **أين يمكنني العثور على أحدث نسخة من Aspose.3D for Java؟** في صفحة التحميل الرسمية المذكورة أدناه.

## ما هو “customize 3d loading java”؟

تخصيص تحميل 3D في Java يتيح لك تحديد كيفية تفسير محرك Aspose.3D للملفات الواردة. من خلال تعديل الخصائص في فئات `*LoadOptions` المختلفة، يمكنك:

* عكس نظام الإحداثيات ليتطابق مع خط أنابيب العرض الخاص بك.  
* تمكين أو تعطيل تحميل المواد في السيناريوهات التي تتطلب أداءً عاليًا.  
* تطبيق تصحيح جاما، تحويلات الرسوم المتحركة، أو الحفاظ على الإعدادات العالمية المدمجة لملفات FBX.  

## لماذا نستخدم Aspose.3D LoadOptions؟

* **تحكم دقيق** – تعديل كل صيغة بشكل مستقل.  
* **اتساق عبر الصيغ** – تطبيق نفس قواعد نظام الإحداثيات على جميع أنواع الملفات المدعومة.  
* **تحسين الأداء** – تخطي البيانات غير الضرورية (مثل المواد) عندما لا تكون مطلوبة.  

## المتطلبات المسبقة

قبل البدء، تأكد من وجود ما يلي:

- فهم قوي لأساسيات Java.  
- تثبيت JDK 8 أو أعلى.  
- مكتبة Aspose.3D for Java محملة من الموقع الرسمي — يمكنك الحصول عليها [هنا](https://releases.aspose.com/3d/java/).  
- إلمام أساسي بصيغ ملفات 3D التي تخطط للعمل معها (3DS، OBJ، STL، U3D، glTF، PLY، X، FBX).

## استيراد الحزم

في مشروع Java الخاص بك، استورد فئات Aspose.3D الأساسية وحزمة الإدخال/الإخراج القياسية:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## تخصيص تحميل ملفات 3D

فيما يلي طريقة مخصصة لكل صيغة مدعومة. كل مقتطف يُظهر أكثر التخصيصات شيوعًا؛ لا تتردد في تعديل الخصائص لتناسب خط أنابيبك.

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

*لماذا هذا مهم:* تمكين `ApplyAnimationTransform` يضمن أن أي بيانات حركة مدمجة تحترم نظام الإحداثيات المستهدف، بينما `GammaCorrectedColor` يصلح مشاكل شدة اللون التي تظهر غالبًا عند الانتقال بين محركات عرض مختلفة.

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

*نصيحة:* إذا كنت تقوم بتحميل ملفات OBJ التي تشير إلى ملفات مواد `.mtl` خارجية، احتفظ بـ `EnableMaterials` مضبوطًا على `true` وتأكد من أن مسار البحث يشير إلى المجلد الذي يحتوي على تلك الملفات.

### الخطوة 3: تخصيص تحميل ملف STL  

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

*نصيحة احترافية:* ملفات STL تحتوي على الهندسة فقط، لذا عادةً ما يكون عكس نظام الإحداثيات هو التعديل الوحيد المطلوب.

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

*لماذا نقلب إحداثيات V للنصوص؟* يستخدم العديد من مُصدِّري glTF أصل UV مختلف عن خطوط أنابيب DirectX التقليدية؛ عكس `TexCoordV` يضبط القوام بشكل صحيح.

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

*متى تستخدم ذلك:* غالبًا ما تتضمن ملفات FBX إعدادات عالمية (الوحدات، المحور العلوي). الحفاظ عليها يضمن أن المشهد المستورد يطابق نية المؤلف الأصلية.

## المشكلات الشائعة والحلول

| المشكلة | السبب المحتمل | الحل |
|---------|---------------|------|
| القوام غير ظاهر | مسار البحث غير محدد أو حساسية الأحرف غير صحيحة | أضف الدليل الصحيح إلى `loadOpts.getLookupPaths()` وتحقق من أسماء الملفات |
| النموذج مقلوب رأسًا على عقب | `FlipCoordinateSystem` غير مفعَّل للصيغة | اضبط `setFlipCoordinateSystem(true)` للـ `*LoadOptions` المناسب |
| الألوان باهتة | تصحيح الجاما غير مفعَّل لملف 3DS | استدعِ `setGammaCorrectedColor(true)` على `Discreet3dsLoadOptions` |
| حركة FBX غير صحيحة | تم تجاوز الإعدادات العالمية | استخدم `setKeepBuiltinGlobalSettings(true)` |

## الأسئلة المتكررة

### س1: أين يمكنني العثور على وثائق Aspose.3D for Java؟  
ج1: الوثائق متاحة [هنا](https://reference.aspose.com/3d/java/).

### س2: كيف يمكنني تنزيل Aspose.3D for Java؟  
ج2: يمكنك تنزيله [هنا](https://releases.aspose.com/3d/java/).

### س3: هل هناك نسخة تجريبية مجانية؟  
ج3: نعم، يمكنك الوصول إلى النسخة التجريبية المجانية [هنا](https://releases.aspose.com/).

### س4: أين يمكنني الحصول على دعم Aspose.3D for Java؟  
ج4: زر منتدى الدعم [هنا](https://forum.aspose.com/c/3d/18).

### س5: هل أحتاج إلى ترخيص مؤقت للاختبار؟  
ج5: نعم، احصل على ترخيص مؤقت [هنا](https://purchase.aspose.com/temporary-license/).

### س6: هل يمكنني تحميل صيغ متعددة في مشهد واحد؟  
ج6: بالتأكيد. أنشئ `LoadOptions` منفصلة لكل صيغة واستدعِ `scene.open()` لكل ملف؛ سيقوم المشهد بدمج الهندسة.

### س7: كيف أحسن أداء التحميل للملفات الكبيرة؟  
ج7: عطل الميزات غير الضرورية (مثل تحميل المواد لملفات STL) واستخدم `LookupPaths` لتجنب عمليات الإدخال/الإخراج المتكررة.

### س8: هل يمكن تغيير نظام الإحداثيات برمجيًا بعد التحميل؟  
ج8: نعم، يمكنك استدعاء `scene.getRootNode().rotate()` أو `scene.getRootNode().scale()` بعد فتح الملف.

---

**آخر تحديث:** 2025-12-19  
**تم الاختبار مع:** Aspose.3D for Java 24.11 (أحدث نسخة وقت الكتابة)  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}