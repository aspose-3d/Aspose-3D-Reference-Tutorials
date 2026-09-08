---
date: 2026-09-08
description: วิธีลดขนาดโมเดล 3d โดยการสร้างเมชทรงกลมใน Java และบีบอัดด้วย Google Draco
  ผ่าน Aspose.3D. เรียนรู้ขั้นตอนทั้งหมดในไม่กี่นาที.
keywords:
- how to reduce 3d model size
- aspose 3d java
- draco mesh compression
- java sphere mesh
- 3d model optimization
lastmod: 2026-09-08
linktitle: วิธีลดขนาดโมเดล 3d – สร้างเมชทรงกลมใน Java ด้วย Google Draco
og_description: วิธีลดขนาดโมเดล 3d โดยการสร้างเมชทรงกลมใน Java และบีบอัดด้วย Google
  Draco โดยใช้ Aspose.3D. ได้ไฟล์ .drc เล็กลงถึง 95% ในไม่กี่นาที.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: วิธีลดขนาดโมเดล 3d ด้วยเมชทรงกลมใน Java และ Draco
schemas:
- author: Aspose
  dateModified: '2026-09-08'
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

# วิธีลดขนาดโมเดล 3 มิติด้วยเมชทรงกลมใน Java และ Draco

## บทนำ

หากคุณกำลังมองหาวิธีที่เร็วในการ **ลดขนาดโมเดล 3 มิติ** ในขณะที่ยังคงให้คุณภาพเรขาคณิตสูง คุณมาถูกที่แล้ว ในบทเรียนนี้เราจะอธิบายขั้นตอนการสร้างเมชทรงกลมด้วย **Aspose.3D for Java** แล้วบีบอัดเมชนั้นด้วย **Google Draco** เมื่อเสร็จคุณจะได้ไฟล์ `.drc` ที่พร้อมใช้งานและมีขนาดเล็กกว่าต้นฉบับอย่างมาก ทำให้เหมาะสำหรับตัวดูบนเว็บ เกมมือถือ หรือแอปพลิเคชัน Java ที่มีข้อจำกัดด้านแบนด์วิดท์

## คำตอบอย่างรวดเร็ว
- **บทเรียนนี้ครอบคลุมอะไร?** การสร้างเมชทรงกลมใน Java และการบีบอัดด้วย Google Draco ผ่าน Aspose.3D.  
- **ไลบรารีหลัก?** Aspose.3D for Java (ใช้สำหรับสร้างเมชและส่งออก Draco).  
- **เวลาในการทำงานโดยประมาณ?** ประมาณ 10‑15 นาทีสำหรับทรงกลมพื้นฐาน.  
- **ข้อกำหนดสำคัญ?** สภาพแวดล้อมการพัฒนา Java ที่มี JAR ของ Aspose.3D อยู่ใน classpath.  
- **ผลลัพธ์?** ไฟล์ `.drc` ที่ **ลดขนาดโมเดล 3 มิติ** ได้ถึง 95 % เมื่อเทียบกับเมชที่ไม่ได้บีบอัด.

## วิธีลดขนาดโมเดล 3 มิติ?

คลาส `Sphere` สร้างเรขาคณิตทรงกลมที่ทำเป็นสามเหลี่ยมตามพารามิเตอร์รัศมีและการตัดแบ่งที่กำหนด โหลดทรงกลมของคุณด้วย `new Sphere(1.0, 32, 32)` แล้วส่งออกโดยตรงเป็น Draco ด้วย `scene.save("sphere.drc", SaveFormat.Draco)` เมธอด `scene.save` จะเขียนฉากปัจจุบันลงไฟล์ในรูปแบบที่ระบุ Aspose.3D จะจัดการการแปลงภายใน ดังนั้นคุณจึงหลีกเลี่ยงขั้นตอนการเข้ารหัสด้วยตนเอง ตัวส่งออก Draco จะทำการควอนติไทซ์เรขาคณิตและกำจัดจุดซ้ำโดยอัตโนมัติ ทำให้ไฟล์มักเล็กลง 80‑95 % ในขณะที่ยังคงรักษาความละเอียดภาพ

## “การลดขนาดโมเดล 3 มิติ” หมายถึงอะไรในบริบทของการพัฒนา 3 มิติ?

**การลดขนาดโมเดล 3 มิติ** หมายถึงการทำให้ข้อมูลเรขาคณิตที่ต้องส่งหรือเก็บมีปริมาณน้อยลงโดยไม่ทำให้คุณภาพภาพลดลงอย่างเห็นได้ชัด Draco ทำเช่นนี้โดยการเข้ารหัสตำแหน่งเวอร์เท็กซ์, ปกติ, และแอตทริบิวต์อื่น ๆ ในรูปแบบไบนารีที่กะทัดรัดอย่างสูง เมื่อใช้ร่วมกับ Aspose.3D กระบวนการทั้งหมดอยู่ภายใน Java ทำให้คุณไม่ต้องจัดการกับไบนารีเนทีฟของ Draco

