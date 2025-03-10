---
title: تطبيق مادة PBR على الصندوق
linktitle: تطبيق مادة PBR على الصندوق
second_title: Aspose.3D.NET API
description: استكشف عالم الرسومات ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. قم بإنشاء مشاهد غامرة دون عناء باستخدام مواد العرض المادية.
weight: 10
url: /ar/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تطبيق مادة PBR على الصندوق

## مقدمة

مرحبًا بك في عالم الرسومات ثلاثية الأبعاد الرائع! في هذا الدليل التفصيلي، سنستكشف مكتبة Aspose.3D لـ .NET القوية ونتعلم كيفية إنشاء مشاهد ثلاثية الأبعاد مذهلة باستخدام مواد العرض الفعلي (PBR). يعمل Aspose.3D على تبسيط العملية المعقدة للرسومات ثلاثية الأبعاد ويفتح عالمًا من الإمكانيات للمطورين.

## المتطلبات الأساسية

قبل أن نتعمق في عالم الرسومات ثلاثية الأبعاد المثير، دعنا نتأكد من إعداد كل شيء لديك:

### قم بتنزيل وتثبيت Aspose.3D لـ .NET

 قم بزيارة[Aspose.3D لتوثيق .NET](https://reference.aspose.com/3d/net/) للحصول على تعليمات مفصلة حول تنزيل المكتبة وتثبيتها.

### الحصول على ترخيص

لفتح الإمكانات الكاملة لـ Aspose.3D، احصل على ترخيص صالح. يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/) أو شراء ترخيص كامل[هنا](https://purchase.aspose.com/buy).

## استيراد مساحات الأسماء

أولاً، تأكد من استيراد مساحات الأسماء اللازمة للاستفادة من إمكانيات Aspose.3D لـ .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## الخطوة 1: تهيئة المشهد

ابدأ بتهيئة مشهد ثلاثي الأبعاد باستخدام مقتطف التعليمات البرمجية التالي:

```csharp
Scene scene = new Scene();
```

## الخطوة 2: تهيئة مادة PBR

قم بإنشاء كائن مادة PBR لتحقيق عرض واقعي:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## الخطوة 3: تعيين خصائص المواد

صقل خصائص المواد، مما يجعلها شبه معدنية وخشنة للغاية:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## الخطوة 4: إنشاء صندوق

قم بإنشاء مربع سيتم تطبيق مادة PBR عليه:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## الخطوة 5: تطبيق المواد على الصندوق

قم بتعيين مادة PBR إلى عقدة الصندوق التي تم إنشاؤها:

```csharp
boxNode.Material = mat;
```

## الخطوة 6: احفظ المشهد ثلاثي الأبعاد

احفظ المشهد ثلاثي الأبعاد بتنسيق STL باستخدام دليل الإخراج المطلوب:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

تهانينا! لقد نجحت في تطبيق مادة PBR على صندوق في مشهد ثلاثي الأبعاد باستخدام Aspose.3D لـ .NET.

## خاتمة

إن المغامرة في الرسومات ثلاثية الأبعاد باستخدام Aspose.3D for .NET تفتح الأبواب أمام إمكانيات إبداعية لا نهاية لها. بفضل واجهة برمجة التطبيقات البديهية والميزات القوية، يصبح إنشاء مشاهد مذهلة بصريًا تجربة ممتعة للمطورين.

## الأسئلة الشائعة

### س1: هل Aspose.3D متوافق مع تنسيقات الملفات ثلاثية الأبعاد الأخرى؟

ج1: نعم، يدعم Aspose.3D العديد من تنسيقات الملفات ثلاثية الأبعاد، مما يضمن المرونة في مشروعاتك.

### س2: هل يمكنني استخدام Aspose.3D للتطبيقات التجارية؟

ج2: بالتأكيد! يوفر Aspose.3D تراخيص تجارية للتكامل السلس في تطبيقاتك.

### س3: هل هناك نسخة تجريبية متاحة؟

 ج3: نعم، يمكنك استكشاف إمكانيات Aspose.3D عن طريق تنزيل النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).

### س4: أين يمكنني العثور على دعم المجتمع والمناقشات؟

 ج4: انضم إلى مجتمع Aspose.3D على[منتديات Aspose.3D](https://forum.aspose.com/c/3d/18) للدعم والمناقشات.

### س5: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D؟

 ج5: يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/) لأغراض التقييم.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
