---
title: การแยกตาข่ายทั้งหมดของฉากตามวัสดุ
linktitle: การแยกตาข่ายทั้งหมดของฉากตามวัสดุ
second_title: Aspose.3D .NET API
description: เรียนรู้วิธีแยก 3D meshes ตามวัสดุโดยใช้ Aspose.3D สำหรับ .NET ปฏิบัติตามคำแนะนำทีละขั้นตอนของเราเพื่อการจัดระเบียบและการจัดการโมเดล 3 มิติที่มีประสิทธิภาพ
weight: 21
url: /th/net/meshes/split-all-meshes-by-material/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การแยกตาข่ายทั้งหมดของฉากตามวัสดุ

## การแนะนำ
ยินดีต้อนรับสู่คำแนะนำทีละขั้นตอนเกี่ยวกับการแยก mesh ทั้งหมดของฉาก 3D ตามวัสดุโดยใช้ Aspose.3D สำหรับ .NET หากคุณกำลังทำงานกับโมเดล 3 มิติและต้องการจัดระเบียบ mesh ของคุณตามวัสดุอย่างมีประสิทธิภาพ บทช่วยสอนนี้เหมาะสำหรับคุณ Aspose.3D เป็นไลบรารี .NET ที่ทรงพลังซึ่งมีฟีเจอร์มากมายสำหรับการทำงานกับไฟล์ 3D ทำให้เป็นตัวเลือกที่ยอดเยี่ยมสำหรับนักพัฒนา
## ข้อกำหนดเบื้องต้น
ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:
- ความเข้าใจพื้นฐานเกี่ยวกับภาษาการเขียนโปรแกรม C#
- ติดตั้ง Visual Studio บนเครื่องของคุณแล้ว
-  Aspose.3D สำหรับไลบรารี .NET คุณสามารถดาวน์โหลดได้จาก[ที่นี่](https://releases.aspose.com/3d/net/).
- ไฟล์ 3D อินพุต (เช่น "test.fbx") ที่คุณต้องการแยก
## นำเข้าเนมสเปซ
เริ่มต้นด้วยการนำเข้าเนมสเปซที่จำเป็นในโปรเจ็กต์ C# ของคุณ:
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
// เส้นทางไปยังไดเร็กทอรีเอกสาร
string input = RunExamples.GetDataFilePath("test.fbx");
// โหลดไฟล์ 3D
Scene scene = new Scene(input);
```
 ในขั้นตอนนี้ เราโหลดไฟล์ 3D โดยใช้ Aspose.3D's`Scene` ระดับ.
## ขั้นตอนที่ 2: แยกตาข่ายทั้งหมด
```csharp
// แยกตาข่ายทั้งหมด
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 ในที่นี้เราใช้.`SplitMesh` วิธีการจาก`PolygonModifier` คลาสเพื่อแยกตาข่ายทั้งหมดตามวัสดุ
## ขั้นตอนที่ 3: บันทึกฉากแยก
```csharp
// บันทึกไฟล์
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
บันทึกฉากที่แก้ไขลงในไฟล์ใหม่เพื่อคงการเปลี่ยนแปลงไว้
## ขั้นตอนที่ 4: แสดงข้อความแสดงความสำเร็จ
```csharp
// แสดงข้อความแสดงความสำเร็จ
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
พิมพ์ข้อความแสดงความสำเร็จที่ระบุว่าการดำเนินการเสร็จสมบูรณ์แล้ว
## บทสรุป
ยินดีด้วย! คุณได้เรียนรู้วิธีแบ่ง mesh ทั้งหมดของฉาก 3D ตามวัสดุโดยใช้ Aspose.3D สำหรับ .NET เรียบร้อยแล้ว นี่อาจเป็นเทคนิคที่มีคุณค่าในการจัดระเบียบและจัดการโมเดล 3 มิติที่ซับซ้อน
## คำถามที่พบบ่อย
### 1. ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับภาษาการเขียนโปรแกรมอื่นๆ ได้หรือไม่
Aspose.3D ได้รับการออกแบบมาเพื่อ .NET เป็นหลัก แต่มีความสามารถในการทำงานร่วมกับภาษาอื่น ๆ ผ่านการผูกภาษา .NET
### 2. มีเวอร์ชันทดลองใช้งานหรือไม่?
 ใช่ คุณสามารถเข้าถึงเวอร์ชันทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).
### 3. ฉันจะหาตัวอย่างและเอกสารเพิ่มเติมได้จากที่ไหน?
 สำรวจเอกสารฉบับสมบูรณ์ได้ที่[เอกสาร Aspose.3D](https://reference.aspose.com/3d/net/).
### 4. ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร
 เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายของชุมชน
### 5. ฉันสามารถขอรับใบอนุญาตชั่วคราวได้หรือไม่?
 ใช่ คุณสามารถรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
