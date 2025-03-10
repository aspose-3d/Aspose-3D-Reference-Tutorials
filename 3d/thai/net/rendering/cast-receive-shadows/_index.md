---
title: การควบคุมเงาในการเรนเดอร์ 3 มิติด้วย Aspose.3D สำหรับ .NET
linktitle: การร่ายและรับเงา
second_title: Aspose.3D .NET API
description: สำรวจโลกแห่งการเรนเดอร์ 3 มิติด้วย Aspose.3D สำหรับ .NET โยนและรับเงาได้อย่างง่ายดาย ดาวน์โหลดทดลองใช้ฟรีตอนนี้!
weight: 10
url: /th/net/rendering/cast-receive-shadows/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การควบคุมเงาในการเรนเดอร์ 3 มิติด้วย Aspose.3D สำหรับ .NET

## การแนะนำ
ยินดีต้อนรับสู่โลกแห่งการเรนเดอร์ 3 มิติด้วย Aspose.3D สำหรับ .NET! ในบทช่วยสอนนี้ เราจะเจาะลึกขอบเขตอันน่าทึ่งของการร่ายและรับเงา ซึ่งเป็นส่วนสำคัญในการสร้างฉาก 3 มิติที่สมจริงและน่าทึ่ง ไม่ว่าคุณจะเป็นนักพัฒนาที่มีประสบการณ์หรือเพิ่งเริ่มต้นการเดินทางสู่กราฟิก 3D คู่มือนี้จะช่วยให้คุณมีความรู้และทักษะในการปรับปรุงความสามารถในการเรนเดอร์โดยใช้ Aspose.3D
## ข้อกำหนดเบื้องต้น
ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
-  Aspose.3D สำหรับ .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้จาก[Aspose.3D สำหรับเอกสาร .NET](https://reference.aspose.com/3d/net/).
- สภาพแวดล้อมการพัฒนา .NET: ตั้งค่าสภาพแวดล้อมการพัฒนา .NET ที่ใช้งานได้บนเครื่องของคุณ
- ตัวแก้ไขโค้ด: เลือกตัวแก้ไขโค้ดที่คุณต้องการ แนะนำให้ใช้ Visual Studio เพื่อประสบการณ์ที่ราบรื่น
## นำเข้าเนมสเปซ
ในโปรเจ็กต์ .NET ของคุณ ให้นำเข้าเนมสเปซที่จำเป็นเพื่อใช้ประโยชน์จากฟังก์ชันการทำงานของ Aspose.3D เพิ่มเนมสเปซต่อไปนี้ที่จุดเริ่มต้นของไฟล์โค้ดของคุณ:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System.Drawing;
using System.Drawing.Imaging;
```
ตอนนี้ เราจะแบ่งโค้ดตัวอย่างออกเป็นหลายขั้นตอนเพื่อทำความเข้าใจวิธีการส่งและรับเงาโดยใช้ Aspose.3D สำหรับ .NET
## ขั้นตอนที่ 1: ตั้งค่าฉาก
```csharp
Scene scene = new Scene();
Camera camera = new Camera();
// รหัสการตั้งค่ากล้องเพิ่มเติม...
```
สร้างฉาก 3 มิติและตั้งค่ากล้องเพื่อดูฉาก ปรับพารามิเตอร์ของกล้องเช่น`NearPlane` และ`LookAt` เพื่อการเรนเดอร์ที่เหมาะสมที่สุด
## ขั้นตอนที่ 2: แนะนำแหล่งกำเนิดแสง
```csharp
Light light;
scene.RootNode.CreateChildNode("light", light = new Light()
{
    // การกำหนดค่าแหล่งกำเนิดแสง...
}).Transform.Translation = new Vector3(9.4785, 5, 3.18);
```
เพิ่มแหล่งกำเนิดแสงให้กับฉาก กำหนดค่าพารามิเตอร์ต่างๆ เช่น สี เงา และ Falloff เพื่อให้ได้เอฟเฟกต์แสงที่สมจริง
## ขั้นตอนที่ 3: สร้างวัตถุในฉาก
```csharp
Node plane = scene.RootNode.CreateChildNode("plane", new Plane(20, 20));
// รหัสการตั้งค่าวัตถุเพิ่มเติม (พรู กล่อง)...
```
สร้างวัตถุ เช่น เครื่องบิน พรู และกล่องภายในฉาก ปรับวัสดุและตำแหน่งเพื่อให้ได้เอฟเฟ็กต์ภาพที่ต้องการ
## ขั้นตอนที่ 4: สร้างฉาก
```csharp
scene.Render(camera, "Your Output Directory" + "CastAndReceiveShadow_out.png", new Size(1024, 1024), ImageFormat.Png, opt);
```
เรนเดอร์ฉากที่กำหนดค่าโดยใช้กล้องที่ระบุและบันทึกภาพที่ส่งออกไปยังไดเร็กทอรีที่กำหนด
## บทสรุป
ยินดีด้วย! คุณได้สำรวจพื้นฐานของการแคสต์และรับเงาในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET สำเร็จแล้ว ไลบรารี่อันทรงพลังนี้เปิดโอกาสให้สร้างประสบการณ์ภาพที่น่าตื่นตาตื่นใจและน่าหลงใหลในแอปพลิเคชันของคุณได้อย่างไม่มีที่สิ้นสุด
## คำถามที่พบบ่อย
### ถาม: ฉันสามารถปรับแต่งคุณสมบัติของเงาเพิ่มเติมได้หรือไม่
ตอบ: ได้ Aspose.3D มีตัวเลือกมากมายในการปรับแต่งการตั้งค่าเงา รวมถึงสีเงา ความเข้ม และอื่นๆ
### ถาม: ฉันจะเพิ่มประสิทธิภาพการเรนเดอร์ได้อย่างไร
ตอบ: พิจารณาปรับความซับซ้อนของฉาก ใช้วัสดุที่มีประสิทธิภาพ และปรับแหล่งกำเนิดแสงให้เหมาะสมเพื่อเพิ่มความเร็วในการเรนเดอร์
### ถาม: Aspose.3D รองรับไฟล์ 3D รูปแบบอื่นหรือไม่
ตอบ: ใช่ Aspose.3D รองรับรูปแบบไฟล์ 3D ที่หลากหลาย ทำให้มีความอเนกประสงค์สำหรับความต้องการของโครงการต่างๆ
### ถาม: มีฟอรัมชุมชนสำหรับการสนับสนุน Aspose.3D หรือไม่
 ตอบ: ได้ คุณสามารถหาการสนับสนุนและมีส่วนร่วมกับชุมชนได้ที่[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18).
### ถาม: ฉันสามารถลองใช้ Aspose.3D ก่อนซื้อได้หรือไม่
 ตอบ: แน่นอน! สำรวจห้องสมุดพร้อมทดลองใช้ฟรี[ที่นี่](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
