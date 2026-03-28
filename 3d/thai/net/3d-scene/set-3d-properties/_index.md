---
date: 2026-03-28
description: เรียนรู้วิธีแสดงคุณสมบัติของวัสดุ, เปลี่ยนสีกระจาย, และแก้ไขแอตทริบิวต์ของวัสดุ
  3 มิติด้วย Aspose.3D สำหรับ .NET พร้อมตัวอย่างโค้ดแบบขั้นตอนต่อขั้นตอน.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: แสดงรายการคุณสมบัติของวัสดุในฉาก 3 มิติด้วย Aspose.3D
url: /th/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# รายการคุณสมบัติวัสดุในฉาก 3D ด้วย Aspose.3D

## บทนำ

หากคุณต้องการ **แสดงรายการคุณสมบัติวัสดุ** ของโมเดล 3D แล้วปรับแต่งอย่างเช่นสี diffuse, คุณมาถูกที่แล้ว Aspose.3D for .NET ให้ API ที่เป็นวัตถุ‑ออริเอนต์ที่สะอาดและทำให้คุณสามารถตรวจสอบ, ดึงข้อมูล, และแก้ไขแอตทริบิวต์ของวัสดุได้โดยไม่ต้องออกจากโค้ด C# ของคุณ ในบทแนะนำนี้เราจะเดินผ่านการโหลดฉาก, การนับคุณสมบัติวัสดุ, และการเปลี่ยนค่าต่าง ๆ เช่นส่วนประกอบ diffuse—เพื่อให้คุณสามารถให้โมเดลของคุณมีลักษณะที่ต้องการได้อย่างแม่นยำ

## คำตอบสั้น
- **เป้าหมายหลักคืออะไร?** แสดงรายการคุณสมบัติวัสดุและแก้ไข (เช่น diffuse color).  
- **ไลบรารีที่ต้องการคืออะไร?** Aspose.3D for .NET.  
- **ต้องการใบอนุญาตหรือไม่?** จำเป็นต้องมีใบอนุญาตชั่วคราวหรือเต็มสำหรับการใช้งานในผลิตภัณฑ์.  
- **รูปแบบไฟล์ที่รองรับ?** FBX, OBJ, STL, STL‑ASCII, 3MF, และอื่น ๆ.  
- **เวลาในการทำงานโดยทั่วไป?** ประมาณ 10‑15 นาทีสำหรับสคริปต์แสดงรายการคุณสมบัติพื้นฐาน.

## **list material properties** คืออะไร?
การแสดงรายการคุณสมบัติวัสดุหมายถึงการวนลูปผ่าน `PropertyCollection` ของวัสดุเพื่ออ่านชื่อคุณสมบัติแต่ละรายการและค่าปัจจุบันของมัน ซึ่งมีประโยชน์สำหรับการดีบัก, การตรวจสอบภาพ, หรือการสร้างคอนโทรล UI ที่ให้ผู้ใช้ปรับแต่งการตั้งค่าวัสดุในขณะทำงาน

## ทำไมต้องใช้ Aspose.3D เพื่อ **access material properties**?
- **ไม่มีตัวแปลงภายนอก** – ทำงานโดยตรงกับอ็อบเจ็กต์ .NET ดั้งเดิม.  
- **โมเดลคุณสมบัติที่หลากหลาย** – รองรับแอตทริบิวต์เฉพาะ FBX ที่กำหนดเองนอกเหนือจากค่า PBR มาตรฐาน.  
- **ข้ามแพลตฟอร์ม** – ทำงานบน .NET Framework, .NET Core, และ .NET 5/6+.  

## ข้อกำหนดเบื้องต้น

