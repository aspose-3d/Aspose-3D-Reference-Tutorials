---
date: 2026-02-22
description: เรียนรู้วิธีตั้งทิศทางในการดันเชิงเส้นและส่งออกโมเดล 3D ในรูปแบบ OBJ
  ด้วย Aspose.3D สำหรับ Java. ปฏิบัติตามคู่มือขั้นตอนโดยละเอียดของเรา.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: วิธีตั้งทิศทางในการดึงเชิงเส้นด้วย Aspose.3D สำหรับ Java
url: /th/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีตั้งทิศทางในการ Extrusion แบบเชิงเส้นด้วย Aspose.3D สำหรับ Java

## บทนำ

ในบทแนะนำฉบับเต็มนี้คุณจะได้เรียนรู้ **วิธีตั้งทิศทาง** เมื่อทำการ Extrusion แบบเชิงเส้นด้วย Aspose.3D สำหรับ Java ไม่ว่าคุณจะกำลังสร้างเครื่องมือแบบ CAD‑like หรือสร้างเรขาคณิตสำหรับเอนจินเกม การควบคุมทิศทางของ Extrusion จะช่วยให้คุณสร้างรูปทรงที่ต้องการได้อย่างแม่นยำ เราจะเดินผ่านแต่ละขั้นตอน ตั้งแต่การกำหนดโปรไฟล์จนถึงการบันทึกผลลัพธ์เป็นไฟล์ OBJ เพื่อให้คุณสามารถ **ส่งออกไฟล์โมเดล 3d obj** โดยตรงจาก Java ได้

