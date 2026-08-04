---
date: 2026-04-08
description: เรียนรู้วิธีสร้างทรงกระบอกที่มีส่วนบนชิดใน Aspose.3D สำหรับ Java, เพิ่มโหนดลูกใน
  Java, ตั้งค่าการชิดส่วนบน, สร้างโมเดล 3 มิติ, และส่งออกเป็น OBJ ด้วยใบอนุญาตชั่วคราวของ
  Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: ใบอนุญาตชั่วคราวของ Aspose – สร้างทรงกระบอกที่มีส่วนบนเลื่อน (Java)
second_title: Aspose.3D Java API
title: ใบอนุญาตชั่วคราวของ Aspose – สร้างทรงกระบอกที่มีส่วนบนชิดลบ (Java)
url: /th/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ใบอนุญาตชั่วคราวของ Aspose – สร้างทรงกระบอกที่มีส่วนบนชิด (Java)

## บทนำ

หากคุณกำลังมองหา **create cylinder** ที่มีส่วนบนชิดแบบกำหนดเองในฉาก 3D ที่ใช้ Java, Aspose.3D ทำให้กระบวนการง่ายดาย ในบทแนะนำนี้เราจะเดินผ่านทุกขั้นตอน—ตั้งแต่การตั้งค่าฉากจนถึงการส่งออกโมเดลขั้นสุดท้ายเป็นไฟล์ OBJ—เพื่อให้คุณสามารถรวมทรงกระบอกที่มีส่วนบนชิดเข้ากับแอปพลิเคชันของคุณได้อย่างมั่นใจ เมื่อจบคู่มือคุณจะเข้าใจว่า **aspose temporary license** ช่วยให้คุณประเมินคุณลักษณะเหล่านี้โดยไม่ต้องซื้อเต็มรูปแบบ

## คำตอบอย่างรวดเร็ว
- **ไลบรารีที่ใช้คืออะไร?** Aspose.3D for Java  
- **ฉันสามารถชิดส่วนบนของทรงกระบอกได้หรือไม่?** ใช่, โดยใช้ `setOffsetTop`  
- **ฉันจะเพิ่มโหนดลูกใน Java อย่างไร?** เรียก `createChildNode` บนโหนดราก  
- **ฉันสามารถส่งออกเป็นรูปแบบใดได้บ้าง?** Wavefront OBJ (`java export obj`)  
- **ฉันต้องการใบอนุญาตสำหรับการทดสอบหรือไม่?** **aspose temporary license** พร้อมให้ใช้สำหรับการประเมิน  

## ใบอนุญาตชั่วคราวของ Aspose คืออะไร?
**aspose temporary license** คือคีย์การประเมินฟรีแบบระยะสั้นที่เปิดใช้งานชุดคุณลักษณะทั้งหมดของ Aspose.3D for Java ระหว่างการพัฒนาและการทดสอบ มันจะลบลายน้ำการประเมินและอนุญาตให้คุณสร้างไฟล์โมเดล 3D เช่น OBJ, STL หรือ FBX ได้อย่างที่ใบอนุญาตแบบชำระเงินทำ

## ทำไมต้องใช้ Aspose.3D สำหรับ Java?
- **High‑level API:** ไม่จำเป็นต้องจัดการข้อมูลเมชระดับต่ำ  
- **Cross‑platform:** ทำงานบนสภาพแวดล้อมที่เข้ากันได้กับ JVM ใด ๆ  
- **Built‑in exporters:** บันทึกโดยตรงเป็น OBJ, STL, FBX และอื่น ๆ  
- **Extensible:** สามารถเพิ่มโหนดลูก, ใช้การแปลง, และรวมกับไลบรารี Java อื่น ๆ ได้อย่างง่ายดาย  

