---
date: 2026-05-24
description: เรียนรู้วิธีการ Extrude รูปร่างโดยใช้ Aspose.3D for Java. บทเรียนการสร้างโมเดล
  3D ด้วย Java นี้ครอบคลุม Linear Extrusion, การควบคุมศูนย์กลาง, ทิศทาง, สไลซ์, การบิดและอื่น
  ๆ อีกมาก!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: สร้างโมเดล 3D ด้วย Linear Extrusion ใน Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: วิธีการ Extrude รูปร่าง - สร้างโมเดล 3D ด้วย Linear Extrusion ใน Java
url: /th/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีการดึงรูปทรง – การสร้างโมเดล 3 มิติด้วยการดึงเชิงเส้นใน Java

หากคุณเคยสงสัย **how to extrude shape** ในแอปพลิเคชัน Java คุณมาถูกที่แล้ว ในบทแนะนำนี้เราจะพาคุณผ่านคุณลักษณะการดึงเชิงเส้นของ Aspose.3D for Java แสดงวิธีการเปลี่ยนโปรไฟล์ 2‑D ง่าย ๆ ให้กลายเป็นโมเดล 3‑D ที่สมบูรณ์ ไม่ว่าคุณกำลังสร้างตัวดูแบบ CAD, สายงานสินทรัพย์เกม, หรือเพียงทดลองกับรูปทรง การเชี่ยวชาญการดึงเชิงเส้นจะทำให้คุณมั่นใจในการสร้างรูปทรงซับซ้อนด้วยโค้ดเพียงไม่กี่บรรทัด

## คำตอบอย่างรวดเร็ว
- **What is linear extrusion?** การแปลงสเก็ตช์ 2‑D ให้เป็นของแข็ง 3‑D โดยการขยายตามทิศทาง  
- **ไลบรารีใดที่ช่วยคุณ?** Aspose.3D for Java provides a fluent API for extrusion tasks.  
- **ต้องการไลเซนส์หรือไม่?** การทดลองใช้ฟรีทำงานสำหรับการเรียนรู้; จำเป็นต้องมีไลเซนส์เชิงพาณิชย์สำหรับการผลิต  
- **ต้องการเวอร์ชัน Java ใด?** Java 8 หรือสูงกว่า  
- **สามารถใช้การบิดหรือการชิดออฟเซ็ตได้หรือไม่?** ใช่ – API รองรับ twist angle และ twist offset โดยอัตโนมัติ  

## “how to extrude shape” คืออะไรใน Java?
การดำเนินการ `Extrusion` เป็นฟีเจอร์หลักของ Aspose.3D ที่แปลงคอนทัวร์แบนให้เป็นเมชปริมาณ. อย่างง่าย คุณให้โปรไฟล์ 2‑D (เช่น สี่เหลี่ยมหรือโพลิกอนที่กำหนดเอง) แล้วบอกเอนจินว่าต้องดึงไกลแค่ไหน และไลบรารีจะสร้างเรขาคณิต 3‑D ให้คุณ

## ทำไมต้องใช้ Aspose.3D for Java?
Aspose.3D รองรับ **50+ รูปแบบการนำเข้าและส่งออก** – รวมถึง OBJ, STL, FBX, และ GLTF – และสามารถสร้างเมชได้สูงสุด **10 000 vertices per extrusion** โดยไม่ต้องโหลดฉากทั้งหมดเข้าสู่หน่วยความจำ. เครื่องยนต์ข้ามแพลตฟอร์มทำงานบน Windows, Linux, และ macOS, ให้ผลลัพธ์ที่สม่ำเสมอไม่ว่าคุณจะอยู่บนเวิร์กสเตชันเดสก์ท็อปหรือเซิร์ฟเวอร์ CI แบบไม่มีหัว

## ข้อกำหนดเบื้องต้น
- Java 8 หรือใหม่กว่า ติดตั้งบนเครื่องพัฒนาของคุณ  
- Maven หรือ Gradle สำหรับการจัดการ dependencies  
- ไฟล์ไลเซนส์ Aspose.3D for Java (ไม่บังคับสำหรับการทดลอง)  

## การทำงานของการดึงเชิงเส้นเป็นอย่างไร?
การดึงเชิงเส้นสร้างของแข็ง 3‑D โดยการสวีปโปรไฟล์ 2‑D ไปตามเส้นตรง. เอนจินจะทำการไตรแองเกิลโปรไฟล์ก่อน, จากนั้นทำสำเนาที่แต่ละสไลซ์ตามแกนการดึง, สุดท้ายเชื่อมสไลซ์เข้าด้วยกันเพื่อสร้างเมชที่แน่นหนา. กระบวนการนี้คำนวณ normal และพิกัด UV อัตโนมัติ, ทำให้คุณสามารถเรนเดอร์ผลลัพธ์ได้โดยไม่ต้องประมวลผลเรขาคณิตเพิ่มเติม

