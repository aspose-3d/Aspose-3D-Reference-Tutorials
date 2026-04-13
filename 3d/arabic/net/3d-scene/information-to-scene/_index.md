---
date: 2026-03-26
description: تعلم كيفية إضافة معلومات البائع إلى مشهد ثلاثي الأبعاد وكيفية حفظ ملفات
  FBX باستخدام Aspose.3D لـ .NET. اتبع هذا الدليل خطوة بخطوة مع كود جاهز للتنفيذ.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: كيفية إضافة معلومات البائع وحفظ مشهد FBX باستخدام Aspose.3D
url: /ar/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية إضافة معلومات البائع وحفظ مشهد FBX باستخدام Aspose.3D

## Introduction

مرحبًا بكم في هذا الدرس الشامل الذي يوضح **كيفية إضافة معلومات البائع** إلى مشهد ثلاثي الأبعاد ثم **كيفية حفظ ملفات FBX** باستخدام Aspose.3D لـ .NET. سواءً كنتم تبنون تصورات معمارية، أو أصول ألعاب، أو نماذج هندسية، فإن تضمين بيانات البائع وتطبيقات الميتاداتا يجعل المشاهد أكثر إيضاحًا وأسهل في الإدارة لاحقًا. دعونا نتبع العملية خطوةً بخطوة.

## Quick Answers
- **ماذا يعني “إضافة بائع”?** يقوم بتخزين أسماء التطبيق والبائع داخل كتلة AssetInfo الخاصة بالمشهد.  
- **أي تنسيق يدعم معلومات البائع؟** يحتفظ FBX (ASCII أو binary) بالميتاداتا عند الحفظ.  
- **كيف يتم حفظ FBX؟** استخدم `scene.Save(path, FileFormat.FBX7500ASCII)` أو ما يعادله من صيغة binary.  
- **هل أحتاج إلى ترخيص؟** الإصدار التجريبي المجاني يكفي للتطوير؛ يتطلب الترخيص التجاري للإنتاج.  
- **هل يمكنني تغيير وحدات القياس؟** نعم، قم بتعيين `AssetInfo.UnitName` و `AssetInfo.UnitScaleFactor`.

## What is “how to add vendor” in a 3D scene?

إضافة معلومات البائع تعني ملء خصائص `AssetInfo` لكائن `Scene`. هذه الخصائص تنتقل مع الملف، مما يسمح لأي مستهلك لملف FBX برؤية أي تطبيق أنشأه ومن هو البائع.

## Why add vendor information?
- **قابلية التتبع:** تحديد مصدر النموذج بسرعة في خطوط الإنتاج الكبيرة.  
- **الامتثال:** تتطلب بعض الصناعات وضع علامة بائع صريحة لإدارة الأصول.  
- **الأتمتة:** يمكن للسكربتات تصفية أو معالجة الملفات بناءً على ميتاداتا البائع.

## Prerequisites

- تم تثبيت Aspose.3D لـ .NET. يمكنك تنزيله من [صفحة Aspose.3D لـ .NET](https://releases.aspose.com/3d/net/).

## Import Namespaces

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## How to Add Vendor Information

### Step 1: Initialize a 3D Scene

```csharp
Scene scene = new Scene();
```

إنشاء `Scene` جديد يمنحك لوحة رسم نظيفة للعمل عليها.

### Step 2: Set Application and Vendor Information

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

هنا نوضح **كيفية إضافة بيانات البائع** عن طريق تعيين سلاسل نصية ذات معنى إلى `ApplicationName` و `ApplicationVendor`.

### Step 3: Define Measurement Units

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

تحديد نظام الوحدات يضمن أن أي شخص يفتح ملف FBX سيفهم الأبعاد بشكل صحيح. في هذا المثال، يساوي “pole” واحد 60 سم.

## How to Save FBX Scene

### Step 4: Save the Scene (how to save fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

هذا السطر يوضح **كيفية حفظ fbx** باستخدام نسخة ASCII من FBX 7.5.0. إذا كنت تفضل الصيغة الثنائية، استبدل `FBX7500ASCII` بـ `FBX7500Binary`.

> **نصيحة احترافية:** حافظ على امتداد الملف `.fbx` متوافقًا مع الصيغة التي تختارها؛ وإلا قد يفسر بعض العارضين المحتوى بشكل خاطئ.

### Step 5: Display Success Message

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

رسالة صديقة في وحدة التحكم تؤكد أن المشهد، مكتمل بميتاداتا البائع، قد تم كتابته إلى القرص.

## Common Issues and Solutions

| المشكلة | الحل |
|-------|----------|
| **معلومات البائع غير ظاهرة في العارض** | تأكد من حفظ الملف كـ **FBX ASCII** أو **Binary**؛ بعض العارضين القديمين يقرؤون صيغة واحدة فقط. |
| **المسار يحتوي على مسافات** | ضع المسار بين علامات اقتباس أو استخدم `Path.Combine` لإنشاء مسار ملف آمن. |
| **مقياس الوحدة يبدو خاطئًا** | تحقق مرة أخرى من `UnitScaleFactor`؛ فهو مضاعف بالنسبة إلى الأمتار. |
| **استثناء الترخيص** | استخدم النسخة التجريبية للاختبار؛ واحصل على ترخيص كامل لبناءات الإنتاج. |

## Frequently Asked Questions

**س: هل يمكنني استخدام Aspose.3D لـ .NET مع لغات برمجة أخرى؟**  
ج: يدعم Aspose.3D أساسًا لغات .NET، لكن يمكنك استكشاف خيارات التوافق مع لغات أخرى.

**س: هل هناك نسخة تجريبية مجانية متاحة لـ Aspose.3D لـ .NET؟**  
ج: نعم، يمكنك الوصول إلى النسخة التجريبية [هنا](https://releases.aspose.com/).

**س: كيف أحصل على دعم للاستفسارات المتعلقة بـ Aspose.3D؟**  
ج: زر [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للمجتمع والدعم.

**س: هل يمكنني شراء ترخيص مؤقت لـ Aspose.3D لـ .NET؟**  
ج: نعم، يمكنك الحصول على ترخيص مؤقت [هنا](https://purchase.aspose.com/temporary-license/).

**س: أين يمكنني العثور على وثائق مفصلة لـ Aspose.3D لـ .NET؟**  
ج: راجع [الوثائق](https://reference.aspose.com/3d/net/) للحصول على معلومات متعمقة.

---

**آخر تحديث:** 2026-03-26  
**تم الاختبار باستخدام:** Aspose.3D 24.11 لـ .NET  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}