---
date: 2025-12-19
description: เรียนรู้วิธีสร้างฉาก 3 มิติและส่งออกไฟล์ 3D OBJ ด้วย Twist Offset ใน
  Linear Extrusion ด้วย Aspose.3D สำหรับ Java.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: สร้างฉาก 3 มิติด้วย Twist Offset – Aspose.3D Java
url: /th/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# สร้าง 3d scene ด้วย Twist Offset – Aspose.3D for Java

## Introduction

ในโลกที่เปลี่ยนแปลงอย่างรวดเร็วของกราฟิก 3D การเรียนรู้วิธี **create 3d scene** ด้วยการดึงเส้นตรงเป็นการเปลี่ยนเกมอย่างมาก ด้วย Aspose.3D for Java คุณสามารถยกระดับทักษะการสร้างโมเดล 3D ของคุณโดยการรวมฟีเจอร์ Twist Offset เข้าไปในกระบวนการดึงเส้นตรง การสอนนี้จะนำคุณผ่านขั้นตอนการใช้ Twist Offset ใน Linear Extrusion ด้วย Aspose.3D for Java เพื่อให้คุณมีเครื่องมือสร้างฉาก 3D ที่น่าตื่นตาตื่นใจ

## Quick Answers
- **What does Twist Offset do?** มันจะเลื่อนจุดเริ่มต้นของการบิดตามเส้นทางการดึงเส้น ทำให้คุณควบคุมรูปทรงได้มากขึ้น  
- **Which file format is used for export?** ตัวอย่างนี้บันทึกโมเดลเป็นไฟล์ Wavefront OBJ (`.obj`)  
- **Do I need a license for development?** สามารถใช้เวอร์ชันทดลองฟรีเพื่อทดสอบได้; ต้องมีใบอนุญาตเชิงพาณิชย์สำหรับการใช้งานจริง  
- **What Java version is required?** Java 8 หรือใหม่กว่า  
- **Can I change the number of slices?** ได้ – วิธี `setSlices` กำหนดความเรียบของการบิด

## Prerequisites

ก่อนเริ่มการสอน โปรดตรวจสอบว่าคุณมีข้อกำหนดต่อไปนี้พร้อมใช้งาน:

