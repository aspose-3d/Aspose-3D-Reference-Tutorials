---
title: การแปลงวัสดุที่ไม่ใช่ PBR เป็น PBR
linktitle: การแปลงวัสดุที่ไม่ใช่ PBR เป็น PBR
second_title: Aspose.3D .NET API
description: สำรวจ Aspose.3D สำหรับ .NET - แปลงวัสดุที่ไม่ใช่ PBR เป็น PBR ได้อย่างง่ายดาย บทช่วยสอนที่ครอบคลุมและ API ที่ทรงพลัง
type: docs
weight: 16
url: /th/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## การแนะนำ

ยินดีต้อนรับสู่คำแนะนำทีละขั้นตอนเกี่ยวกับการใช้ Aspose.3D สำหรับ .NET เพื่อแปลงวัสดุที่ไม่ใช่ PBR (การเรนเดอร์ตามสภาพร่างกาย) เป็นวัสดุ PBR Aspose.3D เป็น API อันทรงพลังที่ช่วยให้นักพัฒนาสามารถทำงานกับรูปแบบไฟล์ 3D ในแอปพลิเคชัน .NET ของตนได้อย่างราบรื่น

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นดังต่อไปนี้:

-  Aspose.3D สำหรับ .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D สำหรับ .NET แล้ว คุณสามารถค้นหาลิงค์ดาวน์โหลด[ที่นี่](https://releases.aspose.com/3d/net/).

- ความเข้าใจพื้นฐานของ C#: บทช่วยสอนนี้ถือว่าคุณมีความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม C#

- IDE (Integrated Development Environment): เลือก IDE ที่คุณต้องการสำหรับการพัฒนา .NET เช่น Visual Studio

## นำเข้าเนมสเปซ

ในโค้ด C# ของคุณ ให้เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็น:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## ขั้นตอนที่ 1: เริ่มต้นฉาก 3 มิติใหม่

เริ่มต้นด้วยการสร้างฉาก 3 มิติใหม่โดยใช้โค้ดต่อไปนี้:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// เริ่มต้นฉาก 3D ใหม่
var scene = new Scene();
```

## ขั้นตอนที่ 2: สร้างวัตถุ 3 มิติ

จากนั้น สร้างวัตถุ 3 มิติ เช่น กล่อง:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## ขั้นตอนที่ 3: กำหนดค่าการแปลงวัสดุ

ตั้งค่าตัวเลือกการแปลงวัสดุสำหรับการแปลงที่ไม่ใช่ PBR เป็น PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## ขั้นตอนที่ 4: บันทึกในรูปแบบ GLTF 2.0

บันทึกฉากที่แปลงแล้วในรูปแบบ GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ตัวอย่าง: Non_PBRtoPBRMaterial
```

ทำซ้ำขั้นตอนเหล่านี้ตามที่จำเป็นสำหรับกรณีการใช้งานเฉพาะของคุณ เพื่อให้แน่ใจว่ารายละเอียดแต่ละรายการได้รับการกำหนดค่าอย่างถูกต้อง

## บทสรุป

ยินดีด้วย! คุณได้เรียนรู้วิธีแปลงวัสดุที่ไม่ใช่ PBR เป็น PBR โดยใช้ Aspose.3D สำหรับ .NET เรียบร้อยแล้ว เครื่องมืออันทรงพลังนี้เปิดความเป็นไปได้ไม่รู้จบสำหรับการปรับแต่งกราฟิก 3D ในแอปพลิเคชัน .NET ของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: Aspose.3D เข้ากันได้กับไฟล์ 3D ทุกรูปแบบหรือไม่

ตอบ 1: ใช่ Aspose.3D รองรับรูปแบบไฟล์ 3D ที่หลากหลาย ซึ่งให้ความยืดหยุ่นในโครงการของคุณ

### คำถามที่ 2: ฉันสามารถใช้ Aspose.3D สำหรับการใช้งานเชิงพาณิชย์ได้หรือไม่

 A2: แน่นอน! Aspose.3D เป็นผลิตภัณฑ์เชิงพาณิชย์ และคุณสามารถซื้อได้[ที่นี่](https://purchase.aspose.com/buy).

### คำถามที่ 3: ฉันจำเป็นต้องมีใบอนุญาตชั่วคราวในการทดสอบหรือไม่

 A3: ได้ คุณสามารถขอรับใบอนุญาตชั่วคราวเพื่อการทดสอบได้[ที่นี่](https://purchase.aspose.com/temporary-license/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้ที่ไหน

 A4: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายของชุมชน

### คำถามที่ 5: มีการทดลองใช้ฟรีหรือไม่?

 A5: ได้ คุณสามารถทดลองใช้เวอร์ชันทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).