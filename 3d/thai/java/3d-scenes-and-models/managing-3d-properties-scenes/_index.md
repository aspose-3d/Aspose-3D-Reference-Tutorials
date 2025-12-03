---
date: 2025-12-01
description: เรียนรู้วิธีเปลี่ยนสีพื้นผิว, เข้าถึงคุณสมบัติของวัสดุ, ตั้งค่า Vector3,
  และดึงคุณสมบัติตามชื่อในฉาก Java ด้วย Aspose.3D – บทเรียน Aspose 3D ฉบับสมบูรณ์
language: th
linktitle: Change texture color and manage 3D properties in Java scenes using Aspose.3D
second_title: Aspose.3D Java API
title: เปลี่ยนสีพื้นผิวและจัดการคุณสมบัติ 3 มิติในฉาก Java ด้วย Aspose.3D
url: /java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# เปลี่ยนสีพื้นผิวและจัดการคุณสมบัติ 3D ในฉาก Java ด้วย Aspose.3D

## บทนำ

ใน **Aspose 3D tutorial** นี้ คุณจะได้ค้นพบวิธี **เปลี่ยนสีพื้นผิว** และทำงานกับคุณสมบัติ 3D รวมถึงข้อมูลที่กำหนดเองภายในฉาก Java ไม่ว่าคุณจะกำลังสร้างเกม, ตัวแสดงผลผลิตภัณฑ์, หรือโปรแกรมดูข้อมูลทางวิทยาศาสตร์ การสามารถแก้ไขแอตทริบิวต์ของวัสดุในขณะทำงานจะให้คุณควบคุมศิลปะได้อย่างเต็มที่ เราจะเดินผ่านกระบวนการทีละขั้นตอน ตั้งแต่การโหลดฉากจนถึงการปรับสี *Diffuse* ด้วยค่า `Vector3`.

## คำตอบอย่างรวดเร็ว
- **อะไรที่ฉันสามารถแก้ไขได้?** คุณสามารถเปลี่ยนสีพื้นผิว, ความทึบ, ความเงา, และคุณสมบัติที่กำหนดเองใด ๆ ที่แนบกับวัสดุได้.  
- **คลาสใดเก็บข้อมูล?** `Material` และ `PropertyCollection` ของมัน.  
- **ฉันจะตั้งค่าสีใหม่อย่างไร?** ใช้ `props.set("Diffuse", new Vector3(r, g, b))`.  
- **ฉันต้องการไลเซนส์หรือไม่?** ไลเซนส์ชั่วคราวทำงานสำหรับการประเมิน; ไลเซนส์เต็มรูปแบบจำเป็นสำหรับการผลิต.  
- **รูปแบบที่รองรับ?** FBX, OBJ, STL, GLTF, และอื่น ๆ อีกมาก.

## ข้อกำหนดเบื้องต้น