## ข้อกำหนดเบื้องต้น
- **Java Development Kit (JDK)** – เวอร์ชันที่เข้ากันได้ถูกติดตั้งไว้  
- **Aspose.3D for Java library** – ดาวน์โหลด JAR ล่าสุดจากเว็บไซต์อย่างเป็นทางการ [here](https://releases.aspose.com/3d/java/)  
- IDE ที่คุณเลือก (Eclipse, IntelliJ IDEA, NetBeans ฯลฯ)  

## นำเข้าชุดแพ็กเกจ
ก่อนอื่นให้นำเข้าคลาสที่เราต้องการใช้ วางคำสั่งเหล่านี้ที่ส่วนบนของไฟล์ Java ของคุณ:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## คู่มือขั้นตอนต่อขั้นตอน

### ขั้นตอนที่ 1: สร้างฉาก Java 3D
**java 3d scene** ทำหน้าที่เป็นคอนเทนเนอร์สำหรับวัตถุ 3D ทั้งหมด

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### ขั้นตอนที่ 2: เริ่มต้นทรงกระบอกด้วยส่วนบนชิด
ที่นี่เราตอบ **how to create cylinder** ด้วยการชิดแบบกำหนดเอง ตัวสร้างกำหนดค่ารัศมี, ความสูง, จำนวน slice, จำนวน stack, และว่าทรงกระบอกจะปิดหรือไม่ หลังจากนั้นเราจะย้ายส่วนบนโดยใช้ `setOffsetTop`

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### ขั้นตอนที่ 3: เพิ่มโหนดลูกใน Java – แนบทรงกระบอกแรก
เราสร้างโหนดลูกภายใต้โหนดรากของฉากและย้ายทรงกระบอกไปยังตำแหน่งที่ต้องการ

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### ขั้นตอนที่ 4: เริ่มต้นทรงกระบอกที่สอง (ไม่มีการชิด)
เพื่อเปรียบเทียบ เราเพิ่มทรงกระบอกปกติที่ไม่มีการชิด

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### ขั้นตอนที่ 5: เพิ่มโหนดลูกใน Java – แนบทรงกระบอกที่สอง
```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### ขั้นตอนที่ 6: ส่งออก OBJ ด้วย Java – บันทึกฉากเป็น OBJ
สุดท้ายเราจะ **java export obj** ฉากทั้งหมด (ทั้งสองทรงกระบอก) เป็นไฟล์ Wavefront OBJ ซึ่งได้รับการสนับสนุนอย่างกว้างขวางโดยเครื่องมือ 3D

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

เมื่อคุณรันโปรแกรม คุณจะพบไฟล์ `CustomizedOffsetTopCylinder.obj` ในไดเรกทอรีที่ระบุ พร้อมเปิดใน Blender, Maya หรือโปรแกรมดู OBJ ใด ๆ ที่รองรับ

## วิธีสร้างโมเดล 3D และส่งออก OBJ ใน Java
การผสมผสานของ `Scene.save(..., FileFormat.WAVEFRONTOBJ)` กับ **aspose temporary license** ทำให้คุณสามารถ **generate 3d model** ไฟล์ได้อย่างรวดเร็วโดยไม่ต้องใช้ตัวแปลงภายนอก ซึ่งเป็นประโยชน์มากในช่วงการสร้างต้นแบบหรือเมื่อแชร์ทรัพยากรกับนักออกแบบ

## กรณีการใช้งานจริง
- **Architectural visualisation:** ทรงกระบอกที่ชิดส่วนบนใช้โมเดลคอลัมน์ที่แคบลงไปด้านบนจนถึงเพดาน  
- **Mechanical parts:** สร้างลูกสูบหรือเคสเกียร์ที่พื้นผิวด้านบนถูกย้ายโดยเจตนา  
- **Game assets:** ผลิตรูปทรงเสาแบบหลากหลายแบบอัตโนมัติ ลดความจำเป็นในการสร้างเมชด้วยมือ  

## ปัญหาทั่วไปและวิธีแก้
| Issue | Reason | Fix |
|-------|--------|-----|
| **OBJ file is empty** | ฉากไม่ได้บันทึกอย่างถูกต้องหรือเส้นทางผิด | ตรวจสอบว่าไดเรกทอรีปลายทางมีอยู่และคุณมีสิทธิ์เขียน |
| **Offset not applied** | ใช้ Aspose.3D เวอร์ชันเก่า | อัปเดตเป็นไลบรารีล่าสุดที่รองรับ `setOffsetTop` |
| **Child node not visible** | การแปลงไม่ได้ถูกนำไปใช้ | ตรวจสอบว่าคุณเรียก `getTransform().setTranslation` หลังจากสร้างโหนดลูก |

## คำถามที่พบบ่อย
**Q: Aspose.3D รองรับ IDE ของ Java ต่าง ๆ หรือไม่?**  
A: ใช่, ทำงานอย่างราบรื่นกับ Eclipse, IntelliJ IDEA, NetBeans และ IDE อื่น ๆ  

**Q: ฉันสามารถใช้เทกเจอร์กับวัตถุ 3D ที่สร้างได้หรือไม่?**  
A: แน่นอน! ใช้คลาส `Material` เพื่อกำหนดเทกเจอร์และคุณสมบัติเชิงพื้นผิว  

**Q: มีตัวเลือกการให้ใบอนุญาตสำหรับ Aspose.3D หรือไม่?**  
A: มีโมเดลการให้ใบอนุญาตหลายแบบ; คุณสามารถสำรวจได้ที่ [here](https://purchase.aspose.com/buy)  

**Q: ฉันจะขอความช่วยเหลือหรือแบ่งปันประสบการณ์ได้อย่างไร?**  
A: เข้าร่วมฟอรั่มชุมชน Aspose.3D [here](https://forum.aspose.com/c/3d/18) เพื่อรับการสนับสนุนและการสนทนา  

**Q: มีใบอนุญาตชั่วคราวสำหรับการทดสอบหรือไม่?**  
A: มี, **aspose temporary license** สามารถขอได้เพื่อการประเมินที่ [here](https://purchase.aspose.com/temporary-license/)  

**อัปเดตล่าสุด:** 2026-04-08  
**ทดสอบด้วย:** Aspose.3D for Java 24.12 (latest)  
**ผู้เขียน:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}