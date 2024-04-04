---
title: การสร้างฉากด้วยพื้นผิวแบบฝัง
linktitle: การสร้างฉากด้วยพื้นผิวแบบฝัง
second_title: Aspose.3D .NET API
description: สร้างฉาก 3 มิติที่น่าตื่นตาตื่นใจด้วยพื้นผิวแบบฝังโดยใช้ Aspose.3D สำหรับ .NET ปฏิบัติตามคำแนะนำทีละขั้นตอนของเราเพื่อผลลัพธ์ที่น่าทึ่ง
type: docs
weight: 10
url: /th/net/materials/create-scene-embedded-texture/
---
## การแนะนำ
ยินดีต้อนรับสู่โลกที่น่าตื่นเต้นของกราฟิก 3 มิติด้วย Aspose.3D สำหรับ .NET! ในบทช่วยสอนที่ครอบคลุมนี้ เราจะแนะนำคุณตลอดกระบวนการสร้างฉาก 3 มิติที่น่าทึ่งด้วยพื้นผิวที่ฝังไว้โดยใช้ Aspose.3D ซึ่งเป็นไลบรารีที่ทรงพลังและอเนกประสงค์สำหรับนักพัฒนา .NET
## ข้อกำหนดเบื้องต้น
ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม C# และ .NET
- ติดตั้ง Visual Studio บนเครื่องของคุณแล้ว
- Aspose.3D สำหรับไลบรารี .NET ซึ่งคุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).
- ความคุ้นเคยกับแนวคิดกราฟิก 3 มิติและการสร้างฉาก
## นำเข้าเนมสเปซ
เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็นลงในโปรเจ็กต์ของคุณ เนมสเปซเหล่านี้จะมอบเครื่องมือและฟังก์ชันที่จำเป็นสำหรับการจัดการกราฟิก 3D
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## ขั้นตอนที่ 1: การสร้างฉาก
เริ่มต้นด้วยการสร้างฉาก 3 มิติใหม่โดยใช้ Aspose.3D สำหรับ .NET สิ่งนี้จะทำหน้าที่เป็นผืนผ้าใบสำหรับผลงานชิ้นเอก 3 มิติของคุณ
```csharp
// สร้างไฟล์ FBX ที่มีพื้นผิวแบบฝัง
Scene scene = new Scene();
```
## ขั้นตอนที่ 2: การสร้างพื้นผิวแบบฝัง
ตอนนี้ มาเพิ่มความโดดเด่นด้านภาพให้กับฉากของคุณด้วยการฝังพื้นผิว เราจะสร้างพื้นผิวด้วยเนื้อหาที่กำหนดเองและกำหนดชื่อไฟล์
```csharp
// สร้างพื้นผิวแบบฝัง
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    //จำเป็นต้องระบุชื่อไฟล์หากใช้พื้นผิวแบบฝัง
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## ขั้นตอนที่ 3: การสร้างวัสดุ
จากนั้น สร้างวัสดุสำหรับวัตถุ 3 มิติของคุณ โดยผสมผสานพื้นผิวที่สร้างขึ้นก่อนหน้านี้และคุณสมบัติแบบกำหนดเอง
```csharp
// สร้างวัสดุที่มีคุณสมบัติแบบกำหนดเอง
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## ขั้นตอนที่ 4: การสร้างวัตถุ 3 มิติ
ตอนนี้ มาทำให้ฉากของคุณมีชีวิตชีวาด้วยการเพิ่มวัตถุ 3 มิติ ในตัวอย่างนี้ เราจะใช้พรูและใช้วัสดุที่คุณเพิ่งสร้างขึ้น
```csharp
// สร้างพรูโดยใช้วัสดุที่สร้างไว้ก่อนหน้านี้
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## ขั้นตอนที่ 5: บันทึกฉาก
สุดท้าย บันทึกผลงานชิ้นเอกของคุณลงในไฟล์ ในตัวอย่างนี้ เราจะบันทึกในรูปแบบ FBX
```csharp
// บันทึกฉากลงในไฟล์
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
ยินดีด้วย! คุณสร้างฉาก 3 มิติด้วยพื้นผิวแบบฝังได้สำเร็จโดยใช้ Aspose.3D สำหรับ .NET
## ซอร์สโค้ด CreateTextureContent
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## บทสรุป
ในบทช่วยสอนนี้ เราได้สำรวจพื้นฐานของการสร้างฉาก 3 มิติที่สวยงามน่าทึ่งด้วยพื้นผิวที่ฝังไว้โดยใช้ Aspose.3D สำหรับ .NET ด้วยความรู้นี้ คุณสามารถปลดปล่อยความคิดสร้างสรรค์และสร้างแอปพลิเคชัน 3D ที่น่าหลงใหลได้

## คำถามที่พบบ่อย

### ถาม: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับภาษาการเขียนโปรแกรมอื่นๆ ได้หรือไม่
ตอบ: Aspose.3D ได้รับการออกแบบมาเพื่อ .NET เป็นหลัก แต่มีไลบรารีที่คล้ายกันสำหรับภาษาอื่น
### ถาม: ฉันจะนำภาพเคลื่อนไหวไปใช้กับฉาก 3D ของฉันได้อย่างไร
ตอบ: Aspose.3D มีความสามารถด้านแอนิเมชั่น โปรดดูเอกสารประกอบสำหรับคำแนะนำโดยละเอียด
### ถาม: Aspose.3D สำหรับ .NET มีเวอร์ชันทดลองใช้งานหรือไม่
 ตอบ: ได้ คุณสามารถดาวน์โหลดเวอร์ชันทดลองได้[ที่นี่](https://releases.aspose.com/).
### ถาม: ฉันจะรับการสนับสนุนและแหล่งข้อมูลเพิ่มเติมได้จากที่ไหน
 ตอบ: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายของชุมชน
### ถาม: ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่
 ตอบ: ได้ คุณสามารถซื้อใบอนุญาตได้[ที่นี่](https://purchase.aspose.com/buy).