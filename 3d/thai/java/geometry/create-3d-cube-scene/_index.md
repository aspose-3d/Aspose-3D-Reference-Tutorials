---
title: สร้างฉาก 3D Cube ใน Java ด้วย Aspose.3D
linktitle: สร้างฉาก 3D Cube ใน Java ด้วย Aspose.3D
second_title: Aspose.3D จาวา API
description: สำรวจความมหัศจรรย์ของกราฟิกฉากคิวบ์ 3 มิติด้วย Aspose.3D สำหรับ Java สร้างฉากที่น่าทึ่งได้อย่างง่ายดาย
weight: 12
url: /th/java/geometry/create-3d-cube-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# สร้างฉาก 3D Cube ใน Java ด้วย Aspose.3D

## การแนะนำ

ยินดีต้อนรับสู่โลกที่น่าหลงใหลของกราฟิก 3 มิติใน Java โดยใช้ Aspose.3D! ในบทช่วยสอนนี้ เราจะแนะนำคุณตลอดกระบวนการสร้างฉากคิวบ์ 3 มิติที่น่าทึ่งโดยใช้ Aspose.3D สำหรับ Java Aspose.3D เป็นไลบรารี Java ที่ทรงพลังซึ่งมีฟังก์ชันการทำงานที่ครอบคลุมสำหรับการทำงานกับโมเดลและฉาก 3D

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเจาะลึกการสร้างฉากคิวบ์ 3D ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

1.  Java Development Kit (JDK): ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง Java บนระบบของคุณแล้ว คุณสามารถดาวน์โหลดเวอร์ชันล่าสุดได้จาก[เว็บไซต์ของออราเคิล](https://www.oracle.com/java/).

2.  Aspose.3D สำหรับไลบรารี Java: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D คุณสามารถค้นหาลิงค์ดาวน์โหลด[ที่นี่](https://releases.aspose.com/3d/java/).

## แพ็คเกจนำเข้า

เริ่มต้นด้วยการนำเข้าแพ็คเกจที่จำเป็นไปยังโปรเจ็กต์ Java ของคุณ:

```java
import java.io.File;

import com.aspose.threed.Box;
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.Scene;
```

ตอนนี้ เรามาแบ่งกระบวนการสร้างฉากคิวบ์ 3D ออกเป็นหลายขั้นตอนกัน

## ขั้นตอนที่ 1: เริ่มต้นฉาก

```java
// เริ่มต้นวัตถุฉาก
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: เริ่มต้นโหนดและตาข่าย

```java
// เริ่มต้นวัตถุคลาสโหนด
Node cubeNode = new Node("box");

// เรียกคลาส Common สร้าง mesh โดยใช้วิธีสร้างรูปหลายเหลี่ยมเพื่อตั้งค่าอินสแตนซ์ mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// ชี้โหนดไปที่เรขาคณิตของ Mesh
cubeNode.setEntity(mesh);
```

## ขั้นตอนที่ 3: เพิ่มโหนดในฉาก

```java
// เพิ่มโหนดให้กับฉาก
scene.getRootNode().getChildNodes().add(cubeNode);
```

## ขั้นตอนที่ 4: บันทึกฉาก 3 มิติ

```java
// เส้นทางไปยังไดเร็กทอรีเอกสาร
String MyDir = "Your Document Directory";
MyDir = MyDir + "CubeScene.fbx";

// บันทึกฉาก 3 มิติในรูปแบบไฟล์ที่รองรับ
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## ขั้นตอนที่ 5: พิมพ์ข้อความแสดงความสำเร็จ

```java
System.out.println("\nCube Scene created successfully.\nFile saved at " + MyDir);
```

## บทสรุป

ยินดีด้วย! คุณสร้างฉากคิวบ์ 3 มิติโดยใช้ Aspose.3D สำหรับ Java สำเร็จแล้ว บทช่วยสอนนี้เป็นรากฐานที่มั่นคงสำหรับการสำรวจคุณสมบัติขั้นสูงเพิ่มเติม และปลดปล่อยความคิดสร้างสรรค์ของคุณในโลกของกราฟิก 3 มิติ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่

 A1: ใช่คุณทำได้ ตรวจสอบ[หน้าซื้อ](https://purchase.aspose.com/buy) สำหรับรายละเอียดใบอนุญาต

### คำถามที่ 2: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร

 A2: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อสนับสนุนชุมชน

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

 A3: ใช่ คุณสามารถทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะหาเอกสารสำหรับ Aspose.3D ได้ที่ไหน

 A4: โปรดดูที่[เอกสาร Aspose.3D](https://reference.aspose.com/3d/java/) สำหรับข้อมูลโดยละเอียด

### คำถามที่ 5: จะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร

 A5: คุณสามารถรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