## ทำไมต้องใช้การบีบอัดเมช Google Draco กับ Aspose.3D?

Google Draco ร่วมกับ Aspose.3D ให้ไพพ์ไลน์ที่มีประสิทธิภาพซึ่งลดขนาดไฟล์เมชอย่างมหาศาลในขณะที่ยังคงง่ายต่อการรวมเข้ากับโปรเจกต์ Java ไลบรารีจัดการการเข้ารหัสระดับล่างทั้งหมด ทำให้นักพัฒนามุ่งเน้นที่การสร้างเรขาคณิตโดยไม่ต้องกังวลกับไบนารีเนทีฟของ Draco ส่งผลให้การพัฒนาเร็วขึ้นและสินทรัพย์มีขนาดเล็กลงสำหรับเว็บและมือถือ

- **การลดขนาดอย่างมหาศาล:** Draco สามารถลดข้อมูลเมชได้ถึง 95 % สำหรับโมเดลทั่วไป ทำให้ไฟล์ OBJ ขนาด 5 MB ลดลงเป็น `.drc` ขนาด 0.3 MB.  
- **การถอดรหัสเร็วในรันไทม์:** เอนจินเช่น Unity, Unreal, และ three.js ถอดรหัส Draco ได้โดยเนทีฟ ทำให้เวลาโหลดเร็วขึ้น.  
- **การบูรณาการกับ Java อย่างไร้รอยต่อ:** Aspose.3D แอบซ้อนไลบรารี Draco เนทีฟ ทำให้คุณอยู่ในระบบนิเวศ Java ทั้งหมด.  
- **การส่งออก Aspose 3D ครบวงจร:** API เดียวที่ใช้สร้างเรขาคณิตยังสามารถส่งออกได้ ทำให้ไพพ์ไลน์ง่ายขึ้น.

## ข้อกำหนดเบื้องต้น

- **Java Development Kit (JDK)** – เวอร์ชัน 8 หรือใหม่กว่า.  
- **Aspose.3D for Java** – ดาวน์โหลด JAR ล่าสุดจาก **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)**.  
- **ความคุ้นเคยพื้นฐานกับ Google Draco** – คุณจะใช้ wrapper ของ Aspose.3D ดังนั้นไม่จำเป็นต้องตั้งค่า Draco เนทีฟ.

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

สร้างโปรเจกต์ Java ใหม่ (IDE ใดก็ได้) แล้วเพิ่ม JAR ของ Aspose.3D ทั้งหมดลงใน classpath เก็บไฟล์ซอร์สของคุณในแพ็กเกจเช่น `com.example.draco` เพื่อความชัดเจน.

### ขั้นตอนที่ 2: วิธีสร้างเมชทรงกลมใน Java

คลาส `Sphere` เป็นตัวสร้างเรขาคณิตในตัวของ Aspose.3D ที่ผลิตเมชสามเหลี่ยมที่สามารถกำหนดรัศมีและการตัดแบ่งได้  

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

> **เคล็ดลับ:** คลาส `Sphere` สร้างเมชสามเหลี่ยมโดยมีรัศมีเริ่มต้นที่ 1.0 คุณสามารถส่งค่ารัศมี, การตัดแบ่ง, หรือพารามิเตอร์วัสดุที่กำหนดเองได้หากต้องการระดับรายละเอียดที่ต่างกันก่อนการบีบอัด.

### ขั้นตอนที่ 3: ส่งออกเมชเป็นรูปแบบ Draco

หลังจากเพิ่มทรงกลมลงในอ็อบเจกต์ `Scene` ให้เรียก `scene.save("sphere.drc", SaveFormat.Draco)` Aspose.3D จะเลือกการตั้งค่าบีบอัดที่เหมาะสมโดยอัตโนมัติ แต่คุณสามารถปรับให้ละเอียดโดยตั้งค่า `DracoCompressionOptions` หากต้องการไฟล์ที่เล็กที่สุดเท่าที่จะเป็นไปได้ `DracoCompressionOptions` ให้คุณกำหนดการตั้งค่าบีบอัดของ Draco เช่น การควอนติไทซ์และระดับการบีบอัด.

### ขั้นตอนที่ 4: ตรวจสอบผลลัพธ์

