---
title: مركز في النتوء الخطي
linktitle: مركز في النتوء الخطي
second_title: Aspose.3D.NET API
description: استكشف عالم النمذجة ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. تقنيات البثق الخطي المركزي، قم بإنشاء تصميمات مذهلة، وأطلق العنان لإبداعك.
type: docs
weight: 10
url: /ar/net/linear-extrusion/center-in-linear-extrusion/
---
## مقدمة

مرحبًا بك في هذا الدليل الشامل حول إتقان البثق الخطي باستخدام Aspose.3D لـ .NET. إذا كنت تتطلع إلى تحسين مهاراتك في النمذجة ثلاثية الأبعاد وإنشاء عمليات سحب مذهلة، فأنت في المكان الصحيح. في هذا البرنامج التعليمي، سوف نتعمق في تقنية البثق الخطي، مع التركيز بشكل خاص على الجانب المركزي للارتقاء بتصميماتك إلى مستوى جديد تمامًا.

## المتطلبات الأساسية

قبل أن نبدأ هذه الرحلة المثيرة، تأكد من توفر المتطلبات الأساسية التالية:

- الفهم الأساسي للغة البرمجة C#.
- تم تثبيت Visual Studio على جهازك.
-  Aspose.3D لمكتبة .NET، والتي يمكنك تنزيلها من[وثائق Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  تأكد من أن لديك حق الوصول إلى[وثائق Aspose.3D .NET](https://reference.aspose.com/3d/net/) للرجوع إليها طوال البرنامج التعليمي.

## استيراد مساحات الأسماء

لبدء الأمور، فلنستورد مساحات الأسماء الضرورية. هذه سوف تضع الأساس لتحفة النمذجة ثلاثية الأبعاد لدينا.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## الخطوة 1: تهيئة ملف التعريف الأساسي

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## الخطوة 2: إنشاء مشهد ثلاثي الأبعاد

```csharp
Scene scene = new Scene();
```

## الخطوة 3: إنشاء العقد اليسرى واليمنى

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## الخطوة 4: إجراء البثق الخطي على العقدة اليسرى

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## الخطوة 5: تعيين الطائرة الأرضية كمرجع

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## الخطوة 6: إجراء البثق الخطي على العقدة اليمنى

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## الخطوة 7: تعيين المستوى الأرضي كمرجع (العقدة اليمنى)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## الخطوة 8: حفظ المشهد ثلاثي الأبعاد

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## خاتمة

تهانينا! لقد أتقنت بنجاح فن البثق الخطي مع التوسيط باستخدام Aspose.3D لـ .NET. لا تتردد في تجربة معلمات مختلفة واستكشاف الإمكانيات الهائلة التي توفرها هذه التقنية.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ .NET مع لغات البرمجة الأخرى؟

A1: يدعم Aspose.3D بشكل أساسي لغات .NET مثل C# وVB.NET.

### س2: أين يمكنني العثور على دعم للاستعلامات المتعلقة بـ Aspose.3D؟

 ج2: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على الدعم المخصص والمناقشات.

### س3: هل تتوفر نسخة تجريبية مجانية من Aspose.3D لـ .NET؟

 ج3: نعم، يمكنك الوصول إلى النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).

### س4: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D لـ .NET؟

 ج4: يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).

### س5: أين يمكنني شراء ترخيص Aspose.3D لـ .NET؟

 ج5: قم بشراء الترخيص الخاص بك[هنا](https://purchase.aspose.com/buy).
