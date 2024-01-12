---
title: التقاط منافذ العرض في مشاهد ثلاثية الأبعاد
linktitle: التقاط منافذ العرض في مشاهد ثلاثية الأبعاد
second_title: Aspose.3D.NET API
description: تعلم كيفية التقاط إطارات عرض ثلاثية الأبعاد مذهلة باستخدام Aspose.3D لـ .NET. دليل خطوة بخطوة لعرض المشاهد بمرونة.
type: docs
weight: 11
url: /ar/net/3d-viewports/capture-viewport/
---
## مقدمة

في عالم الرسومات والتصورات ثلاثية الأبعاد، يعد التقاط منافذ العرض مهارة أساسية تعمل على تحسين عمق المشاهد وتفاصيلها. يوفر Aspose.3D for .NET حلاً قويًا لعرض المشاهد ثلاثية الأبعاد ومعالجتها. سيرشدك هذا البرنامج التعليمي خلال عملية التقاط منافذ العرض في مشاهد ثلاثية الأبعاد باستخدام Aspose.3D، مما يسمح لك بإنشاء تصورات مذهلة بسهولة.

## المتطلبات الأساسية

قبل الغوص في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D لمكتبة .NET: تأكد من تثبيت مكتبة Aspose.3D. يمكنك تنزيله من[هنا](https://releases.aspose.com/3d/net/).

## استيراد مساحات الأسماء

للبدء، قم باستيراد مساحات الأسماء الضرورية إلى مشروع .NET الخاص بك:

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

ابدأ بتحميل مشهد ثلاثي الأبعاد موجود في مشروعك. يوضح مقتطف التعليمات البرمجية التالي هذا:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## الخطوة 2: إنشاء الكاميرا

بعد ذلك، قم بإنشاء مثيل للكاميرا وقم بتعيين موضعها وهدفها:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## الخطوة 3: إضافة الإضاءة إلى المشهد

تعزيز المشهد الخاص بك عن طريق إضافة مصدر الضوء. يوضح مقتطف الكود أدناه كيفية إنشاء نقطة ضوئية:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## الخطوة 4: تكوين العارض والعرض المستهدف

قم بإعداد العارض وإنشاء هدف عرض لالتقاط المشهد:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (التكملة في الخطوات التالية)
    }
}
```

## الخطوة 5: تحديد إطارات العرض والعرض

تحديد منافذ العرض وتقديم المشهد لإنشاء صور الإخراج:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## الخطوة 6: تعديل إطارات العرض والعرض مرة أخرى

قم بتعديل إطارات العرض وعرض المشهد مرة أخرى، مما يوضح مرونة Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

استمر في تجربة التكوينات المختلفة لتحقيق التأثيرات المرئية المطلوبة.

## خاتمة

في هذا البرنامج التعليمي، استكشفنا عملية التقاط إطارات العرض في مشاهد ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. ومن خلال الاستفادة من ميزاته القوية، يمكنك الارتقاء بمشاريع الرسومات ثلاثية الأبعاد الخاصة بك إلى آفاق جديدة، مما يوفر تجارب بصرية آسرة.

## الأسئلة الشائعة

### س1: هل Aspose.3D متوافق مع تنسيقات الملفات ثلاثية الأبعاد الأخرى؟

ج1: نعم، يدعم Aspose.3D العديد من تنسيقات الملفات ثلاثية الأبعاد، مما يضمن التوافق مع مجموعة واسعة من أدوات التصميم.

### س2: هل يمكنني استخدام Aspose.3D لتطوير اللعبة؟

ج2: على الرغم من أن Aspose.3D مصمم بشكل أساسي للرسومات والمرئيات، إلا أن وظائفه يمكن أن تكمل جوانب معينة من تطوير اللعبة.

### س3: أين يمكنني العثور على أمثلة ووثائق إضافية؟

 ج3: استكشاف الشامل[وثائق Aspose.3D](https://reference.aspose.com/3d/net/) لمزيد من الأمثلة والمعلومات التفصيلية.

### س4: هل هناك نسخة تجريبية مجانية متاحة؟

 ج4: نعم، يمكنك الوصول إلى النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).

### س5: كيف يمكنني طلب المساعدة أو المشاركة في المجتمع؟

 ج5: انضم إلى مجتمع Aspose.3D على[منتدى الدعم](https://forum.aspose.com/c/3d/18) للمساعدة والتعاون.