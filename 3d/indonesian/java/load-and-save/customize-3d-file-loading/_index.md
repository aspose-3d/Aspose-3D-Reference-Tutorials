---
title: Sesuaikan Pemuatan File 3D di Java dengan Aspose.3D LoadOptions
linktitle: Sesuaikan Pemuatan File 3D di Java dengan Aspose.3D LoadOptions
second_title: Asumsikan.3D Java API
description: Tingkatkan pemuatan file 3D Anda di Java dengan LoadOptions Aspose.3D yang dapat disesuaikan. Pelajari penyesuaian langkah demi langkah untuk 3DS, OBJ, STL, U3D, glTF, PLY, X, dan FBX opsional.
weight: 12
url: /id/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Sesuaikan Pemuatan File 3D di Java dengan Aspose.3D LoadOptions

## Perkenalan

Dalam lanskap desain dan pengembangan 3D yang terus berkembang, penanganan format file 3D yang efisien sangatlah penting. Aspose.3D untuk Java memberikan solusi ampuh untuk menyesuaikan pemuatan berbagai format file 3D. Tutorial ini akan memandu Anda melalui proses penyesuaian pemuatan file 3D di Java menggunakan LoadOptions Aspose.3D.

## Prasyarat

Sebelum mendalami proses penyesuaian, pastikan Anda memiliki hal berikut:

- Pemahaman dasar pemrograman Java.
- Kit Pengembangan Java (JDK) yang diinstal.
-  Aspose.3D untuk perpustakaan Java diunduh. Anda bisa mendapatkannya[Di Sini](https://releases.aspose.com/3d/java/).
- Keakraban dengan format file 3D seperti 3DS, OBJ, STL, U3D, glTF, PLY, X, dan FBX.

## Paket Impor

Di proyek Java Anda, pastikan untuk mengimpor paket Aspose.3D yang diperlukan:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Sesuaikan Pemuatan File 3D

### Langkah 1: Sesuaikan Pemuatan File 3DS

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

### Langkah 2: Sesuaikan Pemuatan File OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Langkah 3: Sesuaikan Pemuatan File STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Langkah 4: Sesuaikan Pemuatan File U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Langkah 5: Sesuaikan Pemuatan File glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Langkah 6: Sesuaikan Pemuatan File PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Langkah 7: Sesuaikan Pemuatan File X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Langkah 8: Sesuaikan Pemuatan File FBX (Opsional)

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

## Kesimpulan

Menyesuaikan pemuatan file 3D di Java dengan LoadOptions Aspose.3D memberdayakan pengembang untuk menyesuaikan proses impor dengan kebutuhan spesifik. Baik itu menyesuaikan transformasi animasi, membalik sistem koordinat, atau menangani dependensi eksternal, Aspose.3D memberikan fleksibilitas yang diperlukan untuk integrasi yang lancar.

## FAQ

### Q1: Di mana saya dapat menemukan dokumentasi Aspose.3D untuk Java?

 A1: Dokumentasi tersedia[Di Sini](https://reference.aspose.com/3d/java/).

### Q2: Bagaimana cara mengunduh Aspose.3D untuk Java?

 A2: Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/java/).

### Q3: Apakah tersedia uji coba gratis?

 A3: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Di mana saya bisa mendapatkan dukungan untuk Aspose.3D untuk Java?

 A4: Kunjungi forum dukungan[Di Sini](https://forum.aspose.com/c/3d/18).

### Q5: Apakah saya memerlukan lisensi sementara untuk pengujian?

 A5: Ya, dapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
