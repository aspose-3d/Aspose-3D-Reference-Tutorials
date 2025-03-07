---
title: การใช้เอฟเฟ็กต์ภาพในวิวพอร์ต 3 มิติ
linktitle: การใช้เอฟเฟ็กต์ภาพในวิวพอร์ต 3 มิติ
second_title: Aspose.3D .NET API
description: สำรวจโลกแห่งการแสดงภาพ 3 มิติด้วย Aspose.3D สำหรับ .NET เรียนรู้การใช้เอฟเฟ็กต์ภาพที่น่าดึงดูดกับฉากของคุณโดยใช้บทช่วยสอนทีละขั้นตอน ยกระดับโปรเจ็กต์ของคุณด้วยเอฟเฟกต์พิกเซล ระดับสีเทา การตรวจจับขอบ และเอฟเฟกต์เบลอ
weight: 10
url: /th/net/rendering/apply-visual-effects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การใช้เอฟเฟ็กต์ภาพในวิวพอร์ต 3 มิติ

## การแนะนำ

การเพิ่มความดึงดูดใจให้กับฉาก 3D ถือเป็นส่วนสำคัญในการสร้างประสบการณ์ที่ดื่มด่ำ Aspose.3D สำหรับ .NET มีชุดเครื่องมืออันทรงพลังเพื่อใช้เอฟเฟ็กต์ภาพกับวิวพอร์ต 3D ในบทช่วยสอนนี้ เราจะอธิบายขั้นตอนการใช้เอฟเฟกต์ต่างๆ กับฉาก 3 มิติ รวมถึงการสร้างพิกเซล ระดับสีเทา การตรวจจับขอบ และการเบลอ

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีสิ่งต่อไปนี้:

- ความรู้ด้านการทำงานของการพัฒนา C# และ .NET
-  ติดตั้ง Aspose.3D สำหรับไลบรารี .NET แล้ว คุณสามารถดาวน์โหลดได้จาก[ที่นี่](https://releases.aspose.com/3d/net/).
- ไฟล์ฉาก 3 มิติ (เช่น "scene.obj") สำหรับการทดลอง

## นำเข้าเนมสเปซ

ในการเริ่มต้น ให้นำเข้าเนมสเปซที่จำเป็นสำหรับ Aspose.3D และการอ้างอิงอื่นๆ เพิ่มบรรทัดต่อไปนี้ลงในโค้ดของคุณ:

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 โหลดฉาก 3 มิติของคุณโดยใช้ไฟล์`Scene` ระดับ.

## ขั้นตอนที่ 2: สร้างกล้อง

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

สร้างอินสแตนซ์ของกล้องและกำหนดตำแหน่งและเป้าหมาย

## ขั้นตอนที่ 3: เพิ่มแสงสว่างให้กับฉาก

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

แนะนำการจัดแสงเพื่อเพิ่มเอฟเฟ็กต์ภาพ

## ขั้นตอนที่ 4: สร้าง Renderer และ Render Target

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // กำหนดการตั้งค่าตัวแสดงผล
    renderer.EnableShadows = false;

    // สร้างเป้าหมายการแสดงผล
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // กำหนดค่าวิวพอร์ต
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // เรนเดอร์ฉากให้เป็นพื้นผิว
        renderer.Render(rt);

        // บันทึกพื้นผิวที่แสดงผลลงในไฟล์
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // ดำเนินการต่อด้วยเอฟเฟกต์หลังการประมวลผล...
    }
}
```

สร้างตัวเรนเดอร์และเป้าหมายการเรนเดอร์เพื่อจับภาพฉาก

## ขั้นตอนที่ 5: ใช้เอฟเฟกต์หลังการประมวลผล

### ขั้นตอนที่ 5.1 เอฟเฟกต์พิกเซล

```csharp
// สร้างเอฟเฟกต์พิกเซล
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

ใช้เอฟเฟกต์พิกเซลและบันทึกผลลัพธ์

### ขั้นตอนที่ 5.2 เอฟเฟกต์ระดับสีเทา

```csharp
// สร้างเอฟเฟกต์ระดับสีเทา
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

ใช้เอฟเฟกต์ระดับสีเทาและบันทึกผลลัพธ์

### ขั้นตอนที่ 5.3 รวมเอฟเฟกต์

```csharp
// รวมเอฟเฟกต์ระดับสีเทาและพิกเซล
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

รวมเอฟเฟ็กต์หลายรายการเข้าด้วยกันเพื่อให้ได้ผลลัพธ์ที่ไม่ซ้ำใคร

### ขั้นตอนที่ 5.4 ผลการตรวจจับขอบ

```csharp
// สร้างเอฟเฟกต์การตรวจจับขอบ
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

ใช้เอฟเฟกต์การตรวจจับขอบและบันทึกผลลัพธ์

### ขั้นตอนที่ 5.5 เอฟเฟกต์เบลอ

```csharp
// สร้างเอฟเฟกต์เบลอ
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

ใช้เอฟเฟกต์เบลอและบันทึกผลลัพธ์

## บทสรุป

การทดลองใช้เอฟเฟ็กต์ภาพในวิวพอร์ต 3 มิติจะช่วยเพิ่มความลึกและความคิดสร้างสรรค์ให้กับฉากของคุณ Aspose.3D สำหรับ .NET ช่วยให้กระบวนการนี้ง่ายขึ้น โดยนำเสนอเอฟเฟกต์หลังการประมวลผลที่หลากหลายเพื่อยกระดับโครงการของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้เอฟเฟ็กต์หลายรายการพร้อมกันได้หรือไม่

ตอบ 1: ได้ คุณสามารถรวมเอฟเฟกต์หลังการประมวลผลที่แตกต่างกันเพื่อให้ได้ผลลัพธ์ที่ซับซ้อนและมีเอกลักษณ์เฉพาะตัวได้

### คำถามที่ 2: ฉันจะปรับความเข้มของเอฟเฟ็กต์ภาพได้อย่างไร

A2: แต่ละเอฟเฟ็กต์อาจมีพารามิเตอร์ที่คุณสามารถปรับแต่งเพื่อควบคุมความเข้มของเอฟเฟกต์ได้ โปรดดูเอกสารประกอบสำหรับรายละเอียดเฉพาะ

### คำถามที่ 3: Aspose.3D เหมาะสำหรับการพัฒนาเกมหรือไม่

คำชี้แจง 3: แม้ว่า Aspose.3D จะได้รับการออกแบบมาเพื่อการสร้างแบบจำลอง 3 มิติและการเรนเดอร์เป็นหลัก แต่ก็สามารถนำมาใช้ในบางแง่มุมของการพัฒนาเกมได้

### คำถามที่ 4: มีเอฟเฟกต์หลังการประมวลผลเพิ่มเติมหรือไม่

A4: Aspose.3D มีเอฟเฟกต์หลังการประมวลผลในตัวที่หลากหลาย และคุณสามารถสร้างเอฟเฟกต์แบบกำหนดเองได้โดยใช้ไลบรารี

### คำถามที่ 5: ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่

 A5: ได้ คุณสามารถใช้ Aspose.3D เพื่อวัตถุประสงค์ทางการค้าได้ อ้างถึง[หน้าซื้อ](https://purchase.aspose.com/buy) สำหรับรายละเอียดใบอนุญาต
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
