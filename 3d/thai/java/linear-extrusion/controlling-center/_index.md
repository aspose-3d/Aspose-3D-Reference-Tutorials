---
date: 2026-06-13
description: เรียนรู้บทแนะนำกราฟิก 3 มิติด้วย Java เกี่ยวกับการควบคุมศูนย์กลางในการดันเชิงเส้นด้วย
  Aspose.3D รวมถึงวิธีตั้งค่ารัศมีการโค้งและบันทึกไฟล์ OBJ ด้วย Java
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: การควบคุมศูนย์กลางในการดันเชิงเส้นด้วย Aspose.3D สำหรับ Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: สร้าง 3D Mesh Java – ศูนย์กลางในการดันเชิงเส้น
url: /th/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# สร้างเมช 3D Java – ศูนย์กลางใน Linear Extrusion

## บทนำ

หากคุณกำลังสร้างการแสดงผล 3‑D ด้วย Java การเชี่ยวชาญเทคนิค extrusion ถือเป็นสิ่งสำคัญ คู่มือ **java 3d graphics tutorial** นี้จะแสดงวิธี **create 3d mesh java** โดยการควบคุมศูนย์กลางของ linear extrusion ด้วย Aspose.3D for Java เมื่อคุณอ่านจนจบจะเข้าใจว่าทำไมคุณสมบัติ `center` ถึงสำคัญ วิธี **set rounding radius** และวิธี **save obj file java**‑compatible output คุณยังจะได้เห็นวิธี **export 3d model obj** เพื่อใช้ในโปรแกรมแก้ไข 3‑D ใด ๆ

## คำตอบอย่างรวดเร็ว
- **คุณสมบัติ center ทำหน้าที่อะไร?** มันกำหนดว่าการ extrusion จะสมมาตรรอบจุดกำเนิดของโปรไฟล์หรือไม่.  
- **ฉันต้องการใบอนุญาตเพื่อรันโค้ดหรือไม่?** ใบอนุญาตชั่วคราวใช้ได้สำหรับการทดสอบ; ใบอนุญาตเต็มจำเป็นสำหรับการใช้งานจริง.  
- **รูปแบบไฟล์ใดที่ใช้สำหรับผลลัพธ์?** ฉากจะถูกบันทึกเป็นไฟล์ Wavefront OBJ.  
- **ฉันสามารถเปลี่ยนจำนวน slice ได้หรือไม่?** ได้, ใช้ `setSlices(int)` กับอ็อบเจ็กต์ `LinearExtrusion`.  
- **Aspose.3D รองรับ Java 8+ หรือไม่?** แน่นอน – รองรับทุกเวอร์ชัน Java สมัยใหม่.

## java 3d graphics tutorial คืออะไร?

**java 3d graphics tutorial** เป็นคู่มือแบบขั้นตอนที่สอนคุณใช้ไลบรารี Java เพื่อสร้าง, ปรับเปลี่ยน, และเรนเดอร์วัตถุสามมิติ ในบทเรียนนี้คุณจะได้เรียนรู้วิธี **create 3d mesh java** โดยการแปลงโปรไฟล์ 2‑D ให้เป็นโมเดล 3‑D เต็มรูปแบบ, ควบคุมการจัดตำแหน่งศูนย์กลาง, ทำให้มุม extrusion โค้งมน, และสุดท้ายส่งออกผลลัพธ์เป็นไฟล์ OBJ ที่โปรแกรม 3‑D ใด ๆ ก็อ่านได้

## ทำไมต้องใช้ Aspose.3D for Java?