- ติดตั้ง Java Development Kit (JDK) 8 หรือใหม่กว่า.  
- ไลบรารี Aspose.3D for Java (ดาวน์โหลดจาก [Aspose website](https://releases.aspose.com/3d/java/)).  
- มีความคุ้นเคยพื้นฐานกับไวยากรณ์ Java และแนวคิดเชิงวัตถุ.

## นำเข้าแพ็กเกจ

ก่อนเขียนตรรกะใด ๆ ให้นำเข้าคลาสที่ให้คุณเข้าถึงคุณสมบัติของวัสดุและการจัดการเวกเตอร์.

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

### ทำไมต้องนำเข้าคลาสเหล่านี้?

- `Scene` โหลดและแสดงไฟล์ 3D.  
- `Material` ให้คำนิยามพื้นผิว (เท็กซ์เจอร์, สี, ฯลฯ).  
- `PropertyCollection` เป็นคอนเทนเนอร์แบบคล้ายพจนานุกรมที่ให้คุณ **เข้าถึงคุณสมบัติของวัสดุ** ตามชื่อ.  
- `Vector3` เป็นประเภทข้อมูลที่ใช้สำหรับสีและเวกเตอร์สามส่วนอื่น ๆ.

## ขั้นตอนที่ 1: เริ่มต้นฉาก

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

เราสร้างอ็อบเจกต์ `Scene` โดยโหลดไฟล์ FBX ที่มีเท็กซ์เจอร์อยู่แล้ว นี่คือผืนแคนวาสที่เราจะ **เปลี่ยนสีพื้นผิว**.

## ขั้นตอนที่ 2: เข้าถึงคุณสมบัติของวัสดุ

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

ที่นี่เรา **เข้าถึงคุณสมบัติของวัสดุ** ของเมชแรกในฉาก วัตถุ `Material` ถือ `PropertyCollection` ที่เก็บแอตทริบิวต์ที่สามารถกำหนดค่าได้ทั้งหมด เช่น *Diffuse*, *Specular*, และข้อมูลผู้ใช้ที่กำหนดเอง.

## ขั้นตอนที่ 3: แสดงรายการคุณสมบัติทั้งหมด

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

การวนลูป `props` จะพิมพ์ชื่อคุณสมบัติทุกอย่างและค่าปัจจุบันของมัน รายการสั้น ๆ นี้ช่วยให้คุณค้นพบคีย์ที่สามารถแก้ไขได้ในภายหลัง เช่น `"Diffuse"` สำหรับสีพื้นฐาน.

## ขั้นตอนที่ 4: ตั้งค่า Vector3 เพื่อเปลี่ยนสีพื้นผิว

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**เคล็ดลับ:** ตัวสร้าง `Vector3` รับตัวเลขทศนิยมสามค่าแสดงส่วน **แดง, เขียว, และน้ำเงิน** (ช่วง 0‑1). การตั้งค่า `(1, 0, 1)` จะเปลี่ยนสีพื้นฐานของเท็กซ์เจอร์เป็นสีแมเจนตา ทำให้ **เปลี่ยนสีพื้นผิว** ของโมเดลได้อย่างมีประสิทธิภาพ.

## ขั้นตอนที่ 5: ดึงคุณสมบัติตามชื่อ

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

นี่เป็นการสาธิต **ดึงคุณสมบัติตามชื่อ** เราแคสท์ `Object` ที่คืนค่ามาเป็น `Vector3` เพื่อทำงานกับสีในโปรแกรม.

## ขั้นตอนที่ 6: เข้าถึงอินสแตนซ์ของคุณสมบัติ

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` คืนค่าอ็อบเจกต์ `Property` เต็มรูปแบบ ให้คุณเข้าถึงเมตาดาต้าเช่น ประเภทของคุณสมบัติ, ป้ายชื่อ, และข้อมูลที่กำหนดเองที่แนบมา.

## ขั้นตอนที่ 7: เดินทางผ่านคุณสมบัติย่อยของคุณสมบัติ

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

บางคุณสมบัติมีโครงสร้างแบบลำดับชั้น การเดินทางผ่าน `pdiffuse.getProperties()` จะทำให้คุณเห็นแอตทริบิวต์ที่ซ้อนอยู่ (เช่น พิกัดเท็กซ์เจอร์, คีย์แอนิเมชัน) ที่เป็นส่วนของรายการ *Diffuse*.

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|---------|
| **`NullPointerException` on `material`** | โหนดอาจไม่มีวัสดุที่กำหนดไว้ | เรียก `node.setMaterial(new Material())` ก่อนเข้าถึงคุณสมบัติ |
| **Color does not change** | โมเดลใช้เท็กซ์เจอร์ที่ทับซ้อนสี *Diffuse* | ปิดการใช้งานเท็กซ์เจอร์หรือแก้ไขภาพเท็กซ์เจอร์โดยตรง |
| **`ClassCastException` when retrieving** | พยายามแคสท์คุณสมบัติที่ไม่ใช่ Vector3 | ตรวจสอบประเภทของคุณสมบัติก่อนแคสท์ด้วย `pdiffuse.getValue().getClass()` |

## คำถามที่พบบ่อย

**Q: ฉันจะติดตั้งไลบรารี Aspose.3D ในโปรเจกต์ Java ของฉันอย่างไร?**  
A: ดาวน์โหลดไฟล์ JAR จาก [Aspose website](https://releases.aspose.com/3d/java/) แล้วเพิ่มเข้าไปใน classpath ของโปรเจกต์หรือใน dependencies ของ Maven/Gradle.

**Q: มีตัวเลือกทดลองใช้ฟรีสำหรับ Aspose.3D หรือไม่?**  
A: มี, คุณสามารถรับการทดลองใช้งานเต็มรูปแบบ 30‑วันจาก [Aspose free trial page](https://releases.aspose.com/).

**Q: ฉันจะหาเอกสารรายละเอียดของ Aspose.3D ใน Java ได้จากที่ไหน?**  
A: เอกสาร API อย่างเป็นทางการอยู่ที่ [Aspose.3D documentation](https://reference.aspose.com/3d/java/).

**Q: มีฟอรั่มสนับสนุนสำหรับ Aspose.3D ที่ฉันสามารถถามคำถามได้หรือไม่?**  
A: มีแน่นอน—เยี่ยมชม [Aspose.3D support forum](https://forum.aspose.com/c/3d/18) เพื่อเชื่อมต่อกับชุมชนและผู้เชี่ยวชาญ.

**Q: ฉันจะขอรับไลเซนส์ชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?**  
A: ขอได้ผ่าน [temporary license page](https://purchase.aspose.com/temporary-license/) บนเว็บไซต์ Aspose.

**Q: ฉันสามารถเปลี่ยนแอตทริบิวต์ของวัสดุอื่น ๆ นอกจากสีได้หรือไม่?**  
A: ได้, คุณสามารถแก้ไขคุณสมบัติเช่น `Specular`, `Opacity`, และข้อมูลผู้ใช้ที่กำหนดเองโดยใช้รูปแบบ `props.set` เดียวกัน.

## สรุป

คุณได้เรียนรู้วิธี **เปลี่ยนสีพื้นผิว**, **เข้าถึงคุณสมบัติของวัสดุ**, **ตั้งค่า Vector3**, และ **ดึงคุณสมบัติตามชื่อ** ในฉาก Java ด้วย Aspose.3D เทคนิคเหล่านี้ให้คุณควบคุมรายละเอียดของทรัพยากร 3D ใด ๆ ได้อย่างละเอียด ทำให้สามารถสร้างเอฟเฟกต์ภาพแบบไดนามิกและการปรับแต่งในขณะรันไทม์ในแอปพลิเคชันของคุณได้.

---

**อัปเดตล่าสุด:** 2025-12-01  
**ทดสอบด้วย:** Aspose.3D for Java 24.11  
**ผู้เขียน:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}