---
date: 2026-04-05
description: เรียนรู้วิธีตั้งค่าสี vector3 ใน Java, เปลี่ยนสีกระจาย, ดึงคุณสมบัติของวัสดุ,
  และจัดการคุณสมบัติ 3 มิติในฉาก Java ด้วย Aspose.3D – คำแนะนำแบบครบถ้วนขั้นตอนต่อขั้นตอน
keywords:
- set vector3 color java
- Aspose 3D Java
- change diffuse color
linktitle: 'วิธีตั้งค่าสี Vector3 ใน Java: เปลี่ยนสี Diffuse และจัดการคุณสมบัติ 3
  มิติในฉาก Java ด้วย Aspose.3D'
second_title: Aspose.3D Java API
title: 'วิธีตั้งค่าสี vector3 ใน Java: เปลี่ยนสี Diffuse และจัดการคุณสมบัติ 3D ในฉาก
  Java ด้วย Aspose.3D'
url: /th/java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีตั้งค่าสี vector3 ใน Java: เปลี่ยนสี Diffuse และจัดการคุณสมบัติ 3D ในฉาก Java ด้วย Aspose.3D

## บทนำ

ใน **บทแนะนำ Aspose 3D** คุณจะได้ค้นพบ **วิธีตั้งค่าสี vector3 ใน Java** และทำงานกับคุณสมบัติ 3D และข้อมูลกำหนดเองภายในฉาก Java ไม่ว่าคุณจะกำลังสร้างเกม, ตัวแสดงผลผลิตภัณฑ์, หรือโปรแกรมดูข้อมูลทางวิทยาศาสตร์ การสามารถแก้ไขแอตทริบิวต์ของวัสดุในระหว่างการทำงานจะให้คุณควบคุมศิลปะได้อย่างเต็มที่ เราจะเดินผ่านกระบวนการแบบขั้นตอน‑โดย‑ขั้นตอน ตั้งแต่การโหลดฉากจนถึงการปรับสี *Diffuse* ด้วยค่า `Vector3`

## คำตอบสั้น
- **อะไรที่ฉันสามารถแก้ไขได้?** คุณสามารถเปลี่ยนสีเทกซ์เจอร์, ความทึบ, ความเงา, และคุณสมบัติที่กำหนดเองใด ๆ ที่แนบกับวัสดุ.  
- **คลาสใดที่เก็บข้อมูล?** `Material` และ `PropertyCollection` ของมัน.  
- **ฉันจะตั้งค่าสีใหม่อย่างไร?** ใช้ `props.set("Diffuse", new Vector3(r, g, b))`.  
- **ฉันจะตั้งค่าสี vector3 ใน Java อย่างไร?** เรียก `props.set("Diffuse", new Vector3(r, g, b))` บนคอลเลกชันคุณสมบัติของวัสดุ.  
- **ฉันต้องการไลเซนส์หรือไม่?** ไลเซนส์ชั่วคราวใช้ได้สำหรับการประเมิน; ไลเซนส์เต็มจำเป็นสำหรับการใช้งานจริง.  
- **รูปแบบที่รองรับ?** FBX, OBJ, STL, GLTF, และอื่น ๆ อีกมาก.

## ข้อกำหนดเบื้องต้น

