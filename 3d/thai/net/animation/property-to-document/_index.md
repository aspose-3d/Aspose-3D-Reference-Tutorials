---
title: การสร้างภาพเคลื่อนไหวคุณสมบัติเพื่อจัดทำเอกสารในฉาก 3 มิติ
linktitle: การสร้างภาพเคลื่อนไหวคุณสมบัติเพื่อจัดทำเอกสารในฉาก 3 มิติ
second_title: Aspose.3D .NET API
description: เรียนรู้การสร้างภาพเคลื่อนไหวคุณสมบัติ 3 มิติด้วย Aspose.3D สำหรับ .NET คำแนะนำทีละขั้นตอนสำหรับการสร้างฉากแบบไดนามิก
type: docs
weight: 10
url: /th/net/animation/property-to-document/
---
## การแนะนำ

หากคุณกำลังดำดิ่งสู่ขอบเขตของการสร้างฉากและแอนิเมชั่น 3D ใน .NET Aspose.3D คือชุดเครื่องมือที่คุณใช้งานสะดวก ในคำแนะนำทีละขั้นตอนนี้ เราจะสำรวจกระบวนการสร้างภาพเคลื่อนไหวคุณสมบัติในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET ในตอนท้าย คุณจะได้รับความรู้ในการเติมชีวิตชีวาให้กับโปรเจ็กต์ 3 มิติของคุณ

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มต้นการเดินทางที่น่าตื่นเต้นนี้ ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับ .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารีแล้ว คุณสามารถดาวน์โหลดได้จาก[เว็บไซต์ Aspose.3D](https://releases.aspose.com/3d/net/).

- ความรู้เกี่ยวกับ C#: ความคุ้นเคยกับภาษาการเขียนโปรแกรม C# เป็นสิ่งจำเป็นสำหรับการทำความเข้าใจและการนำตัวอย่างไปใช้

- สภาพแวดล้อมการพัฒนาแบบรวม (IDE): ใช้ IDE ที่คุณต้องการ เช่น Visual Studio สำหรับการเขียนโค้ดพร้อมกับตัวอย่าง

- แนวคิดฉาก 3 มิติขั้นพื้นฐาน: ความเข้าใจแนวคิดเกี่ยวกับฉาก 3 มิติขั้นพื้นฐานจะทำให้การเดินทางการเรียนรู้ของคุณราบรื่นยิ่งขึ้น

## นำเข้าเนมสเปซ

ในโค้ด C# ของคุณ ตรวจสอบให้แน่ใจว่าคุณนำเข้าเนมสเปซที่จำเป็นสำหรับ Aspose.3D นี่คือตัวอย่าง:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## ขั้นตอนที่ 1: เริ่มต้นวัตถุฉาก

```csharp
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: สร้าง Mesh โดยใช้ Polygon Builder

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## ขั้นตอนที่ 3: สร้างโหนด Cube

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## ขั้นตอนที่ 4: ค้นหาคุณสมบัติการแปล

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## ขั้นตอนที่ 5: สร้างจุดผูก

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## ขั้นตอนที่ 6: ผูกแอนิเมชั่น Curve บน X Component

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## ขั้นตอนที่ 7: ผูกเส้นโค้งแอนิเมชั่นบนส่วนประกอบ Z

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## ขั้นตอนที่ 8: บันทึกฉาก 3 มิติ

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## ขั้นตอนที่ 9: แสดงข้อความแสดงความสำเร็จ

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## บทสรุป

ยินดีด้วย! คุณเพิ่งเชี่ยวชาญศิลปะในการสร้างภาพเคลื่อนไหวในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET ตอนนี้ ปล่อยให้ความคิดสร้างสรรค์ของคุณไหลลื่นในขณะที่คุณเติมชีวิตชีวาให้กับการสร้างสรรค์ 3 มิติของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันจะหาเอกสาร Aspose.3D ได้ที่ไหน

 A1: มีเอกสารประกอบให้[ที่นี่](https://reference.aspose.com/3d/net/).

### คำถามที่ 2: ฉันจะดาวน์โหลด Aspose.3D สำหรับ .NET ได้อย่างไร

 A2: คุณสามารถดาวน์โหลดได้จากไฟล์[หน้าปล่อย](https://releases.aspose.com/3d/net/).

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

 A3: ใช่ คุณสามารถทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้ที่ไหน

 A4: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุน

### คำถามที่ 5: ฉันสามารถขอรับใบอนุญาตชั่วคราวได้หรือไม่

 A5: ได้ คุณสามารถขอรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).