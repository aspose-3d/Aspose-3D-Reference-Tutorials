---
date: 2025-12-18
description: เรียนรู้วิธีการดึงรูปทรงใน Java ด้วย Aspose.3D, สร้างฉาก 3 มิติ, และส่งออกไฟล์
  Wavefront OBJ อย่างง่ายดาย.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: วิธีดึงรูปทรงใน Java ด้วย Aspose.3D Linear Extrusion
url: /th/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การทำ Linear Extrusion ใน Aspose.3D สำหรับ Java

## คำนำ

ยินดีต้อนรับสู่บทแนะนำฉบับเต็มเกี่ยวกับ **วิธีการ extrude shape** ใน Aspose.3D สำหรับ Java! หากคุณต้องการพัฒนาทักษะการสร้างโมเดล 3 มิติด้วย Java คุณมาถูกที่แล้ว เราจะพาคุณผ่านการสร้างฉาก 3 มิติ, การทำ linear extrusion, และการส่งออกผลลัพธ์เป็นไฟล์ Wavefront OBJ พร้อมตัวอย่างโค้ดที่ชัดเจนเป็นขั้นตอน

## คำตอบสั้น ๆ
- **Linear extrusion คืออะไร?** การขยายโปรไฟล์ 2 มิติไปตามเส้นทางตรงเพื่อสร้างวัตถุ 3 มิติ  
- **ไลบรารีใดจัดการเรื่องนี้ใน Java?** Aspose.3D สำหรับ Java  
- **สามารถส่งออกเป็น OBJ ได้หรือไม่?** ได้, โดยใช้ฟีเจอร์การส่งออก Wavefront OBJ  
- **ต้องใช้ไลเซนส์สำหรับการพัฒนาหรือไม่?** สามารถใช้เวอร์ชันทดลองฟรีสำหรับการทดสอบ; ต้องมีไลเซนส์สำหรับการใช้งานจริง  
- **ต้องใช้ Java เวอร์ชันใด?** Java 1.6 หรือใหม่กว่า

## “how to extrude shape” คืออะไร?
Linear extrusion เป็นเทคนิคพื้นฐานใน **3d modeling java** ที่เปลี่ยนโปรไฟล์แบน—เช่นสี่เหลี่ยมผืนผ้า—ให้เป็นวัตถุที่มีปริมาณโดยการดึงมันตามระยะที่กำหนด วิธีนี้ใช้กันอย่างแพร่หลายสำหรับการสร้างชิ้นส่วนเครื่องกล, องค์ประกอบสถาปัตยกรรม, และโมเดลตกแต่ง

## ทำไมต้องใช้ Aspose.3D สำหรับ linear extrusion?
- **ควบคุมเต็มรูปแบบ** บนรูปทรงเรขาคณิต (slices, twist, offset)  
- **ผสานรวมอย่างไร้รอยต่อ** กับโครงการ Java—ไม่มีการพึ่งพา native dependencies  
- **มีตัวส่งออกในตัว** สำหรับฟอร์แมตยอดนิยมรวมถึง Wavefront OBJ ทำให้ง่ายต่อการ **generate 3d model** สำหรับ pipeline ต่อไป

## ข้อกำหนดเบื้องต้น

ก่อนจะเริ่มทำตามบทแนะนำนี้ โปรดตรวจสอบว่าคุณมีสิ่งต่อไปนี้พร้อมแล้ว:

1. **สภาพแวดล้อมการพัฒนา Java** – JDK (1.6 หรือใหม่กว่า) และ IDE ที่คุณชอบ  
2. **ไลบรารี Aspose.3D** – ดาวน์โหลดและติดตั้งไลบรารีจากเว็บไซต์อย่างเป็นทางการ **[ที่นี่](https://releases.aspose.com/3d/java/)**

## นำเข้าแพ็กเกจ

หลังจากตั้งค่าสภาพแวดล้อมการพัฒนาและติดตั้งไลบรารี Aspose.3D แล้ว ให้นำเข้าแพ็กเกจที่จำเป็น:

```java
import com.aspose.threed.*;
```

### ขั้นตอนที่ 1: กำหนดไดเรกทอรีเอกสาร

ระบุตำแหน่งโฟลเดอร์ที่ไฟล์ที่สร้างขึ้นจะถูกบันทึก:

```java
String MyDir = "Your Document Directory";
```

> สิ่งนี้ทำให้แน่ใจว่าการทำงาน **generate 3d model** จะเขียนไฟล์ OBJ ไปยังตำแหน่งที่ทราบ

### ขั้นตอนที่ 2: เริ่มต้นรูปทรงฐาน

สร้างสี่เหลี่ยมผืนผ้าที่จะใช้เป็นโปรไฟล์สำหรับ extrusion:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

คุณสามารถปรับรัศมีของการโค้งเพื่อให้ได้มุมที่โค้งมนหรือกำหนดเป็น `0` เพื่อให้ได้สี่เหลี่ยมที่คมชัด

### ขั้นตอนที่ 3: ทำ Linear Extrusion

ตอนนี้เราจะทำการ extrude สี่เหลี่ยมไปตามแกน Z, เพิ่ม slices, เปิดการจัดศูนย์, และใส่ twist พร้อม offset:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **ความยาว extrusion** – `10` หน่วย  
- **Slices** – `100` เพื่อให้เรขาคณิตเรียบเนียน  
- **Twist** – `360°` ทำการหมุนเต็มรอบ  
- **Twist offset** – ย้ายจุดเริ่มต้นของ twist ไปที่ `(10, 0, 0)`

### ขั้นตอนที่ 4: สร้าง 3D Scene

สร้างคอนเทนเนอร์ฉากและเพิ่ม extrusion เป็นโหนดลูก ขั้นตอนนี้ **creates 3d scene** ที่สามารถบรรจุหลายวัตถุได้:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### ขั้นตอนที่ 5: บันทึก 3D Scene

ส่งออกฉากเป็นไฟล์ Wavefront OBJ ซึ่งแสดงความสามารถของ **wavefront obj export** และ **save 3d obj**:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

หลังจากรันโค้ด คุณจะพบไฟล์ `LinearExtrusion.obj` ในไดเรกทอรีที่คุณระบุไว้ พร้อมเปิดในโปรแกรมดู 3 มิติใด ๆ หรือทำการประมวลผลต่อ

## ปัญหาทั่วไปและวิธีแก้

| Issue | Reason | Fix |
|-------|--------|-----|
| ไฟล์ OBJ ว่างเปล่า | เส้นทางไดเรกทอรีเอาต์พุตไม่ถูกต้องหรือไม่มีสิทธิ์เขียน | ตรวจสอบว่า `MyDir` ชี้ไปยังโฟลเดอร์ที่มีอยู่และมีสิทธิ์เขียน |
| Twist ไม่ทำงาน | ลืมเรียก `setCenter(true)` | ตรวจสอบให้เปิดการจัดศูนย์หรือปรับค่าของ `setTwistOffset` |
| เกิดข้อผิดพลาดในการคอมไพล์ที่ `LinearExtrusion` | ใช้เวอร์ชัน Aspose.3D เก่า | อัปเดตเป็นเวอร์ชันล่าสุดของ Aspose.3D |

## คำถามที่พบบ่อย

**Q: Aspose.3D รองรับ Java เวอร์ชันทั้งหมดหรือไม่?**  
A: Aspose.3D ทำงานกับ Java 1.6 และใหม่กว่า

**Q: สามารถใช้ Aspose.3D ในโครงการเชิงพาณิชย์ได้หรือไม่?**  
A: ได้, การใช้งานเชิงพาณิชย์ได้รับอนุญาตเมื่อมีไลเซนส์ที่ถูกต้อง คุณสามารถรับไลเซนส์ได้ **[ที่นี่](https://purchase.aspose.com/buy)**

**Q: จะหาการสนับสนุนได้จากที่ไหนหากเจอปัญหา?**  
A: เยี่ยมชม **[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18)**ขอความช่วยเหลือจากชุมชน หรือซื้อ **[ไลเซนส์ชั่วคราว](https://purchase.aspose.com/temporary-license/)** เพื่อรับการสนับสนุนระดับพรีเมียม

**Q: Aspose.3D มีฟีเจอร์การโมเดล 3 มิติอื่น ๆ อะไรบ้าง?**  
A: ไลบรารีนี้รวมถึงการจัดการเมช, การทำ Boolean, การแมปพื้นผิว, และอื่น ๆ ดูรายการเต็มได้ **[ที่นี่](https://reference.aspose.com/3d/java/)**

**Q: มีเวอร์ชันทดลองฟรีหรือไม่?**  
A: มี, คุณสามารถดาวน์โหลดเวอร์ชันทดลอง **[ที่นี่](https://releases.aspose.com/)**

## สรุป

คุณได้เรียนรู้ **วิธีการ extrude shape** ด้วย Aspose.3D สำหรับ Java, สร้าง 3D scene, และส่งออกผลลัพธ์เป็นไฟล์ Wavefront OBJ เทคนิคนี้เปิดประตูสู่โครงการ **3d modeling java** หลากหลาย ตั้งแต่ชิ้นส่วนง่าย ๆ ไปจนถึงการประกอบที่ซับซ้อน ลองสำรวจฟีเจอร์เพิ่มเติมเช่นการทำ Boolean หรือการแมปพื้นผิวเพื่อเพิ่มความสมบูรณ์ให้กับโมเดลของคุณ

---

**อัปเดตล่าสุด:** 2025-12-18  
**ทดสอบกับ:** Aspose.3D 24.11 for Java  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## คำหลักเป้าหมาย:

**คีย์เวิร์ดหลัก (ความสำคัญสูงสุด):**  
how to extrude shape  

**คีย์เวิร์ดรอง (สนับสนุน):**  
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj