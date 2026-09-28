---
date: 2026-09-28
description: เรียนรู้วิธีทำแอนิเมชันฉาก 3D ใน Java ด้วย Aspose.3D, เพิ่ม animation
  properties, สร้าง keyframes, และส่งออกไฟล์ FBX ที่มีแอนิเมชันด้วยเทคนิค linear interpolation
  3D
keywords:
- how to animate 3d
- linear interpolation 3d
- export animated fbx
- create keyframe animation
- add animation properties
lastmod: 2026-09-28
linktitle: วิธีทำแอนิเมชันฉาก 3D ใน Java ด้วย Aspose.3D
og_description: เรียนรู้วิธีทำแอนิเมชันฉาก 3D ใน Java ด้วย Aspose.3D. คู่มือขั้นตอนนี้แสดงการเพิ่ม
  animation properties, การสร้าง keyframes, และการส่งออกไฟล์ FBX ที่มีแอนิเมชัน
og_image_alt: Developer guide showing how to animate 3D scenes in Java with Aspose.3D
og_title: วิธีทำแอนิเมชันฉาก 3D ใน Java – คู่มือ Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-09-28'
  description: Learn how to animate 3D scenes in Java using Aspose.3D, add animation
    properties, create keyframes, and export animated FBX files with linear interpolation
    3d techniques.
  headline: How to animate 3D scenes in Java with Aspose.3D
  type: TechArticle
