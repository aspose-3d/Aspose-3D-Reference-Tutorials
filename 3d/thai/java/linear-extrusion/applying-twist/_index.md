---
title: การใช้ Twist ในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java
linktitle: การใช้ Twist ในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java
second_title: Aspose.3D จาวา API
description: เรียนรู้วิธีเพิ่มความแปลกใหม่ให้กับโมเดล 3 มิติของคุณโดยใช้ Aspose.3D สำหรับ Java ปฏิบัติตามคำแนะนำทีละขั้นตอนของเราเพื่อเพิ่มเอฟเฟกต์การอัดขึ้นรูปเชิงเส้น
weight: 14
url: /th/java/linear-extrusion/applying-twist/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การใช้ Twist ในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java

## การแนะนำ

ยินดีต้อนรับสู่บทช่วยสอนแบบทีละขั้นตอนเกี่ยวกับการใช้การบิดในการอัดขึ้นรูปเชิงเส้นโดยใช้ Aspose.3D สำหรับ Java Aspose.3D เป็นไลบรารี Java อันทรงพลังที่ช่วยให้นักพัฒนาสามารถทำงานกับรูปแบบไฟล์ 3D ได้ โดยมีฟังก์ชันการทำงานที่มีประสิทธิภาพสำหรับการสร้าง จัดการ และเรนเดอร์ฉาก 3D ในบทช่วยสอนนี้ เราจะสำรวจวิธีการใช้เอฟเฟกต์การบิดในระหว่างกระบวนการอัดขึ้นรูปเชิงเส้นเพื่อปรับปรุงโมเดล 3D ของคุณ

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

- สภาพแวดล้อมการพัฒนา Java: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง Java บนระบบของคุณแล้ว
-  ไลบรารี Aspose.3D: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D สำหรับ Java จาก[ลิ้งค์ดาวน์โหลด](https://releases.aspose.com/3d/java/).
-  เอกสารประกอบ: โปรดดูที่[เอกสาร Aspose.3D](https://reference.aspose.com/3d/java/) เพื่อรับคำแนะนำอย่างครอบคลุม

## แพ็คเกจนำเข้า

ก่อนที่จะเริ่มกระบวนการเขียนโค้ด ให้นำเข้าแพ็คเกจที่จำเป็นไปยังโปรเจ็กต์ Java ของคุณ นี่คือตัวอย่างวิธีการดำเนินการนี้:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ขั้นตอนที่ 1: ตั้งค่าไดเรกทอรีเอกสาร

เริ่มต้นด้วยการตั้งค่าไดเร็กทอรีเอกสารที่จะบันทึกฉาก 3 มิติของคุณ

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## ขั้นตอนที่ 2: เริ่มต้นโปรไฟล์ฐาน

เริ่มต้นโปรไฟล์ฐานที่จะทำการอัดขึ้นรูป ในตัวอย่างนี้ เราใช้รูปทรงสี่เหลี่ยมผืนผ้าที่มีรัศมีการปัดเศษ

```java
// ExStart: เตรียมใช้งาน BaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:เตรียมใช้งาน BaseProfile
```

## ขั้นตอนที่ 3: สร้างฉาก

สร้างฉาก 3 มิติเพื่อโฮสต์โหนดที่ถูกอัดขึ้นรูป

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ตัวอย่าง: CreateScene
```

## ขั้นตอนที่ 4: สร้างโหนด

สร้างโหนดด้านซ้ายและขวาภายในฉาก ปรับการแปลโหนดด้านซ้าย

```java
// ExStart: สร้างโหนด
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd: สร้างโหนด
```

## ขั้นตอนที่ 5: ดำเนินการอัดขึ้นรูปเชิงเส้นด้วย Twist

ดำเนินการอัดขึ้นรูปเชิงเส้นบนโหนดทั้งซ้ายและขวา โดยใช้คุณสมบัติการบิดและการแบ่งส่วน

```java
// ExStart:การอัดขึ้นรูปเชิงเส้นด้วยบิด
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:การอัดขึ้นรูปเชิงเส้นด้วยบิด
```

## ขั้นตอนที่ 6: บันทึกฉาก 3 มิติ

บันทึกฉาก 3 มิติในรูปแบบไฟล์ Wavefront OBJ

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:Save3DScene
```

## บทสรุป

ยินดีด้วย! คุณใช้การบิดในการอัดขึ้นรูปเชิงเส้นโดยใช้ Aspose.3D สำหรับ Java ได้สำเร็จ บทช่วยสอนนี้ให้คำแนะนำโดยละเอียดทีละขั้นตอนเพื่อช่วยคุณปรับปรุงความสามารถในการสร้างแบบจำลอง 3 มิติของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ Java เพื่อทำงานกับไฟล์ 3D รูปแบบอื่นๆ ได้หรือไม่

ตอบ 1: ใช่ Aspose.3D รองรับรูปแบบไฟล์ 3D ที่หลากหลาย ทำให้คุณสามารถนำเข้า ส่งออก และจัดการไฟล์ประเภทต่างๆ ได้

### คำถามที่ 2: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D สำหรับ Java ได้ที่ไหน

 A2: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายของชุมชน

### คำถามที่ 3: Aspose.3D สำหรับ Java มีรุ่นทดลองใช้ฟรีหรือไม่

 A3: ใช่ คุณสามารถเข้าถึงเวอร์ชันทดลองใช้ฟรีได้จาก[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ Java ได้อย่างไร

 A4: รับใบอนุญาตชั่วคราวจาก[หน้าใบอนุญาตชั่วคราว](https://purchase.aspose.com/temporary-license/).

### คำถามที่ 5: ฉันจะซื้อ Aspose.3D สำหรับ Java ได้ที่ไหน

 A5: ซื้อ Aspose.3D สำหรับ Java จาก[หน้าซื้อ](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
