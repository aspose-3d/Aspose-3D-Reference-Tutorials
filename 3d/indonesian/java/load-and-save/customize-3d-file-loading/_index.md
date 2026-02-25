---
date: 2026-02-25
description: Pelajari cara membalik sistem koordinat dan menyesuaikan impor 3D menggunakan
  Aspose.3D LoadOptions di Java. Panduan langkah demi langkah untuk 3DS, OBJ, STL,
  U3D, glTF, PLY, X, dan FBX opsional.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Balik Sistem Koordinat – Sesuaikan Pemuatan File 3D di Java dengan Aspose.3D
url: /id/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Balik Sistem Koordinat – Kustomisasi Pemuatan File 3D di Java dengan Aspose.3D

Dalam lanskap desain dan pengembangan 3D yang terus berkembang, **flipping the coordinate system** saat mengimpor model adalah kebutuhan umum. Baik Anda mengonversi aset dari sistem right‑handed ke left‑handed atau perlu menyelaraskan model dengan konvensi sumbu engine Anda, Aspose.3D for Java memberikan kontrol yang sangat detail. Tutorial ini memandu Anda cara **customize 3D import** menggunakan `LoadOptions` Aspose.3D, mencakup format paling populer seperti 3DS, OBJ, STL, U3D, glTF, PLY, X, dan FBX opsional.

## Jawaban Cepat
- **Apa yang dilakukan “flip coordinate system”?** Ia menukar sumbu X/Y/Z untuk menyesuaikan dengan konvensi koordinat target.  
- **Format mana yang mendukung flipping?** Semua format utama (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) menyediakan opsi `setFlipCoordinateSystem`.  
- **Apakah saya memerlukan pustaka tambahan?** Hanya JAR Aspose.3D for Java; tidak diperlukan konverter eksternal.  
- **Bisakah saya memuat material sekaligus?** Ya—gunakan `setEnableMaterials(true)` untuk file OBJ.  
- **Apakah lisensi diperlukan untuk produksi?** Lisensi Aspose.3D yang valid diperlukan untuk penyebaran non‑trial.

## Apa itu “flip coordinate system”?
Flipping the coordinate system mengubah orientasi sumbu yang digunakan oleh model yang diimpor. Hal ini penting ketika file sumber menggunakan handedness yang berbeda (right‑handed vs. left‑handed) dibandingkan engine rendering Anda, sehingga mencegah model tampak terbalik atau termirror.

## Mengapa menyesuaikan impor 3D?
- Pertahankan transformasi animasi (`setApplyAnimationTransform`).  
- Perbaiki penanganan warna (`setGammaCorrectedColor`).  
- Selesaikan jalur sumber daya eksternal melalui `getLookupPaths()`.  
- Optimalkan penggunaan memori dengan memuat hanya apa yang Anda butuhkan.

## Prasyarat

- Pemahaman dasar tentang pemrograman Java.  
- Java Development Kit (JDK) terinstal.  
- Perpustakaan Aspose.3D for Java telah diunduh. Anda dapat memperolehnya [di sini](https://releases.aspose.com/3d/java/).  
- Familiaritas dengan format file 3D seperti 3DS, OBJ, STL, U3D, glTF, PLY, X, dan FBX.

## Impor Paket

Dalam proyek Java Anda, pastikan untuk mengimpor paket Aspose.3D yang diperlukan:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Cara menyesuaikan impor 3D dengan LoadOptions

Berikut adalah potongan kode langkah demi langkah yang menunjukkan cara mengaktifkan opsi **flip coordinate system** untuk setiap format yang didukung. Potongan kode siap disalin ke proyek Anda; cukup ganti `"Your Document Directory"` dengan jalur sebenarnya ke aset Anda.

### Langkah 1: Kustomisasi Pemuatan File 3DS

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

### Langkah 2: Kustomisasi Pemuatan File OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Langkah 3: Kustomisasi Pemuatan File STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Langkah 4: Kustomisasi Pemuatan File U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Langkah 5: Kustomisasi Pemuatan File glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Langkah 6: Kustomisasi Pemuatan File PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Langkah 7: Kustomisasi Pemuatan File X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Langkah 8: Kustomisasi Pemuatan File FBX (Opsional)

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

## Masalah Umum dan Solusinya
- **Model muncul termirror setelah dimuat** – Pastikan `setFlipCoordinateSystem(true)` diatur untuk format yang tepat.  
- **Materials are missing** – Untuk file OBJ, pastikan `setEnableMaterials(true)` dan bahwa file material (.mtl) berada di salah satu jalur lookup.  
- **Texture coordinates are upside‑down** – Untuk glTF, Anda mungkin perlu `setFlipTexCoordV(true)` selain membalik sumbu.  
- **File not found errors** – Tambahkan direktori yang berisi sumber daya eksternal (tekstur, file tambahan) ke `loadOpts.getLookupPaths()`.

## Kesimpulan

Dengan memanfaatkan `LoadOptions` Aspose.3D, Anda dapat **flip the coordinate system** dan **customize 3D import** untuk hampir semua format utama. Tingkat kontrol ini menghilangkan kebutuhan akan skrip pasca‑pemrosesan dan memastikan aset Anda dirender dengan benar pada percobaan pertama.

## Pertanyaan yang Sering Diajukan

### Q1: Di mana saya dapat menemukan dokumentasi Aspose.3D for Java?
A1: Dokumentasi tersedia [di sini](https://reference.aspose.com/3d/java/).

### Q2: Bagaimana cara mengunduh Aspose.3D for Java?
A2: Anda dapat mengunduhnya [di sini](https://releases.aspose.com/3d/java/).

### Q3: Apakah tersedia trial gratis?
A3: Ya, Anda dapat mengakses trial gratis [di sini](https://releases.aspose.com/).

### Q4: Di mana saya dapat mendapatkan dukungan untuk Aspose.3D for Java?
A4: Kunjungi forum dukungan [di sini](https://forum.aspose.com/c/3d/18).

### Q5: Apakah saya memerlukan lisensi sementara untuk pengujian?
A5: Ya, dapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Terakhir Diperbarui:** 2026-02-25  
**Diuji Dengan:** Aspose.3D for Java 24.11 (latest)  
**Penulis:** Aspose