- questions:
  - answer: Yes. Purchase a commercial license on the [Aspose purchase page](https://purchase.aspose.com/buy).
    question: Can I use Aspose.3D for commercial projects?
  - answer: Absolutely. Download a trial from the [Aspose releases page](https://releases.aspose.com/).
    question: Is a free trial available?
  - answer: Join the community at the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18)
      for help from staff and other developers.
    question: Where can I get support?
  - answer: Request a [temporary license](https://purchase.aspose.com/temporary-license/)
      to remove runtime restrictions during testing.
    question: How do I obtain a temporary evaluation license?
  - answer: Yes—explore the full [Aspose.3D documentation](https://reference.aspose.com/3d/java/)
      for advanced scenarios such as skeletal animation, morph targets, and custom
      shaders.
    question: Are there more tutorials?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- animate 3d java
- Aspose.3D
- linear interpolation
- FBX export
- Java animation tutorial
title: วิธีทำแอนิเมชันฉาก 3D ใน Java ด้วย Aspose.3D
url: /th/java/animations/add-animation-properties-to-scenes/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีทำแอนิเมชันฉาก 3D ใน Java ด้วย Aspose.3D

## บทนำ

ในบทแนะนำนี้คุณจะได้เรียนรู้ **วิธีทำแอนิเมชัน 3D** ของวัตถุในแอปพลิเคชัน Java ด้วย Aspose.3D เราจะเริ่มด้วยการสร้างฉาก, สร้างเมชง่าย ๆ, ผูกคุณสมบัติแอนิเมชัน, กำหนดคีย์เฟรมด้วยการอินเทอร์โพเลชันเชิงเส้น, และสุดท้ายส่งออกผลลัพธ์เป็นไฟล์ FBX ที่มีแอนิเมชัน เมื่อเสร็จคุณจะได้ FBX พร้อมใช้งานที่ทำงานใน Unity, Blender หรือโปรแกรมดู 3‑D สมัยใหม่ใด ๆ

## คำตอบสั้น
- **ไลบรารีใดที่เป็นแรงขับเคลื่อนการแอนิเมชัน?** Aspose.3D for Java, เป็นเอนจิน 3‑D แบบ pure‑Java  
- **ฉันสามารถส่งออกผลลัพธ์เป็น FBX ได้หรือไม่?** ใช่ – ตัวอย่างจะบันทึกไฟล์ `FBX7500ASCII` ที่เก็บคีย์เฟรมทั้งหมด  
- **ฉันต้องมีไลเซนส์แบบชำระเงินเพื่อทดลองใช้นี้หรือไม่?** การทดลองใช้แบบฟรีทำงานได้สำหรับการพัฒนา; จำเป็นต้องมีไลเซนส์เชิงพาณิชย์สำหรับการใช้งานในผลิตภัณฑ์  
- **ต้องการเวอร์ชัน Java ใด?** Java 8 หรือใหม่กว่า  
- **การอินเทอร์โพเลชันเป็นเชิงเส้นหรือสไพล์น?** รองรับทั้งสองแบบ; คุณสามารถเลือก `Interpolation.LINEAR` สำหรับการเคลื่อนที่เป็นเส้นตรงหรือ `Interpolation.BEZIER` สำหรับเส้นโค้งที่ราบรื่น  

## การอินเทอร์โพเลชันเชิงเส้น 3D คืออะไร?

การอินเทอร์โพเลชันเชิงเส้น 3D คือการคำนวณค่าการแปลงกลางระหว่างสองคีย์เฟรมโดยใช้สูตรเส้นตรง ใน Aspose.3D คุณเลือก `Interpolation.LINEAR` เมื่อเพิ่มคีย์เฟรม และเอนจินจะสร้างการเคลื่อนที่ด้วยความเร็วคงที่ระหว่างเฟรมโดยอัตโนมัติ

## ทำไมต้องเพิ่มคุณสมบัติแอนิเมชันให้กับฉาก?

การเพิ่มคุณสมบัติแอนิเมชันทำให้เรขาคณิตแบบคงที่กลายเป็นเนื้อหาแบบไดนามิกที่สามารถนำไปใช้ซ้ำในเกม, การจำลอง, หรือการแสดงผลผลิตภัณฑ์ ด้วย Aspose.3D คุณสามารถทำแอนิเมชันหลายโหนดได้อย่างอิสระ, ส่งออกไฟล์ FBX ที่มีแอนิเมชันเต็มรูปแบบ, และรักษากระบวนการทำงานทั้งหมดใน Java บริสุทธิ์โดยไม่ต้องใช้ DLL แบบเนทีฟ

## ทำไมต้องใช้ Aspose.3D สำหรับแอนิเมชัน?

Aspose.3D รองรับ **12+** รูปแบบการส่งออก รวมถึง FBX, OBJ, 3MF, STL, และ GLTF—ทำให้คุณสามารถเลือกใช้ในสายงานใดก็ได้ ไลบรารีทำงานบน JVM เท่านั้น ทำให้ไม่ต้องพึ่งพาไลบรารีเนทีฟ นอกจากนี้ยังมีโหมดการอินเทอร์โพเลชันสามแบบ (BEZIER, LINEAR, STEP) และ API ของกราฟฉากที่ครบถ้วนซึ่งช่วยให้คุณจัดการโหนด, เมช, วัสดุ, และแอนิเมชันผ่านโมเดลอ็อบเจกต์เดียวที่สอดคล้องกัน

## ข้อกำหนดเบื้องต้น

- ความรู้พื้นฐานของการเขียนโปรแกรม Java.  
- Aspose.3D for Java ติดตั้งแล้ว – ดาวน์โหลดจาก [หน้าเผยแพร่](https://releases.aspose.com/3d/java/).  
- ตั้งค่า Maven หรือ Gradle เพื่อคอมไพล์โครงการตัวอย่าง.  

## นำเข้าแพ็กเกจ

ในไฟล์ซอร์ส Java ของคุณ ให้นำเข้าเนมสเปซหลักของ Aspose.3D และคลาสช่วยเหลือ `Common` ที่สร้างเมชลูกบาศก์ง่าย ๆ คลาส `Common` มีเมธอดสเตติกเพื่อสร้างเรขาคณิตพื้นฐาน เช่น ลูกบาศก์หน่วย

```java
import com.aspose.threed.*;
```

เมื่อเนมสเปซพร้อมแล้ว เรามาเริ่มสร้างฉากกัน

## ขั้นตอนที่ 1: เริ่มต้นฉาก

คลาส `Scene` เป็นคอนเทนเนอร์ระดับบนของ Aspose.3D ที่เก็บโหนดทั้งหมด, เมช, แสง, และข้อมูลแอนิเมชัน

```java
// Initialize scene object
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: สร้างเมชโดยใช้ Polygon Builder

คลาส `Mesh` แสดงถึงคอลเลกชันของเวอร์เท็กซ์, เฟซ, และนอร์มัลที่กำหนดวัตถุ 3‑D ในขั้นตอนนี้ ตัวช่วยจะสร้างเมชลูกบาศก์พื้นฐานที่เราจะทำแอนิเมชันต่อไป

```java
Mesh mesh = new Mesh();
```

## ขั้นตอนที่ 3: สร้างโหนดลูกบาศก์พร้อมการแปลตำแหน่ง

`Node` คือองค์ประกอบในกราฟฉากที่สามารถเก็บเมชและคุณสมบัติการแปลง (การแปลตำแหน่ง, การหมุน, การสเกล) ที่นี่เราจะผูกเมชลูกบาศก์เข้ากับโหนดใหม่และวางไว้ที่จุดกำเนิด

```java
// Each cube node has its own translation
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

## ขั้นตอนที่ 4: ค้นหาคุณสมบัติการแปลตำแหน่ง

**bind point** เชื่อมต่อคุณสมบัติเฉพาะ—เช่น translation—กับโค้งแอนิเมชัน การค้นหา bind point ของการแปลตำแหน่งทำให้เอนจินสามารถปรับตำแหน่งของโหนดตามเวลาได้

```java
// Find translation property on node's transform object
Property translation = cube1.getTransform().findProperty("Translation");
```

## ขั้นตอนที่ 5: สร้างโค้งแอนิเมชันสำหรับแกน X

โค้งแอนิเมชันเก็บชุดของคีย์เฟรมสำหรับส่วนประกอบเดียว (X, Y หรือ Z) โค้งด้านล่างกำหนดคีย์เฟรมสามจุดที่ 0 s, 3 s, และ 5 s สองจุดแรกใช้ BEZIER เพื่อความราบรื่น, ส่วนคีย์เฟรมสุดท้ายใช้ LINEAR เพื่อแสดงการอินเทอร์โพเลชันเชิงเส้น 3d

```java
// Create an animation node for the scene
AnimationNode animNode = new AnimationNode("TranslationAnimation");

// Create a bind point for the translation property on the cube's transform
BindPoint bp = animNode.createBindPoint(cube1.getTransform(), "Translation");

// Create the animation curve on the X component of the translation
KeyframeSequence kfsX = new KeyframeSequence();

// Add keyframes for X component
kfsX.add(0, 10.0f, Interpolation.BEZIER);
kfsX.add(3, 20.0f, Interpolation.BEZIER);
kfsX.add(5, 30.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the X channel of the bind point
bp.bindKeyframeSequence("X", kfsX);
```

## ขั้นตอนที่ 6: ทำซ้ำสำหรับส่วนประกอบ Z

การทำแอนิเมชันแกน Z เพิ่มความลึกให้กับการเคลื่อนที่ของลูกบาศก์, สร้างเส้นทาง 3‑D ที่ไดนามิกมากขึ้น ตรรกะของ bind‑point และโค้งเดียวกันใช้ได้, แต่ค่าจะทำให้ลูกบาศก์เคลื่อนที่ไปข้างหน้าและถอยหลัง

```java
// Repeat the process for the Z component
KeyframeSequence kfsZ = new KeyframeSequence();
kfsZ.add(0, 10.0f, Interpolation.BEZIER);
kfsZ.add(3, -10.0f, Interpolation.BEZIER);
kfsZ.add(5, 0.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the Z channel of the same bind point
bp.bindKeyframeSequence("Z", kfsZ);
```

## วิธีส่งออก FBX ที่มีแอนิเมชัน

การเรียก `scene.save(...)` ด้วย `FileFormat.FBX7500ASCII` จะเขียนโค้งแอนิเมชันทั้งหมด, bind point, และคีย์เฟรมลงในคอนเทนเนอร์ FBX เดียว `FileFormat` เป็น enum ที่กำหนดรูปแบบเอาต์พุตที่รองรับ, รวมถึง `FBX7500ASCII` ตรวจสอบให้แน่ใจว่าไดเรกทอรีเป้าหมายมีอยู่และคุณมีสิทธิ์เขียน; มิฉะนั้นการบันทึกจะโยนข้อยกเว้น

```java
// Specify the directory for saving the 3D scene
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

ไฟล์ที่สร้างขึ้นสามารถเปิดใน Blender, Unity, Autodesk Maya หรือโปรแกรมดูใด ๆ ที่รองรับรูปแบบ FBX, ทำให้คุณสามารถดูตัวอย่างแอนิเมชันได้ทันที

## ปัญหาทั่วไปและวิธีแก้

| อาการ | สาเหตุที่เป็นไปได้ | วิธีแก้ |
|---------|--------------|-----|
| ไม่มีการเคลื่อนไหวปรากฏ | คีย์เฟรมถูกเพิ่มในส่วนประกอบผิด (เช่น “Y” แทน “X”) | ตรวจสอบชื่อส่วนประกอบใน `bindKeyframeSequence`. |
| แอนิเมชันกระโดด | ผสมผสาน BEZIER และ LINEAR อย่างไม่ถูกต้อง | รักษาการอินเทอร์โพเลชันให้สอดคล้องเพื่อการเคลื่อนที่ราบรื่น, หรือปรับเทนเจนต์ด้วยตนเอง. |
| ไฟล์ไม่ถูกบันทึก | เส้นทางไดเรกทอรีไม่ถูกต้อง | ตรวจสอบให้ `MyDir` ชี้ไปยังโฟลเดอร์ที่มีอยู่และสามารถเขียนได้และลงท้ายด้วย `.fbx`. |

## คำถามที่พบบ่อย

**Q: ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่?**  
A: ใช่. ซื้อไลเซนส์เชิงพาณิชย์ได้ที่ [Aspose purchase page](https://purchase.aspose.com/buy).

**Q: มีการทดลองใช้แบบฟรีหรือไม่?**  
A: แน่นอน. ดาวน์โหลดรุ่นทดลองจาก [Aspose releases page](https://releases.aspose.com/).

**Q: ฉันจะหาแหล่งสนับสนุนได้จากที่ไหน?**  
A: เข้าร่วมชุมชนที่ [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) เพื่อรับความช่วยเหลือจากทีมงานและนักพัฒนาคนอื่น ๆ.

**Q: ฉันจะขอรับไลเซนส์ประเมินผลชั่วคราวได้อย่างไร?**  
A: ขอรับ [temporary license](https://purchase.aspose.com/temporary-license/) เพื่อยกเลิกข้อจำกัดระหว่างการทดสอบ.

**Q: มีบทแนะนำเพิ่มเติมหรือไม่?**  
A: มี — สำรวจ [Aspose.3D documentation](https://reference.aspose.com/3d/java/) อย่างเต็มเพื่อดูกรณีการใช้งานขั้นสูง เช่น การแอนิเมชันโครงกระดูก, morph targets, และ custom shaders.

## สรุป

คุณตอนนี้รู้แล้ว **วิธีทำแอนิเมชัน 3D** ของวัตถุใน Java ด้วย Aspose.3D: สร้างฉาก, ผูกคุณสมบัติการแปลตำแหน่ง, กำหนดลำดับคีย์เฟรมด้วยการอินเทอร์โพเลชันเชิงเส้น, และส่งออกไฟล์ FBX ที่มีแอนิเมชัน ทดลองใช้การหมุน, การสเกล, หรือหลายโหนดเพื่อสร้างแอนิเมชันที่หลากหลายยิ่งขึ้นสำหรับเกม, การจำลอง, หรือการแสดงผลผลิตภัณฑ์

---

**อัปเดตล่าสุด:** 2026-09-28  
**ทดสอบกับ:** Aspose.3D for Java 24.12 (latest)  
**ผู้เขียน:** Aspose

## บทแนะนำที่เกี่ยวข้อง

- [สร้างไฟล์ FBX ด้วย Aspose.3D สำหรับ Java – บทแนะนำกราฟิก 3D](/3d/java/load-and-save/create-empty-3d-document/)
- [บันทึกฉาก 3D ใน Java ด้วย Aspose.3D – แปลงไฟล์ 3D อย่างมีประสิทธิภาพ](/3d/java/load-and-save/save-3d-scenes/)
- [ส่งออกโมเดลเป็น FBX ด้วยควอร์เทอร์เนียนใน Java โดยใช้ Aspose.3D](/3d/java/geometry/transform-3d-nodes-with-quaternions/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}