---
title: การตั้งค่า UV บน Cube
linktitle: การตั้งค่า UV บน Cube
second_title: Aspose.3D .NET API
description: เรียนรู้วิธีตั้งค่าการทำแผนที่ UV บนคิวบ์ 3 มิติโดยใช้ Aspose.3D สำหรับ .NET สร้างฉากที่สวยงามตระการตาด้วยการทำแผนที่พื้นผิวที่แม่นยำ
weight: 18
url: /th/net/geometry-and-hierarchy/setup-uv-cube/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การตั้งค่า UV บน Cube

## การแนะนำ

การสร้างฉาก 3 มิติที่น่าดึงดูดและดึงดูดสายตามักเกี่ยวข้องกับกระบวนการที่พิถีพิถันในการตั้งค่าการทำแผนที่ UV บนรูปทรงเรขาคณิต ในบทช่วยสอนนี้ เราจะสำรวจวิธีตั้งค่า UV บนคิวบ์โดยใช้ Aspose.3D สำหรับ .NET Aspose.3D เป็นไลบรารี .NET ที่ทรงพลังซึ่งมีชุดคุณสมบัติที่ครอบคลุมสำหรับการสร้างแบบจำลองและการจัดการ 3D

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

1. Aspose.3D สำหรับไลบรารี .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).

2. สภาพแวดล้อมการพัฒนา: ตั้งค่าสภาพแวดล้อมการพัฒนา .NET ด้วยเครื่องมือที่จำเป็น

ตอนนี้เรามาดูบทช่วยสอนกันดีกว่า

## นำเข้าเนมสเปซ

ขั้นแรก นำเข้าเนมสเปซที่จำเป็นเพื่อเข้าถึงฟังก์ชัน Aspose.3D ในแอปพลิเคชัน .NET ของคุณ

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## ขั้นตอนที่ 1: กำหนด UV สำหรับ Cube

กำหนดพิกัด UV สำหรับแต่ละจุดยอดของลูกบาศก์ ซึ่งเกี่ยวข้องกับการระบุค่า U และ V สำหรับแต่ละมุมของคิวบ์

```csharp
// ExStart:กำหนดยูวี
Vector4[] uvs = new Vector4[]
{
    new Vector4(0.0, 1.0, 0.0, 1.0),
    new Vector4(1.0, 0.0, 0.0, 1.0),
    new Vector4(0.0, 0.0, 0.0, 1.0),
    new Vector4(1.0, 1.0, 0.0, 1.0)
};
// ExEnd:กำหนดยูวี
```

## ขั้นตอนที่ 2: กำหนดดัชนี UV

ระบุดัชนีพิกัด UV สำหรับแต่ละรูปหลายเหลี่ยมของลูกบาศก์ วิธีนี้จะกำหนดวิธีการจับคู่ UV กับพื้นผิวของลูกบาศก์

```csharp
// ExStart:กำหนดดัชนี UV
int[] uvsId = new int[]
{
    0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 9, 8, 1, 10, 11, 3, 12, 0, 2, 13
};
// ExEnd:กำหนดดัชนี UV
```

## ขั้นตอนที่ 3: สร้างตาข่าย

ใช้ไลบรารี Aspose.3D เพื่อสร้าง mesh โดยใช้วิธีสร้างรูปหลายเหลี่ยม สิ่งนี้จะทำหน้าที่เป็นรากฐานสำหรับลูกบาศก์ 3 มิติของเรา

```csharp
// ExStart:CreateMesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
// ตัวอย่าง: CreateMesh
```

## ขั้นตอนที่ 4: สร้างองค์ประกอบ UV

สร้างองค์ประกอบ UV ในตาข่ายเพื่อจัดเก็บข้อมูลการทำแผนที่ UV

```csharp
// ExStart: สร้าง UVElement
VertexElementUV elementUV = mesh.CreateElementUV(TextureMapping.Diffuse, MappingMode.PolygonVertex, ReferenceMode.IndexToDirect);
// ตัวอย่าง: สร้าง UVElement
```

## ขั้นตอนที่ 5: คัดลอกข้อมูล UV ไปยัง Mesh

คัดลอกพิกัดและดัชนี UV ที่กำหนดไว้ก่อนหน้านี้ไปยังองค์ประกอบจุดยอด UV ของตาข่าย

```csharp
// ExStart:CopyUVData
elementUV.Data.AddRange(uvs);
elementUV.Indices.AddRange(uvsId);
// ตัวอย่าง: CopyUVData
```

## บทสรุป

ยินดีด้วย! คุณได้ตั้งค่าการจับคู่ UV บนคิวบ์โดยใช้ Aspose.3D สำหรับ .NET เรียบร้อยแล้ว สิ่งนี้เปิดโอกาสในการสร้างฉาก 3 มิติที่ซับซ้อนและสวยงามด้วยภาพด้วยการทำแผนที่พื้นผิวที่แม่นยำ

## คำถามที่พบบ่อย

### คำถามที่ 1: Aspose.3D สำหรับ .NET คืออะไร

คำตอบ 1: Aspose.3D สำหรับ .NET เป็นไลบรารีที่มีประสิทธิภาพสำหรับการสร้างแบบจำลอง 3 มิติและการจัดการในแอปพลิเคชัน .NET

### คำถามที่ 2: ฉันจะหาเอกสาร Aspose.3D ได้ที่ไหน

 A2: มีเอกสารประกอบให้[ที่นี่](https://reference.aspose.com/3d/net/).

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

 A3: ได้ คุณสามารถเข้าถึงรุ่นทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร

 A4: เยี่ยมชมฟอรั่มการสนับสนุน[ที่นี่](https://forum.aspose.com/c/3d/18).

### คำถามที่ 5: มีใบอนุญาตชั่วคราวหรือไม่

 A5: ได้ คุณสามารถขอรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
