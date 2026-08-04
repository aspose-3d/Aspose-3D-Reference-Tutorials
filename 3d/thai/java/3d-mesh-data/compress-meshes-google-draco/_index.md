---
date: 2026-04-29
description: เรียนรู้วิธีลดขนาดโมเดล 3 มิติโดยการสร้างเมชทรงทรงกลมใน Java และบีบอัดด้วย
  Google Draco โดยใช้ Aspose.3D – สิ่งจำเป็นสำหรับการส่งออก Aspose 3D
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: วิธีสร้างเมชทรงกลมใน Java – บีบอัดเมช 3 มิติด้วย Google Draco
second_title: Aspose.3D Java API
title: 'ลดขนาดโมเดล 3 มิติ: สร้างเมชทรงกลมใน Java ด้วย Draco'
url: /th/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ลดขนาดโมเดล 3 มิติ: สร้างเมชทรงทรงกลมใน Java ด้วย Draco

## คำแนะนำ

หากคุณกำลังมองหาวิธีที่รวดเร็วในการ **ลดขนาดโมเดล 3 มิติ** พร้อมยังคงคุณภาพเรขาคณิตที่สูง คุณมาถูกที่แล้ว ในบทแนะนำนี้เราจะอธิบายการสร้างเมชทรงกลมด้วย **Aspose.3D for Java** แล้วบีบอัดเมชนั้นด้วย **Google Draco** เมื่อเสร็จสิ้นคุณจะได้ไฟล์ `.drc` ที่ใช้ได้ทันทีและมีขนาดเล็กกว่าต้นฉบับอย่างมาก เหมาะสำหรับผู้ชมบนเว็บ, เกมมือถือ, หรือแอปพลิเคชัน Java ที่มีข้อจำกัดด้านแบนด์วิธ

## คำตอบสั้น ๆ
- **บทแนะนำนี้ครอบคลุมอะไร?** การสร้างเมชทรงกลมใน Java และการบีบอัดด้วย Google Draco ผ่าน Aspose.3D  
- **ไลบรารีหลัก?** Aspose.3D for Java (ใช้ทั้งการสร้างเมชและการส่งออก Draco)  
- **เวลาในการทำงานโดยประมาณ?** ประมาณ 10‑15 นาทีสำหรับทรงกลมพื้นฐาน  
- **ข้อกำหนดสำคัญ?** สภาพแวดล้อมการพัฒนา Java พร้อม JAR ของ Aspose.3D อยู่ใน classpath  
- **ผลลัพธ์?** ไฟล์ `.drc` ที่ **ลดขนาดโมเดล 3 มิติ** ได้สูงสุดถึง 90 % เมื่อเทียบกับเมชที่ไม่ได้บีบอัด

## “ลดขนาดโมเดล 3 มิติ” หมายถึงอะไรในบริบทของการพัฒนา 3 มิติ?

การลดขนาดโมเดล 3 มิติหมายถึงการทำให้ข้อมูลเรขาคณิตที่ต้องส่งหรือจัดเก็บมีขนาดเล็กลงโดยไม่ทำให้คุณภาพภาพลดลงอย่างเห็นได้ชัด Draco ทำเช่นนี้โดยการเข้ารหัสตำแหน่งเวอร์เท็กซ์, ปกติ, และแอตทริบิวต์อื่น ๆ ในรูปแบบไบนารีที่มีความกะทัดรัดสูง เมื่อใช้ร่วมกับ Aspose.3D กระบวนการทั้งหมดอยู่ใน Java ทำให้ไม่ต้องจัดการกับไบนารีเนทีฟ

## ทำไมต้องใช้การบีบอัดเมช Google Draco กับ Aspose.3D?

- **ลดขนาดอย่างมหาศาล:** Draco สามารถลดข้อมูลเมชได้ถึง 90 % เมื่อเทียบกับฟอร์แมตเช่น OBJ หรือ STL  
- **การถอดรหัสเร็วใน runtime:** เอนจิ้นเช่น Unity, Unreal, และ three.js สามารถถอดรหัส Draco ได้โดยตรง ทำให้เวลาโหลดเร็วขึ้น  
- **การบูรณาการกับ Java อย่างไร้รอยต่อ:** Aspose.3D ทำหน้าที่เป็น wrapper ให้กับไลบรารี Draco เนทีฟ ทำให้คุณอยู่ในระบบนิเวศของ Java ทั้งหมด  
- **การส่งออก Aspose 3D ครบวงจร:** API เดียวที่ใช้สร้างเรขาคณิตยังสามารถส่งออกไฟล์ได้ ทำให้ขั้นตอนง่ายขึ้น

## ข้อกำหนดเบื้องต้น

