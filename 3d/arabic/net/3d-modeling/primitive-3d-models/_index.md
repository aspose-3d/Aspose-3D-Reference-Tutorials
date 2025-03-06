---
title: إنشاء نماذج بدائية ثلاثية الأبعاد
linktitle: إنشاء نماذج بدائية ثلاثية الأبعاد
second_title: Aspose.3D.NET API
description: استكشف عالم النمذجة ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. قم بإنشاء نماذج بدائية مذهلة دون عناء.
weight: 10
url: /ar/net/3d-modeling/primitive-3d-models/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إنشاء نماذج بدائية ثلاثية الأبعاد

## مقدمة

مرحبًا بك في عالم النمذجة ثلاثية الأبعاد المثير باستخدام Aspose.3D لـ .NET! في هذا البرنامج التعليمي الشامل، سوف نستكشف عملية إنشاء نماذج ثلاثية الأبعاد بدائية باستخدام Aspose.3D بطريقة خطوة بخطوة. سواء كنت مطورًا متمرسًا أو مبتدئًا فضوليًا، سيساعدك هذا الدليل على تسخير قوة Aspose.3D لصياغة عناصر ثلاثية الأبعاد مذهلة بصريًا لمشاريعك.

## المتطلبات الأساسية

قبل أن نتعمق في عالم النمذجة ثلاثية الأبعاد الرائع، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D for .NET: قم بتنزيل وتثبيت مكتبة Aspose.3D for .NET من[رابط التحميل](https://releases.aspose.com/3d/net/).

- بيئة التطوير: قم بإعداد بيئة تطوير .NET، مما يضمن التوافق مع Aspose.3D.

الآن بعد أن حصلت على الأساسيات، فلنبدأ رحلتنا لإنشاء نماذج ثلاثية الأبعاد بدائية خطوة بخطوة.

## استيراد مساحات الأسماء

ابدأ باستيراد مساحات الأسماء الضرورية للوصول إلى الوظائف التي يوفرها Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

مع وجود مساحات الأسماء هذه، أنت جاهز لإطلاق العنان لقوة Aspose.3D في تطبيق .NET الخاص بك.

## الخطوة 1: تهيئة كائن المشهد

```csharp
//تهيئة كائن المشهد
Scene scene = new Scene();
```

قم بإنشاء كائن مشهد جديد، والذي يعمل بمثابة لوحة فنية لتحفتك الفنية ثلاثية الأبعاد.

## الخطوة 2: إنشاء نموذج الصندوق

```csharp
// إنشاء نموذج مربع
scene.RootNode.CreateChildNode("box", new Box());
```

أضف نموذج صندوق إلى جذر المشهد الخاص بك. قم بتخصيص أبعاد وخصائص الصندوق حسب رؤيتك الإبداعية.

## الخطوة 3: إنشاء نموذج اسطوانة

```csharp
// إنشاء نموذج اسطوانة
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

قم بتحسين المشهد الخاص بك من خلال تقديم نموذج أسطواني. اضبط معلماته لتحقيق الشكل والحجم المطلوب.

## الخطوة 4: حفظ الرسم بتنسيق FBX

```csharp
// حفظ الرسم بتنسيق FBX
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

احفظ تحفة فنية ثلاثية الأبعاد بتنسيق FBX. اختر دليل إخراج واسم ملف مناسبين لإنشائك.

## الخطوة 5: عرض رسالة النجاح

```csharp
// عرض رسالة النجاح
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

احتفل بإنجازك! تم بناء المشهد بنجاح من نماذج بدائية ثلاثية الأبعاد، ويتم حفظ الملف.

## خاتمة

 تهانينا! لقد نجحت في إنشاء نماذج ثلاثية الأبعاد مذهلة باستخدام Aspose.3D لـ .NET. يغطي هذا الدليل الأساسيات، ولكن الاحتمالات لا حدود لها. اكتشف ال[توثيق](https://reference.aspose.com/3d/net/) لمزيد من الميزات والتقنيات المتقدمة.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ .NET مع لغات البرمجة الأخرى؟

ج1: يدعم Aspose.3D بشكل أساسي .NET، ولكن هناك إصدارات أخرى متاحة لـ Java والأنظمة الأساسية الأخرى.

### س2: هل هناك نسخة تجريبية مجانية متاحة؟

 ج2: نعم، يمكنك استكشاف إمكانيات Aspose.3D باستخدام ملف[تجربة مجانية](https://releases.aspose.com/).

### س3: أين يمكنني العثور على دعم لـ Aspose.3D لـ .NET؟

 ج3: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع والمناقشات.

### س4: كيف يمكنني الحصول على ترخيص مؤقت؟

 ج4: يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).

### س5: هل هناك أي نماذج تعليمية متاحة؟

 ج5: نعم، اكتشف المزيد من البرامج التعليمية والأمثلة في[توثيق](https://reference.aspose.com/3d/net/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
