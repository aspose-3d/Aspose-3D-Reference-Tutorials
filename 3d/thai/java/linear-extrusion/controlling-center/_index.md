---
date: 2026-02-20
description: เรียนบทแนะนำกราฟิก 3 มิติใน Java เกี่ยวกับการควบคุมศูนย์กลางในการดึงเชิงเส้นด้วย
  Aspose.3D รวมถึงวิธีตั้งค่ารัศมีการโค้งและการบันทึกไฟล์ OBJ ใน Java.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: บทเรียนกราฟิก 3 มิติ Java – ศูนย์กลางในการดึงเชิงเส้น
url: /th/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Graphics Tutorial – การจัดศูนย์ใน Linear Extrusion

## บทนำ

หากคุณกำลังสร้างการแสดงผล 3 มิติใน Java การเชี่ยวชาญเทคนิคการ extrusion เป็นสิ่งสำคัญ บทเรียน **java 3d graphics tutorial** นี้จะพาคุณผ่านการควบคุมศูนย์ของ linear extrusion ด้วย Aspose.3D for Java เพื่อให้คุณสร้างโมเดลที่แม่นยำและสมมาตรโดยไม่ต้องคำนวณเพิ่มเติม เมื่อจบคู่มือนี้คุณจะเข้าใจว่าทำไมคุณสมบัติ `center` ถึงสำคัญ วิธี **set rounding radius** และวิธี **save OBJ file java**‑compatible output

## คำตอบสั้นๆ
- **คุณสมบัติ center ทำอะไร?** มันกำหนดว่าการ extrusion จะสมมาตรรอบจุดกำเนิดของโปรไฟล์หรือไม่.  
- **ต้องการใบอนุญาตเพื่อรันโค้ดหรือไม่?** ใบอนุญาตชั่วคราวใช้ได้สำหรับการทดสอบ; ใบอนุญาตเต็มจำเป็นสำหรับการใช้งานจริง.  
- **รูปแบบไฟล์ที่ใช้สำหรับผลลัพธ์คืออะไร?** ฉากจะถูกบันทึกเป็นไฟล์ Wavefront OBJ.  
- **ฉันสามารถเปลี่ยนจำนวน slices ได้หรือไม่?** ได้, ใช้ `setSlices(int)` บนวัตถุ `LinearExtrusion`.  
- **Aspose.3D รองรับ Java 8+ หรือไม่?** แน่นอน – รองรับเวอร์ชัน Java สมัยใหม่ทั้งหมด.

## java 3d graphics tutorial คืออะไร?

บทเรียน **java 3d graphics tutorial** อธิบายขั้นตอนโดยละเอียดว่าใช้ไลบรารี Java เพื่อสร้าง, ปรับแต่ง, และเรนเดอร์วัตถุสามมิติอย่างไร ในกรณีนี้เราจะเน้นที่ API extrusion ของ Aspose.3D ซึ่งเปลี่ยนโปรไฟล์ 2‑D ให้เป็นเมช 3‑D อย่างเต็มรูปแบบ

## ทำไมต้องใช้ Aspose.3D for Java?

- **High‑level API** – ไม่จำเป็นต้องเขียนการคำนวณ mesh ระดับต่ำ.  
- **Cross‑format support** – ส่งออกเป็น OBJ, FBX, STL และอื่นๆ.  
- **Performance‑optimized** – จัดการฉากขนาดใหญ่ได้อย่างมีประสิทธิภาพ.  
- **Rich documentation** – มีตัวอย่างเช่นด้านล่างนี้.

## ข้อกำหนดเบื้องต้น

