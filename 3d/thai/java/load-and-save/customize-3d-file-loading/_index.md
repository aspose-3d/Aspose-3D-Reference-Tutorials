---
title: ปรับแต่งการโหลดไฟล์ 3D ใน Java ด้วย Aspose.3D LoadOptions
linktitle: ปรับแต่งการโหลดไฟล์ 3D ใน Java ด้วย Aspose.3D LoadOptions
second_title: Aspose.3D จาวา API
description: ปรับปรุงการโหลดไฟล์ 3D ของคุณใน Java ด้วย LoadOptions ที่ปรับแต่งได้ของ Aspose.3D เรียนรู้การปรับแต่งทีละขั้นตอนสำหรับ 3DS, OBJ, STL, U3D, glTF, PLY, X และ FBX เสริม
weight: 12
url: /th/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ปรับแต่งการโหลดไฟล์ 3D ใน Java ด้วย Aspose.3D LoadOptions

## การแนะนำ

ในภูมิทัศน์ที่เปลี่ยนแปลงตลอดเวลาของการออกแบบและการพัฒนา 3D การจัดการรูปแบบไฟล์ 3D อย่างมีประสิทธิภาพถือเป็นสิ่งสำคัญ Aspose.3D สำหรับ Java มอบโซลูชันอันทรงพลังในการปรับแต่งการโหลดไฟล์ 3D รูปแบบต่างๆ บทช่วยสอนนี้จะแนะนำคุณตลอดกระบวนการปรับแต่งการโหลดไฟล์ 3D ใน Java โดยใช้ LoadOptions ของ Aspose.3D

## ข้อกำหนดเบื้องต้น

ก่อนที่จะดำดิ่งสู่กระบวนการปรับแต่ง ตรวจสอบให้แน่ใจว่าคุณมีสิ่งต่อไปนี้:

- ความเข้าใจพื้นฐานเกี่ยวกับการเขียนโปรแกรม Java
- ติดตั้ง Java Development Kit (JDK) แล้ว
-  ดาวน์โหลด Aspose.3D สำหรับไลบรารี Java แล้ว คุณสามารถรับมันได้[ที่นี่](https://releases.aspose.com/3d/java/).
- ความคุ้นเคยกับรูปแบบไฟล์ 3D เช่น 3DS, OBJ, STL, U3D, glTF, PLY, X และ FBX

## แพ็คเกจนำเข้า

ในโปรเจ็กต์ Java ของคุณ ตรวจสอบให้แน่ใจว่าได้นำเข้าแพ็คเกจ Aspose.3D ที่จำเป็น:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ปรับแต่งการโหลดไฟล์ 3D

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

### ขั้นตอนที่ 8: ปรับแต่งการโหลดไฟล์ FBX (ไม่บังคับ)

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

## บทสรุป

การปรับแต่งการโหลดไฟล์ 3D ใน Java ด้วย LoadOptions ของ Aspose.3D ช่วยให้นักพัฒนาสามารถปรับแต่งกระบวนการนำเข้าให้ตรงตามความต้องการเฉพาะได้ ไม่ว่าจะเป็นการปรับการแปลงภาพเคลื่อนไหว การพลิกระบบพิกัด หรือการจัดการการพึ่งพาภายนอก Aspose.3D มอบความยืดหยุ่นที่จำเป็นสำหรับการผสานรวมที่ราบรื่น

## คำถามที่พบบ่อย

### คำถามที่ 1: ฉันจะหาเอกสารประกอบ Aspose.3D สำหรับ Java ได้ที่ไหน

 A1: มีเอกสารประกอบให้[ที่นี่](https://reference.aspose.com/3d/java/).

### คำถามที่ 2: ฉันจะดาวน์โหลด Aspose.3D สำหรับ Java ได้อย่างไร

 A2: คุณสามารถดาวน์โหลดได้[ที่นี่](https://releases.aspose.com/3d/java/).

### คำถามที่ 3: มีการทดลองใช้ฟรีหรือไม่?

 A3: ได้ คุณสามารถเข้าถึงรุ่นทดลองใช้ฟรีได้[ที่นี่](https://releases.aspose.com/).

### คำถามที่ 4: ฉันจะรับการสนับสนุนสำหรับ Aspose.3D สำหรับ Java ได้ที่ไหน

 A4: เยี่ยมชมฟอรั่มการสนับสนุน[ที่นี่](https://forum.aspose.com/c/3d/18).

### คำถามที่ 5: ฉันจำเป็นต้องมีใบอนุญาตชั่วคราวในการทดสอบหรือไม่

 A5: ใช่ รับใบอนุญาตชั่วคราว[ที่นี่](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
