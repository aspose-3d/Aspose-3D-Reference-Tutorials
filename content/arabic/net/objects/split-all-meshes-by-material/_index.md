---
title: تقسيم جميع شبكات المشهد حسب المادة
linktitle: تقسيم جميع شبكات المشهد حسب المادة
second_title: Aspose.3D.NET API
description: تعرف على كيفية تقسيم الشبكات ثلاثية الأبعاد حسب المادة باستخدام Aspose.3D لـ .NET. اتبع دليلنا خطوة بخطوة لتنظيم وإدارة النماذج ثلاثية الأبعاد بكفاءة.
type: docs
weight: 21
url: /ar/net/objects/split-all-meshes-by-material/
---
## مقدمة
مرحبًا بك في هذا الدليل التفصيلي خطوة بخطوة حول تقسيم جميع شبكات المشهد ثلاثي الأبعاد حسب المادة باستخدام Aspose.3D لـ .NET. إذا كنت تعمل باستخدام نماذج ثلاثية الأبعاد وترغب في تنظيم شبكاتك بكفاءة استنادًا إلى المواد، فهذا البرنامج التعليمي مناسب لك. Aspose.3D هي مكتبة .NET قوية توفر مجموعة من الميزات للعمل مع الملفات ثلاثية الأبعاد، مما يجعلها خيارًا ممتازًا للمطورين.
## المتطلبات الأساسية
قبل الغوص في البرنامج التعليمي، تأكد من أن لديك المتطلبات الأساسية التالية:
- الفهم الأساسي للغة البرمجة C#.
- تم تثبيت Visual Studio على جهازك.
-  Aspose.3D لمكتبة .NET. يمكنك تنزيله من[هنا](https://releases.aspose.com/3d/net/).
- ملف إدخال ثلاثي الأبعاد (على سبيل المثال، "test.fbx") تريد تقسيمه.
## استيراد مساحات الأسماء
ابدأ باستيراد مساحات الأسماء الضرورية في مشروع C# الخاص بك:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## الخطوة 1: قم بتحميل الملف ثلاثي الأبعاد
```csharp
// المسار إلى دليل المستندات.
string input = RunExamples.GetDataFilePath("test.fbx");
// قم بتحميل ملف ثلاثي الأبعاد
Scene scene = new Scene(input);
```
 في هذه الخطوة، نقوم بتحميل الملف ثلاثي الأبعاد باستخدام Aspose.3D`Scene` فصل.
## الخطوة 2: تقسيم كافة الشبكات
```csharp
// تقسيم كافة الشبكات
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 وهنا نستخدم`SplitMesh` الطريقة من`PolygonModifier`class لتقسيم جميع الشبكات بناءً على المادة.
## الخطوة 3: احفظ المشهد المقسم
```csharp
// احفظ الملف
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
احفظ المشهد المعدل في ملف جديد للاحتفاظ بالتغييرات.
## الخطوة 4: عرض رسالة النجاح
```csharp
// عرض رسالة النجاح
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
اطبع رسالة نجاح تشير إلى إتمام العملية بنجاح.
## خاتمة
تهانينا! لقد تعلمت بنجاح كيفية تقسيم كافة شبكات المشهد ثلاثي الأبعاد حسب المادة باستخدام Aspose.3D لـ .NET. يمكن أن يكون هذا أسلوبًا قيمًا لتنظيم وإدارة النماذج ثلاثية الأبعاد المعقدة.
## الأسئلة الشائعة
### 1. هل يمكنني استخدام Aspose.3D لـ .NET مع لغات البرمجة الأخرى؟
تم تصميم Aspose.3D بشكل أساسي لـ .NET، ولكنه يوفر إمكانية التشغيل التفاعلي مع اللغات الأخرى من خلال روابط لغة .NET.
### 2. هل هناك نسخة تجريبية متاحة؟
 نعم، يمكنك الوصول إلى النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).
### 3. أين يمكنني العثور على المزيد من الأمثلة والوثائق؟
 استكشف الوثائق الشاملة على[Aspose.3D التوثيق](https://reference.aspose.com/3d/net/).
### 4. كيف يمكنني الحصول على الدعم لـ Aspose.3D؟
 قم بزيارة[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع والمناقشات.
### 5. هل يمكنني الحصول على ترخيص مؤقت؟
 نعم، يمكنك الحصول على ترخيص مؤقت[هنا](https://purchase.aspose.com/temporary-license/).