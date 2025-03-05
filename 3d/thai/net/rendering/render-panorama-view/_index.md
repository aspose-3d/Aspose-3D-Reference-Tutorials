---
title: เรนเดอร์ภาพพาโนรามา 3 มิติได้อย่างง่ายดายด้วย Aspose.3D สำหรับ .NET
linktitle: การแสดงภาพพาโนรามาของฉาก 3 มิติ
second_title: Aspose.3D .NET API
description: เรียนรู้วิธีสร้างมุมมองพาโนรามา 3 มิติที่น่าทึ่งโดยใช้ Aspose.3D สำหรับ .NET ปฏิบัติตามคำแนะนำทีละขั้นตอนของเราสำหรับการเรนเดอร์ฉากที่สมจริง
type: docs
weight: 13
url: /th/net/rendering/render-panorama-view/
---
## การแนะนำ
การสร้างฉาก 3 มิติที่น่าดึงดูดใจและการเรนเดอร์ให้เป็นมุมมองแบบพาโนรามาได้กลายเป็นส่วนสำคัญของแอปพลิเคชันสมัยใหม่ Aspose.3D สำหรับ .NET มอบโซลูชันที่มีประสิทธิภาพสำหรับนักพัฒนาที่ต้องการรวมความสามารถในการเรนเดอร์ 3D เข้ากับโปรเจ็กต์ของตนได้อย่างราบรื่น ในบทช่วยสอนนี้ เราจะสำรวจกระบวนการเรนเดอร์มุมมองพาโนรามาของฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET
## ข้อกำหนดเบื้องต้น
ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
-  Aspose.3D สำหรับ .NET: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D คุณสามารถค้นหาห้องสมุดและเอกสารประกอบ[ที่นี่](https://releases.aspose.com/3d/net/).
- สภาพแวดล้อมการพัฒนา .NET: ตรวจสอบให้แน่ใจว่าคุณได้ตั้งค่าสภาพแวดล้อมการพัฒนา .NET ที่ใช้งานได้บนเครื่องของคุณ
- ตัวอย่างฉาก 3 มิติ: ดาวน์โหลดไฟล์ตัวอย่างฉาก 3 มิติ เช่น "VirtualCity.glb" ซึ่งเราจะใช้ในการเรนเดอร์มุมมองพาโนรามา
## นำเข้าเนมสเปซ
ในโปรเจ็กต์ .NET ของคุณ ให้นำเข้าเนมสเปซที่จำเป็นสำหรับการทำงานกับ Aspose.3D:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## ขั้นตอนที่ 1: โหลดฉาก 3 มิติ
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
โหลดฉาก 3 มิติโดยใช้ Aspose.3D แทนที่ "VirtualCity.glb" ด้วยเส้นทางไปยังไฟล์ฉาก 3 มิติที่คุณต้องการ
## ขั้นตอนที่ 2: ตั้งค่ากล้องและไฟ
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
ตั้งค่ากล้องและไฟเพื่อจับภาพฉาก 3 มิติอย่างเหมาะสม
## ขั้นตอนที่ 3: สร้าง Renderer และ Render Target
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024 * 3, 1024);
```
สร้างตัวเรนเดอร์และกำหนดเป้าหมายการเรนเดอร์สำหรับแผนที่คิวบ์และภาพพาโนรามาสุดท้าย
## ขั้นตอนที่ 4: กำหนดค่าวิวพอร์ตและเรนเดอร์
```csharp
rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
renderer.Render(rt);
```
กำหนดค่าวิวพอร์ตโดยใช้กล้องและเรนเดอร์แผนที่คิวบ์
## ขั้นตอนที่ 5: ใช้การประมวลผลภายหลังสำหรับมุมมองพาโนรามา
```csharp
PostProcessing equirectangular = renderer.GetPostProcessing("equirectangular");
equirectangular.Input = rt.Targets[0];
renderer.Execute(equirectangular, final);
```
ใช้การฉายภาพแบบ equirectangle หลังการประมวลผลเพื่อสร้างมุมมองแบบพาโนรามา
## ขั้นตอนที่ 6: บันทึกภาพพาโนรามาที่แสดงผล
```csharp
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "panorama.png", ImageFormat.Png);
```
บันทึกภาพพาโนรามาที่แสดงผลไปยังไดเร็กทอรีเอาต์พุตที่ระบุ
## บทสรุป
ด้วย Aspose.3D สำหรับ .NET การแสดงภาพพาโนรามาของฉาก 3D จะกลายเป็นกระบวนการที่ไม่ซับซ้อน ปรับปรุงแอปพลิเคชันของคุณโดยผสมผสานการแสดงภาพ 3 มิติที่สมจริงอย่างลงตัว
## คำถามที่พบบ่อย
### ถาม: ฉันสามารถใช้ฉาก 3D แบบกำหนดเองเพื่อเรนเดอร์ภาพพาโนรามาได้หรือไม่
ใช่ เพียงแทนที่เส้นทางไฟล์ฉากตัวอย่างด้วยเส้นทางไปยังฉาก 3D ที่คุณกำหนดเอง
### ถาม: มีเอฟเฟกต์หลังการประมวลผลเพิ่มเติมหรือไม่
Aspose.3D สำหรับ .NET ให้เอฟเฟกต์หลังการประมวลผลที่หลากหลายเพื่อปรับปรุงภาพที่เรนเดอร์ของคุณ
### ถาม: ฉันจะเพิ่มประสิทธิภาพการเรนเดอร์ได้อย่างไร
ปรับพารามิเตอร์การแสดงผลและขนาดเป้าหมายตามความต้องการของแอปพลิเคชันของคุณ
### ถาม: ฉันสามารถรวมบทช่วยสอนนี้เข้ากับเว็บแอปพลิเคชันได้หรือไม่
ใช่ โดยการรวม Aspose.3D สำหรับ .NET เข้ากับโปรเจ็กต์เว็บ .NET ของคุณ
### ถาม: มีฟอรัมชุมชนสำหรับการสนับสนุน Aspose.3D หรือไม่
 ใช่แล้ว แวะมาที่.[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อสนับสนุนชุมชน