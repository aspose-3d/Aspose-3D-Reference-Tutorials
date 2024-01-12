---
title: تطبيق التأثيرات المرئية في إطارات العرض ثلاثية الأبعاد
linktitle: تطبيق التأثيرات المرئية في إطارات العرض ثلاثية الأبعاد
second_title: Aspose.3D.NET API
description: استكشف عالم التصور ثلاثي الأبعاد باستخدام Aspose.3D لـ .NET. تعلم كيفية تطبيق تأثيرات بصرية جذابة على مشاهدك باستخدام البرامج التعليمية خطوة بخطوة. ارفع مستوى مشروعاتك من خلال تأثيرات البكسل والتدرج الرمادي واكتشاف الحواف والتأثيرات الضبابية.
type: docs
weight: 10
url: /ar/net/3d-viewports/apply-visual-effects/
---
## مقدمة

يعد تحسين المظهر المرئي للمشاهد ثلاثية الأبعاد جانبًا مهمًا لإنشاء تجارب غامرة. يوفر Aspose.3D for .NET مجموعة قوية من الأدوات لتطبيق التأثيرات المرئية على منافذ العرض ثلاثية الأبعاد. في هذا البرنامج التعليمي، سنتعرف على عملية تطبيق تأثيرات متنوعة على مشهد ثلاثي الأبعاد، بما في ذلك البكسل، والتدرج الرمادي، واكتشاف الحواف، والتمويه.

## المتطلبات الأساسية

قبل الغوص في البرنامج التعليمي، تأكد من أن لديك ما يلي:

- معرفة عملية بتطوير C# و.NET.
-  تم تثبيت Aspose.3D لمكتبة .NET. يمكنك تنزيله من[هنا](https://releases.aspose.com/3d/net/).
- ملف مشهد ثلاثي الأبعاد (على سبيل المثال، "scene.obj") للتجريب.

## استيراد مساحات الأسماء

للبدء، قم باستيراد مساحات الأسماء الضرورية لـ Aspose.3D والتبعيات الأخرى. أضف الأسطر التالية إلى الكود الخاص بك:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## الخطوة 1: قم بتحميل مشهد ثلاثي الأبعاد موجود

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 قم بتحميل المشهد ثلاثي الأبعاد الخاص بك باستخدام`Scene` فصل.

## الخطوة 2: إنشاء الكاميرا

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

قم بإنشاء مثيل للكاميرا وقم بتعيين موضعه وهدفه.

## الخطوة 3: إضافة الضوء إلى المشهد

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

إدخال الإضاءة لتعزيز المؤثرات البصرية.

## الخطوة 4: إنشاء العارض والعرض المستهدف

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // تكوين إعدادات العارض
    renderer.EnableShadows = false;

    // قم بإنشاء هدف تقديم
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // تكوين إطار العرض
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // تقديم المشهد إلى الملمس
        renderer.Render(rt);

        // احفظ النسيج المقدم في ملف
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // متابعة تأثيرات ما بعد المعالجة...
    }
}
```

قم بإنشاء عارض وهدف عرض لالتقاط المشهد.

## الخطوة 5: تطبيق تأثيرات ما بعد المعالجة

### الخطوة 5.1 تأثير البكسل

```csharp
// إنشاء تأثير البكسل
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

تطبيق تأثير البكسل وحفظ النتيجة.

### الخطوة 5.2 تأثير التدرج الرمادي

```csharp
// إنشاء تأثير التدرج الرمادي
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

قم بتطبيق تأثير التدرج الرمادي واحفظ النتيجة.

### الخطوة 5.3 الجمع بين التأثيرات

```csharp
// الجمع بين تأثيرات التدرج الرمادي والبيكسلات
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

الجمع بين تأثيرات متعددة للحصول على نتائج فريدة من نوعها.

### الخطوة 5.4 تأثير اكتشاف الحافة

```csharp
// إنشاء تأثير الكشف عن الحافة
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

تطبيق تأثير الكشف عن الحافة وحفظ النتيجة.

### الخطوة 5.5 تأثير الضبابية

```csharp
// إنشاء تأثير طمس
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

تطبيق تأثير طمس وحفظ النتيجة.

## خاتمة

تجربة التأثيرات المرئية في منافذ العرض ثلاثية الأبعاد تضيف عمقًا وإبداعًا إلى مشاهدك. يعمل Aspose.3D for .NET على تبسيط هذه العملية، حيث يقدم مجموعة من تأثيرات ما بعد المعالجة للارتقاء بمشروعاتك.

## الأسئلة الشائعة

### س1: هل يمكنني تطبيق تأثيرات متعددة في وقت واحد؟

ج1: نعم، يمكنك الجمع بين تأثيرات ما بعد المعالجة المختلفة للحصول على نتائج فريدة ومعقدة.

### س2: كيف يمكنني ضبط شدة التأثيرات المرئية؟

ج2: قد يحتوي كل تأثير على معلمات يمكنك تعديلها للتحكم في شدته. راجع الوثائق للحصول على تفاصيل محددة.

### س3: هل Aspose.3D مناسب لتطوير الألعاب؟

ج3: على الرغم من أن Aspose.3D مصمم بشكل أساسي للنمذجة والعرض ثلاثي الأبعاد، إلا أنه يمكن استخدامه في جوانب معينة من تطوير اللعبة.

### س4: هل هناك تأثيرات إضافية متاحة بعد المعالجة؟

ج4: يوفر Aspose.3D مجموعة متنوعة من تأثيرات ما بعد المعالجة المضمنة، ويمكنك إنشاء تأثيرات مخصصة باستخدام المكتبة.

### س5: هل يمكنني استخدام Aspose.3D للمشاريع التجارية؟

 ج5: نعم، يمكنك استخدام Aspose.3D لأغراض تجارية. الرجوع إلى[صفحة الشراء](https://purchase.aspose.com/buy) للحصول على تفاصيل الترخيص.