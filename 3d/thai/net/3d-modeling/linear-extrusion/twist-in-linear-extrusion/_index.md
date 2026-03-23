---
date: 2026-03-23
description: เรียนรู้วิธีสร้างการดันรูปทรงพร้อมการบิดโดยใช้ Aspose.3D สำหรับ .NET
  คู่มือแบบขั้นตอนนี้ครอบคลุมเทคนิคการบิดการดันเชิงเส้น.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: วิธีสร้างการอัดรูปแบบบิดในกระบวนการอัดรูปเชิงเส้น
url: /th/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีสร้าง Extrusion พร้อมการบิดใน Linear Extrusion

## บทนำ

หากคุณกำลังพัฒนาแอปพลิเคชัน .NET ที่ต้องการภาพ 3D ที่ดึงดูดสายตา คุณจะได้พบว่า **วิธีสร้าง extrusion** เป็นทักษะพื้นฐานที่สำคัญ Aspose.3D for .NET มอบ API ที่สะอาดและประสิทธิภาพสูงเพื่อเปลี่ยนโปรไฟล์ 2‑D แบบง่ายให้เป็นโมเดล 3‑D ที่ซับซ้อน—โดยเฉพาะเมื่อคุณเพิ่มการบิด ในบทแนะนำนี้เราจะเดินผ่านทุกขั้นตอน ตั้งแต่การตั้งค่า scene จนถึงการบันทึกไฟล์ OBJ สุดท้าย เพื่อให้คุณได้เห็นพลังของ linear extrusion twist ในการทำงานจริง

## คำตอบสั้น
- **คลาสหลักสำหรับ extrusion คืออะไร?** `LinearExtrusion`
- **คุณสมบัติใดที่เพิ่มการหมุน?** `Twist`
- **ต้องใช้ slice จำนวนเท่าไหร่จึงได้ผลลัพธ์เรียบ?** ประมาณ 100 slices (ปรับตามต้องการ)
- **ฉันสามารถใช้รูปทรงอื่นได้หรือไม่?** ใช่, `IProfile` ใดก็ได้ เช่น วงกลม, รูปหลายเหลี่ยม, หรือเส้นโค้งที่กำหนดเอง
- **รูปแบบไฟล์ที่ใช้ในตัวอย่างคืออะไร?** Wavefront OBJ (`.obj`)

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มลงมือ โปรดตรวจสอบว่าคุณมีสิ่งต่อไปนี้แล้ว:

