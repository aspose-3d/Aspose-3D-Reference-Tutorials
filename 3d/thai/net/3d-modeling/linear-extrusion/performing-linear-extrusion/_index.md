---
date: 2026-01-07
description: เรียนรู้วิธีดึงเส้นตรง (linear extrude) โปรไฟล์ 2 มิติและส่งออกโมเดล
  3 มิติในรูปแบบ OBJ ด้วย Aspose.3D สำหรับ .NET บทแนะนำการดึงเส้นตรงนี้จะพาคุณผ่านขั้นตอนทีละขั้นตอน.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: วิธีทำ Linear Extrude ด้วย Aspose.3D สำหรับ .NET
url: /th/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีทำ Linear Extrude ด้วย Aspose.3D สำหรับ .NET

## บทนำ

ยินดีต้อนรับสู่ **linear extrusion tutorial** ของเรา! ในคู่มือนี้คุณจะได้เรียนรู้ **how to linear extrude** โปรไฟล์ 2‑D และแปลงเป็นวัตถุ 3‑D ที่สมบูรณ์โดยใช้ Aspose.3D สำหรับ .NET ไม่ว่าคุณจะกำลังสร้างแอปพลิเคชันสไตล์ CAD หรือเพียงต้องการ **export 3d model obj** สำหรับการประมวลผลต่อไป คู่มือขั้นตอนนี้จะช่วยให้คุณมั่นใจในการเพิ่มการสร้างเรขาคณิตที่ทรงพลังให้กับโครงการของคุณ.

## คำตอบอย่างรวดเร็ว
- **What is linear extrusion?** การขยายรูป 2‑D ไปตามเส้นตรงเพื่อสร้างวัตถุ 3‑D ที่เป็นของแข็ง.  
- **Which library do we use?** Aspose.3D for .NET.  
- **Do I need a license?** ใบอนุญาตชั่วคราวใช้ได้สำหรับการทดสอบ; จำเป็นต้องมีใบอนุญาตเต็มสำหรับการใช้งานจริง.  
- **Can I export to OBJ?** ได้ – ฉากสุดท้ายจะถูกบันทึกเป็นไฟล์ Wavefront OBJ.  
- **How many lines of code?** น้อยกว่า 30 บรรทัดของ C# พร้อมคอมเมนต์อธิบาย.

## Linear Extrusion คืออะไร?

Linear extrusion จะรับโปรไฟล์แบน (เช่นสี่เหลี่ยมหรือวงกลม) แล้วสแกนตามเส้นตรง โดยอาจเพิ่มการบิด, การสเกล, หรือการออฟเซ็ต ผลลัพธ์คือของแข็งที่สามารถเรนเดอร์, แก้ไข, หรือส่งออกเพื่อใช้ในเครื่องมือ 3‑D อื่น ๆ ได้.

## ทำไมต้องใช้ Aspose.3D สำหรับ Linear Extrusion?

* **Zero‑dependency:** ไม่จำเป็นต้องใช้เคอร์เนล CAD ภายนอก.  
* **Full .NET support:** ทำงานกับ .NET Framework, .NET Core, และ .NET 5/6+.  
* **Export flexibility:** บันทึกโดยตรงเป็น OBJ, STL, FBX และรูปแบบอื่น ๆ มากมาย.  
* **Rich API:** ควบคุม slices, twist, และ offsets ได้ด้วยคุณสมบัติเพียงไม่กี่ตัว.

## ข้อกำหนดเบื้องต้น

