---
title: Twist Offset ในการอัดขึ้นรูปเชิงเส้น
linktitle: Twist Offset ในการอัดขึ้นรูปเชิงเส้น
second_title: Aspose.3D .NET API
description: สำรวจความมหัศจรรย์ของ Aspose.3D สำหรับ .NET ด้วยคำแนะนำทีละขั้นตอนเกี่ยวกับ Twist Offset ใน Linear Extrusion ยกระดับโครงการ 3D ของคุณได้อย่างง่ายดาย
weight: 15
url: /th/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Twist Offset ในการอัดขึ้นรูปเชิงเส้น

## การแนะนำ

ยินดีต้อนรับสู่โลกของ Aspose.3D สำหรับ .NET ไลบรารีอเนกประสงค์ที่ช่วยให้นักพัฒนาสามารถจัดการกับการปรับแต่ง 3D ได้อย่างง่ายดาย ในบทช่วยสอนนี้ เราจะเจาะลึกถึงหนึ่งในคุณสมบัติที่น่าสนใจ นั่นก็คือ "Twist Offset ในการอัดขึ้นรูปเชิงเส้น" หากคุณพร้อมที่จะยกระดับทักษะการเขียนโปรแกรม 3D มาเริ่มกันเลย!

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มต้นการเดินทางที่น่าตื่นเต้นนี้ ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับ .NET Library: ดาวน์โหลดและติดตั้งไลบรารีจาก[หน้าปล่อย](https://releases.aspose.com/3d/net/).

- สภาพแวดล้อมการพัฒนาของคุณ: ตรวจสอบให้แน่ใจว่าสภาพแวดล้อมการพัฒนาของคุณได้รับการตั้งค่าและพร้อมที่จะใช้งาน

## นำเข้าเนมสเปซ

เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็นเพื่อเข้าถึงฟังก์ชันการทำงานที่ Aspose.3D สำหรับ .NET มอบให้ ในโค้ดของคุณ สิ่งนี้อาจมีลักษณะดังนี้:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

ตอนนี้ เรามาแบ่งตัวอย่างออกเป็นขั้นตอนที่สามารถจัดการได้เพื่อฝึกฝน Twist Offset ใน Linear Extrusion:

## ขั้นตอนที่ 1: เริ่มต้นโปรไฟล์ฐาน

เริ่มต้นด้วยการสร้างโปรไฟล์ฐาน ซึ่งแสดงตัวอย่างด้วยรูปทรงสี่เหลี่ยมผืนผ้าที่มีรัศมีการปัดเศษที่ระบุ

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## ขั้นตอนที่ 2: สร้างฉาก

สร้างฉาก 3 มิติเพื่อโฮสต์โหนดและรูปร่างของคุณ

```csharp
Scene scene = new Scene();
```

## ขั้นตอนที่ 3: สร้างโหนด

สร้างโหนดภายในฉากทั้งซ้ายและขวา

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## ขั้นตอนที่ 4: การอัดขึ้นรูปเชิงเส้นบนโหนดด้านซ้าย

ดำเนินการอัดขึ้นรูปเชิงเส้นบนโหนดด้านซ้ายโดยใช้คุณสมบัติการบิดและสไลซ์

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## ขั้นตอนที่ 5: การอัดขึ้นรูปเชิงเส้นบนโหนดด้านขวาพร้อม Twist Offset

บนโหนดด้านขวา ดำเนินการอัดขึ้นรูปเชิงเส้นโดยใช้คุณสมบัติการบิด การบิดการบิด และการแบ่งส่วน

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## ขั้นตอนที่ 6: บันทึกฉาก 3 มิติ

บันทึกฉาก 3D ไปยังไดเร็กทอรีเอาท์พุตที่คุณต้องการ โดยระบุรูปแบบไฟล์เป็น WavefrontOBJ

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

ยินดีด้วย! คุณใช้งาน Twist Offset ใน Linear Extrusion โดยใช้ Aspose.3D สำหรับ .NET สำเร็จแล้ว

## บทสรุป

ในบทช่วยสอนนี้ เราได้สำรวจความสามารถอันทรงพลังของ Aspose.3D สำหรับ .NET โดยเน้นไปที่ Twist Offset ใน Linear Extrusion โดยเฉพาะ ด้วยทักษะที่เพิ่งค้นพบเหล่านี้ คุณจะมีความพร้อมที่จะใส่ไดนามิกลงในโปรเจ็กต์ 3 มิติของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับภาษาการเขียนโปรแกรมอื่นๆ ได้หรือไม่

ตอบ 1: Aspose.3D รองรับภาษา .NET เป็นหลัก แต่ Aspose มีไลบรารีที่คล้ายกันสำหรับ Java และแพลตฟอร์มอื่นๆ

### คำถามที่ 2: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ .NET ได้อย่างไร

 A2: เยี่ยมเลย[ลิงค์นี้](https://purchase.aspose.com/temporary-license/)เพื่อรับใบอนุญาตชั่วคราวเพื่อการทดสอบ

### คำถามที่ 3: มีฟอรัมชุมชนสำหรับ Aspose.3D สำหรับ .NET หรือไม่

 A3: แน่นอน! เข้าร่วมชุมชนได้ที่[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อมีส่วนร่วมกับเพื่อนนักพัฒนาและขอความช่วยเหลือ

### คำถามที่ 4: มีตัวอย่างและเอกสารประกอบเพิ่มเติมหรือไม่

 A4: สำรวจ[เอกสารประกอบ](https://reference.aspose.com/3d/net/) สำหรับคำแนะนำและตัวอย่างที่ครอบคลุม

### คำถามที่ 5: ฉันจะซื้อ Aspose.3D สำหรับ .NET ได้ที่ไหน

 A5: มุ่งหน้าสู่[ลิงค์นี้](https://purchase.aspose.com/buy) เพื่อซื้อและปลดล็อคศักยภาพเต็มรูปแบบของ Aspose.3D
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
