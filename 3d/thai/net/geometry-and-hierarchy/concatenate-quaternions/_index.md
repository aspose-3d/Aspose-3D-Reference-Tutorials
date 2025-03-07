---
title: การต่อควอเทอร์เนียนเข้าด้วยกัน
linktitle: การต่อควอเทอร์เนียนเข้าด้วยกัน
second_title: Aspose.3D .NET API
description: สำรวจพลังของการจัดการควอเทอร์เนียนในฉาก 3 มิติด้วย Aspose.3D สำหรับ .NET เรียนรู้การต่อควอเทอร์เนียนทีละขั้นตอนเพื่อการเปลี่ยนแปลงที่สมจริง
weight: 11
url: /th/net/geometry-and-hierarchy/concatenate-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การต่อควอเทอร์เนียนเข้าด้วยกัน

## การแนะนำ

ยินดีต้อนรับสู่บทช่วยสอนที่ครอบคลุมเกี่ยวกับการต่อควอเทอร์เนียนในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET! หากคุณเป็นนักพัฒนาหรือผู้ชื่นชอบสามมิติที่ต้องการพัฒนาทักษะในการจัดการควอเทอร์เนียน แสดงว่าคุณมาถูกที่แล้ว บทช่วยสอนนี้จะแนะนำคุณตลอดกระบวนการทีละขั้นตอน เพื่อให้มั่นใจว่าจะได้รับประสบการณ์การเรียนรู้ที่ราบรื่น

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับ .NET Library: ดาวน์โหลดและติดตั้งไลบรารีจาก[เว็บไซต์กำหนด](https://releases.aspose.com/3d/net/).
- สภาพแวดล้อมการพัฒนา: ตรวจสอบให้แน่ใจว่าคุณมีสภาพแวดล้อมการพัฒนาที่ใช้งานได้สำหรับ .NET

## นำเข้าเนมสเปซ

ในโปรเจ็กต์ .NET ของคุณ ให้รวมเนมสเปซที่จำเป็นเพื่อใช้ประโยชน์จากพลังของ Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
```

## ขั้นตอนที่ 1: สร้างฉาก

เริ่มต้นด้วยการสร้างฉาก 3 มิติโดยใช้ไลบรารี Aspose.3D ฉากนี้จะทำหน้าที่เป็นผืนผ้าใบสำหรับการจัดการควอเทอร์เนียน

```csharp
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: กำหนดควอเทอร์เนียน

 กำหนดสามควอเทอร์เนียน`q1`, `q2` , และ`q3`แต่ละอันแสดงถึงการหมุนเฉพาะ

```csharp
Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
Quaternion q3 = q1.Concat(q2);
```

## ขั้นตอนที่ 3: สร้างกระบอกสูบ

สร้างกระบอกสูบสามกระบอก แต่ละกระบอกแทนควอเทอร์เนียน ตั้งค่าคุณสมบัติการหมุนและการแปลตามควอเทอร์เนียนที่กำหนด

```csharp
Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.Transform.Rotation = q1;
cylinder.Transform.Translation = new Vector3(-5, 2, 0);

// ทำซ้ำสำหรับไตรมาสที่ 2 และไตรมาสที่ 3
```

## ขั้นตอนที่ 4: บันทึกเป็นไฟล์

บันทึกฉากลงในไฟล์ โดยระบุรูปแบบเอาต์พุตและชื่อไฟล์

```csharp
var output = "Your Output Directory" + "test_out.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

## ขั้นตอนที่ 5: แสดงข้อความแสดงความสำเร็จ

พิมพ์ข้อความแจ้งความสำเร็จพร้อมกับพาธของไฟล์เมื่อควอเทอร์เนียนถูกต่อเข้าด้วยกันและบันทึกไฟล์แล้ว

```csharp
Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);
```

## บทสรุป

ยินดีด้วย! คุณได้เรียนรู้วิธีการต่อควอเทอร์เนียนในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET เรียบร้อยแล้ว ทดลองใช้ชุดค่าผสมควอเทอร์เนียนต่างๆ เพื่อให้ได้การเปลี่ยนแปลงที่ไม่ซ้ำใครในโปรเจ็กต์ของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ควอเทอร์เนียนในกราฟิก 3 มิติคืออะไร

คำตอบ 1: ควอเทอร์เนียนเป็นเอนทิตีทางคณิตศาสตร์ที่ใช้แทนการหมุนในพื้นที่ 3 มิติ ซึ่งให้ข้อได้เปรียบเหนือการแสดงการหมุนอื่นๆ

### คำถามที่ 2: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับไลบรารี .NET อื่นๆ ได้หรือไม่

ตอบ 2: ใช่ Aspose.3D สำหรับ .NET ได้รับการออกแบบมาให้ทำงานได้อย่างราบรื่นกับไลบรารี .NET อื่นๆ

### คำถามที่ 3: Aspose.3D สำหรับ .NET มีรุ่นทดลองใช้ฟรีหรือไม่

A3: ได้ คุณสามารถทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D สำหรับ .NET ได้อย่างไร

 A4: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายของชุมชน

### คำถามที่ 5: ฉันสามารถใช้ใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ .NET ได้หรือไม่

 A5: ได้ คุณสามารถขอรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
