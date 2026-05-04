---
date: 2026-05-04
description: เรียนรู้วิธีแยกเมชอย่างมีประสิทธิภาพตามวัสดุใน Java ด้วย Aspose.3D คู่มือนี้จะแสดงให้คุณเห็นวิธีลดการเรียกวาดและปรับปรุงประสิทธิภาพการเรนเดอร์ขณะแยกเมชตามวัสดุ.
keywords:
- how to split mesh
- reduce draw calls
- improve rendering performance
- split mesh by material
linktitle: วิธีแยกเมชตามวัสดุใน Java โดยใช้ Aspose.3D
second_title: Aspose.3D Java API
title: วิธีแยกเมชตามวัสดุใน Java ด้วย Aspose.3D
url: /th/java/3d-mesh-data/split-meshes-by-material/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# วิธีแยก Mesh ตามวัสดุใน Java ด้วย Aspose.3D

## บทนำ

หากคุณทำงานกับกราฟิก 3 มิติใน Java คุณจะพบว่า การประมวลผลเมชขนาดใหญ่สามารถเป็นคอขวดด้านประสิทธิภาพได้อย่างรวดเร็ว—โดยเฉพาะเมื่อเมชเดียวมีหลายวัสดุ **การเรียนรู้วิธีแยกเมช** ตามวัสดุช่วยให้คุณแยกกลุ่มโพลิกอนที่เฉพาะเจาะจงต่อวัสดุออกมา ทำให้การเรนเดอร์เร็วขึ้น การคัลลิงง่ายขึ้น และการควบคุมการจัดการเทกซ์เจอร์ละเอียดมากขึ้น ในบทแนะนำนี้เราจะอธิบายขั้นตอนที่แน่นอนเพื่อ **แยกเมชตามวัสดุ** ด้วยไลบรารี Aspose.3D พร้อมคำอธิบายเชิงปฏิบัติ เคล็ดลับการลด draw calls และคำแนะนำในการปรับปรุงประสิทธิภาพการเรนเดอร์

## คำตอบอย่างรวดเร็ว
- **“split mesh by material” หมายความว่าอะไร?** มันจะแยกเมชเดียวออกเป็นหลาย sub‑meshes โดยแต่ละอันจะมีโพลิกอนที่ใช้วัสดุเดียวกัน  
- **ทำไมต้องใช้ Aspose.3D?** มันให้ API ระดับสูงแบบข้ามแพลตฟอร์มที่แยกรายละเอียดไฟล์ระดับต่ำออกไปในขณะที่ยังคงประสิทธิภาพ  
- **การทำงานนี้ใช้เวลานานเท่าไหร่?** ประมาณ 10–15 นาทีของการเขียนโค้ดและทดสอบ  
- **ฉันต้องการไลเซนส์หรือไม่?** มีรุ่นทดลองฟรี; จำเป็นต้องมีไลเซนส์เชิงพาณิชย์สำหรับการใช้งานในผลิตภัณฑ์  
- **รองรับเวอร์ชัน Java ใด?** Java 8 หรือสูงกว่า  

## วิธีแยก Mesh ตามวัสดุ – ภาพรวม
การแยกเมชตามวัสดุเป็นกระบวนการสองขั้นตอน: ขั้นแรกคุณทำเครื่องหมายแต่ละโพลิกอนด้วยดัชนีวัสดุ แล้วคุณสั่งให้ Aspose.3D แยกเมชตามดัชนีนั้น ผลลัพธ์คือคอลเลกชันของเมชขนาดเล็กกว่าแต่ละเมชสามารถเรนเดอร์ด้วย draw call เดียว—เหมาะอย่างยิ่งสำหรับ **การลด draw calls** และ **การปรับปรุงประสิทธิภาพการเรนเดอร์** บน GPU ทั้งแบบเดสก์ท็อปและมือถือ

## Mesh Splitting คืออะไร?
Mesh Splitting คือกระบวนการแบ่งเมช 3 มิติที่ซับซ้อนออกเป็นชิ้นส่วนเล็ก ๆ ที่จัดการได้ง่ายขึ้น เมื่อการแยกทำบนพื้นฐานของวัสดุ แต่ละ sub‑mesh ที่ได้จะมีโพลิกอนที่อ้างอิงวัสดุเดียวเท่านั้น วิธีนี้ช่วยลด draw calls, ปรับปรุงประสิทธิภาพการเรนเดอร์, และทำให้การใช้เชดเดอร์ต่อวัสดุง่ายขึ้น

