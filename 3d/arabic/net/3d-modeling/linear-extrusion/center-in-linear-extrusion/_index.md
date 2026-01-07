---
date: 2026-01-07
description: تعلم كيفية إضافة سطح الأرض أثناء تنفيذ البثق الخطي باستخدام Aspose.3D
  لـ .NET وتصدير ملفات Wavefront OBJ. إتقان تقنيات التمركز والتثبيت في النمذجة ثلاثية
  الأبعاد.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: إضافة سطح أرضي ومركز في البثق الخطي
url: /ar/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إضافة مستوى الأرض والتمركز في البثق الخطي

## المقدمة

مرحبًا بك في هذا الدليل الشامل لإتقان البثق الخطي باستخدام Aspose.3D for .NET. إذا كنت ترغب في **إضافة مستوى الأرض** إلى نماذجك و**تصدير ملفات Wavefront OBJ** مع الحفاظ على تمركز البثق، فأنت في المكان الصحيح. في هذا الشرح، سنستعرض تقنية البثق الخطي، مع التركيز بشكل خاص على جانب التمركز وكيف يساعدك مستوى الأرض على تصور النتيجة بوضوح أكبر.

## إجابات سريعة
- **ما الذي يحققه “إضافة مستوى الأرض”؟** يوفر مرجعًا بصريًا يجعل من السهل رؤية مكان وضع البثق على مستوى X‑Z.  
- **ما هو التنسيق المستخدم لتصدير النموذج؟** يتم حفظ المشهد كملف Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **هل أحتاج إلى ترخيص لتشغيل الكود؟** النسخة التجريبية المجانية تكفي للتطوير؛ يلزم ترخيص دائم للإنتاج.  
- **هل يمكنني تغيير طول البثق؟** نعم – عدل المعامل الثاني لـ `LinearExtrusion`.  
- **هل التمركز اختياري؟** ضبط `Center = true` يضع البثق في مركز الملف التعريفي؛ `false` يضعه على جانب واحد.

## المتطلبات المسبقة

قبل أن نبدأ هذه الرحلة المثيرة، تأكد من توفر المتطلبات التالية:

- فهم أساسي للغة البرمجة C#.  
- تثبيت Visual Studio على جهازك.  
- مكتبة Aspose.3D for .NET، والتي يمكنك تحميلها من [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- تأكد من إمكانية الوصول إلى [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) للرجوع إليها طوال الشرح.

## استيراد مساحات الأسماء

لبدء العمل، لنقم باستيراد مساحات الأسماء الضرورية. هذه ستضع الأساس لتحفتنا في نمذجة ثلاثية الأبعاد.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## الخطوة 1: تهيئة الملف التعريفي الأساسي

نبدأ بتعريف ملف تعريفي مستطيل سيتم بثقّه. يضيف `RoundingRadius` انحناءً خفيفًا إلى الزوايا.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## الخطوة 2: إنشاء مشهد ثلاثي الأبعاد

كائن `Scene` يعمل كحاوية لجميع الهندسات، الإضاءة، والكاميرات.

```csharp
Scene scene = new Scene();
```

## الخطوة 3: إنشاء عقد اليسار واليمين

يتم إنشاء عقدتين شقيتين تحت الجذر. واحدة ستظهر البثق **بدون** تمركز، والأخرى **مع** تمركز. كما نقوم بترجمة العقدة اليسرى حتى لا تتداخل المثالين.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## الخطوة 4: تنفيذ البثق الخطي على العقدة اليسرى (بدون تمركز)

هنا نقوم ببطخ الملف التعريفي دون تمركز. لاحظ علامة `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## الخطوة 5: إضافة مستوى الأرض للمرجعية (العقدة اليسرى)

إضافة صندوق رقيق يعمل كـ **مستوى أرض** حتى تتمكن من رؤية كيفية وضع البثق على القاعدة بوضوح.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## الخطوة 6: تنفيذ البثق الخطي على العقدة اليمنى (مع تمركز)

الآن نقوم ببطخ نفس الملف التعريفي لكن مع تمكين التمركز. سيتم وضع الهندسة بشكل متماثل حول أصل الملف التعريفي.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## الخطوة 7: إضافة مستوى الأرض للمرجعية (العقدة اليمنى)

يتم إضافة مستوى أرض ثانٍ إلى العقدة اليمنى للحفاظ على مقارنة بصرية متسقة.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## الخطوة 8: تصدير ملف Wavefront OBJ

أخيرًا، **نقوم بتصدير Wavefront OBJ** حتى يمكن فتح النتيجة في أي عارض ثلاثي الأبعاد قياسي.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## لماذا نضيف مستوى الأرض؟

إضافة مستوى الأرض يمنحك إشارة بصرية فورية حول ارتفاع البثق ومحاذاته. يكون ذلك مفيدًا بشكل خاص عندما تحتاج إلى مقارنة النتائج المتمركزة مقابل غير المتمركزة، كما هو موضح في هذا الشرح.

## المشكلات الشائعة والنصائح

- **Ground plane not visible:** تأكد من أن سمك المستوى (`0.01` في مُنشئ `Box`) صغير بما يكفي لا يغطي البثق ولكنه كبير بما يكفي ليتم عرضه.  
- **Export fails:** تحقق من وجود دليل الإخراج وأن لديك صلاحيات الكتابة.  
- **Centered extrusion appears offset:** أعد فحص خاصية `Center`؛ `true` يضع الملف التعريفي في المركز، `false` يضعه على جانب واحد.

## الأسئلة المتكررة

### س1: هل يمكنني استخدام Aspose.3D for .NET مع لغات برمجة أخرى؟
A1: يدعم Aspose.3D أساسًا لغات .NET مثل C# و VB.NET.

### س2: أين يمكنني العثور على الدعم للاستفسارات المتعلقة بـ Aspose.3D؟
A2: قم بزيارة [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) للحصول على دعم مخصص ومناقشات.

### س3: هل هناك نسخة تجريبية مجانية متاحة لـ Aspose.3D for .NET؟
A3: نعم، يمكنك الوصول إلى النسخة التجريبية المجانية [من هنا](https://releases.aspose.com/).

### س4: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D for .NET؟
A4: يمكنك الحصول على ترخيص مؤقت [من هنا](https://purchase.aspose.com/temporary-license/).

### س5: أين يمكنني شراء ترخيص Aspose.3D for .NET؟
A5: قم بشراء الترخيص الخاص بك [من هنا](https://purchase.aspose.com/buy).

### س6: هل يمكنني تصدير المشهد إلى صيغ أخرى غير OBJ؟
A6: نعم، يدعم Aspose.3D العديد من الصيغ مثل STL و FBX و GLTF. ما عليك سوى تغيير قيمة تعداد `FileFormat` في طريقة `Save`.

### س7: كيف يمكنني تغيير عدد الشرائح في البثق؟
A7: قم بضبط خاصية `Slices` في مُنشئ `LinearExtrusion` للتحكم في كثافة الشبكة.

**آخر تحديث:** 2026-01-07  
**تم الاختبار مع:** أحدث إصدار من Aspose.3D for .NET  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}