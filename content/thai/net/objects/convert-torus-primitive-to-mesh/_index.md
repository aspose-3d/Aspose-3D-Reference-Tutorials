---
title: การแปลง Torus Primitive เป็น Mesh
linktitle: การแปลง Torus Primitive เป็น Mesh
second_title: Aspose.3D .NET API
description: สำรวจพลังของ Aspose.3D สำหรับ .NET ด้วยคำแนะนำทีละขั้นตอนในการแปลง Torus primitives เป็น meshes ยกระดับการพัฒนา 3D ของคุณอย่างง่ายดาย!
type: docs
weight: 17
url: /th/net/objects/convert-torus-primitive-to-mesh/
---
## การแนะนำ
คุณกระตือรือร้นที่จะควบคุมพลังของ Aspose.3D สำหรับ .NET เพื่อแปลง Torus ดั้งเดิมเป็น mesh ได้อย่างราบรื่นหรือไม่? ไม่ต้องมองอีกต่อไป! ในบทช่วยสอนนี้ เราจะแนะนำคุณตลอดกระบวนการ โดยแจกแจงแต่ละขั้นตอนเพื่อให้แน่ใจว่าการเดินทางจะราบรื่น Aspose.3D สำหรับ .NET มอบแพลตฟอร์มที่แข็งแกร่งในการจัดการฉาก 3D ทำให้เป็นเครื่องมือที่นักพัฒนาต้องการประสิทธิภาพและความยืดหยุ่น
## ข้อกำหนดเบื้องต้น
ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
-  Aspose.3D สำหรับ .NET: ดาวน์โหลดและติดตั้งไลบรารี คุณสามารถค้นหาลิงค์ดาวน์โหลด[ที่นี่](https://releases.aspose.com/3d/net/).
-  ไฟล์ 3D: เตรียมไฟล์ 3D ตัวอย่างในรูปแบบที่รองรับ หากคุณไม่มีคุณสามารถใช้[ทดสอบ.fbx](https://reference.aspose.com/3d/net/) ไฟล์จากเอกสาร Aspose.3D
## นำเข้าเนมสเปซ
ในโปรเจ็กต์ .NET ของคุณ ให้นำเข้าเนมสเปซที่จำเป็นเพื่อให้แน่ใจว่าบูรณาการกับ Aspose.3D ได้อย่างราบรื่น เพิ่มสิ่งต่อไปนี้ที่จุดเริ่มต้นของรหัสของคุณ:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## ขั้นตอนที่ 1: โหลดไฟล์ 3D
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("test.fbx"));
```
โหลดไฟล์ 3D ของคุณลงในฉาก แทนที่`"test.fbx"` พร้อมเส้นทางไปยังไฟล์ของคุณ
## ขั้นตอนที่ 2: เริ่มต้นวัตถุคลาสโหนด
```csharp
Node torusNode = new Node("torus");
```
สร้างวัตถุโหนดใหม่สำหรับ Torus ดั้งเดิม
## ขั้นตอนที่ 3: แปลง Torus เป็น Mesh
```csharp
IMeshConvertible convertible = new Torus();
Mesh mesh = convertible.ToMesh();
```
ใช้ความสามารถของ Aspose.3D เพื่อแปลง Torus ดั้งเดิมเป็น mesh
## ขั้นตอนที่ 4: ชี้โหนดไปที่เรขาคณิตตาข่าย
```csharp
torusNode.Entity = mesh;
```
เชื่อมโยงเรขาคณิตของตาข่ายกับโหนด
## ขั้นตอนที่ 5: เพิ่มโหนดไปที่ฉาก
```csharp
scene.RootNode.ChildNodes.Add(torusNode);
```
รวมโหนดทอรัสเข้ากับฉาก
## ขั้นตอนที่ 6: บันทึกฉาก 3 มิติ
```csharp
var output = "Your Output Directory" + "TorusToMeshScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
Console.WriteLine("\nConverted the primitive Torus to a mesh successfully.\nFile saved at " + output);
```
บันทึกฉาก 3D ที่แก้ไขในรูปแบบไฟล์และตำแหน่งที่ต้องการ
## บทสรุป
ยินดีด้วย! คุณแปลง Torus primitive ให้เป็น mesh ได้สำเร็จโดยใช้ Aspose.3D สำหรับ .NET ไลบรารีอันทรงพลังนี้เปิดโลกแห่งความเป็นไปได้สำหรับการปรับแต่ง 3D ในโครงการ .NET ของคุณ
## คำถามที่พบบ่อย
### Aspose.3D เข้ากันได้กับไฟล์ 3D ทุกรูปแบบหรือไม่
Aspose.3D รองรับรูปแบบไฟล์ 3D ที่หลากหลาย ตรวจสอบเอกสารเพื่อดูรายการทั้งหมด
### ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่
 ใช่ Aspose.3D เสนอใบอนุญาตเชิงพาณิชย์ เยี่ยม[buy.aspose.com/buy](https://purchase.aspose.com/buy) เพื่อดูรายละเอียด
### มีใบอนุญาตชั่วคราวสำหรับการทดสอบหรือไม่?
 ใช่ คุณสามารถขอรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/) สำหรับการทดสอบ
### ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้ที่ไหน
 เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและช่วยเหลือชุมชน
### ฉันสามารถสำรวจบทช่วยสอนและตัวอย่างเพิ่มเติมได้หรือไม่
 ใช่อ้างอิงถึง[เอกสารประกอบ](https://reference.aspose.com/3d/net/) สำหรับบทช่วยสอนและตัวอย่างที่ครอบคลุม