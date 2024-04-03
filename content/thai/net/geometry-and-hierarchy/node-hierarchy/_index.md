---
title: ทำความเข้าใจลำดับชั้นของโหนดในฉาก 3 มิติ
linktitle: ทำความเข้าใจลำดับชั้นของโหนดในฉาก 3 มิติ
second_title: Aspose.3D .NET API
description: ปลดล็อกพลังของ Aspose.3D สำหรับ .NET! เจาะลึกการจัดการลำดับชั้นของโหนดด้วยคำแนะนำทีละขั้นตอนนี้ สร้างฉาก 3D ที่น่าทึ่งได้อย่างง่ายดาย
type: docs
weight: 16
url: /th/net/geometry-and-hierarchy/node-hierarchy/
---
## การแนะนำ

ยินดีต้อนรับสู่โลกของ Aspose.3D สำหรับ .NET ไลบรารีอันทรงพลังที่ช่วยให้นักพัฒนาสามารถทำงานกับฉากและโมเดล 3 มิติในแอปพลิเคชัน .NET ของตนได้อย่างราบรื่น ในบทช่วยสอนนี้ เราจะเจาะลึกความซับซ้อนของการทำความเข้าใจลำดับชั้นของโหนดในฉาก 3 มิติโดยใช้ Aspose.3D ในตอนท้ายของคู่มือนี้ คุณจะมีความเข้าใจอย่างถ่องแท้ถึงวิธีจัดการโครงสร้างของฉาก 3 มิติผ่านโหนด ซึ่งช่วยให้คุณสร้างประสบการณ์ทางภาพที่น่าทึ่งได้

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มต้นการเดินทาง 3 มิตินี้ ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับไลบรารี .NET: ตรวจสอบให้แน่ใจว่าคุณมีไลบรารี Aspose.3D ที่รวมอยู่ในโปรเจ็กต์ .NET ของคุณ หากคุณยังไม่ได้ดำเนินการนี้ ให้ไปที่[เอกสารประกอบ](https://reference.aspose.com/3d/net/) สำหรับคำแนะนำ

-  ดาวน์โหลดไลบรารี: หากคุณยังไม่ได้ดาวน์โหลดไลบรารี Aspose.3D ให้ดาวน์โหลดเวอร์ชันล่าสุดจาก[ลิ้งค์ดาวน์โหลด](https://releases.aspose.com/3d/net/)และปฏิบัติตามคำแนะนำในการติดตั้งที่ให้ไว้ในเอกสารประกอบ

-  รับใบอนุญาต: เพื่อปลดล็อกศักยภาพสูงสุดของ Aspose.3D คุณต้องมีใบอนุญาตที่ถูกต้อง หากคุณไม่มีคุณสามารถรับมันได้[ที่นี่](https://purchase.aspose.com/buy) หรือเลือกใช้ก[ทดลองฟรี](https://releases.aspose.com/) เพื่อสำรวจความสามารถของตน

-  การสนับสนุนและชุมชน: เข้าร่วมชุมชน Aspose.3D บน[ฟอรั่มการสนับสนุน](https://forum.aspose.com/c/3d/18)เพื่อเชื่อมต่อกับนักพัฒนารายอื่น ขอความช่วยเหลือ และติดตามข่าวสารล่าสุดเกี่ยวกับการพัฒนาล่าสุด

-  ใบอนุญาตชั่วคราว (ไม่บังคับ): หากคุณกำลังสำรวจ Aspose.3D ก่อนตัดสินใจซื้อ ให้พิจารณารับ[ใบอนุญาตชั่วคราว](https://purchase.aspose.com/temporary-license/) เพื่อการเข้าถึงที่ขยายออกไป

ตอนนี้เรามีเครื่องมือพร้อมแล้ว เรามาดำดิ่งสู่โลกที่น่าตื่นเต้นของการจัดการลำดับชั้นโหนด 3D โดยใช้ Aspose.3D กัน

## นำเข้าเนมสเปซ

ในโปรเจ็กต์ .NET ของคุณ ตรวจสอบให้แน่ใจว่าคุณนำเข้าเนมสเปซที่จำเป็นเพื่อใช้ประโยชน์จากฟังก์ชันการทำงานของ Aspose.3D เพิ่มบรรทัดต่อไปนี้ลงในโค้ดของคุณ:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

เนมสเปซเหล่านี้จะทำให้คุณสามารถเข้าถึงคลาสและวิธีการที่จำเป็นในการทำงานกับฉาก 3 มิติได้

## ขั้นตอนที่ 1: เริ่มต้นวัตถุฉาก

```csharp
Scene scene = new Scene();
```

 เริ่มต้นด้วยการสร้างฉาก 3 มิติใหม่โดยใช้`Scene` ระดับ.

## ขั้นตอนที่ 2: สร้างโหนดย่อย

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 สร้างโครงสร้างแบบลำดับชั้นโดยการสร้างความสัมพันธ์ระหว่างแม่ลูกระหว่างโหนด ในตัวอย่างนี้`cube1` และ`cube2` เป็นโหนดย่อยของ`top` โหนด

## ขั้นตอนที่ 3: สร้างและกำหนด Mesh

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

 สร้างตาข่ายโดยใช้วิธีที่เหมาะสม (ที่นี่`CreateMeshUsingPolygonBuilder`) และกำหนดให้กับโหนดย่อย

## ขั้นตอนที่ 4: ตั้งค่าการแปล

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

กำหนดการแปลสำหรับแต่ละโหนดคิวบ์ โดยวางตำแหน่งในพื้นที่ 3 มิติ

## ขั้นตอนที่ 5: ใช้การหมุนกับโหนดหลัก

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

หมุนโหนดหลัก (`top`) และสังเกตว่าการเปลี่ยนแปลงนี้ส่งผลต่อโหนดย่อยทั้งหมดอย่างไร

## ขั้นตอนที่ 6: บันทึกฉาก 3 มิติ

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

ระบุไดเร็กทอรีเอาต์พุตและบันทึกฉาก 3 มิติในรูปแบบไฟล์ที่ต้องการ (ที่นี่ FBX7500ASCII)

## ขั้นตอนที่ 7: แสดงข้อความแสดงความสำเร็จ

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

แจ้งให้ผู้ใช้ทราบเกี่ยวกับการเพิ่มลำดับชั้นของโหนดและตำแหน่งไฟล์ที่บันทึกไว้ได้สำเร็จ

## บทสรุป

ยินดีด้วย! คุณสำรวจโลกที่ซับซ้อนของลำดับชั้นโหนด 3D ใน Aspose.3D สำหรับ .NET ได้สำเร็จ บทช่วยสอนนี้จะทำให้คุณมีความรู้ในการสร้าง จัดการ และบันทึกฉาก 3 มิติได้อย่างง่ายดาย ในขณะที่คุณเดินทางต่อไป สำรวจคุณสมบัติเพิ่มเติมและปลดปล่อยศักยภาพสูงสุดของ Aspose.3D ในโปรเจ็กต์ .NET ของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ .NET โดยไม่มีใบอนุญาตได้หรือไม่

ตอบ 1: แม้ว่าใบอนุญาตจะปลดล็อคคุณสมบัติทั้งหมด คุณสามารถสำรวจ Aspose.3D ด้วยความสามารถที่จำกัดได้โดยใช้รุ่นทดลองใช้ฟรี

### คำถามที่ 2: มีรูปแบบไฟล์อื่นที่รองรับสำหรับการบันทึกฉาก 3D หรือไม่?

A2: ใช่ Aspose.3D รองรับรูปแบบต่างๆ โปรดดูเอกสารประกอบสำหรับรายการที่ครอบคลุม

### คำถามที่ 3: ฉันจะสนับสนุนชุมชน Aspose.3D ได้อย่างไร

A3: เข้าร่วมฟอรัมสนับสนุน แบ่งปันประสบการณ์ของคุณ และมีส่วนร่วมโดยช่วยเหลือผู้อื่นในการตอบคำถามของพวกเขา

### คำถามที่ 4: Aspose.3D เหมาะสำหรับการพัฒนาเกมหรือไม่

A4: แน่นอน! Aspose.3D มีความหลากหลายและสามารถรวมเข้ากับโปรเจ็กต์การพัฒนาเกมได้

### คำถามที่ 5: สิทธิ์การใช้งานชั่วคราวและสิทธิ์การใช้งานแบบเต็มแตกต่างกันอย่างไร

A5: ใบอนุญาตชั่วคราวให้การเข้าถึงระยะสั้นเพื่อวัตถุประสงค์ในการประเมิน ในขณะที่ใบอนุญาตแบบเต็มให้การใช้งานที่ไม่จำกัด