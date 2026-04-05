---
date: 2026-03-26
description: تعرّف على كيفية إنشاء نماذج صندوق وأسطوانة ثلاثية الأبعاد وحفظ المشهد
  بصيغة FBX باستخدام Aspose.3D لـ .NET.
linktitle: Create 3D Box and Cylinder Models with Aspose.3D for .NET
second_title: Aspose.3D .NET API
title: إنشاء نماذج صندوق وأسطوانة ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET
url: /ar/net/3d-modeling/primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# إنشاء نماذج صندوق وأسطوانة ثلاثية الأبعاد باستخدام Aspose.3D

## المقدمة

مرحبًا بك في عالم النمذجة ثلاثية الأبعاد المثير مع Aspose.3D لـ .NET! في هذا البرنامج التعليمي ستتعلم **كيفية إنشاء صندوق ثلاثي الأبعاد**، إضافة أسطوانة، وتصدير المشهد بالكامل إلى FBX. سواءً كنت تبني نموذجًا أوليًا سريعًا أو خط أنابيب أصول جاهز للإنتاج، فإن هذه الخطوات تمنحك أساسًا صلبًا للعمل مع الهندسة ثلاثية الأبعاد في .NET.

## إجابات سريعة
- **ما الذي يغطيه هذا البرنامج التعليمي؟** إنشاء صندوق ثلاثي الأبعاد، أسطوانة ثلاثية الأبعاد، وحفظ المشهد كملف FBX.  
- **ما المكتبة المطلوبة؟** Aspose.3D لـ .NET (قم بتنزيلها من الموقع الرسمي).  
- **كم يستغرق التنفيذ؟** حوالي 10‑15 دقيقة لإنشاء مشهد أساسي.  
- **هل يمكن تخصيص الأبعاد؟** نعم – مُنشئا Box و Cylinder يقبلان معلمات الحجم.  
- **هل هناك حاجة إلى ترخيص للإنتاج؟** يلزم وجود ترخيص Aspose.3D صالح للبُنى غير التجريبية.

## ما هو “إنشاء صندوق ثلاثي الأبعاد”؟

إنشاء صندوق ثلاثي الأبعاد يعني توليد مكعب بسيط أو متوازي مستطيلات يمكن أن يكون وحدة بناء لنماذج أكثر تعقيدًا. في Aspose.3D، تمثل فئة `Box` هذا الشكل الأولي، ويمكنك إضافته إلى المشهد بسطر واحد من الشيفرة.

## لماذا نستخدم Aspose.3D لهذه المهمة؟

- **واجهة برمجة تطبيقات .NET صافية:** لا توجد تبعيات أصلية، مثالية لمشاريع C# و VB.NET.  
- **دعم واسع للتنسيقات:** تصدير إلى FBX، OBJ، STL، والعديد غيرها.  
- **أشكال أولية عالية المستوى:** Box، Cylinder، Sphere، إلخ، تتيح لك التركيز على المنطق بدلاً من بناء الشبكة منخفض المستوى.  
- **محسّن للأداء:** يتعامل بفعالية مع المشاهد الكبيرة.

## المتطلبات المسبقة

قبل أن نبدأ، تأكد من وجود ما يلي:

- Aspose.3D لـ .NET: قم بتنزيل وتثبيت المكتبة من [رابط التنزيل](https://releases.aspose.com/3d/net/).  
- بيئة تطوير .NET (Visual Studio، Rider، أو VS Code) متوافقة مع نسخة Aspose.3D التي قمت بتثبيتها.

الآن بعد أن لديك الأساسيات، لنبدأ بناء المشهد خطوة بخطوة.

## استيراد المساحات الاسمية

ابدأ باستيراد المساحات الاسمية الضرورية للوصول إلى الوظائف التي توفرها Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

مع هذه المساحات الاسمية في مكانها، أنت جاهز لإطلاق قوة Aspose.3D في تطبيق .NET الخاص بك.

## الخطوة 1: تهيئة كائن المشهد

```csharp
// Initialize a Scene object
Scene scene = new Scene();
```

كائن `Scene` يعمل كقماش حيث ستعيش جميع الكيانات ثلاثية الأبعاد.

## الخطوة 2: إنشاء نموذج صندوق

```csharp
// Create a Box model
scene.RootNode.CreateChildNode("box", new Box());
```

هذه السطر يضيف شكلًا أوليًا **صندوقًا ثلاثيًا الأبعاد** إلى جذر المشهد الخاص بك. يمكنك لاحقًا تعديل عرضه وارتفاعه وعمقه بتمرير المعلمات إلى مُنشئ `Box`.

## الخطوة 3: إنشاء نموذج أسطوانة

```csharp
// Create a Cylinder model
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

تُكمل الأسطوانة الصندوق وتظهر مدى سهولة دمج أشكال أولية مختلفة.

## الخطوة 4: حفظ الرسم بتنسيق FBX

```csharp
// Save drawing in the FBX format
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

هنا نقوم **بتحويل النموذج إلى FBX** عن طريق حفظ المشهد بالكامل كملف FBX. لا تتردد في تغيير المسار واسم الملف ليتناسب مع بنية مشروعك.

## الخطوة 5: عرض رسالة نجاح

```csharp
// Display success message
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

رسالة صديقة في وحدة التحكم تؤكد أن عملية **إنشاء مشهد ثلاثي الأبعاد** انتهت دون أخطاء.

## المشكلات الشائعة والنصائح

- **مجلد الإخراج غير موجود:** تأكد من وجود المجلد في `output` أو استخدم `Directory.CreateDirectory()` قبل الحفظ.  
- **الترخيص غير مُحدد:** في بنية غير تجريبية، استدعِ `License license = new License(); license.SetLicense("Aspose.3D.lic");` قبل إنشاء الـ `Scene`.  
- **الأبعاد المخصصة:** استخدم `new Box(width, height, depth)` أو `new Cylinder(radius, height)` للتحكم في الحجم.

## الخاتمة

تهانينا! لقد نجحت في **إنشاء صندوق وأسطوانة ثلاثية الأبعاد**، بناء مشهد بسيط، وحفظه كملف FBX باستخدام Aspose.3D لـ .NET. الآن الأساسيات في صندوق أدواتك، ويمكنك استكشاف [الوثائق](https://reference.aspose.com/3d/net/) للمزيد من الميزات المتقدمة مثل المواد، الإضاءة، والرسوم المتحركة.

## الأسئلة المتكررة

### س1: هل يمكنني استخدام Aspose.3D لـ .NET مع لغات برمجة أخرى؟
ج1: يدعم Aspose.3D أساسًا .NET، لكن هناك إصدارات أخرى متاحة لـ Java ومنصات أخرى.

### س2: هل هناك نسخة تجريبية مجانية؟
ج2: نعم، يمكنك استكشاف قدرات Aspose.3D عبر [نسخة تجريبية مجانية](https://releases.aspose.com/).

### س3: أين يمكنني العثور على دعم Aspose.3D لـ .NET؟
ج3: زر [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على دعم المجتمع والنقاشات.

### س4: كيف يمكنني الحصول على ترخيص مؤقت؟
ج4: يمكنك الحصول على ترخيص مؤقت [من هنا](https://purchase.aspose.com/temporary-license/).

### س5: هل هناك أي دروس نموذجية متاحة؟
ج5: نعم، استكشف المزيد من الدروس والأمثلة في [الوثائق](https://reference.aspose.com/3d/net/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**آخر تحديث:** 2026-03-26  
**تم الاختبار مع:** Aspose.3D 24.11 لـ .NET  
**المؤلف:** Aspose  

---