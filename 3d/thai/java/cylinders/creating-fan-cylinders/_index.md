---
date: 2026-04-03
description: เรียนรู้วิธีสร้างรูปทรงพัดลมทรงกระบอกใน Java ด้วย Aspose.3D คู่มือนี้ครอบคลุมการสร้างโมเดล
  3 มิติด้วย Java และเทคนิคการบันทึกไฟล์ OBJ ด้วย Java
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
linktitle: วิธีสร้างรูปทรงพัดลมทรงกระบอกโดยใช้ Aspose.3D สำหรับ Java
second_title: Aspose.3D Java API
title: วิธีสร้างรูปทรงพัดลมทรงกระบอกโดยใช้ Aspose.3D สำหรับ Java
url: /th/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีสร้างรูปทรงพัดลมทรงกระบอกโดยใช้ Aspose.3D สำหรับ Java

## บทนำ

พร้อมหรือยังที่จะเชี่ยวชาญ **วิธีสร้างรูปทรงพัดลมทรงกระบอก** ในสภาพแวดล้อม Java? ในบทแนะนำนี้เราจะเดินผ่านทุกขั้นตอน— ตั้งแต่การตั้งค่าฉากจนถึงการส่งออกไฟล์ Wavefront OBJ— โดยใช้ Aspose.3D ไม่ว่าคุณจะสร้างสินทรัพย์เกม, ตัวอย่าง CAD, หรือเพียงทดลองกับเรขาคณิต 3 มิติ, คุณจะเห็นว่า การสร้างโมเดล 3D ด้วย Java สามารถทำได้ง่ายแค่ไหนด้วยไลบรารีที่ทรงพลังนี้.

## คำตอบอย่างรวดเร็ว
- **เป้าหมายหลักคืออะไร?** สร้างทรงกระบอกรูปพัดลมที่ปรับแต่งได้และบันทึกเป็นไฟล์ OBJ.  
- **ไลบรารีที่ใช้คืออะไร?** Aspose.3D for Java.  
- **ฉันต้องการไลเซนส์หรือไม่?** รุ่นทดลองฟรีใช้งานได้สำหรับการพัฒนา; จำเป็นต้องมีไลเซนส์เชิงพาณิชย์สำหรับการผลิต.  
- **ข้อกำหนดเบื้องต้นคืออะไร?** ติดตั้ง JDK แล้วและเพิ่มแพคเกจ Aspose.3D Java ลงในโปรเจคของคุณ.  
- **ฉันสามารถส่งออกเป็นรูปแบบอื่นได้หรือไม่?** ได้—Aspose.3D รองรับหลายรูปแบบ; ตัวอย่างนี้ใช้ Wavefront OBJ.

## พัดลมทรงกระบอกคืออะไร

พัดลมทรงกระบอกคือทรงกระบอกที่มีพื้นผิวบางส่วนซึ่งส่วนของฐานวงกลมถูกตัดออก, ทำให้เกิดช่องเปิดแบบ “พัดลม”. เรขาคณิตนี้มีประโยชน์สำหรับการแสดงสไลซ์, แดชบอร์ด, หรือชิ้นส่วนเครื่องกลแบบกำหนดเอง.

## ทำไมต้องใช้ Aspose.3D สำหรับการสร้างโมเดล 3D ด้วย Java?

Aspose.3D มี API ที่สะอาดและเชิงวัตถุซึ่งทำให้ซับซ้อนของคณิตศาสตร์ระดับต่ำของกราฟิก 3D หายไป. คุณสามารถมุ่งเน้นที่การออกแบบแทนที่จะกังวลเรื่องความแปลกของรูปแบบไฟล์, และไลบรารีจะจัดการการดำเนินการ **save obj file java** โดยอัตโนมัติ.

## ข้อกำหนดเบื้องต้น

Before we dive in, make sure you have:

