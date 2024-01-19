---
title: กำลังโหลดและบันทึก - การใช้ CancellationToken
linktitle: กำลังโหลดและบันทึก - การใช้ CancellationToken
second_title: Aspose.3D .NET API
description: สำรวจโลกที่ไร้รอยต่อของการสร้างแบบจำลอง 3 มิติด้วย Aspose.3D สำหรับ .NET เรียนรู้การโหลดและบันทึกเอกสาร 3 มิติอย่างมีประสิทธิภาพโดยใช้ CancellationToken
type: docs
weight: 10
url: /th/net/loading-and-saving/cancellation-token/
---
## การแนะนำ

ยินดีต้อนรับสู่คำแนะนำที่ครอบคลุมของเราเกี่ยวกับการใช้ Aspose.3D สำหรับ .NET เพื่อปรับปรุงการสร้างแบบจำลอง 3 มิติและการเรนเดอร์โปรเจ็กต์ของคุณ Aspose.3D เป็นไลบรารีอันทรงพลังที่ช่วยให้นักพัฒนา .NET สามารถทำงานกับไฟล์ 3D ได้อย่างราบรื่น ในบทช่วยสอนนี้ เราจะเจาะลึกแง่มุมต่างๆ ของการโหลดและการบันทึก โดยเน้นที่การใช้ CancellationToken โดยเฉพาะเพื่อการจัดการงานอะซิงโครนัสอย่างมีประสิทธิภาพ

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มต้นการเดินทางครั้งนี้ ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับ .NET: ดาวน์โหลดและติดตั้งไลบรารีจาก[ที่นี่](https://releases.aspose.com/3d/net/).
- สภาพแวดล้อม .NET: ตรวจสอบให้แน่ใจว่าคุณได้ตั้งค่าสภาพแวดล้อมการพัฒนา .NET ที่เข้ากันได้
- ความเข้าใจพื้นฐานของ C#: แนะนำให้คุ้นเคยกับภาษาการเขียนโปรแกรม C#

## นำเข้าเนมสเปซ

ในการเริ่มต้น ตรวจสอบให้แน่ใจว่าคุณได้ใส่เนมสเปซที่จำเป็นในโครงการของคุณ เนมสเปซเหล่านี้จะให้การเข้าถึงฟังก์ชันที่จำเป็นสำหรับการจัดการไฟล์ 3D

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## กำลังโหลดและบันทึก - การใช้ CancellationToken

### ขั้นตอนที่ 1: สร้าง CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

ที่นี่ เราสร้างอินสแตนซ์ CancellationTokenSource ซึ่งเป็นองค์ประกอบสำคัญสำหรับการจัดการการยกเลิกในการดำเนินการแบบอะซิงโครนัส

### ขั้นตอนที่ 2: เริ่มต้นฉาก 3D

```csharp
Scene scene = new Scene();
```

สร้างอินสแตนซ์ของคลาส Scene นี่จะเป็นผืนผ้าใบสำหรับกิจกรรมการสร้างแบบจำลอง 3 มิติของคุณ

### ขั้นตอนที่ 3: ตั้งค่าการหมดเวลาของ CancellationToken

```csharp
cts.CancelAfter(1000);
```

 ตั้งค่าการหมดเวลาการยกเลิกโดยใช้`CancelAfter` วิธี. ในตัวอย่างนี้ การหมดเวลาถูกตั้งค่าเป็น 1,000 มิลลิวินาที (1 วินาที)

### ขั้นตอนที่ 4: เปิดเอกสาร 3 มิติ

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 พยายามเปิดเอกสาร 3 มิติภายในกรอบเวลาที่กำหนด ที่`cts.Token`พารามิเตอร์ช่วยให้แน่ใจว่าการดำเนินการสามารถยกเลิกได้หากเกินระยะหมดเวลาที่ตั้งไว้

### ขั้นตอนที่ 5: จัดการข้อยกเว้นการนำเข้า

ในกรณีของ ImportException ให้จัดการอย่างดีโดยตรวจสอบว่าเกิดจาก OperationCanceledException หรือไม่

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ตัวอย่าง: CancellationTokenSource
```

## บทสรุป

ยินดีด้วย! คุณได้สำรวจกระบวนการใช้ Aspose.3D สำหรับ .NET ด้วย CancellationToken เพื่อจัดการการโหลดเอกสาร 3D สำเร็จแล้ว เทคนิคนี้ช่วยให้มั่นใจได้ถึงการดำเนินการนำเข้าที่มีประสิทธิภาพและทันเวลา ซึ่งช่วยเพิ่มประสิทธิภาพโดยรวมของแอปพลิเคชัน 3D ของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: Aspose.3D เข้ากันได้กับไฟล์ 3D ทุกรูปแบบหรือไม่

 A1: Aspose.3D รองรับรูปแบบไฟล์ 3D ที่หลากหลาย รวมถึง FBX, STL, OBJ และอื่นๆ อ้างถึง[เอกสารประกอบ](https://reference.aspose.com/3d/net/) สำหรับรายการทั้งหมด

### คำถามที่ 2: ฉันจะรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร

 A2: รับใบอนุญาตชั่วคราวโดยการเยี่ยมชม[ลิงค์นี้](https://purchase.aspose.com/temporary-license/).

### คำถามที่ 3: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้ที่ไหน

 A3: เข้าร่วมการสนทนาของชุมชนที่[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18).

### คำถามที่ 4: ฉันสามารถทดลองใช้ Aspose.3D ฟรีก่อนซื้อได้หรือไม่

 A4: ใช่ สำรวจฟีเจอร์ต่างๆ พร้อมให้ทดลองใช้ฟรี[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 5: Aspose.3D สำหรับ .NET เวอร์ชันล่าสุดคืออะไร

 A5: ติดตามข่าวสารล่าสุดโดยการตรวจสอบ[หน้าดาวน์โหลด](https://releases.aspose.com/3d/net/) สำหรับรุ่นล่าสุด