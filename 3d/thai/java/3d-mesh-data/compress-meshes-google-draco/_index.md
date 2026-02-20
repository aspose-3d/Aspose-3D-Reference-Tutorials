---
date: 2026-01-27
description: เรียนรู้วิธีสร้างเมชทรงกลมใน Java และบีบอัดไฟล์เมช 3 มิติด้วย Google
  Draco พร้อม Aspose.3D คู่มือขั้นตอนต่อขั้นตอนสำหรับการพัฒนา 3 มิติที่มีประสิทธิภาพ
linktitle: How to Create Sphere Mesh in Java – Compress 3D Meshes with Google Draco
second_title: Aspose.3D Java API
title: วิธีสร้างเมชทรงกลมใน Java – บีบอัดเมช 3 มิติด้วย Google Draco
url: /th/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีสร้าง Sphere Mesh ใน Java – บีบอัด 3D Mesh ด้วย Google Draco

## คำแนะนำเบื้องต้น

หากคุณกำลังมองหา **วิธีสร้าง sphere** mesh ใน Java พร้อมไฟล์ขนาดเล็กที่สุด คุณมาถูกที่แล้ว ในบทเรียนนี้เราจะใช้ **Aspose.3D** ร่วมกับ **Google Draco** เพื่อ **บีบอัด 3D mesh** อย่างมีประสิทธิภาพ เมื่อเสร็จสิ้นคุณจะได้ sphere mesh ที่พร้อมใช้งานและบันทึกเป็นไฟล์ `.drc` ที่บีบอัดด้วย Draco ซึ่งโหลดได้เร็วขึ้นและใช้แบนด์วิดท์น้อยลงในแอปพลิเคชัน 3D ที่พัฒนาโดย Java

## คำตอบสั้น ๆ
- **บทเรียนนี้ครอบคลุมอะไร?** การสร้าง sphere mesh ใน Java และการบีบอัดด้วย Google Draco ผ่าน Aspose.3D  
- **ไลบรารีหลัก?** Aspose.3D for Java  
- **เวลาในการทำงานโดยประมาณ?** ประมาณ 10‑15 นาทีสำหรับ sphere พื้นฐาน  
- **ข้อกำหนดเบื้องต้นสำคัญ?** มีสภาพแวดล้อมการพัฒนา Java และ Aspose.3D JARs อยู่ใน classpath ของคุณ  
- **ผลลัพธ์?** ไฟล์ `.drc` ที่บรรจุ sphere mesh ที่บีบอัดแล้ว  

## “วิธีสร้าง sphere” หมายถึงอะไรในบริบทของการพัฒนา 3D?

การสร้าง sphere mesh หมายถึงการสร้างชุดของจุดยอด (vertices), เส้นเชื่อม (edges) และหน้า (faces) ที่ประมาณรูปทรงทรงกลมที่สมบูรณ์แบบ คลาส `Sphere` ของ Aspose.3D ทำงานหนักให้คุณโดยสร้าง mesh ที่เป็นรูปสามเหลี่ยม (triangulated) ที่สามารถนำไปประมวลผลหรือบีบอัดต่อได้

## ทำไมต้องใช้ Google Draco mesh compression กับ Aspose.3D?

- **ลดขนาดอย่างมหาศาล:** Draco สามารถทำให้ข้อมูล mesh ลดลงได้ถึง 90 % เมื่อเทียบกับรูปแบบที่ไม่ได้บีบอัด  
- **การถอดรหัสเร็วใน runtime:** เอนจิ้นสมัยใหม่เช่น Unity และ three.js รองรับการถอดรหัส Draco โดยตรง ทำให้เวลาโหลดสั้นลง  
- **การผสานรวมกับ Java อย่างไร้รอยต่อ:** Aspose.3D แอบซ่อนไลบรารี Draco ดั้งเดิม ทำให้คุณทำงานอยู่ใน ecosystem ของ Java โดยไม่ต้องจัดการกับไบนารีเนทีฟ  

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเริ่มทำตามขั้นตอน ตรวจสอบให้แน่ใจว่าคุณมี:

