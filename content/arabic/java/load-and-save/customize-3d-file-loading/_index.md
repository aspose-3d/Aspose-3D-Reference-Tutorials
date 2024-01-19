---
title: قم بتخصيص تحميل الملفات ثلاثية الأبعاد في Java باستخدام Aspose.3D LoadOptions
linktitle: قم بتخصيص تحميل الملفات ثلاثية الأبعاد في Java باستخدام Aspose.3D LoadOptions
second_title: Aspose.3D جافا API
description: قم بتحسين تحميل الملفات ثلاثية الأبعاد في Java باستخدام خيارات التحميل القابلة للتخصيص من Aspose.3D. تعلم التخصيص خطوة بخطوة لـ 3DS وOBJ وSTL وU3D وglTF وPLY وX وFBX الاختياري.
type: docs
weight: 12
url: /ar/java/load-and-save/customize-3d-file-loading/
---
## مقدمة

في المشهد المتطور باستمرار للتصميم والتطوير ثلاثي الأبعاد، يعد التعامل الفعال مع تنسيقات الملفات ثلاثية الأبعاد أمرًا بالغ الأهمية. يوفر Aspose.3D for Java حلاً قويًا لتخصيص تحميل تنسيقات الملفات ثلاثية الأبعاد المختلفة. سيرشدك هذا البرنامج التعليمي خلال عملية تخصيص تحميل الملفات ثلاثية الأبعاد في Java باستخدام LoadOptions الخاص بـ Aspose.3D.

## المتطلبات الأساسية

قبل الغوص في عملية التخصيص، تأكد من أن لديك ما يلي:

- الفهم الأساسي لبرمجة جافا.
- مجموعة تطوير جافا المثبتة (JDK).
-  تم تنزيل Aspose.3D لمكتبة Java. يمكنك الحصول عليه[هنا](https://releases.aspose.com/3d/java/).
- الإلمام بتنسيقات الملفات ثلاثية الأبعاد مثل 3DS وOBJ وSTL وU3D وglTF وPLY وX وFBX.

## حزم الاستيراد

في مشروع Java الخاص بك، تأكد من استيراد حزم Aspose.3D الضرورية:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## تخصيص تحميل الملفات ثلاثية الأبعاد

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

## خاتمة

يؤدي تخصيص تحميل الملفات ثلاثية الأبعاد في Java باستخدام LoadOptions الخاص بـ Aspose.3D إلى تمكين المطورين من تخصيص عملية الاستيراد وفقًا لمتطلبات محددة. سواء أكان الأمر يتعلق بضبط تحويلات الرسوم المتحركة، أو قلب أنظمة الإحداثيات، أو التعامل مع التبعيات الخارجية، فإن Aspose.3D يوفر المرونة اللازمة للتكامل السلس.

## الأسئلة الشائعة

### س1: أين يمكنني العثور على وثائق Aspose.3D الخاصة بـ Java؟

 ج1: الوثائق متاحة[هنا](https://reference.aspose.com/3d/java/).

### س2: كيف يمكنني تنزيل Aspose.3D لـ Java؟

 ج2: يمكنك تنزيله[هنا](https://releases.aspose.com/3d/java/).

### س3: هل هناك نسخة تجريبية مجانية متاحة؟

 ج3: نعم، يمكنك الوصول إلى النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).

### س4: أين يمكنني الحصول على دعم Aspose.3D لـ Java؟

 ج4: قم بزيارة منتدى الدعم[هنا](https://forum.aspose.com/c/3d/18).

### س5: هل أحتاج إلى ترخيص مؤقت للاختبار؟

 ج5: نعم، احصل على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).