Aspose.3D for Java มี API ระดับสูงที่ลบความจำเป็นในการคำนวณเมชด้วยตนเอง ทำให้คุณมุ่งเน้นที่การออกแบบแทนที่จะเป็นเรขาคณิตระดับล่าง มันรองรับ **50+ รูปแบบการนำเข้าและส่งออก** — รวมถึง OBJ, FBX, STL, และ GLTF — ดังนั้นคุณสามารถ **export 3d model obj** หรือรูปแบบอื่นใดก็ได้ด้วยการเรียกเมธอดเดียว ไลบรารีสามารถประมวลผลฉากหลายร้อยหน้าโดยไม่ต้องโหลดไฟล์ทั้งหมดเข้าสู่หน่วยความจำ ให้ประสิทธิภาพ **เร็วขึ้นถึง 3×** เมื่อเทียบกับการใช้ OpenGL ดิบบนฮาร์ดแวร์เซิร์ฟเวอร์ทั่วไป

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่ม, โปรดตรวจสอบว่าคุณมี:

1. **Java Development Environment** – ติดตั้ง JDK 8 หรือใหม่กว่า.  
2. **Aspose.3D for Java** – ดาวน์โหลดไลบรารีและเอกสาร [ที่นี่](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – สร้างโฟลเดอร์บนเครื่องของคุณเพื่อเก็บไฟล์ที่สร้าง; เราจะอ้างถึงมันว่า **“Your Document Directory.”**

## นำเข้าแพ็กเกจ

ใน IDE ของ Java, นำเข้าคลาส Aspose.3D ที่คุณต้องการ ซึ่งจะทำให้คอมไพเลอร์เข้าถึงฟีเจอร์ extrusion และการสร้างฉากได้

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## คู่มือแบบขั้นตอน

### ขั้นตอน 1: ตั้งค่า Base Profile

แรกเริ่มสร้างรูปทรง 2‑D ที่จะทำ extrusion ที่นี่เราใช้สี่เหลี่ยมและ **set rounding radius** เป็น 0.3 เพื่อทำให้มุมโค้งและแสดงวิธี **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### ขั้นตอน 2: สร้าง 3D Scene

**Scene** เป็นคอนเทนเนอร์ระดับบนสุดที่เก็บวัตถุ 3‑D, แสง, และกล้องทั้งหมด

```java
Scene scene = new Scene();
```

### ขั้นตอน 3: เพิ่ม Left and Right Nodes

**Node** แทนวัตถุที่สามารถแปลงตำแหน่งได้ในกราฟฉาก, ช่วยจัดตำแหน่งและลำดับชั้น

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### ขั้นตอน 4: Linear Extrusion – ไม่มีศูนย์กลาง (Left Node)

**LinearExtrusion** แปลงโปรไฟล์ 2‑D ให้เป็นเมช 3‑D โดยการสวีปตามเส้นตรง  
**setCenter(boolean)** สลับว่าการ extrusion จะอยู่ศูนย์กลางรอบจุดกำเนิดของโปรไฟล์หรือไม่

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### ขั้นตอน 5: เพิ่ม Ground Plane เพื่ออ้างอิง (Left Node)

กล่องบางแผ่นทำหน้าที่เป็นพื้นมองเห็น, ช่วยให้คุณเห็นทิศทางของ extrusion

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### ขั้นตอน 6: Linear Extrusion – มีศูนย์กลาง (Right Node)

ตอนนี้ทำ extrusion อีกครั้งโดยเปิดใช้งาน `center`. รูปร่างจะสมมาตรรอบจุดกำเนิดของโปรไฟล์, ให้ผลลัพธ์ **create 3d mesh java** ที่สมดุลอย่างสมบูรณ์

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### ขั้นตอน 7: เพิ่ม Ground Plane เพื่ออ้างอิง (Right Node)

ใช้พื้นเดียวกันสำหรับด้านขวาเพื่อให้การเปรียบเทียบชัดเจน

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### ขั้นตอน 8: บันทึก 3D Scene

สุดท้ายส่งออกฉากทั้งหมดเป็นไฟล์ Wavefront OBJ – รูปแบบที่ใช้ได้กับโปรแกรมแก้ไข 3‑D ส่วนใหญ่ เมธอด `save` จะทำการแปลงเมชเป็นสเปค OBJ โดยอัตโนมัติ, ทำให้คุณ **save obj file java** ได้โดยไม่ต้องทำขั้นตอนหลังเพิ่มเติม

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|----------|
| **Extrusion appears offset** | `setCenter(false)` ทำให้โปรไฟล์ถูกยึดที่มุมหนึ่ง | ใช้ `setCenter(true)` เพื่อให้ผลลัพธ์สมมาตร |
| **OBJ file is empty** | เส้นทางไดเรกทอรีผลลัพธ์ไม่ถูกต้องหรือไม่มีสิทธิ์เขียน | ตรวจสอบว่า `MyDir` ชี้ไปยังโฟลเดอร์ที่มีอยู่และแอปพลิเคชันมีสิทธิ์เขียน |
| **Rounded corners look sharp** | รัศมีการโค้งน้อยเกินไปเมื่อเทียบกับขนาดสี่เหลี่ยม | เพิ่มค่ารัศมี (เช่น `setRoundingRadius(0.5)`) |

## คำถามที่พบบ่อย

### Q1: ฉันสามารถใช้ Aspose.3D for Java ในโครงการเชิงพาณิชย์ได้หรือไม่?

A1: ใช่, Aspose.3D for Java สามารถใช้ในเชิงพาณิชย์ได้ สำหรับรายละเอียดการให้ใบอนุญาต, เยี่ยมชม [ที่นี่](https://purchase.aspose.com/buy).

### Q2: มีรุ่นทดลองฟรีหรือไม่?

A2: มี, คุณสามารถทดลองใช้ Aspose.3D for Java ฟรีได้ที่ [ที่นี่](https://releases.aspose.com/).

### Q3: ฉันจะหาแหล่งสนับสนุนสำหรับ Aspose.3D for Java ได้จากที่ไหน?

A3: ฟอรั่มชุมชน Aspose.3D เป็นสถานที่ดีสำหรับขอความช่วยเหลือและแบ่งปันประสบการณ์. เยี่ยมชมฟอรั่ม [ที่นี่](https://forum.aspose.com/c/3d/18).

### Q4: ฉันต้องการใบอนุญาตชั่วคราวสำหรับการทดสอบหรือไม่?

A4: ใช่, หากคุณต้องการใบอนุญาตชั่วคราวสำหรับการทดสอบ, คุณสามารถรับได้ที่ [ที่นี่](https://purchase.aspose.com/temporary-license/).

### Q5: ฉันจะหาเอกสารได้จากที่ไหน?

A5: เอกสารสำหรับ Aspose.3D for Java มีให้ที่ [ที่นี่](https://reference.aspose.com/3d/java/).

## สรุป

โดยการทำตาม **java 3d graphics tutorial** นี้ คุณได้เรียนรู้วิธี **create 3d mesh java**, ควบคุมศูนย์กลางของ linear extrusion, ปรับรัศมีการโค้ง, และ **save obj file java** ด้วย Aspose.3D เทคนิคเหล่านี้ให้การควบคุมเมชอย่างละเอียด ซึ่งสำคัญสำหรับสินทรัพย์เกม, โปรโตไทป์ CAD, และการแสดงผลทางวิทยาศาสตร์ อย่าลังเลที่จะทดลองกับโปรไฟล์ต่าง ๆ, จำนวน slice, และรูปแบบการส่งออกเพื่อขยายเครื่องมือ 3‑D ของคุณ

---

**อัพเดทล่าสุด:** 2026-06-13  
**ทดสอบด้วย:** Aspose.3D for Java 24.11  
**ผู้เขียน:** Aspose

## บทแนะนำที่เกี่ยวข้อง

- [สร้าง 3D Extrusion Java ด้วย Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [วิธีตั้งค่า Direction ใน Linear Extrusion ด้วย Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [สร้าง 3D Scene พร้อม Twist ใน Linear Extrusion – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}