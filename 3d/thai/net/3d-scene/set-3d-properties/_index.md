---
date: 2026-01-17
description: เรียนรู้วิธีการแสดงรายการคุณสมบัติของวัสดุ, เปลี่ยนสีกระจาย, และแก้ไขแอตทริบิวต์ของวัสดุ
  3 มิติโดยใช้ Aspose.3D สำหรับ .NET พร้อมตัวอย่างโค้ดทีละขั้นตอน
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: รายการคุณสมบัติวัสดุในฉาก 3 มิติด้วย Aspose.3D
url: /th/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# แสดงรายการคุณสมบัติของวัสดุในฉาก 3D ด้วย Aspose.3D

## Introduction

หากคุณต้องการ **แสดงรายการคุณสมบัติของวัสดุ** ของโมเดล 3D แล้วปรับเปลี่ยนอย่างเช่นสี diffuse คุณมาถูกที่แล้ว Aspose.3D for .NET ให้ API ที่เป็นวัตถุ‑ออริเอนต์ที่สะอาดตา ช่วยให้คุณตรวจสอบ ดึงข้อมูล และแก้ไขแอตทริบิวต์ของวัสดุโดยไม่ต้องออกจากโค้ด C# ของคุณ ในบทแนะนำนี้เราจะพาคุณผ่านการโหลดฉาก การวนลูปรายการคุณสมบัติของวัสดุ และการเปลี่ยนค่าต่าง ๆ เช่นส่วนประกอบ diffuse — เพื่อให้คุณสามารถให้โมเดลของคุณมีลักษณะที่ต้องการได้อย่างแม่นยำ

## Quick Answers
- **What is the primary goal?** แสดงรายการคุณสมบัติของวัสดุและแก้ไขมัน (เช่น สี diffuse)  
- **Which library is required?** Aspose.3D for .NET  
- **Do I need a license?** จำเป็นต้องมีใบอนุญาตชั่วคราวหรือเต็มสำหรับการใช้งานในผลิตภัณฑ์  
- **Supported file formats?** FBX, OBJ, STL, STL‑ASCII, 3MF, และอื่น ๆ  
- **Typical implementation time?** ประมาณ 10‑15 นาทีสำหรับสคริปต์พื้นฐานที่แสดงรายการคุณสมบัติ

## What is **list material properties**?
การแสดงรายการคุณสมบัติของวัสดุหมายถึงการวนลูปผ่าน `PropertyCollection` ของวัสดุเพื่ออ่านชื่อคุณสมบัติแต่ละรายการและค่าปัจจุบันของมัน ซึ่งเป็นประโยชน์สำหรับการดีบัก การตรวจสอบด้วยสายตา หรือการสร้าง UI ที่ให้ผู้ใช้ปรับตั้งค่าวัสดุในขณะรันไทม์

## Why use Aspose.3D to **access material properties**?
- **No external converters** – ทำงานโดยตรงกับอ็อบเจ็กต์ .NET แท้ ๆ  
- **Rich property model** – รองรับแอตทริบิวต์เฉพาะของ FBX นอกเหนือจากค่า PBR มาตรฐาน  
- **Cross‑platform** – ทำงานบน .NET Framework, .NET Core, และ .NET 5/6+  

## Prerequisites