- **Java Development Kit (JDK)** – เวอร์ชัน 8 หรือใหม่กว่า ติดตั้งและตั้งค่าเรียบร้อยแล้ว  
- **Aspose.3D for Java** – ดาวน์โหลด JAR ล่าสุดจากหน้าอย่างเป็นทางการ [ที่นี่](https://releases.aspose.com/3d/java/)  
- **ความรู้พื้นฐานเกี่ยวกับ Google Draco** – เข้าใจว่า Draco เป็นไลบรารีบีบอัดเรขาคณิต; เราจะใช้ wrapper ของ Aspose.3D เพื่อจัดการงานหนัก  

## การนำเข้าแพ็กเกจ

ในไฟล์ซอร์ส Java ของคุณ ให้นำเข้าคลาสที่จำเป็นสำหรับการสร้าง mesh และการบีบอัด Draco

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## คู่มือขั้นตอนโดยละเอียด

### ขั้นตอนที่ 1: ตั้งค่าโปรเจกต์

สร้างโปรเจกต์ Java ใหม่ (IDE ที่คุณชอบ) แล้วเพิ่ม Aspose.3D JARs ลงใน classpath ของโปรเจกต์ จัดโฟลเดอร์ซอร์สให้โค้ดด้านล่างอยู่ในแพ็กเกจที่สะอาด เช่น `com.example.draco`

### ขั้นตอนที่ 2: วิธีสร้าง Sphere Mesh ใน Java

ต่อไปเราจะสร้างโมเดล sphere อย่างง่าย ซึ่งจะเป็น mesh ที่เราต้องการบีบอัด

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **เคล็ดลับ:** คลาส `Sphere` จะสร้าง mesh ที่เป็นรูปสามเหลี่ยมโดยอัตโนมัติด้วยรัศมีเริ่มต้นที่ 1.0 คุณสามารถปรับรัศมี, การแบ่งส่วน (tessellation) และวัสดุได้ตามความต้องการของคุณ  

### ขั้นตอนที่ 3: วิธีบีบอัด Mesh ด้วย Google Draco

เมื่อ sphere พร้อมแล้ว เราจะเรียกใช้การบีบอัด Draco ผ่าน `DracoSaveOptions` ของ Aspose.3D การตั้งค่าระดับบีบอัดเป็น `OPTIMAL` จะให้การลดขนาดที่ดีที่สุดพร้อมรักษาคุณภาพ

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

### ขั้นตอนที่ 4: บันทึก Mesh ที่บีบอัดแล้ว

สุดท้ายให้เขียนอาร์เรย์ไบต์ที่บีบอัดแล้วลงไฟล์ `.drc` ไฟล์นี้สามารถสตรีมไปยังไคลเอนต์หรือเก็บไว้ใช้ในภายหลังได้

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

คุณสามารถทำซ้ำขั้นตอนเหล่านี้กับวัตถุ 3D ใด ๆ — ลูกบาศก์, โมเดลที่กำหนดเอง, หรือฉากที่นำเข้า — เพียงเปลี่ยนการเรียกสร้างเรขาคณิตเท่านั้น  

## ปัญหาที่พบบ่อยและวิธีแก้

| Issue | Reason | Fix |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D JARs ไม่อยู่ใน classpath | ตรวจสอบให้แน่ใจว่าไฟล์ Aspose.3D JAR ทั้งหมดรวมอยู่และเวอร์ชันตรงกับเอกสาร |
| **Output file is empty** | `MyDir` ชี้ไปยังโฟลเดอร์ที่ไม่มีอยู่ | สร้างโฟลเดอร์นั้นก่อนหรือให้โค้ดสร้างโดยอัตโนมัติ |
| **Compressed mesh looks distorted** | ใช้ระดับบีบอัดต่ำ | เปลี่ยนเป็น `DracoCompressionLevel.OPTIMAL` หรือปรับการแบ่งส่วนของ mesh ก่อนบีบอัด |

## คำถามที่พบบ่อย

**Q: Aspose.3D รองรับรูปแบบไฟล์ 3D ต่าง ๆ หรือไม่?**  
A: ใช่, Aspose.3D รองรับรูปแบบหลากหลายรวมถึง OBJ, FBX, STL, และ GLTF ทำให้ใช้งานได้หลากหลายใน pipeline ต่าง ๆ  

**Q: สามารถใช้ Google Draco บีบอัดในภาษาโปรแกรมอื่นได้หรือไม่?**  
A: แน่นอน. Draco มีไลบรารีเนทีฟสำหรับ C++, Python, และ JavaScript บทเรียนนี้เน้นที่ Java แต่แนวคิดสามารถนำไปใช้กับภาษาอื่นได้  

**Q: จะหาเอกสารเพิ่มเติมของ Aspose.3D ได้จากที่ไหน?**  
A: เยี่ยมชม [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) เพื่อดูรายละเอียด API และตัวอย่างเพิ่มเติม  

**Q: จะขอรับลิขสิทธิ์ชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?**  
A: สำรวจตัวเลือกลิขสิทธิ์ชั่วคราวได้ [ที่นี่](https://purchase.aspose.com/temporary-license/)  

**Q: มีฟอรั่มชุมชนสำหรับการสนับสนุน Aspose.3D หรือไม่?**  
A: มี, สำหรับการสนับสนุนและการสนทนาชุมชน ไปที่ [Aspose.3D Forum](https://forum.aspose.com/c/3d/18)  

## สรุป

ในบทเรียนนี้เราได้แสดง **วิธีสร้าง sphere** mesh ใน Java แล้ว **บีบอัด 3D mesh** ด้วย Google Draco ผ่าน Aspose.3D ด้วยการทำตามขั้นตอนเหล่านี้ คุณจะสามารถลดขนาดไฟล์ mesh อย่างมหาศาล, ปรับปรุงเวลาโหลด, และทำให้แอปพลิเคชัน 3D ที่พัฒนาโดย Java มีความตอบสนองที่ดีขึ้น  

---

**อัปเดตล่าสุด:** 2026-01-27  
**ทดสอบด้วย:** Aspose.3D for Java 24.12 (latest)  
**ผู้เขียน:** Aspose  

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**อัปเดตล่าสุด:** 2026-01-27  
**ทดสอบด้วย:** Aspose.3D for Java 24.12 (latest)  
**ผู้เขียน:** Aspose  

---