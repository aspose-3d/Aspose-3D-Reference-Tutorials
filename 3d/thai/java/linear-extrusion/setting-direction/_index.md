---
date: 2025-12-18
description: เรียนรู้วิธีสร้างฉาก 3 มิติและบันทึกไฟล์ OBJ ด้วย Aspose.3D สำหรับ Java.
  ปฏิบัติตามคู่มือขั้นตอนต่อขั้นตอนของเราสำหรับทิศทางการดึงเส้นตรง.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: สร้างฉาก 3 มิติ – ตั้งค่าทิศทางการดึง Aspose.3D Java
url: /th/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# สร้าง 3D Scene – ตั้งค่าทิศทาง Extrusion Aspose.3D Java

## บทนำ

ในบทแนะนำนี้คุณจะได้เรียนรู้ **วิธีสร้าง 3d scene** objects และควบคุมทิศทาง extrusion ด้วย Aspose.3D สำหรับ Java ไม่ว่าคุณจะสร้างการแสดงผลสถาปัตยกรรม, ตัวอย่างผลิตภัณฑ์, หรือทรัพยากรเกม การเชี่ยวชาญ linear extrusion จะให้ความยืดหยุ่นในการสร้างรูปทรงซับซ้อนได้อย่างรวดเร็ว เราจะอธิบายทุกขั้นตอน ตั้งแต่การเพิ่ม nodes ใน Java ไปจนถึง **export 3d model obj** files เพื่อให้คุณเห็นผลลัพธ์ทันที

## คำตอบด่วน
- **“create 3d scene” หมายถึงอะไร?** หมายถึงการเริ่มต้นวัตถุ Aspose.3D `Scene` ที่จะเก็บเรขาคณิตทั้งหมด, แสง, และกล้อง.  
- **ฉันจะค่าทิศทาง extrusion อย่างไร?** ใช้เมธอด `setDirection(Vector3)` บนอินสแตนซ์ `LinearExtrusion`.  
- **ฉันควรใช้รูปแบบใดในการส่งออก?** รูปแบบ OBJ (`FileFormat.WAVEFRONTOBJ`) ได้รับการสนับสนุนอย่างกว้างขวางสำหรับเวิร์กโฟลว์ 3‑D.  
- **ฉันต้องการไลเซนส์สำหรับ Aspose.3D หรือไม่?** การทดลองใช้งานฟรีใช้ได้สำหรับการพัฒนา; จำเป็นต้องมีไลเซนส์เชิงพาณิชย์สำหรับการผลิต.  
- **ฉันสามารถเพิ่ม nodes เพิ่มเติมใน Java ได้หรือไม่?** ได้ — ใช้ `scene.getRootNode().createChildNode()` เพื่อเพิ่มวัตถุตามต้องการ.

## “create 3d scene” workflow คืออะไร?

Workflow **create 3d scene** เริ่มต้นด้วยวัตถุ `Scene` ว่าง, เพิ่มเรขาคณิต (เช่นโปรไฟล์ที่ extrusion), กำหนดตำแหน่งด้วยการแปลง, และสุดท้ายบันทึก scene เป็นรูปแบบไฟล์เช่น OBJ. รูปแบบนี้เป็นโครงสร้างหลักของแอปพลิเคชัน 3‑D ส่วนใหญ่ที่สร้างด้วย Asp.3D.

## ทำไมต้องตั้งค่าทิศทาง extrusion?

การตั้งค่าทิศทาง extrusion จะทำให้คุณเอียง, หมุน, หรือบิดรูปทรงขณะ extrusion, ให้คุณควบคุมเรขาคณิตสุดท้ายโดยไม่ต้องทำการประมวลผลต่อภายหลัง. มีประโยชน์เป็นพิเศษสำหรับ:
- สร้างคอลัมน์ทรงแคบหรือท่อรูปร่างกำหนดเอง
- จัดแนว extrusion กับแกนที่ไม่เป็นมาตรฐานในชิ้นส่วนเครื่องกล
- สร้างรูปทรงศิลปะสำหรับเอฟเฟกต์ภาพ

## ข้อกำหนดเบื้องต้น

