---
date: 2025-12-19
description: Pelajari cara menyesuaikan pemuatan 3D di Java menggunakan Aspose.3D
  LoadOptions. Panduan langkah demi langkah yang mencakup file 3DS, OBJ, STL, U3D,
  glTF, PLY, X, dan file FBX opsional.
linktitle: Customize 3D Loading Java – How to customize 3d loading java with Aspose.3D
  LoadOptions
second_title: Aspose.3D Java API
title: Sesuaikan Pemuatan 3D Java – Cara menyesuaikan pemuatan 3D Java dengan Aspose.3D
  LoadOptions
url: /id/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Sesuaikan 3D Loading Java – Cara menyesuaikan 3d loading java dengan Aspose.3D LoadOptions

## Pendahuluan

Dalam aplikasi 3D modern, **customize 3d loading java** sangat penting untuk memastikan bahwa model muncul persis seperti yang diharapkan, terlepas dari format sumbernya. Baik Anda sedang membangun mesin game, penampil AR/VR, atau alat konversi CAD, kemampuan mengontrol cara file 3DS, OBJ, STL, U3D, glTF, PLY, X, dan bahkan FBX diimpor dapat menghemat jam‑jam proses pasca‑pemrosesan. Tutorial ini memandu Anda melalui setiap langkah menyesuaikan pemuatan file 3D di Java menggunakan kelas `LoadOptions` yang fleksibel dari Aspose.3D.

## Jawaban Cepat
- **Apa arti “customize 3d loading java”?** Itu berarti mengonfigurasi `LoadOptions` Aspose.3D untuk mengontrol perilaku impor seperti pembalikan sistem koordinat, penanganan material, dan transformasi animasi.  
- **Format apa saja yang dapat saya sesuaikan?** 3DS, OBJ, STL, U3D, glTF, PLY, X, dan secara opsional FBX.  
- **Apakah saya memerlukan lisensi untuk mencoba ini?** Lisensi sementara diperlukan untuk fungsi penuh; versi percobaan gratis juga tersedia.  
- **Apakah ada data tambahan yang diperlukan?** Anda mungkin perlu menyediakan jalur pencarian untuk sumber eksternal seperti tekstur atau perpustakaan material.  
- **Di mana saya dapat menemukan versi terbaru Aspose.3D untuk Java?** Pada halaman unduhan resmi yang ditautkan di bawah.

## Apa itu “customize 3d loading java”?

Menyesuaikan pemuatan 3D di Java memungkinkan Anda menentukan bagaimana mesin Aspose.3D menafsirkan file yang masuk. Dengan menyesuaikan properti pada berbagai kelas `*LoadOptions`, Anda dapat:

* Membalik sistem koordinat agar cocok dengan pipeline rendering Anda.  
* Mengaktifkan atau menonaktifkan pemuatan material untuk skenario yang memerlukan kinerja tinggi.  
* Menerapkan koreksi gamma, transformasi animasi, atau mempertahankan pengaturan global bawaan untuk file FBX.  

## Mengapa menggunakan Aspose.3D LoadOptions?

* **Kontrol halus** – Sesuaikan setiap format secara independen.  
* **Konsistensi lintas‑format** – Terapkan aturan sistem koordinat yang sama pada semua tipe file yang didukung.  
* **Optimisasi kinerja** – Lewati data yang tidak diperlukan (misalnya, material) bila tidak dibutuhkan.  

## Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- Pemahaman yang kuat tentang dasar‑dasar Java.  
- JDK 8 atau yang lebih tinggi terpasang.  
- Perpustakaan Aspose.3D untuk Java yang diunduh dari situs resmi — Anda dapat memperolehnya [di sini](https://releases.aspose.com/3d/java/).  
- Familiaritas dasar dengan format file 3D yang akan Anda gunakan (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX).

## Impor Paket

Di proyek Java Anda, impor kelas inti Aspose.3D dan paket I/O standar:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Sesuaikan Pemuatan File 3D

Berikut ini Anda akan menemukan metode khusus untuk setiap format yang didukung. Setiap potongan kode menampilkan penyesuaian yang paling umum; silakan ubah properti sesuai kebutuhan pipeline Anda.

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

*Mengapa ini penting:* Mengaktifkan `ApplyAnimationTransform` memastikan bahwa data animasi yang tertanam menghormati sistem koordinat target, sementara `GammaCorrectedColor` memperbaiki masalah intensitas warna yang sering muncul saat berpindah antar mesin rendering.

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

*Tip:* Jika Anda memuat file OBJ yang merujuk ke file material `.mtl` eksternal, biarkan `EnableMaterials` bernilai `true` dan pastikan jalur pencarian mengarah ke folder yang berisi file‑file tersebut.

### Langkah 3: Sesuaikan Pemuatan File STL  

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

*Pro tip:* File STL hanya berisi geometri, jadi biasanya satu‑satunya penyesuaian yang diperlukan adalah membalik sistem koordinat.

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

*Mengapa membalik koordinat V tekstur?* Banyak pengekspor glTF menggunakan asal UV yang berbeda dari pipeline DirectX tradisional; membalik `TexCoordV` menyelaraskan tekstur dengan benar.

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

*Kapan menggunakan ini:* File FBX sering menyertakan pengaturan global (unit, sumbu‑up). Mempertahankannya memastikan adegan yang diimpor cocok dengan niat penulis asli.

## Masalah Umum dan Solusinya

| Masalah | Penyebab Kemungkinan | Solusi |
|-------|---------------|-----|
| Tekstur tidak muncul | Jalur pencarian tidak diset atau sensitivitas huruf besar/kecil salah | Tambahkan direktori yang tepat ke `loadOpts.getLookupPaths()` dan verifikasi nama file |
| Model muncul terbalik | `FlipCoordinateSystem` tidak diaktifkan untuk format tersebut | Setel `setFlipCoordinateSystem(true)` pada `*LoadOptions` yang relevan |
| Warna tampak pudar | Koreksi gamma tidak diaktifkan untuk 3DS | Panggil `setGammaCorrectedColor(true)` pada `Discreet3dsLoadOptions` |
| Animasi FBX terlihat salah | Pengaturan global ditimpa | Gunakan `setKeepBuiltinGlobalSettings(true)` |

## Pertanyaan yang Sering Diajukan

### Q1: Di mana saya dapat menemukan dokumentasi Aspose.3D untuk Java?  
A1: Dokumentasi tersedia [di sini](https://reference.aspose.com/3d/java/).

### Q2: Bagaimana cara mengunduh Aspose.3D untuk Java?  
A2: Anda dapat mengunduhnya [di sini](https://releases.aspose.com/3d/java/).

### Q3: Apakah ada versi percobaan gratis?  
A3: Ya, Anda dapat mengakses percobaan gratis [di sini](https://releases.aspose.com/).

### Q4: Di mana saya dapat mendapatkan dukungan untuk Aspose.3D untuk Java?  
A4: Kunjungi forum dukungan [di sini](https://forum.aspose.com/c/3d/18).

### Q5: Apakah saya memerlukan lisensi sementara untuk pengujian?  
A5: Ya, dapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

### Q6: Bisakah saya memuat beberapa format dalam satu adegan?  
A6: Tentu saja. Buat `LoadOptions` terpisah untuk setiap format dan panggil `scene.open()` untuk masing‑masing file; adegan akan menggabungkan geometri.

### Q7: Bagaimana cara meningkatkan kinerja pemuatan untuk file besar?  
A7: Nonaktifkan fitur yang tidak diperlukan (misalnya, pemuatan material untuk STL) dan gunakan `LookupPaths` untuk menghindari I/O berulang.

### Q8: Apakah mungkin mengubah sistem koordinat secara programatis setelah pemuatan?  
A8: Ya, Anda dapat memanggil `scene.getRootNode().rotate()` atau `scene.getRootNode().scale()` setelah file dibuka.

**Terakhir Diperbarui:** 2025-12-19  
**Diuji Dengan:** Aspose.3D for Java 24.11 (versi terbaru pada saat penulisan)  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}