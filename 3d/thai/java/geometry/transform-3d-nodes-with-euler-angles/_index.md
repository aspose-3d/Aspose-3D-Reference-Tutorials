---
date: 2025-12-13
description: เรียนรู้วิธีใช้ Aspose 3D Java เพื่อแปลงโหนด 3D คู่มือนี้แสดงวิธีใช้มุมออยเลอร์,
  เพิ่มการหมุน 3D และตั้งค่าการแปลใน Java.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – แปลงโหนด 3D ด้วยมุมออยเลอร์
url: /th/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# แปลงโหนด 3D ด้วยมุมออยเลอร์ใน Java โดยใช้ Aspose.3D

## บทนำ

ในบทแนะนำนี้คุณจะได้ค้นพบ **วิธีใช้ aspose 3d java** เพื่อแปลงโหนด 3D โดยใช้มุมออยเลอร์ เมื่อจบคู่มือคุณจะสามารถเพิ่มการหมุน 3d, ตั้งค่าการแปลตำแหน่ง java, และสร้างฉากไดนามิกที่ตอบสนองต่อข้อมูลแบบเรียลไทม์ได้

## คำตอบด่วน
- **ไลบรารีใดที่จัดการการแปลง 3D ใน Java?** Aspose 3D for Java.  
- **เมธอดใดที่ตั้งค่าการหมุนโดยใช้มุมออยเลอร์?** `setEulerAngles()` บนการแปลงของโหนด.  
- **ฉันจะย้ายโหนดในอวกาศอย่างไร?** ใช้ `setTranslation()` พร้อมกับ `Vector3`.  
- **ฉันต้องการไลเซนส์สำหรับการผลิตหรือไม่?** ใช่, จำเป็นต้องมีไลเซนส์เชิงพาณิชย์ของ Aspose 3D.  
- **ฉันสามารถส่งออกเป็น FBX ได้หรือไม่?** แน่นอน – `scene.save(..., FileFormat.FBX7500ASCII)` ทำงานได้ทันที

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะลงลึกในบทแนะนำนี้, โปรดตรวจสอบว่าคุณมีข้อกำหนดต่อไปนี้พร้อมใช้งานแล้ว:

