---
title: خيارات التحميل المخصصة
linktitle: خيارات التحميل المخصصة
second_title: Aspose.3D.NET API
description: استكشف Aspose.3D for .NET، وهو الحل الأمثل لتحميل النماذج ثلاثية الأبعاد وحفظها بشكل سلس.
type: docs
weight: 15
url: /ar/net/loading-and-saving/custom-load-options/
---
## مقدمة

مرحبًا بك في عالم Aspose.3D for .NET - وهي مكتبة قوية تمكّن المطورين من العمل بسلاسة مع الملفات ثلاثية الأبعاد. في هذا البرنامج التعليمي، سنتعمق في تعقيدات تحميل النماذج ثلاثية الأبعاد وحفظها، مع التركيز على خيارات التحميل المخصصة. سواء كنت مطورًا متمرسًا أو وافدًا جديدًا، سيرشدك هذا الدليل خلال العملية خطوة بخطوة، مما يضمن لك الاستفادة الكاملة من إمكانات Aspose.3D لـ .NET.

## المتطلبات الأساسية

قبل أن نبدأ هذه الرحلة، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D لـ .NET: تأكد من تثبيت المكتبة. يمكنك تنزيله[هنا](https://releases.aspose.com/3d/net/).

- دليل المستندات: قم بإنشاء دليل لتخزين ملفات النماذج ثلاثية الأبعاد الخاصة بك.

الآن بعد أن أصبحت لديك الأساسيات، دعنا نتعمق في عالم معالجة النماذج ثلاثية الأبعاد المثير!

## استيراد مساحات الأسماء

أول الأشياء أولاً، فلنستورد مساحات الأسماء الضرورية. وهذا سوف يمهد الطريق لرحلتنا إلى عالم Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## التحميل والحفظ - خيارات التحميل المخصصة

### الخطوة 1: تحميل ملفات Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //ضبط الخيارات المخصصة
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //قم بتحميل الملف باستخدام خيارات التحميل
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### الخطوة 2: تحميل ملفات OBJ

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //ضبط الخيارات المخصصة
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //قم بتحميل الملف باستخدام خيارات التحميل
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### الخطوة 3: تحميل ملفات STL

```csharp
private static void STLLoadOption()
{
    // المسار إلى دليل المستندات.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //ضبط الخيارات المخصصة
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //قم بتحميل الملف باستخدام خيارات التحميل
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### الخطوة 4: تحميل ملفات U3D

```csharp
private static void U3DLoadOption()
{
    // المسار إلى دليل المستندات.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //ضبط الخيارات المخصصة
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //قم بتحميل الملف باستخدام خيارات التحميل
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### الخطوة 5: تحميل ملفات glTF

```csharp
private static void glTFLoadOptions()
{
    // المسار إلى دليل المستندات.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //ضبط الخيارات المخصصة
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### الخطوة 6: تحميل ملفات PLY

```csharp
private static void PlyLoadOptions()
{
    // المسار إلى دليل المستندات.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //ضبط الخيارات المخصصة
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### الخطوة 7: تحميل ملفات FBX

```csharp
private static void FBXLoadOptions()
{
    // المسار إلى دليل المستندات.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //ضبط الخيارات المخصصة
    scene.Open("test.FBX", opt);

    // خصائص الإخراج المحددة في GlobalSettings في ملف FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## خاتمة

تهانينا! لقد نجحت في التنقل عبر العالم المعقد لتحميل النماذج ثلاثية الأبعاد وحفظها باستخدام Aspose.3D لـ .NET. يغطي هذا البرنامج التعليمي تنسيقات الملفات المختلفة وخيارات التحميل المخصصة لها، مما يمكّنك من التعامل مع الأصول ثلاثية الأبعاد بسهولة.

## الأسئلة الشائعة

### س1: هل Aspose.3D for .NET مناسب للمبتدئين؟

ج1: بالتأكيد! يوفر Aspose.3D for .NET واجهة سهلة الاستخدام، مما يجعله في متناول المطورين من جميع المستويات.

### س2: هل يمكنني استخدام Aspose.3D للمشاريع التجارية؟

ج2: نعم، يأتي Aspose.3D for .NET مزودًا برخصة تجارية، مما يسمح لك باستخدامه في مشاريعك.

### س3: هل هناك أي قيود على تنسيقات الملفات المدعومة؟

 ج3: يدعم Aspose.3D for .NET نطاقًا واسعًا من تنسيقات الملفات ثلاثية الأبعاد الشائعة، بما في ذلك OBJ وSTL وFBX والمزيد. الرجوع إلى[توثيق](https://reference.aspose.com/3d/net/) للحصول على قائمة شاملة.

### س4: هل هناك نسخة تجريبية متاحة؟

ج4: نعم، يمكنك استكشاف إمكانيات Aspose.3D لـ .NET عن طريق تنزيل ملف[تجربة مجانية](https://releases.aspose.com/).

### س5: أين يمكنني طلب الدعم لـ Aspose.3D لـ .NET؟

 ج5: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع ومساعدته.