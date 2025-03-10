---
title: ใช้วัสดุ PBR กับวัตถุ 3 มิติใน Java ด้วย Aspose.3D
linktitle: ใช้วัสดุ PBR กับวัตถุ 3 มิติใน Java ด้วย Aspose.3D
second_title: Aspose.3D จาวา API
description: เรียนรู้การใช้วัสดุ PBR ที่สมจริงกับวัตถุ 3 มิติใน Java โดยใช้ Aspose.3D ปรับปรุงคุณภาพของภาพด้วยการเรนเดอร์ตามทางกายภาพ
weight: 10
url: /th/java/geometry/apply-pbr-materials-to-objects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ใช้วัสดุ PBR กับวัตถุ 3 มิติใน Java ด้วย Aspose.3D

## การแนะนำ

ยินดีต้อนรับสู่คำแนะนำทีละขั้นตอนเกี่ยวกับการใช้วัสดุการเรนเดอร์ตามทางกายภาพ (PBR) กับวัตถุ 3 มิติใน Java โดยใช้ Aspose.3D Aspose.3D เป็นไลบรารี Java ที่ทรงพลังซึ่งมีฟังก์ชันการทำงานที่ครอบคลุมสำหรับการทำงานกับโมเดลและฉาก 3D ในบทช่วยสอนนี้ เราจะมุ่งเน้นไปที่การใช้วัสดุ PBR ซึ่งจำลองแสงและคุณสมบัติพื้นผิวในโลกแห่งความเป็นจริง เพิ่มความสมจริงของวัตถุ 3 มิติของคุณ

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

1. สภาพแวดล้อมการพัฒนา Java: ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง Java บนระบบของคุณแล้ว

2.  ไลบรารี Aspose.3D: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D จาก[ลิ้งค์ดาวน์โหลด](https://releases.aspose.com/3d/java/).

3.  เอกสารประกอบ: โปรดดูที่[เอกสารประกอบ](https://reference.aspose.com/3d/java/)เพื่อให้ Aspose.3D ทำความคุ้นเคยกับคุณสมบัติของไลบรารี

4.  ใบอนุญาตชั่วคราว (ไม่บังคับ): หากคุณไม่มีใบอนุญาต คุณสามารถขอรับ[ใบอนุญาตชั่วคราว](https://purchase.aspose.com/temporary-license/) สำหรับการทดสอบ

## แพ็คเกจนำเข้า

ในโปรเจ็กต์ Java ของคุณ ให้รวมแพ็คเกจที่จำเป็นเพื่อใช้ Aspose.3D เพิ่มคำสั่งการนำเข้าต่อไปนี้ลงในโค้ดของคุณ:

```java
import com.aspose.threed.*;
```

## ขั้นตอนที่ 1: เริ่มต้นฉาก

เริ่มต้นด้วยการสร้างฉาก 3 มิติโดยใช้ Aspose.3D ฉากนี้ทำหน้าที่เป็นผืนผ้าใบสำหรับวัตถุ 3 มิติของคุณ

```java
// ExStart: เตรียมใช้งาน Scene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd: เตรียมใช้งานฉาก
```

## ขั้นตอนที่ 2: เริ่มต้นวัสดุ PBR

สร้างวัสดุ PBR และปรับแต่งคุณสมบัติของมัน เช่น โลหะและความหยาบ

```java
// ExStart: เตรียมใช้งาน PBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd: เตรียมใช้งาน PBRMaterial
```

## ขั้นตอนที่ 3: สร้างวัตถุ 3 มิติ

สร้างวัตถุ 3 มิติ (เช่น กล่อง) ที่จะใช้วัสดุ PBR

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

## ขั้นตอนที่ 4: บันทึกฉาก 3 มิติ

บันทึกฉาก 3D รวมถึงวัสดุ PBR ที่นำไปใช้ เป็นรูปแบบไฟล์เฉพาะ เช่น STL

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
//ExEnd:Save3DScene
```

ทำซ้ำขั้นตอนเหล่านี้สำหรับฉากที่ซับซ้อนมากขึ้นหรือวัตถุต่างๆ

## บทสรุป

ยินดีด้วย! คุณนำวัสดุ PBR ไปใช้กับวัตถุ 3 มิติใน Java โดยใช้ Aspose.3D ได้สำเร็จ สิ่งนี้จะช่วยเพิ่มความน่าดึงดูดด้านภาพของโมเดล 3 มิติของคุณ ทำให้สมจริงและน่าทึ่งยิ่งขึ้น

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่

 A1: ใช่คุณทำได้ เยี่ยมชม[หน้าซื้อ](https://purchase.aspose.com/buy) สำหรับรายละเอียดใบอนุญาต

### คำถามที่ 2: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้อย่างไร

 A2: เข้าร่วม[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) สำหรับการสนับสนุนและช่วยเหลือชุมชน

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

 A3: ใช่ คุณสามารถสำรวจได้[ทดลองฟรี](https://releases.aspose.com/) ก่อนตัดสินใจซื้อ

### คำถามที่ 4: ฉันจะหาเอกสารโดยละเอียดสำหรับ Aspose.3D ได้ที่ไหน

 A4: โปรดดูที่[เอกสารประกอบ](https://reference.aspose.com/3d/java/) เพื่อรับคำแนะนำอย่างครอบคลุม

### คำถามที่ 5: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับการทดสอบได้อย่างไร

 A5: เยี่ยมเลย[ลิงค์นี้](https://purchase.aspose.com/temporary-license/) เพื่อรับใบอนุญาตชั่วคราว
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
