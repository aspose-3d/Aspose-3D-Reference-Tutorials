---
title: تويست أوفست في النتوء الخطي
linktitle: تويست أوفست في النتوء الخطي
second_title: Aspose.3D.NET API
description: اكتشف سحر Aspose.3D لـ .NET من خلال دليلنا خطوة بخطوة حول Twist Offset في Linear Extrusion. ارفع مستوى مشروعاتك ثلاثية الأبعاد دون عناء.
type: docs
weight: 15
url: /ar/net/linear-extrusion/twist-offset-in-linear-extrusion/
---
## مقدمة

مرحبًا بك في عالم Aspose.3D for .NET، وهي مكتبة متعددة الاستخدامات تمكن المطورين من التعامل مع المعالجة ثلاثية الأبعاد بسهولة. في هذا البرنامج التعليمي، سوف نتعمق في إحدى الميزات المثيرة للاهتمام - "Twist Offset in Linear Extrusion". إذا كنت مستعدًا لرفع مستوى مهاراتك في البرمجة ثلاثية الأبعاد، فلنتعمق في الأمر!

## المتطلبات الأساسية

قبل أن نبدأ هذه الرحلة المثيرة، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D for .NET Library: قم بتنزيل المكتبة وتثبيتها من[صفحة الإصدار](https://releases.aspose.com/3d/net/).

- بيئة التطوير الخاصة بك: تأكد من إعداد بيئة التطوير الخاصة بك وجاهزة للتشغيل.

## استيراد مساحات الأسماء

ابدأ باستيراد مساحات الأسماء الضرورية للوصول إلى الوظائف التي يوفرها Aspose.3D لـ .NET. في التعليمات البرمجية الخاصة بك، قد يبدو هذا كما يلي:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

الآن، دعونا نقسم المثال إلى خطوات يمكن التحكم فيها لإتقان Twist Offset في Linear Extrusion:

## الخطوة 1: تهيئة ملف التعريف الأساسي

ابدأ بإنشاء ملف تعريف أساسي، يتمثل هنا في شكل مستطيل بنصف قطر تقريب محدد.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## الخطوة 2: إنشاء مشهد

قم بإنشاء مشهد ثلاثي الأبعاد لاستضافة العقد والأشكال الخاصة بك.

```csharp
Scene scene = new Scene();
```

## الخطوة 3: إنشاء العقد

قم ببناء العقد داخل المشهد، على كلا الجانبين الأيسر والأيمن.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## الخطوة 4: النتوء الخطي على العقدة اليسرى

إجراء قذف خطي على العقدة اليسرى باستخدام خاصية الالتواء والشرائح.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## الخطوة 5: النتوء الخطي على العقدة اليمنى مع إزاحة ملتوية

على العقدة اليمنى، قم بإجراء قذف خطي باستخدام خاصية الالتواء والإزاحة والشرائح.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## الخطوة 6: حفظ المشهد ثلاثي الأبعاد

احفظ المشهد ثلاثي الأبعاد في دليل الإخراج المطلوب، مع تحديد تنسيق الملف كـ WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

تهانينا! لقد نجحت في تنفيذ Twist Offset في Linear Extrusion باستخدام Aspose.3D لـ .NET.

## خاتمة

في هذا البرنامج التعليمي، اكتشفنا الإمكانات القوية لـ Aspose.3D لـ .NET، مع التركيز بشكل خاص على Twist Offset في Linear Extrusion. باستخدام هذه المهارات المكتشفة حديثًا، أنت مجهز جيدًا لإضفاء الديناميكية على مشاريعك ثلاثية الأبعاد.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ .NET مع لغات البرمجة الأخرى؟

ج1: يدعم Aspose.3D بشكل أساسي لغات .NET، لكن Aspose يوفر مكتبات مشابهة لـ Java والأنظمة الأساسية الأخرى.

### س2: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D لـ .NET؟

 ج2: زيارة[هذا الرابط](https://purchase.aspose.com/temporary-license/) للحصول على ترخيص مؤقت لأغراض الاختبار.

### س3: هل يوجد منتدى مجتمعي لـ Aspose.3D لـ .NET؟

ج3: بالتأكيد! انضم إلى المجتمع في[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للتعامل مع زملائك المطورين وطلب المساعدة.

### س4: هل هناك أمثلة ووثائق إضافية متاحة؟

 ج4: اكتشف[توثيق](https://reference.aspose.com/3d/net/) للحصول على أدلة وأمثلة واسعة النطاق.

### س5: أين يمكنني شراء Aspose.3D لـ .NET؟

 ج5: توجه إلى[هذا الرابط](https://purchase.aspose.com/buy) لإجراء عملية شراء وفتح الإمكانات الكاملة لـ Aspose.3D.