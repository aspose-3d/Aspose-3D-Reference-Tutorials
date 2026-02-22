---
date: 2026-02-22
description: เรียนรู้วิธีสร้างการดันออก 3 มิติพร้อมชั้นโดยใช้ Aspose.3D สำหรับ Java
  คู่มือแบบทีละขั้นตอนนี้ครอบคลุมการดันออกเชิงเส้น การตั้งค่ารัศมีโค้งมน และการส่งออกเป็น
  OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: สร้างการดึงออก 3 มิติด้วยชั้น – Aspose.3D สำหรับ Java
url: /th/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# สร้าง 3D Extrusion ด้วย Slices – Aspose.3D for Java

## คำแนะนำ

หากคุณต้องการ **create 3d extrusion** ที่ดูเรียบเนียนและแม่นยำ การควบคุมจำนวน slices คือกุญแจสำคัญ ในบทแนะนำนี้เราจะอธิบายวิธีการระบุ slices ขณะทำ linear extrusion ด้วย Aspose.3D for Java คุณจะเห็นว่าทำไมจำนวน slice ถึงสำคัญ วิธีตั้งค่ารัศมีการโค้งมน และวิธีส่งออกผลลัพธ์เป็นไฟล์ OBJ ที่สามารถใช้ในสายงาน 3D ใดก็ได้

## คำตอบอย่างรวดเร็ว
- **What does “slices” control?** จำนวน cross‑section กลางที่ใช้ประมาณพื้นผิว extrusion  
- **Which method sets the slice count?** `LinearExtrusion.setSlices(int)`  
- **Can I change the rounding radius of the profile?** ได้โดยใช้ `RectangleShape.setRoundingRadius(double)`  
- **What file format is used in this example?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Do I need a license to run the code?** สามารถใช้ trial ฟรีเพื่อประเมินผลได้; ต้องมี license เชิงพาณิชย์สำหรับการใช้งานจริง

## การ Extrusion เชิงเส้นด้วย slices คืออะไร?

Linear extrusion รับโปรไฟล์ 2‑D (เช่นสี่เหลี่ยม) แล้วยืดออกตามเส้นตรงเพื่อสร้างวัตถุ 3‑D โดยการระบุ **slices** คุณบอก Aspose.3D ว่าต้องการขั้นตอนกลางกี่ขั้นตอน ซึ่งส่งผลโดยตรงต่อความเรียบของขอบโค้งเช่นสี่เหลี่ยมมุมโค้ง

## ทำไมต้องใช้ Aspose.3D for Java เพื่อสร้าง 3d extrusion?

* **Full control** – สามารถปรับจำนวน slice, รัศมีการโค้งมน, และรูปแบบการส่งออกได้โดยโปรแกรม  
* **Cross‑platform** – ทำงานได้บนทุกสภาพแวดล้อมที่รองรับ Java โดยไม่มีการพึ่งพา native library  
* **Export flexibility** – บันทึกโดยตรงเป็น OBJ, FBX, STL และรูปแบบอื่น ๆ มากมาย

## ข้อกำหนดเบื้องต้น

1. **Java Development Kit** – ติดตั้ง JDK 8 หรือสูงกว่า  
2. **Aspose.3D for Java** – ดาวน์โหลดไลบรารีจากเว็บไซต์อย่างเป็นทางการ [here](https://releases.aspose.com/3d/java/)  
3. IDE หรือโปรแกรมแก้ไขข้อความที่คุณชอบ

## นำเข้าแพ็กเกจ

เพิ่ม namespace ของ Aspose.3D ลงในโปรเจกต์ของคุณเพื่อให้เข้าถึงคลาสการสร้างโมเดล 3‑D

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## คู่มือขั้นตอน

### ขั้นตอน 1: ตั้งค่า scene และกำหนดโปรไฟล์

ก่อนอื่นเราจะสร้าง `RectangleShape` และกำหนด **rounding radius** เพื่อให้มุมเรียบ จากนั้นเราจะสร้าง `Scene` ใหม่เพื่อเก็บเรขาคณิตทั้งหมด

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### ขั้นตอน 2: **Create child node** objects for each extrusion

แต่ละชิ้นส่วนของเรขาคณิตจะอยู่ภายใต้ `Node` ที่นี่เราจะสร้าง node พี่น้องสองตัว – หนึ่งสำหรับ extrusion ที่มี slice ต่ำและอีกหนึ่งสำหรับ slice สูง – แล้วเลื่อน node ด้านซ้ายเล็กน้อยเพื่อให้เปรียบเทียบผลลัพธ์ได้ง่าย

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### ขั้นตอน 3: Perform linear extrusion and **set slices**

ต่อไปเราจะ **create 3d extrusion** จริง ๆ ตัวสร้าง `LinearExtrusion` รับโปรไฟล์และความลึกของ extrusion โดยใช้ **anonymous inner class** เราเรียก `setSlices` เพื่อควบคุมความเรียบของพื้นผิว Node ด้านซ้ายจะมีเพียง 2 slices (หยาบ) ส่วน Node ด้านขวาจะมี 10 slices (เรียบ)

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### ขั้นตอน 4: **Export OBJ** – save the scene

สุดท้ายเราจะบันทึก scene เป็นไฟล์ Wavefront OBJ ซึ่งเป็นรูปแบบที่ได้รับการสนับสนุนอย่างกว้างขวางโดยโปรแกรมแก้ไข 3‑D และเอนจินเกม การทำเช่นนี้แสดงความสามารถ **export obj java** ของ Aspose.3D

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## ปัญหาและวิธีแก้ไขทั่วไป

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|----------|
| **Extrusion appears flat** | ตั้งค่า slice count เป็น 1 หรือ 0 | ตรวจสอบให้ `setSlices` ถูกเรียกด้วยค่าที่ ≥ 2 |
| **Rounded corners look jagged** | รัศมีการโค้งมนเล็กเกินไปเมื่อเทียบกับจำนวน slice | เพิ่มรัศมีหรือเพิ่มจำนวน slice เพื่อให้เส้นโค้งเรียบขึ้น |
| **File not found on save** | `MyDir` ชี้ไปยังโฟลเดอร์ที่ไม่มีอยู่ | สร้างโฟลเดอร์ล่วงหน้าหรือใช้เส้นทางแบบ absolute |

## คำถามที่พบบ่อย

**Q: จะดาวน์โหลด Aspose.3D for Java ได้จากที่ไหน?**  
A: คุณสามารถดาวน์โหลดไลบรารีได้จาก [here](https://releases.aspose.com/3d/java/)

**Q: จะหาเอกสารอ้างอิงของ Aspose.3D ได้จากที่ไหน?**  
A: ดูเอกสารอ้างอิงได้ที่ [here](https://reference.aspose.com/3d/java/)

**Q: มี trial ฟรีให้ใช้หรือไม่?**  
A: มี คุณสามารถทดลองใช้ trial ฟรีได้จาก [here](https://releases.aspose.com/)

**Q: จะขอรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร?**  
A: เยี่ยมชมฟอรั่มสนับสนุนได้ที่ [here](https://forum.aspose.com/c/3d/18)

**Q: สามารถซื้อ license ชั่วคราวได้หรือไม่?**  
A: ได้ คุณสามารถขอรับ license ชั่วคราวได้จาก [here](https://purchase.aspose.com/temporary-license/)

**อัปเดตล่าสุด:** 2026-02-22  
**ทดสอบด้วย:** Aspose.3D for Java 24.11 (latest at time of writing)  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}