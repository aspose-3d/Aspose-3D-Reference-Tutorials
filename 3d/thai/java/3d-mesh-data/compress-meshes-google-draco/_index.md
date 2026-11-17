---
date: 2026-11-17
description: วิธีลดขนาดโมเดล 3d โดยการสร้างเมชทรงกลมใน Java และบีบอัดด้วย Google Draco
  ผ่าน Aspose.3D เรียนรู้ขั้นตอนทั้งหมดในไม่กี่นาที
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: วิธีลดขนาดโมเดล 3d – สร้างเมชทรงกลมใน Java ด้วย Google Draco
og_description: สร้างเมชทรงกลมและบีบอัดโมเดล 3D ด้วย Java โดยใช้ Aspose.3D และ Google
  Draco บทเรียนนี้แสดงวิธีสร้างทรงกลม ส่งออกเป็น .drc และลดขนาดได้สูงถึง 95% ในไม่กี่นาที
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: สร้างเมชทรงกลมและบีบอัดโมเดล 3D ด้วย Java และ Draco
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: วิธีลดขนาดโมเดล 3d ด้วยเมชทรงกลมใน Java และ Draco
url: /th/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีลดขนาดโมเดล 3 มิติด้วยเมชทรงทรงกลมใน Java และ Draco

## บทนำ

Aspose.3D for Java เป็นไลบรารีที่ช่วยให้คุณสร้าง, ปรับเปลี่ยน, และแปลงรูปแบบโมเดล 3‑D ได้โดยตรงจากโค้ด Java หากคุณกำลังมองหาวิธีที่เร็วในการ **ลดขนาดโมเดล 3d** พร้อมยังคงคุณภาพเรขาคณิตสูง คุณมาถูกที่แล้ว ในบทเรียนนี้เราจะอธิบายการสร้างเมชทรงกลมด้วย **Aspose.3D for Java** แล้วบีบอัดเมชนั้นด้วย **Google Draco** เมื่อเสร็จคุณจะได้ไฟล์ `.drc` ที่ใช้ได้ทันทีและมีขนาดเล็กกว่าต้นฉบับอย่างมาก ทำให้เหมาะสำหรับผู้ชมบนเว็บ, เกมมือถือ, หรือแอปพลิเคชัน Java ที่มีข้อจำกัดด้านแบนด์วิธ

## คำตอบอย่างรวดเร็ว
- **บทเรียนนี้ครอบคลุมอะไร?** การสร้างเมชทรงกลมใน Java และการบีบอัดด้วย Google Draco ผ่าน Aspose.3D.  
- **ไลบรารีหลัก?** Aspose.3D for Java (ใช้สำหรับการสร้างเมชและการส่งออก Draco).  
- **เวลาในการทำงานโดยประมาณ?** ประมาณ 10‑15 นาทีสำหรับทรงกลมพื้นฐาน.  
- **ข้อกำหนดเบื้องต้น?** สภาพแวดล้อมการพัฒนา Java ที่มี Aspose.3D JARs อยู่ใน classpath.  
- **ผลลัพธ์?** ไฟล์ `.drc` ที่ **ลดขนาดโมเดล 3d** ได้ถึง 95 % เมื่อเทียบกับเมชที่ไม่ได้บีบอัด.

## วิธีลดขนาดโมเดล 3d ?

โหลดทรงกลมของคุณและบีบอัดในสองขั้นตอนง่าย ๆ ขั้นแรกคุณ **สร้างเมชทรงกลม** ด้วย `new Sphere(1.0, 32, 32)` จากนั้นส่งออกฉากโดยตรงเป็น Draco ด้วย `scene.save("sphere.drc", SaveFormat.Draco)` Aspose.3D จะจัดการการควอนตาไลซ์เรขาคณิตและการลบจุดซ้ำโดยอัตโนมัติ ส่งมอบไฟล์ที่มักจะเล็กลง 80‑95 % พร้อมคงความคมชัดของภาพ

คลาส `Sphere` เป็นเครื่องมือสร้างเรขาคณิตในตัวของ Aspose.3D ที่สร้างเมชทรงกลมแบบสามเหลี่ยม มันรับค่ารัศมีและพารามิเตอร์การตัดแบ่ง (tessellation) เพื่อให้คุณควบคุมระดับรายละเอียดก่อนการบีบอัด

## “การลดขนาดโมเดล 3d” หมายถึงอะไรในบริบทของการพัฒนา 3d ?

**การลดขนาดโมเดล 3d** หมายถึงการทำให้ข้อมูลเรขาคณิตที่ต้องส่งหรือเก็บน้อยลงโดยไม่ทำให้คุณภาพภาพลดลงอย่างเห็นได้ชัด Draco ทำเช่นนี้โดยการเข้ารหัสตำแหน่งเวอร์เท็กซ์, ปกติ, และแอตทริบิวต์อื่น ๆ ในรูปแบบไบนารีที่กะทัดรัด เมื่อใช้ร่วมกับ Aspose.3D กระบวนการทั้งหมดอยู่ใน Java ทำให้คุณไม่ต้องจัดการไบนารีเนทีฟของ Draco

