---
date: 2026-02-17
description: เรียนรู้วิธีแปลงเมชเป็น FBX พร้อมตั้งค่าสีวัสดุและแชร์ข้อมูลเรขาคณิตของเมชใน
  Java 3D โดยใช้ Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: แปลงเมชเป็น FBX และตั้งค่าสีวัสดุใน Java 3D
url: /th/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# แปลง Mesh เป็น FBX และตั้งค่าสีวัสดุใน Java 3D

## การแนะนำ

ด้วยแอปพลิเคชัน 3D ที่ใช้ Java คุณมักจะต้องการใช้ระบบเดียวกันซ้ำหลายสิ่งพร้อมกับให้แต่ละส่วนของระบบเฉพาะในบทเรียนนี้คุณจะได้เรียนรู้ **วิธี mesh เป็น FBX**, วิธีแปลง mesh เพื่อแสดงหลาย ๆ อย่าง, และ ** ติดตั้งสีวัสดุที่มีประสิทธิภาพในประสิทธิภาพ** ในครั้งแรกที่คุณต้องมีฉาก FBX ที่พร้อมส่งออกและเน้นย้ำหรือดูโปรแกรมทั่วไป

## คำตอบด่วน
- **เป้าหมายหลักคืออะไร** เป้าหมายหลักคืออะไร? รูปแบบ mesh เป็น FBX, ส่วนใหญ่จะเป็น mesh, และการตั้งค่าสีฮาร์ดแวร์สำหรับคอนโซล
- **ต้องใช้ไลบรารีใด** ต้องใช้ไลบรารีอะไร? Aspose.3D สำหรับจาวา
- **ฉันจะส่งออกผลลัพธ์ได้อย่างไร** ฉันส่งออกผลลัพธ์อย่างไร? บันทึกฉากเป็นไฟล์ FBX เป็นเพียง `FileFormat.FBX7400ASCII`.
- **ฉันจำเป็นต้องมีใบอนุญาตหรือไม่** จำเป็นต้องมีหรือไม่? ต้องมีชั่วคราวหรือเต็มรูปแบบในผลิตภัณฑ์
- **Java เวอร์ชันใดใช้งานได้?** เซิร์ฟเวอร์ Java ใด ๆ ที่ทำงานได้? ทุกรายการใน Java8+

## **แปลง mesh เป็น FBX** คืออะไร

`แปลง mesh เป็น fbx` คือส่วนหนึ่งของการนำอ็อบเจ็กต์ mesh การล่าสัตว์หรือแก้ไขในเชิงวิเคราะห์และเขียนออกไฟล์ FBX ความเชื่อสนับสนุนโดยเครื่องมือ 3D ได้แก่ Maya, Blender, และ Unity Aspose.3D ส่วนนี้เป็นส่วนหนึ่ง, ดังนั้นคุณเพียงแค่เรียก `scene.save(...)` พร้อม `FileFormat` ที่ดี

## เหตุใดจึงต้องแชร์ข้อมูลเรขาคณิตของตาข่าย

แบ่งปันข้อมูลอย่างเต็มที่ mesh? การแบ่งปันเริ่มต้นการตรวจสอบและคุณสมบัติของการเรนเดอร์เนื่องจากความเชื่อของเวอร์็กซ์พื้นฐานถูกจัดเก็บในเทคนิคนี้สำหรับฉากที่มีวัตถุซ้ำจำนวนมาก— เช่น โฟลเดอร์, ฝูงคน, หรือการตรวจสอบฮาร์ดแวร์าร์—ที่แต่ละแห่งจะตรวจสอบเพียงเทหรือวัสดุเท่านั้น

## ข้อกำหนดเบื้องต้น

เบื้องต้น

ก่อนที่เราจะเริ่มเรียนรู้, ระบบควบคุมของคุณมีข้อกำหนดเพิ่มเติมพร้อมแล้ว:

