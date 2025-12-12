---
date: 2025-12-12
description: เรียนรู้วิธีตั้งค่าสีวัสดุขณะแชร์ข้อมูลเรขาคณิตเมชและบันทึกฉากเป็น FBX
  ใน Java 3D ด้วย Aspose.3D.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: ตั้งค่าสีวัสดุและแชร์ข้อมูลเรขาคณิตเมชใน Java 3D ด้วย Aspose.3D
url: /th/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ตั้งค่าสีวัสดุและแชร์ข้อมูลเรขาคณิตเมชใน Java 3D ด้วย Aspose.3D

## Introduction

การเริ่มต้นเดินทางสู่โลกของ Java 3D ด้วย Aspose.3D เปิดประตูสู่ความเป็นไปได้มากมายสำหรับการสร้างการแสดงผลที่สวยงามและประสบการณ์ที่ดื่มด่ำ ในบทเรียนนี้ เราจะสอน **วิธีแชร์ข้อมูลเมช** ใน Java 3D ด้วย Aspose.3D และจะแสดงให้คุณเห็น **วิธีตั้งค่าสีวัสดุ** สำหรับแต่ละอินสแตนซ์ของเมช ทำตามขั้นตอนแต่ละขั้นอย่างระมัดระวัง และเมื่อเสร็จสิ้น คุณจะสามารถแลกเปลี่ยนข้อมูลเมชระหว่างโหนดหลาย ๆ โหนดได้อย่างราบรื่น พร้อมควบคุมสีและส่งออกเป็น FBX

## Quick Answers
- **เป้าหมายหลักคืออะไร?** ตั้งค่าสีวัสดุสำหรับแต่ละโหนดและแชร์ข้อมูลเรขาคณิตเมช  
- **ต้องใช้ไลบรารีอะไร?** Aspose.3D for Java  
- **ฉันจะส่งออกผลลัพธ์อย่างไร?** บันทึกฉากเป็นไฟล์ FBX (FBX7400ASCII)  
- **ต้องมีลิขสิทธิ์หรือไม่?** จำเป็นต้องมีลิขสิทธิ์ชั่วคราวหรือเต็มสำหรับการใช้งานในผลิตภัณฑ์  
- **เวอร์ชัน Java ใดที่ทำงานได้?** สภาพแวดล้อม Java 8+ ใดก็ได้

## Prerequisites

ก่อนที่เราจะลงลึกในบทเรียน โปรดตรวจสอบว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้พร้อมใช้งานแล้วหรือยัง:

- สภาพแวดล้อมการพัฒนา Java: ตรวจสอบว่าคุณได้ตั้งค่าสภาพแวดล้อมการพัฒนา Java บนระบบของคุณแล้ว  
- ไลบรารี Aspose.3D: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D คุณสามารถหาไลบรารีได้จาก [ที่นี่](https://releases.aspose.com/3d/java/)

## Import Packages

เริ่มต้นด้วยการนำเข้าแพ็กเกจที่จำเป็นเข้าสู่โปรเจกต์ Java ของคุณ ขั้นตอนนี้สำคัญเพื่อให้เข้าถึงฟังก์ชันที่ Aspose.3D มีให้

```java
import com.aspose.threed.*;
```

## Step 1: Initialize Scene Object (initialize scene java)

มาเริ่มกระบวนการด้วยการสร้างอ็อบเจ็กต์ฉาก ซึ่งจะทำหน้าที่เป็นผืนผ้าใบสำหรับเวทมนตร์ 3 มิติของเรา

```java
// Initialize scene object
Scene scene = new Scene();
```

## Step 2: Define Color Vectors

ในขั้นตอนนี้ เราจะกำหนดอาเรย์ของเวกเตอร์สีที่จะนำไปใช้กับองค์ประกอบต่าง ๆ ของฉาก 3 มิติ

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Step 3: Create 3D Mesh Java Using Polygon Builder (create 3 mesh java)

ใช้คลาส Common เพื่อสร้างเมชโดยใช้วิธี polygon builder เมชนี้จะเป็นพื้นฐานสำหรับองค์ประกอบ 3 มิติของเรา

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## How to set material color for each node?

วนลูปผ่านเวกเตอร์สี สร้างโหนดลูกบาศก์ และตั้งค่าแอตทริบิวต์ต่าง ๆ เช่น วัสดุ, **ตั้งค่าสีวัสดุ**, และการแปลตำแหน่ง นี่คือหัวใจของการควบคุมลักษณะการแสดงผลของแต่ละอินสแตนซ์เมช

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

## Step 5: Save the 3D Scene (save scene fbx, convert mesh to fbx)

ระบุไดเรกทอรีและชื่อไฟล์สำหรับบันทึกฉาก 3 มิติในรูปแบบไฟล์ที่รองรับ ในกรณีนี้คือ FBX7400ASCII ขั้นตอนนี้ยังแสดงการ **แปลงเมชเป็น FBX** อีกด้วย

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Conclusion

ขอแสดงความยินดี! คุณได้ **ตั้งค่าสีวัสดุ** สำเร็จ, แชร์ข้อมูลเรขาคณิตเมชระหว่างโหนดหลาย ๆ โหนด, และส่งออกผลลัพธ์เป็นไฟล์ FBX ด้วย Aspose.3D for Java ซึ่งเปิดโอกาสไม่จำกัดสำหรับการสร้างแอปพลิเคชัน 3 มิติที่สวยงามและโต้ตอบได้

## FAQ's

### Q1: Can I use Aspose.3D with other Java frameworks?

A1: Yes, Aspose.3D is designed to work seamlessly with various Java frameworks.

### Q2: Are there any licensing options available for Aspose.3D?

A2: Yes, you can explore licensing options [here](https://purchase.aspose.com/buy).

### Q3: How can I get support for Aspose.3D?

A3: Visit the Aspose.3D [forum](https://forum.aspose.com/c/3d/18) for support and discussions.

### Q4: Is there a free trial available?

A4: Yes, you can get a free trial [here](https://releases.aspose.com/).

### Q5: How do I obtain a temporary license for Aspose.3D?

A5: You can get a temporary license [here](https://purchase.aspose.com/temporary-license/).

## Additional Frequently Asked Questions

**Q: Can I export the scene to other formats besides FBX?**  
A: Yes, Aspose.3D supports OBJ, STL, 3MF, and more. Just change the `FileFormat` enum in the `save` call.

**Q: What if I need to change the material after the scene is created?**  
A: Retrieve the node, modify its `LambertMaterial` (e.g., `setDiffuseColor`), and re‑save the scene.

**Q: Does the library handle large meshes efficiently?**  
A: Aspose.3D uses optimized data structures; however, for extremely large meshes consider streaming or splitting the scene.

**Q: Is there a way to animate the color change?**  
A: Yes, you can animate material properties using the `AnimationController` API.

---

**Last Updated:** 2025-12-12  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}