- ความรู้พื้นฐานเกี่ยวกับการเขียนโปรแกรม Java.  
- Java Development Kit (JDK) ติดตั้งบนเครื่องของคุณ.  
- ไลบรารี Aspose.3D, ซึ่งคุณสามารถรับได้จาก [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## นำเข้าแพ็กเกจ

เริ่มต้นด้วยการนำเข้าแพ็กเกจที่จำเป็นเข้าสู่โครงการ Java ของคุณ. ตรวจสอบให้แน่ใจว่าไลบรารี Aspose.3D ถูกเพิ่มลงใน classpath อย่างถูกต้อง. หากคุณยังไม่ได้ดาวน์โหลด, คุณสามารถค้นหาลิงก์ดาวน์โหลดได้ [ที่นี่](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – การทำงานกับมุมออยเลอร์

### ขั้นตอนที่ 1. เริ่มต้น Scene และ Node

แรกเริ่ม, สร้าง scene และ node ที่จะเก็บเรขาคณิตที่คุณต้องการแปลง.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### ขั้นตอนที่ 2. สร้าง Mesh และตั้งค่า Geometry

ต่อไป, สร้าง mesh ง่าย ๆ (เช่น ลูกบาศก์ในกรณีนี้) และผูกเข้ากับ node.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## เพิ่มการหมุน 3D ให้กับ Node

### ขั้นตอนที่ 3. ตั้งค่ามุมออยเลอร์และการแปลตำแหน่ง

ตอนนี้เราจะใช้มุมออยเลอร์เพื่อหมุนและย้าย node ไปยังตำแหน่งที่มองเห็นได้.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## ตั้งค่า Translation Java – การวางตำแหน่ง Node

ขั้นตอนการแปลตำแหน่งด้านบนแสดง **set translation java** ในการปฏิบัติ: node ถูกเลื่อน 20 หน่วยตามแกน Z เพื่อให้คุณเห็นหลังการเรนเดอร์.

## ขั้นตอนที่ 4. เพิ่ม Node ไปยัง Scene

ผูก node ที่แปลงแล้วเข้ากับ root node ของ scene.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## ขั้นตอนที่ 5. บันทึก Scene 3D

สุดท้าย, ส่งออก scene เป็นไฟล์ FBX (หรือรูปแบบอื่นที่รองรับ).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

ตรวจสอบให้แน่ใจว่าได้แทนที่ `"Your Document Directory"` ด้วยพาธที่เหมาะสมบนเครื่องของคุณ.

## สรุป

ขอแสดงความยินดี! คุณได้แปลงโหนด 3D ด้วยมุมออยเลอร์ใน Java ด้วย **aspose 3d java** อย่างสำเร็จแล้ว. ทดลองกับมุมและการแปลตำแหน่งต่าง ๆ เพื่อสร้างฉาก 3D ที่ไดนามิกและน่าสนใจ

## คำถามที่พบบ่อย

### Q1: ฉันสามารถใช้ Aspose.3D สำหรับ Java ในโครงการเชิงพาณิชย์ได้หรือไม่?

A1: ได้, คุณสามารถทำได้. เยี่ยมชม [purchase page](https://purchase.aspose.com/buy) เพื่อดูรายละเอียดการไลเซนส์.

### Q2: ฉันจะหาแหล่งสนับสนุนสำหรับ Aspose.3D ได้จากที่ไหน?

A2: [Aspose.3D forum](https://forum.aspose.com/c/3d/18) คือสถานที่ที่คุณสามารถขอความช่วยเหลือและเชื่อมต่อกับชุมชนได้.

### Q3: มีการทดลองใช้ฟรีหรือไม่?

A3: มี, คุณสามารถสำรวจ [free trial](https://releases.aspose.com/) เพื่อสัมผัสความสามารถของ Aspose.3D.

### Q4: ฉันจะขอรับใบอนุญาตชั่วคราวได้อย่างไร?

A4: คุณสามารถขอรับใบอนุญาตชั่วคราวได้ [ที่นี่](https://purchase.aspose.com/temporary-license/).

### Q5: ฉันจะหาเอกสารได้จากที่ไหน?

A5: [documentation](https://reference.aspose.com/3d/java/) ให้คำแนะนำที่ครอบคลุมในการใช้ Aspose.3D สำหรับ Java.

## คำถามที่พบบ่อย

**Q: ความแตกต่างระหว่างมุมออยเลอร์และการหมุนด้วยควอเทอร์เนียนคืออะไร?**  
A: มุมออยเลอร์เข้าใจง่าย (pitch, yaw, roll) แต่บางครั้งอาจเจอปัญหา gimbal lock, ส่วนควอเทอร์เนียนหลีกเลี่ยงปัญหานี้และเหมาะกับการแทรกสลับอย่างราบรื่น.

**Q: ฉันสามารถเชื่อมต่อการแปลงหลาย ๆ อย่างบนโหนดเดียวกันได้หรือไม่?**  
A: ได้. เรียก `setEulerAngles`, `setTranslation`, และ `setScale` ในลำดับใดก็ได้; ไลบรารีจะรวมเป็นเมทริกซ์การแปลงเดียว.

**Q: สามารถส่งออกเป็นรูปแบบอื่นเช่น OBJ หรือ STL ได้หรือไม่?**  
A: แน่นอน. แทนที่ `FileFormat.FBX7500ASCII` ด้วย `FileFormat.OBJ` หรือ `FileFormat.STL` ในการเรียก `scene.save`.

**Q: ฉันจะใช้การหมุนเดียวกันกับหลายโหนดพร้อมกันอย่างไร?**  
A: สร้าง parent node, ตั้งค่าการหมุนให้กับ parent, แล้วเพิ่ม child node ภายใต้มัน. โหนดลูกทั้งหมดจะสืบทอดการแปลงนั้น.

**Q: ฉันต้องเรียกเมธอดทำความสะอาดหลังการบันทึกหรือไม่?**  
A: ตัวเก็บขยะของ Java จะจัดการทรัพยากรส่วนใหญ่, แต่คุณสามารถเรียก `scene.dispose()` อย่างชัดเจนหากทำงานกับ scene ขนาดใหญ่ในแอปพลิเคชันที่ทำงานต่อเนื่องเป็นเวลานาน.

---

**Last Updated:** 2025-12-13  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}