## ทำไมต้องใช้การบีบอัดเมช Google Draco กับ Aspose.3D ?

Google Draco ร่วมกับ Aspose.3D ให้ไพป์ไลน์ที่มีประสิทธิภาพซึ่งลดขนาดไฟล์เมชอย่างมหาศาลพร้อมยังคงง่ายต่อการรวมเข้ากับโปรเจกต์ Java ไลบรารีจัดการการเข้ารหัสระดับต่ำทั้งหมด ทำให้นักพัฒนามุ่งเน้นที่การสร้างเรขาคณิตโดยไม่ต้องยุ่งกับไบนารี Draco เนทีฟ ส่งผลให้การพัฒนาเร็วขึ้นและสินทรัพย์เล็กลงสำหรับเว็บและมือถือ

- **การลดขนาดอย่างมหาศาล:** Draco สามารถลดข้อมูลเมชได้ถึง 95 % สำหรับโมเดลทั่วไป, ทำให้ไฟล์ OBJ ขนาด 5 MB กลายเป็น `.drc` ขนาด 0.3 MB.  
- **การถอดรหัสเร็วใน runtime:** Engine เช่น Unity, Unreal, และ three.js สามารถถอดรหัส Draco ได้โดยตรง, ทำให้เวลาโหลดเร็วขึ้น.  
- **การบูรณาการกับ Java อย่างราบรื่น:** Aspose.3D ทำหน้าที่เป็น wrapper ของไลบรารี Draco ดั้งเดิม, ให้คุณทำงานอยู่ใน ecosystem ของ Java.  
- **การส่งออก Aspose 3D ครบวงจร:** API เดียวที่ใช้สร้างเรขาคณิตยังสามารถส่งออกได้, ทำให้กระบวนการง่ายขึ้น.  

Aspose.3D รองรับ **รูปแบบไฟล์เข้าและออกกว่า 50 แบบ** — รวมถึง OBJ, FBX, STL, GLTF, และอื่น ๆ อีกมาก — และสามารถประมวลผลโมเดลหลายร้อยหน้าโดยไม่ต้องโหลดไฟล์ทั้งหมดเข้าสู่หน่วยความจำ

## ข้อกำหนดเบื้องต้น

- **Java Development Kit (JDK)** – เวอร์ชัน 8 หรือใหม่กว่า.  
- **Aspose.3D for Java** – ดาวน์โหลด JAR ล่าสุดจาก **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)**.  
- **ความคุ้นเคยพื้นฐานกับ Google Draco** – คุณจะใช้ wrapper ของ Aspose.3D, ดังนั้นไม่จำเป็นต้องตั้งค่า Draco เนทีฟ

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

## คู่มือขั้นตอนต่อขั้นตอน

### ขั้นตอน 1: ตั้งค่าโปรเจกต์

สร้างโปรเจกต์ Java ใหม่ (IDE ใดก็ได้) แล้วเพิ่ม JAR ของ Aspose.3D ทั้งหมดลงใน classpath เก็บไฟล์ซอร์สของคุณในแพ็กเกจเช่น `com.example.draco` เพื่อความชัดเจน

### ขั้นตอน 2: วิธีสร้างเมชทรงกลมใน Java

คลาส `Sphere` เป็นเครื่องมือสร้างเรขาคณิตในตัวของ Aspose.3D ที่สร้างเมชทรงกลมแบบสามเหลี่ยม  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **เคล็ดลับ:** คลาส `Sphere` สร้างเมชสามเหลี่ยมด้วยรัศมีเริ่มต้นที่ 1.0 คุณสามารถส่งรัศมี, การตัดแบ่ง, หรือพารามิเตอร์วัสดุที่กำหนดเองได้หากต้องการระดับรายละเอียดที่แตกต่างก่อนการบีบอัด

### ขั้นตอน 3: ส่งออกเมชเป็นรูปแบบ Draco

คลาส `Scene` แทนฉาก 3‑D สมบูรณ์ที่สามารถบรรจุเมช, แสง, และกล้อง คลาส `DracoCompressionOptions` ให้คุณปรับแต่งการตั้งค่าการบีบอัด Draco เช่น การควอนตาไลซ์และระดับการบีบอัด หลังจากเพิ่มทรงกลมลงในอ็อบเจกต์ `Scene` แล้วเรียก `scene.save("sphere.drc", SaveFormat.Draco)` Aspose.3D จะเลือกการตั้งค่าการบีบอัดที่เหมาะสมโดยอัตโนมัติ, แต่คุณสามารถปรับให้ละเอียดโดยแก้ไข `DracoCompressionOptions` หากต้องการไฟล์ที่เล็กที่สุดเท่าที่จะเป็นไปได้ `DracoCompressionOptions` ให้คุณ

### ขั้นตอน 4: ตรวจสอบผลลัพธ์