- Aspose.3D for .NET ที่ติดตั้งในโปรเจกต์ของคุณ ดาวน์โหลดได้จาก [here](https://releases.aspose.com/3d/net/).
- โฟลเดอร์บนดิสก์เพื่อเก็บไฟล์ต้นฉบับ 3‑D ของคุณ (เช่นไฟล์ FBX ที่มีเทกเจอร์ฝังอยู่).

เมื่อคุณจัดการพื้นฐานเรียบร้อยแล้ว, มาเริ่มดูโค้ดกัน

## นำเข้า Namespaces

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

## ขั้นตอนที่ 1: โหลดฉาก 3D

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## ขั้นตอนที่ 2: **Access material properties** ของโหนดแรก

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## ขั้นตอนที่ 3: **List material properties** – ดูทุกคู่ชื่อ/ค่า

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

## ขั้นตอนที่ 4: **How to change diffuse** – แก้ไขคุณสมบัติ Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## ขั้นตอนที่ 5: **Retrieve property by name** – รับอินสแตนซ์ที่มีประเภทชัดเจน

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## ขั้นตอนที่ 6: เดินทางผ่านคุณสมบัติของคุณสมบัติ (ขั้นสูง)

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

## วิธี **change 3d material color** นอกเหนือจาก diffuse
หากคุณต้องการปรับสี specular, ambient, หรือ emissive เพียงแทนที่ `"Diffuse"` ด้วย `"Specular"` หรือ `"Ambient"` ในการกำหนดค่า `props["..."]` ด้านบน โครงสร้าง `Vector3` หรือ `Vector4` ที่ใช้ก็เหมือนกัน

## วิธี **update material color in C#**
การเปลี่ยนลักษณะการแสดงผลของวัสดุสรุปได้โดยการอัปเดตคุณสมบัติที่เหมาะสมใน `PropertyCollection` ไม่ว่าคุณจะต้องการแก้ไข diffuse, specular หรือแอตทริบิวต์สีที่กำหนดเองใด ๆ รูปแบบก็เหมือนเดิม:

1. ดึงคุณสมบัติตามชื่อที่ตรงกัน (คำนึงถึงตัวพิมพ์ใหญ่‑เล็ก)  
2. กำหนดค่า `Vector3` (RGB) หรือ `Vector4` (RGBA) ใหม่  

เนื่องจาก API ทำงานโดยตรงกับอ็อบเจ็กต์ C# คุณสามารถ **update material color C#** โค้ดได้โดยไม่ต้องใช้ไฟล์หรือตัวแปลงกลาง ซึ่งทำให้เหมาะกับตัวแก้ไขแบบเรียลไทม์หรือกระบวนการประมวลผลแบบแบตช์

## ข้อผิดพลาดทั่วไป & เคล็ดลับ
- **ความไวต่อกรณีของชื่อคุณสมบัติ** – คีย์คุณสมบัติของ Aspose.3D แยกแยะตัวพิมพ์ใหญ่‑เล็ก; ใช้ชื่อที่ตรงกับที่แสดงในผลลัพธ์.  
- **คุณสมบัติที่หายไป** – วัสดุบางประเภทไม่ได้เปิดเผยทุกแอตทริบิวต์ PBR ตรวจสอบ `props.ContainsKey("Specular")` ก่อนเข้าถึง.  
- **การบันทึกการเปลี่ยนแปลง** – หลังจากแก้ไขคุณสมบัติแล้ว ให้เรียก `scene.Save("output.fbx");` เพื่อบันทึกการเปลี่ยนแปลง.

## สรุป

คุณได้เรียนรู้วิธี **list material properties**, **retrieve a property by name**, และ **change the diffuse color** (หรือแอตทริบิวต์วัสดุอื่น) ด้วย Aspose.3D for .NET แล้ว ทดลองใช้ประเภทคุณสมบัติต่าง ๆ เพื่อปรับแต่งลักษณะของสินทรัพย์ 3‑D ของคุณ และจำไว้ว่า คุณสามารถ **update material color C#** ได้ด้วยเพียงบรรทัดเดียวของโค้ด

## คำถามที่พบบ่อย

### Q1: ฉันสามารถใช้ Aspose.3D for .NET กับรูปแบบไฟล์ 3D อื่น ๆ ได้หรือไม่?
A1: ใช่, Aspose.3D รองรับรูปแบบไฟล์ 3D ต่าง ๆ รวมถึง FBX, STL, และอื่น ๆ อีกมาก

### Q2: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D for .NET ได้อย่างไร?
A2: เยี่ยมชม [here](https://purchase.aspose.com/temporary-license/) เพื่อรับใบอนุญาตชั่วคราว

### Q3: มีฟอรั่มชุมชนสำหรับผู้ใช้ Aspose.3D หรือไม่?
A3: ใช่, คุณสามารถค้นหาการสนับสนุนและการสนทนาที่ [Aspose.3D forum](https://forum.aspose.com/c/3d/18)

### Q4: ฉันจะหาเอกสารรายละเอียดสำหรับ Aspose.3D for .NET ได้จากที่ไหน?
A4: ดูที่ [documentation](https://reference.aspose.com/3d/net/) เพื่อรับคำแนะนำอย่างละเอียด

### Q5: ฉันสามารถลอง Aspose.3D for .NET ฟรีก่อนซื้อได้หรือไม่?
A5: แน่นอน! ดาวน์โหลด [free trial version](https://releases.aspose.com/) เพื่อสำรวจคุณสมบัติต่าง ๆ

## คำถามที่พบบ่อย

**Q: `Vector3(1, 0, 1)` แสดงอะไร?**  
A: มันตั้งค่าสี diffuse เป็นสีเมเจนตา (แดง = 1, เขียว = 0, น้ำเงิน = 1) ในพื้นที่สีเชิงเส้น

**Q: จำเป็นต้องเรียก `scene.Save` หลังจากเปลี่ยนคุณสมบัติหรือไม่?**  
A: ใช่, การบันทึกฉากจะเขียนการแก้ไขของคุณลงดิสก์; หากไม่ทำการบันทึก การเปลี่ยนแปลงจะอยู่ในหน่วยความจำเท่านั้น

**Q: ฉันสามารถแสดงรายการแอตทริบิวต์ FBX ที่กำหนดเองได้หรือไม่?**  
A: แน่นอน. `PropertyCollection` จะรวมแอตทริบิวต์ที่กำหนดเองใด ๆ ที่คุณสามารถเข้าถึงได้ผ่าน `GetProperty("customName")`

**Q: มีวิธีการอัปเดตหลายวัสดุพร้อมกันหรือไม่?**  
A: วนลูปผ่าน `scene.RootNode.ChildNodes` และทำขั้นตอนการแก้ไขคุณสมบัติซ้ำสำหรับแต่ละวัสดุ

**Q: Aspose.3D รองรับ .NET 6 หรือไม่?**  
A: ใช่, ไลบรารีนี้เข้ากันได้เต็มที่กับ .NET 6 และรุ่นต่อไป

---

**อัปเดตล่าสุด:** 2026-03-28  
**ทดสอบด้วย:** Aspose.3D 24.11 for .NET  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}