## คำตอบสั้น
- **คลาสหลักสำหรับการ Extrusion แบบเชิงเส้นคืออะไร?** `LinearExtrusion`
- **เมธอดใดที่กำหนดทิศทางของ Extrusion?** `setDirection(Vector3 direction)`
- **ฉันสามารถส่งออกผลลัพธ์เป็น OBJ ได้หรือไม่?** ได้ โดยใช้ `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **ต้องมีลิขสิทธิ์สำหรับการพัฒนาหรือไม่?** มีรุ่นทดลองฟรี; จำเป็นต้องมีลิขสิทธิ์สำหรับการใช้งานในผลิตภัณฑ์
- **IDE ของ Java ตัวใดเหมาะที่สุด?** IntelliJ IDEA หรือ Eclipse ทั้งสองรองรับเต็มที่

## Linear Extrusion คืออะไร?

Linear extrusion คือการนำโปรไฟล์ 2‑D (เช่น สี่เหลี่ยมหรือวงกลม) มาขยายตามเส้นตรงเพื่อสร้างของแข็ง 3‑D โดยค่าเริ่มต้นการ Extrusion จะตามแกน Z‑บวก แต่ Aspose.3D ให้คุณเปลี่ยนเส้นทางนั้นได้ด้วยคุณสมบัติ `setDirection`

## ทำไมต้องตั้งทิศทางใน Linear Extrusion?

การตั้งทิศทางที่กำหนดเองมีประโยชน์เมื่อ:
- จัดตำแหน่งเรขาคณิตให้สอดคล้องกับวัตถุที่มีอยู่ในฉาก
- สร้างชิ้นส่วนที่เอียงหรือมีมุมโดยไม่ต้องทำขั้นตอนการแปลงเพิ่มเติม
- ส่งออกโมเดลที่ต้องตรงกับระบบพิกัดเฉพาะ (เช่น สำหรับการพิมพ์ 3‑D หรือเอนจินเกม)

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มทำตามขั้นตอน โปรดตรวจสอบว่าคุณมี:

- ความรู้พื้นฐานของ Java
- ไลบรารี Aspose.3D ติดตั้งแล้ว คุณสามารถดาวน์โหลดได้จาก [here](https://releases.aspose.com/3d/java/)
- IDE เช่น Eclipse หรือ IntelliJ IDEA

## การนำเข้าแพ็กเกจ

เริ่มต้นด้วยการนำเข้า namespace ที่ให้คลาส 3‑D หลักและประเภทยูทิลิตี้ต่าง ๆ

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ขั้นตอนที่ 1: กำหนดโปรไฟล์พื้นฐาน

สร้างรูปทรงที่จะทำการ Extrude ตัวอย่างนี้เราใช้ `RectangleShape` พร้อมรัศมีการโค้งเล็กน้อยเพื่อให้ขอบเรียบ

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## ขั้นตอนที่ 2: สร้าง Scene

อ็อบเจ็กต์ `Scene` ทำหน้าที่เป็นคอนเทนเนอร์สำหรับโหนด 3‑D ทั้งหมด, แสง, กล้อง และวัสดุต่าง ๆ

```java
Scene scene = new Scene();
```

## ขั้นตอนที่ 3: สร้างโหนด

เพิ่มโหนดลูกสองโหนดลงในรูทของ Scene — โหนดหนึ่งสำหรับ Extrusion ด้านซ้ายและอีกโหนดหนึ่งสำหรับ Extrusion ด้านขวา โหนดด้านขวาจะถูกแปลตำแหน่งเพื่อไม่ให้สองวัตถุทับกัน

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ขั้นตอนที่ 4: ทำ Linear Extrusion บนโหนดซ้าย

Extrude โปรไฟล์บนโหนดซ้ายโดยใช้ทิศทางแกน Z‑บวกค่าเริ่มต้น เราเพิ่มการบิด 360° เต็มรอบและเพิ่มจำนวน slice เพื่อให้เมชเรียบขึ้น

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## ขั้นตอนที่ 5: ทำ Linear Extrusion บนโหนดขวาพร้อมตั้งทิศทาง

นี่คือจุดที่เราจะ **ตั้งทิศทาง** โดยการส่ง `Vector3` ที่กำหนดเองให้กับ `setDirection` ทำให้การ Extrusion ตามเวกเตอร์ (0.3, 0.2, 1) ผลลัพธ์เป็นรูปทรงเอียง

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## ขั้นตอนที่ 6: บันทึก 3D Scene

สุดท้าย ส่งออก Scene ไปเป็นรูปแบบ Wavefront OBJ ขั้นตอนนี้แสดงวิธี **บันทึกไฟล์ obj ด้วย Java** ทำให้คุณสามารถดูผลลัพธ์ในโปรแกรมดู 3‑D ใดก็ได้

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|---------|
| ไฟล์ OBJ ว่างเปล่า | โปรไฟล์ไม่ได้ถูกเพิ่มเข้าโหนด | ตรวจสอบให้แน่ใจว่าได้เรียก `createChildNode` บนโหนดที่ถูกต้อง |
| ทิศทางไม่เปลี่ยนแปลง | `setDirection` ถูกเรียกหลังจาก Extrusion สร้างเสร็จแล้ว | ตั้งค่าทิศทางภายในตัวสร้าง `LinearExtrusion` ตามตัวอย่าง |
| เมชความละเอียดต่ำ | ค่า `setSlices` ต่ำเกินไป | เพิ่มจำนวน slice (เช่น 100 ขึ้นไป) |

## สรุป

คุณได้เรียนรู้ **วิธีตั้งทิศทาง** ใน Linear Extrusion, วิธีปรับค่า twist และ slice, และ **วิธีส่งออกไฟล์โมเดล 3d obj** ด้วย Aspose.3D สำหรับ Java เทคนิคเหล่านี้ให้การควบคุมรายละเอียดของการสร้างเรขาคณิตอย่างละเอียดและทำให้การรวมทรัพยากร 3‑D เข้ากับ pipeline ขนาดใหญ่เป็นเรื่องง่าย

## คำถามที่พบบ่อย

### Q1: สามารถใช้ Aspose.3D กับภาษาโปรแกรมอื่นได้หรือไม่?

A1: Aspose.3D รองรับหลายภาษาโปรแกรม รวมถึง .NET และ Java

### Q2. มีรุ่นทดลองฟรีสำหรับ Aspose.3D หรือไม่?

A2: มี คุณสามารถสำรวจคุณสมบัติของ Aspose.3D ด้วยรุ่นทดลองฟรีได้ที่ [here](https://releases.aspose.com/)

### Q3: จะหาเอกสารรายละเอียดของ Aspose.3D สำหรับ Java ได้จากที่ไหน?

A3: เอกสารฉบับเต็มพร้อมให้บริการที่ [here](https://reference.aspose.com/3d/java/)

### Q4: จะขอรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร?

A4: เยี่ยมชม [Aspose.3D forum](https://forum.aspose.com/c/3d/18) เพื่อขอความช่วยเหลือหรือสอบถามข้อมูล

### Q5: มีลิขสิทธิ์ชั่วคราวสำหรับ Aspose.3D หรือไม่?

A5: มี คุณสามารถขอรับลิขสิทธิ์ชั่วคราวได้ที่ [here](https://purchase.aspose.com/temporary-license/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**อัปเดตล่าสุด:** 2026-02-22  
**ทดสอบด้วย:** Aspose.3D for Java (รุ่นล่าสุด)  
**ผู้เขียน:** Aspose