---
date: 2025-12-09
description: เรียนรู้วิธีเพิ่มโหนดลูก, กำหนดตำแหน่งวัตถุ 3 มิติ, และบันทึกฉากเป็นไฟล์
  OBJ พร้อมสร้างทรงกระบอกพัดลมแบบกำหนดเองโดยใช้ Aspose.3D สำหรับ Java.
language: th
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: เพิ่มโหนดลูกเพื่อสร้างทรงกระบอกพัดลมด้วย Aspose.3D สำหรับ Java
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# เพิ่มโหนดลูกเพื่อสร้างทรงกระบอกพัดลมด้วย Aspose.3D สำหรับ Java

## Introduction

พร้อมหรือยังที่จะ **เพิ่มโหนดลูก** ไปยังฉาก 3‑D และสร้างทรงกระบอกพัดลมที่ดึงดูดสายตา? ในบทเรียนนี้เราจะเดินผ่านทุกขั้นตอน—from การตั้งค่าฉาก, การวางตำแหน่งวัตถุ 3D, จนถึงการ **บันทึกฉากเป็น OBJ**—โดยใช้ Aspose.3D สำหรับ Java ไม่ว่าคุณจะกำลังขัดเกลาสินทรัพย์เกมหรือสร้างต้นแบบอย่างรวดเร็ว แนวคิดเหล่านี้จะให้การควบคุมที่มั่นคงต่อโมเดล 3‑D ของคุณ

## Quick Answers
- **add child node** ทำอะไร?** มันแทรกวัตถุใหม่เข้าไปในกราฟฉาก โดยสืบทอดการแปลงจากโหนดพาเรนท์  
- **ฉันจะวางตำแหน่งวัตถุ 3D อย่างไร?** โดยการใช้การแปล (หรือการหมุน/สเกล) กับการแปลงของโหนด  
- **รูปแบบไฟล์ใดที่ใช้สำหรับการส่งออก?** ตัวอย่างบันทึกโมเดลเป็นไฟล์ Wavefront OBJ  
- **ฉันต้องมีลิขสิทธิ์เพื่อรันโค้ดหรือไม่?** การทดลองใช้ฟรีทำงานสำหรับการประเมิน; จำเป็นต้องมีลิขสิทธิ์สำหรับการผลิต  
- **IDE ใดที่เหมาะสมที่สุด?** IDE Java ใดก็ได้ (IntelliJ IDEA, Eclipse, VS Code) ที่รองรับ JDK 8+

## What is “add child node” in Aspose.3D?
การเพิ่มโหนดลูกหมายถึงการสร้างโหนดใหม่ภายใต้พาเรนท์ที่มีอยู่ในโครงสร้างฉาก โหนดลูกจะสืบทอดระบบพิกัดของพาเรนท์ ทำให้การ **วางตำแหน่งวัตถุ 3d** อย่างสัมพันธ์กันเป็นเรื่องง่าย

## Why add a child node when building fan cylinders?
- **การออกแบบแบบโมดูลาร์:** แต่ละทรงกระบอก (พัดลมหรือไม่พัดลม) อยู่ในโหนดของตนเอง ทำให้การแก้ไขภายหลังง่ายขึ้น  
- **การสืบทอดการแปลง:** ย้าย, หมุน, หรือสเกลพาเรนท์และโหนดลูกทั้งหมดจะตามโดยอัตโนมัติ  
- **กราฟฉากที่สะอาดขึ้น:** ปรับปรุงความอ่านง่ายและการดีบักของโมเดลที่ซับซ้อน  

## Prerequisites