- **Java Development Kit (JDK)** – ดาวน์โหลดจาก [ที่นี่](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – รับ JAR เวอร์ชันล่าสุดจาก [ลิงก์ดาวน์โหลด](https://releases.aspose.com/3d/java/).  

เพิ่มไฟล์ JAR ของ Aspose.3D ไปยัง classpath ของโปรเจคของคุณ.

## นำเข้าแพ็กเกจ

Begin by importing the necessary classes. This gives you access to the 3D scene, geometry primitives, and utility methods.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ขั้นตอนที่ 1: สร้างฉาก

First, we instantiate a new `Scene`. Think of a scene as the container that holds all your 3D objects, lights, and cameras.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## ขั้นตอนที่ 2: สร้างพัดลมทรงกระบอก (วิธีสร้างทรงกระบอก)

Now we build the fan cylinder itself. The constructor parameters define radius, height, tessellation, and whether the geometry is generated as a fan.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **เคล็ดลับ:** ปรับ `setThetaLength` เพื่อเปลี่ยนมุมเปิด. 270° สร้างพัดลมสามในสี่; 180° จะให้ครึ่งทรงกระบอก.

## ขั้นตอนที่ 3: กำหนดตำแหน่งพัดลมทรงกระบอก

Next, we add the fan cylinder to the scene and move it to a convenient location. The translation coordinates are in the order (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## ขั้นตอนที่ 4: สร้างทรงกระบอกแบบไม่เป็นพัดลม (การเปรียบเทียบการสร้างโมเดล 3d ด้วย java)

To illustrate the flexibility of Aspose.3D, we also create a regular cylinder without a fan opening.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## ขั้นตอนที่ 5: บันทึกฉาก (บันทึกไฟล์ obj ด้วย java)

Finally, we export the entire scene to a Wavefront OBJ file. This format is widely supported by most 3D editors and game engines.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **หมายเหตุ:** แทนที่ `"Your Document Directory"` ด้วยเส้นทางแบบ absolute หรือ relative ที่คุณมีสิทธิ์เขียน.

## วิธีบันทึกไฟล์ OBJ ใน Java ด้วย Aspose 3D

Aspose.3D’s `Scene.save` method automatically handles the **aspose 3d export obj** process. You only need to specify the target file name and the `FileFormat.WAVEFRONTOBJ` enum value, as shown in the previous step.

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|-----|
| ไฟล์ OBJ ว่าง | ฉากไม่ได้บันทึกหรือเส้นทางไม่ถูกต้อง | ตรวจสอบว่าไดเรกทอรีผลลัพธ์มีอยู่และมีสิทธิ์เขียน. |
| ช่องเปิดพัดลมดูผิด | ค่า `ThetaLength` ไม่ถูกต้อง | ใช้ `MathUtils.toRadian(degrees)` เพื่อตั้งค่ามุมที่ต้องการอย่างแม่นยำ. |
| ข้อผิดพลาดการคอมไพล์ | ไม่มีไฟล์ JAR ของ Aspose.3D ใน classpath | เพิ่มไฟล์ JAR ไปยังโฟลเดอร์ `libs` ของโปรเจคและรวมไว้ในเส้นทางการสร้าง. |

## คำถามที่พบบ่อย

**Q:** Aspose.3D เข้ากันได้กับไลบรารี Java 3D อื่นหรือไม่?  
**A:** ใช่, Aspose.3D สามารถทำงานร่วมกับไลบรารีเช่น Java 3D หรือ jMonkeyEngine, ทำให้คุณสามารถรวมเรขาคณิตที่กำหนดเองเข้าไปใน pipeline ที่ใหญ่ขึ้น.

**Q:** ฉันสามารถปรับแต่งลักษณะของพัดลมทรงกระบอกได้เพิ่มเติมหรือไม่?  
**A:** แน่นอน. คุณสามารถใช้วัสดุ, เทกซ์เจอร์, และแสงโดยเข้าถึงคอลเลกชัน `Material` และ `Light` ของโหนด.

**Q:** ฉันจะหาแหล่งสนับสนุนเพิ่มเติมได้จากที่ไหน?  
**A:** เยี่ยมชม [Aspose.3D forum](https://forum.aspose.com/c/3d/18) เพื่อรับความช่วยเหลือจากชุมชนและการตอบอย่างเป็นทางการ.

**Q:** มีรุ่นทดลองฟรีหรือไม่?  
**A:** มี, คุณสามารถสำรวจ Aspose.3D ด้วย [free trial](https://releases.aspose.com/) ก่อนทำการซื้อ.

**Q:** ฉันจะขอรับไลเซนส์ชั่วคราวสำหรับการทดสอบได้อย่างไร?  
**A:** รับได้จาก [ที่นี่](https://purchase.aspose.com/temporary-license/) เพื่อเปิดใช้งานฟังก์ชันเต็มในระหว่างการพัฒนา.

---

**อัปเดตล่าสุด:** 2026-04-03  
**ทดสอบด้วย:** Aspose.3D 24.11 for Java  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}