1. **Aspose.3D installed** – ดาวน์โหลดได้จาก [here](https://releases.aspose.com/3d/net/).  
2. **Documentation access** – ทำตามคู่มือการตั้งค่า [here](https://reference.aspose.com/3d/net/).  
3. สภาพแวดล้อมการพัฒนา .NET (Visual Studio, VS Code, หรือ Rider) พร้อมอ้างอิงเนมสเปซที่จำเป็น.

## นำเข้า Namespaces

รวมเนมสเปซที่จำเป็นเพื่อเปิดใช้งานฟังก์ชันของ Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

เนมสเปซเหล่านี้ให้คุณเข้าถึง `Scene`, `LinearExtrusion`, `RectangleShape` และคลาสยูทิลิตี้เช่น `Vector3`.

## การทำ Linear Extrusion

ด้านล่างเป็นขั้นตอนการทำงานทั้งหมด แต่ละขั้นจะอธิบายด้วยภาษาง่าย ๆ ก่อนโค้ดบล็อกที่สอดคล้องกัน เพื่อให้คุณทำตามได้โดยไม่ต้องเดาว่าโค้ดทำอะไร

### ขั้นตอนที่ 1: เริ่มต้น Base Profile

แรกสุด สร้างรูป 2‑D ที่จะทำการ extrude ในตัวอย่างนี้เราใช้สี่เหลี่ยมที่มีรัศมีการโค้งเล็กน้อย.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*ทำไมสิ่งนี้สำคัญ:* โปรไฟล์กำหนดส่วนตัดของวัตถุ 3‑D สุดท้าย ปรับ `RoundingRadius`, ความกว้าง หรือความสูงเพื่อให้ได้รูปทรงที่ต่างกัน.

### ขั้นตอนที่ 2: ใช้ Linear Extrusion

ต่อไปเราจะสแกนโปรไฟล์ 10 หน่วยตามแกน Z, เพิ่ม 100 slices เพื่อความเรียบ, จัดศูนย์ geometry, และใช้การบิดเต็ม 360° พร้อมออฟเซ็ต.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*เคล็ดลับ:* ปรับ `Slices` เพื่อสมดุลระหว่างประสิทธิภาพและคุณภาพภาพ, และทดลองกับ `Twist` เพื่อสร้างเอฟเฟกต์สไปรัล.

### ขั้นตอนที่ 3: สร้าง Scene

`Scene` ทำหน้าที่เป็นคอนเทนเนอร์สำหรับเอนทิตี 3‑D ทั้งหมด — คิดว่าเป็นผ้าใบ.

```csharp
Scene scene = new Scene();
```

### ขั้นตอนที่ 4: เพิ่ม Extrusion ไปยัง Scene

แนบ geometry ที่ทำการ extrude ไปยังโหนดรากของ scene เพื่อให้เป็นส่วนหนึ่งของโครงสร้างที่สามารถเรนเดอร์ได้.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### ขั้นตอนที่ 5: บันทึกโมเดล 3‑D

สุดท้าย ส่งออก scene ไปยังไฟล์ OBJ ที่รองรับอย่างกว้างขวาง นี้แสดงความสามารถ **export 3d model obj** ของ Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

เมื่อคุณเปิดไฟล์ `LinearExtrusion.obj` ที่ได้ในโปรแกรมดู 3‑D ใด ๆ คุณจะเห็นรูปปริซึมสี่เหลี่ยมบิด – ตรงกับที่โค้ดอธิบาย.

## ปัญหาที่พบบ่อยและเคล็ดลับ

| Issue | Why it Happens | How to Fix |
|-------|----------------|------------|
| **Profile not visible** | ลืมเพิ่ม extrusion ไปยัง scene. | ตรวจสอบให้แน่ใจว่าเรียก `CreateChildNode`. |
| **Twist looks flat** | `Slices` ต่ำเกินไป ทำให้ geometry หยาบ. | เพิ่มค่า `Slices` (เช่น 200) เพื่อให้การบิดเรียบขึ้น. |
| **Export fails** | โฟลเดอร์ปลายทางไม่มีหรือไม่มีสิทธิ์เขียน. | ใช้ `RunExamples.GetOutputFilePath` หรือสร้างโฟลเดอร์ด้วยตนเอง. |
| **Unexpected scaling** | ตั้งค่า `Center` เป็น `false` ทำให้ geometry เลื่อน. | ตั้งค่า `Center = true` เว้นแต่ต้องการออฟเซ็ต. |

## คำถามที่พบบ่อย Q1: Aspose.3D เหมาะสำหรับผู้เริ่มต้นหรือไม่?
A1: แน่นอน! Aspose.3D มี API ที่เป็นมิตรต่อผู้ใช้ และบทเรียนนี้พาคุณผ่านพื้นฐานของ linear extrusion.

### Q2: ฉันสามารถใช้ Aspose.3D ในโครงการเชิงพาณิชย์ได้หรือไม่?
A2: ใช่, Aspose.3D มีตัวเลือกการให้ลิขสิทธิ์สำหรับการใช้งานส่วนบุคคลและเชิงพาณิชย์ ตรวจสอบรายละเอียดได้ที่ [here](https://purchase.aspose.com/buy).

### Q3: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับการทดสอบได้อย่างไร?
A3: เยี่ยมชม [this link](https://purchase.aspose.com/temporary-license/) เพื่อรับใบอนุญาตชั่วคราวสำหรับการทดสอบ.

### Q4: ฉันจะหาแหล่งสนับสนุนจากชุมชนได้ที่ไหน?
A4: เข้าร่วม [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) เพื่อเชื่อมต่อกับชุมชนที่กระตือรือร้นและขอความช่วยเหลือ.

### Q5: มีรุ่นทดลองฟรีหรือไม่?
A5: แน่นอน! ดาวน์โหลดรุ่นทดลองฟรี [here](https://releases.aspose.com/) เพื่อสัมผัสความสามารถของ Aspose.3D ด้วยตนเอง.

**อัปเดตล่าสุด:** 2026-01-07  
**ทดสอบด้วย:** Aspose.3D 24.11 for .NET  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}