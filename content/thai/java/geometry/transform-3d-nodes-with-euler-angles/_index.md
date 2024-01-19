---
title: แปลงโหนด 3 มิติด้วย Euler Angles ใน Java โดยใช้ Aspose.3D
linktitle: แปลงโหนด 3 มิติด้วย Euler Angles ใน Java โดยใช้ Aspose.3D
second_title: Aspose.3D จาวา API
description: สำรวจโลกแห่งการเปลี่ยนแปลง 3 มิติใน Java ด้วย Aspose.3D ทำตามคำแนะนำทีละขั้นตอนของเราเพื่อเพิ่มมุมออยเลอร์แบบไดนามิกให้กับโหนด 3 มิติของคุณ
type: docs
weight: 19
url: /th/java/geometry/transform-3d-nodes-with-euler-angles/
---
## การแนะนำ

ยินดีต้อนรับสู่บทช่วยสอนแบบทีละขั้นตอนเกี่ยวกับการแปลงโหนด 3 มิติด้วยมุมออยเลอร์ใน Java โดยใช้ Aspose.3D ในคู่มือนี้ เราจะเจาะลึกกระบวนการเพิ่มการแปลงไปยังโหนด 3 มิติ โดยใช้มุมออยเลอร์เพื่อให้ได้ตำแหน่งและการวางแนวแบบไดนามิก

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

- ความรู้พื้นฐานเกี่ยวกับการเขียนโปรแกรม Java
- ติดตั้ง Java Development Kit (JDK) บนเครื่องของคุณแล้ว
-  ไลบรารี Aspose.3D ซึ่งคุณสามารถรับได้จาก[เอกสาร Java Aspose.3D](https://reference.aspose.com/3d/java/).

## แพ็คเกจนำเข้า

 เริ่มต้นด้วยการนำเข้าแพ็คเกจที่จำเป็นไปยังโปรเจ็กต์ Java ของคุณ ตรวจสอบให้แน่ใจว่าไลบรารี Aspose.3D ถูกเพิ่มใน classpath ของคุณอย่างถูกต้อง หากคุณยังไม่ได้ดาวน์โหลด คุณสามารถดูลิงก์ดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## ขั้นตอนที่ 1 เริ่มต้นฉากและโหนด

```java
// ExStart: เพิ่มการเปลี่ยนแปลง ToNodeByEulerAngles
// เริ่มต้นวัตถุฉาก
Scene scene = new Scene();

// เริ่มต้นวัตถุคลาสโหนด
Node cubeNode = new Node("cube");
```

## ขั้นตอนที่ 2 สร้าง Mesh และตั้งค่าเรขาคณิต

```java
// เรียกคลาส Common สร้าง mesh โดยใช้วิธีสร้างรูปหลายเหลี่ยมเพื่อตั้งค่าอินสแตนซ์ mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// ชี้โหนดไปที่เรขาคณิตของ Mesh
cubeNode.setEntity(mesh);
```

## ขั้นตอนที่ 3 ตั้งค่ามุมออยเลอร์และการแปล

```java
// มุมออยเลอร์
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// ตั้งค่าการแปล
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## ขั้นตอนที่ 4 เพิ่มโหนดไปที่ฉาก

```java
// เพิ่มลูกบาศก์ลงในฉาก
scene.getRootNode().getChildNodes().add(cubeNode);
```

## ขั้นตอนที่ 5 บันทึกฉาก 3 มิติ

```java
// เส้นทางไปยังไดเร็กทอรีเอกสาร
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

//บันทึกฉาก 3 มิติในรูปแบบไฟล์ที่รองรับ
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ตัวอย่าง: เพิ่มการเปลี่ยนแปลง ToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

ตรวจสอบให้แน่ใจว่าได้แทนที่ "Your Document Directory" ด้วยเส้นทางที่เหมาะสมบนเครื่องของคุณ

## บทสรุป

ยินดีด้วย! คุณแปลงโหนด 3 มิติได้สำเร็จโดยใช้มุมออยเลอร์ใน Java ด้วย Aspose.3D ทดลองกับมุมต่างๆ และการแปลเพื่อสร้างฉาก 3 มิติแบบไดนามิกและน่าดึงดูด

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ Java ในโครงการเชิงพาณิชย์ได้หรือไม่

 A1: ใช่คุณทำได้ เยี่ยมชม[หน้าซื้อ](https://purchase.aspose.com/buy) สำหรับรายละเอียดใบอนุญาต

### คำถามที่ 2: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้ที่ไหน

 A2: เดอะ[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เป็นสถานที่ขอความช่วยเหลือและเชื่อมต่อกับชุมชน

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

 A3: ใช่ คุณสามารถสำรวจได้[ทดลองฟรี](https://releases.aspose.com/) เพื่อสัมผัสความสามารถของ Aspose.3D

### คำถามที่ 4: ฉันจะขอรับใบอนุญาตชั่วคราวได้อย่างไร

 A4: คุณสามารถขอรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).

### Q5: ฉันจะหาเอกสารได้จากที่ไหน?

 A5: เดอะ[เอกสารประกอบ](https://reference.aspose.com/3d/java/) ให้คำแนะนำที่ครอบคลุมเกี่ยวกับการใช้ Aspose.3D สำหรับ Java