- ติดตั้ง Aspose.3D for .NET ในโปรเจกต์ของคุณ ดาวน์โหลดได้จาก [here](https://releases.aspose.com/3d/net/)  
- โฟลเดอร์บนดิสก์เพื่อเก็บไฟล์แหล่งที่มาของ 3‑D (เช่นไฟล์ FBX ที่ฝังเทกซ์เจอร์)

เมื่อคุณจัดการพื้นฐานเรียบร้อยแล้ว มาดำดิ่งสู่โค้ดกันเถอะ

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

## How to **change 3d material color** beyond diffuse
หากคุณต้องการปรับสี specular, ambient หรือ emissive เพียงแทนที่ `"Diffuse"` ด้วย `"Specular"` หรือ `"Ambient"` ในการกำหนดค่า `props["..."]` ด้านบน โครงสร้าง `Vector3` หรือ `Vector4` จะใช้ได้เช่นเดียวกัน

## Common Pitfalls & Tips
- **Property name case‑sensitivity** – คีย์ของคุณสมบัติใน Aspose.3D แยกแยะตัวพิมพ์ใหญ่‑เล็ก; ใช้ชื่อที่แสดงในผลลัพธ์การแสดงรายการอย่างตรงกัน  
- **Missing property** – วัสดุบางประเภทอาจไม่เปิดเผยแอตทริบิวต์ PBR ทุกอย่าง ตรวจสอบ `props.ContainsKey("Specular")` ก่อนเข้าถึง  
- **Saving changes** – หลังจากแก้ไขคุณสมบัติแล้วเรียก `scene.Save("output.fbx");` เพื่อบันทึกการเปลี่ยนแปลง

## Conclusion

คุณได้เรียนรู้วิธี **แสดงรายการคุณสมบัติของวัสดุ**, **ดึงคุณสมบัติตามชื่อ**, และ **เปลี่ยนสี diffuse** (หรือแอตทริบิวต์วัสดุอื่น) ด้วย Aspose.3D for .NET แล้ว ทดลองใช้ประเภทคุณสมบัติต่าง ๆ เพื่อปรับแต่งลักษณะของทรัพยากร 3‑D ของคุณให้เหมาะสมที่สุด

## FAQ's

### Q1: Can I use Aspose.3D for .NET with other 3D file formats?

A1: ใช่, Aspose.3D รองรับรูปแบบไฟล์ 3D หลากหลาย รวมถึง FBX, STL, และอื่น ๆ อีกมากมาย

### Q2: How can I obtain a temporary license for Aspose.3D for .NET?

A2: เยี่ยมชม [here](https://purchase.aspose.com/temporary-license/) เพื่อรับใบอนุญาตชั่วคราว

### Q3: Is there a community forum for Aspose.3D users?

A3: มี, คุณสามารถหาการสนับสนุนและการสนทนาได้ที่ [Aspose.3D forum](https://forum.aspose.com/c/3d/18)

### Q4: Where can I find detailed documentation for Aspose.3D for .NET?

A4: ดูที่ [documentation](https://reference.aspose.com/3d/net/) สำหรับคำแนะนำอย่างละเอียด

### Q5: Can I try Aspose.3D for .NET for free before purchasing?

A5: แน่นอน! ดาวน์โหลด [free trial version](https://releases.aspose.com/) เพื่อสำรวจคุณสมบัติต่าง ๆ

## Frequently Asked Questions

**Q: What does the `Vector3(1, 0, 1)` represent?**  
A: มันตั้งค่าสี diffuse ให้เป็นสีแมจนตา (แดง = 1, เขียว = 0, น้ำเงิน = 1) ในพื้นที่สีเชิงเส้น

**Q: Do I need to call `scene.Save` after changing properties?**  
A: ใช่, การบันทึกฉากจะเขียนการแก้ไขของคุณลงดิสก์; หากไม่ทำการบันทึก การเปลี่ยนแปลงจะคงอยู่ในหน่วยความจำเท่านั้น

**Q: Can I enumerate custom FBX attributes?**  
A: แน่นอน, `PropertyCollection` จะรวมแอตทริบิวต์ที่กำหนดเองใด ๆ ที่คุณสามารถเข้าถึงผ่าน `GetProperty("customName")`

**Q: Is there a way to batch‑update multiple materials?**  
A: ใช้ลูปผ่าน `scene.RootNode.ChildNodes` แล้วทำซ้ำขั้นตอนการแก้ไขคุณสมบัติสำหรับแต่ละวัสดุ

**Q: Does Aspose.3D support .NET 6?**  
A: ใช่, ไลบรารีนี้เข้ากันได้เต็มที่กับ .NET 6 และรุ่นต่อ ๆ ไป

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}