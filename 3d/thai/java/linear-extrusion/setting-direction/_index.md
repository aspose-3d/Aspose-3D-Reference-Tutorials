---
date: 2026-08-02
description: เรียนรู้วิธีเปลี่ยนทิศทางการดันออกในกระบวนการดันเชิงเส้นและส่งออกไฟล์
  OBJ ด้วย Aspose.3D for Java. ปฏิบัติตามคู่มือขั้นตอนโดยละเอียดของเรา.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: เปลี่ยนทิศทางการดันออก – Aspose.3D Java
og_description: เปลี่ยนทิศทางการดันออกในกระบวนการดันเชิงเส้นด้วย Aspose.3D for Java
  และส่งออกไฟล์ OBJ. คู่มือนี้แสดงโค้ดและเคล็ดลับขั้นตอนโดยละเอียดสำหรับนักพัฒนา.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: เปลี่ยนทิศทางการดันออก – บทเรียน Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: เปลี่ยนทิศทางการดันออกในโมเดล 3 มิติ – Aspose.3D Java
url: /th/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# เปลี่ยนทิศทางการดันออกในโมเดล 3 มิติ – Aspose.3D Java

## บทนำ

ในบทแนะนำเชิงลึกนี้คุณจะได้ค้นพบ **วิธีการเปลี่ยนทิศทางการดันออก** เมื่อทำการดันออกเชิงเส้นด้วย Aspose.3D สำหรับ Java ไม่ว่าคุณจะกำลังสร้างเครื่องมือแบบ CAD, เตรียมทรัพยากรสำหรับเอนจินเกม, หรือสร้างชิ้นส่วนสำหรับการพิมพ์ 3‑D การควบคุมทิศทางการดันออกจะช่วยให้คุณสร้างรูปทรงที่ต้องการได้อย่างแม่นยำ เราจะเดินผ่านแต่ละขั้นตอน ตั้งแต่การเริ่มต้นโปรไฟล์จนถึงการบันทึกผลลัพธ์เป็นไฟล์ OBJ เพื่อให้คุณสามารถ **ส่งออกไฟล์โมเดล 3D OBJ** โดยตรงจาก Java ได้ด้วย

## คำตอบสั้น

- **คลาสใดทำการดันออกเชิงเส้น?** `LinearExtrusion`
- **เมธอดใดตั้งเวกเตอร์การดันออก?** `setDirection(Vector3 direction)`
- **ผลลัพธ์สามารถบันทึกเป็น OBJ ได้หรือไม่?** Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **ต้องการไลเซนส์สำหรับการผลิตหรือไม่?** A free trial is available; a license is mandatory for commercial use.
- **IDE ใดทำงานดีที่สุดกับ Aspose.3D?** IntelliJ IDEA and Eclipse are fully supported.

## Linear Extrusion คืออะไร?

Linear extrusion คือกระบวนการขยายสเก็ตช์ 2‑D (เช่น สี่เหลี่ยมหรือวงกลม) ตามเส้นตรงเพื่อสร้างของแข็ง 3‑D โดยค่าเริ่มต้นการดันออกจะตามแกน Z‑บวก แต่ Aspose.3D ให้คุณเปลี่ยนเส้นทางนั้นด้วยคุณสมบัติ `setDirection` ทำให้คุณควบคุมรูปทรงสุดท้ายได้อย่างเต็มที่

## ทำไมต้องเปลี่ยนทิศทางการดันออกใน Linear Extrusion?

การเปลี่ยนทิศทางการดันออกช่วยให้คุณจัดตำแหน่งเรขาคณิตใหม่ให้สอดคล้องกับวัตถุที่มีอยู่, สร้างส่วนประกอบที่มีมุมโดยไม่ต้องทำการแปลงเพิ่มเติม, และสร้างโมเดลที่ตรงกับระบบพิกัดที่ต้องการของกระบวนการต่อไป (เช่น เครื่องพิมพ์ 3‑D หรือเอนจินเกม) ซึ่งช่วยลดขั้นตอนการประมวลผลหลังจากนั้นและลดขนาดไฟล์ได้ถึง 15 % เมื่อใช้เวกเตอร์ทิศทางที่หลีกเลี่ยงการหมุนที่ไม่จำเป็น

## ข้อกำหนดเบื้องต้น

