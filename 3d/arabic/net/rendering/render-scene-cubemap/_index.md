---
title: تقديم المشهد في Cubemap مع ستة وجوه
linktitle: تقديم المشهد في Cubemap مع ستة وجوه
second_title: Aspose.3D.NET API
description: قم بإنشاء خرائط مكعبة مذهلة باستخدام Aspose.3D لـ .NET. اتبع دليلنا خطوة بخطوة لتحويل المشاهد ثلاثية الأبعاد إلى خرائط مكعبة جذابة ذات ستة وجوه.
type: docs
weight: 14
url: /ar/net/rendering/render-scene-cubemap/
---
## مقدمة
مرحبًا بك في هذا الدليل المفصّل خطوة بخطوة حول عرض مشهد في خريطة مكعبة بستة وجوه باستخدام Aspose.3D لـ .NET. في هذا البرنامج التعليمي، سنرشدك خلال عملية إنشاء خريطة مكعبة مذهلة من خلال عرض مشهد ثلاثي الأبعاد. Aspose.3D عبارة عن واجهة برمجة تطبيقات .NET قوية تعمل على تبسيط معالجة الرسومات ثلاثية الأبعاد، ومع هذا الدليل، ستستغل إمكاناتها لإنشاء خرائط مكعبة جذابة.
## المتطلبات الأساسية
قبل أن نتعمق في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:
- معرفة عملية بتطوير C# و.NET.
-  تم تثبيت Aspose.3D لـ .NET. يمكنك تنزيله[هنا](https://releases.aspose.com/3d/net/).
- ملف مشهد ثلاثي الأبعاد بتنسيق GLB (على سبيل المثال، "VirtualCity.glb") للعرض.
## استيراد مساحات الأسماء
ابدأ باستيراد مساحات الأسماء الضرورية لـ Aspose.3D في كود C# الخاص بك:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## الخطوة 1: تحميل المشهد
قم بتحميل ملف المشهد ثلاثي الأبعاد باستخدام الكود التالي:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## الخطوة 2: إنشاء الكاميرا والأضواء
قم بإنشاء كاميرا ومصباحين لإضاءة المشهد:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## الخطوة 3: إنشاء العارض وعرض الهدف
قم بإنشاء عارض وهدف عرض خريطة مكعبة بنسيج عميق:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## الخطوة 4: حفظ وجوه Cubemap
احفظ كل وجه من خريطة cubemap على القرص بأسماء الملفات المحددة:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## خاتمة
تهانينا! لقد نجحت في تحويل مشهد ثلاثي الأبعاد إلى خريطة مكعبة باستخدام Aspose.3D لـ .NET. استكشف المزيد من خيارات التخصيص وقم بتحسين مشاريع الرسومات ثلاثية الأبعاد الخاصة بك باستخدام واجهة برمجة التطبيقات القوية هذه.
## أسئلة مكررة
### س: هل يمكنني استخدام Aspose.3D لـ .NET مع تنسيقات ملفات ثلاثية الأبعاد أخرى؟
نعم، يدعم Aspose.3D العديد من تنسيقات الملفات ثلاثية الأبعاد، مما يوفر المرونة في مشروعاتك.
### س: كيف يمكنني الحصول على الدعم لـ Aspose.3D؟
 قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع والمناقشات.
### س: هل هناك نسخة تجريبية مجانية متاحة؟
 نعم، يمكنك الوصول إلى النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).
### س: هل يمكنني عرض المشاهد باستخدام الرسوم المتحركة باستخدام Aspose.3D؟
قطعاً! يدعم Aspose.3D عرض المشاهد المتحركة ثلاثية الأبعاد.
### س: أين يمكنني العثور على وثائق مفصلة؟
 الرجوع إلى[وثائق Aspose.3D](https://reference.aspose.com/3d/net/) للحصول على معلومات متعمقة.