---
date: 2026-01-09
description: เรียนรู้วิธีสร้างฉาก 3 มิติและบันทึกโมเดล 3 มิติด้วย Aspose.3D สำหรับ
  .NET รวมถึงการส่งออกไฟล์ Wavefront OBJ และการตัดชั้นแบบดึงเชิงเส้น
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: สร้างฉาก 3 มิติด้วยชิ้นส่วนการดึงเชิงเส้น
url: /th/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# สร้างฉาก 3D ด้วย Linear Extrusion Slices

## แนะนำ

ยินดีต้อนรับสู่โลกของการออกแบบ 3D ด้วย Aspose.3D for .NET! ในบทเรียนนี้คุณจะ **สร้าง 3d scene** วัตถุ, ใช้ linear extrusion พร้อมจำนวน slice ที่กำหนดเอง, และสุดท้าย **บันทึก 3d model** เป็นไฟล์ Wavefront OBJ ไม่ว่าคุณจะสร้างต้นแบบอย่างรวดเร็วหรือการแสดงผลพร้อมใช้งานในผลิตภัณฑ์ ขั้นตอนต่อไปนี้จะแสดงให้คุณ **วิธีใช้ Aspose** เพื่อสร้างเรขาคณิตคุณภาพสูงโดยตรงจาก C#.

## คำตอบด่วน
- **What does “create 3d scene” mean?** หมายถึงการสร้างอ็อบเจ็กต์ Scene ที่เก็บเอาเอนทิตี 3D ทั้งหมด (meshes, lights, cameras).  
- **Which format is used for export?** ตัวอย่างส่งออกเป็น **Wavefront OBJ** (`export wavefront obj`).  
- **How many slices can I set?** คุณสามารถตั้งค่าเป็นจำนวนเต็มใดก็ได้; ตัวอย่างแสดง 2 และ 10 slices.  
- **Do I need a license?** จำเป็นต้องมีใบอนุญาตชั่วคราวหรือเต็มสำหรับการใช้งานในผลิตภัณฑ์.  
- **Can I run this on .NET Core?** ใช่, Aspose.3D รองรับ .NET Framework และ .NET Core.

## ข้อกำหนดเบื้องต้น

ก่อนจะดำดิ่งสู่โลกของการออกแบบ 3D ด้วย Aspose.3D, โปรดตรวจสอบว่าคุณมีข้อกำหนดต่อไปนี้:

