---
title: حفظ الشبكات ثلاثية الأبعاد بتنسيق ثنائي مخصص
linktitle: حفظ الشبكات ثلاثية الأبعاد بتنسيق ثنائي مخصص
second_title: Aspose.3D.NET API
description: استكشف عالم الأبعاد الثلاثية باستخدام Aspose.3D لـ .NET. تعلم كيفية حفظ الشبكات بتنسيق ثنائي مخصص.
type: docs
weight: 13
url: /ar/net/3d-scene/save-3d-meshes-binary-format/
---
## مقدمة

مرحبًا بك في عالم Aspose.3D for .NET، وهي مكتبة قوية تمكّن المطورين من العمل مع الملفات ثلاثية الأبعاد دون عناء. في هذا البرنامج التعليمي، سنتعمق في عملية حفظ الشبكات ثلاثية الأبعاد بتنسيق ثنائي مخصص باستخدام Aspose.3D لـ .NET. يفترض هذا الدليل أن لديك فهمًا أساسيًا لـ C# وأنك على دراية بمكتبة Aspose.3D.

## المتطلبات الأساسية

قبل أن ننتقل إلى البرنامج التعليمي، تأكد من أن لديك ما يلي:

-  Aspose.3D لـ .NET: تأكد من تثبيت مكتبة Aspose.3D. يمكنك تنزيله من[هنا](https://releases.aspose.com/3d/net/).

- بيئة التطوير: قم بإعداد بيئة تطوير C# المفضلة لديك، مثل Visual Studio.

- ملف الإدخال ثلاثي الأبعاد: لديك ملف ثلاثي الأبعاد (على سبيل المثال، test.fbx) تريد تحويله إلى تنسيق ثنائي مخصص.

## استيراد مساحات الأسماء

في كود C# الخاص بك، قم بتضمين مساحات الأسماء الضرورية للوصول إلى وظائف Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## الخطوة 1: قم بتحميل ملف ثلاثي الأبعاد

قم بتحميل ملفك ثلاثي الأبعاد باستخدام Aspose.3D. في هذا المثال، نقوم بتحميل ملف باسم "test.fbx":

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## الخطوة 2: تحديد التنسيق الثنائي المخصص

حدد بنية التنسيق الثنائي المخصص الذي تريد حفظ شبكاتك ثلاثية الأبعاد فيه. يستخدم المثال بنية تحتوي على MeshBlock وVertex وTriangle كمكونات.

```csharp
// تخطيط الذاكرة للقمة هو
// موقف تعويم[3]؛
// تعويم[3] عادي؛
// تعويم [3] الأشعة فوق البنفسجية؛
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## الخطوة 3: افتح الملف للكتابة

افتح ملفًا ثنائيًا للكتابة، حيث سيتم حفظ الشبكات ثلاثية الأبعاد المحولة:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## الخطوة 4: التكرار عبر العقد والكيانات

قم بزيارة كل عقدة في المشهد ثلاثي الأبعاد وقم بتحويل كيانات الشبكة إلى التنسيق الثنائي المخصص. تجاهل الأضواء والكاميرات والكيانات الأخرى غير الشبكية:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (متابعة المعالجة)
    }
    return true;
});
```

## الخطوة 5: تحويل وكتابة نقاط التحكم والمثلثات

لكل كيان شبكي، قم بتحويل نقاط التحكم إلى مساحة عالمية واكتبها في الملف الثنائي مع فهارس المثلث:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//تخطيط ذاكرة الشبكة هو:
// تعويم[16] Transform_matrix؛
// int vertices_count;
// indices_count;
// قمة [vertices_count] القمم؛
// مؤشرات ushort[indices_count]؛


//تحويل الكتابة
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//اكتب عدد القمم/المؤشرات
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//كتابة القمم والمؤشرات
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## خاتمة

في هذا البرنامج التعليمي، قمنا بتغطية عملية حفظ الشبكات ثلاثية الأبعاد بتنسيق ثنائي مخصص باستخدام Aspose.3D لـ .NET. توفر هذه المكتبة القوية للمطورين الأدوات اللازمة لمعالجة الملفات ثلاثية الأبعاد بسلاسة. قم بتجربة تنسيقات وإعدادات مختلفة لفتح الإمكانات الكاملة لـ Aspose.3D في مشاريعك.

## الأسئلة الشائعة

### س1: هل يمكنني استخدام Aspose.3D لـ .NET مع لغات البرمجة الأخرى؟

ج1: يدعم Aspose.3D بشكل أساسي لغات .NET، ولكن يمكنك استكشاف خيارات التوافق للغات الأخرى.

### س2: أين يمكنني العثور على أمثلة وموارد إضافية؟

 ج2: ال[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18)يعد مكانًا رائعًا للعثور على الدعم والأمثلة والتفاعل مع المجتمع.

### س3: هل هناك نسخة تجريبية متاحة لـ Aspose.3D؟

 ج3: نعم، يمكنك الحصول على نسخة تجريبية مجانية من[هنا](https://releases.aspose.com/).

### س4: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D؟

 ج4: زيارة[هذا الرابط](https://purchase.aspose.com/temporary-license/) للحصول على ترخيص مؤقت لأغراض الاختبار.

### س5: هل يمكنني شراء Aspose.3D لـ .NET؟

 ج5: نعم، يمكنك شراء Aspose.3D من[صفحة الشراء](https://purchase.aspose.com/buy).