---
title: การโหลดและการบันทึก - ตัวเลือกการโหลดแบบกำหนดเอง
linktitle: การโหลดและการบันทึก - ตัวเลือกการโหลดแบบกำหนดเอง
second_title: Aspose.3D .NET API
description: สำรวจ Aspose.3D สำหรับ .NET ซึ่งเป็นโซลูชันขั้นสูงสุดสำหรับการโหลดและบันทึกโมเดล 3 มิติที่ราบรื่น
type: docs
weight: 15
url: /th/net/loading-and-saving/custom-load-options/
---
## การแนะนำ

ยินดีต้อนรับสู่โลกของ Aspose.3D สำหรับ .NET – ไลบรารีอันทรงพลังที่ช่วยให้นักพัฒนาสามารถทำงานกับไฟล์ 3D ได้อย่างราบรื่น ในบทช่วยสอนนี้ เราจะเจาะลึกความซับซ้อนของการโหลดและบันทึกโมเดล 3 มิติ โดยเน้นที่ตัวเลือกการโหลดแบบกำหนดเอง ไม่ว่าคุณจะเป็นนักพัฒนาที่มีประสบการณ์หรือเป็นมือใหม่ คู่มือนี้จะแนะนำคุณตลอดกระบวนการทีละขั้นตอน เพื่อให้มั่นใจว่าคุณจะได้ใช้ประโยชน์จากศักยภาพของ Aspose.3D สำหรับ .NET ได้อย่างเต็มที่

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มต้นการเดินทางนี้ ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับ .NET: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารีแล้ว คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/net/).

- ไดเร็กทอรีเอกสาร: สร้างไดเร็กทอรีเพื่อจัดเก็บไฟล์โมเดล 3 มิติของคุณ

ตอนนี้คุณมีสิ่งที่จำเป็นแล้ว มาดำดิ่งสู่โลกแห่งการจัดการโมเดล 3 มิติที่น่าตื่นเต้นกันเถอะ!

## นำเข้าเนมสเปซ

ก่อนอื่น มานำเข้าเนมสเปซที่จำเป็นกันก่อน นี่จะเป็นการปูทางสำหรับการเดินทางของเราสู่อาณาจักร Aspose.3D

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## การโหลดและการบันทึก - ตัวเลือกการโหลดแบบกำหนดเอง

### ขั้นตอนที่ 1: กำลังโหลดไฟล์ Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    // เส้นทางไปยังไดเร็กทอรีเอกสาร
    string dataDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //ตั้งค่าตัวเลือกแบบกำหนดเอง
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### ขั้นตอนที่ 2: กำลังโหลดไฟล์ OBJ

```csharp
private static void ObjLoadOption()
{
    // เส้นทางไปยังไดเร็กทอรีเอกสาร
    string dataDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //ตั้งค่าตัวเลือกแบบกำหนดเอง
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### ขั้นตอนที่ 3: กำลังโหลดไฟล์ STL

```csharp
private static void STLLoadOption()
{
    // เส้นทางไปยังไดเร็กทอรีเอกสาร
    string dataDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //ตั้งค่าตัวเลือกแบบกำหนดเอง
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### ขั้นตอนที่ 4: กำลังโหลดไฟล์ U3D

```csharp
private static void U3DLoadOption()
{
    // เส้นทางไปยังไดเร็กทอรีเอกสาร
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //ตั้งค่าตัวเลือกแบบกำหนดเอง
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### ขั้นตอนที่ 5: กำลังโหลดไฟล์ glTF

```csharp
private static void glTFLoadOptions()
{
    // เส้นทางไปยังไดเร็กทอรีเอกสาร
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //ตั้งค่าตัวเลือกแบบกำหนดเอง
    loadOpt.FlipTexCoordV = true;
    scene.Open(dataDir + "Duck.gltf", loadOpt);
}
```

### ขั้นตอนที่ 6: กำลังโหลดไฟล์ PLY

```csharp
private static void PlyLoadOptions()
{
    // เส้นทางไปยังไดเร็กทอรีเอกสาร
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //ตั้งค่าตัวเลือกแบบกำหนดเอง
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open(RunExamples.GetDataFilePath("vase-v2.ply"), loadPLYOpts);
}
```

### ขั้นตอนที่ 7: กำลังโหลดไฟล์ FBX

```csharp
private static void FBXLoadOptions()
{
    // เส้นทางไปยังไดเร็กทอรีเอกสาร
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //ตั้งค่าตัวเลือกแบบกำหนดเอง
    scene.Open(dataDir + "test.FBX", opt);

    // คุณสมบัติเอาต์พุตที่กำหนดใน GlobalSettings ในไฟล์ FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## บทสรุป

ยินดีด้วย! คุณประสบความสำเร็จในการท่องโลกที่ซับซ้อนของการโหลดและบันทึกโมเดล 3 มิติโดยใช้ Aspose.3D สำหรับ .NET บทช่วยสอนนี้ครอบคลุมถึงรูปแบบไฟล์ที่หลากหลายและตัวเลือกการโหลดแบบกำหนดเอง ซึ่งช่วยให้คุณจัดการเนื้อหา 3 มิติได้อย่างง่ายดาย

## คำถามที่พบบ่อย

### คำถามที่ 1: Aspose.3D สำหรับ .NET เหมาะสำหรับผู้เริ่มต้นหรือไม่

A1: แน่นอน! Aspose.3D สำหรับ .NET มีอินเทอร์เฟซที่ใช้งานง่าย ทำให้นักพัฒนาทุกระดับสามารถเข้าถึงได้

### คำถามที่ 2: ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่

ตอบ 2: ใช่ Aspose.3D สำหรับ .NET มาพร้อมกับใบอนุญาตเชิงพาณิชย์ ซึ่งทำให้คุณสามารถใช้ในโครงการของคุณได้

### คำถามที่ 3: มีข้อจำกัดเกี่ยวกับรูปแบบไฟล์ที่รองรับหรือไม่

 A3: Aspose.3D สำหรับ .NET รองรับรูปแบบไฟล์ 3D ยอดนิยมที่หลากหลาย รวมถึง OBJ, STL, FBX และอื่นๆ อ้างถึง[เอกสารประกอบ](https://reference.aspose.com/3d/net/) สำหรับรายการที่ครอบคลุม

### คำถามที่ 4: มีเวอร์ชันทดลองใช้งานหรือไม่

A4: ได้ คุณสามารถสำรวจความสามารถของ Aspose.3D สำหรับ .NET ได้ด้วยการดาวน์โหลด[ทดลองฟรี](https://releases.aspose.com/).

### คำถามที่ 5: ฉันจะขอรับการสนับสนุนสำหรับ Aspose.3D สำหรับ .NET ได้ที่ไหน

A5: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและช่วยเหลือชุมชน