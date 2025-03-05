---
title: ตัวเลือกการบันทึกแบบกำหนดเอง
linktitle: ตัวเลือกการบันทึกแบบกำหนดเอง
second_title: Aspose.3D .NET API
description: สำรวจพลังของ Aspose.3D สำหรับ .NET เรียนรู้วิธีปรับแต่งการบันทึกฉาก 3D ของคุณด้วยคำแนะนำทีละขั้นตอนในรูปแบบ Collada, USD, 3DS, FBX, OBJ, STL, U3D, glTF, DRC และ RVM
type: docs
weight: 21
url: /th/net/loading-and-saving/custom-save-options/
---
## การแนะนำ

ยินดีต้อนรับสู่โลกของ Aspose.3D สำหรับ .NET! หากคุณต้องการเพิ่มขีดความสามารถในการพัฒนา 3D คุณมาถูกที่แล้ว ในบทช่วยสอนนี้ เราจะเจาะลึกเกี่ยวกับฟังก์ชันการโหลดและการบันทึก โดยเน้นไปที่ตัวเลือกการบันทึกแบบกำหนดเองโดยเฉพาะ Aspose.3D สำหรับ .NET เป็นไลบรารีอันทรงพลังที่ช่วยให้นักพัฒนาจัดการและบันทึกฉาก 3D ได้อย่างมีประสิทธิภาพ

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มสำรวจคุณสมบัติที่น่าตื่นเต้นของ Aspose.3D ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นดังต่อไปนี้:

- ความเข้าใจพื้นฐานเกี่ยวกับการพัฒนา C# และ .NET
-  ติดตั้ง Aspose.3D สำหรับไลบรารี .NET แล้ว คุณสามารถดาวน์โหลดได้จาก[หน้าปล่อย](https://releases.aspose.com/3d/net/).
- สภาพแวดล้อมการพัฒนาที่ตั้งค่าด้วย Visual Studio หรือ C# IDE ที่ต้องการอื่นๆ

## นำเข้าเนมสเปซ

ในการเริ่มต้น ให้นำเข้าเนมสเปซที่จำเป็น:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

ตอนนี้เราได้กำหนดขั้นตอนแล้ว เรามาแบ่งบทแนะนำออกเป็นหลายขั้นตอนกัน

## ขั้นตอนที่ 1: ตัวเลือกบันทึก Collada

เริ่มจาก Collada ซึ่งเป็นรูปแบบไฟล์ 3 มิติยอดนิยมกันก่อน ทำตามขั้นตอนเหล่านี้เพื่อปรับแต่งตัวเลือกการบันทึก Collada:

### 1. ตั้งค่าไดเรกทอรี:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. เริ่มต้นตัวเลือกการบันทึก Collada:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. กำหนดค่าตัวเลือก:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## ขั้นตอนที่ 2: ตัวเลือกการบันทึก Discreet 3DS

ตอนนี้ เรามาสำรวจ Discreet 3DS และตัวเลือกการปรับแต่งต่างๆ กัน:

### 1. ตั้งค่าไดเรกทอรี:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. เริ่มต้นตัวเลือกการบันทึก 3DS:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. กำหนดค่าตัวเลือก:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // ตัวเลือกการกำหนดค่าเพิ่มเติม...
   ```

ดำเนินการตามแนวทางทีละขั้นตอนนี้ต่อไปสำหรับตัวเลือกการบันทึก FBX, OBJ, STL, U3D, glTF และ DRC โดยปรับแต่งแต่ละรายการตามความต้องการของคุณ

## ขั้นตอนที่ 3: ตัวเลือกการบันทึก glTF

ตอนนี้ เรามาเน้นที่ glTF ซึ่งเป็นรูปแบบที่ใช้กันอย่างแพร่หลายในเว็บและแอปพลิเคชันบนมือถือ ปรับแต่งตัวเลือกการบันทึก glTF ของคุณด้วยขั้นตอนเหล่านี้:

### 1. เริ่มต้นวัตถุฉาก:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. ตั้งค่าตัวเลือกการบันทึก glTF:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. บันทึกไฟล์ glTF:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

ปฏิบัติตามโครงสร้างที่คล้ายกันสำหรับตัวเลือกการบันทึกอื่นๆ เช่น DRC และ RVM

## บทสรุป

ยินดีด้วย! คุณได้สำรวจตัวเลือกการบันทึกแบบกำหนดเองใน Aspose.3D สำหรับ .NET สำเร็จแล้ว ไลบรารีอันทรงพลังนี้มีตัวเลือกมากมายเพื่อปรับแต่งกระบวนการบันทึกฉาก 3 มิติของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ .NET กับเฟรมเวิร์ก .NET อื่นๆ ได้หรือไม่

ตอบ 1: ใช่ Aspose.3D เข้ากันได้กับเฟรมเวิร์ก .NET ต่างๆ ทำให้มั่นใจได้ถึงความยืดหยุ่นในสภาพแวดล้อมการพัฒนาของคุณ

### คำถามที่ 2: มีตัวเลือกสิทธิ์การใช้งานสำหรับ Aspose.3D หรือไม่

 ตอบ 2: ได้ คุณสามารถสำรวจตัวเลือกใบอนุญาตได้[ที่นี่](https://purchase.aspose.com/buy).

### คำถามที่ 3: ฉันจะรับการสนับสนุนสำหรับการสืบค้นที่เกี่ยวข้องกับ Aspose.3D ได้ที่ไหน

 A3: คุณสามารถขอรับการสนับสนุนได้ที่[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18).

### คำถามที่ 4: มีการทดลองใช้ฟรีหรือไม่?

 A4: ได้ คุณสามารถทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 5: ฉันจะรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร

 A5: รับใบอนุญาตชั่วคราว[ที่นี่](https://purchase.aspose.com/temporary-license/).