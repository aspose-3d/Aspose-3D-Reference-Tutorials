---
title: การใช้เอฟเฟกต์เลนส์ Fisheye กับ Aspose.3D สำหรับ .NET
linktitle: การใช้เอฟเฟ็กต์เลนส์ Fisheye กับฉาก 3D
second_title: Aspose.3D .NET API
description: ปรับปรุงฉาก 3 มิติของคุณด้วย Aspose.3D สำหรับ .NET! เรียนรู้วิธีใช้เอฟเฟ็กต์เลนส์ฟิชอายที่น่าหลงใหลทีละขั้นตอน ดาวน์โหลดเดี๋ยวนี้!
weight: 12
url: /th/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การใช้เอฟเฟกต์เลนส์ Fisheye กับ Aspose.3D สำหรับ .NET

## การแนะนำ
คุณกำลังมองหาวิธีเพิ่มความดึงดูดใจให้กับฉาก 3D ของคุณหรือไม่? ดำดิ่งสู่โลกอันน่าทึ่งของเอฟเฟกต์เลนส์ฟิชอายด้วย Aspose.3D สำหรับ .NET บทช่วยสอนนี้จะแนะนำคุณทีละขั้นตอนเกี่ยวกับวิธีการใช้เอฟเฟ็กต์เลนส์ฟิชอายกับฉาก 3 มิติของคุณ ทำให้ฉากมีมุมมองที่มีเอกลักษณ์และน่าดึงดูด
## ข้อกำหนดเบื้องต้น
ก่อนที่เราจะเริ่มต้น ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
-  Aspose.3D สำหรับ .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D สำหรับ .NET แล้ว ถ้าไม่คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).
-  ตัวอย่างฉาก 3 มิติ: เราจะทำงานกับไฟล์ฉาก 3 มิติตัวอย่าง (VirtualCity.glb) คุณสามารถใช้ฉากของคุณเองหรือดาวน์โหลดตัวอย่างได้จาก[เอกสาร Aspose.3D](https://reference.aspose.com/3d/net/).
## นำเข้าเนมสเปซ
ในโปรเจ็กต์ .NET ของคุณ ให้รวมเนมสเปซที่จำเป็นเพื่อเข้าถึงฟังก์ชัน Aspose.3D เพิ่มเนมสเปซต่อไปนี้ที่จุดเริ่มต้นของโค้ดของคุณ:
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
โหลดไฟล์ฉาก 3 มิติในโครงการของคุณโดยใช้รหัสต่อไปนี้:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## ขั้นตอนที่ 2: ตั้งค่ากล้องและไฟ
สร้างกล้องและไฟเพื่อเพิ่มทัศนวิสัยในฉากของคุณ ปรับพารามิเตอร์เช่น NearPlane, FarPlane และ RotationMode ตามต้องการ:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## ขั้นตอนที่ 3: สร้าง Renderer และ Render Target
ตั้งค่าตัวเรนเดอร์และสร้างเป้าหมายการเรนเดอร์สำหรับคิวบ์แมปและพื้นผิว 2 มิติ:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## ขั้นตอนที่ 4: ใช้เอฟเฟ็กต์เลนส์ Fisheye
ดำเนินการหลังการประมวลผลเอฟเฟกต์เลนส์ฟิชอายบนแผนที่คิวบ์ที่เรนเดอร์แล้ว:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## บทสรุป
ยินดีด้วย! คุณใช้เอฟเฟกต์เลนส์ฟิชอายกับฉาก 3 มิติของคุณได้สำเร็จโดยใช้ Aspose.3D สำหรับ .NET ทดลองใช้ฉากและพารามิเตอร์ต่างๆ เพื่อปลดปล่อยความคิดสร้างสรรค์ของคุณ
## คำถามที่พบบ่อย
### ฉันสามารถใช้เอฟเฟ็กต์ฟิชอายกับฉาก 3D ใดๆ ได้หรือไม่
ได้ คุณสามารถใช้เอฟเฟ็กต์ฟิชอายกับฉาก 3D ใดก็ได้ ตรวจสอบให้แน่ใจว่าฉากได้รับการโหลดอย่างเหมาะสมและมีแสงสว่างเพื่อผลลัพธ์ที่ดีที่สุด
### การปรับขอบเขตการมองเห็น (fov) เป็น 360 องศามีความสำคัญอย่างไร?
มุมมอง 360 องศาช่วยให้สามารถฉายภาพเป็นทรงกลมได้อย่างสมบูรณ์ สร้างเอฟเฟกต์ฟิชอายอันน่าทึ่ง
### ฉันจะปรับแต่งแสงในฉาก 3D ของฉันได้อย่างไร
คุณสามารถปรับคุณสมบัติของไฟ เช่น ตำแหน่ง ประเภท และสี เพื่อให้ได้เอฟเฟ็กต์แสงที่ต้องการ
### มีการจำกัดขนาดของฉาก 3D ที่สามารถประมวลผลได้หรือไม่?
ขนาดของฉาก 3D ถูกจำกัดโดยทรัพยากรระบบเป็นหลัก ตรวจสอบให้แน่ใจว่าฮาร์ดแวร์ของคุณสามารถรองรับขนาดของฉากของคุณได้
### ฉันสามารถใช้รูปแบบเอาต์พุตอื่นแทน PNG สำหรับผลลัพธ์เอฟเฟกต์ฟิชอายได้หรือไม่
ได้ คุณสามารถแก้ไขโค้ดเพื่อบันทึกเอาต์พุตในรูปแบบรูปภาพต่างๆ ได้ตามความต้องการของคุณ
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
