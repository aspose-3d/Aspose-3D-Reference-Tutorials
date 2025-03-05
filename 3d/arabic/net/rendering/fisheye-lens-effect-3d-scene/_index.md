---
title: تطبيق تأثير عدسة عين السمكة باستخدام Aspose.3D لـ .NET
linktitle: تطبيق تأثير عدسة عين السمكة على المشهد ثلاثي الأبعاد
second_title: Aspose.3D.NET API
description: عزز مشاهدك ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET! تعلم كيفية تطبيق تأثير عدسة عين السمكة الجذاب خطوة بخطوة. التحميل الان!
type: docs
weight: 12
url: /ar/net/rendering/fisheye-lens-effect-3d-scene/
---
## مقدمة
هل تتطلع إلى تحسين المظهر البصري لمشاهدك ثلاثية الأبعاد؟ انغمس في عالم تأثيرات عدسة عين السمكة الرائع باستخدام Aspose.3D لـ .NET. سيرشدك هذا البرنامج التعليمي خطوة بخطوة حول كيفية تطبيق تأثير عدسة عين السمكة على المشاهد ثلاثية الأبعاد، مما يمنحها منظورًا فريدًا وجذابًا.
## المتطلبات الأساسية
قبل أن نبدأ، تأكد من توفر المتطلبات الأساسية التالية:
-  Aspose.3D لـ .NET: تأكد من تثبيت مكتبة Aspose.3D لـ .NET. إذا لم يكن الأمر كذلك، يمكنك تنزيله[هنا](https://releases.aspose.com/3d/net/).
-  نموذج مشهد ثلاثي الأبعاد: سنعمل مع نموذج ملف مشهد ثلاثي الأبعاد (VirtualCity.glb). يمكنك استخدام المشهد الخاص بك أو تنزيل العينة من[وثائق Aspose.3D](https://reference.aspose.com/3d/net/).
## استيراد مساحات الأسماء
في مشروع .NET الخاص بك، قم بتضمين مساحات الأسماء الضرورية للوصول إلى وظائف Aspose.3D. أضف مساحات الأسماء التالية في بداية التعليمات البرمجية الخاصة بك:
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
## الخطوة 1: قم بتحميل المشهد ثلاثي الأبعاد
قم بتحميل ملف المشهد ثلاثي الأبعاد في مشروعك باستخدام الكود التالي:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## الخطوة 2: إعداد الكاميرا والأضواء
قم بإنشاء كاميرا وأضواء لتعزيز الجوانب المرئية للمشهد الخاص بك. اضبط المعلمات مثل NearPlane وFarPlane وRotationMode حسب الحاجة:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## الخطوة 3: إنشاء العارض وأهداف العرض
قم بإعداد العارض وإنشاء أهداف عرض لخريطة المكعب والملمس ثنائي الأبعاد:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## الخطوة 4: تطبيق تأثير عدسة عين السمكة
قم بتنفيذ تأثير عدسة عين السمكة بعد المعالجة على خريطة المكعب المعروضة:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## خاتمة
تهانينا! لقد نجحت في تطبيق تأثير عدسة عين السمكة على مشهدك ثلاثي الأبعاد باستخدام Aspose.3D لـ .NET. قم بتجربة مشاهد ومعايير مختلفة لإطلاق العنان لإبداعك.
## أسئلة مكررة
### هل يمكنني تطبيق تأثير عين السمكة على أي مشهد ثلاثي الأبعاد؟
نعم، يمكنك تطبيق تأثير عين السمكة على أي مشهد ثلاثي الأبعاد. تأكد من تحميل المشهد وإضاءته بشكل صحيح للحصول على أفضل النتائج.
### ما أهمية ضبط مجال الرؤية (fov) على 360 درجة؟
يضمن مجال الرؤية الذي يبلغ 360 درجة إسقاطًا كرويًا كاملاً، مما يخلق تأثيرًا مذهلاً لعين السمكة.
### كيف يمكنني تخصيص الإضاءة في المشهد ثلاثي الأبعاد الخاص بي؟
يمكنك ضبط خصائص الأضواء، مثل الموضع والنوع واللون، لتحقيق تأثيرات الإضاءة المطلوبة.
### هل هناك حد لحجم المشهد ثلاثي الأبعاد الذي يمكن معالجته؟
يقتصر حجم المشهد ثلاثي الأبعاد بشكل أساسي على موارد النظام. تأكد من أن أجهزتك يمكنها التعامل مع حجم المشهد الخاص بك.
### هل يمكنني استخدام تنسيق إخراج مختلف بدلاً من PNG للحصول على نتيجة تأثير عين السمكة؟
نعم، يمكنك تعديل الكود لحفظ المخرجات بتنسيقات صور مختلفة بناءً على متطلباتك.