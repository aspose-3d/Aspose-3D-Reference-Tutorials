---
title: การแปลงรูปทรงกระบอกดั้งเดิมเป็นตาข่าย
linktitle: การแปลงรูปทรงกระบอกดั้งเดิมเป็นตาข่าย
second_title: Aspose.3D .NET API
description: เรียนรู้วิธีแปลงทรงกระบอกดั้งเดิมเป็น Mesh ได้อย่างง่ายดายโดยใช้ Aspose.3D สำหรับ .NET ปฏิบัติตามคำแนะนำทีละขั้นตอนของเราเพื่อการแปลง 3 มิติที่ราบรื่น
type: docs
weight: 13
url: /th/net/objects/convert-cylinder-primitive-to-mesh/
---
## การแนะนำ
ยินดีต้อนรับสู่คำแนะนำที่ครอบคลุมเกี่ยวกับการใช้ Aspose.3D สำหรับ .NET เพื่อแปลงทรงกระบอกดั้งเดิมเป็น Mesh Aspose.3D เป็นไลบรารีอันทรงพลังที่ช่วยให้นักพัฒนา .NET สามารถทำงานกับรูปแบบไฟล์ 3D ได้อย่างราบรื่น ในบทช่วยสอนนี้ เราจะแนะนำคุณตลอดขั้นตอนการแปลงทรงกระบอกดั้งเดิมให้เป็น Mesh โดยให้ขั้นตอนและคำอธิบายโดยละเอียดแก่คุณ
## ข้อกำหนดเบื้องต้น
ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
-  Aspose.3D สำหรับ .NET Library: ดาวน์โหลดและติดตั้งไลบรารีจาก[ที่นี่](https://releases.aspose.com/3d/net/).
- สภาพแวดล้อมการพัฒนา .NET: ตรวจสอบให้แน่ใจว่าคุณมีสภาพแวดล้อมการพัฒนา .NET ที่ใช้งานได้
## นำเข้าเนมสเปซ
เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็นในโครงการ .NET ของคุณ:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
ตอนนี้ เรามาแบ่งตัวอย่างออกเป็นหลายขั้นตอนกัน
## ขั้นตอนที่ 1: เริ่มต้นวัตถุฉาก
```csharp
Scene scene = new Scene();
```
ที่นี่ เราสร้างวัตถุฉากใหม่ ซึ่งทำหน้าที่เป็นคอนเทนเนอร์สำหรับเอนทิตี 3 มิติ
## ขั้นตอนที่ 2: เริ่มต้นวัตถุคลาสโหนด
```csharp
Node cubeNode = new Node("cylinder");
```
ต่อไป เราจะเริ่มต้นวัตถุ Node ที่ชื่อว่า "cylinder" เพื่อเป็นตัวแทนของวัตถุ 3 มิติของเรา
## ขั้นตอนที่ 3: แปลงรูปทรงกระบอกเป็นตาข่าย
```csharp
IMeshConvertible convertible = new Cylinder();
Mesh mesh = convertible.ToMesh();
```
ใช้ไลบรารี Aspose.3D เพื่อแปลงทรงกระบอกดั้งเดิมให้เป็น Mesh
## ขั้นตอนที่ 4: ชี้โหนดไปที่เรขาคณิตตาข่าย
```csharp
cubeNode.Entity = mesh;
```
เชื่อมโยงเรขาคณิตของ Mesh กับโหนดที่สร้างไว้ก่อนหน้านี้
## ขั้นตอนที่ 5: เพิ่มโหนดไปที่ฉาก
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
รวมโหนดไว้ในฉากด้วยการเพิ่มลงในโหนดย่อยของโหนดรูท
## ขั้นตอนที่ 6: บันทึกฉาก 3 มิติ
```csharp
string output = "Your Output Directory" + "CylinderToMeshScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
Console.WriteLine("\n Converted the primitive Cylinder to a mesh successfully.\nFile saved at " + output);
```
ระบุไดเร็กทอรีเอาต์พุตและบันทึกฉาก 3D ในรูปแบบไฟล์ที่ต้องการ (ในกรณีนี้คือ FBX)
## บทสรุป
ยินดีด้วย! คุณได้แปลงทรงกระบอกดั้งเดิมเป็น Mesh โดยใช้ Aspose.3D สำหรับ .NET สำเร็จแล้ว บทช่วยสอนนี้ได้จัดเตรียมขั้นตอนพื้นฐานที่จำเป็นสำหรับการเปลี่ยนแปลงนี้ให้กับคุณ
## คำถามที่พบบ่อย
### ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับภาษาการเขียนโปรแกรมอื่นได้หรือไม่
ไม่ Aspose.3D ได้รับการออกแบบมาโดยเฉพาะสำหรับการพัฒนา .NET
### มีการทดลองใช้ฟรีหรือไม่?
 ใช่ คุณสามารถเข้าถึงการทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).
### ฉันจะหาเอกสาร Aspose.3D ได้ที่ไหน
 โปรดดูเอกสารประกอบ[ที่นี่](https://reference.aspose.com/3d/net/).
### ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร
 เยี่ยมชมฟอรั่มการสนับสนุน[ที่นี่](https://forum.aspose.com/c/3d/18).
### มีตัวเลือกใบอนุญาตชั่วคราวหรือไม่?
 ใช่ รับใบอนุญาตชั่วคราว[ที่นี่](https://purchase.aspose.com/temporary-license/).