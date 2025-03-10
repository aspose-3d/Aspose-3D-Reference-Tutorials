---
title: إعداد الأشعة فوق البنفسجية على المكعب
linktitle: إعداد الأشعة فوق البنفسجية على المكعب
second_title: Aspose.3D.NET API
description: تعلم كيفية إعداد تعيين الأشعة فوق البنفسجية على مكعب ثلاثي الأبعاد باستخدام Aspose.3D لـ .NET. قم بإنشاء مشاهد مذهلة بصريًا باستخدام خريطة نسيج دقيقة.
weight: 18
url: /ar/net/geometry-and-hierarchy/setup-uv-cube/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إعداد الأشعة فوق البنفسجية على المكعب

## مقدمة

غالبًا ما يتضمن إنشاء مشاهد ثلاثية الأبعاد جذابة وجذابة بصريًا عملية دقيقة لإعداد خرائط الأشعة فوق البنفسجية على الأشكال الهندسية. في هذا البرنامج التعليمي، سوف نستكشف كيفية إعداد الأشعة فوق البنفسجية على المكعب باستخدام Aspose.3D لـ .NET. Aspose.3D هي مكتبة .NET قوية توفر مجموعة شاملة من الميزات للنمذجة والمعالجة ثلاثية الأبعاد.

## المتطلبات الأساسية

قبل الغوص في البرنامج التعليمي، تأكد من أن لديك المتطلبات الأساسية التالية:

1. Aspose.3D لمكتبة .NET: تأكد من تثبيت مكتبة Aspose.3D. يمكنك تنزيله[هنا](https://releases.aspose.com/3d/net/).

2. بيئة التطوير: قم بإعداد بيئة تطوير .NET باستخدام الأدوات اللازمة.

الآن، دعونا ننتقل إلى البرنامج التعليمي.

## استيراد مساحات الأسماء

أولاً، قم باستيراد مساحات الأسماء الضرورية للوصول إلى وظائف Aspose.3D في تطبيق .NET الخاص بك.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## الخطوة 1: تحديد الأشعة فوق البنفسجية للمكعب

تحديد إحداثيات الأشعة فوق البنفسجية لكل قمة من المكعب. يتضمن ذلك تحديد قيم U وV لكل ركن من أركان المكعب.

```csharp
// ExStart: تحديد الأشعة فوق البنفسجية
Vector4[] uvs = new Vector4[]
{
    new Vector4(0.0, 1.0, 0.0, 1.0),
    new Vector4(1.0, 0.0, 0.0, 1.0),
    new Vector4(0.0, 0.0, 0.0, 1.0),
    new Vector4(1.0, 1.0, 0.0, 1.0)
};
// ExEnd:DefineUVs
```

## الخطوة 2: تحديد مؤشرات الأشعة فوق البنفسجية

حدد مؤشرات إحداثيات الأشعة فوق البنفسجية لكل مضلع من المكعب. يحدد هذا كيفية تعيين الأشعة فوق البنفسجية على أسطح المكعب.

```csharp
// ExStart: تحديد مؤشرات UV
int[] uvsId = new int[]
{
    0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 9, 8, 1, 10, 11, 3, 12, 0, 2, 13
};
// ExEnd:DefineUVIIndices
```

## الخطوة 3: إنشاء شبكة

استخدم مكتبة Aspose.3D لإنشاء شبكة باستخدام طريقة إنشاء المضلعات. سيكون هذا بمثابة الأساس لمكعبنا ثلاثي الأبعاد.

```csharp
// ExStart:CreateMesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
// ExEnd:CreateMesh
```

## الخطوة 4: إنشاء عنصر الأشعة فوق البنفسجية

قم بإنشاء عنصر للأشعة فوق البنفسجية في الشبكة لتخزين بيانات رسم خرائط الأشعة فوق البنفسجية.

```csharp
// ExStart:إنشاءUVElement
VertexElementUV elementUV = mesh.CreateElementUV(TextureMapping.Diffuse, MappingMode.PolygonVertex, ReferenceMode.IndexToDirect);
// ExEnd:CreateUVElement
```

## الخطوة 5: نسخ بيانات الأشعة فوق البنفسجية إلى الشبكة

انسخ إحداثيات ومؤشرات الأشعة فوق البنفسجية المحددة مسبقًا إلى عنصر قمة الأشعة فوق البنفسجية للشبكة.

```csharp
// ExStart:نسخUVData
elementUV.Data.AddRange(uvs);
elementUV.Indices.AddRange(uvsId);
// ExEnd:CopyUVData
```

## خاتمة

تهانينا! لقد قمت بنجاح بإعداد تعيين الأشعة فوق البنفسجية على مكعب باستخدام Aspose.3D لـ .NET. وهذا يفتح إمكانيات إنشاء مشاهد ثلاثية الأبعاد معقدة ومذهلة بصريًا مع رسم خرائط نسيجية دقيقة.

## الأسئلة الشائعة

### س1: ما هو Aspose.3D لـ .NET؟

A1: Aspose.3D for .NET هي مكتبة قوية للنمذجة ثلاثية الأبعاد ومعالجتها في تطبيقات .NET.

### س2: أين يمكنني العثور على وثائق Aspose.3D؟

 ج2: الوثائق متاحة[هنا](https://reference.aspose.com/3d/net/).

### س3: هل هناك نسخة تجريبية مجانية متاحة؟

 ج3: نعم، يمكنك الوصول إلى النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).

### س4: كيف يمكنني الحصول على الدعم لـ Aspose.3D؟

 ج4: قم بزيارة منتدى الدعم[هنا](https://forum.aspose.com/c/3d/18).

### س5: هل التراخيص المؤقتة متاحة؟

 ج5: نعم، يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