- **Java Development Environment** – ยังคงมีการพัฒนา Java – IDE หรือคำสั่งทั่วไปที่ใช้ Java8 หรือใหม่กว่า
- **Aspose.3D Library** – ไลบรารี Aspose.3D – ดาวน์โหลด JAR ล่าสุดจากเว็บไซต์อย่างเป็นทางการ: [ที่นี่](https://releases.aspose.com/3d/java/)

## แพคเกจนำเข้า

พาร์ตเมนท์

เริ่มต้นด้วยการนำเข้าแพ็คเกจที่จำเป็นไปยังโปรเจ็กต์ Java ของคุณ ขั้นตอนนี้มีความสำคัญอย่างยิ่งในการเข้าถึงฟังก์ชันการทำงานที่ได้รับจากไลบรารี Aspose.3D

```java
import com.aspose.threed.*;
```

## ขั้นตอนที่ 1: เริ่มต้นอ็อบเจ็กต์ Scene (initialize scene java)

เริ่มต้นด้วยการสร้างอ็อบเจ็กต์ฉากก่อน อ็อบเจ็กต์นี้จะทำหน้าที่เป็นผืนผ้าใบสำหรับการสร้างสรรค์งานศิลปะ 3 มิติของเรา

```java
// Initialize scene object
Scene scene = new Scene();
```

## ขั้นตอนที่ 2: กำหนดเวกเตอร์สี

ในขั้นตอนนี้ เราจะกำหนดอาร์เรย์ของเวกเตอร์สีที่จะนำไปใช้กับองค์ประกอบต่างๆ ในฉาก 3 มิติของเรา

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## ขั้นตอนที่ 3: สร้าง 3D Mesh ด้วย Java โดยใช้ Polygon Builder (create 3d mesh java)

ใช้คลาส Common เพื่อสร้างตาข่ายโดยใช้วิธีสร้างโพลีกอน ตาข่ายนี้จะเป็นรากฐานสำหรับองค์ประกอบ 3 มิติของเรา

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## วิธีตั้งค่าสีวัสดุสำหรับแต่ละโหนด?

วนลูปผ่านเวกเตอร์สี สร้างโหนดลูกบาศก์ และกำหนดแอตทริบิวต์ เช่น วัสดุ **กำหนดสีของวัสดุ** และการแปล นี่คือหัวใจหลักของการควบคุมลักษณะที่ปรากฏของแต่ละอินสแตนซ์ของตาข่าย

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## ขั้นตอนที่ 5: บันทึกฉาก 3D (save scene fbx, convert mesh to fbx)

Specify the directory and filename for saving the 3D scene in the supported file format, in this case, FBX7400ASCII. This step also demonstrates **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## ข้อผิดพลาดทั่วไปและเคล็ดลับ

- **Path Issues** – ตรวจสอบให้แน่ใจว่าเส้นทางไดเรกทอรีลงท้ายด้วยตัวคั่นไฟล์ (`/` หรือ `\\`) ก่อนต่อชื่อไฟล์.  
- **License Initialization** – หากคุณลืมตั้งค่าใบอนุญาต Aspose.3D ก่อนเรียก `scene.save` ไลบรารีจะทำงานในโหมดทดลองและอาจฝังลายน้ำ.  
- **Material Overwrites** – การใช้ `LambertMaterial` ตัวเดียวกันซ้ำหลายโหนดจะทำให้ทุกโหนดแชร์สีเดียวกัน ควรสร้างวัสดุใหม่ในแต่ละรอบการวนซ้ำตามที่แสดงด้านบน.  
- **Large Meshes** – สำหรับ mesh ที่มีล้านจุดยอด, ควรใช้ `MeshBuilder` กับพอลิกอนแบบดัชนีเพื่อควบคุมขนาดไฟล์ FBX ให้จัดการได้.

## คำถามที่พบบ่อยเพิ่มเติม

**คำถามที่ 1: ฉันสามารถใช้ Aspose.3D กับเฟรมเวิร์ก Java อื่นๆ ได้หรือไม่**
A1: จริงอยู่, Aspose.3D ได้รับการออกแบบมาให้หลังคานั้นเหมือนกับ Java ที่แตกต่างกันออกไป.

**คำถามที่ 2: มีตัวเลือกสิทธิ์การใช้งานสำหรับ Aspose.3D หรือไม่**
ตอบ 2: มี ไม่เคยสำรวจสิทธิพิเศษมากมาย [ที่นี่](https://purchase.aspose.com/buy)

**คำถามที่ 3: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร**
A3: จำเป็นต้องมีฟอรั่ม Aspose.3D [forum](https://forum.aspose.com/c/3d/18) เพื่อรับและรับชม

**คำถามที่ 4: มีการทดลองใช้ฟรีหรือไม่**
A4: มี, ไม่เคยรับความรู้สึกส่วนตัวใช้ฟรีได้ [ที่นี่](https://releases.aspose.com/)

**Q5: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?**
A5: ฉันจะขอรับใบอนุญาตชั่วคราวได้ [ที่นี่](https://purchase.aspose.com/temporary-license/)

## ความสำเร็จ

ขอแสดงความยินดี! คุณได้ **แปลง mesh เป็น FBX** แชร์ข้อมูลรูปทรงเรขาคณิตของ mesh ระหว่างโหนดหลายโหนด และตั้งค่าสีวัสดุแต่ละชิ้นโดยใช้ Aspose.3D สำหรับ Java เรียบร้อยแล้ว เวิร์กโฟลว์นี้ให้สถาปัตยกรรม mesh ที่มีน้ำหนักเบาและนำกลับมาใช้ใหม่ได้ ซึ่งสามารถส่งออกไปยังไปป์ไลน์ที่เข้ากันได้กับ FBX ใดๆ ก็ได้

---

**อัปเดตล่าสุด:** 2026-02-17
**ทดสอบกับ:** Aspose.3D 24.11 สำหรับ Java
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}