## ทำไมต้องแยก Mesh ตามวัสดุ?
- **ประสิทธิภาพ:** เอนจินการเรนเดอร์สามารถทำ batch draw calls ต่อวัสดุ ลดการเปลี่ยนแปลงสถานะของ GPU  
- **ความยืดหยุ่น:** คุณสามารถใช้เอฟเฟกต์ post‑processing หรือตรรกะการชนต่าง ๆ ต่อวัสดุได้  
- **การจัดการหน่วยความจำ:** Mesh ที่เล็กลงง่ายต่อการสตรีมเข้าและออกจากหน่วยความจำ ซึ่งสำคัญสำหรับแอปพลิเคชันมือถือหรือ VR  
- **ลด Draw Calls:** การเปลี่ยนแปลงสถานะน้อยลงทำให้ GPU ประมวลผลเฟรมได้อย่างมีประสิทธิภาพมากขึ้น  
- **ปรับปรุงประสิทธิภาพการเรนเดอร์:** การแยกวัสดุมักทำให้การคัลลิงและการเชดดิ้งดีขึ้น  

## กรณีการใช้งานทั่วไป

| สถานการณ์ | ประโยชน์ของการแยก |
|-----------|-------------------|
| **Real‑time strategy games** | แต่ละประเภทของพื้นดินสามารถมีวัสดุของตนเอง ทำให้เอนจินสามารถวาดทุกส่วนของหญ้าในหนึ่งครั้ง |
| **Architectural visualization** | ผนัง, แก้ว, และโลหะสามารถจัดการแยกกันเพื่อเอฟเฟกต์เชดเดอร์ที่แตกต่าง |
| **Mobile AR apps** | การลด draw calls ช่วยรักษา 60 fps บนอุปกรณ์ที่มีทรัพยากรจำกัด |
| **VR experiences** | ภาระงานของ GPU ที่น้อยลงลดความหน่วงเวลา ทำให้ผู้ใช้สบายตา |

## ข้อกำหนดเบื้องต้น

ก่อนจะลงมือเขียนโค้ด ให้ตรวจสอบว่าคุณมีสิ่งต่อไปนี้พร้อม:

