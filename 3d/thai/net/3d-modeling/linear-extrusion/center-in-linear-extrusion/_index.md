---
title: ศูนย์กลางในการอัดขึ้นรูปเชิงเส้น
linktitle: ศูนย์กลางในการอัดขึ้นรูปเชิงเส้น
second_title: Aspose.3D .NET API
description: สำรวจโลกแห่งการสร้างแบบจำลอง 3 มิติด้วย Aspose.3D สำหรับ .NET เทคนิคการอัดขึ้นรูปเชิงเส้นตรงกลาง สร้างการออกแบบที่น่าทึ่ง และปลดปล่อยความคิดสร้างสรรค์ของคุณ
weight: 10
url: /th/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ศูนย์กลางในการอัดขึ้นรูปเชิงเส้น

## การแนะนำ

ยินดีต้อนรับสู่คู่มือที่ครอบคลุมเกี่ยวกับการเรียนรู้การอัดขึ้นรูปเชิงเส้นโดยใช้ Aspose.3D สำหรับ .NET หากคุณกำลังมองหาที่จะพัฒนาทักษะการสร้างแบบจำลอง 3 มิติและสร้างการอัดขึ้นรูปที่น่าทึ่ง คุณมาถูกที่แล้ว ในบทช่วยสอนนี้ เราจะเจาะลึกเทคนิคการอัดขึ้นรูปเชิงเส้น โดยเน้นไปที่ลักษณะศูนย์กลางโดยเฉพาะเพื่อนำการออกแบบของคุณไปสู่อีกระดับหนึ่ง

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มต้นการเดินทางที่น่าตื่นเต้นนี้ ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

- ความเข้าใจพื้นฐานเกี่ยวกับภาษาการเขียนโปรแกรม C#
- ติดตั้ง Visual Studio บนเครื่องของคุณแล้ว
-  Aspose.3D สำหรับไลบรารี .NET ซึ่งคุณสามารถดาวน์โหลดได้จากไฟล์[เอกสาร Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  ตรวจสอบให้แน่ใจว่าคุณสามารถเข้าถึง[เอกสาร Aspose.3D .NET](https://reference.aspose.com/3d/net/) เพื่อใช้อ้างอิงตลอดบทช่วยสอน

## นำเข้าเนมสเปซ

เพื่อเริ่มต้นสิ่งต่างๆ เรามานำเข้าเนมสเปซที่จำเป็นกันดีกว่า สิ่งเหล่านี้จะวางรากฐานสำหรับผลงานชิ้นเอกด้านการสร้างแบบจำลอง 3 มิติของเรา

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## ขั้นตอนที่ 1: เริ่มต้นโปรไฟล์ฐาน

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## ขั้นตอนที่ 2: สร้างฉาก 3 มิติ

```csharp
Scene scene = new Scene();
```

## ขั้นตอนที่ 3: สร้างโหนดซ้ายและขวา

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## ขั้นตอนที่ 4: ดำเนินการอัดขึ้นรูปเชิงเส้นบนโหนดด้านซ้าย

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## ขั้นตอนที่ 5: ตั้งค่าระนาบกราวด์สำหรับการอ้างอิง

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## ขั้นตอนที่ 6: ดำเนินการอัดขึ้นรูปเชิงเส้นบนโหนดด้านขวา

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## ขั้นตอนที่ 7: ตั้งค่าระนาบกราวด์สำหรับการอ้างอิง (โหนดขวา)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## ขั้นตอนที่ 8: บันทึกฉาก 3 มิติ

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## บทสรุป

ยินดีด้วย! คุณเชี่ยวชาญศิลปะของการอัดขึ้นรูปเชิงเส้นด้วยการวางศูนย์กลางโดยใช้ Aspose.3D สำหรับ .NET สำเร็จแล้ว คุณสามารถทดลองใช้พารามิเตอร์ต่างๆ ได้อย่างอิสระและสำรวจความเป็นไปได้มากมายที่เทคนิคนี้นำเสนอ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับภาษาการเขียนโปรแกรมอื่นๆ ได้หรือไม่

A1: Aspose.3D รองรับภาษา .NET เป็นหลัก เช่น C# และ VB.NET

### คำถามที่ 2: ฉันจะรับการสนับสนุนสำหรับการสืบค้นที่เกี่ยวข้องกับ Aspose.3D ได้ที่ไหน

 A2: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายโดยเฉพาะ

### คำถามที่ 3: Aspose.3D สำหรับ .NET มีรุ่นทดลองใช้ฟรีหรือไม่

 A3: ได้ คุณสามารถเข้าถึงรุ่นทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ .NET ได้อย่างไร

 A4: คุณสามารถขอรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).

### คำถามที่ 5: ฉันจะซื้อใบอนุญาต Aspose.3D สำหรับ .NET ได้ที่ไหน

 A5: ซื้อใบอนุญาตของคุณ[ที่นี่](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
