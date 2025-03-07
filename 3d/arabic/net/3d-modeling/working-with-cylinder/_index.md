---
title: تخصيص اسطوانة القص السفلية
linktitle: تخصيص اسطوانة القص السفلية
second_title: Aspose.3D.NET API
description: تعلم كيفية إنشاء أسطوانات سفلية مخصصة للقص باستخدام Aspose.3D لـ .NET من خلال دليلنا التفصيلي خطوة بخطوة. ارفع مهاراتك في النمذجة ثلاثية الأبعاد اليوم!
weight: 12
url: /ar/net/3d-modeling/working-with-cylinder/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تخصيص اسطوانة القص السفلية

## مقدمة
مرحبًا بك في دليلنا الشامل حول إنشاء أسطوانة مخصصة باستخدام Aspose.3D لـ .NET. إذا كنت تتطلع إلى تحسين مهاراتك في تصميم النماذج ثلاثية الأبعاد وإضافة ميزات فريدة لمشاريعك، فأنت في المكان الصحيح. في هذا البرنامج التعليمي، سنرشدك خلال العملية خطوة بخطوة، باستخدام شرح واضح ومقتطفات التعليمات البرمجية.
## المتطلبات الأساسية
قبل أن نتعمق في البرنامج التعليمي، تأكد من أن لديك ما يلي:
- الفهم الأساسي لبرمجة C# و.NET.
-  تم تثبيت Aspose.3D لمكتبة .NET. يمكنك تنزيله[هنا](https://releases.aspose.com/3d/net/).
- بيئة تطوير تم إعدادها لبرمجة .NET.
## استيراد مساحات الأسماء
في كود C# الخاص بك، ابدأ باستيراد مساحات الأسماء الضرورية:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## الخطوة 1: إنشاء مشهد
ابدأ بإنشاء مشهد ثلاثي الأبعاد باستخدام Aspose.3D:
```csharp
Scene scene = new Scene();
```
## الخطوة 2: إنشاء الاسطوانة 1
إنشاء الاسطوانة الأولى وضبط خصائصها:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## الخطوة 3: تخصيص قاع القص للأسطوانة 1
قم بتطبيق قاع القص المخصص على الاسطوانة الأولى:
```csharp
//القص 47.5 درجة في المستوى xy (المحور z)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// اضبط GenerateFanCylinder على القيمة true
cylinder1.GenerateFanCylinder = true;
// اضبط طول ثيتا
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// تعيين أوفستتوب
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## الخطوة 4: أضف الاسطوانة 1 إلى المشهد
أضف الاسطوانة الأولى إلى المشهد واضبط ترجمتها:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## الخطوة 5: إنشاء الاسطوانة 2
قم بإنشاء أسطوانة ثانية ذات خصائص مماثلة:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## الخطوة 6: إضافة الاسطوانة 2 إلى المشهد
أضف الأسطوانة الثانية إلى المشهد بدون معلمات مخصصة:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## الخطوة 7: احفظ المشهد
احفظ المشهد كملف Wavefront OBJ في دليل المستند الخاص بك:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## خاتمة
تهانينا! لقد نجحت في إنشاء أسطوانة قص سفلية مخصصة باستخدام Aspose.3D لـ .NET. يهدف هذا البرنامج التعليمي إلى توفير دليل خطوة بخطوة للمستخدمين ذوي مستويات مختلفة من الخبرة في النمذجة والبرمجة ثلاثية الأبعاد.
## أسئلة مكررة
### هل Aspose.3D for .NET مناسب للمبتدئين؟
قطعاً! يقدم Aspose.3D for .NET واجهة سهلة الاستخدام، مما يجعله في متناول المطورين المبتدئين وذوي الخبرة.
### هل يمكنني تطبيق زوايا قص مختلفة على الأسطوانات؟
نعم، يمكنك تخصيص الجزء السفلي من القص لكل أسطوانة على حدة، مما يسمح لك بتحقيق تأثيرات فريدة.
### هل هناك نسخة تجريبية متاحة؟
 نعم، يمكنك استكشاف النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).
### أين يمكنني العثور على دعم إضافي؟
 قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع والمناقشات.
### كيف يمكنني الحصول على ترخيص مؤقت؟
 احصل على ترخيصك المؤقت[هنا](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
