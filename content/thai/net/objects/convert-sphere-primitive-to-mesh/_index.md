---
title: การแปลง Sphere Primitive เป็น Mesh
linktitle: การแปลง Sphere Primitive เป็น Mesh
second_title: Aspose.3D .NET API
description: สำรวจ Aspose.3D สำหรับ .NET และแปลง Sphere Mesh เป็น Triangle Mesh ได้อย่างง่ายดายด้วยเค้าโครงหน่วยความจำแบบกำหนดเอง ปฏิบัติตามคำแนะนำทีละขั้นตอนของเราเพื่อการบูรณาการที่ราบรื่น
type: docs
weight: 16
url: /th/net/objects/convert-sphere-primitive-to-mesh/
---
## การแนะนำ
คุณต้องการควบคุมพลังของ Aspose.3D สำหรับ .NET เพื่อแปลง Sphere Mesh เป็น Triangle Mesh ด้วยเค้าโครงหน่วยความจำแบบกำหนดเองหรือไม่? คำแนะนำทีละขั้นตอนนี้จะแนะนำคุณตลอดกระบวนการ ทำให้ง่ายสำหรับผู้เริ่มต้นที่จะปฏิบัติตาม เมื่อสิ้นสุดบทช่วยสอนนี้ คุณจะมีความเข้าใจอย่างถ่องแท้เกี่ยวกับวิธีการบรรลุเป้าหมายนี้โดยใช้ Aspose.3D สำหรับ .NET
## ข้อกำหนดเบื้องต้น
ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
- ความรู้พื้นฐานเกี่ยวกับการเขียนโปรแกรม .NET
-  ติดตั้ง Aspose.3D สำหรับไลบรารี .NET แล้ว คุณสามารถดาวน์โหลดได้จาก[หน้าดาวน์โหลด Aspose.3D สำหรับ .NET](https://releases.aspose.com/3d/net/).
- ความคุ้นเคยกับภาษาการเขียนโปรแกรม C#
## นำเข้าเนมสเปซ
ในโปรเจ็กต์ C# ของคุณ ตรวจสอบให้แน่ใจว่าได้นำเข้าเนมสเปซที่จำเป็นเพื่อใช้ประโยชน์จากฟังก์ชัน Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## ขั้นตอนที่ 1: เริ่มต้นวัตถุฉาก
```csharp
// เริ่มต้นวัตถุฉาก
Scene scene = new Scene();
```
## ขั้นตอนที่ 2: เริ่มต้นวัตถุคลาสโหนด
```csharp
// เริ่มต้นวัตถุคลาสโหนด
Node cubeNode = new Node("sphere");
```
## ขั้นตอนที่ 3: แปลง Sphere Mesh เป็น TriMesh ที่พิมพ์
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## ขั้นตอนที่ 4: รับข้อมูล Vertex ในโครงสร้างที่กำหนดเอง
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## ขั้นตอนที่ 5: รับดัชนี 32 บิตและ 16 บิต
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## ขั้นตอนที่ 6: เขียนข้อมูลจุดสุดยอดและดัชนีไปยังสตรีมหน่วยความจำ
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## ขั้นตอนที่ 7: ชี้โหนดไปที่เรขาคณิตตาข่าย
```csharp
cubeNode.Entity = sphere;
```
## ขั้นตอนที่ 8: เพิ่มโหนดไปที่ฉาก
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## ขั้นตอนที่ 9: บันทึกฉาก 3 มิติ
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## ขั้นตอนที่ 10: แสดงผล
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## ซอร์สโค้ดตัวอย่าง MyVertex
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## บทสรุป
ยินดีด้วย! คุณได้แปลง Sphere Mesh เป็น Triangle Mesh สำเร็จด้วยเลย์เอาต์หน่วยความจำแบบกำหนดเองโดยใช้ Aspose.3D สำหรับ .NET ไลบรารีอันทรงพลังนี้มอบวิธีที่ราบรื่นในการจัดการกับวัตถุ 3 มิติในแอปพลิเคชัน .NET ของคุณ
## คำถามที่พบบ่อย
### ถาม: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับเฟรมเวิร์ก .NET อื่นๆ ได้หรือไม่
ตอบ: ใช่ Aspose.3D สำหรับ .NET เข้ากันได้กับเฟรมเวิร์ก .NET ต่างๆ
### ถาม: ฉันจะหาเอกสารโดยละเอียดสำหรับ Aspose.3D สำหรับ .NET ได้ที่ไหน
 ตอบ: โปรดดูที่[Aspose.3D สำหรับเอกสาร .NET](https://reference.aspose.com/3d/net/) เพื่อข้อมูลเชิงลึก
### ถาม: ฉันจะรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ .NET ได้อย่างไร
 ตอบ: เยี่ยมชม[ลิงค์นี้](https://purchase.aspose.com/temporary-license/) เพื่อขอรับใบอนุญาตชั่วคราว
### ถาม: มีโปรเจ็กต์ตัวอย่างสำหรับ Aspose.3D สำหรับ .NET หรือไม่
 ตอบ: สำรวจเอกสาร Aspose.3D สำหรับ .NET และ[พื้นที่เก็บข้อมูล GitHub](https://github.com/aspose-3d/Aspose.3D-for-.NET) สำหรับโครงการตัวอย่าง
### ถาม: มีชุมชนที่กระตือรือร้นสำหรับ Aspose.3D สำหรับการสนับสนุน .NET หรือไม่
 ตอบ: ใช่ เข้าร่วมกับ[Aspose.3D สำหรับฟอรัม .NET](https://forum.aspose.com/c/3d/18) เพื่อรับความช่วยเหลือจากชุมชน