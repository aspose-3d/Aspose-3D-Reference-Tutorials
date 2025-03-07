---
title: กระบอกสูบด้านล่างแบบเฉือนแบบกำหนดเอง
linktitle: กระบอกสูบด้านล่างแบบเฉือนแบบกำหนดเอง
second_title: Aspose.3D .NET API
description: เรียนรู้วิธีสร้างกระบอกสูบก้นเฉือนแบบกำหนดเองโดยใช้ Aspose.3D สำหรับ .NET พร้อมคำแนะนำทีละขั้นตอนโดยละเอียดของเรา ยกระดับทักษะการสร้างแบบจำลอง 3 มิติของคุณวันนี้!
weight: 12
url: /th/net/3d-modeling/working-with-cylinder/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# กระบอกสูบด้านล่างแบบเฉือนแบบกำหนดเอง

## การแนะนำ
ยินดีต้อนรับสู่คำแนะนำที่ครอบคลุมของเราเกี่ยวกับการสร้างกระบอกแบบกำหนดเองโดยใช้ Aspose.3D สำหรับ .NET หากคุณกำลังมองหาที่จะพัฒนาทักษะการสร้างแบบจำลอง 3 มิติและเพิ่มคุณสมบัติพิเศษให้กับโครงการของคุณ คุณมาถูกที่แล้ว ในบทช่วยสอนนี้ เราจะแนะนำคุณตลอดกระบวนการทีละขั้นตอน โดยใช้คำอธิบายและข้อมูลโค้ดที่ชัดเจน
## ข้อกำหนดเบื้องต้น
ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีสิ่งต่อไปนี้:
- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม C# และ .NET
-  ติดตั้ง Aspose.3D สำหรับไลบรารี .NET แล้ว คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).
- สภาพแวดล้อมการพัฒนาที่ตั้งค่าไว้สำหรับการเขียนโปรแกรม .NET
## นำเข้าเนมสเปซ
ในโค้ด C# ของคุณ ให้เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็น:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## ขั้นตอนที่ 1: สร้างฉาก
เริ่มต้นด้วยการสร้างฉาก 3 มิติโดยใช้ Aspose.3D:
```csharp
Scene scene = new Scene();
```
## ขั้นตอนที่ 2: สร้างกระบอก 1
สร้างกระบอกแรกและตั้งค่าคุณสมบัติ:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## ขั้นตอนที่ 3: ปรับแต่งแรงเฉือนด้านล่างสำหรับกระบอกสูบ 1
ใช้แรงเฉือนด้านล่างแบบกำหนดเองกับกระบอกสูบแรก:
```csharp
//แรงเฉือน 47.5 องศาในระนาบ xy (แกน z)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// ตั้งค่า GenerateFanCylinder เป็นจริง
cylinder1.GenerateFanCylinder = true;
// ตั้งค่า ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// ตั้งค่า OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## ขั้นตอนที่ 4: เพิ่มกระบอก 1 ลงในฉาก
เพิ่มกระบอกแรกเข้าไปในฉากและตั้งค่าการแปล:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## ขั้นตอนที่ 5: สร้างกระบอก 2
สร้างกระบอกที่สองที่มีคุณสมบัติคล้ายกัน:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## ขั้นตอนที่ 6: เพิ่มกระบอก 2 ลงในฉาก
เพิ่มกระบอกที่สองลงในฉากโดยไม่มีพารามิเตอร์ที่กำหนดเอง:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## ขั้นตอนที่ 7: บันทึกฉาก
บันทึกฉากเป็นไฟล์ Wavefront OBJ ในไดเรกทอรีเอกสารของคุณ:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## บทสรุป
ยินดีด้วย! คุณได้สร้างกระบอกสูบก้นเฉือนแบบกำหนดเองโดยใช้ Aspose.3D สำหรับ .NET สำเร็จแล้ว บทช่วยสอนนี้มีวัตถุประสงค์เพื่อให้คำแนะนำทีละขั้นตอนสำหรับผู้ใช้ที่มีความเชี่ยวชาญในระดับต่างๆ ในการสร้างแบบจำลอง 3 มิติและการเขียนโปรแกรม
## คำถามที่พบบ่อย
### Aspose.3D สำหรับ .NET เหมาะสำหรับผู้เริ่มต้นหรือไม่
อย่างแน่นอน! Aspose.3D สำหรับ .NET นำเสนออินเทอร์เฟซที่ใช้งานง่าย ทำให้ทั้งผู้เริ่มต้นและนักพัฒนาที่มีประสบการณ์สามารถเข้าถึงได้
### ฉันสามารถใช้มุมตัดที่แตกต่างกันกับกระบอกสูบได้หรือไม่
ใช่ คุณสามารถปรับแต่งแรงเฉือนด้านล่างสำหรับแต่ละกระบอกสูบได้ ทำให้ได้เอฟเฟกต์เฉพาะตัว
### มีรุ่นทดลองใช้งานหรือไม่?
 ใช่ คุณสามารถสำรวจเวอร์ชันทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).
### ฉันจะหาการสนับสนุนเพิ่มเติมได้จากที่ไหน?
 เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายของชุมชน
### ฉันจะขอรับใบอนุญาตชั่วคราวได้อย่างไร
 รับใบอนุญาตชั่วคราวของคุณ[ที่นี่](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
