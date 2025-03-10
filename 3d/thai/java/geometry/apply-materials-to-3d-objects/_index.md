---
title: ใช้วัสดุกับวัตถุ 3 มิติใน Java ด้วย Aspose.3D
linktitle: ใช้วัสดุกับวัตถุ 3 มิติใน Java ด้วย Aspose.3D
second_title: Aspose.3D จาวา API
description: สำรวจโลกของกราฟิก 3 มิติด้วย Aspose.3D สำหรับ Java เรียนรู้วิธีการนำวัสดุไปใช้กับวัตถุ 3 มิติได้อย่างราบรื่น ยกระดับโครงการของคุณด้วยภาพที่สมจริง
weight: 14
url: /th/java/geometry/apply-materials-to-3d-objects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ใช้วัสดุกับวัตถุ 3 มิติใน Java ด้วย Aspose.3D

## การแนะนำ

ในโลกแบบไดนามิกของกราฟิก 3D Aspose.3D สำหรับ Java มีความโดดเด่นในฐานะเครื่องมืออันทรงพลังในการทำให้โปรเจ็กต์ของคุณมีชีวิตชีวา การเพิ่มวัสดุให้กับวัตถุ 3 มิติช่วยเพิ่มความน่าดึงดูดทางสายตา ทำให้วัตถุมีความสมจริงมากขึ้น ในบทช่วยสอนนี้ เราจะแนะนำคุณตลอดขั้นตอนการนำวัสดุไปใช้กับคิวบ์ 3 มิติโดยใช้ Aspose.3D สำหรับ Java

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

- ติดตั้ง Java Development Kit (JDK) บนระบบของคุณ
- ดาวน์โหลดและเพิ่ม Aspose.3D สำหรับไลบรารี Java ลงในโปรเจ็กต์ของคุณ
- ความคุ้นเคยกับแนวคิดการเขียนโปรแกรม Java ขั้นพื้นฐาน

## แพ็คเกจนำเข้า

ในการเริ่มต้น ให้นำเข้าแพ็คเกจที่จำเป็นไปยังโปรเจ็กต์ Java ของคุณ เพิ่มบรรทัดต่อไปนี้ที่จุดเริ่มต้นของโค้ดของคุณ:

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## ขั้นตอนที่ 1: เริ่มต้นวัตถุฉาก

```java
// เริ่มต้นวัตถุฉาก
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: เริ่มต้นวัตถุ Cube Node

```java
// เตรียมข้อมูลเบื้องต้นให้กับอ็อบเจ็กต์โหนดคิวบ์
Node cubeNode = new Node("cube");
```

## ขั้นตอนที่ 3: สร้าง Mesh โดยใช้ Polygon Builder

```java
// เรียกคลาส Common สร้าง mesh โดยใช้วิธีสร้างรูปหลายเหลี่ยมเพื่อตั้งค่าอินสแตนซ์ mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## ขั้นตอนที่ 4: ชี้โหนดไปที่ตาข่าย

```java
// ชี้โหนดไปที่ตาข่าย
cubeNode.setEntity(mesh);
```

## ขั้นตอนที่ 5: เพิ่ม Cube ลงในฉาก

```java
// เพิ่มลูกบาศก์ลงในฉาก
scene.getRootNode().addChildNode(cubeNode);
```

## ขั้นตอนที่ 6: เริ่มต้นวัตถุ PhongMaterial

```java
// เริ่มต้นวัตถุ PhongMaterial
PhongMaterial mat = new PhongMaterial();
```

## ขั้นตอนที่ 7: เริ่มต้นวัตถุพื้นผิว

```java
// เริ่มต้นวัตถุพื้นผิว
Texture diffuse = new Texture();
```

## ขั้นตอนที่ 8: ตั้งค่าเส้นทางไฟล์ในเครื่องสำหรับพื้นผิว

```java
// เส้นทางไปยังไดเร็กทอรีเอกสาร
String MyDir = "Your Document Directory";
```

## ขั้นตอนที่ 9: ตั้งค่าเส้นทางไฟล์ในเครื่องสำหรับพื้นผิวที่ฝัง

```java
// กำหนดเส้นทางไฟล์ในเครื่องสำหรับพื้นผิวที่ฝัง
diffuse.setFileName(MyDir + "surface.dds");
```

## ขั้นตอนที่ 10: ตั้งค่าพื้นผิวของวัสดุ

```java
// กำหนดพื้นผิวของวัสดุ
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## ขั้นตอนที่ 11: ฝังข้อมูลเนื้อหาดิบลงใน FBX (ไม่บังคับ)

```java
// ตั้งชื่อไฟล์สำหรับพื้นผิวที่ฝัง
diffuse.setFileName("embedded-texture.png");
// ตั้งค่าเนื้อหาไบนารี
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## ขั้นตอนที่ 12: ตั้งค่าสีพิเศษ

```java
// ตั้งค่าสีพิเศษ
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## ขั้นตอนที่ 13: ตั้งค่าความสว่าง

```java
// ตั้งค่าความสว่าง
mat.setShininess(100);
```

## ขั้นตอนที่ 14: ตั้งค่าคุณสมบัติวัสดุของวัตถุ Cube

```java
// ตั้งค่าคุณสมบัติวัสดุของวัตถุคิวบ์
cubeNode.setMaterial(mat);
```

## ขั้นตอนที่ 15: บันทึกฉาก 3 มิติ

```java
// ตั้งชื่อไฟล์
MyDir = MyDir + "MaterialToCube.fbx";
// บันทึกฉาก 3 มิติในรูปแบบไฟล์ที่รองรับ
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## บทสรุป

ยินดีด้วย! คุณนำวัสดุไปใช้กับลูกบาศก์ 3 มิติโดยใช้ Aspose.3D สำหรับ Java ได้สำเร็จ เทคนิคที่เรียบง่ายแต่ทรงพลังนี้สามารถยกระดับโปรเจ็กต์ 3D ของคุณไปสู่อีกระดับหนึ่ง โดยมอบประสบการณ์ที่สมจริงและน่าทึ่ง

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้วัสดุหลายรายการกับวัตถุ 3 มิติชิ้นเดียวได้หรือไม่

ตอบ 1: ได้ Aspose.3D อนุญาตให้คุณใช้วัสดุหลายชนิดกับส่วนต่างๆ ของวัตถุ 3 มิติเพื่อการปรับแต่งที่ดียิ่งขึ้น

### คำถามที่ 2: Aspose.3D รองรับไฟล์รูปแบบใดบ้างในการบันทึกฉาก

 A2: Aspose.3D รองรับไฟล์ได้หลากหลายรูปแบบ รวมถึง FBX, STL และ 3DS อ้างถึง[เอกสารประกอบ](https://reference.aspose.com/3d/java/) สำหรับรายการทั้งหมด

### คำถามที่ 3: มีใบอนุญาตชั่วคราวสำหรับ Aspose.3D สำหรับ Java หรือไม่

 A3: ใช่ คุณสามารถขอรับ[ใบอนุญาตชั่วคราว](https://purchase.aspose.com/temporary-license/) เพื่อวัตถุประสงค์ในการประเมินผล

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้ที่ไหน

 A4: เยี่ยมชม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและการอภิปรายของชุมชน

### คำถามที่ 5: ฉันสามารถดาวน์โหลดไลบรารี Aspose.3D จากลิงก์เฉพาะได้หรือไม่

 A5: ใช่ ใช้[ลิ้งค์ดาวน์โหลด](https://releases.aspose.com/3d/java/) เพื่อเข้าถึง Aspose.3D สำหรับ Java เวอร์ชันล่าสุด
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
