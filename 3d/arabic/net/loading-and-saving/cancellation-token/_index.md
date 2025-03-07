---
title: باستخدام CancelToken
linktitle: باستخدام CancelToken
second_title: Aspose.3D.NET API
description: استكشف العالم السلس للنمذجة ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. تعلم كيفية تحميل المستندات ثلاثية الأبعاد وحفظها بكفاءة باستخدام CancellationToken.
weight: 10
url: /ar/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# باستخدام CancelToken

## مقدمة

مرحبًا بك في دليلنا الشامل حول استخدام Aspose.3D لـ .NET لتحسين مشاريع النمذجة والعرض ثلاثية الأبعاد. Aspose.3D هي مكتبة قوية تمكّن مطوري .NET من العمل بسلاسة مع الملفات ثلاثية الأبعاد. في هذا البرنامج التعليمي، سنتعمق في جوانب التحميل والحفظ، مع التركيز بشكل خاص على استخدام CancellationToken لإدارة المهام غير المتزامنة بكفاءة.

## المتطلبات الأساسية

قبل أن نبدأ هذه الرحلة، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D لـ .NET: قم بتنزيل المكتبة وتثبيتها من[هنا](https://releases.aspose.com/3d/net/).
- بيئة .NET: تأكد من إعداد بيئة تطوير .NET متوافقة.
- الفهم الأساسي لـ C#: يوصى بالإلمام بلغة البرمجة C#.

## استيراد مساحات الأسماء

للبدء، تأكد من تضمين مساحات الأسماء الضرورية في مشروعك. ستوفر مساحات الأسماء هذه إمكانية الوصول إلى الوظائف اللازمة لمعالجة الملفات ثلاثية الأبعاد.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## التحميل والحفظ - استخدام CancelToken

### الخطوة 1: إنشاء CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

هنا، نقوم بإنشاء مثيل CancellationTokenSource، وهو مكون حاسم لإدارة الإلغاء في العمليات غير المتزامنة.

### الخطوة 2: تهيئة المشهد ثلاثي الأبعاد

```csharp
Scene scene = new Scene();
```

إنشاء مثيل لفئة المشهد. ستكون هذه هي اللوحة القماشية لأنشطة النمذجة ثلاثية الأبعاد الخاصة بك.

### الخطوة 3: تعيين مهلة CancelToken

```csharp
cts.CancelAfter(1000);
```

 اضبط مهلة الإلغاء باستخدام`CancelAfter` طريقة. في هذا المثال، يتم تعيين المهلة إلى 1000 مللي ثانية (ثانية واحدة).

### الخطوة 4: افتح المستند ثلاثي الأبعاد

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 حاول فتح المستند ثلاثي الأبعاد خلال الإطار الزمني المحدد. ال`cts.Token` تضمن المعلمة إمكانية إلغاء العملية إذا تجاوزت المهلة المحددة.

### الخطوة 5: التعامل مع استثناء الاستيراد

في حالة وجود ImportException، تعامل معه بأمان عن طريق التحقق مما إذا كان سببه OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## خاتمة

تهانينا! لقد نجحت في التنقل عبر عملية استخدام Aspose.3D لـ .NET مع CancellationToken لإدارة تحميل المستندات ثلاثية الأبعاد. تضمن هذه التقنية عمليات استيراد فعالة وفي الوقت المناسب، مما يعزز الأداء العام لتطبيقاتك ثلاثية الأبعاد.

## الأسئلة الشائعة

### س1: هل Aspose.3D متوافق مع كافة تنسيقات الملفات ثلاثية الأبعاد؟

 A1: يدعم Aspose.3D نطاقًا واسعًا من تنسيقات الملفات ثلاثية الأبعاد، بما في ذلك FBX وSTL وOBJ والمزيد. الرجوع إلى[توثيق](https://reference.aspose.com/3d/net/) للحصول على القائمة الكاملة.

### س2: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D؟

 ج2: الحصول على ترخيص مؤقت عن طريق الزيارة[هذا الرابط](https://purchase.aspose.com/temporary-license/).

### س3: أين يمكنني العثور على الدعم لـ Aspose.3D؟

 ج3: انضم إلى مناقشة المجتمع في[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18).

### س4: هل يمكنني تجربة Aspose.3D مجانًا قبل الشراء؟

 ج4: نعم، استكشف الميزات من خلال النسخة التجريبية المجانية المتاحة[هنا](https://releases.aspose.com/).

### س5: ما هو أحدث إصدار من Aspose.3D لـ .NET؟

 ج5: ابق على اطلاع دائم عن طريق التحقق من[صفحة التحميل](https://releases.aspose.com/3d/net/) لأحدث إصدار.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