- ความรู้พื้นฐาน Java  
- ติดตั้งไลบรารี Aspose.3D – ดาวน์โหลดได้จาก [here](https://releases.aspose.com/3d/java/).  
- IDE เช่น Eclipse หรือ IntelliJ IDEA

## นำเข้า Packages

ก่อนอื่นให้นำเข้าคลาส Aspose.3D ที่จำเป็น:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ขั้นตอนที่ 1: เริ่มต้น Base Profile

สร้างโปรไฟล์ 2‑D ที่จะถูก extrusion. ในตัวอย่างนี้เราใช้สี่เหลี่ยมมุมโค้ง:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **เคล็ดลับ:** ปรับรัศมีการโค้งเพื่อควบคุมว่ามุมสี่เหลี่ยมจะคมหรือเรียบก่อน extrusion.

## ขั้นตอนที่ 2: สร้าง Scene

ตอนนี้เราจะ **สร้าง 3d scene** ที่จะเป็นโฮสต์สำหรับวัตถุของเรา:

```java
Scene scene = new Scene();
```

## ขั้นตอนที่ 3: เพิ่ม Nodes Java – การจัดตำแหน่งวัตถุ

เราจะเพิ่มสอง child node (ซ้ายและขวา) ไปยัง root node ของ scene และย้าย node ซ้ายเล็กน้อยไปด้านข้าง:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ขั้นตอนที่ 4: วิธีการ extrude – Node ซ้าย (ทิศทางเริ่มต้น)

Extrude โปรไฟล์บน node ซ้ายโดยใช้ทิศทางแกน Z เริ่มต้น. เรายังตั้งการบิดเต็ม 360° และเพิ่มจำนวน slice เพื่อความเรียบเนียน:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## ขั้นตอนที่ 5: วิธีการตั้งค่าทิศทาง – Node ขวา

ที่นี่เราจะ **how to set direction** โดยให้ค่า `Vector3` ที่กำหนดเอง. ค่าดังกล่าวจะเอียง extrusion ไปยังเวกเตอร์ (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## ขั้นตอนที่ 6: บันทึกไฟล์ OBJ – ส่งออกโมเดล 3D

สุดท้ายเราจะ **save obj file** เพื่อดูผลลัพธ์ในโปรแกรมดู 3‑D ใดก็ได้:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

เมื่อคุณเปิดไฟล์ OBJ ที่สร้างขึ้น, คุณจะเห็นสี่เหลี่ยม extrusion สองรูป: หนึ่งรูปที่ใช้ทิศทางเริ่มต้นและอีกหนึ่งรูปที่เอียงตามเวกเตอร์ที่ตั้งค่าไว้.

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|-----|
| ไฟล์ OBJ ปรากฏว่าง | Scene ไม่ได้บันทึกหรือเส้นทางไม่ถูกต้อง | ตรวจสอบว่า `MyDir` ชี้ไปยังโฟลเดอร์ที่สามารถเขียนได้และชื่อไฟล์ลงท้ายด้วย `.obj`. |
| Extrusion ดูแบน | `setSlices` ต่ำเกินไป | เพิ่มค่า `setSlices` (เช่น 200) เพื่อให้เรขาคณิตเรียบเนียนขึ้น. |
| ทิศทางดูเหมือนไม่เปลี่ยนแปลง | Vector ไม่ได้ทำการ normalize | ใช้ `Vector3` ที่ทำการ normalize หรือปรับค่าตามที่ต้องการเพื่อให้ได้การเอียงที่ต้องการ. |

## คำถามที่พบบ่อย

### Q1: ฉสามารถใช้ Aspose.3D กับภาษาโปรแกรมอื่นได้หรือไม่?
A1: Aspose.3D รองรับหลายภาษา รวมถึง .NET และ Java.

### Q2: มีการทดลองใช้ฟรีสำหรับ Aspose.3D หรือไม่?
A2: มี คุณสามารถสำรวจคุณสมบัติของ Aspose.3D ด้วยการทดลองใช้ฟรี [here](https://releases.aspose.com/).

### Q3: ฉันจะหาเอกสารรายละเอียดสำหรับ Aspose.3D สำหรับ Java ได้จากที่ไหน?
A3: เอกสารที่ครอบคลุมสามารถเข้าถึงได้ [here](https://reference.aspose.com/3d/java/).

### Q4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D อย่างไร?
A4: เยี่ยมชม [Aspose.3D forum](https://forum.aspose.com/c/3d/18) เพื่อขอความช่วยเหลือหรือสอบถาม.

### Q5: มีไลเซนส์ชั่วคราวสำหรับ Aspose.3D หรือไม่?
A5: มี คุณสามารถขอรับไลเซนส์ชั่วคราวได้ [here](https://purchase.aspose.com/temporary-license/).

---

**อัปเดตล่าสุด:** 2025-12-18  
**ทดสอบกับ:** Aspose.3D 24.11 for Java  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}