---
title: تحويل المجال البدائي إلى شبكة
linktitle: تحويل المجال البدائي إلى شبكة
second_title: Aspose.3D.NET API
description: استكشف Aspose.3D لـ .NET وقم بتحويل Sphere Mesh إلى Triangle Mesh بسهولة باستخدام تخطيط ذاكرة مخصص. اتبع دليلنا خطوة بخطوة للتكامل السلس.
type: docs
weight: 16
url: /ar/net/objects/convert-sphere-primitive-to-mesh/
---
## مقدمة
هل تتطلع إلى تسخير قوة Aspose.3D لـ .NET لتحويل Sphere Mesh إلى Triangle Mesh مع تخطيط ذاكرة مخصص؟ سيرشدك هذا الدليل خطوة بخطوة خلال العملية، مما يسهل على المبتدئين متابعتها. بنهاية هذا البرنامج التعليمي، سيكون لديك فهم قوي لكيفية تحقيق ذلك باستخدام Aspose.3D لـ .NET.
## المتطلبات الأساسية
قبل الغوص في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:
- المعرفة الأساسية ببرمجة .NET.
- تم تثبيت Aspose.3D لمكتبة .NET. يمكنك تنزيله من[صفحة تنزيل Aspose.3D لـ .NET](https://releases.aspose.com/3d/net/).
- الإلمام بلغة البرمجة C#.
## استيراد مساحات الأسماء
في مشروع C# الخاص بك، تأكد من استيراد مساحات الأسماء اللازمة للاستفادة من وظيفة Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## الخطوة 1: تهيئة كائن المشهد
```csharp
// تهيئة كائن المشهد
Scene scene = new Scene();
```
## الخطوة 2: تهيئة كائن فئة العقدة
```csharp
// تهيئة كائن فئة العقدة
Node cubeNode = new Node("sphere");
```
## الخطوة 3: تحويل شبكة المجال إلى TriMesh المكتوبة
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## الخطوة 4: احصل على بيانات Vertex في بنية مخصصة
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## الخطوة 5: احصل على مؤشرات 32 بت و16 بت
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## الخطوة 6: كتابة بيانات Vertex وفهرسها إلى تدفق الذاكرة
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## الخطوة 7: نقطة العقدة إلى هندسة الشبكة
```csharp
cubeNode.Entity = sphere;
```
## الخطوة 8: إضافة عقدة إلى المشهد
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## الخطوة 9: حفظ المشهد ثلاثي الأبعاد
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## الخطوة 10: عرض النتائج
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## نموذج كود مصدر MyVertex
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## خاتمة
تهانينا! لقد نجحت في تحويل Sphere Mesh إلى Triangle Mesh مع تخطيط ذاكرة مخصص باستخدام Aspose.3D لـ .NET. توفر هذه المكتبة القوية طريقة سلسة للتعامل مع الكائنات ثلاثية الأبعاد في تطبيقات .NET الخاصة بك.
## الأسئلة الشائعة
### س: هل يمكنني استخدام Aspose.3D لـ .NET مع أطر عمل .NET الأخرى؟
ج: نعم، Aspose.3D for .NET متوافق مع أطر عمل .NET المختلفة.
### س: أين يمكنني العثور على الوثائق التفصيلية لـ Aspose.3D لـ .NET؟
 ج: راجع[Aspose.3D لتوثيق .NET](https://reference.aspose.com/3d/net/) للحصول على معلومات متعمقة.
### س: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D لـ .NET؟
 زيارة[هذا الرابط](https://purchase.aspose.com/temporary-license/) للحصول على ترخيص مؤقت.
### س: هل هناك أي نماذج مشاريع متاحة لـ Aspose.3D لـ .NET؟
 ج: استكشف Aspose.3D لوثائق .NET و[مستودع جيثب](https://github.com/aspose-3d/Aspose.3D-for-.NET) لمشاريع العينة.
### س: هل يوجد مجتمع نشط لـ Aspose.3D لدعم .NET؟
 ج: نعم، انضم إلى[Aspose.3D لمنتدى .NET](https://forum.aspose.com/c/3d/18) للحصول على المساعدة من المجتمع.