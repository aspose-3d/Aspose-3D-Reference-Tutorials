---
date: 2025-12-08
description: เรียนการสอนกราฟิก 3 มิติใน Java ว่าจะเพิ่มเทกเจอร์ใน Java อย่างไรโดยใช้
  Aspose.3D. ใช้วัสดุที่เหมือนจริงกับวัตถุ 3 มิติใน Java อย่างรวดเร็ว.
language: th
linktitle: Apply Materials to 3D Objects in Java with Aspose.3D
second_title: Aspose.3D Java API
title: บทเรียนกราฟิก 3 มิติใน Java – การใช้วัสดุกับวัตถุ 3 มิติใน Java ด้วย Aspose.3D
url: /java/geometry/apply-materials-to-3d-objects/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ใช้วัสดุกับวัตถุ 3D ใน Java ด้วย Aspose.3D

## บทนำ

ใน **java 3d graphics tutorial** นี้ เราจะสาธิต **วิธีเพิ่ม texture java** ให้กับลูกบาศก์ 3‑D ง่าย ๆ โดยใช้ Aspose.3D Java API การใช้วัสดุและเท็กซ์เจอร์เป็นขั้นตอนสำคัญที่ทำให้เมชแบนกลายเป็นวัตถุที่ดูสมจริง ซึ่งคุณสามารถนำไปใช้ในเกม การแสดงผลภาพ หรือการสาธิตผลิตภัณฑ์ได้ เมื่อทำตามคู่มือนี้เสร็จแล้ว คุณจะได้ไฟล์ FBX ที่มีเท็กซ์เจอร์เต็มรูปแบบซึ่งสามารถเปิดได้ในโปรแกรมดู 3‑D ใดก็ได้

## คำตอบอย่างรวดเร็ว
- **เป้าหมายหลักคืออะไร?** ใช้วัสดุ Phong พร้อมเท็กซ์เจอร์กระจายบนลูกบาศก์.  
- **ใช้ไลบรารีใด?** Aspose.3D for Java (มีรุ่นทดลองฟรี).  
- **ใช้เวลานานเท่าไหร่?** ประมาณ 10‑15 นาทีสำหรับตัวอย่างที่ทำงานได้.  
- **ต้องการไลเซนส์หรือไม่?** จำเป็นต้องมีไลเซนส์ชั่วคราวสำหรับการสร้างที่ไม่ใช่การประเมินผล.  
- **รูปแบบไฟล์ที่สร้างคืออะไร?** FBX 7.4 ASCII (เข้ากันได้กับเครื่องมือ 3‑D ส่วนใหญ่).

## การสอนกราฟิก 3D ด้วย Java คืออะไร?

**java 3d graphics tutorial** จะพาคุณผ่านการสร้าง การจัดการ และการส่งออกเนื้อหา 3‑D ด้วยไลบรารีที่ใช้ Java ในกรณีนี้เรามุ่งเน้นที่การจัดการวัสดุ—การกำหนดสี เท็กซ์เจอร์ และคุณสมบัติการเชดดิ้งให้กับเอนทิตี้เชิงเรขาคณิต

## ทำไมต้องใช้ Aspose.3D เพื่อเพิ่มเท็กซ์เจอร์ใน Java?

Aspose.3D มี API เชิงวัตถุที่สะอาดและแยกความซับซ้อนของรูปแบบไฟล์ระดับล่างออกไป มันรองรับรูปแบบหลากหลาย (FBX, STL, OBJ, ฯลฯ) และให้คุณฝังเท็กซ์เจอร์โดยตรงลงในไฟล์ ซึ่งเหมาะอย่างยิ่งเมื่อคุณต้องการสินทรัพย์เดียวที่พกพาได้

## ข้อกำหนดเบื้องต้น

- Java Development Kit (JDK 8 หรือสูงกว่า) ติดตั้งแล้ว.  
- ไฟล์ JAR ของ Aspose.3D for Java เวอร์ชันล่าสุดที่เพิ่มใน classpath ของโปรเจกต์ของคุณ.  
- ความเข้าใจพื้นฐานเกี่ยวกับไวยากรณ์ Java และการเขียนโปรแกรมเชิงวัตถุ.

## นำเข้าแพ็กเกจ

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## ขั้นตอนที่ 1: เริ่มต้นอ็อบเจ็กต์ Scene