- Java Environment: ตรวจสอบให้แน่ใจว่าคุณได้ตั้งค่าสภาพแวดล้อมการพัฒนา Java บนระบบของคุณแล้ว  
- Aspose.3D for Java: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D จาก [download link](https://releases.aspose.com/3d/java/)  
- Documentation: ทำความคุ้นเคยกับ [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)  

## Import Packages

ในโครงการ Java ของคุณ ให้นำเข้าแพ็กเกจที่จำเป็นเพื่อเริ่มใช้ Aspose.3D for Java อย่าลืมรวมไลบรารีที่ต้องการเพื่อการผสานรวมที่ราบรื่น

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Step 1: Set Up the Environment

เริ่มต้นด้วยการตั้งค่าสภาพแวดล้อมการพัฒนา Java ของคุณและตรวจสอบว่า Aspose.3D for Java ได้รับการติดตั้งอย่างถูกต้อง

## Step 2: Initialize the Base Profile

สร้างโปรไฟล์ฐานสำหรับการดึงเส้น ในกรณีนี้คือ `RectangleShape` ที่มีรัศมีการโค้ง 0.3

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 3: Create a 3D Scene

สร้างฉาก 3D เพื่อเป็นที่เก็บวัตถุที่ดึงเส้นของคุณ

```java
// Create a scene
Scene scene = new Scene();
```

## Step 4: Create Nodes

สร้างโหนดภายในฉากเพื่อแทนเอนทิตีต่าง ๆ

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 5: Perform Linear Extrusion

ใช้การดึงเส้นแบบเชิงเส้นบนโหนดซ้ายและขวาพร้อมคุณสมบัติต่าง ๆ

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Step 6: Save the 3D Scene

บันทึกฉาก 3D ที่คุณสร้างใหม่ด้วยรูปแบบไฟล์ที่ระบุ

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## How to save 3d model and export 3d obj

คำสั่ง `scene.save` ในขั้นตอนก่อนหน้านี้ **saves the 3d model** เป็นไฟล์ OBJ ซึ่งเป็นรูปแบบ **export 3d obj** ที่ได้รับการสนับสนุนอย่างกว้างขวาง คุณสามารถเปลี่ยนชื่อไฟล์หรือเลือกรูปแบบที่สนับสนุนอื่น (เช่น STL, FBX) โดยปรับค่าใน enum `FileFormat`

## Conclusion

ขอแสดงความยินดี! คุณได้ทำการนำ Twist Offset ไปใช้ใน Linear Extrusion ด้วย Aspose.3D for Java อย่างสำเร็จ ฟีเจอร์ที่ทรงพลังนี้เปิดโลกของความเป็นไปได้ใหม่สำหรับการสร้างโมเดล 3D ของคุณ ให้คุณ **create 3d scene** ด้วยการบิดและออฟเซ็ตที่ซับซ้อน และจากนั้น **save 3d model** ในรูปแบบที่พร้อมสำหรับกระบวนการต่อไป

## FAQ's

### Q1: Can I use Aspose.3D for Java in non-commercial projects?

A1: ใช่, Aspose.3D for Java สามารถใช้ได้ทั้งในโครงการเชิงพาณิชย์และไม่เชิงพาณิชย์ ตรวจสอบ [licensing options](https://purchase.aspose.com/buy) สำหรับรายละเอียดเพิ่มเติม

### Q2: Where can I find support for Aspose.3D for Java?

A2: เยี่ยมชม [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18) เพื่อขอความช่วยเหลือและเชื่อมต่อกับชุมชน

### Q3: Is there a free trial available for Aspose.3D for Java?

A3: มี คุณสามารถสำรวจเวอร์ชันทดลองฟรีจาก [releases page](https://releases.aspose.com/)

### Q4: How do I obtain a temporary license for Aspose.3D for Java?

A4: รับใบอนุญาตชั่วคราวสำหรับโครงการของคุณโดยไปที่ [this link](https://purchase.aspose.com/temporary-license/)

### Q5: Are there additional examples and tutorials available?

A5: มี โปรดอ้างอิงที่ [documentation](https://reference.aspose.com/3d/java/) สำหรับตัวอย่างและการสอนเชิงลึกเพิ่มเติม

## Frequently Asked Questions

**Q: Is this tutorial part of an Aspose 3d tutorial series?**  
A: ใช่ – นี่คือ **aspose 3d tutorial** อย่างเป็นทางการที่แสดงฟีเจอร์เฉพาะของไลบรารี

**Q: Can I use a different shape instead of a rectangle?**  
A: แน่นอน ทุกการทำงานของ `IProfile` (เช่น `CircleShape`, `PolygonShape` ที่กำหนดเอง) สามารถดึงเส้นได้

**Q: What happens if I omit `setTwistOffset`?**  
A: การดึงเส้นจะเริ่มบิดจากจุดกำเนิดของโปรไฟล์ ทำให้เกิดการบิดที่สมมาตร

**Q: How do I increase the smoothness of the twist?**  
A: เพิ่มค่าที่ส่งให้ `setSlices`; จำนวน slice ที่มากขึ้นจะทำให้รูปทรงบิดเรียบขึ้น

**Q: Which other file formats can I export besides OBJ?**  
A: Aspose.3D รองรับ STL, FBX, GLTF, 3MF และหลายรูปแบบอื่น ๆ ผ่าน enum `FileFormat`

---

**Last Updated:** 2025-12-19  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## TARGET KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**  
create 3d scene  

**Secondary Keywords (SUPPORTING):**  
save 3d model, export 3d obj, aspose 3d tutorial