---
date: 2026-01-17
description: تعلم كيفية سرد خصائص المادة، وتغيير اللون المنتشر، وتعديل خصائص المادة
  ثلاثية الأبعاد باستخدام Aspose.3D لـ .NET. تتضمن أمثلة شفرة خطوة بخطوة.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: قائمة خصائص المواد في المشاهد ثلاثية الأبعاد باستخدام Aspose.3D
url: /ar/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# قائمة خصائص المواد في المشاهد ثلاثية الأبعاد باستخدام Aspose.3D

## مقدمة

إذا كنت بحاجة إلى **قائمة خصائص المواد** لنموذج ثلاثي الأبعاد ثم تعديل أشياء مثل لون الانتشار، فأنت في المكان الصحيح. Aspose.3D for .NET يوفّر لك واجهة برمجة تطبيقات نظيفة كائنية التوجه تسمح لك بفحص، استرجاع، وتعديل سمات المادة دون مغادرة كود C# الخاص بك. في هذا الدرس سنستعرض تحميل مشهد، تعداد خصائص مادته، وتغيير قيم مثل المكوّن الانتشاري—حتى تتمكن من إعطاء نماذجك المظهر الدقيق الذي تريده.

## إجابات سريعة
- **ما هو الهدف الأساسي؟** قائمة خصائص المواد وتعديلها (مثل لون الانتشار).  
- **ما المكتبة المطلوبة؟** Aspose.3D for .NET.  
- **هل أحتاج إلى ترخيص؟** يلزم ترخيص مؤقت أو كامل للاستخدام في الإنتاج.  
- **ما صيغ الملفات المدعومة؟** FBX, OBJ, STL, STL‑ASCII, 3MF, وغيرها.  
- **ما هو الوقت التقريبي للتنفيذ؟** حوالي 10‑15 دقيقة لسكربت أساسي لقائمة الخصائص.

## ما هو **list material properties**؟
قائمة خصائص المواد تعني التكرار عبر `PropertyCollection` الخاصة بالمادة لقراءة كل اسم خاصية وقيمتها الحالية. هذا مفيد للتصحيح، الفحص البصري، أو بناء عناصر واجهة مستخدم تسمح للمستخدمين بتعديل إعدادات المادة أثناء التشغيل.

## لماذا تستخدم Aspose.3D لـ **access material properties**؟
- **No external converters** – العمل مباشرة مع كائنات .NET الأصلية.  
- **Rich property model** – يدعم سمات مخصصة خاصة بـ FBX بالإضافة إلى قيم PBR القياسية.  
- **Cross‑platform** – يعمل على .NET Framework, .NET Core, و .NET 5/6+.

## المتطلبات المسبقة

- تثبيت Aspose.3D for .NET في مشروعك. حمّله [هنا](https://releases.aspose.com/3d/net/).
- مجلد على القرص لتخزين ملفات المصدر ثلاثية الأبعاد (مثل ملف FBX يحتوي على القوام المدمجة).

## Import Namespaces

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Step 1: Load 3D Scene

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Step 2: **Access material properties** of the first node

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Step 3: **List material properties** – see every name/value pair

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Step 4: **How to change diffuse** – modify the Diffuse property

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Step 5: **Retrieve property by name** – get a strongly‑typed instance

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Step 6: Traverse a property's own properties (advanced)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## كيفية **change 3d material color** بما يتجاوز الانتشار
إذا كنت بحاجة إلى تعديل ألوان الانعكاس، الإضاءة المحيطة، أو الإشعاع، ما عليك سوى استبدال `"Diffuse"` بـ `"Specular"` أو `"Ambient"` في تعيين `props["..."]` أعلاه. نفس هياكل `Vector3` أو `Vector4` تُطبق.

## المشكلات الشائعة والنصائح
- **Property name case‑sensitivity** – مفاتيح خصائص Aspose.3D حساسة لحالة الأحرف؛ استخدم الاسم الدقيق كما هو معروض في ناتج القائمة.  
- **Missing property** – ليست كل المواد تُظهر كل سمة PBR. تحقق من `props.ContainsKey("Specular")` قبل الوصول.  
- **Saving changes** – بعد تعديل الخصائص، استدعِ `scene.Save("output.fbx");` لحفظ التغييرات.

## الخلاصة

لقد تعلمت الآن كيفية **list material properties**، **retrieve a property by name**، و**change the diffuse color** (أو أي سمة مادة أخرى) باستخدام Aspose.3D for .NET. جرّب أنواع خصائص مختلفة لضبط مظهر أصولك ثلاثية الأبعاد بدقة.

## الأسئلة المتكررة

### Q1: هل يمكنني استخدام Aspose.3D for .NET مع صيغ ملفات ثلاثية الأبعاد أخرى؟

A1: نعم، يدعم Aspose.3D صيغ ملفات ثلاثية الأبعاد مختلفة، بما في ذلك FBX, STL، والعديد غيرها.

### Q2: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D for .NET؟

A2: زر [هنا](https://purchase.aspose.com/temporary-license/) للحصول على ترخيص مؤقت.

### Q3: هل هناك منتدى مجتمع لمستخدمي Aspose.3D؟

A3: نعم، يمكنك العثور على الدعم والنقاشات في [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: أين يمكنني العثور على وثائق مفصلة لـ Aspose.3D for .NET؟

A4: راجع [الوثائق](https://reference.aspose.com/3d/net/) للحصول على إرشادات شاملة.

### Q5: هل يمكنني تجربة Aspose.3D for .NET مجانًا قبل الشراء؟

A5: بالتأكيد! حمّل [نسخة التجربة المجانية](https://releases.aspose.com/) لاستكشاف ميزاته.

## الأسئلة المتكررة

**س: ماذا يمثل `Vector3(1, 0, 1)`؟**  
ج: يحدد لون الانتشار إلى اللون الأرجواني (أحمر = 1، أخضر = 0، أزرق = 1) في مساحة اللون الخطية.

**س: هل يجب استدعاء `scene.Save` بعد تغيير الخصائص؟**  
ج: نعم، حفظ المشهد يكتب تعديلاتك إلى القرص؛ وإلا ستبقى التغييرات في الذاكرة فقط.

**س: هل يمكنني تعداد سمات FBX المخصصة؟**  
ج: بالتأكيد. سيتضمن `PropertyCollection` أي سمات مخصصة يمكنك الوصول إليها عبر `GetProperty("customName")`.

**س: هل هناك طريقة لتحديث عدة مواد دفعة واحدة؟**  
ج: كرّر خطوات تعديل الخصائص داخل حلقة تمر على `scene.RootNode.ChildNodes` لكل مادة.

**س: هل يدعم Aspose.3D .NET 6؟**  
ج: نعم، المكتبة متوافقة بالكامل مع .NET 6 وما بعده.

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}