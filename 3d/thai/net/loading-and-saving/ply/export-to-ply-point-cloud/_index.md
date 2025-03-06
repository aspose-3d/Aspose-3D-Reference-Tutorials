---
title: ส่งออกเป็นรูปแบบ PLY เป็น Point Cloud
linktitle: ส่งออกเป็นรูปแบบ PLY เป็น Point Cloud
second_title: Aspose.3D .NET API
description: สำรวจโลกแห่งการสร้างแบบจำลอง 3 มิติด้วย Aspose.3D สำหรับ .NET เรียนรู้การส่งออกโมเดลเป็นรูปแบบ PLY ได้อย่างง่ายดาย ยกระดับโครงการของคุณด้วยภาพที่น่าทึ่ง
weight: 16
url: /th/net/loading-and-saving/ply/export-to-ply-point-cloud/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ส่งออกเป็นรูปแบบ PLY เป็น Point Cloud

## การแนะนำ
ในโลกแบบไดนามิกของการสร้างแบบจำลอง 3 มิติและการพัฒนา Aspose.3D สำหรับ .NET มีความโดดเด่นในฐานะชุดเครื่องมืออันทรงพลัง บทช่วยสอนนี้จะแนะนำคุณตลอดขั้นตอนการส่งออกโมเดล 3D เป็นรูปแบบ PLY เป็นพอยต์คลาวด์โดยใช้ Aspose.3D สำหรับ .NET หากคุณพร้อมที่จะปรับปรุงโครงการของคุณด้วยภาพที่สวยงาม ให้ปฏิบัติตามและปลดล็อกศักยภาพสูงสุดของไลบรารีอเนกประสงค์นี้
## ข้อกำหนดเบื้องต้น
ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
-  Aspose.3D สำหรับ .NET: ดาวน์โหลดและติดตั้งไลบรารีจาก[หน้าดาวน์โหลด](https://releases.aspose.com/3d/net/).
- สภาพแวดล้อมการพัฒนา: ตั้งค่าสภาพแวดล้อมการพัฒนา .NET ที่คุณต้องการ เช่น Visual Studio
## นำเข้าเนมสเปซ
หากต้องการเริ่มต้นใช้งาน Aspose.3D สำหรับ .NET ให้นำเข้าเนมสเปซที่จำเป็นในโปรเจ็กต์ของคุณ:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## ขั้นตอนที่ 1: สร้างโมเดล 3 มิติ
เริ่มต้นด้วยการสร้างแบบจำลอง 3 มิติที่คุณต้องการส่งออกเป็นพอยต์คลาวด์ ตัวอย่างเช่น เรามาสร้างทรงกลมกัน:
```csharp
Sphere sphere = new Sphere();
```
## ขั้นตอนที่ 2: กำหนดการตั้งค่าการส่งออก
ระบุการตั้งค่าการส่งออก รวมถึงรูปแบบไฟล์ (PLY) และเปิดใช้งานการส่งออกพอยต์คลาวด์:
```csharp
PlySaveOptions saveOptions = new PlySaveOptions() { PointCloud = true };
```
## ขั้นตอนที่ 3: ตั้งค่าเส้นทางการส่งออก
กำหนดไดเร็กทอรีที่คุณต้องการบันทึกไฟล์ PLY ที่ส่งออก:
```csharp
string exportPath = "Your Document Directory" + "sphere.ply";
```
## ขั้นตอนที่ 4: เข้ารหัสและส่งออก
 ใช้`Encode` วิธีการส่งออกโมเดล 3 มิติเป็นรูปแบบ PLY:
```csharp
FileFormat.PLY.Encode(sphere, exportPath, saveOptions);
```
## บทสรุป
ยินดีด้วย! คุณได้ส่งออกโมเดล 3 มิติเป็นรูปแบบ PLY ในรูปแบบพอยต์คลาวด์โดยใช้ Aspose.3D สำหรับ .NET เรียบร้อยแล้ว นี่เป็นการเปิดโอกาสให้เป็นไปได้ไม่รู้จบในการผสานรวมภาพที่สมจริงเข้ากับแอปพลิเคชันของคุณ

## คำถามที่พบบ่อย
### 1. Aspose.3D เข้ากันได้กับเฟรมเวิร์ก .NET ทั้งหมดหรือไม่
Aspose.3D รองรับเฟรมเวิร์ก .NET ที่หลากหลาย ทำให้มั่นใจได้ถึงความเข้ากันได้ในสภาพแวดล้อมการพัฒนาที่หลากหลาย
### 2. ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่
 อย่างแน่นอน! Aspose.3D เสนอตัวเลือกสิทธิ์การใช้งานที่ยืดหยุ่น รวมถึงการใช้งานเชิงพาณิชย์ ตรวจสอบ[หน้าซื้อ](https://purchase.aspose.com/buy) เพื่อดูรายละเอียด
### 3. ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร
 เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อเชื่อมต่อกับชุมชนและรับความช่วยเหลือจากผู้เชี่ยวชาญ
### 4. มีการทดลองใช้ฟรีหรือไม่?
 ใช่ สำรวจคุณสมบัติด้วย[ทดลองฟรี](https://releases.aspose.com/) ก่อนที่จะให้คำมั่นสัญญา
### 5. ฉันจะขอรับใบอนุญาตชั่วคราวได้อย่างไร?
 สำหรับตัวเลือกใบอนุญาตชั่วคราว โปรดไปที่[ลิงค์นี้](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
