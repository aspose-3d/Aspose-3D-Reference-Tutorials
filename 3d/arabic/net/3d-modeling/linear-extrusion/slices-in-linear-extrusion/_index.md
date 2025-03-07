---
title: شرائح في النتوء الخطي
linktitle: شرائح في النتوء الخطي
second_title: Aspose.3D.NET API
description: استكشف عالم التصميم ثلاثي الأبعاد باستخدام Aspose.3D لـ .NET. قم بإنشاء نماذج مذهلة باستخدام برنامجنا التعليمي للبثق الخطي.
weight: 13
url: /ar/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# شرائح في النتوء الخطي

## مقدمة

مرحبًا بك في عالم التصميم ثلاثي الأبعاد باستخدام Aspose.3D لـ .NET! سواء كنت مطورًا متمرسًا أو بدأت للتو، سيرشدك هذا البرنامج التعليمي خلال عملية إنشاء تصورات ثلاثية الأبعاد مذهلة باستخدام مكتبة Aspose.3D القوية.

## المتطلبات الأساسية

قبل الغوص في عالم التصميم ثلاثي الأبعاد مع Aspose.3D، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D لمكتبة .NET: تأكد من تثبيت مكتبة Aspose.3D. يمكنك تنزيله من[هنا](https://releases.aspose.com/3d/net/).

- بيئة التطوير المتكاملة (IDE): استخدم أي بيئة تطوير متكاملة مفضلة متوافقة مع تطوير .NET.

- الفهم الأساسي لـ C#: تعرف على أساسيات لغة البرمجة C#.

- الرغبة في استكشاف التصميم ثلاثي الأبعاد: شغف لإنشاء نماذج ثلاثية الأبعاد مذهلة بصريًا!

## استيراد مساحات الأسماء

لبدء رحلة التصميم ثلاثي الأبعاد باستخدام Aspose.3D، ستحتاج إلى استيراد مساحات الأسماء الضرورية. وهذا يضمن أن التعليمات البرمجية الخاصة بك يمكنها الوصول إلى الفئات والوظائف المطلوبة.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## النتوء الخطي - شرائح في النتوء الخطي

الآن، دعونا نتعمق في مثال عملي - النتوء الخطي بالشرائح. تتيح لك هذه التقنية إنشاء نماذج ثلاثية الأبعاد معقدة بمستويات مختلفة من التفاصيل.

### الخطوة 1: تهيئة ملف التعريف الأساسي

```csharp
// ExStart: تهيئة الملف الشخصي الأساسي
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd: تهيئة الملف الشخصي الأساسي
```

### الخطوة 2: إنشاء مشهد ثلاثي الأبعاد

```csharp
// ExStart: إنشاء مشهد ثلاثي الأبعاد
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### الخطوة 3: إنشاء العقد اليسرى واليمنى

```csharp
// ExStart: إنشاء العقد اليسرى واليمنى
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### الخطوة 4: إجراء البثق الخطي على العقدة اليسرى

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### الخطوة 5: إجراء البثق الخطي على العقدة اليمنى

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### الخطوة 6: حفظ المشهد ثلاثي الأبعاد

```csharp
// ExStart: Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
//ExEnd:Save3DScene
```

## خاتمة

تهانينا! لقد تعلمت بنجاح كيفية تنفيذ عملية البثق الخطي باستخدام الشرائح باستخدام Aspose.3D لـ .NET. هذه مجرد بداية لرحلة التصميم ثلاثي الأبعاد مع Aspose.3D - أطلق العنان لإبداعك واستكشف الاحتمالات التي لا نهاية لها!

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ .NET مع لغات البرمجة الأخرى؟

ج1: تم تصميم Aspose.3D بشكل أساسي لـ .NET، ولكن يمكنك استكشاف خيارات التشغيل التفاعلي مع لغات مثل Python باستخدام روابط .NET.

### س2: أين يمكنني العثور على الوثائق التفصيلية لـ Aspose.3D لـ .NET؟

 ج2: راجع الوثائق[هنا](https://reference.aspose.com/3d/net/) للحصول على معلومات متعمقة حول إمكانيات Aspose.3D واستخدامه.

### س3: هل تتوفر نسخة تجريبية مجانية من Aspose.3D لـ .NET؟

 ج3: نعم، يمكنك الحصول على النسخة التجريبية المجانية[هنا](https://releases.aspose.com/)لاستكشاف ميزات المكتبة قبل إجراء عملية الشراء.

### س4: كيف يمكنني الحصول على الدعم الفني لـ Aspose.3D لـ .NET؟

 ج4: قم بزيارة منتدى Aspose.3D[هنا](https://forum.aspose.com/c/3d/18) لطلب المساعدة والتفاعل مع المجتمع.

### س5: هل يمكنني استخدام ترخيص مؤقت لـ Aspose.3D لـ .NET؟

 ج5: نعم، احصل على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/) لأغراض التقييم.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
