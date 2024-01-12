---
title: الاتجاه في النتوء الخطي
linktitle: الاتجاه في النتوء الخطي
second_title: Aspose.3D.NET API
description: أطلق العنان لعالم النمذجة ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. تعلم اتجاه البثق الخطي، وعزز الإبداع، واصنع تطبيقات غامرة دون عناء.
type: docs
weight: 11
url: /ar/net/linear-extrusion/direction-in-linear-extrusion/
---
## مقدمة

في عالم تطوير البرمجيات الديناميكي، يعد إنشاء نماذج ثلاثية الأبعاد غامرة مهارة لا غنى عنها. يوفر Aspose.3D for .NET للمطورين مجموعة قوية من الأدوات لتسخير إمكانات النمذجة ثلاثية الأبعاد في تطبيقاتهم. في هذا البرنامج التعليمي، سوف نتعمق في عالم البثق الخطي المثير للاهتمام ونستكشف الفروق الدقيقة في ميزة "الاتجاه في البثق الخطي".

## المتطلبات الأساسية

قبل أن نبدأ هذه الرحلة المثيرة، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D لـ .NET: قم بتنزيل المكتبة وتثبيتها من[وثائق Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- بيئة التطوير: تأكد من إعداد بيئة تطوير .NET صالحة للعمل.

## استيراد مساحات الأسماء

في مشروع .NET الخاص بك، قم باستيراد مساحات الأسماء الضرورية للوصول إلى وظائف Aspose.3D. أضف الأسطر التالية إلى بداية الكود الخاص بك:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## الخطوة 1: تهيئة ملف التعريف الأساسي

ابدأ بتهيئة ملف التعريف الأساسي المراد قذفه. في هذا المثال، قمنا بإنشاء شكل مستطيل بنصف قطر تقريب قدره 0.3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## الخطوة 2: إنشاء مشهد ثلاثي الأبعاد

قم ببناء الأساس لتحفتك الفنية ثلاثية الأبعاد من خلال إنشاء مشهد.

```csharp
Scene scene = new Scene();
```

## الخطوة 3: إنشاء العقد

قم بإنشاء العقد داخل المشهد لتمثيل المكونات المختلفة لبيئتك ثلاثية الأبعاد.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## الخطوة 4: البثق الخطي بدون اتجاه

 إجراء قذف خطي على العقدة اليسرى باستخدام`Twist` و`Slices` ملكيات.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## الخطوة 5: البثق الخطي مع الاتجاه

 توسيع قدرات البثق من خلال دمج`Direction` الملكية في العقدة اليمنى.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## الخطوة 6: احفظ المشهد ثلاثي الأبعاد

 حافظ على إبداعك عن طريق حفظ المشهد ثلاثي الأبعاد. يستبدل`"Your Output Directory"` مع الدليل المطلوب

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

تهانينا! لقد نجحت في تنفيذ البثق الخطي باستخدام Aspose.3D لـ .NET، واستكشاف كل من الأساليب التقليدية والاتجاهية.

## خاتمة

في هذا البرنامج التعليمي، انتقلنا عبر عالم النمذجة ثلاثية الأبعاد الرائع باستخدام Aspose.3D لـ .NET. يفتح البثق الخطي، مع الاتجاه وبدونه، إمكانيات لا حصر لها للمطورين الذين يسعون إلى إنشاء تطبيقات مذهلة بصريًا. مع Aspose.3D، أصبحت قوة النمذجة ثلاثية الأبعاد في متناول يدك.

## الأسئلة الشائعة

### س1: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D لـ .NET؟

 ج1: زيارة[Aspose الترخيص المؤقت](https://purchase.aspose.com/temporary-license/) للحصول على ترخيص مؤقت.

### س2: أين يمكنني العثور على الدعم لـ Aspose.3D؟

 ج2: انضم إلى[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لطلب المساعدة والتواصل مع المجتمع.

### س3: هل هناك نسخة تجريبية مجانية متاحة؟

 ج3: نعم، استكشف الميزات من خلال النسخة التجريبية المجانية على[إصدارات Aspose.3D](https://releases.aspose.com/).

### س4: كيف يمكنني شراء Aspose.3D لـ .NET؟

 A4: انتقل إلى[Aspose صفحة الشراء](https://purchase.aspose.com/buy) للحصول على خيارات الترخيص وتفاصيل الشراء.

### س5: أين يمكنني العثور على الوثائق التفصيلية لـ Aspose.3D لـ .NET؟

 ج5: راجع الشامل[وثائق Aspose.3D .NET](https://reference.aspose.com/3d/net/) للحصول على معلومات متعمقة.