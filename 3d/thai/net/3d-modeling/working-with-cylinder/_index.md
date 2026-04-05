---
date: 2026-03-26
description: เรียนรู้วิธีสร้างทรงกระบอกและส่งออกไฟล์ OBJ ด้วย Aspose.3D สำหรับ .NET
  คู่มือสำหรับผู้เริ่มต้นนี้ครอบคลุมการตั้งค่าฉาก 3 มิติและการส่งออก OBJ
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: วิธีสร้างทรงกระบอกพร้อมฐานตัดเฉือน – Aspose.3D สำหรับ .NET
url: /th/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีสร้างทรงกระบอกพร้อมฐานเชียร์ – Aspose.3D สำหรับ .NET

## บทนำ
หากคุณกำลังสงสัย **วิธีสร้างทรงกระบอก** ที่มีฐานเชียร์แบบกำหนดเองในสภาพแวดล้อม .NET คุณมาถูกที่แล้ว ในบทเรียนนี้เราจะพาคุณผ่านทุกขั้นตอน—from การตั้งค่า 3‑D scene ไปจนถึงการส่งออกโมเดลสุดท้ายเป็นไฟล์ OBJ—เพื่อให้คุณพัฒนาทักษะ *การสร้างโมเดล 3D ระดับเริ่มต้น* ของคุณด้วย **Aspose.3D for .NET**.

## คำตอบด่วน
- **คลาสหลักที่ใช้เริ่มต้นโมเดล 3D คืออะไร?** `Scene` สร้างคอนเทนเนอร์รากสำหรับเรขาคณิตทั้งหมด.  
- **เมธอดใดที่ใช้ส่งออกโมเดลเป็น OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **ฉันต้องการไลเซนส์สำหรับการทดสอบหรือไม่?** มีการทดลองใช้ฟรี — ดูลิงก์ทดลองใน FAQ.  
- **ฉันสามารถเปลี่ยนมุมเชียร์ได้หรือไม่?** ได้, ปรับ `ShearBottom` ด้วยค่า `Vector2`.  
- **เหมาะสำหรับผู้เริ่มต้นหรือไม่?** แน่นอน; API จะทำให้การจัดการเมชระดับต่ำเป็นนามธรรม.

## 3D Scene คืออะไร?
*3D scene* คือคอนเทนเนอร์แบบลำดับชั้นที่บรรจุเอนทิตีเรขาคณิตทั้งหมด, แสง, กล้อง, และการแปลง. ใน Aspose.3D คลาส `Scene` ให้วิธีที่สะอาดในการจัดระเบียบและส่งออกโมเดลของคุณในภายหลัง.

## ทำไมต้องส่งออกเป็น OBJ?
OBJ เป็นฟอร์แมตแบบข้อความที่ได้รับการสนับสนุนอย่างกว้างขวางและหลายแอปพลิเคชัน 3‑D (Blender, Maya, Unity) สามารถนำเข้าได้ การส่งออกเป็น OBJ ทำให้คุณสามารถแชร์หรือแก้ไขโมเดลทรงกระบอกของคุณต่อได้นอก .NET.