- Aspose.3D for .NET Library: ตรวจสอบว่าคุณได้ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้จาก [here](https://releases.aspose.com/3d/net/).
- Integrated Development Environment (IDE): ใช้ IDE ที่คุณชื่นชอบซึ่งเข้ากันได้กับการพัฒนา .NET.
- Basic Understanding of C#: ทำความคุ้นเคยกับพื้นฐานของภาษาโปรแกรม C#.
- Desire to Explore 3D Design: ความหลงใหลในการสร้างโมเดล 3D ที่สวยงาม!

## นำเข้า Namespaces

เพื่อเริ่มต้นการเดินทางออกแบบ 3D ของคุณด้วย Aspose.3D, คุณจะต้องนำเข้า namespaces ที่จำเป็น ซึ่งจะทำให้โค้ดของคุณเข้าถึงคลาสและฟังก์ชันที่ต้องการได้

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## วิธีสร้าง 3d scene ด้วย Linear Extrusion

ด้านล่างนี้เราจะอธิบายขั้นตอนแต่ละขั้นตอนที่จำเป็นสำหรับการสร้างฉาก, ใช้ extrusion, และ **บันทึก 3d model** เป็นไฟล์ OBJ คำอธิบายถูกเขียนในสไตล์สนทนาเพื่อให้คุณตามได้ง่าย

### ขั้นตอนที่ 1: เริ่มต้น Base Profile

ก่อนอื่นเรากำหนดรูปทรง 2‑D ที่จะทำการ extrusion ในกรณีนี้คือสี่เหลี่ยมผืนผ้าที่มุมโค้ง

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### ขั้นตอนที่ 2: สร้าง 3D Scene

อ็อบเจ็กต์ `Scene` เป็นคอนเทนเนอร์สำหรับเรขาคณิตทั้งหมด, แสง, และกล้อง – เป็นหัวใจของ **creating a 3d scene**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### ขั้นตอนที่ 3: สร้าง Left และ Right Nodes

เราจะเพิ่มโหนดลูกสองโหนดลงในรากของฉาก โหนดหนึ่งจะใช้จำนวน slice ต่ำ อีกโหนดหนึ่งจะใช้จำนวนสูงกว่า เพื่อให้คุณเห็นความแตกต่างทางภาพ

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### ขั้นตอนที่ 4: ทำ Linear Extrusion บน Left Node

ที่นี่เราทำ extrusion สี่เหลี่ยมด้วย **2 slices** จำนวน slice ที่น้อยจะทำให้ได้ลักษณะหยาบ

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### ขั้นตอนที่ 5: ทำ Linear Extrusion บน Right Node

ตอนนี้เราทำ extrusion โปรไฟล์เดียวกันแต่ใช้ **10 slices** เพื่อให้ได้พื้นผิวที่เรียบเนียนขึ้น

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### ขั้นตอนที่ 6: บันทึก 3D Scene

สุดท้ายเราจะส่งออกฉากเป็นไฟล์ Wavefront OBJ ซึ่งจะแสดง **how to save obj** และ **export wavefront obj** ด้วย Aspose.3D

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|---------|
| ไฟล์ OBJ ปรากฏว่างเปล่า | เส้นทางออกไม่ถูกต้องหรือไม่มีสิทธิ์เขียน | ตรวจสอบว่าไดเรกทอรีมีอยู่และแอปพลิเคชันมีสิทธิ์เขียน |
| Slices ไม่ส่งผลต่อความเรียบเนียน | ค่าของ `Slices` ต่ำเกินไปสำหรับขนาดเรขาคณิต | เพิ่มจำนวน slice หรือปรับขนาดของ profile |
| ข้อยกเว้นใบอนุญาต | รันโดยไม่มีใบอนุญาตที่ถูกต้องในรุ่นที่ไม่ใช่ trial | ใช้ใบอนุญาตชั่วคราวหรือถาวรโดยใช้ `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## คำถามที่พบบ่อย

**Q: Can I use Aspose.3D for .NET with other programming languages?**  
A: Aspose.3D ถูกออกแบบมาสำหรับ .NET เป็นหลัก, แต่คุณสามารถสำรวจตัวเลือกการทำงานร่วมกับภาษาอื่นเช่น Python ผ่าน .NET bindings

**Q: Where can I find detailed documentation for Aspose.3D for .NET?**  
A: ดูเอกสารที่ [here](https://reference.aspose.com/3d/net/) เพื่อรับข้อมูลเชิงลึกเกี่ยวกับความสามารถและการใช้งานของ Aspose.3D

**Q: Is there a free trial available for Aspose.3D for .NET?**  
A: มี, คุณสามารถรับการทดลองใช้ฟรีได้จาก [here](https://releases.aspose.com/) เพื่อสำรวจคุณสมบัติของไลบรารีก่อนตัดสินใจซื้อ

**Q: How can I get technical support for Aspose.3D for .NET?**  
A: เยี่ยมชมฟอรั่ม Aspose.3D ที่ [here](https://forum.aspose.com/c/3d/18) เพื่อขอความช่วยเหลือและร่วมสนทนากับชุมชน

**Q: Can I use a temporary license for Aspose.3D for .NET?**  
A: ได้, คุณสามารถขอใบอนุญาตชั่วคราวได้จาก [here](https://purchase.aspose.com/temporary-license/) เพื่อการประเมินผล

## สรุป

ขอแสดงความยินดี! คุณได้เรียนรู้วิธี **สร้าง 3d scene**, ใช้ linear extrusion พร้อมจำนวน slice ที่กำหนดเอง, และ **บันทึก 3d model** เป็นไฟล์ Wavefront OBJ ด้วย Aspose.3D for .NET นี่เป็นเพียงจุดเริ่มต้นของการเดินทางออกแบบ 3D ของคุณ — อย่าลังเลที่จะทดลองกับโปรไฟล์ต่าง ๆ, ค่า slice, และรูปแบบการส่งออกเพื่อเปิดศักยภาพเต็มของ **3d modeling c#**.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**อัปเดตล่าสุด:** 2026-01-09  
**ทดสอบด้วย:** Aspose.3D 24.11 for .NET  
**ผู้เขียน:** Aspose