---
date: 2025-12-17
description: เรียนรู้วิธีสร้างโมเดล 3 มิติแบบบิดโดยใช้ Aspose.3D สำหรับ Java ด้วยการบิดแบบดึงเส้นตรงและส่งออกไฟล์
  OBJ ใน Java ทำตามคู่มือขั้นตอนต่อขั้นตอนของเรา
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: สร้างโมเดล 3 มิติแบบบิด – การใช้การบิดในการดึงเชิงเส้นด้วย Aspose.3D สำหรับ
  Java
url: /th/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การใช้ Twist ใน Linear Extrusion ด้วย Aspose.3D สำหรับ Java

## บทนำ

ยินดีต้อนรับสู่บทแนะนำแบบขั้นตอนต่อขั้นตอนเกี่ยวกับ **วิธีสร้างโมเดล 3 มิติที่บิด** โดยการใช้ twist ระหว่างการทำ linear extrusion ด้วย Aspose.3D สำหรับ Java ไม่ว่าคุณจะสร้างภาพจำลองสถาปัตยกรรม, สินทรัพย์เกม, หรือโพรโทไทป์ด้านวิศวกรรม การเพิ่ม twist สามารถทำให้รูปทรงของคุณดูมีความเคลื่อนไหวและเป็นสไปรัลได้ด้วยเพียงไม่กี่บรรทัดของโค้ด

## คำตอบด่วน
- **“twist” หมายถึงอะไรใน extrusion?** มันทำการหมุนโปรไฟล์รอบแกน extrusion ขณะที่รูปร่างถูกขยายออก  
- **คลาส API ใดที่จัดการ twist?** `LinearExtrusion` มีเมธอด `setTwist`  
- **ฉันต้องมีไลเซนส์เพื่อรันตัวอย่างหรือไม่?** เวอร์ชันทดลองฟรีใช้ได้สำหรับการประเมิน; จำเป็นต้องมีไลเซนส์เชิงพาณิชย์สำหรับการใช้งานจริง  
- **ฉันสามารถส่งออกผลลัพธ์เป็น OBJ ได้หรือไม่?** ใช่, ใช้ `scene.save(..., FileFormat.WAVEFRONTOBJ)`  
- **ต้องการเวอร์ชัน Java ใด?** รองรับ Java 8 หรือใหม่กว่าอย่างเต็มที่  

## ข้อกำหนดเบื้องต้น

ก่อนจะลงลึกในบทแนะนำ, ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดต่อไปนี้พร้อมใช้งาน:

