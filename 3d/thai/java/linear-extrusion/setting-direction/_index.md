---
title: การตั้งค่าทิศทางในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java
linktitle: การตั้งค่าทิศทางในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java
second_title: Aspose.3D จาวา API
description: เชี่ยวชาญการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java! ปฏิบัติตามคำแนะนำของเราสำหรับการเขียนโปรแกรม 3D ที่ราบรื่น ดาวน์โหลดทันทีเพื่อประสบการณ์อันน่าหลงใหล
weight: 12
url: /th/java/linear-extrusion/setting-direction/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# การตั้งค่าทิศทางในการอัดขึ้นรูปเชิงเส้นด้วย Aspose.3D สำหรับ Java

## การแนะนำ

ยินดีต้อนรับสู่คำแนะนำทีละขั้นตอนเกี่ยวกับการกำหนดทิศทางในการอัดขึ้นรูปเชิงเส้นโดยใช้ Aspose.3D สำหรับ Java Aspose.3D เป็นไลบรารี Java อันทรงพลังที่ช่วยให้นักพัฒนาสามารถทำงานกับไฟล์และฉาก 3D ได้อย่างราบรื่น ในบทช่วยสอนนี้ เราจะมุ่งเน้นไปที่งานเฉพาะในการกำหนดทิศทางในการอัดขึ้นรูปเชิงเส้น ซึ่งช่วยเพิ่มความเชี่ยวชาญในการเขียนโปรแกรม 3D

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

- ความรู้พื้นฐานเกี่ยวกับภาษาการเขียนโปรแกรม Java
-  ติดตั้งไลบรารี Aspose.3D แล้ว คุณสามารถดาวน์โหลดได้จาก[ที่นี่](https://releases.aspose.com/3d/java/).
- สภาพแวดล้อมการพัฒนาแบบรวม (IDE) สำหรับ Java เช่น Eclipse หรือ IntelliJ

## แพ็คเกจนำเข้า

ตรวจสอบให้แน่ใจว่าคุณนำเข้าแพ็คเกจที่จำเป็นเพื่อเริ่มต้นโปรเจ็กต์ของคุณ:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ขั้นตอนที่ 1: เริ่มต้นโปรไฟล์ฐาน

 เริ่มต้นด้วยการเริ่มต้นโปรไฟล์ฐานที่จะทำการอัดขึ้นรูป ในตัวอย่างนี้ เราใช้ a`RectangleShape` ด้วยรัศมีการปัดเศษ 0.3:

```java
// เส้นทางไปยังไดเร็กทอรีเอกสาร
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## ขั้นตอนที่ 2: สร้างฉาก

จากนั้น สร้างฉาก 3 มิติเพื่อบรรจุวัตถุที่อัดออกมา:

```java
Scene scene = new Scene();
```

## ขั้นตอนที่ 3: สร้างโหนด

สร้างโหนดด้านซ้ายและขวาภายในฉาก:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ขั้นตอนที่ 4: ดำเนินการอัดขึ้นรูปเชิงเส้นบนโหนดด้านซ้าย

 ดำเนินการอัดขึ้นรูปเชิงเส้นบนโหนดด้านซ้ายโดยใช้`LinearExtrusion`คลาสที่มีพารามิเตอร์ที่ระบุ เช่น twist และ Slice:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## ขั้นตอนที่ 5: ดำเนินการอัดขึ้นรูปเชิงเส้นบนโหนดด้านขวาพร้อมทิศทาง

 ดำเนินการอัดขึ้นรูปเชิงเส้นบนโหนดด้านขวา โดยแนะนำ`setDirection` คุณสมบัติเพื่อกำหนดทิศทางการอัดขึ้นรูป:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## ขั้นตอนที่ 6: บันทึกฉาก 3 มิติ

บันทึกฉาก 3D เป็นรูปแบบไฟล์ที่ต้องการ ในตัวอย่างนี้ เราบันทึกเป็นไฟล์ Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## บทสรุป

ยินดีด้วย! คุณได้เรียนรู้วิธีกำหนดทิศทางในการอัดขึ้นรูปเชิงเส้นโดยใช้ Aspose.3D สำหรับ Java เรียบร้อยแล้ว บทช่วยสอนนี้ช่วยเพิ่มทักษะของคุณในการเขียนโปรแกรม 3D และเปิดโอกาสใหม่ๆ สำหรับโครงการสร้างสรรค์

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D กับภาษาการเขียนโปรแกรมอื่นได้หรือไม่

A1: Aspose.3D รองรับภาษาการเขียนโปรแกรมที่หลากหลาย รวมถึง .NET และ Java

### ไตรมาสที่ 2 มีการทดลองใช้ Aspose.3D ฟรีหรือไม่

 ตอบ 2: ได้ คุณสามารถสำรวจฟีเจอร์ของ Aspose.3D ได้ด้วยการทดลองใช้ฟรี[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 3: ฉันจะหาเอกสารโดยละเอียดสำหรับ Aspose.3D สำหรับ Java ได้ที่ไหน

 A3: มีเอกสารประกอบที่ครอบคลุม[ที่นี่](https://reference.aspose.com/3d/java/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร

 A4: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับความช่วยเหลือหรือข้อสงสัยใด ๆ

### คำถามที่ 5: Aspose.3D มีใบอนุญาตชั่วคราวหรือไม่

 A5: ได้ คุณสามารถขอรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
