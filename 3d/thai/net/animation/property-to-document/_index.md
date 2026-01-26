---
date: 2026-01-14
description: เรียนรู้วิธีทำให้ลูกบาศก์เคลื่อนไหวในฉาก 3 มิติด้วย Aspose.3D สำหรับ
  .NET คู่มือนี้แสดงวิธีสร้างเส้นโค้งแอนิเมชัน, ผูกคีย์เฟรม และทำให้คุณสมบัติ 3 มิติเคลื่อนไหว
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: วิธีทำแอนิเมชันลูกบาศก์ในฉาก 3 มิติด้วย Aspose.3D สำหรับ .NET
url: /th/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีทำแอนิเมชันลูกบาศก์ในฉาก 3D ด้วย Aspose.3D สำหรับ .NET

## บทนำ

หากคุณกำลังสำรวจการสร้างและทำแอนิเมชันฉาก 3D ใน .NET, Aspose.3D คือเครื่องมือที่คุณควรใช้ ในคู่มือขั้นตอนนี้ เราจะสำรวจ **วิธีทำแอนิเมชันลูกบาศก์** โดยการแอนิเมชันคุณสมบัติต่าง ๆ ของมัน, สร้างเส้นโค้งแอนิเมชัน, และผูกคีย์เฟรม สุดท้ายคุณจะได้ลูกบาศก์ที่แอนิเมชันเต็มรูปแบบและสามารถส่งออกเป็นฟอร์แมต 3D ยอดนิยมได้

## คำตอบสั้น
- **ใช้ไลบรารีอะไร?** Aspose.3D สำหรับ .NET  
- **งานหลักที่สอนในบทนี้คืออะไร?** วิธีทำแอนิเมชันลูกบาศก์ในฉาก 3D  
- **ขั้นตอนสำคัญ?** นำเข้า namespace, สร้างฉาก, ผูกคีย์เฟรม, บันทึกไฟล์  
- **ต้องมีไลเซนส์หรือไม่?** ทดลองใช้งานฟรีสำหรับการเรียนรู้; ต้องมีไลเซนส์เชิงพาณิชย์สำหรับการผลิต  
- **ฟอร์แมตผลลัพธ์ที่รองรับ?** FBX (ASCII 7500) และฟอร์แมตอื่น ๆ ที่ Aspose.3D รองรับ  

## “วิธีทำแอนิเมชันลูกบาศก์” ใน Aspose.3D คืออะไร?
การทำแอนิเมชันลูกบาศก์หมายถึงการเปลี่ยนแปลงคุณสมบัติการแปลง (เช่น Translation, Rotation หรือ Scale) ของมันตามเวลาโดยใช้ข้อมูลคีย์เฟรม Aspose.3D มี API ที่ชัดเจนสำหรับสร้าง **เส้นโค้งแอนิเมชัน**, **ผูกคีย์เฟรม**, และ **ทำแอนิเมชันคุณสมบัติ 3D** โดยตรงบนโหนดของฉาก

## ทำไมต้องทำแอนิเมชันลูกบาศก์ด้วย Aspose.3D?
- **บูรณาการเต็มรูปแบบกับ .NET** – ทำงานกับ .NET Framework, .NET Core, และ .NET 5/6  
- **ไม่มีการพึ่งพาภายนอก** – ไม่ต้องใช้ Unity หรือเอนจิ้นอื่นสำหรับแอนิเมชันง่าย ๆ  
- **ความยืดหยุ่นในการส่งออก** – ฉากที่แอนิเมชันแล้วสามารถบันทึกเป็น FBX, OBJ, GLTF ฯลฯ สำหรับขั้นตอนต่อไปได้  

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มการเดินทางที่น่าตื่นเต้นนี้ โปรดตรวจสอบว่าคุณมีข้อกำหนดต่อไปนี้พร้อมใช้งาน:

