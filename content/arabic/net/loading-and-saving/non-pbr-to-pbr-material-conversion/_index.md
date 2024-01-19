---
title: التحميل والحفظ - تحويل المواد من غير PBR إلى PBR
linktitle: التحميل والحفظ - تحويل المواد من غير PBR إلى PBR
second_title: Aspose.3D.NET API
description: استكشف Aspose.3D for .NET - قم بتحويل المواد غير PBR إلى PBR بسهولة. برنامج تعليمي شامل وواجهة برمجة تطبيقات قوية.
type: docs
weight: 16
url: /ar/net/loading-and-saving/non-pbr-to-pbr-material-conversion/
---
## مقدمة

مرحبًا بك في هذا الدليل التفصيلي حول استخدام Aspose.3D لـ .NET لتحويل المواد غير PBR (العرض المادي) إلى مواد PBR. Aspose.3D عبارة عن واجهة برمجة تطبيقات قوية تتيح للمطورين العمل بسلاسة مع تنسيقات الملفات ثلاثية الأبعاد في تطبيقات .NET الخاصة بهم.

## المتطلبات الأساسية

قبل أن نتعمق في البرنامج التعليمي، تأكد من أن لديك المتطلبات الأساسية التالية:

-  Aspose.3D لـ .NET: تأكد من تثبيت مكتبة Aspose.3D لـ .NET. يمكنك العثور على رابط التحميل[هنا](https://releases.aspose.com/3d/net/).

- الفهم الأساسي لـ C#: يفترض هذا البرنامج التعليمي أن لديك فهمًا أساسيًا لبرمجة C#.

- IDE (بيئة التطوير المتكاملة): اختر IDE المفضل لديك لتطوير .NET، مثل Visual Studio.

## استيراد مساحات الأسماء

في كود C# الخاص بك، ابدأ باستيراد مساحات الأسماء الضرورية:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## الخطوة 1: تهيئة مشهد ثلاثي الأبعاد جديد

ابدأ بإنشاء مشهد ثلاثي الأبعاد جديد باستخدام الكود التالي:

```csharp
// ExStart: Non_PBRtoPBRMaterial
// تهيئة مشهد ثلاثي الأبعاد جديد
var scene = new Scene();
```

## الخطوة 2: إنشاء كائن ثلاثي الأبعاد

بعد ذلك، قم بإنشاء كائن ثلاثي الأبعاد، على سبيل المثال، مربع:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## الخطوة 3: تكوين تحويل المواد

قم بإعداد خيارات تحويل المواد للتحويل من غير PBR إلى PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## الخطوة 4: احفظ بتنسيق GLTF 2.0

احفظ المشهد المحول بتنسيق GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

كرر هذه الخطوات حسب الحاجة لحالة الاستخدام المحددة الخاصة بك، مع التأكد من تكوين كل التفاصيل بشكل صحيح.

## خاتمة

تهانينا! لقد تعلمت بنجاح كيفية تحويل المواد غير PBR إلى PBR باستخدام Aspose.3D لـ .NET. تفتح هذه الأداة القوية إمكانيات لا حصر لها لمعالجة الرسومات ثلاثية الأبعاد في تطبيقات .NET الخاصة بك.

## الأسئلة الشائعة

### س1: هل Aspose.3D متوافق مع كافة تنسيقات الملفات ثلاثية الأبعاد؟

ج1: نعم، يدعم Aspose.3D نطاقًا واسعًا من تنسيقات الملفات ثلاثية الأبعاد، مما يوفر المرونة في مشروعاتك.

### س2: هل يمكنني استخدام Aspose.3D للتطبيقات التجارية؟

 ج2: بالتأكيد! Aspose.3D هو منتج تجاري، ويمكنك شرائه[هنا](https://purchase.aspose.com/buy).

### س3: هل أحتاج إلى ترخيص مؤقت للاختبار؟

ج3: نعم، يمكنك الحصول على ترخيص مؤقت لأغراض الاختبار[هنا](https://purchase.aspose.com/temporary-license/).

### س4: أين يمكنني العثور على الدعم لـ Aspose.3D؟

 ج4: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع والمناقشات.

### س5: هل هناك نسخة تجريبية مجانية متاحة؟

 ج5: نعم، يمكنك استكشاف نسخة تجريبية مجانية[هنا](https://releases.aspose.com/).