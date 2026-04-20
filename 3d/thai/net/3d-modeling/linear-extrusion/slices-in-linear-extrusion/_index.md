---
date: 2026-03-23
description: เรียนรู้วิธีการทำการดึงเส้นตรงด้วยชั้นโดยใช้ Aspose.3D สำหรับ .NET สร้างโมเดล
  3 มิติที่ละเอียดด้วยตัวอย่างโค้ดทีละขั้นตอน.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: วิธีทำการดึงเชิงเส้นด้วยชั้นโดยใช้ Aspose.3D สำหรับ .NET
url: /th/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีทำ Linear Extrusion ด้วย Slices โดยใช้ Aspose.3D สำหรับ .NET

## บทนำ

ยินดีต้อนรับสู่โลกของการออกแบบ 3D ด้วย Aspose.3D สำหรับ .NET! ในบทเรียนนี้คุณจะได้ค้นพบ **วิธีทำ linear extrusion** ด้วย slices ซึ่งเป็นเทคนิคที่ช่วยให้คุณควบคุมระดับรายละเอียดในโมเดลของคุณ ไม่ว่าคุณจะเป็นนักพัฒนาที่มีประสบการณ์หรือเพิ่งเริ่มต้น เราจะพาคุณผ่านทุกขั้นตอน อธิบายเหตุผลเบื้องหลังแต่ละการกระทำ และให้เคล็ดลับที่สามารถนำไปใช้ได้ทันที.

## คำตอบอย่างรวดเร็ว
- **Linear extrusion with slices คืออะไร?** เป็นวิธีการขยายโปรไฟล์ 2D ไปเป็น 3D พร้อมระบุจำนวน cross‑sections (slices) ระหว่างกลางที่สร้างขึ้น.  
- **ทำไมต้องใช้ slices?** Slices มากกว่าจะให้ความโค้งที่เรียบขึ้น; Slices น้อยจะทำให้เมชมีน้ำหนักเบา.  
- **ข้อกำหนดเบื้องต้น?** Aspose.3D สำหรับ .NET, IDE ที่รองรับ .NET, และความรู้พื้นฐานของ C#.  
- **เวลาในการทำงานโดยทั่วไป?** ตัวอย่างทำงานภายในไม่ถึงหนึ่งวินาทีบน PC สมัยใหม่.  
- **รูปแบบผลลัพธ์?** ตัวอย่างบันทึกเป็น Wavefront OBJ แต่ Aspose.3D รองรับหลายรูปแบบ.

## Linear Extrusion with Slices คืออะไร?

Linear extrusion จะรับรูปทรง 2‑D (โปรไฟล์) แล้วยืดออกตามเส้นตรงเพื่อสร้างของแข็ง 3‑D คุณสมบัติ **Slices** กำหนดจำนวน cross‑sections ระหว่างจุดเริ่มต้นและสิ้นสุดของการ extrusion ซึ่งส่งผลต่อความเรียบและจำนวนโพลิกอน.

## ทำไมต้องใช้ Slices ใน Linear Extrusion?

- **ควบคุมความหนาแน่นของ Mesh:** ปรับสมดุลระหว่างคุณภาพภาพและขนาดไฟล์อย่างละเอียด.  
- **เพิ่มประสิทธิภาพ:** ใช้ Slices น้อยสำหรับแอปพลิเคชันแบบเรียลไทม์, มากสำหรับการเรนเดอร์ความละเอียดสูง.  
- **ความยืดหยุ่นเชิงสร้างสรรค์:** ผสมผสานจำนวน slices ที่ต่างกันบนวัตถุต่าง ๆ เพื่อเน้นเจตนาการออกแบบ.

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มทำงาน, ตรวจสอบว่าคุณมี:

