---
date: 2026-05-24
description: เรียนรู้วิธีสร้าง 3d extrusion ด้วย slices โดยใช้ Aspose.3D for Java
  คู่มือแบบขั้นตอนต่อขั้นตอนครอบคลุม linear extrusion, การตั้งค่า rounding radius,
  และการส่งออก OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: สร้าง 3D Extrusion ด้วย Slices – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: สร้าง 3D Extrusion ด้วย Slices – Aspose.3D for Java
url: /th/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# สร้างการดัน 3D ด้วยชั้น – Aspose.3D for Java

## บทนำ

หากคุณต้องการ **สร้างการดัน 3d** ที่ดูเรียบและแม่นยำ การควบคุมจำนวนชั้นเป็นกุญแจสำคัญ ในบทแนะนำนี้เราจะอธิบายวิธีระบุชั้นขณะทำการดันเชิงเส้นด้วย Aspose.3D for Java คุณจะเห็นว่าทำไมจำนวนชั้นถึงสำคัญ วิธีตั้งค่ารัศมีการโค้ง และวิธีส่งออกผลลัพธ์เป็นไฟล์ OBJ ที่สามารถใช้ในสายงาน 3‑D ใดก็ได้

## คำตอบด่วน
- **“slices” ควบคุมอะไร?** จำนวนส่วนตัดขวางกลางที่ใช้ประมาณพื้นผิวการดัน  
- **เมธอดใดตั้งค่าจำนวนชั้น?** `LinearExtrusion.setSlices(int)`  
- **ฉันสามารถเปลี่ยนรัศมีการโค้งของโปรไฟล์ได้หรือไม่?** ใช่ ผ่าน `RectangleShape.setRoundingRadius(double)`  
- **รูปแบบไฟล์ที่ใช้ในตัวอย่างนี้คืออะไร?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **ฉันต้องมีลิขสิทธิ์เพื่อรันโค้ดหรือไม่?** การทดลองใช้ฟรีเพียงพอสำหรับการประเมิน; ต้องมีลิขสิทธิ์เชิงพาณิชย์สำหรับการผลิต

`LinearExtrusion.setSlices(int)` กำหนดจำนวนชั้นกลางที่การดันจะสร้าง  
`RectangleShape.setRoundingRadius(double)` กำหนดรัศมีมุมของโปรไฟล์สี่เหลี่ยม

## วิธีสร้างการดัน 3d ด้วย Java และชั้น?

โหลดโปรไฟล์ 2‑D ของคุณ เลือกจำนวนชั้น ตั้งรัศมีการโค้ง และเรียก `save` – ทั้งกระบวนการทั้งหมดใช้เพียงไม่กี่บรรทัด Aspose.3D for Java จัดการการสร้างเรขาคณิต การแทรกชั้น และการส่งออก OBJ อัตโนมัติ ทำให้คุณมุ่งเน้นที่คุณภาพภาพแทนการคำนวณเมชระดับล่าง

## การดันเชิงเส้นด้วยชั้นคืออะไร?

การดันเชิงเส้นด้วยชั้นเปลี่ยนรูปทรง 2‑D แบนให้เป็นของแข็ง 3‑D โดยการลากตามเส้นตรงพร้อมสร้างส่วนตัดขวางกลางจำนวนที่กำหนด จำนวนชั้นมีผลโดยตรงต่อความเรียบของขอบโค้ง เช่น มุมโค้ง

## ทำไมต้องใช้ Aspose.3D for Java เพื่อสร้างการดัน 3D?

Aspose.3D ให้ **การควบคุมโปรแกรมเต็มรูปแบบ** ต่อพารามิเตอร์การดันทุกอย่าง รองรับ **รูปแบบเข้า‑ออกกว่า 50 รูปแบบ** (รวม OBJ, FBX, STL, และ GLTF) และสามารถประมวลผล **โมเดลหลายร้อยหน้า** โดยไม่ต้องโหลดไฟล์ทั้งหมดเข้าสู่หน่วยความจำ ทำงานบนแพลตฟอร์มที่รองรับ Java ทุกประเภท ไม่ต้องใช้ DLL เนทีฟ และรับประกันผลลัพธ์ที่แน่นอนบน Windows, Linux, และ macOS

## ข้อกำหนดเบื้องต้น

