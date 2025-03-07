---
title: ตาข่ายสามเหลี่ยม
linktitle: ตาข่ายสามเหลี่ยม
second_title: Aspose.3D .NET API
description: สำรวจพลังของ Aspose.3D สำหรับ .NET ในคำแนะนำทีละขั้นตอนนี้ เรียนรู้วิธีสามเหลี่ยมตาข่าย 3 มิติอย่างง่ายดายเพื่อการสร้างแบบจำลองที่ได้รับการปรับปรุง
weight: 22
url: /th/net/geometry-and-hierarchy/triangulate-mesh/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ตาข่ายสามเหลี่ยม

## การแนะนำ

ยินดีต้อนรับสู่บทช่วยสอนที่ครอบคลุมเกี่ยวกับสามเหลี่ยมตาข่ายในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET Aspose.3D เป็นไลบรารีอันทรงพลังที่ช่วยให้นักพัฒนา .NET สามารถทำงานกับไฟล์ 3D ได้อย่างราบรื่น โดยมีฟังก์ชันการทำงานที่หลากหลายสำหรับการสร้าง จัดการ และแปลงโมเดล 3D

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

- Aspose.3D สำหรับไลบรารี .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).

-  ตัวอย่างโมเดล 3 มิติ: มีโมเดล 3 มิติในรูปแบบ FBX ที่คุณต้องการสร้างรูปสามเหลี่ยม คุณสามารถใช้สิ่งที่จัดให้ได้[เอกสาร.fbx](https://reference.aspose.com/3d/net/) ไฟล์สำหรับฝึกซ้อม.

## นำเข้าเนมสเปซ

เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็นลงในโปรเจ็กต์ของคุณเพื่อเข้าถึงฟังก์ชัน Aspose.3D:

```csharp
using System;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

## ขั้นตอนที่ 1: เริ่มต้นวัตถุฉาก

```csharp
Scene scene = new Scene();
scene.Open(RunExamples.GetDataFilePath("document.fbx"));
```

เริ่มต้นวัตถุฉากใหม่และโหลดโมเดล 3 มิติของคุณ (document.fbx) ลงไป

## ขั้นตอนที่ 2: สามเหลี่ยมตาข่าย

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    Mesh mesh = node.GetEntity<Mesh>();
    if (mesh != null)
    {
        // สามเหลี่ยมตาข่าย
        Mesh newMesh = PolygonModifier.Triangulate(mesh);
        // เปลี่ยนตาข่ายเก่า
        node.Entity = mesh;
    }
    return true;
});
```

 วนซ้ำโหนดในฉาก ระบุเมช และใช้รูปสามเหลี่ยมโดยใช้`PolygonModifier.Triangulate` วิธี.

## ขั้นตอนที่ 3: บันทึกผลลัพธ์

```csharp
var output = "Your Output Directory" + "document.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

ระบุไดเร็กทอรีเอาต์พุตและบันทึกฉากที่แก้ไข เพื่อให้แน่ใจว่าการเปลี่ยนแปลงจะถูกบันทึกในรูปแบบ FBX

## ขั้นตอนที่ 4: แสดงผล

```csharp
Console.WriteLine("\nMesh has been Triangulated.\nFile saved at " + output);
```

พิมพ์ข้อความเพื่อยืนยันการทำสามเหลี่ยมสำเร็จ และระบุเส้นทางในการบันทึกไฟล์ที่แก้ไข

## บทสรุป

ยินดีด้วย! คุณได้เรียนรู้วิธีการหาตำแหน่งสามเหลี่ยมของ mesh ในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET เรียบร้อยแล้ว ไลบรารีอันทรงพลังนี้เปิดโอกาสที่เป็นไปได้ไม่รู้จบสำหรับการสร้างแบบจำลอง 3 มิติและการจัดการในแอปพลิเคชัน .NET ของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D กับไฟล์ 3D รูปแบบอื่นได้หรือไม่

ตอบ 1: ใช่ Aspose.3D รองรับไฟล์ 3D หลากหลายรูปแบบ รวมถึง FBX, STL, OBJ และอื่นๆ

### คำถามที่ 2: Aspose.3D เหมาะสำหรับทั้งเดสก์ท็อปและเว็บแอปพลิเคชันหรือไม่

A2: แน่นอน. Aspose.3D สามารถผสานรวมเข้ากับทั้งเดสก์ท็อปและเว็บแอปพลิเคชันได้อย่างราบรื่น

### คำถามที่ 3: มีตัวเลือกสิทธิ์การใช้งานสำหรับ Aspose.3D หรือไม่

 A3: ได้ คุณสามารถสำรวจตัวเลือกใบอนุญาตและทำการซื้อได้[ที่นี่](https://purchase.aspose.com/buy).

### คำถามที่ 4: มีฟอรัมชุมชนสำหรับการสนับสนุน Aspose.3D หรือไม่

 A4: ได้ คุณสามารถรับการสนับสนุนจากชุมชนและแบ่งปันคำถามของคุณได้ที่[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18).

### คำถามที่ 5: ฉันสามารถทดลองใช้ Aspose.3D ฟรีก่อนซื้อได้หรือไม่

 A5: แน่นอน! คุณสามารถดาวน์โหลดเวอร์ชันทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
