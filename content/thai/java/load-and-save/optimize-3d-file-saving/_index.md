---
title: เพิ่มประสิทธิภาพการบันทึกไฟล์ 3D ใน Java ด้วย Aspose.3D SaveOptions
linktitle: เพิ่มประสิทธิภาพการบันทึกไฟล์ 3D ใน Java ด้วย Aspose.3D SaveOptions
second_title: Aspose.3D จาวา API
description: เรียนรู้วิธีเพิ่มประสิทธิภาพการบันทึกไฟล์ 3D ใน Java ด้วย Aspose.3D SaveOptions เพิ่มประสิทธิภาพและปรับแต่งเอาท์พุตได้อย่างง่ายดาย
type: docs
weight: 16
url: /th/java/load-and-save/optimize-3d-file-saving/
---
## การแนะนำ

Aspose.3D เป็นไลบรารี Java ที่มีฟีเจอร์มากมายซึ่งช่วยให้นักพัฒนาสามารถทำงานกับโมเดล 3D ได้อย่างราบรื่น เมื่อพูดถึงการบันทึกไฟล์ 3D คลาส SaveOptions มีการตั้งค่ามากมายเพื่อปรับแต่งเอาต์พุตตามความต้องการของคุณ ในบทช่วยสอนนี้ เราจะสำรวจตัวเลือกการบันทึกต่างๆ และวิธีการใช้ประโยชน์จากตัวเลือกเหล่านั้นเพื่อปรับกระบวนการให้เหมาะสม

## ข้อกำหนดเบื้องต้น

ก่อนที่เราจะเจาะลึกบทช่วยสอน ตรวจสอบให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นต่อไปนี้:

-  Aspose.3D สำหรับ Java: ตรวจสอบให้แน่ใจว่าคุณมีไลบรารี Aspose.3D ที่รวมอยู่ในโปรเจ็กต์ Java ของคุณ คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/java/).

- สภาพแวดล้อมการพัฒนา Java: ตั้งค่าสภาพแวดล้อมการพัฒนา Java ที่ใช้งานได้บนเครื่องของคุณ

- ไดเร็กทอรีเอกสาร: สร้างไดเร็กทอรีที่คุณต้องการบันทึกไฟล์ 3D ของคุณและบันทึกเส้นทางเพื่อใช้ในภายหลัง

## แพ็คเกจนำเข้า

 ในโปรเจ็กต์ Java ของคุณ ให้นำเข้าแพ็คเกจที่จำเป็นสำหรับการทำงานกับ Aspose.3D ซึ่งรวมถึง`Scene` คลาสและคลาส SaveOptions ต่างๆ ด้านล่างนี้เป็นตัวอย่างพื้นฐาน:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

ตอนนี้ เราจะแบ่งแต่ละตัวอย่างออกเป็นหลายขั้นตอนเพื่อสาธิตการใช้งาน SaveOptions ต่างๆ

## ขั้นตอนที่ 1: พิมพ์สวยใน GLTF SaveOption

 ที่`prettyPrintInGltfSaveOption` วิธีการนี้ช่วยให้คุณสร้างไฟล์ GLTF ที่มีเนื้อหา JSON ที่เยื้องไว้เพื่อให้มนุษย์สามารถอ่านได้

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // เริ่มต้นฉาก 3D
    Scene scene = new Scene(new Sphere());
    
    // เตรียมใช้งาน GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // เปิดใช้งานการพิมพ์แบบสวยเพื่อให้อ่านง่ายขึ้น
    opt.setPrettyPrint(true);
    
    // บันทึกฉาก 3 มิติ
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## ขั้นตอนที่ 2: ตัวเลือกการบันทึก HTML5

 ที่`html5SaveOption` วิธีการสาธิตวิธีการบันทึกฉาก 3 มิติเป็นไฟล์ HTML5 รวมถึงตัวเลือกการปรับแต่ง

```java
public static void html5SaveOption() throws IOException {
    // เริ่มต้นฉาก
    Scene scene = new Scene();
    
    // สร้างโหนดย่อยด้วยทรงกระบอก
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //ตั้งค่าคุณสมบัติสำหรับโหนดลูก
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // เพิ่มแสงสว่างให้กับฉาก
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // เริ่มต้น HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // ปรับแต่งตัวเลือกต่างๆ (เช่น ปิดกริดและอินเทอร์เฟซผู้ใช้)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // บันทึกฉากเป็นไฟล์ HTML5
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 ดำเนินการแยกย่อยที่คล้ายกันต่อไปสำหรับวิธี SaveOptions อื่นๆ เช่น`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , และ`drcSaveOptions`.

## บทสรุป

ด้วยการทำตามบทช่วยสอนที่ครอบคลุมนี้ คุณได้เรียนรู้วิธีเพิ่มประสิทธิภาพการบันทึกไฟล์ 3D ใน Java โดยใช้ Aspose.3D SaveOptions ไม่ว่าคุณจะสนใจการพิมพ์ไฟล์ GLTF ที่สวยงามหรือการปรับแต่งเอาต์พุต HTML5 Aspose.3D ก็จัดเตรียมเครื่องมือเพื่อปรับปรุงเวิร์กโฟลว์กราฟิก 3D ของคุณ

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันจะฝังเนื้อหาในไฟล์ glTF ได้อย่างไร

 A1: หากต้องการฝังเนื้อหา ให้ใช้`setEmbedAssets(true)` วิธีการใน`GltfSaveOptions` ระดับ.

###  Q2: อะไรคือจุดประสงค์ของ`setPositionBits` method in `DracoSaveOptions`?

 A2: เดอะ`setPositionBits` method จะตั้งค่าบิตการหาปริมาณสำหรับตำแหน่งในอัลกอริธึมการบีบอัดของ Draco

### คำถามที่ 3: ฉันสามารถส่งออกข้อมูลปกติเป็นไฟล์ U3D ได้หรือไม่

 A3: ได้ คุณสามารถส่งออกข้อมูลปกติได้โดยการตั้งค่า`setExportNormals(true)` ใน`U3dSaveOptions` ระดับ.

### คำถามที่ 4: ฉันจะละทิ้งไฟล์วัสดุที่บันทึกไว้ในการส่งออก OBJ ได้อย่างไร

A4: ใช้`setFileSystem(new DummyFileSystem())` วิธีการใน`ObjSaveOptions` คลาสที่จะทิ้งไฟล์สื่อการสอน

### คำถามที่ 5: มีวิธีบันทึกการขึ้นต่อกันไปยังไดเร็กทอรีในเครื่องในไฟล์ OBJ หรือไม่?

 A5: ใช่ ใช้`setFileSystem(new LocalFileSystem(MyDir))` วิธีการใน`ObjSaveOptions` คลาสเพื่อบันทึกการขึ้นต่อกันในเครื่อง