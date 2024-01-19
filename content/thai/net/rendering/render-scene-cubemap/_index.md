---
title: การเรนเดอร์ฉากลงใน Cubemap ด้วย Six Faces
linktitle: การเรนเดอร์ฉากลงใน Cubemap ด้วย Six Faces
second_title: Aspose.3D .NET API
description: สร้างคิวบ์แมปที่น่าทึ่งด้วย Aspose.3D สำหรับ .NET ปฏิบัติตามคำแนะนำทีละขั้นตอนของเราในการเรนเดอร์ฉาก 3 มิติให้เป็นคิวบ์แมปหกหน้าที่น่าหลงใหล
type: docs
weight: 14
url: /th/net/rendering/render-scene-cubemap/
---
## การแนะนำ
ยินดีต้อนรับสู่คำแนะนำทีละขั้นตอนในการเรนเดอร์ฉากลงในคิวบ์แมปที่มีหกใบหน้าโดยใช้ Aspose.3D สำหรับ .NET ในบทช่วยสอนนี้ เราจะแนะนำคุณตลอดขั้นตอนการสร้างคิวบ์แมปที่น่าทึ่งด้วยการแสดงฉาก 3 มิติ Aspose.3D เป็น .NET API อันทรงพลังที่ทำให้การจัดการกราฟิก 3 มิติง่ายขึ้น และด้วยคำแนะนำนี้ คุณจะควบคุมความสามารถของมันในการสร้างคิวบ์แมปที่น่าดึงดูด
## ข้อกำหนดเบื้องต้น
ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
- ความรู้ด้านการทำงานของการพัฒนา C# และ .NET
-  ติดตั้ง Aspose.3D สำหรับ .NET แล้ว คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).
- ไฟล์ฉาก 3 มิติในรูปแบบ GLB (เช่น "VirtualCity.glb") สำหรับการเรนเดอร์
## นำเข้าเนมสเปซ
เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็นสำหรับ Aspose.3D ในโค้ด C# ของคุณ:
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
## ขั้นตอนที่ 1: โหลดฉาก
โหลดไฟล์ฉาก 3 มิติโดยใช้รหัสต่อไปนี้:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## ขั้นตอนที่ 2: สร้างกล้องและไฟ
สร้างกล้องและไฟสองดวงเพื่อให้แสงสว่างแก่ฉาก:
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
## ขั้นตอนที่ 3: สร้าง Renderer และ Render Target
สร้างตัวเรนเดอร์และเป้าหมายการเรนเดอร์แมปคิวบ์ด้วยพื้นผิวเชิงลึก:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## ขั้นตอนที่ 4: บันทึกใบหน้า Cubemap
บันทึกแต่ละหน้าของ cubemap ลงในดิสก์ด้วยชื่อไฟล์ที่ระบุ:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## บทสรุป
ยินดีด้วย! คุณเรนเดอร์ฉาก 3 มิติลงใน cubemap ได้สำเร็จโดยใช้ Aspose.3D สำหรับ .NET สำรวจตัวเลือกการปรับแต่งเพิ่มเติมและปรับปรุงโปรเจ็กต์กราฟิก 3 มิติของคุณด้วย API อันทรงพลังนี้
## คำถามที่พบบ่อย
### ถาม: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับไฟล์ 3D รูปแบบอื่นได้หรือไม่
ใช่ Aspose.3D รองรับรูปแบบไฟล์ 3D ที่หลากหลาย ซึ่งให้ความยืดหยุ่นในโครงการของคุณ
### ถาม: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร
 เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายของชุมชน
### ถาม: มีการทดลองใช้ฟรีหรือไม่?
 ใช่ คุณสามารถเข้าถึงการทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).
### ถาม: ฉันสามารถเรนเดอร์ฉากต่างๆ ด้วยแอนิเมชั่นโดยใช้ Aspose.3D ได้หรือไม่
อย่างแน่นอน! Aspose.3D รองรับการเรนเดอร์ฉาก 3D แบบเคลื่อนไหว
### ถาม: ฉันจะหาเอกสารโดยละเอียดได้จากที่ไหน?
 อ้างถึง[เอกสาร Aspose.3D](https://reference.aspose.com/3d/net/) เพื่อข้อมูลเชิงลึก