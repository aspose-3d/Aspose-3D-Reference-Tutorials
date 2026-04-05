---
date: 2026-02-25
description: เรียนรู้วิธีสลับระบบพิกัดและปรับแต่งการนำเข้า 3D ด้วย Aspose.3D LoadOptions
  ใน Java คู่มือขั้นตอนต่อขั้นตอนสำหรับ 3DS, OBJ, STL, U3D, glTF, PLY, X และ FBX (เป็นตัวเลือก)
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: พลิกระบบพิกัด – ปรับแต่งการโหลดไฟล์ 3D ใน Java ด้วย Aspose.3D
url: /th/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# พลิกระบบพิกัด – ปรับแต่งการโหลดไฟล์ 3D ใน Java ด้วย Aspose.3D

ในภูมิทัศน์ที่เปลี่ยนแปลงอย่างต่อเนื่องของการออกแบบและพัฒนา 3D, **การพลิกระบบพิกัด** ขณะนำเข้าโมเดลเป็นความต้องการทั่วไป ไม่ว่าคุณจะกำลังแปลงสินทรัพย์จากระบบขวาเป็นซ้ายหรือจำเป็นต้องจัดแนวโมเดลให้สอดคล้องกับแนวแกนของเอนจิ้นของคุณ, Aspose.3D for Java ให้การควบคุมที่ละเอียดอ่อน บทแนะนำนี้จะพาคุณผ่านขั้นตอนการ **ปรับแต่งการนำเข้า 3D** ด้วย `LoadOptions` ของ Aspose.3D, ครอบคลุมรูปแบบที่นิยมที่สุดเช่น 3DS, OBJ, STL, U3D, glTF, PLY, X, และ FBX ที่เป็นตัวเลือกเสริม.

## คำตอบอย่างรวดเร็ว
- **การพลิกระบบพิกัดทำอะไร?** มันสลับแกน X/Y/Z เพื่อให้ตรงกับแนวพิกัดเป้าหมาย.  
- **รูปแบบใดสนับสนุนการพลิก?** ทุกรูปแบบหลัก (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) มีตัวเลือก `setFlipCoordinateSystem`.  
- **ต้องใช้ไลบรารีเพิ่มเติมหรือไม่?** เพียงแค่ JAR ของ Aspose.3D for Java; ไม่ต้องใช้ตัวแปลงภายนอก.  
- **สามารถโหลดวัสดุพร้อมกันได้หรือไม่?** ได้—ใช้ `setEnableMaterials(true)` สำหรับไฟล์ OBJ.  
- **ต้องมีลิขสิทธิ์สำหรับการใช้งานจริงหรือไม่?** จำเป็นต้องมีลิขสิทธิ์ Aspose.3D ที่ถูกต้องสำหรับการใช้งานที่ไม่ใช่รุ่นทดลอง.

## การ “พลิกระบบพิกัด” คืออะไร?
การพลิกระบบพิกัดเปลี่ยนการจัดแนวของแกนที่ใช้โดยโมเดลที่นำเข้า ซึ่งจำเป็นเมื่อไฟล์ต้นฉบับใช้การกำหนดมือ (handedness) ที่ต่างกัน (ขวา vs. ซ้าย) จากเอนจิ้นการเรนเดอร์ของคุณ เพื่อป้องกันไม่ให้โมเดลปรากฏเป็นภาพสะท้อนหรือกลับหัว.

## ทำไมต้องปรับแต่งการนำเข้า 3D?
การปรับแต่งการนำเข้าให้คุณ:
- รักษาการแปลงแอนิเมชัน (`setApplyAnimationTransform`).  
- แก้ไขการจัดการสีให้ถูกต้อง (`setGammaCorrectedColor`).  
- แก้ไขเส้นทางของทรัพยากรภายนอกผ่าน `getLookupPaths()`.  
- ปรับการใช้หน่วยความจำโดยโหลดเฉพาะที่คุณต้องการ.

## ข้อกำหนดเบื้องต้น

- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม Java.  
- ติดตั้ง Java Development Kit (JDK).  
- ดาวน์โหลดไลบรารี Aspose.3D for Java. คุณสามารถรับได้จาก [ที่นี่](https://releases.aspose.com/3d/java/).  
- ความคุ้นเคยกับรูปแบบไฟล์ 3D เช่น 3DS, OBJ, STL, U3D, glTF, PLY, X, และ FBX.

## นำเข้าแพ็กเกจ

ในโครงการ Java ของคุณ, ตรวจสอบให้แน่ใจว่าได้ทำการนำเข้าแพ็กเกจ Aspose.3D ที่จำเป็นแล้ว:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## วิธีปรับแต่งการนำเข้า 3D ด้วย LoadOptions

ด้านล่างเป็นโค้ดตัวอย่างแบบขั้นตอนต่อขั้นตอนที่แสดงวิธีเปิดใช้งานตัวเลือก **พลิกระบบพิกัด** สำหรับแต่ละรูปแบบที่รองรับ โค้ดเหล่านี้พร้อมคัดลอกไปใช้ในโปรเจกต์ของคุณ; เพียงเปลี่ยน `"Your Document Directory"` ให้เป็นเส้นทางจริงของทรัพยากรของคุณ.

### ขั้นตอนที่ 1: ปรับแต่งการโหลดไฟล์ 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### ขั้นตอนที่ 2: ปรับแต่งการโหลดไฟล์ OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### ขั้นตอนที่ 3: ปรับแต่งการโหลดไฟล์ STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### ขั้นตอนที่ 4: ปรับแต่งการโหลดไฟล์ U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### ขั้นตอนที่ 5: ปรับแต่งการโหลดไฟล์ glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### ขั้นตอนที่ 6: ปรับแต่งการโหลดไฟล์ PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### ขั้นตอนที่ 7: ปรับแต่งการโหลดไฟล์ X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### ขั้นตอนที่ 8: ปรับแต่งการโหลดไฟล์ FBX (ตัวเลือกเสริม)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## ปัญหาทั่วไปและวิธีแก้
- **โมเดลปรากฏเป็นภาพสะท้อนหลังจากโหลด** – ตรวจสอบว่าได้ตั้งค่า `setFlipCoordinateSystem(true)` สำหรับรูปแบบที่ถูกต้อง.  
- **วัสดุหาย** – สำหรับไฟล์ OBJ, ตรวจสอบว่าได้ตั้งค่า `setEnableMaterials(true)` และไฟล์วัสดุ (.mtl) อยู่ในหนึ่งในเส้นทาง lookup.  
- **พิกัดเทกซ์เจอร์กลับหัว** – สำหรับ glTF, คุณอาจต้องใช้ `setFlipTexCoordV(true)` ร่วมกับการพลิกแกน.  
- **เกิดข้อผิดพลาดไม่พบไฟล์** – เพิ่มไดเรกทอรีที่มีทรัพยากรภายนอก (เทกซ์เจอร์, ไฟล์เสริม) ไปยัง `loadOpts.getLookupPaths()`.

## สรุป

โดยใช้ `LoadOptions` ของ Aspose.3D, คุณสามารถ **พลิกระบบพิกัด** และ **ปรับแต่งการนำเข้า 3D** สำหรับรูปแบบหลักเกือบทุกประเภท การควบคุมระดับนี้ช่วยขจัดความจำเป็นในการใช้สคริปต์หลังการประมวลผลและทำให้ทรัพยากรของคุณแสดงผลได้อย่างถูกต้องตั้งแต่ครั้งแรก.

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันสามารถหาเอกสาร Aspose.3D for Java ได้จากที่ไหน?
A1: เอกสารพร้อมให้บริการ [ที่นี่](https://reference.aspose.com/3d/java/).

### คำถามที่ 2: ฉันจะดาวน์โหลด Aspose.3D for Java ได้อย่างไร?
A2: คุณสามารถดาวน์โหลดได้จาก [ที่นี่](https://releases.aspose.com/3d/java/).

### คำถามที่ 3: มีรุ่นทดลองฟรีหรือไม่?
A3: มี, คุณสามารถเข้าถึงรุ่นทดลองฟรีได้ [ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D for Java ได้จากที่ไหน?
A4: เยี่ยมชมฟอรั่มสนับสนุน [ที่นี่](https://forum.aspose.com/c/3d/18).

### คำถามที่ 5: ฉันต้องการลิขสิทธิ์ชั่วคราวสำหรับการทดสอบหรือไม่?
A5: ต้องการ, รับลิขสิทธิ์ชั่วคราวได้จาก [ที่นี่](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**อัปเดตล่าสุด:** 2026-02-25  
**ทดสอบด้วย:** Aspose.3D for Java 24.11 (latest)  
**ผู้เขียน:** Aspose