## ข้อกำหนดเบื้องต้น
- ความรู้พื้นฐานเกี่ยวกับ C# และการพัฒนา .NET.  
- **Aspose.3D for .NET** ติดตั้งแล้ว – คุณสามารถดาวน์โหลดได้ **[here](https://releases.aspose.com/3d/net/)**.  
- IDE ของ .NET (Visual Studio, Rider, หรือ VS Code) พร้อมสำหรับการเขียนโค้ด.

## นำเข้า Namespaces
ขั้นแรก นำ namespaces ที่จำเป็นเข้ามาในสโคปเพื่อให้ประเภทของ API ถูกจดจำ.

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

## ขั้นตอนที่ 1: สร้าง 3D Scene
อ็อบเจกต์ `Scene` ทำหน้าที่เป็นรากของลำดับชั้นโมเดลของคุณ.

```csharp
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: สร้าง Cylinder 1
เราจะสร้างทรงกระบอกแรกด้วยรัศมี 2, ความสูง 10, และ 20 ส่วนรัศมี.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## ขั้นตอนที่ 3: ปรับแต่ง Shear Bottom สำหรับ Cylinder 1
ใช้การแปลงเชียร์, เปิดใช้งานการสร้าง fan‑cylinder, และปรับคุณสมบัติอื่น ๆ เพื่อให้ได้รูปทรงที่ต้องการ.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## ขั้นตอนที่ 4: เพิ่ม Cylinder 1 ลงใน Scene
วางทรงกระบอกแรกในตำแหน่งที่สะดวกโดยใช้การแปลงการย้ายตำแหน่ง.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## ขั้นตอนที่ 5: สร้าง Cylinder 2
ทรงกระบอกที่สองถูกสร้างด้วยมิติฐานเดียวกันแต่ไม่มีการเชียร์แบบกำหนดเอง—เหมาะสำหรับการเปรียบเทียบเคียงข้างกัน.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## ขั้นตอนที่ 6: เพิ่ม Cylinder 2 ลงใน Scene
เราจะเชื่อมต่อทรงกระบอกที่สองเข้ากับกราฟของ scene อย่างง่ายดาย.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## ขั้นตอนที่ 7: ส่งออก Scene เป็นไฟล์ OBJ
สุดท้าย เราจะบันทึก scene ทั้งหมดเป็นไฟล์ OBJ เพื่อให้สามารถเปิดได้ในโปรแกรมดู 3‑D มาตรฐานใด ๆ.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## ปัญหาที่พบบ่อยและวิธีแก้
| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|----------|
| **ไฟล์ OBJ ว่างเปล่า** | Scene ไม่มีเรขาคณิตใด ๆ ถูกแนบ. | ตรวจสอบให้แน่ใจว่าทั้งสองทรงกระบอกถูกเพิ่มไปยัง `scene.RootNode`. |
| **เชียร์ดูผิด** | `ShearBottom` ต้องการค่าแทนเจนต์ของมุม. | ใช้ `Math.Tan(angleInRadians)` หรือค่า `0.83` ที่ให้ไว้สำหรับประมาณ 47.5°. |
| **ข้อผิดพลาดของเส้นทางไฟล์** | ไดเรกทอรีไม่ถูกต้องหรือหายไป. | ใช้ `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## คำถามที่พบบ่อย
### Aspose.3D for .NET เหมาะสำหรับผู้เริ่มต้นหรือไม่?
แน่นอน! Aspose.3D for .NET มี API ระดับสูงที่ทำให้ส่วนที่คณิตศาสตร์ซับซ้อนของการสร้างโมเดล 3‑D เป็นนามธรรม ทำให้เข้าถึงได้สำหรับนักพัฒนาที่มีทักษะระดับใดก็ได้.

### ฉันสามารถใช้มุมเชียร์ที่ต่างกันกับทรงกระบอกได้หรือไม่?
ได้, แต่ละอินสแตนซ์ของ `Cylinder` มีคุณสมบัติ `ShearBottom` ของตนเอง, ดังนั้นคุณสามารถกำหนดมุมที่แตกต่างให้กับแต่ละอ็อบเจกต์ได้.

### มีเวอร์ชันทดลองหรือไม่?
มี, คุณสามารถสำรวจเวอร์ชันทดลองฟรี **[here](https://releases.aspose.com/)**.

### ฉันจะหาแหล่งสนับสนุนเพิ่มเติมได้จากที่ไหน?
เยี่ยมชม **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** เพื่อรับความช่วยเหลือจากชุมชน, ตัวอย่างโค้ด, และการสนทนา.

### ฉันจะขอรับไลเซนส์ชั่วคราวได้อย่างไร?
รับไลเซนส์ชั่วคราวของคุณ **[here](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q: ฉันจะส่งออกโมเดลในฟอร์แมตอื่น เช่น STL ได้อย่างไร?**  
A: แทนที่ `FileFormat.WavefrontOBJ` ด้วย `FileFormat.STL` ในการเรียก `scene.Save`.

**Q: ฉันสามารถทำแอนิเมชันให้กับทรงกระบอกหลังจากสร้างได้หรือไม่?**  
A: ได้, คุณสามารถเพิ่มแอนิเมชันแบบคีย์เฟรมให้กับการแปลงของโหนดโดยใช้คลาส `Animation` ที่ Aspose.3D จัดให้.

**Q: API รองรับ .NET Core หรือไม่?**  
A: ไลบรารีนี้เข้ากันได้อย่างเต็มที่กับ .NET Core, .NET 5+, และ .NET 6+.

---

**อัปเดตล่าสุด:** 2026-03-26  
**ทดสอบด้วย:** Aspose.3D for .NET (รุ่นล่าสุด)  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}