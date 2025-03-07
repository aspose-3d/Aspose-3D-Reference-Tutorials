---
title: การแปลงโหนดโดย Quaternion
linktitle: การแปลงโหนดโดย Quaternion
second_title: Aspose.3D .NET API
description: เรียนรู้วิธีการแปลงโหนด 3 มิติด้วยควอเทอร์เนียนโดยใช้ Aspose.3D สำหรับ .NET คำแนะนำทีละขั้นตอนสำหรับผู้เริ่มต้น
weight: 20
url: /th/net/geometry-and-hierarchy/transformation-node-quaternion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การแปลงโหนดโดย Quaternion

## การแนะนำ

ยินดีต้อนรับสู่คำแนะนำทีละขั้นตอนเกี่ยวกับการแปลงโหนดตามควอเทอร์เนียนในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET ในบทช่วยสอนนี้ เราจะสำรวจความสามารถอันทรงพลังของ Aspose.3D สำหรับ .NET และอธิบายกระบวนการเพิ่มการแปลงให้กับโหนด 3D โดยใช้ควอเทอร์เนียน

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับ .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้จาก[หน้าปล่อย](https://releases.aspose.com/3d/net/).

- สภาพแวดล้อมการพัฒนา: ตั้งค่าสภาพแวดล้อมการพัฒนา .NET ของคุณด้วยเครื่องมือและการกำหนดค่าที่จำเป็น

- ความเข้าใจพื้นฐานเกี่ยวกับแนวคิด 3 มิติ: ความคุ้นเคยกับกราฟิกและแนวคิด 3 มิติจะเป็นประโยชน์

## นำเข้าเนมสเปซ

ในโปรเจ็กต์ .NET ของคุณ ให้รวมเนมสเปซที่จำเป็นสำหรับ Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## ขั้นตอนที่ 1: เริ่มต้นวัตถุฉาก

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// เริ่มต้นวัตถุฉาก
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: เริ่มต้นวัตถุคลาสโหนด

```csharp
// เริ่มต้นวัตถุคลาสโหนด
Node cubeNode = new Node("cube");
```

## ขั้นตอนที่ 3: สร้าง Mesh โดยใช้ Polygon Builder

```csharp
// เรียกคลาส Common สร้าง mesh โดยใช้วิธีสร้างรูปหลายเหลี่ยมเพื่อตั้งค่าอินสแตนซ์ mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## ขั้นตอนที่ 4: ชี้โหนดไปที่เรขาคณิตของตาข่าย

```csharp
// ชี้โหนดไปที่เรขาคณิตของ Mesh
cubeNode.Entity = mesh;
```

## ขั้นตอนที่ 5: ตั้งค่าการหมุนโดยใช้ Quaternion

```csharp
// ตั้งค่าการหมุน
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## ขั้นตอนที่ 6: ตั้งค่าการแปล

```csharp
// ตั้งค่าการแปล
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## ขั้นตอนที่ 7: เพิ่ม Cube ลงในฉาก

```csharp
// เพิ่มลูกบาศก์ลงในฉาก
scene.RootNode.ChildNodes.Add(cubeNode);
```

## ขั้นตอนที่ 8: บันทึกฉาก 3 มิติ

```csharp
// เส้นทางไปยังไดเร็กทอรีเอกสาร
var output = "Your Output Directory" + "TransformationToNode.fbx";

// บันทึกฉาก 3 มิติในรูปแบบไฟล์ที่รองรับ
scene.Save(output, FileFormat.FBX7500ASCII);
// ตัวอย่าง: AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## บทสรุป

 ยินดีด้วย! คุณได้เรียนรู้วิธีแปลงโหนดทีละควอเทอร์เนียนในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET เรียบร้อยแล้ว สำรวจคุณสมบัติและความเป็นไปได้เพิ่มเติมโดยอ้างอิงจาก[เอกสารประกอบ](https://reference.aspose.com/3d/net/).

## คำถามที่พบบ่อย

### คำถามที่ 1: ควอเทอร์เนียนในกราฟิก 3 มิติคืออะไร

คำตอบ 1: ควอเทอร์เนียนเป็นเอนทิตีทางคณิตศาสตร์ที่ใช้แทนการหมุนในพื้นที่ 3 มิติ

### คำถามที่ 2: ฉันจะดาวน์โหลด Aspose.3D สำหรับ .NET ได้อย่างไร

 A2: คุณสามารถดาวน์โหลดไลบรารีได้จากไฟล์[หน้าปล่อย](https://releases.aspose.com/3d/net/).

### คำถามที่ 3: Aspose.3D สำหรับ .NET มีรุ่นทดลองใช้ฟรีหรือไม่

 A3: ได้ คุณสามารถทดลองใช้งานฟรีได้จาก[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D สำหรับ .NET ได้ที่ไหน

 A4: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปราย

### คำถามที่ 5: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร

 A5: รับใบอนุญาตชั่วคราว[ที่นี่](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
