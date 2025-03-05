---
title: อัปเกรดวัสดุ 3D เป็น PBR เพื่อความสมจริงที่เพิ่มขึ้นใน Java ด้วย Aspose.3D
linktitle: อัปเกรดวัสดุ 3D เป็น PBR เพื่อความสมจริงที่เพิ่มขึ้นใน Java ด้วย Aspose.3D
second_title: Aspose.3D จาวา API
description: อัปเกรดวัสดุ 3D เป็น PBR ได้อย่างง่ายดายใน Java ด้วย Aspose.3D บรรลุความสมจริงที่เพิ่มขึ้นเพื่อภาพที่น่าหลงใหล
type: docs
weight: 13
url: /th/java/load-and-save/upgrade-materials-to-pbr/
---
## การแนะนำ

การอัปเกรดวัสดุ 3D ของคุณเป็น PBR ถือเป็นขั้นตอนการเปลี่ยนแปลงในการบรรลุภาพที่เหมือนจริงในแอปพลิเคชัน Java ของคุณ Aspose.3D ทำให้กระบวนการนี้ง่ายขึ้น ช่วยให้คุณสามารถเปลี่ยนจากวัสดุแบบดั้งเดิมไปเป็นวัสดุ PBR ได้อย่างราบรื่น ในบทช่วยสอนนี้ เราจะสำรวจข้อกำหนดเบื้องต้นที่จำเป็น นำเข้าแพ็คเกจ และแยกย่อยแต่ละตัวอย่างออกเป็นขั้นตอนโดยละเอียด

## ข้อกำหนดเบื้องต้น

ก่อนที่จะเข้าสู่บทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

1.  Aspose.3D สำหรับ Java: ดาวน์โหลดและติดตั้งไลบรารี Aspose.3D จาก[หน้าปล่อย](https://releases.aspose.com/3d/java/).

2. สภาพแวดล้อมการพัฒนา Java: ตรวจสอบให้แน่ใจว่าคุณได้ตั้งค่าสภาพแวดล้อมการพัฒนา Java บนเครื่องของคุณ

3. ไดเร็กทอรีเอกสาร: สร้างไดเร็กทอรีเฉพาะสำหรับเอกสาร 3D ของคุณ

## แพ็คเกจนำเข้า

เพื่อเริ่มกระบวนการอัพเกรด ให้นำเข้าแพ็คเกจที่จำเป็นไปยังโปรเจ็กต์ Java ของคุณ ใช้ข้อมูลโค้ดต่อไปนี้เป็นแนวทาง:

```java
import com.aspose.threed.*;
```

ตรวจสอบให้แน่ใจว่าคุณได้รวมแพ็คเกจ Aspose.3D ที่จำเป็นทั้งหมดเพื่อใช้ประโยชน์จากฟังก์ชันการทำงานได้อย่างราบรื่น

## ขั้นตอนที่ 1: เริ่มต้นฉาก 3 มิติใหม่

เริ่มต้นด้วยการเริ่มต้นฉาก 3 มิติใหม่โดยใช้โค้ดต่อไปนี้:

```java
// ExStart: เตรียมใช้งาน Scene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd: เตรียมใช้งานฉาก
```

## ขั้นตอนที่ 2: สร้างกล่องด้วย PhongMaterial

สร้างกล่อง 3D และกำหนด PhongMaterial ให้กับมัน:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ตัวอย่าง: CreateBoxWithMaterial
```

## ขั้นตอนที่ 3: บันทึกในรูปแบบ GLTF 2.0

บันทึกฉากในรูปแบบ GLTF 2.0 โดยแปลง PhongMaterial เป็น PBRMaterial ในระหว่างกระบวนการ:

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

ทำตามขั้นตอนเหล่านี้อย่างพิถีพิถันเพื่ออัปเกรดวัสดุ 3D ของคุณเป็น PBR ได้อย่างราบรื่น ซึ่งเพิ่มความสมจริงในแอปพลิเคชัน Java

## บทสรุป

โดยสรุป Aspose.3D สำหรับ Java ช่วยให้คุณยกระดับความน่าดึงดูดทางภาพของกราฟิก 3D ของคุณโดยการอัพเกรดวัสดุเป็น PBR นำเทคโนโลยีนี้มาใช้เพื่อเพิ่มความสมจริงและดึงดูดผู้ชมของคุณด้วยแอปพลิเคชัน Java ที่สวยงามตระการตา

## คำถามที่พบบ่อย

### คำถามที่ 1: Aspose.3D เข้ากันได้กับสภาพแวดล้อมการพัฒนา Java อื่นที่ไม่ใช่ Eclipse หรือไม่

ตอบ 1: ใช่ Aspose.3D เข้ากันได้กับสภาพแวดล้อมการพัฒนา Java ต่างๆ

### คำถามที่ 2: ฉันสามารถใช้ Aspose.3D สำหรับโครงการเชิงพาณิชย์ได้หรือไม่

 ตอบ 2: ได้ คุณสามารถใช้ Aspose.3D สำหรับทั้งโครงการส่วนตัวและเชิงพาณิชย์ เยี่ยมชม[หน้าซื้อ](https://purchase.aspose.com/buy) สำหรับรายละเอียดใบอนุญาต

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

A3: ได้ คุณสามารถทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D ได้ที่ไหน

 A4: สำรวจ[ฟอรั่ม Aspose.3D](https://forum.aspose.com/c/3d/18) เพื่อสนับสนุนชุมชน

### คำถามที่ 5: ฉันจะขอรับใบอนุญาตชั่วคราวสำหรับ Aspose.3D ได้อย่างไร

 A5: เยี่ยมเลย[ลิงค์นี้](https://purchase.aspose.com/temporary-license/) สำหรับข้อมูลใบอนุญาตชั่วคราว