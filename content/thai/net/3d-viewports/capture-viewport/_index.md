---
title: การบันทึกวิวพอร์ตในฉาก 3 มิติ
linktitle: การบันทึกวิวพอร์ตในฉาก 3 มิติ
second_title: Aspose.3D .NET API
description: เรียนรู้วิธีจับภาพวิวพอร์ต 3 มิติที่น่าทึ่งโดยใช้ Aspose.3D สำหรับ .NET คำแนะนำทีละขั้นตอนสำหรับการเรนเดอร์ฉากอย่างยืดหยุ่น
type: docs
weight: 11
url: /th/net/3d-viewports/capture-viewport/
---
## การแนะนำ

ในขอบเขตของกราฟิก 3 มิติและการแสดงภาพ การจับภาพวิวพอร์ตเป็นทักษะสำคัญที่ช่วยเพิ่มความลึกและรายละเอียดของฉากของคุณ Aspose.3D สำหรับ .NET มอบโซลูชันที่มีประสิทธิภาพสำหรับการเรนเดอร์และจัดการฉาก 3 มิติ บทช่วยสอนนี้จะแนะนำคุณตลอดกระบวนการจับภาพวิวพอร์ตในฉาก 3 มิติโดยใช้ Aspose.3D ช่วยให้คุณสร้างการแสดงภาพที่น่าทึ่งได้อย่างง่ายดาย

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับไลบรารี .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้จาก[ที่นี่](https://releases.aspose.com/3d/net/).

## นำเข้าเนมสเปซ

ในการเริ่มต้น ให้นำเข้าเนมสเปซที่จำเป็นลงในโปรเจ็กต์ .NET ของคุณ:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## ขั้นตอนที่ 1: โหลดฉาก 3 มิติที่มีอยู่

เริ่มต้นด้วยการโหลดฉาก 3 มิติที่มีอยู่ในโปรเจ็กต์ของคุณ ข้อมูลโค้ดต่อไปนี้แสดงให้เห็นสิ่งนี้:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## ขั้นตอนที่ 2: สร้างกล้อง

จากนั้น สร้างตัวอย่างกล้องและกำหนดตำแหน่งและเป้าหมาย:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## ขั้นตอนที่ 3: เพิ่มแสงสว่างให้กับฉาก

ปรับปรุงฉากของคุณด้วยการเพิ่มแหล่งกำเนิดแสง ข้อมูลโค้ดด้านล่างแสดงวิธีสร้างไฟส่องเฉพาะจุด:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## ขั้นตอนที่ 4: กำหนดค่า Renderer และ Render Target

ตั้งค่าตัวเรนเดอร์และสร้างเป้าหมายการเรนเดอร์สำหรับการจับภาพฉาก:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (มีต่อในขั้นตอนต่อไป)
    }
}
```

## ขั้นตอนที่ 5: กำหนดวิวพอร์ตและเรนเดอร์

กำหนดวิวพอร์ตและเรนเดอร์ฉากเพื่อสร้างอิมเมจเอาต์พุต:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## ขั้นตอนที่ 6: แก้ไขวิวพอร์ตและเรนเดอร์อีกครั้ง

ปรับเปลี่ยนวิวพอร์ตและเรนเดอร์ฉากอีกครั้ง แสดงให้เห็นถึงความยืดหยุ่นของ Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

ทดลองการกำหนดค่าต่างๆ ต่อไปเพื่อให้ได้เอฟเฟ็กต์ภาพที่ต้องการ

## บทสรุป

ในบทช่วยสอนนี้ เราได้สำรวจกระบวนการจับภาพวิวพอร์ตในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET ด้วยการใช้ประโยชน์จากคุณสมบัติอันทรงพลัง คุณสามารถยกระดับโปรเจ็กต์กราฟิก 3D ของคุณให้สูงขึ้นอีกขั้น โดยมอบประสบการณ์ทางภาพที่น่าดึงดูดใจ

## คำถามที่พบบ่อย

### คำถามที่ 1: Aspose.3D เข้ากันได้กับรูปแบบไฟล์ 3D อื่นๆ หรือไม่

ตอบ 1: ใช่ Aspose.3D รองรับไฟล์ 3D หลากหลายรูปแบบ จึงรับประกันความเข้ากันได้กับเครื่องมือออกแบบที่หลากหลาย

### คำถามที่ 2: ฉันสามารถใช้ Aspose.3D เพื่อการพัฒนาเกมได้หรือไม่

ตอบ 2: แม้ว่า Aspose.3D จะได้รับการออกแบบมาเพื่อกราฟิกและการแสดงภาพเป็นหลัก แต่ฟังก์ชันของ Aspose.3D ก็สามารถเสริมการพัฒนาเกมในบางแง่มุมได้

### คำถามที่ 3: ฉันจะหาตัวอย่างและเอกสารประกอบเพิ่มเติมได้ที่ไหน

 A3: สำรวจอย่างครอบคลุม[เอกสาร Aspose.3D](https://reference.aspose.com/3d/net/) สำหรับตัวอย่างเพิ่มเติมและข้อมูลโดยละเอียด

### คำถามที่ 4: มีการทดลองใช้ฟรีหรือไม่?

 A4: ได้ คุณสามารถทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 5: ฉันจะขอความช่วยเหลือหรือมีส่วนร่วมในชุมชนได้อย่างไร?

 A5: เข้าร่วมชุมชน Aspose.3D บน[ฟอรั่มการสนับสนุน](https://forum.aspose.com/c/3d/18) เพื่อขอความช่วยเหลือและความร่วมมือ