- ความรู้พื้นฐานของการเขียนโปรแกรม Java  
- ไลบรารี Aspose.3D for Java ติดตั้งแล้ว (ดาวน์โหลดจาก [Aspose website](https://releases.aspose.com/3d/java/))  
- IDE เช่น IntelliJ IDEA, Eclipse หรือ VS Code ที่ตั้งค่าเพื่อการพัฒนา Java  

## นำเข้าแพ็กเกจ

เริ่มต้นโดยนำเข้าคลาส Aspose.3D ที่จำเป็นและยูทิลิตี้มาตรฐานของ Java ที่คุณต้องการใช้:

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

## คู่มือแบบขั้นตอน

ต่อไปนี้เป็นการอธิบายสั้น ๆ ของแต่ละขั้นตอน พร้อมคำอธิบายก่อนโค้ดเพื่อให้คุณเข้าใจว่ากำลังทำอะไร

### ขั้นตอนที่ 1: สร้าง Mesh ของกล่อง

เราจะเริ่มด้วย primitive แบบง่าย ๆ — กล่อง — เพื่อให้เห็นชัดว่าแต่ละหน้า (plane) จะได้รับวัสดุของตนเองอย่างไร

```java
// ExStart:SplitMeshbyMaterial

// Create a mesh of a box (composed of 6 planes)
Mesh box = (new Box()).toMesh();
```

### ขั้นตอนที่ 2: สร้าง Material Element

`VertexElementMaterial` จะเก็บดัชนีวัสดุสำหรับแต่ละโพลิกอน การแนบมันเข้ากับเมชทำให้เราควบคุมได้ว่าแต่ละหน้าใช้วัสดุอะไร

```java
// Create a material element on the box mesh
VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
```

### ขั้นตอนที่ 3: ระบุ Material Index ที่แตกต่างกัน

ที่นี่เรากำหนดดัชนีวัสดุที่ไม่ซ้ำกันให้กับแต่ละหน้า 6 หน้า ของกล่อง ลำดับของอาเรย์สอดคล้องกับลำดับของโพลิกอนที่สร้างโดย primitive `Box`

```java
// Specify different material indices for each plane
mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
```

### ขั้นตอนที่ 4: แยก Mesh เป็น Sub‑Meshes

การเรียก `PolygonModifier.splitMesh` พร้อม `SplitMeshPolicy.CLONE_DATA` จะสร้าง sub‑mesh ใหม่สำหรับแต่ละดัชนีวัสดุที่แตกต่างกันโดยคงข้อมูลเวอร์เท็กซ์เดิมไว้

```java
// Split the mesh into 6 sub-meshes, each plane becoming a sub-mesh
Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
```

### ขั้นตอนที่ 5: อัปเดต Material Index และแยกอีกครั้ง

เพื่อสาธิตกลยุทธ์การแยกแบบอื่น เราจะรวมหน้าแรกสามหน้าไว้ภายใต้วัสดุ 0 และอีกสามหน้าไว้ภายใต้วัสดุ 1 แล้วแยกด้วย `COMPACT_DATA` เพื่อลบเวอร์เท็กซ์ที่ไม่ได้ใช้

```java
// Update material indices and split into 2 sub-meshes
mat.getIndices().clear();
mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
```

### ขั้นตอนที่ 6: ยืนยันความสำเร็จ

ข้อความคอนโซลง่าย ๆ จะบอกคุณว่าการดำเนินการเสร็จสมบูรณ์โดยไม่มีข้อผิดพลาด

```java
// Display success message
System.out.println("\nSplitting a mesh by specifying the material successfully.");
// ExEnd:SplitMeshbyMaterial
```

## ลด Draw Calls และปรับปรุงประสิทธิภาพการเรนเดอร์

เมื่อทำให้แต่ละวัสดุกลายเป็นเมชของตนเอง คุณทำให้กราฟิกพายป์ไลน์สามารถส่ง draw call เดียวต่อวัสดุแทนที่จะเป็นหนึ่งต่อหนึ่งโพลิกอน การลด draw calls นี้จะทำให้เฟรมเรตราบรื่นขึ้นโดยเฉพาะบนฮาร์ดแวร์ระดับล่าง นอกจากนี้นโยบาย `COMPACT_DATA` ยังลบเวอร์เท็กซ์ที่ไม่ได้ใช้ ลดแบนด์วิธของหน่วยความจำและช่วยให้ GPU เรนเดอร์ได้อย่างมีประสิทธิภาพยิ่งขึ้น

## ปัญหาทั่วไปและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|--------|
| **Sub‑meshes contain duplicate vertices** | การใช้ `CLONE_DATA` คัดลอกข้อมูลเวอร์เท็กซ์ทั้งหมดสำหรับแต่ละ sub‑mesh | เปลี่ยนเป็น `COMPACT_DATA` เมื่อคุณต้องการให้เวอร์เท็กซ์ที่ใช้ร่วมกันถูกลบซ้ำ |
| **Incorrect material assignment** | อาร์เรย์ของดัชนีมีความยาวไม่ตรงกับจำนวนโพลิกอน | ตรวจสอบจำนวนโพลิกอน (เช่น กล่องมี 6) และให้อาร์เรย์ดัชนีที่ตรงกัน |

## คำถามที่พบบ่อย

**Q:** **Is Aspose.3D compatible with other Java 3D libraries?**  
**A:** ใช่, Aspose.3D สามารถทำงานร่วมกับไลบรารีอื่น ๆ เช่น Java 3D หรือ jMonkeyEngine ทำให้คุณสามารถ import/export เมชระหว่างกันได้  

**Q:** **Can this technique be applied to complex models with hundreds of materials?**  
**A:** แน่นอน. การเรียก API เดียวกันทำงานได้ไม่ว่าความซับซ้อนของเมชจะเป็นเท่าใด; เพียงตรวจสอบให้แน่ใจว่าอาเรย์ดัชนีของคุณสะท้อนการจัดเรียงวัสดุอย่างถูกต้อง  

**Q:** **Where can I find the full Aspose.3D Java documentation?**  
**A:** เยี่ยมชม [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) อย่างเป็นทางการสำหรับอ้างอิง API รายละเอียดและตัวอย่างเพิ่มเติม  

**Q:** **Is a free trial available for Aspose.3D for Java?**  
**A:** มี, คุณสามารถดาวน์โหลดรุ่นทดลองจาก [Aspose Releases page](https://releases.aspose.com/)  

**Q:** **How can I get support if I run into issues?**  
**A:** ฟอรั่มชุมชนของ Aspose ([Aspose.3D forum](https://forum.aspose.com/c/3d/18)) เป็นสถานที่ที่ดีสำหรับถามคำถามและรับความช่วยเหลือจากทีม Aspose และนักพัฒนาคนอื่น ๆ  

## สรุป

คุณมีวิธีการครบถ้วนและพร้อมใช้งานสำหรับ **การแยก Mesh ตามวัสดุ** ด้วย Aspose.3D ใน Java แล้ว การนำเทคนิคนี้ไปใช้จะทำให้คุณลด draw calls, ใช้หน่วยความจำน้อยลง, และเรนเดอร์ได้ราบรื่นบนอุปกรณ์หลากหลาย อย่าลังเลที่จะทดลองใช้ตัวเลือก `SplitMeshPolicy` ต่าง ๆ หรือผสาน sub‑meshes ที่ได้เข้ากับ pipeline การเรนเดอร์ของคุณเอง

---

**อัปเดตล่าสุด:** 2026-05-04  
**ทดสอบด้วย:** Aspose.3D for Java 24.11  
**ผู้เขียน:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}