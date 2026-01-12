---
date: 2026-01-12
description: เรียนรู้วิธีสร้างทรงกระบอกฐานตัดและวิธีส่งออกโมเดล 3D ในรูปแบบ OBJ ด้วย
  Aspose.3D สำหรับ .NET. ปฏิบัติตามคู่มือขั้นตอนต่อขั้นตอนนี้เพื่อเชี่ยวชาญการสร้างโมเดล
  3D.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: วิธีสร้างทรงกระบอกฐานตัดด้วย Aspose.3D สำหรับ .NET
url: /th/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ทรงกระบอกฐานตัดเฉือนที่กำหนดเอง

## บทนำ
ยินดีต้อนรับสู่คู่มือฉบับสมบูรณ์ของเรา ซึ่ง **you’ll learn how to create shear bottom cylinder** โมเดลด้วย Aspose.3D for .NET ไม่ว่าคุณจะสร้างสินทรัพย์เกม, ส่วนเครื่องกล, หรือการสาธิตภาพ, บทเรียนนี้จะแสดงให้คุณเห็นอย่างชัดเจนว่าจะรูปร่างฐานของทรงกระบอกอย่างไร, ใช้การตัดเฉือน, และสุดท้าย **export the 3D model OBJ** ไฟล์เพื่อใช้ในขั้นตอนต่อไปใด ๆ เราจะเดินผ่านแต่ละขั้นตอนด้วยกัน เพื่อให้คุณเริ่มผลิตเรขาคณิตที่กำหนดเองได้ในไม่กี่นาที

## คำตอบอย่างรวดเร็ว
- **What is a shear bottom cylinder?** ทรงกระบอกที่ใบหน้าต่ำของมันถูกเอียง (ตัดเฉือน) แทนที่จะเป็นแนวราบ  
- **Which library is used?** Aspose.3D for .NET  
- **How do I export the model?** ใช้ `scene.Save(..., FileFormat.WavefrontOBJ)`  
- **Do I need a license?** มีรุ่นทดลองให้ใช้; จำเป็นต้องมีใบอนุญาตเชิงพาณิชย์สำหรับการผลิต  
- **What prerequisites are required?** สภาพแวดล้อมการพัฒนา .NET และแพ็กเกจ NuGet ของ Aspose.3D  

## ทรงกระบอกฐานตัดเฉือนคืออะไร?
ทรงกระบอกฐานตัดเฉือนคือเมชทรงกระบอกมาตรฐานที่ใบหน้าต่ำถูกแปลงโดยการทำ shear ซึ่งช่วยให้คุณสร้างฐานเอียง, ทางลาด, หรือคอนเนคเตอร์ที่กำหนดเองโดยไม่ต้องแก้ไขเวอร์เท็กซ์ด้วยตนเอง

## ทำไมต้องใช้ Aspose.3D สำหรับงานนี้?
- **Full control**เหนือพารามิเตอร์ของรูปทรง (รัศมี, ความสูง, ส่วนแบ่ง)  
- **Built‑in shear support**ผ่านคุณสมบัติ `ShearBottom`, ช่วยคุณหลีกเลี่ยงการจัดการเมชระดับต่ำ  
- **One‑click export**ไปยังรูปแบบยอดนิยมเช่น OBJ, FBX, และ STL, ทำให้การรวมกับเครื่องมืออื่น ๆ ราบรื่น  