- ติดตั้ง Java Development Kit (JDK) 8 หรือใหม่กว่า.  
- ไลบรารี Aspose.3D for Java (ดาวน์โหลดจาก [เว็บไซต์ Aspose](https://releases.aspose.com/3d/java/)).  
- ความคุ้นเคยพื้นฐานกับไวยากรณ์ Java และแนวคิดเชิงวัตถุ.

## นำเข้าแพ็กเกจ

ก่อนเขียนโค้ดใด ๆ ให้ทำการนำเข้าคลาสที่ให้คุณเข้าถึงคุณสมบัติของวัสดุและการจัดการเวกเตอร์

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

### ทำไมต้องนำเข้าแพ็กเกจเหล่านี้?

- `Scene` โหลดและเป็นตัวแทนของไฟล์ 3D.  
- `Material` ให้คำนิยามพื้นผิว (เทกซ์เจอร์, สี, ฯลฯ).  
- `PropertyCollection` เป็นคอนเทนเนอร์แบบพจนานุกรมที่ให้คุณ **เข้าถึงคุณสมบัติของวัสดุ** ตามชื่อ.  
- `Vector3` เป็นประเภทข้อมูลที่ใช้สำหรับสีและเวกเตอร์สามส่วนอื่น ๆ.

## วิธีตั้งค่าสี vector3 ใน Java – คำแนะนำขั้นตอนการเปลี่ยน Diffuse

### ขั้นตอนที่ 1: เริ่มต้น Scene

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

เราสร้างอ็อบเจกต์ `Scene` โดยโหลดไฟล์ FBX ที่มีเทกซ์เจอร์อยู่แล้ว นี่คือผืนผ้าใบที่เราจะ **เปลี่ยนสี diffuse**.

### ขั้นตอนที่ 2: เข้าถึงคุณสมบัติของวัสดุ

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

ที่นี่เรา **เข้าถึงคุณสมบัติของวัสดุ** ของเมชแรกในฉาก `Material` เก็บ `PropertyCollection` ที่บรรจุแอตทริบิวต์ที่กำหนดค่าได้ทั้งหมด เช่น *Diffuse*, *Specular*, และข้อมูลผู้ใช้ที่กำหนดเอง.

### ขั้นตอนที่ 3: แสดงรายการคุณสมบัติทั้งหมด (ตรวจสอบก่อนเปลี่ยนแปลง)

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

การวนลูป `props` จะพิมพ์ชื่อคุณสมบัติและค่าปัจจุบันของแต่ละรายการ รายการสั้น ๆ นี้ช่วยให้คุณค้นพบคีย์ที่สามารถแก้ไขได้ในภายหลัง เช่น `"Diffuse"` สำหรับสีพื้นฐาน.

### ขั้นตอนที่ 4: ตั้งค่า Vector3 เพื่อเปลี่ยนสี Diffuse

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**Pro tip:** ตัวสร้าง `Vector3` รับตัวเลขทศนิยมสามค่าแทนส่วน **แดง, เขียว, และน้ำเงิน** (ช่วง 0‑1). การตั้งค่า `(1, 0, 1)` จะทำให้สีพื้นฐานของเทกซ์เจอร์เป็นสีม่วงแดง, ซึ่งเป็นการ **เปลี่ยนสี diffuse** ของโมเดล นี่คือหัวใจของ **การตั้งค่าสี vector3 ใน Java**.

### ขั้นตอนที่ 5: ดึงคุณสมบัติของวัสดุตามชื่อ

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

ตัวอย่างนี้แสดงการ **ดึงคุณสมบัติของวัสดุ** ตามชื่อ เราแคสต์ `Object` ที่คืนค่ามาเป็น `Vector3` เพื่อทำงานกับสีในโค้ด.

### ขั้นตอนที่ 6: เข้าถึงอินสแตนซ์ Property โดยตรง

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` คืนค่าอ็อบเจกต์ `Property` เต็มรูปแบบ ให้คุณเข้าถึงเมตาดาต้า เช่น ประเภทของคุณสมบัติ, ป้ายชื่อ, และข้อมูลกำหนดเองที่แนบมา.

### ขั้นตอนที่ 7: เดินทางผ่าน Sub‑Properties ของ Property

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

บางคุณสมบัติมีโครงสร้างแบบลำดับชั้น การเดินทาง `pdiffuse.getProperties()` จะเปิดเผยแอตทริบิวต์ที่ซ้อนอยู่ (เช่น พิกัดเทกซ์เจอร์, คีย์แอนิเมชัน) ที่เป็นส่วนของรายการ *Diffuse*.

## ทำไมเรื่องนี้ถึงสำคัญ

การเปลี่ยนสี diffuse ในระหว่างการทำงานทำให้คุณสร้างเอฟเฟกต์ภาพแบบไดนามิก—เช่น ตัวกำหนดสีผลิตภัณฑ์ที่ผู้ใช้เลือกสี, หรือเกมที่ตอบสนองต่อเหตุการณ์ในเกม เนื่องจากการเปลี่ยนทำผ่าน `PropertyCollection` คุณยังสามารถเขียนสคริปต์อัปเดตเป็นกลุ่มบนหลายวัสดุด้วยโค้ดเพียงเล็กน้อย.

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|---------|
| **`NullPointerException` on `material`** | โหนดอาจไม่มีวัสดุที่กำหนดไว้. | เรียก `node.setMaterial(new Material())` ก่อนเข้าถึงคุณสมบัติ. |
| **สีไม่เปลี่ยน** | โมเดลใช้เทกซ์เจอร์ที่เขียนทับสี *Diffuse*. | ปิดการใช้งานเทกซ์เจอร์หรือแก้ไขภาพเทกซ์เจอร์โดยตรง. |
| **`ClassCastException` เมื่อดึงค่า** | พยายามแคสต์คุณสมบัติที่ไม่ใช่ประเภท Vector3. | ตรวจสอบประเภทของคุณสมบัติก่อนแคสต์ด้วย `pdiffuse.getValue().getClass()` ก่อนแคสต์. |

## คำถามที่พบบ่อย

**ถาม: ฉันจะติดตั้งไลบรารี Aspose.3D ในโปรเจกต์ Java ของฉันได้อย่างไร?**  
ตอบ: ดาวน์โหลดไฟล์ JAR จาก [เว็บไซต์ Aspose](https://releases.aspose.com/3d/java/) แล้วเพิ่มลงใน classpath ของโปรเจกต์หรือใน dependencies ของ Maven/Gradle.

**ถาม: มีตัวเลือกการทดลองใช้ฟรีสำหรับ Aspose.3D หรือไม่?**  
ตอบ: มี, เวอร์ชันทดลองใช้งานเต็มรูปแบบ 30‑วันพร้อมให้ดาวน์โหลดจาก [หน้าทดลองใช้ฟรีของ Aspose](https://releases.aspose.com/).

**ถาม: ฉันจะหาเอกสารรายละเอียดของ Aspose.3D สำหรับ Java ได้จากที่ไหน?**  
ตอบ: เอกสารอ้างอิง API อย่างเป็นทางการอยู่ที่ [เอกสาร Aspose.3D](https://reference.aspose.com/3d/java/).

**ถาม: มีฟอรั่มสนับสนุนสำหรับ Aspose.3D ที่ฉันสามารถถามคำถามได้หรือไม่?**  
ตอบ: แน่นอน—เยี่ยมชม [ฟอรั่มสนับสนุน Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อเชื่อมต่อกับชุมชนและผู้เชี่ยวชาญ.

**ถาม: ฉันจะขอรับลิขสิทธิ์ชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?**  
ตอบ: ขอรับได้ผ่าน [หน้าลิขสิทธิ์ชั่วคราว](https://purchase.aspose.com/temporary-license/) บนเว็บไซต์ Aspose.

**ถาม: ฉันสามารถเปลี่ยนแอตทริบิวต์ของวัสดุอื่น ๆ นอกจาก diffuse ได้หรือไม่?**  
ตอบ: ได้, คุณสามารถแก้ไขคุณสมบัติเช่น `Specular`, `Opacity`, และข้อมูลผู้ใช้ที่กำหนดเองโดยใช้รูปแบบ `props.set` เดียวกัน.

## สรุป

คุณได้เรียนรู้ **วิธีตั้งค่าสี vector3 ใน Java**, **ดึงคุณสมบัติของวัสดุ**, ตั้งค่า `Vector3` และนำทางข้อมูลคุณสมบัติแบบลำดับชั้นในฉาก Java ด้วย Aspose.3D เทคนิคเหล่านี้ให้คุณควบคุมรายละเอียดของทรัพย์สิน 3D ได้อย่างละเอียด ส่งผลให้สร้างเอฟเฟกต์ภาพแบบไดนามิกและการปรับแต่งในเวลารันไทม์ในแอปพลิเคชันของคุณได้

---

**Last Updated:** 2026-04-05  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}