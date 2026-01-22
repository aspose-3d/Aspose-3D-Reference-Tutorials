---
date: 2026-01-22
description: تعلم كيفية تطبيق مصفوفة التحويل على عقدة في Aspose.3D لـ .NET، وتحويل
  المشهد إلى FBX، وتطبيق تحولات متعددة باستخدام كود خطوة بخطوة.
linktitle: Apply Transformation Matrix to a Node – Aspose.3D for .NET
second_title: Aspose.3D .NET API
title: تطبيق مصفوفة التحويل على عقدة – Aspose.3D لـ .NET
url: /ar/net/geometry-and-hierarchy/transformation-node-matrix/
weight: 21
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تطبيق مصفوفة التحويل على عقدة

## مقدمة

في رسومات 3D الحديثة، **تطبيق مصفوفة التحويل** على عقدة هو الأساس لتحريك أو تدوير أو تحجيم الكائنات بدقة. باستخدام Aspose.3D لـ .NET يمكنك بسهولة **تطبيق مصفوفة التحويل** على أي عقدة، مما يمنحك السيطرة الإبداعية الكاملة على المشهد. هذا الدليل يشرح لك العملية بالكامل—من إنشاء صندوق شبكة إلى تحويل المشهد إلى FBX—حتى تتمكن من رؤية النتائج فورًا.

## إجابات سريعة
- **ماذا يفعل “apply transformation matrix”?** إنه يغيّر موضع العقدة أو اتجاهها أو مقياسها باستخدام مصفوفة 4×4.  
- **ما هو تنسيق الملف الذي يمكنني التصدير إليه؟** يمكنك **تحويل المشهد إلى FBX** (أ متعددة** عن طريق ضرب المما إصدارات .NET المدعومة؟** .NET Framework 4.5+، .NET Core 3.1+، .NET 5/6 وما بعدها.

## ما هي مصفوفة التحويل؟

مصفوفة التحويل هي شبكة رقمية 4 × 4 تشفر الترجمة، الدوران، التحجيم، أو أي تركيبة من هذه العمليات عندما تُعيّن هذه المصفوفة إلى عقدة، يتم تحويل هندسة العقدة وفقًا لذلك في مساحة العالم ثلاثية الأبعاد.

## لماذا تستخدم Aspose.3D لتحويلات العقد؟

- **واجهة برمجة تطبيقات عالية المستوى** – منخفضة المستوى؛ Aspose يتعامل مع إنشاء المصفوفة وتطبيقها.  
- **دعم واسع للتنسيقات** – احفظ مباشرة إلى FBX، STL3D لـ .NET** – حمّلها [هنا](https://reVisual) مع مشروع وحدة تحكم أو مكتبة فئات جديد.  

## استيراد مساحات الأسماء

ابدأ باستيراد مساحات الأسماء الأساسية التي تمنحك الوصول إلى فئات محرك 3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

الآن دعنا نفصل سير عمل التحويل خطوة بخطوة.

## كيفية تطبيق مصفوفة التحويل على عقدة

### الخطوة 1: تهيئة مشهد جديد

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix            
// Initialize scene object
Scene scene = new Scene();

```

إنشاء `Scene` جديد يمنحك لوحة رسم نظيفة حيث ستضيف الهندسة والتحويلات.

### الخطوة 2: إنشاء صندوق شبكة وإرفاقه بالمشهد

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = (new Box()).ToMesh();

// Create a container node for the mesh.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

هنا نقوم **بإنشاء صندوق شبكة** باستخدام الكائن الأولي المدمج `Box` ونرفقه بعقدة فرعية جديدة تسمى `cubeNode`. ستكون هذه العقدة هدف تحويلنا.

### الخطوة 3: تعيين مصفوفة ترجمة مخصصة (Apply Transformation Matrix)

```csharp
// Set custom translation matrix
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

منشئ `Matrix4` يحدد مصفوفة 4 × 4. اضبط القيم لتحقيق الترجمة أو الدوران أو التحجيم المطلوب. في هذا المثال نقوم بترجمة المكعب 20 وحدة على المحور Y مع تطبيق قص بسيط.

> **نصيحة احترافية:** لتطبيق **تحولات متعددة**، اضرب مصفوفات إضافية مع المصفوفة الحالية قبل تعيينها إلى `TransformMatrix`.

### الخطوة 4: حفظ المشهد – تحويل المشهد إلى FBX

```csharp
// The path to the documents directory.
var output = "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

نختار تنسيق FBX لهذا المثال، وبالتالي **تحويل المشهد إلى FBX**. Aspose.3D يختار تلقائيًا نسخة FBX المناسبة بناءً على امتداد الملف.

## المشكلات الشائعة والحلول

| المشكلة | الحل |
|-------|----------|
| العقدة تظهر دون تغيير | تحقق من أن قيم المصفوفة ليست هوية (أي ليست جميعها أصفار ما عدا القطر). |
| ملف FBX المُصدّر يبدو مشوّهًا | تأكد من أنك تستخدم أحدث نسخة من Aspose.3D وأن المصفوفة تحترم قواعد نظام الإحداثيات الأيمن. |
| استثناء الترخيص أثناء التشغيل | طبق ترخيصًا مؤقتًا أو كاملاً قبل استدعاء أي من واجهات Aspose. |

## الأسئلة المتكررة

### س1: ما هي مصفوفة التحويل في رسومات 3D؟

**ج:** إنها تمثيل رياضي يشفر الترجمة، الدوران، التحجيم، أو أي تركيبة من هذه العمليات، مما يتيح لك **تطبيق مصفوفة التحويل** على الكائنات.

### س2: هل يمكنني **تطبيق تحولات متعددة** على عقدة واحدة؟

**ج:** نعم. اضرب المصفوفات الفردية (مثلاً، ترجمة × دوران × تحجيم) وعيّن المصفاة الناتجة إلى `TransformMatrix` الخاصة بالعقدة.

### س3: ما هي تنسيقات الملفات التي يمكنني **تحويل المشهد إلى FBX** أو أنواع أخرى؟

**ج:** Aspose.3D يدعم FBX، STL، GLTF، OBJ، 3MF، وأكثر. راجع القائمة الكاملة في [التوثيق](https://reference.aspose.com/3d/net/).

### س4: كيف أحصل على ترخيص مؤقت لـ Aspose.3D لـ .NET؟

**ج:** زر [صفحة الترخيص المؤقت](https://purchase.aspose.com/temporary-license/) لطلب ترخيص تجريبي.

### س5: أين يمكنني الحصول على دعم المجتمع لـ Aspose.3D؟

**ج:** انضم إلى النقاش في [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لطرح الأسئلة ومشاركة التجارب.

## الخلاصة

لقد تعلمت الآن كيفية **تطبيق مصفوفة التحويل** على عقدة، إنشاء صندوق شبكة، و**تحويل المشهد إلى FBX** باستخدام Aspose.3D لـ .NET. تفتح هذه التقنيات الباب أمام تطبيقات 3D متقدمة مثل العارضات التفاعلية، خطوط أنابيب أصول الألعاب، وتوليد المشاهد تلقائيًا.

---

**آخر تحديث:** 2026-01-22  
**تم الاختبار مع:** Aspose.3D 24.11 for .NET  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}