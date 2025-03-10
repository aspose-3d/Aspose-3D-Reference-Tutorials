---
title: ส่งออกฉาก 3 มิติเป็น Point Clouds ด้วย Aspose.3D สำหรับ Java
linktitle: ส่งออกฉาก 3 มิติเป็น Point Clouds ด้วย Aspose.3D สำหรับ Java
second_title: Aspose.3D จาวา API
description: เรียนรู้วิธีส่งออกฉาก 3 มิติเป็นพอยต์คลาวด์ใน Java ด้วย Aspose.3D ปรับปรุงแอปพลิเคชันของคุณด้วยกราฟิก 3 มิติและการแสดงภาพอันทรงพลัง
weight: 15
url: /th/java/point-clouds/export-3d-scenes-point-clouds-java/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ส่งออกฉาก 3 มิติเป็น Point Clouds ด้วย Aspose.3D สำหรับ Java

## การแนะนำ

Aspose.3D สำหรับ Java อำนวยความสะดวกในการส่งออกฉาก 3D ในรูปแบบต่างๆ รวมถึงการสร้าง point cloud พอยต์คลาวด์มีความสำคัญอย่างยิ่งในอุตสาหกรรมต่างๆ ตั้งแต่การเล่นเกมไปจนถึงการจำลอง โดยนำเสนอการแสดงพื้นที่ทางกายภาพผ่านการรวบรวมจุดในระบบพิกัด 3 มิติ

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน โปรดตรวจสอบให้แน่ใจว่ามีคุณสมบัติตรงตามข้อกำหนดเบื้องต้นต่อไปนี้:

1.  Aspose.3D สำหรับ Java Library: ดาวน์โหลดและติดตั้งไลบรารีจาก[ที่นี่](https://releases.aspose.com/3d/java/).
2. สภาพแวดล้อมการพัฒนา Java: ตั้งค่าสภาพแวดล้อมการพัฒนา Java ด้วยเวอร์ชัน 19.8 หรือสูงกว่า

## แพ็คเกจนำเข้า

เริ่มต้นด้วยการนำเข้าแพ็คเกจที่จำเป็นไปยังโปรเจ็กต์ Java ของคุณ แพ็คเกจเหล่านี้จำเป็นสำหรับการใช้ฟังก์ชัน Aspose.3D เพิ่มบรรทัดต่อไปนี้ลงในโค้ดของคุณ:

```java
import com.aspose.threed.ObjSaveOptions;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;


import java.io.IOException;
```

## ขั้นตอนที่ 1: เริ่มต้นฉาก

ในการเริ่มต้น ให้เริ่มต้นฉาก 3 มิติโดยใช้ Aspose.3D นี่คือผืนผ้าใบที่วัตถุ 3 มิติของคุณมีชีวิตขึ้นมา ใช้ข้อมูลโค้ดต่อไปนี้:

```java
// เอ็กซ์สตาร์ท:1
// เริ่มต้นฉาก
Scene scene = new Scene(new Sphere());
// สิ้นสุด:1
```

## ขั้นตอนที่ 2: เริ่มต้น ObjSaveOptions

 ตอนนี้เริ่มต้น`ObjSaveOptions`ซึ่งจัดเตรียมการตั้งค่าสำหรับการบันทึกฉาก 3D ในรูปแบบ OBJ:

```java
// เริ่มต้น ObjSaveOptions
ObjSaveOptions opt = new ObjSaveOptions();
```

## ขั้นตอนที่ 3: ตั้งค่า Point Cloud

 เปิดใช้งานคุณสมบัติการส่งออก point cloud โดยการตั้งค่า`setPointCloud` ตัวเลือกในการ`true`-

```java
// ในการส่งออกฉาก 3 มิติเป็น point cloud setPointCloud
opt.setPointCloud(true);
```

## ขั้นตอนที่ 4: บันทึกฉาก

บันทึกฉาก 3 มิติเป็นพอยต์คลาวด์ในไดเร็กทอรีที่ต้องการ:

```java
//บันทึก
scene.save("Your Document Directory" + "export3DSceneAsPointCloud.obj", opt);
```

## บทสรุป

ยินดีด้วย! คุณส่งออกฉาก 3 มิติเป็นพอยต์คลาวด์ได้สำเร็จโดยใช้ Aspose.3D สำหรับ Java บทช่วยสอนนี้ได้ให้ข้อมูลคร่าวๆ เกี่ยวกับการบูรณาการอย่างราบรื่นและความสามารถอันทรงพลังที่ Aspose.3D มอบให้กับนักพัฒนา Java

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันจะหาเอกสารประกอบ Aspose.3D สำหรับ Java ได้ที่ไหน

 A1: มีเอกสารประกอบที่ครอบคลุม[ที่นี่](https://reference.aspose.com/3d/java/).

### คำถามที่ 2: ฉันจะดาวน์โหลด Aspose.3D สำหรับ Java ได้อย่างไร

 A2: ดาวน์โหลดไลบรารี[ที่นี่](https://releases.aspose.com/3d/java/).

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

 A3: ใช่ สำรวจการทดลองใช้ฟรี[ที่นี่](https://releases.aspose.com/).

### Q4: ต้องการความช่วยเหลือหรือมีคำถาม?

 A4: เยี่ยมชมฟอรั่มชุมชน Aspose.3D[ที่นี่](https://forum.aspose.com/c/3d/18).

### คำถามที่ 5: ต้องการซื้อ Aspose.3D สำหรับ Java หรือไม่

 A5: สำรวจตัวเลือกการซื้อ[ที่นี่](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