- Aspose.3D for .NET ติดตั้งแล้ว หากคุณยังไม่ได้ดาวน์โหลด, ดาวน์โหลดได้ **[ที่นี่](https://releases.aspose.com/3d/net/)**.
- สภาพแวดล้อมการพัฒนา .NET ที่ทำงานได้ (Visual Studio, VS Code หรือ IDE ใดก็ได้ที่คุณชอบ)
- ความคุ้นเคยพื้นฐานกับไวยากรณ์ C# และแนวคิดเชิงวัตถุ

## นำเข้า Namespaces

ในโครงการ .NET ใด ๆ การใช้ namespaces อย่างเหมาะสมเป็นสิ่งสำคัญ เริ่มต้นโดยการนำเข้า namespaces ที่จำเป็นเพื่อใช้ประโยชน์จากฟังก์ชันของ Aspose.3D อย่างเต็มที่ นี่คือตัวอย่างโค้ดสั้น ๆ เพื่อเป็นแนวทางให้คุณ:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## คู่มือขั้นตอนต่อขั้นตอน

### ขั้นตอนที่ 1: เริ่มต้น Base Profile

เราจะกำหนดรูปทรงที่จะทำการ extrusion ในตัวอย่างนี้เราใช้สี่เหลี่ยมผืนผ้าที่มีรัศมีการโค้งเล็กน้อยเพื่อให้ขอบมีลักษณะโค้งอ่อนโยน

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### ขั้นตอนที่ 2: สร้าง 3D Scene

อ็อบเจกต์ `Scene` ทำหน้าที่เป็นผ้าใบที่ทุกเอนทิตี 3‑D อาศัยอยู่ คิดว่าเป็นเวทีสำหรับ extrusion ของคุณ

```csharp
// Create a scene 
Scene scene = new Scene();
```

### ขั้นตอนที่ 3: เพิ่ม Left และ Right Nodes

Nodes ช่วยให้คุณจัดระเบียบอ็อบเจกต์แบบลำดับชั้น เราจะสร้างสอง node พี่น้อง—หนึ่งสำหรับ extrusion แบบตรงและอีกหนึ่งสำหรับเวอร์ชันที่บิด

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### ขั้นตอนที่ 4: ทำ Linear Extrusion พร้อม Twist บน Left Node

คุณสมบัติ `Twist` ควบคุมว่ารูปโปรไฟล์จะหมุนเท่าไหร่ขณะ extrusion การตั้งค่าเป็น **0** จะให้ extrusion แบบตรงคลาสสิก

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### ขั้นตอนที่ 5: ทำ Linear Extrusion พร้อม Twist บน Right Node

ตอนนี้เราจะใช้การบิด 90 องศากับโปรไฟล์เดียวกัน ซึ่งจะแสดงผลของ **linear extrusion twist** อย่างชัดเจน

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### ขั้นตอนที่ 6: บันทึก 3D Scene

สุดท้าย ส่งออก scene ไปเป็นรูปแบบที่คุณสามารถดูในโปรแกรม 3‑D ใดก็ได้ ตัวอย่างใช้ Wavefront OBJ แต่ Aspose.3D รองรับรูปแบบอื่น ๆ อีกมากมาย

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## ทำไมต้องใช้ Linear Extrusion พร้อม Twist?

- **Rapid prototyping:** แปลงสเก็ตช์ 2‑D ให้เป็นชิ้นส่วน 3‑D โดยไม่ต้องโมเดลด้วยมือ
- **Design flexibility:** ปรับค่า `Twist` เพื่อสร้างสปิรัล, ริบแบบเกลียว, หรือฟีเจอร์ตกแต่ง
- **Performance‑friendly:** พารามิเตอร์ `Slices` ช่วยให้คุณสมดุลระหว่างความละเอียดภาพและความเร็วการทำงาน

## ปัญหาที่พบบ่อยและเคล็ดลับ

- **Slices มากเกินไป:** แม้ 100 slices จะดูเรียบ, ค่าที่สูงมากอาจทำให้การเรนเดอร์ช้า. ทดสอบด้วยจำนวนน้อยลงหากประสิทธิภาพเป็นปัญหา
- **ค่าการบิดเป็นลบ:** `Twist` ที่เป็นลบจะหมุนในทิศทางตรงกันข้าม—มีประโยชน์สำหรับการออกแบบแบบสะท้อน
- **เส้นทางไฟล์:** ตรวจสอบให้แน่ใจว่าไดเรกทอรีปลายทางมีอยู่และคุณมีสิทธิ์เขียน; มิฉะนั้น `scene.Save` จะโยนข้อยกเว้น

## สรุป

ในบทแนะนำนี้เราได้แสดง **วิธีสร้าง extrusion** พร้อมการบิดโดยใช้ Aspose.3D for .NET โดยการปรับค่า `Twist` และ `Slices` คุณสามารถสร้างรูปทรงที่หลากหลาย ตั้งแต่บาร์บิดง่าย ๆ ไปจนถึงโครงสร้างเกลียวซับซ้อน ทั้งหมดนี้ทำได้ด้วยเพียงไม่กี่บรรทัดของโค้ด

## คำถามที่พบบ่อย

**Q: ฉันสามารถใช้ linear extrusion พร้อมการบิดกับรูปทรงอื่นได้หรือไม่?**  
A: แน่นอน! คลาสใดก็ตามที่ implements `IProfile`—เช่น `CircleShape`, `PolygonShape` หรือ spline ที่กำหนดเอง—สามารถทำ extrusion พร้อมบิดได้

**Q: คุณสมบัติ `Twist` จริง ๆ แล้วหมายถึงอะไร?**  
A: มันระบุมุมการหมุนรวม (เป็นองศา) ที่นำไปใช้กับโปรไฟล์ตลอดความยาวของ extrusion

**Q: การเพิ่มจำนวน slices จะส่งผลต่อการใช้หน่วยความจำหรือไม่?**  
A: ใช่, slices มากขึ้นจะสร้าง vertices และ faces มากขึ้น ซึ่งใช้หน่วยความจำเพิ่มและอาจทำให้ประสิทธิภาพบนอุปกรณ์ระดับต่ำลดลง

**Q: ฉันสามารถรวม linear extrusion กับฟีเจอร์อื่นของ Aspose.3D ได้หรือไม่?**  
A: ได้เลย คุณสามารถใส่วัสดุ, texture หรือแม้กระทั่งการทำ Boolean หลังการ extrusion เพื่อสร้างโมเดลที่สมบูรณ์ยิ่งขึ้น

**Q: ฉันจะหาแหล่งช่วยเหลือหรือพูดคุยกับนักพัฒนาอื่นได้จากที่ไหน?**  
A: เข้าร่วมชุมชน Aspose.3D ที่ **[Aspose Forum](https://forum.aspose.com/c/3d/18)** เพื่อรับการสนับสนุน, ตัวอย่าง, และการสนทนาต่าง ๆ

---

**อัปเดตล่าสุด:** 2026-03-23  
**ทดสอบด้วย:** Aspose.3D 24.11 for .NET  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}