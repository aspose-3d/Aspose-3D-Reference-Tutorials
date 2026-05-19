---
date: 2026-03-28
description: เรียนรู้วิธีทำให้ลูกบาศก์เคลื่อนไหวในฉาก 3 มิติด้วย Aspose.3D สำหรับ
  .NET และส่งออกฉากที่เคลื่อนไหวเป็นไฟล์ FBX คู่มือนี้จะแสดงวิธีสร้างโค้งแอนิเมชัน
  ผูกคีย์เฟรม และทำให้คุณสมบัติ 3 มิติเคลื่อนไหว
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: วิธีทำแอนิเมชันลูกบาศก์ในฉาก 3D ด้วย Aspose.3D สำหรับ .NET
url: /th/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีทำให้ลูกบาศก์เคลื่อนไหวในฉาก 3D ด้วย Aspose.3D สำหรับ .NET

## บทนำ

ถ้าคุณกำลังสำรวจโลกของการสร้างฉาก 3D และการทำแอนิเมชันใน .NET, Aspose.3D คือเครื่องมือที่คุณควรใช้ ในคู่มือขั้นตอนนี้ เราจะสำรวจ **how to animate cube** โดยการทำแอนิเมชันให้กับคุณสมบัติต่าง ๆ ของมัน, สร้าง animation curves, และผูก keyframes. เมื่อเสร็จคุณจะได้ลูกบาศก์ที่เคลื่อนไหวเต็มรูปแบบและสามารถส่งออกไปยังรูปแบบ 3D ที่นิยมได้

## คำตอบสั้น
- **ไลบรารีที่ใช้คืออะไร?** Aspose.3D for .NET  
- **งานหลักที่บทเรียนนี้ครอบคลุมคืออะไร?** วิธีทำให้ลูกบาศก์เคลื่อนไหวในฉาก 3D  
- **ขั้นตอนสำคัญ?** Import namespaces, create a scene, bind keyframes, save the file  
- **ฉันต้องการไลเซนส์หรือไม่?** A free trial works for learning; a commercial license is required for production  
- **รูปแบบเอาต์พุตที่รองรับ?** FBX (ASCII 7500) and others supported by Aspose.3D  

## อะไรคือ “how to animate cube” ใน Aspose.3D?
การทำแอนิเมชันให้กับลูกบาศก์หมายถึงการปรับเปลี่ยนคุณสมบัติการแปลง (เช่น Translation, Rotation หรือ Scale) ตามเวลาโดยใช้ข้อมูล keyframe. Aspose.3D มี API ที่สะอาดเพื่อสร้าง **animation curves**, **bind keyframes**, และ **animate 3D properties** โดยตรงบนโหนดของฉาก

## ทำไมต้องทำแอนิเมชันให้ลูกบาศก์ด้วย Aspose.3D?
- **Full .NET integration** – ทำงานกับ .NET Framework, .NET Core, และ .NET 5/6.  
- **No external dependencies** – ไม่จำเป็นต้องใช้ Unity หรือเอนจินอื่นสำหรับแอนิเมชันง่าย ๆ.  
- **Export flexibility** – ฉากที่ทำแอนิเมชันสามารถบันทึกเป็น FBX, OBJ, GLTF ฯลฯ สำหรับกระบวนการต่อไป  

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มการเดินทางที่น่าตื่นเต้นนี้ โปรดตรวจสอบว่าคุณมีข้อกำหนดต่อไปนี้พร้อมแล้ว:

- Aspose.3D for .NET: ตรวจสอบว่าคุณได้ติดตั้งไลบรารีแล้ว คุณสามารถดาวน์โหลดได้จาก [Aspose.3D website](https://releases.aspose.com/3d/net/).
- Knowledge of C#: ความคุ้นเคยกับภาษาโปรแกรม C# เป็นสิ่งจำเป็นสำหรับการเข้าใจและทำตามตัวอย่าง
- Integrated Development Environment (IDE): ใช้ IDE ที่คุณชื่นชอบ เช่น Visual Studio สำหรับเขียนโค้ดตามตัวอย่าง
- Basic 3D Scene Concepts: ความเข้าใจพื้นฐานเกี่ยวกับแนวคิดฉาก 3D จะทำให้การเรียนรู้ของคุณราบรื่นขึ้น

## นำเข้า Namespaces

ในโค้ด C# ของคุณ ให้แน่ใจว่าคุณได้นำเข้า namespaces ที่จำเป็นสำหรับ Aspose.3D ต่อไปนี้คือชุดที่ต้องใช้:

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

## ขั้นตอนที่ 1: เริ่มต้นอ็อบเจ็กต์ Scene

สร้างฉากเปล่าที่จะเก็บโหนดและแอนิเมชันทั้งหมดของเรา

```csharp
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: สร้าง Mesh ด้วย Polygon Builder

เราสร้าง mesh ลูกบาศก์ง่าย ๆ ด้วยเมธอดช่วยเหลือ `Common.CreateMeshUsingPolygonBuilder()`.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## ขั้นตอนที่ 3: สร้างโหนดลูกบาศก์

เพิ่ม mesh ลูกบาศก์ลงในฉากเป็นโหนดลูกของราก ชื่อโหนด **cube1** จะถูกใช้ในภายหลังเมื่อเราผูก keyframes.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## ขั้นตอนที่ 4: ค้นหาคุณสมบัติ Translation

เพื่อทำให้ลูกบาศก์เคลื่อนที่ เราต้องหาคุณสมบัติ **Translation** บนการแปลงของโหนด

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## ขั้นตอนที่ 5: สร้าง Bind Point

`BindPoint` เชื่อมคุณสมบัติของฉากกับ animation curve ที่นี่เราผูกคุณสมบัติ translation

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## ขั้นตอนที่ 6: ผูก Animation Curve บนส่วนประกอบ X

ตอนนี้เราสร้าง animation curve สำหรับแกน **X** นี้เป็นการสาธิตขั้นตอน **create animation curve** และแสดงวิธี **bind keyframes**.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## ขั้นตอนที่ 7: ผูก Animation Curve บนส่วนประกอบ Z

เช่นเดียวกัน เราทำแอนิเมชันแกน **Z** เพื่อให้ลูกบาศก์มีเส้นทางการเคลื่อนที่ที่ไดนามิกมากขึ้น

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## ขั้นตอนที่ 8: บันทึกฉาก 3D

ส่งออกฉากที่ทำแอนิเมชันเป็นไฟล์ FBX รูปแบบ `FBX7500ASCII` ได้รับการสนับสนุนอย่างกว้างขวางโดยเครื่องมือ 3D

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## ขั้นตอนที่ 9: แสดงข้อความสำเร็จ

ให้ผู้ใช้รับทราบว่าการทำแอนิเมชันได้ถูกเพิ่มสำเร็จแล้ว

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## ส่งออกฉากที่ทำแอนิเมชันเป็น FBX

หนึ่งในงานที่พบบ่อยที่สุดหลังจากทำแอนิเมชันให้กับลูกบาศก์คือ **export animated scene FBX** เพื่อให้แอปพลิเคชัน 3D อื่น ๆ สามารถใช้งานได้ โค้ดข้างต้นได้บันทึกฉากในรูปแบบ FBX7500ASCII ซึ่งรักษาข้อมูล keyframe ไว้และทำงานได้อย่างราบรื่นกับเครื่องมือเช่น Autodesk Maya, Blender, และ Unity เมื่อคุณเปิดไฟล์ `.fbx` ที่ได้ คุณควรเห็นลูกบาศก์เคลื่อนที่ตามแกน X และ Z ตามที่กำหนดในลำดับ keyframe

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|-----|
| ไม่พบการเคลื่อนที่ | เวลา keyframe ไม่ตรงกับช่วงการเล่น | ตรวจสอบให้แน่ใจว่าไทม์ไลน์แอนิเมชันของฉากครอบคลุมช่วงเวลา keyframe (0‑5 วินาทีในตัวอย่างนี้). |
| เส้นทางไฟล์ไม่ถูกต้อง | `output` ชี้ไปยังไดเรกทอรีที่ไม่มีอยู่ | สร้างไดเรกทอรีก่อนหรือใช้เส้นทางแบบ absolute. |
| ข้อยกเว้นไลเซนส์ | รันโดยไม่มีไลเซนส์ที่ถูกต้องในสภาพการผลิต | ใช้ไลเซนส์ Aspose.3D ของคุณก่อนสร้าง `Scene`. |

## คำถามที่พบบ่อย

### Q1: ฉันสามารถหาเอกสาร Aspose.3D ได้จากที่ไหน?
A1: เอกสารพร้อมให้บริการ [ที่นี่](https://reference.aspose.com/3d/net/).

### Q2: ฉันจะดาวน์โหลด Aspose.3D สำหรับ .NET ได้อย่างไร?
A2: คุณสามารถดาวน์โหลดได้จาก [หน้ารีลีส](https://releases.aspose.com/3d/net/).

### Q3: มีการทดลองใช้ฟรีหรือไม่?
A3: มี, คุณสามารถรับการทดลองใช้ฟรี [ที่นี่](https://releases.aspose.com/).

### Q4: ฉันจะขอรับการสนับสนุนสำหรับ Aspose.3D ได้จากที่ไหน?
A4: เยี่ยมชม [ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อรับการสนับสนุน.

### Q5: ฉันสามารถขอรับไลเซนส์ชั่วคราวได้หรือไม่?
A5: มี, คุณสามารถรับไลเซนส์ชั่วคราว [ที่นี่](https://purchase.aspose.com/temporary-license/).

## FAQ เพิ่มเติม (AI‑Optimized)

**Q: ฉันสามารถทำแอนิเมชันคุณสมบัติอื่น ๆ เช่น การหมุนหรือการสเกลได้หรือไม่?**  
A: แน่นอน ใช้ `cube1.Transform.FindProperty("Rotation")` หรือ `"Scale"` และผูกลำดับ keyframe ในลักษณะเดียวกัน

**Q: Aspose.3D รองรับประเภทการแทรกค่ากลาง keyframe นอกเหนือจาก Bezier และ Linear หรือไม่?**  
A: ใช่, ยังรองรับ `Interpolation.Step` และ `Interpolation.Cubic` เพื่อการควบคุมที่มากขึ้น

**Q: ฉันจะดูตัวอย่างแอนิเมชันก่อนการส่งออกได้อย่างไร?**  
A: Aspose.3D มีตัวดูอย่างง่ายใน API; หรือคุณสามารถโหลด FBX ที่ส่งออกไปยังโปรแกรมดู 3D เช่น Autodesk FBX Review

**Q: สามารถทำแอนิเมชันหลายลูกบาศก์พร้อมกันได้หรือไม่?**  
A: สร้างโหนดแยกสำหรับแต่ละลูกบาศก์ ดึงคุณสมบัติเฉพาะของแต่ละอัน และผูกลำดับ keyframe อย่างอิสระ

## สรุป

ยินดีด้วย! คุณเพิ่งเชี่ยวชาญ **how to animate cube** ในฉาก 3D ด้วย Aspose.3D สำหรับ .NET ตอนนี้คุณรู้วิธี **create animation curves**, **bind keyframes**, และ **export animated scene FBX** เพื่อทำให้เรขาคณิตคงที่มีชีวิตชีวา อย่าลังเลที่จะทดลองการหมุน, การสเกล, หรือแม้กระทั่ง morph targets เพื่อขยายชุดเครื่องมือแอนิเมชันของคุณ

---

**อัปเดตล่าสุด:** 2026-03-28  
**ทดสอบด้วย:** Aspose.3D 24.11 for .NET  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}