- สภาพแวดล้อมการพัฒนา Java: ตรวจสอบว่าคุณได้ติดตั้ง Java บนระบบของคุณแล้ว  
- ไลบรารี Aspose.3D: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D สำหรับ Java จาก [download link](https://releases.aspose.com/3d/java/).  
- เอกสารอ้างอิง: ดูที่ [Aspose.3D documentation](https://reference.aspose.com/3d/java/) เพื่อคำแนะนำที่ครอบคลุม  

## นำเข้าแพ็กเกจ

ก่อนเริ่มกระบวนการเขียนโค้ด, นำเข้าแพ็กเกจที่จำเป็นเข้าสู่โครงการ Java ของคุณ ตัวอย่างเช่น:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ตั้งค่าไดเรกทอรีเอกสาร

แรกสุด, กำหนดตำแหน่งที่ไฟล์ 3D ที่สร้างขึ้นจะถูกบันทึก

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## เริ่มต้น Base Profile

ต่อไป, สร้างรูปทรงที่จะทำ extrusion ในตัวอย่างนี้เราใช้สี่เหลี่ยมที่มีรัศมีการโค้งเล็กน้อย

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## สร้าง Scene

อ็อบเจ็กต์ `Scene` ทำหน้าที่เป็นคอนเทนเนอร์สำหรับโหนด 3D ทั้งหมด

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## สร้าง Nodes

เพิ่มโหนดลูกสองโหนดลงใน scene – หนึ่งโหนดจะคงเป็นเส้นตรง, อีกโหนดหนึ่งจะรับ twist

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Linear Extrusion Twist

ตอนนี้เราจะทำ **linear extrusion twist** บนโหนดทั้งสอง โหนดซ้ายจะได้รับ twist 0° (เส้นตรง), ส่วนโหนดขวาจะได้รับ twist 90° เพื่อสร้างรูปทรงสไปรัล เรายังตั้งค่าจำนวน slices เพื่อให้ได้เรขาคณิตที่เรียบเนียน

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## ส่งออกไฟล์ OBJ ด้วย Java

สุดท้าย, บันทึก scene ในรูปแบบ OBJ ที่ได้รับการสนับสนุนอย่างกว้างขวาง นี้แสดงความสามารถ **export OBJ file Java** ของ Aspose.3D

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## ทำไมเรื่องนี้ถึงสำคัญ

การสร้างโมเดล 3D ที่บิดให้คุณได้เอฟเฟกต์ภาพที่ทรงพลังโดยไม่ต้องใช้เครื่องมือโมเดลภายนอก มีประโยชน์โดยเฉพาะสำหรับ:

- **ชิ้นส่วนเครื่องกล** ที่ต้องการลักษณะเฮลิกซ์ (เช่น สปริง, สกรู)  
- **การออกแบบศิลปะ** ที่สไปรัลอ่อนๆ เพิ่มความน่าสนใจ  
- **สินทรัพย์เกม** ที่ได้ประโยชน์จากรูปทรง low‑poly ที่สร้างโดยอัตโนมัติ  

## ปัญหาที่พบบ่อยและเคล็ดลับ

| ปัญหา | วิธีแก้ |
|-------|----------|
| Twist ปรากฏเป็นแบนหรือหายไป | ตรวจสอบให้แน่ใจว่า `setSlices` มีค่ามากพอ (เช่น 100) เพื่อการหมุนที่เรียบเนียน |
| ไฟล์ OBJ ไม่เปิดในโปรแกรมดู | ตรวจสอบว่าเส้นทางออก (`MyDir`) ถูกต้องและไฟล์มีสิทธิ์เขียน |
| การสเกลที่ไม่คาดคิด | ตรวจสอบระบบหน่วยของโปรไฟล์ต้นทาง; Aspose.3D ใช้หน่วยเมตรเป็นค่าเริ่มต้น |

## คำถามที่พบบ่อย

**ถาม: ฉันสามารถใช้ Aspose.3D สำหรับ Java ทำงานกับรูปแบบไฟล์ 3D อื่นได้หรือไม่?**  
ตอบ: ใช่, Aspose.3D รองรับรูปแบบไฟล์หลากหลายเช่น FBX, STL, 3MF, และอื่นๆ  

**ถาม: ฉันจะหาแหล่งสนับสนุนสำหรับ Aspose.3D สำหรับ Java ได้จากที่ไหน?**  
ตอบ: เยี่ยมชม [Aspose.3D forum](https://forum.aspose.com/c/3d/18) เพื่อรับความช่วยเหลือจากชุมชนและการสนับสนุนอย่างเป็นทางการ.  

**ถาม: มีเวอร์ชันทดลองฟรีหรือไม่?**  
ตอบ: มี, คุณสามารถดาวน์โหลดเวอร์ชันทดลองได้จาก [ที่นี่](https://releases.aspose.com/).  

**ถาม: ฉันจะขอรับไลเซนส์ชั่วคราวสำหรับการทดสอบได้อย่างไร?**  
ตอบ: รับไลเซนส์ชั่วคราวจาก [temporary license page](https://purchase.aspose.com/temporary-license/).  

**ถาม: ฉันจะซื้อไลเซนส์เต็มได้จากที่ไหน?**  
ตอบ: ซื้อ Aspose.3D สำหรับ Java จาก [buying page](https://purchase.aspose.com/buy).  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**อัปเดตล่าสุด:** 2025-12-17  
**ทดสอบด้วย:** Aspose.3D 24.11 for Java**ผู้เขียน:** Aspose  

---