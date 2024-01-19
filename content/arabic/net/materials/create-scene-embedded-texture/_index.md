---
title: إنشاء مشهد باستخدام مادة مضمنة
linktitle: إنشاء مشهد باستخدام مادة مضمنة
second_title: Aspose.3D.NET API
description: قم بإنشاء مشاهد ثلاثية الأبعاد رائعة باستخدام مواد مضمنة باستخدام Aspose.3D لـ .NET. اتبع دليلنا خطوة بخطوة للحصول على نتائج مذهلة.
type: docs
weight: 10
url: /ar/net/materials/create-scene-embedded-texture/
---
## مقدمة
مرحبًا بك في عالم الرسومات ثلاثية الأبعاد المثير باستخدام Aspose.3D لـ .NET! في هذا البرنامج التعليمي الشامل، سنرشدك خلال عملية إنشاء مشاهد ثلاثية الأبعاد مذهلة مع مواد مضمنة باستخدام Aspose.3D، وهي مكتبة قوية ومتعددة الاستخدامات لمطوري .NET.
## المتطلبات الأساسية
قبل الغوص في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:
- فهم أساسي لبرمجة C# و.NET.
- تم تثبيت Visual Studio على جهازك.
-  Aspose.3D لمكتبة .NET، والتي يمكنك تنزيلها[هنا](https://releases.aspose.com/3d/net/).
- الإلمام بمفاهيم الرسومات ثلاثية الأبعاد وإنشاء المشهد.
## استيراد مساحات الأسماء
ابدأ باستيراد مساحات الأسماء الضرورية إلى مشروعك. ستزودك مساحات الأسماء هذه بالأدوات والوظائف المطلوبة لمعالجة الرسومات ثلاثية الأبعاد.
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## الخطوة 1: إنشاء مشهد
ابدأ بإنشاء مشهد ثلاثي الأبعاد جديد باستخدام Aspose.3D لـ .NET. سيكون هذا بمثابة لوحة فنية لتحفتك ثلاثية الأبعاد.
```csharp
// قم بإنشاء ملف FBX باستخدام مواد مضمنة
Scene scene = new Scene();
```
## الخطوة 2: إنشاء نسيج مضمن
الآن، دعونا نضيف بعض الذوق البصري إلى المشهد الخاص بك عن طريق تضمين مادة. سنقوم بإنشاء نسيج بمحتوى مخصص وتخصيص اسم ملف له.
```csharp
// إنشاء نسيج مضمن
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    // اسم الملف مطلوب في حالة استخدام المادة المضمنة.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## الخطوة 3: إنشاء مادة
بعد ذلك، قم بإنشاء مادة للكائنات ثلاثية الأبعاد الخاصة بك، تتضمن النسيج الذي تم إنشاؤه مسبقًا والخصائص المخصصة.
```csharp
// قم بإنشاء مادة ذات خاصية مخصصة
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## الخطوة 4: إنشاء كائن ثلاثي الأبعاد
الآن، دعنا نجعل المشهد الخاص بك ينبض بالحياة عن طريق إضافة كائن ثلاثي الأبعاد. في هذا المثال، سنستخدم إطارًا دائريًا ونطبق المادة التي قمت بإنشائها للتو.
```csharp
// قم بإنشاء طارة باستخدام المادة التي تم إنشاؤها مسبقًا والتي تم تطبيقها
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## الخطوة 5: حفظ المشهد
أخيرًا، احفظ تحفتك الفنية في ملف. في هذا المثال، سنقوم بحفظه بتنسيق FBX.
```csharp
// احفظ المشهد في ملف
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
تهانينا! لقد نجحت في إنشاء مشهد ثلاثي الأبعاد بأنسجة مضمنة باستخدام Aspose.3D لـ .NET.
## كود مصدر CreateTextureContent
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## خاتمة
في هذا البرنامج التعليمي، اكتشفنا أساسيات إنشاء مشاهد ثلاثية الأبعاد مذهلة بصريًا باستخدام مواد مضمنة باستخدام Aspose.3D لـ .NET. ومن خلال تسلحك بهذه المعرفة، يمكنك إطلاق العنان لإبداعك وإنشاء تطبيقات ثلاثية الأبعاد جذابة.

## أسئلة مكررة

### س: هل يمكنني استخدام Aspose.3D لـ .NET مع لغات البرمجة الأخرى؟
ج: تم تصميم Aspose.3D بشكل أساسي لـ .NET، ولكن هناك مكتبات مماثلة متاحة للغات أخرى.
### س: كيف يمكنني تطبيق الرسوم المتحركة على المشاهد ثلاثية الأبعاد الخاصة بي؟
ج: يوفر Aspose.3D إمكانيات الرسوم المتحركة؛ الرجوع إلى الوثائق للحصول على تعليمات مفصلة.
### س: هل هناك إصدار تجريبي متاح لـ Aspose.3D لـ .NET؟
 ج: نعم، يمكنك تنزيل النسخة التجريبية[هنا](https://releases.aspose.com/).
### س: أين يمكنني العثور على دعم وموارد إضافية؟
 ج: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع والمناقشات.
### س: هل يمكنني استخدام Aspose.3D للمشاريع التجارية؟
 ج: نعم، يمكنك شراء ترخيص[هنا](https://purchase.aspose.com/buy).