## ข้อกำหนดเบื้องต้น
- ความรู้พื้นฐานของ C# และ .NET  
- Aspose.3D for .NET ติดตั้งแล้ว คุณสามารถดาวน์โหลดได้ **[here](https://releases.aspose.com/3d/net/)**  
- IDE ที่เข้ากันได้กับ .NET (Visual Studio, Rider, หรือ VS Code)  

## นำเข้า Namespaces
ในไฟล์ C# ของคุณ, เริ่มต้นด้วยการนำเข้า namespaces ที่จำเป็น:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## ขั้นตอนที่ 1: สร้าง Scene
แรก, สร้างอินสแตนซ์ของ Scene 3‑D ใหม่ที่จะเก็บวัตถุทั้งหมดของเรา

```csharp
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: สร้าง Cylinder 1
สร้างทรงกระบอกหลักที่เราจะปรับแต่งด้วยฐานที่ตัดเฉือน

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## ขั้นตอนที่ 3: ปรับแต่ง Shear Bottom สำหรับ Cylinder 1
ใช้การตัดเฉือน, เปิดการสร้าง fan, และปรับคุณสมบัติอื่น ๆ เพื่อให้ได้รูปทรงที่ต้องการ

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## ขั้นตอนที่ 4: เพิ่ม Cylinder 1 ไปยัง Scene
วางทรงกระบอกที่ปรับแต่งแล้วใน Scene และเลื่อนมันเล็กน้อยไปทางขวาเพื่อให้เรามองเห็นวัตถุทั้งสองข้างกัน

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## ขั้นตอนที่ 5: สร้าง Cylinder 2
สร้างทรงกระบอกที่สอง, ธรรมดา, เพื่อเปรียบเทียบ

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## ขั้นตอนที่ 6: เพิ่ม Cylinder 2 ไปยัง Scene
เพิ่มทรงกระบอกที่สองโดยไม่มีการตัดเฉือนที่กำหนดเอง—สิ่งนี้ช่วยแสดงผลของขั้นตอนก่อนหน้า

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## ขั้นตอนที่ 7: บันทึก Scene
สุดท้าย, ส่งออก Scene ทั้งหมดเป็นไฟล์ OBJ เพื่อให้คุณสามารถเปิดใน Blender, Maya, หรือโปรแกรมดู 3‑D ใด ๆ

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## ปัญหาทั่วไปและเคล็ดลับ
- **Shear values**: `Vector2` รับค่าแฟกเตอร์การตัดเฉือน X และ Y. ค่า `0.83` ประมาณ 47.5°, แต่คุณสามารถปรับให้เป็นมุมอื่นได้  
- **Export path**: ตรวจสอบให้แน่ใจว่าโฟลเดอร์ที่ระบุมีอยู่และคุณมีสิทธิ์เขียน; มิฉะนั้น `scene.Save` จะโยนข้อยกเว้น  
- **Performance**: สำหรับทรงกระบอกที่มีส่วนแบ่งสูงมาก, พิจารณาลดจำนวนส่วน (`20` ในตัวอย่าง) เพื่อให้ขนาดไฟล์ OBJ จัดการได้  

## คำถามที่พบบ่อย

### Aspose.3D for .NET เหมาะสำหรับผู้เริ่มต้นหรือไม่?
แน่นอน! Aspose.3D for .NET มี API ที่เป็นมิตรต่อผู้ใช้ ทำให้เข้าถึงได้ทั้งผู้เริ่มต้นและนักพัฒนาที่มีประสบการณ์

### ฉันสามารถใช้มุมการตัดเฉือนที่ต่างกันกับทรงกระบอกได้หรือไม่?
ได้, คุณสามารถปรับแต่ง `ShearBottom` สำหรับแต่ละทรงกระบอกแยกกัน เพื่อให้ได้เอฟเฟกต์ที่เป็นเอกลักษณ์

### มีเวอร์ชันทดลองหรือไม่?
มี, คุณสามารถสำรวจเวอร์ชันทดลองฟรี **[here](https://releases.aspose.com/)**

### ฉันจะหาแหล่งสนับสนุนเพิ่มเติมได้จากที่ไหน?
เยี่ยมชม **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** เพื่อรับการสนับสนุนจากชุมชนและการสนทนาต่าง ๆ

### ฉันจะขอรับใบอนุญาตชั่วคราวได้อย่างไร?
รับใบอนุญาตชั่วคราว **[here](https://purchase.aspose.com/temporary-license/)**

**คำถามเพิ่มเติม**

**Q: How do I change the export format to FBX?**  
A: Replace `FileFormat.WavefrontOBJ` with `FileFormat.FBX` in the `scene.Save` call.

**Q: Can I animate the cylinder after exporting?**  
A: OBJ does not support animation; use FBX or GLTF if you need animated data.

**Q: What if I need a larger cylinder radius?**  
A: Adjust the first two parameters of the `Cylinder` constructor (e.g., `new Cylinder(4, 4, …)`).

## สรุป
คุณได้เรียนรู้วิธี **create shear bottom cylinder** โมเดลและส่งออกเป็นไฟล์ OBJ ด้วย Aspose.3D for .NET แล้ว ทดลองใช้ค่า shear ที่ต่างกัน, จำนวนส่วน, และรูปแบบการส่งออกเพื่อให้ตรงกับความต้องการของโครงการของคุณ ขอให้สนุกกับการสร้างโมเดล!

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}