- Aspose.3D for .NET Library – ดาวน์โหลดได้จาก [here](https://releases.aspose.com/3d/net/).  
- IDE ที่รองรับ C# (Visual Studio, Rider, VS Code, เป็นต้น).  
- ความคุ้นเคยพื้นฐานกับไวยากรณ์ C# และแนวคิดเชิงวัตถุ.  
- ความอยากทดลองกับเรขาคณิต 3‑D!

## นำเข้า Namespaces

ก่อนอื่น, นำเข้า namespaces ที่ให้คุณเข้าถึงคลาสหลักของ Aspose.3D

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## คู่มือขั้นตอนต่อขั้นตอน

### ขั้นตอนที่ 1: เริ่มต้น Base Profile

เราเริ่มด้วยรูปสี่เหลี่ยมธรรมดาและกำหนดรัศมีการโค้งเล็กน้อยเพื่อให้ขอบไม่คมเกินไป.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### ขั้นตอนที่ 2: สร้าง 3D Scene

`Scene` ทำหน้าที่เป็นคอนเทนเนอร์สำหรับโหนดทั้งหมด, mesh, แสง, และกล้อง.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### ขั้นตอนที่ 3: เพิ่ม Left และ Right Nodes

เราจะสร้างสองโหนดพี่น้องภายใต้ root ของ scene. โหนดซ้ายจะได้รับจำนวน slice ต่ำ, โหนดขวาจะได้รับจำนวน slice สูง, เพื่อให้คุณเปรียบเทียบความแตกต่างของภาพ.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### ขั้นตอนที่ 4: ทำ Linear Extrusion บน Left Node (รายละเอียดต่ำ)

ที่นี่เราทำ extrusion สี่เหลี่ยมโดยใช้เพียง **2 slices**. ผลลัพธ์เป็น mesh แบบหยาบ—เหมาะสำหรับการพรีวิวอย่างรวดเร็ว.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### ขั้นตอนที่ 5: ทำ Linear Extrusion บน Right Node (รายละเอียดสูง)

ตอนนี้เราใช้ **10 slices** เพื่อให้ผลลัพธ์เรียบขึ้นมาก สังเกตว่าเรขาคณิตกลายเป็นละเอียดมากขึ้น.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### ขั้นตอนที่ 6: บันทึก 3D Scene

สุดท้าย, เขียน scene ไปยังไฟล์ OBJ. แทนที่ `"Your Output Directory"` ด้วยพาธที่ถูกต้องบนเครื่องของคุณ.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## ปัญหาที่พบบ่อยและวิธีแก้

| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| **ไม่มีไฟล์ถูกสร้าง** | พาธเอาต์พุตไม่ถูกต้องหรือไม่มีสิทธิ์การเขียน. | ใช้พาธแบบเต็มและตรวจสอบให้แน่ใจว่าโฟลเดอร์มีอยู่. |
| **วัตถุดูแบน** | `Slices` ถูกตั้งเป็น 1 หรือ 0. | ตั้งค่า `Slices` อย่างน้อยเป็น 2 เพื่อให้ extrusion ปรากฏ. |
| **เรขาคณิตไม่คาดคิด** | รัศมีการโค้งใหญ่เกินขนาดของสี่เหลี่ยม. | ปรับค่า `RoundingRadius` ให้มีค่าน้อยกว่าครึ่งหนึ่งของด้านสั้นที่สุดของสี่เหลี่ยม. |

## คำถามที่พบบ่อย

**Q: ฉันสามารถเปลี่ยนทิศทางของ extrusion ได้หรือไม่?**  
A: ใช่. ใช้คุณสมบัติ `Transform` บนโหนดเพื่อหมุนหรือย้ายตำแหน่งเรขาคณิตที่ extrusion ก่อนบันทึก.

**Q: Aspose.3D รองรับประเภท extrusion อื่น ๆ หรือไม่?**  
A: แน่นอน. นอกจาก `LinearExtrusion` คุณสามารถใช้ `RevolveExtrusion`, `SweepExtrusion`, และอื่น ๆ

**Q: ฉันสามารถส่งออกเป็นไฟล์รูปแบบใดได้บ้าง?**  
A: Aspose.3D รองรับ OBJ, STL, FBX, 3MF, Collada และอื่น ๆ อีกมาก. เพียงเปลี่ยนค่า enum `FileFormat`.

**Q: มีวิธีตั้งค่า material ผ่านโปรแกรมได้หรือไม่?**  
A: มี. หลังจากสร้างโหนด, กำหนด `Material` ให้กับคอลเลกชัน `Entity` ของมัน.

**Q: จำนวน slices มีผลต่อการใช้หน่วยความจำอย่างไร?**  
A: Slices มากขึ้นจะเพิ่มจำนวนเวอร์เท็กซ์และหน้า, ซึ่งทำให้การใช้หน่วยความจำเพิ่มขึ้นตามสัดส่วน. ใช้การ profiling เพื่อหาจุดที่เหมาะสมสำหรับแพลตฟอร์มเป้าหมายของคุณ.

## FAQ ดั้งเดิม

### Q1: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับภาษาโปรแกรมอื่นได้หรือไม่?

A1: Aspose.3D ถูกออกแบบมาสำหรับ .NET เป็นหลัก, แต่คุณสามารถสำรวจตัวเลือกการทำงานร่วมกับภาษาอื่นเช่น Python โดยใช้ .NET bindings.

### Q2: ฉันจะหาเอกสารรายละเอียดของ Aspose.3D สำหรับ .NET ได้จากที่ไหน?

A2: ดูเอกสารที่ [here](https://reference.aspose.com/3d/net/) เพื่อรับข้อมูลเชิงลึกเกี่ยวกับความสามารถและการใช้งานของ Aspose.3D.

### Q3: มีการทดลองใช้งานฟรีสำหรับ Aspose.3D สำหรับ .NET หรือไม่?

A3: มี, คุณสามารถรับการทดลองใช้งานฟรีได้ที่ [here](https://releases.aspose.com/) เพื่อสำรวจคุณสมบัติของไลบรารีก่อนทำการซื้อ.

### Q4: ฉันจะรับการสนับสนุนทางเทคนิคสำหรับ Aspose.3D สำหรับ .NET อย่างไร?

A4: เยี่ยมชมฟอรั่ม Aspose.3D ที่ [here](https://forum.aspose.com/c/3d/18) เพื่อขอความช่วยเหลือและเข้าร่วมกับชุมชน.

### Q5: ฉันสามารถใช้ใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ .NET ได้หรือไม่?

A5: มี, รับใบอนุญาตชั่วคราวได้ที่ [here](https://purchase.aspose.com/temporary-license/) เพื่อการประเมิน.

## สรุป

คุณได้เห็น **วิธีทำ linear extrusion** ด้วย slices โดยใช้ Aspose.3D สำหรับ .NET, สำรวจผลกระทบของจำนวน slice ที่ต่างกัน, และเรียนรู้วิธีส่งออกงานของคุณ. ทดลองกับโปรไฟล์อื่น ๆ, ปรับค่า `Slices`, และรวม material หรือแสงเพื่อสร้างทรัพย์สิน 3‑D ที่พร้อมใช้งานในผลิตภัณฑ์.

---

**อัปเดตล่าสุด:** 2026-03-23  
**ทดสอบด้วย:** Aspose.3D 24.11 สำหรับ .NET (ล่าสุด ณ เวลาที่เขียน)  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}