`DRACOLoader` เป็นยูทิลิตี้ของ three.js ที่โหลดไฟล์ `.drc` ที่บีบอัดด้วย Draco และแปลงเป็นเรขาคณิตที่เข้ากันได้กับ WebGL เปิดไฟล์ `.drc` ที่สร้างขึ้นด้วยตัวดู Draco (เช่น three.js `DRACOLoader`) เพื่อยืนยันว่าเรขาคณิตแสดงผลถูกต้อง คุณจะสังเกตเห็นการลดขนาดไฟล์อย่างมหาศาล — มักเป็นปัจจัยสิบเท่าหรือมากกว่า

## กรณีการใช้งานทั่วไป

| สถานการณ์ | ทำไมต้องลดขนาดโมเดล? | วิธีที่บทเรียนนี้ช่วยได้ |
|----------|-----------------------|--------------------------|
| ตัวกำหนดผลิตภัณฑ์บนเว็บ | โหลดหน้าเร็วขึ้นบนการเชื่อมต่อช้า | ไฟล์ `.drc` ที่บีบอัดด้วย Draco โหลดได้ในไม่กี่วินาที |
| แอป AR/VR บนมือถือ | ใช้หน่วยความจำน้อยลงบนอุปกรณ์ | เมชขนาดเล็กทำให้แอปตอบสนองได้ดี |
| ฉากที่เรนเดอร์บนคลาวด์ | ลดค่าใช้จ่ายแบนด์วิธ | ส่งออกด้วยคลิกเดียวจาก Aspose.3D ไปยัง Draco |

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | JAR ของ Aspose.3D ไม่อยู่ใน classpath | ตรวจสอบว่า *ทั้งหมด* ไฟล์ JAR ของ Aspose.3D ถูกใส่ไว้และเวอร์ชันตรงกับเอกสาร |
| **ไฟล์ผลลัพธ์ว่างเปล่า** | `MyDir` ชี้ไปยังโฟลเดอร์ที่ไม่มีอยู่ | สร้างโฟลเดอร์โดยโปรแกรม (`Files.createDirectories(Paths.get(MyDir))`) ก่อนเขียนไฟล์ |
| **เมชที่บีบอัดดูบิดเบี้ยว** | ใช้ระดับการบีบอัดต่ำหรือ tessellation ไม่เพียงพอ | เปลี่ยนเป็น `DracoCompressionLevel.OPTIMAL` และเพิ่ม tessellation ของทรงกลม (เช่น `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` เลือกคุณภาพการบีบอัดสูงสุดสำหรับผลลัพธ์ Draco |

## คำถามที่พบบ่อย

**ถาม: Aspose.3D รองรับรูปแบบไฟล์ 3d ต่าง ๆ หรือไม่?**  
ตอบ: ใช่, Aspose.3D รองรับ OBJ, FBX, STL, GLTF, และรูปแบบอื่น ๆ มากมาย ทำให้เป็นตัวเลือกที่หลากหลายสำหรับ **การส่งออก Aspose 3d** pipelines

**ถาม: ฉันสามารถใช้ Google Draco สำหรับการบีบอัดในภาษาโปรแกรมอื่นได้หรือไม่?**  
ตอบ: แน่นอน. Draco มีไลบรารีเนทีฟสำหรับ C++, Python, และ JavaScript บทเรียนนี้เน้นที่ Java แต่แนวคิดเดียวกันใช้ได้กับหลายภาษา

**ถาม: ฉันจะหาเอกสารเพิ่มเติมของ Aspose.3D ได้จากที่ไหน?**  
ตอบ: เยี่ยมชม **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** เพื่อดู API อย่างเต็มและตัวอย่างเพิ่มเติม

**ถาม: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?**  
ตอบ: สำรวจตัวเลือกใบอนุญาตชั่วคราวได้ที่ **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**

**ถาม: มีฟอรั่มชุมชนสำหรับการสนับสนุน Aspose.3D หรือไม่?**  
ตอบ: มี, เข้าร่วมการสนทนาที่ **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**

## สรุป

ในคู่มือนี้เราได้แสดงวิธี **ลดขนาดโมเดล 3d** ด้วยการสร้างเมชทรงกลมใน Java แล้วบีบอัดด้วย Google Draco ผ่าน Aspose.3D โดยทำตามขั้นตอนสั้น ๆ นี้คุณสามารถลดขนาดไฟล์เมชได้อย่างมาก, ปรับปรุงเวลาโหลด, และทำให้แอปพลิเคชัน 3d ที่ใช้ Java ของคุณตอบสนองได้ดีและใช้แบนด์วิธน้อยลง

---

**อัปเดตล่าสุด:** 2026-11-17  
**ทดสอบกับ:** Aspose.3D for Java 24.12 (latest)  
**ผู้เขียน:** Aspose

## บทเรียนที่เกี่ยวข้อง

- [ลดขนาดไฟล์ 3D – บีบอัดฉากด้วย Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [สร้างคลาวด์จุด Draco จากทรงกลมโดยใช้ Aspose.3D for Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [เรียนรู้วิธีทำให้เมชเป็นสามเหลี่ยมเพื่อการเรนเดอร์ที่เพิ่มประสิทธิภาพใน Java ด้วย Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}