- Aspose.3D สำหรับ .NET: ตรวจสอบว่าคุณได้ติดตั้งไลบรารีแล้ว คุณสามารถดาวน์โหลดได้จาก [เว็บไซต์ Aspose.3D](https://releases.aspose.com/3d/net/)  
- ความรู้ด้าน C#: ความคุ้นเคยกับภาษาโปรแกรม C# เป็นสิ่งจำเป็นสำหรับการเข้าใจและนำตัวอย่างไปใช้  
- Integrated Development Environment (IDE): ใช้ IDE ที่คุณชื่นชอบ เช่น Visual Studio สำหรับเขียนโค้ดตามตัวอย่าง  
- แนวคิดพื้นฐานของฉาก 3D: ความเข้าใจพื้นฐานเกี่ยวกับฉาก 3D จะทำให้การเรียนรู้ของคุณราบรื่นขึ้น  

## นำเข้า Namespace

ในโค้ด C# ของคุณ ให้แน่ใจว่าได้นำเข้า namespace ที่จำเป็นสำหรับ Aspose.3D ดังนี้:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## ขั้นตอนที่ 1: เริ่มต้นอ็อบเจกต์ Scene

สร้างฉากเปล่าที่จะเก็บโหนดและแอนิเมชันทั้งหมดของเรา

```csharp
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: สร้าง Mesh ด้วย Polygon Builder

เราจะสร้างเมชลูกบาศก์ง่าย ๆ ด้วยเมธอดช่วย `Common.CreateMeshUsingPolygonBuilder()`

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## ขั้นตอนที่ 3: สร้างโหนดลูกบาศก์

เพิ่มเมชลูกบาศก์ลงในฉากเป็นโหนดลูกของราก โหนดชื่อ **cube1** จะถูกใช้ต่อไปเมื่อผูกคีย์เฟรม

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## ขั้นตอนที่ 4: ค้นหาคุณสมบัติ Translation

เพื่อทำแอนิเมชันตำแหน่งของลูกบาศก์ เราต้องหา **Translation** บน Transform ของโหนด

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## ขั้นตอนที่ 5: สร้าง Bind Point

`BindPoint` เชื่อมคุณสมบัติของฉากกับเส้นโค้งแอนิเมชัน ที่นี่เราจะผูกคุณสมบัติ Translation

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## ขั้นตอนที่ 6: ผูกเส้นโค้งแอนิเมชันบนแกน X

ต่อไปเราจะสร้างเส้นโค้งแอนิเมชันสำหรับแกน **X** ซึ่งเป็นการสาธิตขั้นตอน **create animation curve** และแสดงวิธี **bind keyframes**

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## ขั้นตอนที่ 7: ผูกเส้นโค้งแอนิเมชันบนแกน Z

เช่นเดียวกัน เราจะทำแอนิเมชันแกน **Z** เพื่อให้ลูกบาศก์มีเส้นทางการเคลื่อนที่ที่ไดนามิกมากขึ้น

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## ขั้นตอนที่ 8: บันทึกฉาก 3D

ส่งออกฉากที่แอนิเมชันแล้วเป็นไฟล์ FBX ฟอร์แมต `FBX7500ASCII` ได้รับการสนับสนุนอย่างกว้างขวางโดยเครื่องมือ 3D ต่าง ๆ

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## ขั้นตอนที่ 9: แสดงข้อความสำเร็จ

แจ้งผู้ใช้ว่าการแอนิเมชันได้ถูกเพิ่มสำเร็จแล้ว

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|-----|
| ไม่เห็นการเคลื่อนที่ | เวลาในคีย์เฟรมไม่ตรงกับช่วงการเล่น | ตรวจสอบให้แน่ใจว่าไทม์ไลน์ของฉากครอบคลุมเวลาคีย์เฟรม (0‑5 วินาทีในตัวอย่างนี้) |
| เส้นทางไฟล์ไม่ถูกต้อง | `output` ชี้ไปยังไดเรกทอรีที่ไม่มีอยู่ | สร้างไดเรกทอรีก่อนหรือใช้เส้นทางแบบเต็ม |
| ข้อผิดพลาดไลเซนส์ | รันโดยไม่มีไลเซนส์ที่ถูกต้องในสภาพการผลิต | ใช้ไลเซนส์ Aspose.3D ของคุณก่อนสร้าง `Scene` |

## คำถามที่พบบ่อย

### Q1: ฉันจะหาเอกสาร Aspose.3D ได้จากที่ไหน?

A1: เอกสารพร้อมให้บริการ [ที่นี่](https://reference.aspose.com/3d/net/)

### Q2: ฉันจะดาวน์โหลด Aspose.3D สำหรับ .NET ได้อย่างไร?

A2: คุณสามารถดาวน์โหลดได้จาก [หน้ารีลีส](https://releases.aspose.com/3d/net/)

### Q3: มีรุ่นทดลองฟรีหรือไม่?

A3: มี, คุณสามารถรับรุ่นทดลองฟรี [ที่นี่](https://releases.aspose.com/)

### Q4: จะหาการสนับสนุนสำหรับ Aspose.3D ได้จากที่ไหน?

A4: เยี่ยมชม [ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อรับการสนับสนุน

### Q5: ฉันสามารถขอไลเซนส์ชั่วคราวได้หรือไม่?

A5: ได้, คุณสามารถขอไลเซนส์ชั่วคราว [ที่นี่](https://purchase.aspose.com/temporary-license/)

## FAQ เพิ่มเติม (AI‑Optimized)

**Q: ฉันสามารถทำแอนิเมชันคุณสมบัติอื่น ๆ เช่น การหมุนหรือสเกลได้หรือไม่?**  
A: แน่นอน ใช้ `cube1.Transform.FindProperty("Rotation")` หรือ `"Scale"` แล้วผูกลำดับคีย์เฟรมในลักษณะเดียวกัน

**Q: Aspose.3D รองรับประเภทการแทรกค่าคีย์เฟรมอื่น ๆ นอกจาก Bezier และ Linear หรือไม่?**  
A: รองรับ `Interpolation.Step` และ `Interpolation.Cubic` เพื่อควบคุมที่ละเอียดขึ้น

**Q: ฉันจะดูตัวอย่างแอนิเมชันก่อนส่งออกได้อย่างไร?**  
A: Aspose.3D มี viewer ง่ายใน API; หรือโหลดไฟล์ FBX ที่ส่งออกแล้วเปิดใน 3D viewer เช่น Autodesk FBX Review

**Q: สามารถทำแอนิเมชันหลายลูกบาศก์พร้อมกันได้หรือไม่?**  
A: สร้างโหนดแยกสำหรับแต่ละลูกบาศก์, ดึงคุณสมบัติของแต่ละโหนด, แล้วผูกลำดับคีย์เฟรมอิสระกัน

## สรุป

ขอแสดงความยินดี! คุณเพิ่งเชี่ยวชาญ **วิธีทำแอนิเมชันลูกบาศก์** ในฉาก 3D ด้วย Aspose.3D สำหรับ .NET ตอนนี้คุณรู้วิธี **สร้างเส้นโค้งแอนิเมชัน**, **ผูกคีย์เฟรม**, และ **ทำแอนิเมชันคุณสมบัติ 3D** เพื่อทำให้เรขาคณิตคงที่มีชีวิตชีวา อย่าลังเลที่จะทดลองหมุน, ขยาย, หรือแม้กระทั่ง morph targets เพื่อขยายชุดเครื่องมือแอนิเมชันของคุณ

---

**อัปเดตล่าสุด:** 2026-01-14  
**ทดสอบด้วย:** Aspose.3D 24.11 สำหรับ .NET  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}