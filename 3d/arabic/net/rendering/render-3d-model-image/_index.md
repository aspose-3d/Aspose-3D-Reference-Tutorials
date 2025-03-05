---
title: عرض صورة نموذجية ثلاثية الأبعاد من الكاميرا
linktitle: عرض صورة نموذجية ثلاثية الأبعاد من الكاميرا
second_title: Aspose.3D.NET API
description: استكشف عالم العرض ثلاثي الأبعاد باستخدام Aspose.3D لـ .NET. تعرف على كيفية إنشاء تصورات جذابة بسهولة باستخدام دليلنا خطوة بخطوة.
type: docs
weight: 11
url: /ar/net/rendering/render-3d-model-image/
---
## مقدمة
يعد إنشاء تصورات ثلاثية الأبعاد مذهلة جانبًا مثيرًا لتطوير البرامج، ومع Aspose.3D for .NET، يمكنك إضفاء الحيوية على نماذجك ثلاثية الأبعاد. في هذا البرنامج التعليمي، سنرشدك خلال عرض صورة نموذجية ثلاثية الأبعاد من الكاميرا باستخدام Aspose.3D، مع توفير إرشادات خطوة بخطوة ورؤى قيمة.
## المتطلبات الأساسية
قبل أن نتعمق في عملية العرض، تأكد من توفر المتطلبات الأساسية التالية:
-  Aspose.3D for .NET Library: قم بتنزيل المكتبة وتثبيتها من[رابط التحميل](https://releases.aspose.com/3d/net/).
- نموذج ثلاثي الأبعاد: قم بإعداد ملف نموذج ثلاثي الأبعاد (على سبيل المثال، Aspose3D.obj) الذي تريد عرضه.
- بيئة تطوير .NET: تأكد من أن لديك بيئة تطوير .NET جاهزة للعمل.
## استيراد مساحات الأسماء
في مشروع .NET الخاص بك، قم بتضمين مساحات الأسماء الضرورية لـ Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Drawing;
using System.Drawing.Imaging;
```
## الخطوة 1: قم بتحميل المشهد ثلاثي الأبعاد
```csharp
Scene scene = new Scene();
var path = RunExamples.GetDataFilePath("Aspose3D.obj");
scene.Open(path);
```
## الخطوة 2: إنشاء الكاميرا
```csharp
Camera cam = new Camera(ProjectionType.Perspective);
cam.NearPlane = 1;
cam.FarPlane = 500;
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(170, 16, 130);
cam.LookAt = new Vector3(28, 0, -30);
```
## الخطوة 3: إضافة الأضواء إلى المشهد
```csharp
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Point,
    ConstantAttenuation = 0.3,
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(30, 10, 10);
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Directional,
    ConstantAttenuation = 0.3,
    Direction = new Vector3(-0.3, -0.4, 0.3),
    Color = new Vector3(Color.White)
});
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Spot,
    CastShadows = true,
    LookAt = new Vector3(28, 10, -30),
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(40, 10, 50);
```
## الخطوة 4: تحديد خيارات عرض الصورة
```csharp
ImageRenderOptions opt = new ImageRenderOptions();
opt.BackgroundColor = Color.AliceBlue;
opt.AssetDirectories.Add("Your Document Directory" + "textures");
opt.EnableShadows = true;
```
## الخطوة 5: تقديم المشهد
```csharp
scene.Render(cam, "Your Output Directory" + "Render3DModelImageFromCamera.png", new Size(1024, 1024), ImageFormat.Png, opt);
```
## خاتمة
تهانينا! لقد نجحت في عرض صورة نموذج ثلاثي الأبعاد من الكاميرا باستخدام Aspose.3D لـ .NET. لا تتردد في تجربة نماذج مختلفة وزوايا الكاميرا وإعدادات الإضاءة لتحسين تصوراتك ثلاثية الأبعاد.
## الأسئلة الشائعة
### س: هل يمكنني استخدام Aspose.3D لـ .NET مع أدوات النمذجة ثلاثية الأبعاد الأخرى؟
ج: يدعم Aspose.3D العديد من تنسيقات النماذج ثلاثية الأبعاد، مما يجعله متوافقًا مع العديد من أدوات النمذجة الشائعة.
### س: كيف يمكنني استكشاف مشكلات العرض وإصلاحها؟
 ج: تحقق من Aspose.3D[المنتدى](https://forum.aspose.com/c/3d/18) للحصول على الدعم والحلول لمشاكل العرض الشائعة.
### س: هل هناك نسخة تجريبية مجانية متاحة؟
ج: نعم، يمكنك استكشاف ميزات Aspose.3D عن طريق الحصول على ملف[تجربة مجانية](https://releases.aspose.com/).
### س: أين يمكنني العثور على وثائق شاملة؟
 ج: راجع[توثيق](https://reference.aspose.com/3d/net/) للحصول على إرشادات متعمقة حول Aspose.3D لـ .NET.
### س: كيف يمكنني شراء Aspose.3D لـ .NET؟
 ج: قم بزيارة[صفحة الشراء](https://purchase.aspose.com/buy) للحصول على الترخيص الذي يناسب احتياجاتك.