1. **Java Development Environment** – ติดตั้ง JDK 8 หรือใหม่กว่า.  
2. **Aspose.3D for Java** – ดาวน์โหลดไลบรารีและเอกสาร [ที่นี่](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – สร้างโฟลเดอร์บนเครื่องของคุณเพื่อเก็บไฟล์ที่สร้าง; เราจะเรียกมันว่า **“Your Document Directory.”**

## นำเข้าแพ็กเกจ

ใน IDE ของ Java ของคุณ ให้นำเข้าคลาส Aspose.3D ที่จำเป็น ซึ่งจะทำให้คอมไพเลอร์เข้าถึงฟีเจอร์ extrusion และการสร้างฉาก

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## คู่มือขั้นตอนต่อขั้นตอน

### ขั้นตอนที่ 1: ตั้งค่า Base Profile

แรกสุด สร้างรูปทรง 2‑D ที่จะทำการ extrusion ที่นี่เราใช้สี่เหลี่ยมและ **set rounding radius** เป็น 0.3 เพื่อทำให้มุมเรียบ

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### ขั้นตอนที่ 2: สร้าง 3D Scene

อ็อบเจ็กต์ `Scene` ทำหน้าที่เป็นคอนเทนเนอร์สำหรับโหนด 3‑D, แสง, และกล้องทั้งหมด

```java
Scene scene = new Scene();
```

### ขั้นตอนที่ 3: เพิ่มโหนดซ้ายและขวา

เราจะวางโหนดสองอันแยกกันเคียงข้างกันเพื่อให้คุณเปรียบเทียบ extrusion ที่มีและไม่มีการจัดศูนย์

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### ขั้นตอนที่ 4: Linear Extrusion – ไม่มีศูนย์ (โหนดซ้าย)

สร้าง extrusion บนโหนดซ้าย ปิดการจัดศูนย์ และจำกัด mesh ให้มีสาม slices เพื่อดูตัวอย่าง low‑poly

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### ขั้นตอนที่ 5: เพิ่ม Ground Plane เพื่ออ้างอิง (โหนดซ้าย)

กล่องบางๆ ทำหน้าที่เป็นพื้นมองเห็น ช่วยให้คุณเห็นทิศทางของ extrusion

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### ขั้นตอนที่ 6: Linear Extrusion – จัดศูนย์ (โหนดขวา)

ตอนนี้ทำการ extrusion อีกครั้ง โดยเปิด `center`. รูปร่างจะสมมาตรรอบจุดกำเนิดของโปรไฟล์

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### ขั้นตอนที่ 7: เพิ่ม Ground Plane เพื่ออ้างอิง (โหนดขวา)

ใช้ Ground Plane เดียวกันสำหรับด้านขวา ทำให้การเปรียบเทียบชัดเจน

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### ขั้นตอนที่ 8: บันทึก 3D Scene

สุดท้าย ส่งออกฉากทั้งหมดเป็นไฟล์ Wavefront OBJ – รูปแบบที่ใช้ได้ง่ายในโปรแกรมแก้ไข 3‑D ส่วนใหญ่

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|----------|
| **การ Extrusion แสดงผลลอยออก** | `setCenter(false)` ทำให้โปรไฟล์ถูกยึดที่มุมของมัน. | ใช้ `setCenter(true)` เพื่อให้ได้ผลลัพธ์สมมาตร. |
| **ไฟล์ OBJ ว่างเปล่า** | เส้นทางไดเรกทอรีเอาต์พุตไม่ถูกต้องหรือไม่มีสิทธิ์เขียน. | ตรวจสอบว่า `MyDir` ชี้ไปยังโฟลเดอร์ที่มีอยู่และแอปพลิเคชันมีสิทธิ์เขียน. |
| **มุมที่ทำให้โค้งดูคมเกินไป** | รัศมีการโค้งเล็กเกินไปเมื่อเทียบกับขนาดสี่เหลี่ยม. | เพิ่มค่ารัศมี (เช่น `setRoundingRadius(0.5)`). |

## คำถามที่พบบ่อย

### Q1: ฉันสามารถใช้ Aspose.3D for Java ในโครงการเชิงพาณิชย์ได้หรือไม่?

A1: ใช่, Aspose.3D for Java มีให้ใช้ในเชิงพาณิชย์ สำหรับรายละเอียดการให้สิทธิ์ ดูที่ [ที่นี่](https://purchase.aspose.com/buy).

### Q2: มีรุ่นทดลองฟรีหรือไม่?

A2: ใช่, คุณสามารถทดลองใช้ Aspose.3D for Java ฟรีได้ที่ [ที่นี่](https://releases.aspose.com/).

### Q3: ฉันจะหาแหล่งสนับสนุนสำหรับ Aspose.3D for Java ได้จากที่ไหน?

A3: ฟอรั่มชุมชน Aspose.3D เป็นสถานที่ที่ดีในการขอความช่วยเหลือและแบ่งปันประสบการณ์ของคุณ เยี่ยมชมฟอรั่มได้ที่ [ที่นี่](https://forum.aspose.com/c/3d/18).

### Q4: ฉันต้องการใบอนุญาตชั่วคราวสำหรับการทดสอบหรือไม่?

A4: ใช่, หากคุณต้องการใบอนุญาตชั่วคราวเพื่อการทดสอบ คุณสามารถรับได้ที่ [ที่นี่](https://purchase.aspose.com/temporary-license/).

### Q5: ฉันจะหาเอกสารได้จากที่ไหน?

A5: เอกสารสำหรับ Aspose.3D for Java มีให้ที่ [ที่นี่](https://reference.aspose.com/3d/java/).

## สรุป

โดยการทำให้เสร็จสิ้น **java 3d graphics tutorial** นี้ คุณจะรู้วิธีควบคุมศูนย์ของ linear extrusion, ปรับรัศมีการโค้ง, และ **save OBJ file java** output ด้วย Aspose.3D เทคนิคเหล่านี้ให้การควบคุมละเอียดของสมมาตร mesh ซึ่งสำคัญสำหรับทรัพยากรเกม, ตัวอย่าง CAD, และการแสดงผลทางวิทยาศาสตร์. อย่าลังเลที่จะทดลองกับโปรไฟล์ต่างๆ, จำนวน slices, และรูปแบบการส่งออกเพื่อขยายเครื่องมือ 3‑D ของคุณ.

---

**อัปเดตล่าสุด:** 2026-02-20  
**ทดสอบด้วย:** Aspose.3D for Java 24.11  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}