1. **Java Development Kit** – ติดตั้ง JDK 8 หรือสูงกว่า  
2. **Aspose.3D for Java** – ดาวน์โหลดไลบรารีจากเว็บไซต์อย่างเป็นทางการ [ที่นี่](https://releases.aspose.com/3d/java/)  
3. IDE หรือโปรแกรมแก้ไขข้อความตามที่คุณเลือก

## นำเข้าแพ็กเกจ

เพิ่ม namespace ของ Aspose.3D ไปยังโปรเจกต์ของคุณเพื่อให้เข้าถึงคลาสการสร้างโมเดล 3‑D

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## คู่มือขั้นตอนโดยละเอียด

### ขั้นตอนที่ 1: ตั้งค่าฉากและกำหนดโปรไฟล์

`RectangleShape` เป็นคลาสที่กำหนดโปรไฟล์สี่เหลี่ยม 2‑D  
แรกเราจะสร้าง `RectangleShape` และกำหนด **รัศมีการโค้ง** เพื่อให้มุมเรียบ  
`Scene` เป็นคอนเทนเนอร์รากสำหรับโหนดและเรขาคณิตทั้งหมด  
จากนั้นเราจะเริ่มต้น `Scene` ใหม่ที่เก็บเรขาคณิตทั้งหมด

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### ขั้นตอนที่ 2: สร้างอ็อบเจ็กต์โหนดลูกสำหรับแต่ละการดัน

`Node` แทนองค์ประกอบในกราฟฉากที่สามารถเก็บเรขาคณิตและการแปลงรูปได้  
ทุกชิ้นส่วนของเรขาคณิตอยู่ภายใต้ `Node` ที่นี่เราจะสร้างโหนดพี่น้องสองโหนด – หนึ่งสำหรับการดันชั้นต่ำและอีกหนึ่งสำหรับการดันชั้นสูง – แล้วย้ายโหนดซ้ายเล็กน้อยไปด้านข้างเพื่อให้ผลลัพธ์เปรียบเทียบได้ง่าย

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### ขั้นตอนที่ 3: ทำการดันเชิงเส้นและตั้งค่าชั้น

`LinearExtrusion` เป็นคลาสที่สร้างของแข็งโดยการลากโปรไฟล์แบบเชิงเส้น  
`LinearExtrusion` เป็นคลาสของ Aspose.3D ที่สร้างของแข็งโดยการดันโปรไฟล์ 2‑D ตามเส้นตรง ใช้ **anonymous inner class** เราเรียก `setSlices` เพื่อควบคุมความเรียบ โหนดซ้ายจะมีเพียง 2 ชั้น (หยาบ) ส่วนโหนดขวาจะมี 10 ชั้น (เรียบ)

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### ขั้นตอนที่ 4: ส่งออก OBJ – บันทึกฉาก

สุดท้ายเราจะเขียนฉากเป็นไฟล์ Wavefront OBJ ซึ่งเป็นรูปแบบที่ได้รับการสนับสนุนอย่างกว้างขวางโดยโปรแกรมแก้ไข 3‑D และเอนจินเกม นี้แสดงความสามารถ **export OBJ Java** ของ Aspose.3D

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|----------|
| **การดันปรากฏแบน** | จำนวนชั้นตั้งเป็น 1 หรือ 0 | ตรวจสอบให้แน่ใจว่า `setSlices` ถูกเรียกด้วยค่าที่ ≥ 2 |
| **มุมโค้งดูหยัก** | รัศมีการโค้งเล็กเกินไปเมื่อเทียบกับจำนวนชั้น | เพิ่มรัศมีหรือจำนวนชั้นเพื่อให้เส้นโค้งเรียบขึ้น |
| **ไฟล์ไม่พบเมื่อบันทึก** | `MyDir` ชี้ไปยังโฟลเดอร์ที่ไม่มีอยู่ | สร้างไดเรกทอรีล่วงหน้าหรือใช้เส้นทางแบบเต็ม |

## คำถามที่พบบ่อย

**ถาม: ฉันจะดาวน์โหลด Aspose.3D for Java ได้อย่างไร?**  
ตอบ: คุณสามารถดาวน์โหลดไลบรารีได้จาก [ที่นี่](https://releases.aspose.com/3d/java/)

**ถาม: ฉันจะหาเอกสารสำหรับ Aspose.3D ได้จากที่ไหน?**  
ตอบ: ดูเอกสารได้ที่ [ที่นี่](https://reference.aspose.com/3d/java/)

**ถาม: มีการทดลองใช้ฟรีหรือไม่?**  
ตอบ: ใช่, คุณสามารถสำรวจการทดลองใช้ฟรีได้ที่ [ที่นี่](https://releases.aspose.com/)

**ถาม: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร?**  
ตอบ: เยี่ยมชมฟอรั่มสนับสนุนได้ที่ [ที่นี่](https://forum.aspose.com/c/3d/18)

**ถาม: ฉันสามารถซื้อใบอนุญาตชั่วคราวได้หรือไม่?**  
ตอบ: ใช่, สามารถขอใบอนุญาตชั่วคราวได้ที่ [ที่นี่](https://purchase.aspose.com/temporary-license/)

**อัปเดตล่าสุด:** 2026-05-24  
**ทดสอบด้วย:** Aspose.3D for Java 24.11 (ล่าสุด ณ เวลาที่เขียน)  
**ผู้เขียน:** Aspose

## บทแนะนำที่เกี่ยวข้อง

- [สร้างการดัน 3D ด้วย Java ด้วย Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [วิธีตั้งทิศทางในการดันเชิงเส้นด้วย Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [สร้างฉาก 3D ด้วยการบิดในดันเชิงเส้น – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}