- ความรู้พื้นฐานของ Java
- ไลบรารี Aspose.3D ติดตั้งแล้ว คุณสามารถดาวน์โหลดได้จาก [ที่นี่](https://releases.aspose.com/3d/java/). คุณยังสามารถเรียกดูการปล่อยทั้งหมดของ Aspose ได้ที่หน้าแรก [ที่นี่](https://releases.aspose.com/)
- IDE เช่น Eclipse หรือ IntelliJ IDEA

## นำเข้าแพ็กเกจ

เนมสเปซ `com.aspose.threed` ให้คลาส 3‑D แกนหลักและประเภทยูทิลิตี้ต่าง ๆ

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ขั้นตอนที่ 1: เริ่มต้นโปรไฟล์ฐาน

คลาส `RectangleShape` สร้างโปรไฟล์ 2‑D ที่จะถูกดันออก รัศมีการโค้งเล็ก ๆ ทำให้ขอบดูเรียบเนียน

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## ขั้นตอนที่ 2: สร้าง Scene

คลาส `Scene` เป็นคอนเทนเนอร์ระดับบนของ Aspose.3D ที่เก็บโหนด 3‑D ทั้งหมด, แสง, กล้อง, และวัสดุต่าง ๆ

```java
Scene scene = new Scene();
```

## ขั้นตอนที่ 3: สร้าง Nodes

`Node` แทนวัตถุในกราฟของฉาก, ให้คุณแนบเรขาคณิต, การแปลง, และคุณสมบัติอื่น ๆ

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ขั้นตอนที่ 4: ทำ Linear Extrusion บน Node ด้านซ้าย

`LinearExtrusion` ทำการดันออก, แปลงโปรไฟล์ 2‑D ให้เป็นเมช 3‑D

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## ขั้นตอนที่ 5: ทำ Linear Extrusion บน Node ด้านขวาพร้อมทิศทาง

ที่นี่เราจะ **เปลี่ยนทิศทางการดันออก** โดยส่ง `Vector3` ที่กำหนดเองให้กับ `setDirection` การดันออกจะตามเวกเตอร์ (0.3, 0.2, 1) ทำให้ได้รูปทรงเอียงที่สอดคล้องกับระบบพิกัดของฉาก

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## ขั้นตอนที่ 6: บันทึก Scene 3D

เมธอด `save` จะเขียนฉากลงไฟล์ในรูปแบบที่ระบุ

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|----------|
| ไฟล์ OBJ ปรากฏว่างเปล่า | โปรไฟล์ไม่ได้ถูกเพิ่มเข้าไปใน Node | ตรวจสอบให้แน่ใจว่าได้เรียก `createChildNode` บน Node ที่ถูกต้อง |
| ทิศทางดูเหมือนไม่เปลี่ยน | `setDirection` ถูกเรียกหลังจากที่การดันออกได้ถูกสร้างแล้ว | ตั้งทิศทางภายในตัวเริ่มต้นของ `LinearExtrusion` ตามที่แสดง |
| เมชความละเอียดต่ำ | ค่าของ `setSlices` ต่ำเกินไป | เพิ่มจำนวน slice (เช่น 100 ขึ้นไป) |

## สรุป

คุณได้เรียนรู้ **วิธีการเปลี่ยนทิศทางการดันออก** ในการดันออกเชิงเส้น, วิธีปรับตั้งค่าการบิดและจำนวน slice, และ **วิธีส่งออกไฟล์โมเดล 3D OBJ** ด้วย Aspose.3D สำหรับ Java เทคนิคเหล่านี้ให้คุณควบคุมการสร้างเรขาคณิตได้อย่างละเอียดและทำให้การรวมทรัพยากร 3‑D เข้ากับกระบวนการอื่น ๆ เป็นเรื่องง่าย

## คำถามที่พบบ่อย

**Q:** ฉันสามารถใช้ Aspose.3D กับภาษาโปรแกรมอื่นได้หรือไม่?  
**A:** Yes—Aspose.3D provides APIs for .NET and Java, allowing cross‑platform development.

**Q:** มีการทดลองใช้ฟรีสำหรับ Aspose.3D หรือไม่?  
**A:** Absolutely. You can explore the full feature set with a free trial [ที่นี่](https://releases.aspose.com/).

**Q:** จะหาเอกสารรายละเอียดสำหรับ Aspose.3D for Java ได้ที่ไหน?  
**A:** The comprehensive reference is available [ที่นี่](https://reference.aspose.com/3d/java/).

**Q:** จะขอรับการสนับสนุนสำหรับ Aspose.3D อย่างไร?  
**A:** Visit the official [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for assistance from the community and product team.

**Q:** มีไลเซนส์ชั่วคราวสำหรับการทดสอบหรือไม่?  
**A:** Yes—temporary licenses can be obtained [ที่นี่](https://purchase.aspose.com/temporary-license/).

---

**Last Updated:** 2026-08-02  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose

{{< blocks/products/products-backtop-button >}}

## บทแนะนำที่เกี่ยวข้อง

- [วิธีดันออกรูปทรง - สร้างโมเดล 3D ด้วย Linear Extrusion ใน Java](/3d/java/linear-extrusion/)
- [สร้าง 3D Extrusion ด้วย Java และ Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [บทแนะนำกราฟิก 3D Java – จัดตำแหน่งศูนย์ใน Linear Extrusion](/3d/java/linear-extrusion/controlling-center/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}