- **Java Development Kit (JDK)** – ดาวน์โหลดจาก [official site](https://www.oracle.com/java/technologies/javase-downloads.html)  
- **Aspose.3D for Java** – รับไลบรารีล่าสุดจาก [download link](https://releases.aspose.com/3d/java/)  

## Import Packages

เริ่มต้นด้วยการนำเข้าแพ็กเกจที่จำเป็นเข้าสู่โครงการ Java ของคุณ ขั้นตอนนี้สำคัญสำหรับการเข้าถึงฟังก์ชันที่ Aspose.3D ให้ไว้

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Create a Scene

ขั้นแรก เราจะสร้างฉาก 3‑D ว่างเปล่าที่จะเป็นที่เก็บวัตถุทั้งหมดของเรา

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Step 2: Create a Fan Cylinder

ต่อไป เราจะสร้างทรงกระบอกที่จะแสดงเป็นพัดลม (การสวิงบางส่วน)

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Step 3: Add Child Node & Position 3D Object

ตอนนี้เราจะ **เพิ่มโหนดลูก** ไปยังฉากและ **วางตำแหน่งวัตถุ 3d** โดยตั้งค่าการแปลของมัน นี่คือจุดที่ทรงกระบอกพัดลมกลายเป็นส่วนหนึ่งของกราฟฉาก

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Step 4: Create a Non‑Fan Cylinder

เพื่อแสดงความยืดหยุ่นของ Aspose.3D เราจะสร้างทรงกระบอกปกติที่ไม่มีพัดลมและเพิ่มเป็นโหนดลูกอีกอันหนึ่ง

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Step 5: Save the Scene as OBJ

สุดท้าย เราจะ **บันทึกฉากเป็น OBJ** เพื่อให้คุณสามารถดูผลลัพธ์ในโปรแกรมดู 3‑D มาตรฐานใดก็ได้

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

ยินดีด้วย! คุณได้ **เพิ่มโหนดลูก** อย่างสำเร็จ, วางตำแหน่งวัตถุของคุณ, และส่งออกโมเดลเรียบร้อยแล้ว

## Common Issues & Tips

| ปัญหา | วิธีแก้ |
|-------|----------|
| **File not found** เมื่อบันทึก | ตรวจสอบว่าไดเรกทอรีเป้าหมายมีอยู่และคุณมีสิทธิ์เขียน |
| **Cylinder appears flat** | ตรวจสอบค่ารัศมีและความสูง; Aspose.3D คาดหวังหน่วยในสเกลเดียวกัน |
| **Fan slice looks incomplete** | ปรับ `ThetaLength` (เป็นเรเดียน) เพื่อครอบคลุมมุมที่ต้องการ |
| **Scene not visible in viewer** | ยืนยันว่าไฟล์ OBJ ถูกบันทึกพร้อมไฟล์ `.mtl` (วัสดุ) ที่เกี่ยวข้องหากจำเป็น |

## Frequently Asked Questions

**Q:** *Aspose.3D เข้ากันได้กับไลบรารี Java อื่นสำหรับการสร้างโมเดล 3D หรือไม่?*  
**A:** ใช่, Aspose.3D ทำงานร่วมกับไลบรารี Java 3‑D อื่น ๆ ให้คุณผสานคุณลักษณะตามต้องการ  

**Q:** *ฉันสามารถปรับแต่งลักษณะของทรงกระบอกพัดลมที่สร้างขึ้นเพิ่มเติมได้หรือไม่?*  
**A:** แน่นอน คุณสามารถใช้วัสดุ, เทกซ์เจอร์, และแสงโดยใช้คลาส `Material` และ `Light`  

**Q:** *ฉันจะหาแหล่งสนับสนุนหรือความช่วยเหลือเพิ่มเติมสำหรับ Aspose.3D ได้จากที่ไหน?*  
**A:** เยี่ยมชม [Aspose.3D forum](https://forum.aspose.com/c/3d/18) เพื่อรับความช่วยเหลือจากชุมชนและการตอบจากทางการ  

**Q:** *มีการทดลองใช้ฟรีสำหรับ Aspose.3D หรือไม่?*  
**A:** มี คุณสามารถสำรวจ Aspose.3D ด้วย [free trial](https://releases.aspose.com/) ก่อนซื้อ  

**Q:** *ฉันจะขอรับลิขสิทธิ์ชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?*  
**A:** รับลิขสิทธิ์ชั่วคราว [ที่นี่](https://purchase.aspose.com/temporary-license/) สำหรับการทดสอบและพัฒนา  

## Conclusion

ในคู่มือนี้เราได้สาธิตวิธี **เพิ่มโหนดลูก**, **วางตำแหน่งวัตถุ 3d**, และ **บันทึกฉากเป็น OBJ** พร้อมกับการสร้างทรงกระบอกพัดลมที่ปรับแต่งได้ด้วย Aspose.3D สำหรับ Java บล็อกการสร้างเหล่านี้ให้ความยืดหยุ่นในการสร้างโครงสร้าง 3‑D ที่ซับซ้อนและส่งออกเพื่อใช้ในกระบวนการต่อไปใด ๆ

---

**อัปเดตล่าสุด:** 2025-12-09  
**ทดสอบด้วย:** Aspose.3D 24.12 for Java  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}