---
title: تحويل العقدة بواسطة Quaternion
linktitle: تحويل العقدة بواسطة Quaternion
second_title: Aspose.3D.NET API
description: تعلم كيفية تحويل العقد ثلاثية الأبعاد باستخدام الكواترنيونات باستخدام Aspose.3D لـ .NET. دليل خطوة بخطوة للمبتدئين.
weight: 20
url: /ar/net/geometry-and-hierarchy/transformation-node-quaternion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تحويل العقدة بواسطة Quaternion

## مقدمة

مرحبًا بك في دليل خطوة بخطوة حول تحويل عقدة بواسطة quaternion في مشاهد ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. في هذا البرنامج التعليمي، سنستكشف الإمكانات القوية لـ Aspose.3D لـ .NET ونستعرض عملية إضافة التحويلات إلى عقدة ثلاثية الأبعاد باستخدام الكواترنيونات.

## المتطلبات الأساسية

قبل أن نتعمق في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D لـ .NET: تأكد من تثبيت مكتبة Aspose.3D. يمكنك تنزيله من[صفحة الإصدار](https://releases.aspose.com/3d/net/).

- بيئة التطوير: قم بإعداد بيئة تطوير .NET الخاصة بك باستخدام الأدوات والتكوينات اللازمة.

- الفهم الأساسي للمفاهيم ثلاثية الأبعاد: الإلمام بالرسومات والمفاهيم ثلاثية الأبعاد سيكون مفيدًا.

## استيراد مساحات الأسماء

في مشروع .NET الخاص بك، قم بتضمين مساحات الأسماء المطلوبة لـ Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## الخطوة 1: تهيئة كائن المشهد

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// تهيئة كائن المشهد
Scene scene = new Scene();
```

## الخطوة 2: تهيئة كائن فئة العقدة

```csharp
// تهيئة كائن فئة العقدة
Node cubeNode = new Node("cube");
```

## الخطوة 3: إنشاء شبكة باستخدام Polygon Builder

```csharp
// استدعاء الفئة المشتركة لإنشاء شبكة باستخدام طريقة إنشاء المضلع لتعيين مثيل الشبكة
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## الخطوة 4: أشر العقدة إلى هندسة الشبكة

```csharp
// نقطة العقدة إلى هندسة الشبكة
cubeNode.Entity = mesh;
```

## الخطوة 5: ضبط التدوير باستخدام Quaternion

```csharp
// ضبط التدوير
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## الخطوة 6: تعيين الترجمة

```csharp
// تعيين الترجمة
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## الخطوة 7: إضافة المكعب إلى المشهد

```csharp
// إضافة مكعب إلى مكان الحادث
scene.RootNode.ChildNodes.Add(cubeNode);
```

## الخطوة 8: حفظ المشهد ثلاثي الأبعاد

```csharp
// المسار إلى دليل المستندات.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// حفظ المشهد ثلاثي الأبعاد بتنسيقات الملفات المدعومة
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## خاتمة

 تهانينا! لقد تعلمت بنجاح كيفية تحويل عقدة بواسطة quaternion في مشاهد ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. اكتشف المزيد من الميزات والإمكانيات من خلال الرجوع إلى[توثيق](https://reference.aspose.com/3d/net/).

## الأسئلة الشائعة

### س1: ما هو الكواترنيون في الرسومات ثلاثية الأبعاد؟

A1: Quaternions هي كيانات رياضية تستخدم لتمثيل عمليات التدوير في الفضاء ثلاثي الأبعاد.

### س2: كيف يمكنني تنزيل Aspose.3D لـ .NET؟

 ج2: يمكنك تنزيل المكتبة من[صفحة الإصدار](https://releases.aspose.com/3d/net/).

### س3: هل تتوفر نسخة تجريبية مجانية من Aspose.3D لـ .NET؟

 ج3: نعم، يمكنك الحصول على نسخة تجريبية مجانية من[هنا](https://releases.aspose.com/).

### س 4: أين يمكنني العثور على دعم Aspose.3D لـ .NET؟

 ج4: قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للدعم والمناقشات.

### س5: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D؟

 ج5: الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