```java
// Initialize scene object
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: เริ่มต้นอ็อบเจ็กต์ Cube Node

```java
// Initialize cube node object
Node cubeNode = new Node("cube");
```

## ขั้นตอนที่ 3: สร้าง Mesh ด้วย Polygon Builder

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## ขั้นตอนที่ 4: ชี้ Node ไปยัง Mesh

```java
// Point node to the mesh
cubeNode.setEntity(mesh);
```

## ขั้นตอนที่ 5: เพิ่ม Cube ไปยัง Scene

```java
// Add cube to the scene
scene.getRootNode().addChildNode(cubeNode);
```

## ขั้นตอนที่ 6: เริ่มต้นอ็อบเจ็กต์ PhongMaterial

```java
// Initialize PhongMaterial object
PhongMaterial mat = new PhongMaterial();
```

## ขั้นตอนที่ 7: เริ่มต้นอ็อบเจ็กต์ Texture

```java
// Initialize Texture object
Texture diffuse = new Texture();
```

## ขั้นตอนที่ 8: ตั้งค่าเส้นทางไฟล์ท้องถิ่นสำหรับ Texture

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
```

## ขั้นตอนที่ 9: ตั้งค่าเส้นทางไฟล์ท้องถิ่นสำหรับ Embedded Texture

```java
// Set local file path for embedded texture
diffuse.setFileName(MyDir + "surface.dds");
```

## ขั้นตอนที่ 10: ตั้งค่า Texture ของ Material

```java
// Set Texture of the material
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## ขั้นตอนที่ 11: ฝังข้อมูลดิบลงใน FBX (ไม่บังคับ)

```java
// Set file name for embedded texture
diffuse.setFileName("embedded-texture.png");
// Set binary content
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## ขั้นตอนที่ 12: ตั้งค่าสี Specular

```java
// Set specular color
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## ขั้นตอนที่ 13: ตั้งค่าความสว่าง

```java
// Set brightness
mat.setShininess(100);
```

## ขั้นตอนที่ 14: ตั้งค่าคุณสมบัติวัสดุของอ็อบเจ็กต์ Cube

```java
// Set material property of the cube object
cubeNode.setMaterial(mat);
```

## ขั้นตอนที่ 15: บันทึก 3D Scene

```java
// Set the file name
MyDir = MyDir + "MaterialToCube.fbx";
// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|-----|
| **เท็กซ์เจอร์ไม่แสดง** | เส้นทางไฟล์ผิดหรือรูปแบบเท็กซ์เจอร์ไม่รองรับ. | ตรวจสอบว่า `MyDir` ชี้ไปยังโฟลเดอร์ที่ถูกต้องและใช้รูปแบบที่รองรับเช่น `.dds` หรือ `.png`. |
| **ไฟล์ FBX โหลดไม่สำเร็จ** | ขาดข้อมูลเท็กซ์เจอร์ที่ฝังอยู่. | ใช้บล็อกทางเลือก (ขั้นตอน 11) เพื่อฝังไบต์ของเท็กซ์เจอร์โดยตรงลงใน FBX. |
| **วัสดุแสดงเป็นสีดำ** | ค่าของ Specular หรือ Diffuse ไม่ได้ตั้งค่า. | ตรวจสอบว่าได้เรียก `setSpecularColor` และ `setTexture` ก่อนบันทึก. |

## คำถามที่พบบ่อย

**ถาม: ฉันสามารถใช้วัสดุหลายชั้นกับวัตถุ 3D เดียวได้หรือไม่?**  
ตอบ: ใช่, Aspose.3D อนุญาตให้คุณกำหนดวัสดุที่แตกต่างกันให้กับส่วนของเมชหรือโหนดย่อยที่แยกกัน.

**ถาม: Aspose.3D รองรับรูปแบบไฟล์ใดบ้างสำหรับการบันทึกฉาก?**  
ตอบ: FBX, STL, OBJ, 3DS และอื่น ๆ อีกหลายรูปแบบ ดูที่ [documentation](https://reference.aspose.com/3d/java/) อย่างเป็นทางการสำหรับรายการเต็ม.

**ถาม: มีไลเซนส์ชั่วคราวสำหรับ Aspose.3D for Java หรือไม่?**  
ตอบ: มี, คุณสามารถรับ [temporary license](https://purchase.aspose.com/temporary-license/) สำหรับการประเมินผลได้.

**ถาม: ฉันจะหาแหล่งสนับสนุนสำหรับ Aspose.3D ได้จากที่ไหน?**  
ตอบ: [Aspose.3D forum](https://forum.aspose.com/c/3d/18) เป็นสถานที่ที่ดีที่สุดสำหรับความช่วยเหลือจากชุมชน.

**ถาม: ฉันสามารถดาวน์โหลดไลบรารี Aspose.3D จากลิงก์เฉพาะได้หรือไม่?**  
ตอบ: แน่นอน—ใช้ [download link](https://releases.aspose.com/3d/java/) เพื่อรับไฟล์ JAR ล่าสุด.

**อัปเดตล่าสุด:** 2025-12-08  
**ทดสอบด้วย:** Aspose.3D for Java 24.11  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}