---
date: 2025-11-30
description: เรียนรู้วิธีใช้ Aspose ใน Java เพื่อแก้ไขรัศมีของทรงกลม 3 มิติ คู่มือขั้นตอนต่อขั้นตอนนี้ครอบคลุมไลบรารี
  Aspose.3D Java วิธีตั้งค่ารัศมี การเพิ่มทรงกลมลงในฉาก และการเขียนไฟล์ OBJ ด้วย Java.
language: th
linktitle: 'How to Use Aspose: Modify 3D Sphere Radius in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'วิธีใช้ Aspose: ปรับขนาดรัศมีของทรงกลม 3 มิติใน Java ด้วย Aspose.3D'
url: /java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีใช้ Aspose: ปรับรัศมีของทรงกลม 3D ใน Java ด้วย Aspose.3D

## บทนำ

หากคุณกำลังมองหา **วิธีใช้ Aspose** เพื่อทำงานกับโมเดล 3D ใน Java คุณมาถูกที่แล้ว ในบทแนะนำนี้เราจะเดินผ่านทุกขั้นตอนที่จำเป็นเพื่อเปลี่ยนขนาดของทรงกลม, เพิ่มลงในซีน, และสุดท้ายเขียนไฟล์ OBJ ด้วย **Aspose.3D Java library** เมื่อ็จคุณจะได้สคริปต์ที่นำกลับมาใช้ใหม่ได้ซึ่งสามารถใส่ลงในแอปพลิเคชัน 3D ที่ใช้ Java ใดก็ได้