เปิดไฟล์ `.drc` ที่สร้างขึ้นด้วยตัวดู Draco (เช่น three.js `DRACOLoader`) เพื่อให้แน่ใจว่าเรขาคณิตแสดงผลอย่างถูกต้อง คุณจะสังเกตเห็นการลดขนาดไฟล์อย่างชัดเจน—มักเป็นระดับสิบเท่าหรือมากกว่า.

## กรณีการใช้งานทั่วไป

| สถานการณ์ | ทำไมต้องลดขนาดโมเดล? | วิธีที่บทเรียนนี้ช่วยได้ |
|----------|-----------------------|--------------------------|
| ตัวกำหนดผลิตภัณฑ์บนเว็บ | โหลดหน้าเร็วขึ้นบนการเชื่อมต่อช้า | ไฟล์ `.drc` ที่บีบอัดด้วย Draco โหลดได้ในไม่กี่วินาที |
| แอป AR/VR บนมือถือ | ลดการใช้หน่วยความจำบนอุปกรณ์ | เมชขนาดเล็กทำให้แอปตอบสนองได้ดี |
| ฉากที่เรนเดอร์บนคลาวด์ | ลดค่าแบนด์วิดท์ | ส่งออกด้วยคลิกเดียวจาก Aspose.3D ไปยัง Draco |

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | JAR ของ Aspose.3D ไม่อยู่ใน classpath | ตรวจสอบให้แน่ใจว่า *ทั้งหมด* ไฟล์ JAR ของ Aspose.3D ถูกใส่และเวอร์ชันตรงกับเอกสาร |
| **ไฟล์ผลลัพธ์เป็นไฟล์ว่าง** | `MyDir` ชี้ไปยังโฟลเดอร์ที่ไม่มีอยู่ | สร้างโฟลเดอร์โดยโปรแกรม (`Files.createDirectories(Paths.get(MyDir))`) ก่อนเขียนไฟล์ |
| **เมชที่บีบอัดดูบิดเบือน** | ใช้ระดับบีบอัดต่ำหรือการตัดแบ่งไม่เพียงพอ | เปลี่ยนเป็น `DracoCompressionLevel.OPTIMAL` และเพิ่มการตัดแบ่งของทรงกลม (เช่น `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` เลือกคุณภาพบีบอัดสูงสุดสำหรับผลลัพธ์ Draco |

## คำถามที่พบบ่อย

**Q: Aspose.3D รองรับรูปแบบไฟล์ 3 มิติที่ต่างกันหรือไม่?**  
A: ใช่, Aspose.3D รองรับ OBJ, FBX, STL, GLTF และรูปแบบอื่น ๆ มากมาย ทำให้เป็นตัวเลือกที่หลากหลายสำหรับ **Aspose 3d export** pipelines.

**Q: ฉันสามารถใช้ Google Draco สำหรับการบีบอัดในภาษาโปรแกรมอื่นได้หรือไม่?**  
A: แน่นอน. Draco มีไลบรารีเนทีฟสำหรับ C++, Python, และ JavaScript บทเรียนนี้เน้นที่ Java แต่แนวคิดสามารถนำไปใช้กับภาษาอื่นได้.

**Q: ฉันจะหาเอกสารเพิ่มเติมของ Aspose.3D ได้จากที่ไหน?**  
A: เยี่ยมชม **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** เพื่อดูอ้างอิง API อย่างเต็มและตัวอย่างเพิ่มเติม.

**Q: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?**  
A: สำรวจตัวเลือกใบอนุญาตชั่วคราวได้ที่ **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**.

**Q: มีฟอรั่มชุมชนสำหรับการสนับสนุน Aspose.3D หรือไม่?**  
A: มี, เข้าร่วมการสนทนาที่ **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.

## สรุป

ในคู่มือนี้เราได้สาธิตวิธี **ลดขนาดโมเดล 3 มิติ** ด้วยการสร้างเมชทรงกลมใน Java แล้วบีบอัดด้วย Google Draco ผ่าน Aspose.3D โดยทำตามขั้นตอนสั้น ๆ นี้ คุณสามารถลดขนาดไฟล์เมชได้อย่างมหาศาล ปรับปรุงเวลาโหลด และทำให้แอปพลิเคชัน 3 มิติที่ใช้ Java ของคุณตอบสนองได้ดีและใช้แบนด์วิดท์น้อยลง

---

**Last Updated:** 2026-09-08  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

## บทเรียนที่เกี่ยวข้อง

- [ลดขนาดไฟล์ 3D – บีบอัดฉากด้วย Aspose.3D สำหรับ Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [สร้างคลาวด์จุด Draco จากทรงกลมโดยใช้ Aspose.3D สำหรับ Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [เรียนรู้วิธีทำให้เมชเป็นรูปสามเหลี่ยมเพื่อการเรนเดอร์ที่เพิ่มประสิทธิภาพใน Java ด้วย Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}