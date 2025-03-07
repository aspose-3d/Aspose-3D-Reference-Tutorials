---
title: การแสดงภาพโมเดล 3 มิติจากกล้อง
linktitle: การแสดงภาพโมเดล 3 มิติจากกล้อง
second_title: Aspose.3D .NET API
description: สำรวจโลกแห่งการเรนเดอร์ 3 มิติด้วย Aspose.3D สำหรับ .NET เรียนรู้วิธีสร้างการแสดงภาพที่น่าดึงดูดใจได้อย่างง่ายดายโดยใช้คำแนะนำทีละขั้นตอนของเรา
weight: 11
url: /th/net/rendering/render-3d-model-image/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การแสดงภาพโมเดล 3 มิติจากกล้อง

## การแนะนำ
การสร้างการแสดงภาพ 3 มิติที่น่าทึ่งถือเป็นส่วนที่น่าตื่นเต้นของการพัฒนาซอฟต์แวร์ และด้วย Aspose.3D สำหรับ .NET คุณสามารถทำให้โมเดล 3 มิติของคุณมีชีวิตขึ้นมาได้ ในบทช่วยสอนนี้ เราจะแนะนำคุณเกี่ยวกับการแสดงภาพโมเดล 3 มิติจากกล้องโดยใช้ Aspose.3D โดยให้คำแนะนำทีละขั้นตอนและข้อมูลเชิงลึกอันมีค่า
## ข้อกำหนดเบื้องต้น
ก่อนที่เราจะเจาะลึกกระบวนการเรนเดอร์ ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
-  Aspose.3D สำหรับ .NET Library: ดาวน์โหลดและติดตั้งไลบรารีจาก[ลิ้งค์ดาวน์โหลด](https://releases.aspose.com/3d/net/).
- โมเดล 3 มิติ: เตรียมไฟล์โมเดล 3 มิติ (เช่น Aspose3D.obj) ที่คุณต้องการเรนเดอร์
- สภาพแวดล้อมการพัฒนา .NET: ตรวจสอบให้แน่ใจว่าคุณมีสภาพแวดล้อมการพัฒนา .NET ที่ใช้งานได้พร้อม
## นำเข้าเนมสเปซ
ในโปรเจ็กต์ .NET ของคุณ ให้รวมเนมสเปซที่จำเป็นสำหรับ Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Drawing;
using System.Drawing.Imaging;
```
## ขั้นตอนที่ 1: โหลดฉาก 3 มิติ
```csharp
Scene scene = new Scene();
var path = RunExamples.GetDataFilePath("Aspose3D.obj");
scene.Open(path);
```
## ขั้นตอนที่ 2: สร้างกล้อง
```csharp
Camera cam = new Camera(ProjectionType.Perspective);
cam.NearPlane = 1;
cam.FarPlane = 500;
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(170, 16, 130);
cam.LookAt = new Vector3(28, 0, -30);
```
## ขั้นตอนที่ 3: เพิ่มแสงให้กับฉาก
```csharp
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Point,
    ConstantAttenuation = 0.3,
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(30, 10, 10);
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Directional,
    ConstantAttenuation = 0.3,
    Direction = new Vector3(-0.3, -0.4, 0.3),
    Color = new Vector3(Color.White)
});
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Spot,
    CastShadows = true,
    LookAt = new Vector3(28, 10, -30),
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(40, 10, 50);
```
## ขั้นตอนที่ 4: ระบุตัวเลือกการเรนเดอร์รูปภาพ
```csharp
ImageRenderOptions opt = new ImageRenderOptions();
opt.BackgroundColor = Color.AliceBlue;
opt.AssetDirectories.Add("Your Document Directory" + "textures");
opt.EnableShadows = true;
```
## ขั้นตอนที่ 5: สร้างฉาก
```csharp
scene.Render(cam, "Your Output Directory" + "Render3DModelImageFromCamera.png", new Size(1024, 1024), ImageFormat.Png, opt);
```
## บทสรุป
ยินดีด้วย! คุณเรนเดอร์รูปภาพโมเดล 3 มิติจากกล้องโดยใช้ Aspose.3D สำหรับ .NET สำเร็จแล้ว รู้สึกอิสระที่จะทดลองกับโมเดลต่างๆ มุมกล้อง และการตั้งค่าการจัดแสง เพื่อปรับปรุงการแสดงภาพ 3 มิติของคุณ
## คำถามที่พบบ่อย
### ถาม: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับเครื่องมือสร้างแบบจำลอง 3D อื่นๆ ได้หรือไม่
ตอบ: Aspose.3D รองรับรูปแบบโมเดล 3 มิติที่หลากหลาย ทำให้เข้ากันได้กับเครื่องมือสร้างโมเดลยอดนิยมมากมาย
### ถาม: ฉันจะแก้ไขปัญหาการเรนเดอร์ได้อย่างไร
 ตอบ: ตรวจสอบ Aspose.3D[ฟอรั่ม](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและแนวทางแก้ไขปัญหาการเรนเดอร์ทั่วไป
### ถาม: มีการทดลองใช้ฟรีหรือไม่?
ตอบ: ได้ คุณสามารถสำรวจคุณสมบัติของ Aspose.3D ได้โดยการได้รับ[ทดลองฟรี](https://releases.aspose.com/).
### ถาม: ฉันจะหาเอกสารประกอบที่ครอบคลุมได้จากที่ไหน?
 ตอบ: โปรดดูที่[เอกสารประกอบ](https://reference.aspose.com/3d/net/) สำหรับคำแนะนำเชิงลึกเกี่ยวกับ Aspose.3D สำหรับ .NET
### ถาม: ฉันจะซื้อ Aspose.3D สำหรับ .NET ได้อย่างไร
 ตอบ: เยี่ยมชม[หน้าซื้อ](https://purchase.aspose.com/buy) เพื่อรับใบอนุญาตที่เหมาะสมกับความต้องการของคุณมากที่สุด
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
