---
title: การระบุสไลซ์ในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java
linktitle: การระบุสไลซ์ในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java
second_title: Aspose.3D จาวา API
description: เรียนรู้วิธีระบุสไลซ์ในการอัดขึ้นรูปเชิงเส้นโดยใช้ Aspose.3D สำหรับ Java ยกระดับทักษะการสร้างแบบจำลอง 3 มิติของคุณด้วยคำแนะนำทีละขั้นตอนนี้
weight: 13
url: /th/java/linear-extrusion/specifying-slices/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การระบุสไลซ์ในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java

## การแนะนำ

การสร้างโมเดล 3 มิติที่ซับซ้อนมักต้องใช้มากกว่าความคิดสร้างสรรค์ มันต้องการความเข้าใจอย่างถ่องแท้เกี่ยวกับเครื่องมือที่คุณมี Aspose.3D สำหรับ Java เป็นตัวเปลี่ยนเกมในเรื่องนี้ ในบทช่วยสอนนี้ เราจะเน้นไปที่ลักษณะเฉพาะ - การระบุชิ้นในการอัดขึ้นรูปเชิงเส้น

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

1. สภาพแวดล้อม Java: ตรวจสอบให้แน่ใจว่าคุณได้ตั้งค่าสภาพแวดล้อมการพัฒนา Java บนระบบของคุณ
2.  Aspose.3D สำหรับ Java: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D คุณสามารถค้นหาแพ็คเกจที่จำเป็นได้[ที่นี่](https://releases.aspose.com/3d/java/).

## แพ็คเกจนำเข้า

ในโปรเจ็กต์ Java ของคุณ ให้นำเข้าไลบรารี Aspose.3D นี่เป็นสิ่งสำคัญสำหรับการเข้าถึงฟังก์ชันการทำงานที่เราจะทำงานด้วย เพิ่มคำสั่งนำเข้าต่อไปนี้ลงในรหัสของคุณ:

```java
import com.aspose.threed.*;

import java.io.IOException;
```

ตอนนี้ เรามาแบ่งตัวอย่างออกเป็นหลายขั้นตอนกัน

## ขั้นตอนที่ 1: ตั้งค่าฉาก

เริ่มต้นโปรไฟล์ฐานที่จะทำการอัด ในกรณีนี้คือ a`RectangleShape` โดยมีรัศมีการปัดเศษที่กำหนด สร้างฉาก 3 มิติเพื่อทำงานภายใน

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: สร้างโหนด

สร้างโหนดด้านซ้ายและขวาภายในฉาก ปรับการแปลโหนดด้านซ้ายสำหรับการเปลี่ยนแปลงเชิงพื้นที่

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ขั้นตอนที่ 3: การอัดขึ้นรูปเชิงเส้นด้วยชิ้น

ดำเนินการอัดรีดเชิงเส้นบนทั้งสองโหนด โดยระบุจำนวนชิ้นสำหรับแต่ละชิ้น นี่คือจุดที่ความมหัศจรรย์เกิดขึ้น

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## ขั้นตอนที่ 4: บันทึกฉาก

บันทึกฉาก 3D ในรูปแบบที่ต้องการ ในกรณีนี้คือไฟล์ Wavefront OBJ

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## บทสรุป

ยินดีด้วย! คุณได้เรียนรู้วิธีระบุชิ้นในการอัดขึ้นรูปเชิงเส้นโดยใช้ Aspose.3D สำหรับ Java เรียบร้อยแล้ว ทักษะนี้เปิดโอกาสใหม่ๆ ในเส้นทางการสร้างแบบจำลอง 3 มิติของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันจะดาวน์โหลด Aspose.3D สำหรับ Java ได้อย่างไร

 A1: คุณสามารถดาวน์โหลดห้องสมุดได้[ที่นี่](https://releases.aspose.com/3d/java/).

### คำถามที่ 2: ฉันจะหาเอกสารสำหรับ Aspose.3D ได้ที่ไหน

 A2: โปรดดูเอกสารประกอบ[ที่นี่](https://reference.aspose.com/3d/java/).

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

 A3: ได้ คุณสามารถทดลองใช้งานฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร

 A4: เยี่ยมชมฟอรั่มการสนับสนุน[ที่นี่](https://forum.aspose.com/c/3d/18).

### คำถามที่ 5: ฉันสามารถซื้อใบอนุญาตชั่วคราวได้หรือไม่

 A5: ได้ สามารถรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
