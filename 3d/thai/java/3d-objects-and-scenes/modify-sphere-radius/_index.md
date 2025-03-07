---
title: ปรับเปลี่ยนรัศมี 3D Sphere ใน Java ด้วย Aspose.3D
linktitle: ปรับเปลี่ยนรัศมี 3D Sphere ใน Java ด้วย Aspose.3D
second_title: Aspose.3D จาวา API
description: สำรวจการเขียนโปรแกรม Java 3D ด้วย Aspose.3D ปรับเปลี่ยนรัศมีทรงกลมได้อย่างง่ายดาย ดาวน์โหลดทันทีเพื่อประสบการณ์การพัฒนา 3D ที่ราบรื่น
weight: 10
url: /th/java/3d-objects-and-scenes/modify-sphere-radius/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ปรับเปลี่ยนรัศมี 3D Sphere ใน Java ด้วย Aspose.3D

## การแนะนำ

ยินดีต้อนรับสู่คำแนะนำทีละขั้นตอนเกี่ยวกับการปรับเปลี่ยนรัศมีของทรงกลม 3 มิติโดยใช้ Aspose.3D สำหรับ Java Aspose.3D เป็นไลบรารี Java อันทรงพลังที่ช่วยให้นักพัฒนาสามารถทำงานกับไฟล์ 3D และจัดการไฟล์เหล่านั้นได้อย่างราบรื่น ในบทช่วยสอนนี้ เราจะเน้นที่การเปลี่ยนรัศมีของทรงกลม 3 มิติโดยใช้ตัวอย่างที่ใช้งานได้จริงและคำอธิบายโดยละเอียด

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม Java
-  ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้จาก[Aspose.3D สำหรับเอกสาร Java](https://reference.aspose.com/3d/java/).
- ติดตั้ง Java Development Kit (JDK) บนเครื่องของคุณแล้ว

## แพ็คเกจนำเข้า

ในการเริ่มต้น ให้นำเข้าแพ็คเกจที่จำเป็นไปยังโปรเจ็กต์ Java ของคุณ เพิ่มบรรทัดต่อไปนี้ลงในโค้ดของคุณ:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## ขั้นตอนที่ 1: เริ่มต้นฉาก

```java
// ExStart:WorkingWithSphereRadius

// เริ่มต้นฉาก
Scene scene = new Scene();
```

ที่นี่ เราสร้างฉาก 3 มิติใหม่โดยใช้ Aspose.3D สำหรับ Java

## ขั้นตอนที่ 2: เริ่มต้นทรงกลม

```java
// เริ่มต้น Sphere
Sphere sphere = new Sphere();
```

สร้างวัตถุ Sphere ใหม่ที่จะถูกเพิ่มลงในฉาก

## ขั้นตอนที่ 3: ตั้งค่ารัศมี

```java
// ตั้งรัศมี
sphere.setRadius(10);
```

กำหนดรัศมีที่ต้องการสำหรับทรงกลม ในตัวอย่างนี้ เราตั้งค่าเป็น 10 หน่วย

## ขั้นตอนที่ 4: เพิ่ม Sphere ให้กับฉาก

```java
// เพิ่มทรงกลมให้กับฉาก
scene.getRootNode().createChildNode(sphere);
```

เพิ่มทรงกลมที่สร้างขึ้นไปยังโหนดรูทของฉาก

## ขั้นตอนที่ 5: บันทึกฉาก

```java
// บันทึกฉาก
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

บันทึกฉากที่แก้ไขด้วยทรงกลมใหม่เป็นไฟล์ 3D ในกรณีนี้ เราจะบันทึกเป็น "sphere.obj" ในรูปแบบ Wavefront OBJ

## บทสรุป

ยินดีด้วย! คุณได้แก้ไขรัศมีทรงกลม 3 มิติโดยใช้ Aspose.3D สำหรับ Java สำเร็จแล้ว บทช่วยสอนนี้ให้คำแนะนำที่ชัดเจนและกระชับ ช่วยให้คุณสามารถรวมขั้นตอนเหล่านี้เข้ากับโปรเจ็กต์ Java ของคุณได้อย่างง่ายดาย

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันจะหาเอกสารสำหรับ Aspose.3D สำหรับ Java ได้ที่ไหน

 A1: คุณสามารถอ้างถึง[Aspose.3D สำหรับเอกสาร Java](https://reference.aspose.com/3d/java/) เพื่อรับข้อมูลและแนวทางการใช้งานอย่างครอบคลุม

### คำถามที่ 2: ฉันจะดาวน์โหลด Aspose.3D สำหรับ Java ได้อย่างไร

 A2: คุณสามารถดาวน์โหลดไลบรารีได้จากหน้าเผยแพร่:[ดาวน์โหลด Aspose.3D สำหรับ Java](https://releases.aspose.com/3d/java/).

### คำถามที่ 3: Aspose.3D สำหรับ Java มีรุ่นทดลองใช้ฟรีหรือไม่

 A3: ได้ คุณสามารถสำรวจฟีเจอร์ต่างๆ พร้อมทดลองใช้ฟรีได้โดยไปที่[Aspose.3D ทดลองใช้ฟรี](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D สำหรับ Java ได้ที่ไหน

 A4: เข้าร่วมชุมชน Aspose ได้ที่[ฟอรัมสนับสนุน Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อขอความช่วยเหลือและหารือ

### คำถามที่ 5: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร

 A5: คุณสามารถรับใบอนุญาตชั่วคราวได้โดยไปที่[ใบอนุญาตชั่วคราว](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
