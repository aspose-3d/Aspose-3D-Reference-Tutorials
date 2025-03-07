---
title: تحويل العقدة بواسطة زوايا أويلر
linktitle: تحويل العقدة بواسطة زوايا أويلر
second_title: Aspose.3D.NET API
description: تعلم كيفية تحويل العقد ثلاثية الأبعاد بسهولة باستخدام Aspose.3D لـ .NET. اتبع دليلنا خطوة بخطوة للحصول على نتائج مذهلة في مشاريعك.
weight: 19
url: /ar/net/geometry-and-hierarchy/transformation-node-euler-angles/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تحويل العقدة بواسطة زوايا أويلر

## مقدمة

مرحبًا بك في هذا البرنامج التعليمي الشامل حول تحويل العقد بواسطة زوايا أويلر في مشاهد ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. في هذا الدليل، سوف نتعمق في عالم الرسومات ثلاثية الأبعاد المثير ونستكشف عملية إضافة التحويلات إلى العقدة باستخدام زوايا أويلر. يوفر Aspose.3D for .NET أدوات قوية للعمل مع المشاهد والشبكات ثلاثية الأبعاد، مما يجعله خيارًا ممتازًا للمطورين الذين يبحثون عن التنوع والكفاءة في مشاريعهم.

## المتطلبات الأساسية

قبل أن نتعمق في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D لمكتبة .NET: تأكد من تثبيت مكتبة Aspose.3D. يمكنك تنزيله[هنا](https://releases.aspose.com/3d/net/).

- بيئة التطوير: قم بإعداد بيئة تطوير .NET المفضلة لديك، مثل Visual Studio.

## استيراد مساحات الأسماء

ابدأ باستيراد مساحات الأسماء الضرورية للوصول إلى الوظائف التي يوفرها Aspose.3D لـ .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

الآن، دعونا نقسم المثال إلى خطوات متعددة لفهم واضح.

## الخطوة 1: تهيئة كائن المشهد

```csharp
// ExStart:AddTransformationToNodeByEulerAngles
// تهيئة كائن المشهد
Scene scene = new Scene();
```

 ابدأ بإنشاء مشهد ثلاثي الأبعاد جديد باستخدام`Scene` فصل.


## الخطوة 2: إنشاء شبكة باستخدام الصندوق البدائي

```csharp
// استدعاء الفئة المشتركة لإنشاء شبكة باستخدام طريقة إنشاء المضلع لتعيين مثيل الشبكة
Mesh mesh = (new Box()).ToMesh();
```

 استدعاء طريقة (في هذه الحالة،`CreateMeshUsingPolygonBuilder` من العرف`Common`class) لإنشاء شبكة للكائن ثلاثي الأبعاد.

## الخطوة 3: إنشاء عقدة حاوية للشبكة

```csharp
// نقطة العقدة إلى هندسة الشبكة
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

 قم بإنشاء عقدة داخل المشهد باستخدام`Node` فصل. ستكون هذه العقدة بمثابة حاوية لكائننا ثلاثي الأبعاد.

## الخطوة 4: ضبط زوايا أويلر والترجمة

```csharp
// زوايا أويلر
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// تعيين الترجمة
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

حدد زوايا أويلر وترجمتها للعقدة لوضعها في الفضاء ثلاثي الأبعاد.

## الخطوة 5: احفظ المشهد ثلاثي الأبعاد

```csharp
// المسار إلى دليل المستندات.
var output = "TransformationToNode.fbx";

// حفظ المشهد ثلاثي الأبعاد بتنسيقات الملفات المدعومة
scene.Save(output);
// ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

حدد دليل الإخراج واحفظ المشهد ثلاثي الأبعاد، بما في ذلك العقدة المحولة، بتنسيق الملف المطلوب (FBX7500ASCII في هذه الحالة).

## خاتمة

تهانينا! لقد تعلمت بنجاح كيفية تحويل عقدة بواسطة زوايا أويلر في مشاهد ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. تفتح هذه المكتبة القوية الباب أمام إمكانيات لا حصر لها في تطوير الرسومات ثلاثية الأبعاد.

## الأسئلة الشائعة

### س1: هل Aspose.3D متوافق مع أدوات النمذجة ثلاثية الأبعاد الأخرى؟

ج1: يدعم Aspose.3D العديد من تنسيقات الملفات ثلاثية الأبعاد، مما يعزز التوافق مع أدوات التصميم الشائعة.

### س2: هل يمكنني تطبيق تحويلات متعددة على عقدة واحدة؟

ج2: نعم، يمكنك دمج وتطبيق تحويلات متعددة لتحقيق تأثيرات معقدة.

### س3: أين يمكنني العثور على وثائق Aspose.3D إضافية؟

 ج3: راجع[توثيق](https://reference.aspose.com/3d/net/) للحصول على معلومات وأمثلة مفصلة.

### س4: هل أحتاج إلى ترخيص لاستخدام Aspose.3D لـ .NET؟

 ج4: نعم، يمكنك الحصول على ترخيص[هنا](https://purchase.aspose.com/buy) أو استكشاف أ[تجربة مجانية](https://releases.aspose.com/).

### س5: هل تحتاج إلى مساعدة أو لديك أسئلة محددة؟

 ج5: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
