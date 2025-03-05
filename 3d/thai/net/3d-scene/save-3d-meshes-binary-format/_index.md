---
title: บันทึก 3D Meshes ในรูปแบบไบนารีที่กำหนดเอง
linktitle: บันทึก 3D Meshes ในรูปแบบไบนารีที่กำหนดเอง
second_title: Aspose.3D .NET API
description: สำรวจโลกแห่ง 3D ด้วย Aspose.3D สำหรับ .NET เรียนรู้วิธีบันทึก Meshes ในรูปแบบไบนารีที่กำหนดเอง
type: docs
weight: 13
url: /th/net/3d-scene/save-3d-meshes-binary-format/
---
## การแนะนำ

ยินดีต้อนรับสู่โลกของ Aspose.3D สำหรับ .NET ไลบรารีอันทรงพลังที่ช่วยให้นักพัฒนาสามารถทำงานกับไฟล์ 3D ได้อย่างง่ายดาย ในบทช่วยสอนนี้ เราจะเจาะลึกกระบวนการบันทึก 3D mesh ในรูปแบบไบนารีแบบกำหนดเองโดยใช้ Aspose.3D สำหรับ .NET คู่มือนี้ถือว่าคุณมีความเข้าใจพื้นฐานเกี่ยวกับ C# และคุ้นเคยกับไลบรารี Aspose.3D

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีสิ่งต่อไปนี้:

-  Aspose.3D สำหรับ .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้จาก[ที่นี่](https://releases.aspose.com/3d/net/).

- สภาพแวดล้อมการพัฒนา: ตั้งค่าสภาพแวดล้อมการพัฒนา C# ที่คุณต้องการ เช่น Visual Studio

- อินพุตไฟล์ 3D: มีไฟล์ 3D (เช่น test.fbx) ที่คุณต้องการแปลงเป็นรูปแบบไบนารีแบบกำหนดเอง

## นำเข้าเนมสเปซ

ในโค้ด C# ของคุณ ให้รวมเนมสเปซที่จำเป็นเพื่อเข้าถึงฟังก์ชัน Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## ขั้นตอนที่ 1: โหลดไฟล์ 3D

โหลดไฟล์ 3D ของคุณโดยใช้ Aspose.3D ในตัวอย่างนี้ เราโหลดไฟล์ชื่อ "test.fbx":

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## ขั้นตอนที่ 2: กำหนดรูปแบบไบนารีแบบกำหนดเอง

กำหนดโครงสร้างของรูปแบบไบนารีแบบกำหนดเองที่คุณต้องการบันทึก 3D Meshes ของคุณ ตัวอย่างนี้ใช้โครงสร้างที่มี MeshBlock, Vertex และ Triangle เป็นส่วนประกอบ

```csharp
// รูปแบบหน่วยความจำของจุดยอดคือ
// ตำแหน่งลอย [3];
// ลอย [3] ปกติ;
// ลอย[3]ยูวี;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## ขั้นตอนที่ 3: เปิดไฟล์เพื่อเขียน

เปิดไฟล์ไบนารี่เพื่อเขียน โดยที่ 3D meshes ที่แปลงแล้วจะถูกบันทึก:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## ขั้นตอนที่ 4: วนซ้ำผ่านโหนดและเอนทิตี

เยี่ยมชมแต่ละโหนดในฉาก 3 มิติและแปลงเอนทิตีแบบตาข่ายเป็นรูปแบบไบนารีที่กำหนดเอง ละเว้นไฟ กล้อง และเอนทิตีอื่นๆ ที่ไม่ใช่ตาข่าย:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (ดำเนินการประมวลผลต่อ)
    }
    return true;
});
```

## ขั้นตอนที่ 5: แปลงและเขียนจุดควบคุมและสามเหลี่ยม

สำหรับแต่ละเอนทิตีแบบตาข่าย ให้แปลงจุดควบคุมเป็นพื้นที่โลกและเขียนลงในไฟล์ไบนารีพร้อมกับดัชนีสามเหลี่ยม:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//เค้าโครงหน่วยความจำของ mesh คือ:
// ลอย [16] แปลง_เมทริกซ์;
// int vertices_count;
// ดัชนี int_count;
// จุดยอด [vertices_count] จุดยอด;
// ushort[indices_count] ดัชนี;


//เขียนการแปลง
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//เขียนจำนวนจุดยอด/ดัชนี
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//เขียนจุดยอดและดัชนี
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## บทสรุป

ในบทช่วยสอนนี้ เราได้กล่าวถึงกระบวนการบันทึก 3D mesh ในรูปแบบไบนารีแบบกำหนดเองโดยใช้ Aspose.3D สำหรับ .NET ไลบรารีอันทรงพลังนี้มอบเครื่องมือที่จำเป็นสำหรับนักพัฒนาในการจัดการไฟล์ 3D ได้อย่างราบรื่น ทดลองใช้รูปแบบและการตั้งค่าต่างๆ เพื่อปลดล็อกศักยภาพสูงสุดของ Aspose.3D ในโปรเจ็กต์ของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับภาษาการเขียนโปรแกรมอื่นๆ ได้หรือไม่

คำตอบ 1: Aspose.3D รองรับภาษา .NET เป็นหลัก แต่คุณสามารถสำรวจตัวเลือกความเข้ากันได้สำหรับภาษาอื่นได้

### คำถามที่ 2: ฉันจะหาตัวอย่างและแหล่งข้อมูลเพิ่มเติมได้จากที่ไหน

 A2: เดอะ[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18)เป็นสถานที่ที่ดีในการค้นหาการสนับสนุน ตัวอย่าง และการมีส่วนร่วมกับชุมชน

### คำถามที่ 3: Aspose.3D มีเวอร์ชันทดลองใช้งานหรือไม่

 A3: ได้ คุณสามารถทดลองใช้งานฟรีได้จาก[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร

 A4: เยี่ยมเลย[ลิงค์นี้](https://purchase.aspose.com/temporary-license/) เพื่อรับใบอนุญาตชั่วคราวเพื่อการทดสอบ

### คำถามที่ 5: ฉันสามารถซื้อ Aspose.3D สำหรับ .NET ได้หรือไม่

 A5: ได้ คุณสามารถซื้อ Aspose.3D ได้จาก[หน้าซื้อ](https://purchase.aspose.com/buy).