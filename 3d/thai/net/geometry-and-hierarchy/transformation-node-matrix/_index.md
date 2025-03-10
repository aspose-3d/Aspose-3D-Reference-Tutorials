---
title: การแปลงโหนดโดยเมทริกซ์การแปลง
linktitle: การแปลงโหนดโดยเมทริกซ์การแปลง
second_title: Aspose.3D .NET API
description: แปลงโหนดอย่างง่ายดายในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET เรียนรู้การแปลงโหนดทีละขั้นตอนด้วยบทช่วยสอน
weight: 21
url: /th/net/geometry-and-hierarchy/transformation-node-matrix/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การแปลงโหนดโดยเมทริกซ์การแปลง

## การแนะนำ

ในขอบเขตไดนามิกของกราฟิก 3 มิติและการแสดงภาพ ความสามารถในการจัดการวัตถุภายในฉากถือเป็นสิ่งสำคัญ Aspose.3D สำหรับ .NET ช่วยให้นักพัฒนาสามารถแปลงโหนดได้อย่างราบรื่นโดยใช้เมทริกซ์การแปลง เพิ่มเลเยอร์ของความคิดสร้างสรรค์และการควบคุมฉาก 3 มิติ บทช่วยสอนนี้จะแนะนำคุณตลอดกระบวนการเปลี่ยนโหนดในฉาก 3 มิติทีละขั้นตอน

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

1.  Aspose.3D สำหรับไลบรารี .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D ในโปรเจ็กต์ .NET ของคุณ คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).

2. สภาพแวดล้อมการพัฒนา: ตั้งค่าสภาพแวดล้อมการพัฒนา .NET ที่ใช้งานได้ และหากคุณยังไม่ได้สร้าง ให้สร้างโปรเจ็กต์ใหม่ที่คุณจะนำการเปลี่ยนแปลงไปใช้

## นำเข้าเนมสเปซ

เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็นไปยังโปรเจ็กต์ .NET ของคุณ เนมสเปซเหล่านี้จัดเตรียมคลาสและวิธีการที่จำเป็นสำหรับการจัดการฉาก 3 มิติ

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

ตอนนี้เราได้พูดถึงข้อมูลพื้นฐานแล้ว เรามาแจกแจงกระบวนการเปลี่ยนแปลงเป็นคำแนะนำทีละขั้นตอนกัน

## ขั้นตอนที่ 1: เริ่มต้นฉาก

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// เริ่มต้นวัตถุฉาก
Scene scene = new Scene();

```

ในขั้นตอนนี้ เราจะสร้างฉาก 3D เปล่าใหม่

## ขั้นตอนที่ 2: สร้าง Mesh และแนบไปกับฉาก

```csharp
// เรียกคลาส Common สร้าง mesh โดยใช้วิธีสร้างรูปหลายเหลี่ยมเพื่อตั้งค่าอินสแตนซ์ mesh
Mesh mesh = (new Box()).ToMesh();

// สร้างโหนดคอนเทนเนอร์สำหรับตาข่าย
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

ที่นี่ เราสร้าง mesh โดยใช้วิธีสร้างรูปหลายเหลี่ยมและกำหนดให้กับโหนด โดยสร้างรูปทรงเรขาคณิตสำหรับคิวบ์ของเรา

## ขั้นตอนที่ 3: ตั้งค่าเมทริกซ์การแปลแบบกำหนดเอง

```csharp
// ตั้งค่าเมทริกซ์การแปลแบบกำหนดเอง
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

กำหนดเมทริกซ์การแปลที่กำหนดเองเพื่อกำหนดการเปลี่ยนแปลงเฉพาะที่ใช้กับโหนด ปรับค่าเมทริกซ์ตามต้องการสำหรับการแปลงที่คุณต้องการ

รวมโหนดคิวบ์ไว้ในฉาก ทำให้เป็นส่วนหนึ่งของสภาพแวดล้อม 3 มิติโดยรวม

## ขั้นตอนที่ 4: บันทึกฉาก

```csharp
// เส้นทางไปยังไดเร็กทอรีเอกสาร
var output = "TransformationToNode.fbx";

// บันทึกฉาก 3 มิติในรูปแบบไฟล์ที่รองรับ
scene.Save(output);
// ตัวอย่าง: เพิ่มTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

ระบุไดเร็กทอรีเอาต์พุตและชื่อไฟล์ จากนั้นบันทึกฉาก 3D ในรูปแบบไฟล์ที่ต้องการ ในตัวอย่างนี้ เรากำลังบันทึกในรูปแบบ FBX7500ASCII

## บทสรุป

ยินดีด้วย! คุณแปลงโหนดได้สำเร็จโดยใช้เมทริกซ์การแปลงในฉาก 3 มิติด้วย Aspose.3D สำหรับ .NET ความสามารถนี้เปิดประตูสู่แอพพลิเคชั่น 3D ที่หลากหลายและน่าดึงดูดสายตา

## คำถามที่พบบ่อย

### คำถามที่ 1: เมทริกซ์การแปลงในกราฟิก 3 มิติคืออะไร

A1: เมทริกซ์การแปลงเป็นการแทนค่าทางคณิตศาสตร์ที่ใช้เพื่อใช้การแปลงต่างๆ (การแปล การหมุน การปรับขนาด) กับวัตถุในพื้นที่ 3 มิติ

### คำถามที่ 2: ฉันสามารถใช้การแปลงหลายรายการกับโหนดเดียวได้หรือไม่

A2: ได้ คุณสามารถรวมการแปลงหลายรายการได้โดยการคูณเมทริกซ์ตามลำดับแล้วนำผลลัพธ์ไปใช้กับโหนด

### คำถามที่ 3: มีรูปแบบไฟล์อื่นที่รองรับสำหรับการบันทึกฉาก 3D หรือไม่?

 A3: Aspose.3D สำหรับ .NET รองรับรูปแบบไฟล์ที่หลากหลาย รวมถึง STL, GLTF, OBJ และอื่นๆ อ้างถึง[เอกสารประกอบ](https://reference.aspose.com/3d/net/) สำหรับรายการที่ครอบคลุม

### คำถามที่ 4: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ .NET ได้อย่างไร

 A4: เยี่ยมชม[หน้าใบอนุญาตชั่วคราว](https://purchase.aspose.com/temporary-license/)บนเว็บไซต์ Aspose เพื่อขอรับใบอนุญาตชั่วคราวเพื่อวัตถุประสงค์ในการประเมิน

### คำถามที่ 5: ฉันจะขอความช่วยเหลือหรือเชื่อมต่อกับชุมชน Aspose.3D ได้ที่ไหน

 A5: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อถามคำถาม แบ่งปันประสบการณ์ และเชื่อมต่อกับนักพัฒนารายอื่นโดยใช้ Aspose.3D
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
