---
date: 2025-12-22
description: เรียนรู้วิธีการส่งออกฉากเป็น glTF ใน Java ด้วย Aspose.3D พร้อมอัปเกรดวัสดุ
  3D เป็น PBR เพื่อเพิ่มความสมจริง
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: ส่งออกฉากเป็น glTF ใน Java ด้วย Aspose.3D
url: /th/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ส่งออกฉากเป็น glTF ใน Java ด้วย Aspose.3D – ปรับปรุงวัสดุเป็น PBR

## บทนำ

ในบทเรียนนี้คุณจะได้เรียนรู้วิธี **export scene to glTF** ใน Java ด้วย Aspose.3D พร้อมกับการอัปเกรดวัสดุ 3D ของคุณให้เป็น Physically‑Based Rendering (PBR) การอัปเกรดเป็น PBR จะทำให้โมเดลของคุณดูสมจริงมากขึ้น และการส่งออกเป็นรูปแบบ glTF 2.0 ที่ได้รับการสนับสนุนอย่างกว้างขวาง จะช่วยให้คุณสามารถแชร์สินทรัพย์คุณภาพสูงเหล่านี้ไปยังเอนจิ้นต่าง ๆ, เบราว์เซอร์, และแพลตฟอร์ม AR/VR เราจะอธิบายขั้นตอนที่จำเป็น, นำเข้าแพ็กเกจที่ต้องใช้, และแยกย่อยแต่ละตัวอย่างอย่างเป็นขั้นตอนเพื่อให้คุณนำเทคนิคนี้ไปใช้ในโครงการของคุณเองได้

## คำตอบอย่างรวดเร็ว
- **“export scene to glTF” หมายถึงอะไร?** มันจะแปลงฉาก Aspose.3D ให้เป็นไฟล์รูปแบบ glTF 2.0 โดยคงไว้ซึ่งเรขาคณิต, วัสดุ, และโครงสร้างลำดับชั้น  
- **ทำไมต้องอัปเกรดวัสดุเป็น PBR ก่อน?** วัสดุ PBR ตรงกับกระบวนการทำงาน metallic‑roughness ของ glTF ทำให้แสงสว่างดูสมจริงโดยไม่ต้องทำขั้นตอนแปลงเพิ่มเติม  
- **ต้องมีลิขสิทธิ์เพื่อรันโค้ดหรือไม่?** สามารถใช้เวอร์ชันทดลองฟรีสำหรับการพัฒนา; ต้องมีลิขสิทธิ์เชิงพาณิชย์สำหรับการใช้งานในผลิตภัณฑ์จริง  
- **IDE ของ Java ที่รองรับมีอะไรบ้าง?** IDE ใดก็ได้ที่สามารถคอมไพล์ Java (Eclipse, IntelliJ IDEA, VS Code ฯลฯ)  
- **สามารถส่งออกฉากขนาดใหญ่ได้หรือไม่?** ได้, Aspose.3D จะสตรีมข้อมูลอย่างมีประสิทธิภาพ; เพียงตรวจสอบให้มีหน่วยความจำ heap เพียงพอสำหรับโมเดลขนาดใหญ่มาก

## “export scene to glTF” คืออะไร?
การส่งออกฉากเป็น glTF หมายถึงการทำให้ฉาก 3D ทั้งหมด—รวมถึงเมช, โหนด, กล้อง, แสง, และวัสดุ—ถูกจัดเก็บเป็นรูปแบบ GL Transmission Format (glTF) glTF เป็นรูปแบบมาตรฐานเปิดที่ได้รับการปรับให้เหมาะกับการเรนเดอร์แบบเรียลไทม์ ทำให้เหมาะสำหรับการใช้งานบนเว็บ, มือถือ, และเอนจิ้นเกม

## ทำไมต้องอัปเกรดวัสดุเป็น PBR ก่อนการส่งออก?
วัสดุ PBR (Physically‑Based Rendering) อธิบายการทำงานของแสงกับพื้นผิวโดยใช้พารามิเตอร์เช่น albedo, metallic, และ roughness glTF 2.0 รองรับ PBR โดยตรง ดังนั้นการแปลงวัสดุ Phong หรือวัสดุที่กำหนดเองเป็น PBR จะทำให้สี, การสะท้อน, และการเงาแสดงผลถูกต้องเมื่อโมเดลถูกโหลดในตัวดู glTF ใด ๆ

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มทำตามขั้นตอนต่อไปนี้ให้แน่ใจว่าคุณมี:

