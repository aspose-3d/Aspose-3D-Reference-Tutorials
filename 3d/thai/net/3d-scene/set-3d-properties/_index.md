---
title: การตั้งค่าคุณสมบัติสามมิติในฉาก 3 มิติ
linktitle: การตั้งค่าคุณสมบัติสามมิติในฉาก 3 มิติ
second_title: Aspose.3D .NET API
description: สำรวจบทช่วยสอน Aspose.3D สำหรับ .NET เกี่ยวกับการตั้งค่าคุณสมบัติ 3D เรียนรู้ทีละขั้นตอนพร้อมตัวอย่างโค้ด ยกระดับทักษะการจัดการฉาก 3 มิติของคุณ
weight: 14
url: /th/net/3d-scene/set-3d-properties/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การตั้งค่าคุณสมบัติสามมิติในฉาก 3 มิติ

## การแนะนำ

การสร้างฉากสามมิติที่น่าดึงดูดมักต้องใช้ความสามารถในการจัดการคุณสมบัติต่างๆ เพิ่มความลึกและความสมจริงให้กับโปรเจ็กต์ของคุณ Aspose.3D สำหรับ .NET มอบชุดเครื่องมือที่มีประสิทธิภาพเพื่อให้บรรลุเป้าหมายนี้ ช่วยให้คุณสามารถตั้งค่าและแก้ไขคุณสมบัติสามมิติภายในฉาก 3 มิติของคุณได้อย่างง่ายดาย ในบทช่วยสอนนี้ เราจะสำรวจกระบวนการทีละขั้นตอน เพื่อเพิ่มความเข้าใจเกี่ยวกับวิธีการใช้ประโยชน์จาก Aspose.3D สำหรับ .NET อย่างมีประสิทธิภาพ

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับ .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารีในโปรเจ็กต์ .NET ของคุณ คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).

- ไดเร็กทอรีเอกสาร: สร้างไดเร็กทอรีเพื่อจัดเก็บเอกสาร 3 มิติของคุณ

เมื่อคุณมีสิ่งที่จำเป็นพร้อมแล้ว เรามาสำรวจกระบวนการตั้งค่าคุณสมบัติสามมิติในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET กันดีกว่า

## นำเข้าเนมสเปซ

ในการเริ่มต้น ให้นำเข้าเนมสเปซที่จำเป็นลงในโปรเจ็กต์ของคุณ เนมสเปซเหล่านี้มีคลาสและวิธีการที่จำเป็นสำหรับการทำงานกับคุณสมบัติสามมิติใน Aspose.3D สำหรับ .NET

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## ขั้นตอนที่ 1: โหลดฉาก 3 มิติ

เริ่มต้นด้วยการโหลดฉาก 3 มิติ ในตัวอย่างนี้ เราใช้ไฟล์ FBX ที่มีพื้นผิวแบบฝัง

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//สิ้นสุด: Load3DScene
```

## ขั้นตอนที่ 2: เข้าถึงคุณสมบัติของวัสดุ

เข้าถึงคุณสมบัติของวัสดุของฉาก 3D ที่โหลดเพื่อปรับแต่งคุณลักษณะ

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ตัวอย่าง: AccessMaterialProperties
```

## ขั้นตอนที่ 3: แสดงรายการคุณสมบัติทั้งหมด

แสดงรายการคุณสมบัติทั้งหมดของวัสดุโดยใช้ foreach loop หรือ ordinal for loop

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//หรือใช้ลำดับสำหรับวง
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ตัวอย่าง: ListAllProperties
```

## ขั้นตอนที่ 4: รับและแก้ไขทรัพย์สินตามชื่อ

ดึงข้อมูลและแก้ไขคุณสมบัติเฉพาะตามชื่อ

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//แก้ไขค่าคุณสมบัติตามชื่อ
props["Diffuse"] = new Vector3(1, 0, 1);
//ตัวอย่าง: GetModifyPropertyByName
```

## ขั้นตอนที่ 5: รับอินสแตนซ์คุณสมบัติตามชื่อ

ดึงข้อมูลอินสแตนซ์คุณสมบัติตามชื่อเพื่อการจัดการเพิ่มเติม

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ตัวอย่าง: GetPropertyInstanceByName
```

## ขั้นตอนที่ 6: คุณสมบัติของ Traverse Property

 เนื่องจาก`Property` สืบทอดมาจาก`A3DObject`คุณสามารถสำรวจคุณสมบัติของทรัพย์สินได้

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//และคุณสมบัติบางอย่างที่กำหนดไว้ในไฟล์ FBX เท่านั้น:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//สามารถทะลุผ่านทรัพย์สินของทรัพย์สินได้
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ตัวอย่าง: TraversePropertyProperties
```

## บทสรุป

ยินดีด้วย! ตอนนี้คุณเชี่ยวชาญศิลปะในการตั้งค่าคุณสมบัติสามมิติในฉาก 3 มิติโดยใช้ Aspose.3D สำหรับ .NET แล้ว ทดลองใช้คุณสมบัติและค่าต่างๆ เพื่อทำให้โครงการ 3D ของคุณมีชีวิตขึ้นมา

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับไฟล์ 3D รูปแบบอื่นได้หรือไม่

ตอบ 1: ใช่ Aspose.3D รองรับไฟล์ 3D หลากหลายรูปแบบ รวมถึง FBX, STL และอื่นๆ อีกมากมาย

### คำถามที่ 2: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ .NET ได้อย่างไร

 A2: เยี่ยมเลย[ที่นี่](https://purchase.aspose.com/temporary-license/) เพื่อขอรับใบอนุญาตชั่วคราว

### คำถามที่ 3: มีฟอรัมชุมชนสำหรับผู้ใช้ Aspose.3D หรือไม่

 A3: ใช่ คุณสามารถค้นหาการสนับสนุนและการสนทนาได้ที่[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18).

### คำถามที่ 4: ฉันจะหาเอกสารโดยละเอียดสำหรับ Aspose.3D สำหรับ .NET ได้ที่ไหน

 A4: โปรดดูที่[เอกสารประกอบ](https://reference.aspose.com/3d/net/) เพื่อรับคำแนะนำอย่างครอบคลุม

### คำถามที่ 5: ฉันสามารถทดลองใช้ Aspose.3D สำหรับ .NET ฟรีก่อนซื้อได้หรือไม่

 A5: แน่นอน! ดาวน์โหลด[รุ่นทดลองใช้ฟรี](https://releases.aspose.com/) เพื่อสำรวจคุณลักษณะต่างๆ

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