## พารามิเตอร์สำคัญของการดึงเชิงเส้นคืออะไร?
การดึงเชิงเส้นสามารถปรับแต่งได้ด้วยพารามิเตอร์หลายตัว. **center** กำหนดจุดศูนย์กลางของโปรไฟล์ก่อนการดึง. **direction** เวกเตอร์กำหนดแกนการดึง, ค่าเริ่มต้นคือแกน Z บวก. **Slices** ควบคุมจำนวนหน้าตัดกลางที่สร้าง, มีผลต่อความเรียบของรูปบิดหรือแคบ. **Twist angle** หมุนโปรไฟล์อย่างต่อเนื่องจากเริ่มถึงจบ, **twist offset** เพิ่มการเคลื่อนที่เชิงเส้นตามแกน, ทำให้เกิดรูปสไปรัล

- **Center** – จุดศูนย์กลางที่โปรไฟล์ตั้งอยู่ก่อนการดึง  
- **Direction** – เวกเตอร์ที่กำหนดแกนการดึง; ค่าเริ่มต้นคือแกน Z บวก  
- **Slices** – จำนวนหน้าตัดกลาง; จำนวนมากขึ้นให้การเปลี่ยนแปลงที่เรียบเนียนยิ่งขึ้นสำหรับการดึงที่บิดหรือแคบ  
- **Twist Angle** – การหมุนรวมที่ใช้กับโปรไฟล์จากเริ่มถึงจบ, แสดงเป็นองศา  
- **Twist Offset** – การชิดออฟเซ็ตเชิงเส้นที่ย้ายโปรไฟล์ตามแกนการดึงขณะบิด, ทำให้เกิดรูปสไปรัล  

## การทำ Linear Extrusion ใน Aspose.3D for Java
โหลดโปรไฟล์ของคุณ, ตั้งค่าพารามิเตอร์, แล้วให้ API สร้างเมช. ขั้นตอนต่อไปนี้สรุปขั้นตอนการทำงานทั่วไป

### ขั้นตอนที่ 1: กำหนดโปรไฟล์ 2‑D
สร้าง `Polygon` หรือ `Polyline` ที่แสดงรูปทรงที่คุณต้องการดึง.  
*`Polygon` แสดงรูปแบบปิดที่กำหนดโดยจุดยอด, ส่วน `Polyline` เป็นชุดเส้นเปิด.*  
พร้อมเริ่มหรือยัง? [ทำ Linear Extrusion ตอนนี้](./performing-linear-extrusion/)  
สำหรับบทแนะนำโดยละเอียด, ดูที่ [ทำ Linear Extrusion ใน Aspose.3D for Java](./performing-linear-extrusion/).

### ขั้นตอนที่ 2: ตั้งค่าตัวเลือกการดึง
ตั้งค่า center, direction, slices, twist, และ twist offset บนวัตถุ `Extrusion`.  
*คลาส `Extrusion` รวมพารามิเตอร์ทั้งหมดที่จำเป็นสำหรับการสร้างเมช 3‑D จากโปรไฟล์ 2‑D.*  
ลองควบคุม center: [ควบคุม Center ใน Linear Extrusion](./controlling-center/)  
อ่านเพิ่มเติมเกี่ยวกับการควบคุม center: [การควบคุม Center ใน Linear Extrusion ด้วย Aspose.3D for Java](./controlling-center/)

### ขั้นตอนที่ 3: เพิ่มการดึงเข้าไปใน Scene
สร้างอินสแตนซ์ของ `Scene`, แนบเมชการดึง, และส่งออกเป็นฟอร์แมตที่ต้องการ.  
*`Scene` เป็นคอนเทนเนอร์ที่เก็บวัตถุ 3‑D ทั้งหมดและจัดการการส่งออกเป็นไฟล์หลายรูปแบบ.*  
พร้อมตั้ง direction หรือยัง? [สำรวจตอนนี้](./setting-direction/)  
เรียนรู้เพิ่มเติมเกี่ยวกับ direction: [การตั้ง Direction ใน Linear Extrusion ด้วย Aspose.3D for Java](./setting-direction/)

### ขั้นตอนที่ 4: ส่งออกหรือเรนเดอร์
ใช้ `Scene.save()` เพื่อบันทึกโมเดลเป็น OBJ, STL, หรือฟอร์แมตที่รองรับอื่น ๆ.  
*`Scene.save()` เขียนฉากทั้งหมดไปยังฟอร์แมตไฟล์ที่ระบุ, พร้อมทำ post‑processing ที่จำเป็น.*  
เริ่มกำหนด slices: [เรียนรู้เพิ่มเติม](./specifying-slices/)  
คู่มือโดยละเอียด: [การกำหนด Slices ใน Linear Extrusion ด้วย Aspose.3D for Java](./specifying-slices/)