1. **Aspose.3D for Java** – ดาวน์โหลดจาก [release page](https://releases.aspose.com/3d/java/)  
2. **สภาพแวดล้อมการพัฒนา Java** – JDK 8 หรือสูงกว่าและ IDE ที่คุณเลือก  
3. **โฟลเดอร์เอกสาร** – โฟลเดอร์บนเครื่องของคุณที่ใช้สำหรับอ่าน/เขียนไฟล์ 3D

## นำเข้าแพ็กเกจ

เพิ่ม namespace หลักของ Aspose.3D ไปยังโปรเจกต์ของคุณ:

```java
import com.aspose.threed.*;
```

การนำเข้าครั้งเดียวนี้จะทำให้คุณเข้าถึง `Scene`, `Box`, `PhongMaterial`, `PbrMaterial`, `GltfSaveOptions` และ API การแปลงวัสดุได้ทั้งหมด

## ขั้นตอนที่ 1: สร้างฉาก 3D ใหม่

สร้างฉากใหม่ที่จะเก็บเรขาคณิตและวัสดุของคุณ:

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **เคล็ดลับ:** ให้ใช้ `MyDir` เป็นเส้นทางแบบ absolute ระหว่างการพัฒนาเพื่อหลีกเลี่ยงข้อผิดพลาดไฟล์ไม่พบ

## ขั้นตอนที่ 2: สร้างกล่องพร้อม PhongMaterial

เราจะเริ่มด้วยกล่องง่าย ๆ ที่ใช้วัสดุ Phong แบบคลาสสิก ซึ่งจะถูกแปลงเป็นวัสดุ PBR ระหว่างการส่งออก:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **ทำไมต้องใช้ Phong?** PhongMaterial ตั้งค่าได้ง่ายและแสดงให้เห็นว่าตรรกะการแปลงทำงานอย่างไร

## ขั้นตอนที่ 3: บันทึกเป็นรูปแบบ GLTF 2.0 (Export Scene to glTF)

กำหนดตัวเลือกการบันทึก GLTF ให้แปลง `PhongMaterial` ใด ๆ เป็น `PbrMaterial` โดยอัตโนมัติ นี่คือหัวใจของ **export scene to glTF**:

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

เมื่อโค้ดนี้ทำงาน ฉากจะถูกเขียนลงในไฟล์ `Non_PBRtoPBRMaterial_Out.gltf` ตัวแปลง `MaterialConverter` ที่กำหนดเองจะทำให้วัสดุ Phong ถูกเปลี่ยนเป็นวัสดุ PBR ดังนั้นไฟล์ glTF ที่ได้จะแสดงเงาที่สมจริงในตัวดู glTF ใด ๆ

## ปัญหาและวิธีแก้ไขทั่วไป

| Issue | Solution |
|-------|----------|
| **FileNotFoundException** ขณะบันทึก | ตรวจสอบให้ `MyDir` ชี้ไปยังโฟลเดอร์ที่มีอยู่และแอปพลิเคชันมีสิทธิ์เขียน |
| **ClassCastException** ในตัวแปลง | ตรวจสอบให้แน่ใจว่าวัสดุที่ส่งให้ตัวแปลงเป็น `PhongMaterial` จริง ๆ เพิ่มการตรวจสอบ `instanceof` หากใช้วัสดุหลายประเภท |
| **Missing textures** หลังการส่งออก | glTF ต้องการเทกเจอร์แยกออก; เพิ่มการจัดการเทกเจอร์ในตัวแปลงหากจำเป็น |

## คำถามที่พบบ่อย

**Q: Aspose.3D รองรับสภาพแวดล้อมการพัฒนา Java อื่น ๆ นอกจาก Eclipse หรือไม่?**  
A: ใช่, Aspose.3D ทำงานกับ IDE Java ใด ๆ รวมถึง IntelliJ IDEA, NetBeans, และ VS Code

**Q: สามารถใช้ Aspose.3D ในโครงการเชิงพาณิชย์ได้หรือไม่?**  
A: ใช้ได้, คุณสามารถใช้ Aspose.3D ทั้งในโครงการส่วนบุคคลและเชิงพาณิชย์ ดูรายละเอียดลิขสิทธิ์ได้ที่ [purchase page](https://purchase.aspose.com/buy)

**Q: มีเวอร์ชันทดลองฟรีหรือไม่?**  
A: มี, คุณสามารถเข้าถึงเวอร์ชันทดลองฟรีได้ที่ [here](https://releases.aspose.com/)

**Q: จะหาแหล่งสนับสนุนสำหรับ Aspose.3D ได้จากที่ไหน?**  
A: สำรวจ [Aspose.3D forum](https://forum.aspose.com/c/3d/18) เพื่อรับการสนับสนุนจากชุมชน

**Q: จะขอรับลิขสิทธิ์ชั่วคราวสำหรับ Aspose.3D ได้อย่างไร?**  
A: เยี่ยมชม [this link](https://purchase.aspose.com/temporary-license/) เพื่อดูข้อมูลลิขสิทธิ์ชั่วคราว

## สรุป

โดยทำตามขั้นตอนข้างต้น คุณจะรู้วิธี **export scene to glTF** ใน Java ด้วย Aspose.3D พร้อมกับการอัปเกรดวัสดุ Phong เป็น PBR โดยอัตโนมัติ กระบวนการนี้ช่วยให้คุณสร้างสินทรัพย์คุณภาพสูงที่อิงตามฟิสิกส์และพร้อมใช้งานในไพป์ไลน์การเรนเดอร์สมัยใหม่, ตัวดูเว็บ, และประสบการณ์ AR/VR ทดลองใช้เรขาคณิตที่ซับซ้อนมากขึ้น, เทกเจอร์, และแสงเพื่อใช้ศักยภาพเต็มที่ของ PBR และ glTF

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-22  
**Tested With:** Aspose.3D 24.12 for Java  
**Author:** Aspose  

---