- **Java Development Kit (JDK)** – เวอร์ชัน 8 หรือใหม่กว่า  
- **Aspose.3D for Java** – ดาวน์โหลด JAR ล่าสุดจากหน้าอย่างเป็นทางการ [ที่นี่](https://releases.aspose.com/3d/java/)  
- **ความคุ้นเคยพื้นฐานกับ Google Draco** – คุณจะใช้ wrapper ของ Aspose.3D จึงไม่ต้องตั้งค่า Draco แบบเนทีฟ

## นำเข้าแพ็กเกจ

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

สร้างโปรเจกต์ Java ใหม่ (IDE ใดก็ได้) แล้วเพิ่ม JAR ของ Aspose.3D ทั้งหมดลงใน classpath เก็บไฟล์ซอร์สของคุณในแพ็กเกจเช่น `com.example.draco` เพื่อความชัดเจน

### ขั้นตอนที่ 2: วิธีสร้างเมชทรงกลมใน Java

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **เคล็ดลับ:** คลาส `Sphere` จะสร้างเมชที่ทำไตรแองเกิลโดยมีรัศมีเริ่มต้นที่ 1.0 คุณสามารถกำหนดรัศมี, การตัดแบ่ง (tessellation) หรือพารามิเตอร์วัสดุอื่น ๆ หากต้องการระดับรายละเอียดที่แตกต่างก่อนบีบอัด

### ขั้นตอนที่ 3: วิธีบีบอัดเมชด้วย Google Draco

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

การตั้งค่าระดับการบีบอัดเป็น `OPTIMAL` จะให้การลดขนาดสูงสุดพร้อมคงคุณภาพภาพไว้ ทำให้คุณ **ลดขนาดโมเดล 3 มิติ** ได้อย่างมีประสิทธิภาพ

### ขั้นตอนที่ 4: บันทึกเมชที่บีบอัดแล้ว

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

ไฟล์ `SphereMeshtoDRC_Out.drc` ที่ได้สามารถสตรีมให้ลูกค้า, เก็บไว้ใน CDN, หรือโหลดโดยตรงโดยเอนจิ้นที่รองรับ Draco ใด ๆ

## กรณีการใช้งานทั่วไป

| สถานการณ์ | ทำไมต้องลดขนาดโมเดล? | วิธีที่บทแนะนำนี้ช่วย |
|----------|-----------------------|------------------------|
| ตัวกำหนดค่าผลิตภัณฑ์บนเว็บ | โหลดหน้าเร็วขึ้นบนการเชื่อมต่อช้า | ไฟล์ `.drc` บีบอัดด้วย Draco โหลดได้ในไม่กี่วินาที |
| แอป AR/VR บนมือถือ | ลดการใช้หน่วยความจำบนอุปกรณ์ | เมชขนาดเล็กทำให้แอปตอบสนองได้ดี |
| ฉากที่เรนเดอร์บนคลาวด์ | ลดค่าแบนด์วิธ | ส่งออกด้วยคลิกเดียวจาก Aspose.3D ไปยัง Draco |

## ปัญหาที่พบบ่อยและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|--------|
| **`NoClassDefFoundError` สำหรับคลาส Draco** | JAR ของ Aspose.3D ไม่อยู่ใน classpath | ตรวจสอบให้แน่ใจว่า *ทุก* JAR ของ Aspose.3D ถูกเพิ่มและเวอร์ชันตรงกับเอกสาร |
| **ไฟล์ผลลัพธ์ว่างเปล่า** | ตัวแปร `MyDir` ชี้ไปยังโฟลเดอร์ที่ไม่มีอยู่ | สร้างโฟลเดอร์โดยโปรแกรม (`Files.createDirectories(Paths.get(MyDir))`) ก่อนเขียนไฟล์ |
| **เมชที่บีบอัดดูบิดเบี้ยว** | ใช้ระดับการบีบอัดต่ำหรือ tessellation ไม่เพียงพอ | เปลี่ยนเป็น `DracoCompressionLevel.OPTIMAL` และเพิ่ม tessellation ของทรงกลม (เช่น `new Sphere(1.0, 64, 64)`) |

## คำถามที่พบบ่อย

**ถาม: Aspose.3D รองรับฟอร์แมตไฟล์ 3 มิติหลายประเภทหรือไม่?**  
ตอบ: ใช่, Aspose.3D รองรับ OBJ, FBX, STL, GLTF และอื่น ๆ อีกมาก ทำให้เป็นตัวเลือกที่หลากหลายสำหรับ **การส่งออก Aspose 3D**  

**ถาม: สามารถใช้ Google Draco สำหรับบีบอัดในภาษาโปรแกรมอื่นได้หรือไม่?**  
ตอบ: แน่นอน. Draco มีไลบรารีเนทีฟสำหรับ C++, Python, และ JavaScript บทแนะนำนี้เน้นที่ Java แต่แนวคิดเดียวกันใช้ได้กับหลายภาษา  

**ถาม: จะหาเอกสารเพิ่มเติมของ Aspose.3D ได้จากที่ไหน?**  
ตอบ: เยี่ยมชม [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) เพื่อดู API อย่างเต็มและตัวอย่างเพิ่มเติม  

**ถาม: จะขอรับไลเซนส์ชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?**  
ตอบ: สำรวจตัวเลือกไลเซนส์ชั่วคราว [ที่นี่](https://purchase.aspose.com/temporary-license/)  

**ถาม: มีฟอรั่มชุมชนสำหรับการสนับสนุน Aspose.3D หรือไม่?**  
ตอบ: มี, เข้าร่วมการสนทนาที่ [Aspose.3D Forum](https://forum.aspose.com/c/3d/18)  

## สรุป

ในคู่มือนี้เราได้สาธิตวิธี **ลดขนาดโมเดล 3 มิติ** ด้วยการสร้างเมชทรงกลมใน Java แล้วบีบอัดด้วย Google Draco ผ่าน Aspose.3D โดยทำตามขั้นตอนสั้น ๆ นี้คุณสามารถทำให้ไฟล์เมชเล็กลงอย่างมาก, ปรับปรุงเวลาโหลด, และทำให้แอปพลิเคชัน 3 มิติบน Java ของคุณตอบสนองได้ดีและใช้แบนด์วิธน้อยลง

---

**อัปเดตล่าสุด:** 2026-04-29  
**ทดสอบด้วย:** Aspose.3D for Java 24.12 (ล่าสุด)  
**ผู้เขียน:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}