## คำตอบอย่างรวดเร็ว
- **วัตถุประสงค์หลักของคู่มือนี้คืออะไร?** เพื่อแสดงวิธีปรับรัศมีของทรงกลมด้วย Aspose.3D ใน Java.  
- **เราใช้ไลบรารีใด?** Aspose.3D Java library (ไลบรารี **java 3d** ที่ครบถ้วน).  
- **ฉันตั้งรัศมีอย่างไร?** เรียก `sphere.setRadius(double)` บนอ็อบเจกต์ `Sphere`.  
- **สามารถส่งออกเป็น OBJ ได้หรือไม่?** ได้ – ใช้ `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **ต้องมีลิขสิทธิ์หรือไม่?** รุ่นทดลองฟรีใช้ได้สำหรับการพัฒนา; ต้องมีลิขสิทธิ์สำหรับการใช้งานจริง.

## Aspose.3D สำหรับ Java คืออะไร?

Aspose.3D เป็น **java 3d library** ที่ช่วยให้นักพัฒนาสร้าง, แก้ไข, และแปลงไฟล์ 3D ได้โดยไม่ต้องพึ่งพาไลบรารีภายนอก รองรับฟอร์แมตยอดนิยมเช่น OBJ, FBX, STL, และอื่น ๆ ทำให้เหมาะสำหรับเกม, เครื่องมือ CAD, และการแสดงผลทางวิทยาศาสตร์

## ทำไมต้องใช้ Aspose.3D เพื่อเปลี่ยนขนาดทรงกลม?

- **ไม่ต้องใช้เอนจิน 3D เนทีฟ** – ทุกการดำเนินการทำบนโมเดลอ็อบเจกต์.  
- **ข้ามแพลตฟอร์ม** – ทำงานบน OS ใดก็ได้ที่รัน Java.  
- **เรขาคณิตความแม่นยำสูง** – สามารถตั้งค่ารัศมีที่แน่นอนได้, ไม่ใช่แค่การสเกลโดยประมาณ.  

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มทำงาน, โปรดตรวจสอบว่าคุณมี:

- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม Java.  
- ไลบรารี Aspose.3D ติดตั้งแล้ว – สามารถดาวน์โหลดได้จาก [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- Java Development Kit (JDK) ติดตั้งบนเครื่องคุณ.

## นำเข้าแพ็กเกจ

เพื่อเริ่มต้น, นำเข้าคลาสที่จำเป็นเข้าสู่โปรเจกต์ Java ของคุณ:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## ขั้นตอนที่ 1: เริ่มต้นซีน

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

ที่นี่เราสร้าง **ซีน 3D** ใหม่ที่จะเก็บเรขาคณิตทั้งหมดของเรา

## ขั้นตอนที่ 2: เริ่มต้นทรงกลม

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

อ็อบเจกต์ `Sphere` แทนทรงกลมพื้นฐาน ณ จุดนี้ใช้รัศมีเริ่มต้นที่ 1.0

## ขั้นตอนที่ 3: วิธีตั้งรัศมีของทรงกลม

```java
// set radius
sphere.setRadius(10);
```

บรรทัดนี้แสดง **วิธีตั้งรัศมี** คุณสามารถเปลี่ยน `10` เป็นค่า `double` ใดก็ได้ตามต้องการ

## ขั้นตอนที่ 4: เพิ่มทรงกลมลงในซีน

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

การเรียกนี้ **เพิ่มทรงกลมลงในซีน** (หรือ “add sphere to scene”) โดยสร้างโหนดลูกภายใต้โหนดราก

## ขั้นตอนที่ 5: เขียนไฟล์ OBJ ด้วย Java

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

สุดท้าย, เรา **เขียนไฟล์ OBJ** แบบ Java ด้วย `scene.save` ไฟล์ผลลัพธ์ `sphere.obj` สามารถเปิดได้ในโปรแกรมดู 3D ใดก็ได้ที่รองรับฟอร์แมต Wavefront OBJ

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | วิธีแก้ |
|-------|----------|
| **ทรงกลมแสดงผลเล็กเกินไปในโปรแกรมดู** | ตรวจสอบว่าค่ารัศมีตั้งค่าอย่างถูกต้อง; จำไว้ว่าหน่วยเป็นค่าอิสระจนกว่าจะใช้การแปลงสเกล. |
| **OBJ ที่ส่งออกไม่มีวัสดุ** | Aspose.3D จะเขียนเฉพาะเรขาคณิต; หากต้องการเทกซ์เจอร์ให้เพิ่มวัสดุให้กับทรงกลม (`sphere.setMaterial(...)`). |
| **ข้อยกเว้นลิขสิทธิ์ขณะรัน** | ตรวจสอบว่ามีไฟล์ลิขสิทธิ์ชั่วคราวหรือถาวรโหลดก่อนสร้าง `Scene`. |

## คำถามที่พบบ่อย

### ถ: ฉันจะหาเอกสารสำหรับ Aspose.3D for Java ได้จากที่ไหน?

ตอบ: คุณสามารถอ้างอิงที่ [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) สำหรับข้อมูลและแนวทางการใช้งานอย่างครบถ้วน

### ถ: ฉันจะดาวน์โหลด Aspose.3D for Java ได้อย่างไร?

ตอบ: ดาวน์โหลดไลบรารีจากหน้าปล่อยเวอร์ชัน: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/)

### ถ: มีรุ่นทดลองฟรีสำหรับ Aspose.3D for Java หรือไม่?

ตอบ: มี, คุณสามารถสำรวจคุณสมบัติต่าง ๆ ด้วยรุ่นทดลองฟรีโดยเยี่ยมชม [Aspose.3D Free Trial](https://releases.aspose.com/)

### ถ: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D for Java ได้จากที่ไหน?

ตอบ: เข้าร่วมชุมชน Aspose ที่ [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) เพื่อขอความช่วยเหลือและสนทนา

### ถ: ฉันจะขอรับลิขสิทธิ์ชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?

ตอบ: รับลิขสิทธิ์ชั่วคราวได้ที่ [Temporary License](https://purchase.aspose.com/temporary-license/)

### ถ: ฉันสามารถใช้โค้ดนี้กับฟอร์แมต 3D อื่น ๆ เช่น STL ได้หรือไม่?

ตอบ: แน่นอน – เพียงเปลี่ยนค่า enum `FileFormat` เมื่อเรียก `scene.save`, เช่น `FileFormat.STL`

## สรุป

คุณได้เรียนรู้ **วิธีใช้ Aspose** เพื่อปรับรัศมีของทรงกลม, เพิ่มลงในซีน, และส่งออกผลลัพธ์เป็นไฟล์ OBJ ใน Java แล้ว อย่าลังเลที่จะทดลองกับ primitive อื่น ๆ, เพิ่มวัสดุ, หรือเชื่อมต่อการแปลงหลายขั้นตอนเพื่อสร้างโมเดล 3D ที่ซับซ้อนยิ่งขึ้น

---

**อัปเดตล่าสุด:** 2025-11-30  
**ทดสอบด้วย:** Aspose.3D for Java 24.11  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}