---
date: 2026-03-26
description: تعلم كيفية إنشاء أسطوانة وتصدير ملف OBJ باستخدام Aspose.3D لـ .NET. يغطي
  هذا الدليل المناسب للمبتدئين إعداد المشهد ثلاثي الأبعاد وتصدير OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: كيفية إنشاء أسطوانة بقاعدة مائلة – Aspose.3D لـ .NET
url: /ar/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية إنشاء أسطوانة مع قاعدة قص – Aspose.3D for .NET

## المقدمة
إذا كنت تتساءل **كيفية إنشاء أسطوانة** مع قاعدة قص مخصصة في بيئة .NET، فقد وصلت إلى المكان الصحيح. في هذا البرنامج التعليمي سنستعرض كل خطوة—من إعداد مشهد ثلاثي الأبعاد إلى تصدير النموذج النهائي كملف OBJ—حتى تتمكن من تعزيز مهاراتك في *نمذجة ثلاثية الأبعاد للمبتدئين* باستخدام **Aspose.3D for .NET**.

## إجابات سريعة
- **ما هو الصنف الأساسي لبدء نموذج ثلاثي الأبعاد؟** `Scene` ينشئ الحاوية الجذرية لجميع الهندسة.  
- **أي طريقة تصدر النموذج إلى OBJ؟** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **هل أحتاج إلى ترخيص للاختبار؟** تتوفر نسخة تجريبية مجانية — انظر رابط التجربة في الأسئلة المتكررة.  
- **هل يمكنني تغيير زاوية القص؟** نعم، عدل `ShearBottom` باستخدام قيمة `Vector2`.  
- **هل هذا مناسب للمبتدئين؟** بالتأكيد؛ الـ API يج abstracts التعامل منخفض المستوى مع الـ mesh.

## ما هو المشهد ثلاثي الأبعاد؟
*المشهد ثلاثي الأبعاد* هو حاوية هرمية تحتوي على جميع الكيانات الهندسية، الأضواء، الكاميرات، والتحويلات. في Aspose.3D يوفر الصنف `Scene` طريقة منظمة لتجميع نماذجك وتصديرها لاحقًا.

## لماذا تصدير OBJ؟
OBJ هو تنسيق نصي مدعوم على نطاق واسع يمكن للعديد من تطبيقات 3‑D (Blender, Maya, Unity) استيراده. تصدير إلى OBJ يتيح لك مشاركة أو تعديل نماذج الأسطوانة خارج .NET.

## المتطلبات المسبقة
قبل أن نبدأ، تأكد من أن لديك:

- معرفة أساسية بـ C# وتطوير .NET.  
- **Aspose.3D for .NET** مثبت – يمكنك تنزيله **[هنا](https://releases.aspose.com/3d/net/)**.  
- بيئة تطوير .NET (Visual Studio, Rider, أو VS Code) جاهزة للبرمجة.

## استيراد المساحات الاسمية
أولاً، استورد المساحات الاسمية المطلوبة حتى يتم التعرف على أنواع الـ API.

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

## الخطوة 1: إنشاء مشهد ثلاثي الأبعاد
كائن `Scene` يعمل كجذر هرمية نموذجك.

```csharp
Scene scene = new Scene();
```

## الخطوة 2: إنشاء أسطوانة 1
نولد الأسطوانة الأولى بنصف قطر 2، ارتفاع 10، و20 قطاعًا شعاعيًا.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## الخطوة 3: تخصيص قاعدة القص للأسطوانة 1
طبق تحويل القص، فعّل توليد أسطوانة‑مروحة، وعدّل الخصائص الأخرى لتحقيق الشكل المطلوب.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## الخطوة 4: إضافة الأسطوانة 1 إلى المشهد
ضع الأسطوانة الأولى في موقع مناسب باستخدام تحويل إزاحة.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## الخطوة 5: إنشاء أسطوانة 2
يتم إنشاء أسطوانة ثانية بنفس أبعاد القاعدة ولكن بدون قص مخصص—مثالية للمقارنة جنبًا إلى جنب.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## الخطوة 6: إضافة الأسطوانة 2 إلى المشهد
نقوم ببساطة بربط الأسطوانة الثانية بشجرة المشهد.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## الخطوة 7: تصدير المشهد كملف OBJ
أخيرًا، نحفظ المشهد بالكامل كملف OBJ حتى يمكن فتحه في أي عارض ثلاثي الأبعاد قياسي.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## المشكلات الشائعة والحلول
| المشكلة | لماذا يحدث | الحل |
|-------|----------------|-----|
| **ملف OBJ فارغ** | المشهد لا يحتوي على أي هندسة مرفقة. | تأكد من إضافة كلتا الأسطوانتين إلى `scene.RootNode`. |
| **القص يبدو غير صحيح** | `ShearBottom` يتوقع المماس للزاوية. | استخدم `Math.Tan(angleInRadians)` أو القيمة `0.83` المقدمة لزاوية تقريبًا 47.5°. |
| **أخطاء مسار الملف** | دليل غير صالح أو مفقود. | استخدم `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## الأسئلة المتكررة
### هل Aspose.3D for .NET مناسب للمبتدئين؟
بالتأكيد! Aspose.3D for .NET يقدم API عالي المستوى يج abstracts الأجزاء الرياضية الثقيلة من نمذجة 3‑D، مما يجعله مناسبًا للمطورين من جميع المستويات.

### هل يمكنني تطبيق زوايا قص مختلفة على الأسطوانات؟
نعم، كل كائن `Cylinder` لديه خاصية `ShearBottom` الخاصة به، لذا يمكنك تعيين زاوية فريدة لكل كائن.

### هل تتوفر نسخة تجريبية؟
نعم، يمكنك استكشاف النسخة التجريبية المجانية **[هنا](https://releases.aspose.com/)**.

### أين يمكنني العثور على دعم إضافي؟
زر **[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18)** للحصول على مساعدة المجتمع، عينات الكود، والنقاش.

### كيف يمكنني الحصول على ترخيص مؤقت؟
احصل على ترخيصك المؤقت **[هنا](https://purchase.aspose.com/temporary-license/)**.

**أسئلة وإجابات إضافية**

**س: كيف يمكنني تصدير النموذج بصيغة مختلفة، مثل STL؟**  
ج: استبدل `FileFormat.WavefrontOBJ` بـ `FileFormat.STL` في استدعاء `scene.Save`.

**س: هل يمكنني تحريك الأسطوانات بعد إنشائها؟**  
ج: نعم، يمكنك إضافة رسومات متحركة بإطارات مفتاحية إلى تحويلات العقد باستخدام فئات `Animation` التي توفرها Aspose.3D.

**س: هل يدعم الـ API .NET Core؟**  
ج: المكتبة متوافقة بالكامل مع .NET Core، .NET 5+، و .NET 6+.

---

**آخر تحديث:** 2026-03-26  
**تم الاختبار مع:** Aspose.3D for .NET (latest release)  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}