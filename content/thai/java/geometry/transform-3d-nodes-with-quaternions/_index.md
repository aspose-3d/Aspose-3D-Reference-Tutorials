---
title: แปลงโหนด 3 มิติด้วย Quaternions ใน Java โดยใช้ Aspose.3D
linktitle: แปลงโหนด 3 มิติด้วย Quaternions ใน Java โดยใช้ Aspose.3D
second_title: Aspose.3D จาวา API
description: ปรับปรุงแอปพลิเคชัน Java ของคุณด้วย Aspose.3D เพื่อการแปลง 3D อันทรงพลัง เรียนรู้การแปลงโหนดโดยใช้ควอเทอร์เนียนในคำแนะนำทีละขั้นตอนนี้
type: docs
weight: 20
url: /th/java/geometry/transform-3d-nodes-with-quaternions/
---
## การแนะนำ

ยินดีต้อนรับสู่คำแนะนำทีละขั้นตอนเกี่ยวกับการแปลงโหนด 3D ด้วยควอเทอร์เนียนใน Java โดยใช้ Aspose.3D หากคุณต้องการปรับปรุงแอปพลิเคชัน Java ของคุณด้วยการแปลง 3D อันทรงพลัง บทช่วยสอนนี้เหมาะสำหรับคุณ Aspose.3D สำหรับ Java มอบชุดคุณลักษณะที่มีประสิทธิภาพสำหรับการทำงานกับกราฟิก 3D และในบทช่วยสอนนี้ เราจะเน้นที่การแปลงโหนด 3D โดยใช้ควอเทอร์เนียน

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

- ความรู้พื้นฐานเกี่ยวกับการเขียนโปรแกรม Java
-  ติดตั้ง Aspose.3D สำหรับ Java แล้ว คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/java/).
- ไดเร็กทอรีเอกสารที่ตั้งค่าไว้สำหรับบันทึกฉาก 3 มิติของคุณ

## แพ็คเกจนำเข้า

ในส่วนนี้ เราจะนำเข้าแพ็คเกจที่จำเป็นเพื่อเริ่มต้นการแปลงสามมิติโดยใช้ Aspose.3D

```java
import com.aspose.threed.*;
```

## ขั้นตอนที่ 1: เริ่มต้นวัตถุฉาก

ในการเริ่มต้น ให้สร้างวัตถุฉากที่จะทำหน้าที่เป็นคอนเทนเนอร์สำหรับองค์ประกอบ 3 มิติของคุณ

```java
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: เริ่มต้นวัตถุคลาสโหนด

ตอนนี้ ให้สร้างอ็อบเจ็กต์คลาสโหนด ในกรณีนี้ แทนคิวบ์

```java
Node cubeNode = new Node("cube");
```

## ขั้นตอนที่ 3: สร้าง Mesh โดยใช้ Polygon Builder

ใช้คลาสทั่วไปเพื่อสร้างตาข่ายโดยใช้วิธีสร้างรูปหลายเหลี่ยม

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## ขั้นตอนที่ 4: ตั้งค่าเรขาคณิตของตาข่าย

กำหนดตาข่ายที่สร้างขึ้นให้กับโหนดคิวบ์

```java
cubeNode.setEntity(mesh);
```

## ขั้นตอนที่ 5: ตั้งค่าการหมุนด้วย Quaternion

ใช้การหมุนกับโหนดคิวบ์โดยใช้ควอเทอร์เนียน

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## ขั้นตอนที่ 6: ตั้งค่าการแปล

ระบุการแปลสำหรับโหนดคิวบ์

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## ขั้นตอนที่ 7: เพิ่ม Cube ลงในฉาก

รวมโหนดคิวบ์ไว้ในฉาก

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## ขั้นตอนที่ 8: บันทึกฉาก 3 มิติ

บันทึกฉาก 3D ในรูปแบบไฟล์ที่รองรับ เช่น FBX7500ASCII

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## บทสรุป

ยินดีด้วย! คุณได้เรียนรู้วิธีการแปลงโหนด 3D โดยใช้ควอเทอร์เนียนใน Java ด้วย Aspose.3D เรียบร้อยแล้ว ทดลองใช้การเปลี่ยนแปลงต่างๆ เพื่อทำให้แอปพลิเคชัน 3D ของคุณมีชีวิตชีวา

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับ Java ได้ฟรีหรือไม่

ตอบ 1: Aspose.3D สำหรับ Java ให้ทดลองใช้ฟรี คุณสามารถหามันได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 2: ฉันจะหาเอกสารสำหรับ Aspose.3D สำหรับ Java ได้ที่ไหน

 A2: มีเอกสารประกอบให้[ที่นี่](https://reference.aspose.com/3d/java/).

### คำถามที่ 3: ฉันจะได้รับการสนับสนุนสำหรับ Aspose.3D สำหรับ Java ได้อย่างไร

 A3: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุน

### คำถามที่ 4: มีใบอนุญาตชั่วคราวหรือไม่

 A4: ได้ คุณสามารถขอรับใบอนุญาตชั่วคราวได้[ที่นี่](https://purchase.aspose.com/temporary-license/).

### คำถามที่ 5: ฉันจะซื้อ Aspose.3D สำหรับ Java ได้ที่ไหน

 A5: คุณสามารถซื้อได้[ที่นี่](https://purchase.aspose.com/buy).