## วิธีการใช้ twist กับการดึง?
ใช้ twist โดยตั้งค่าคุณสมบัติ `twistAngle` ในตัวเลือกการดึง. เอนจินจะหมุนแต่ละสไลซ์ตามสัดส่วน, สร้างเอฟเฟกต์เกลียว. การปรับมุมสามารถสร้างได้ตั้งแต่การบิดเล็กน้อยจนถึงเกลียว 360° เต็มรูปแบบ, มีประโยชน์สำหรับองค์ประกอบตกแต่งหรือสปริงทำงาน.  
พร้อมบิดหรือยัง? [Apply Twist Now](./applying-twist/)  
ตัวอย่างเต็ม: [Applying Twist in Linear Extrusion with Aspose.3D for Java](./applying-twist/)

## วิธีการใช้ twist offset สำหรับรูปสไปรัล?
twist offset ย้ายแต่ละสไลซ์ตามแกนการดึงขณะหมุน, สร้างบันไดสไปรัลหรือรูปทรงคอร์กสกรูว์. การรวม twist angle กับออฟเซ็ตบวกให้ทางลาดเกลียวเรียบ, ส่วนออฟเซ็ตลบสามารถสร้างสไปรัลลง. เทคนิคนี้เหมาะสำหรับการสร้างเธรด, สปริง, หรือริบบิ้นศิลปะ.  
พัฒนาทักษะของคุณ: [Learn Twist Offset](./using-twist-offset/)  
คู่มือครบถ้วน: [Using Twist Offset in Linear Extrusion with Aspose.3D for Java](./using-twist-offset/)

## กรณีการใช้งานทั่วไปของ Linear Extrusion
- **Mechanical parts** – สร้างบอ๊ต, แกน, และบรากเก็ตอย่างรวดเร็วจากสเก็ตช์ง่าย  
- **Architectural elements** – ดึงแผนผังชั้นเป็นผนังหรือคอลัมน์สำหรับต้นแบบ BIM  
- **Game assets** – สร้างพร็อพ low‑poly เช่น รั้ว, ท่อ, หรือราวตกแต่งโดยตรงจากศิลปะ 2‑D  
- **Educational tools** – แสดงพื้นผิวคณิตศาสตร์โดยการดึงเส้นโค้งพารามิเตอร์  

## การแก้ไขปัญหาทั่วไป
- **Missing faces** – ตรวจสอบว่าโปรไฟล์เป็นลูปปิด; คอนทัวร์เปิดจะทำให้เกิดช่องว่าง  
- **Excessive memory usage** – ลดจำนวน `slices` หรือเปิดใช้งาน `scene.setMemoryOptimization(true)`  
- **Incorrect twist direction** – มุมบวกหมุนตามเข็มนาฬิกาเมื่อมองตามทิศทางการดึง; ใช้มุมลบเพื่อย้อนกลับ  

## คำถามที่พบบ่อย

**Q: สามารถใช้ Aspose.3D for Java ในโครงการเชิงพาณิชย์ได้หรือไม่?**  
A: ใช่, จำเป็นต้องมีไลเซนส์ Aspose ที่ถูกต้องสำหรับการใช้งานในผลิตภัณฑ์, แต่สามารถใช้การทดลองฟรีเพื่อประเมินได้  

**Q: ไลบรารีรองรับเวอร์ชัน Java ใด?**  
A: ไลบรารีทำงานกับ Java 8 และรันไทม์ที่ใหม่กว่า, รวมถึง Java 11, 17, และ 21  

**Q: ต้องจัดการหน่วยความจำสำหรับการดึงขนาดใหญ่หรือไม่?**  
A: Aspose.3D จัดการการสร้างเมชอย่างมีประสิทธิภาพ, แต่คุณสามารถเรียก `scene.dispose()` เมื่อเสร็จสิ้นกับฉากขนาดใหญ่เพื่อปล่อยทรัพยากรเนทีฟ  

**Q: สามารถรวมหลายการดึงในโมเดลเดียวได้หรือไม่?**  
A: แน่นอน – คุณสามารถสร้างวัตถุ extrusion หลายอัน, กำหนดตำแหน่งอิสระกัน, แล้วเพิ่มลงใน Scene เดียว  

**Q: มีตัวอย่างโค้ดสำหรับการใช้ twist และ twist offset พร้อมกันหรือไม่?**  
A: มี, บทแนะนำ “Applying Twist” และ “Using Twist Offset” แสดงวิธีตั้งค่าทั้งสองคุณสมบัติบนวัตถุ extrusion เดียว  

**Last Updated:** 2026-05-24  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< blocks/products/products-backtop-button >}}

## บทแนะนำที่เกี่ยวข้อง

- [Java 3D Graphics Tutorial – Center in Linear Extrusion](/3d/java/linear-extrusion/controlling-center/)
- [How to Set Direction in Linear Extrusion with Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Create 3D Extrusion with Slices – Aspose.3D for Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}