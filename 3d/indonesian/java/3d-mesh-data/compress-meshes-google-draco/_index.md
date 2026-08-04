---
date: 2026-04-29
description: Pelajari cara mengurangi ukuran model 3D dengan membuat mesh bola di
  Java dan mengompresnya menggunakan Google Draco dengan Aspose.3D – penting untuk
  ekspor Aspose 3D.
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: Cara Membuat Mesh Bola di Java – Kompres Mesh 3D dengan Google Draco
second_title: Aspose.3D Java API
title: 'Kurangi Ukuran Model 3D: Buat Mesh Bola di Java dengan Draco'
url: /id/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Kurangi Ukuran Model 3D: Buat Mesh Bola di Java dengan Draco

## Pendahuluan

Jika Anda mencari cara cepat untuk **mengurangi ukuran model 3D** sambil tetap menghasilkan geometri berkualitas tinggi, Anda berada di tempat yang tepat. Dalam tutorial ini kami akan menjelaskan cara membuat mesh bola dengan **Aspose.3D for Java** dan kemudian mengompres mesh tersebut menggunakan **Google Draco**. Pada akhir tutorial Anda akan memiliki file `.drc` siap pakai yang jauh lebih kecil daripada yang asli, menjadikannya sempurna untuk penampil berbasis web, game seluler, atau aplikasi Java dengan keterbatasan bandwidth.

## Jawaban Cepat
- **Apa yang dibahas dalam tutorial ini?** Membuat mesh bola di Java dan mengompresnya dengan Google Draco melalui Aspose.3D.  
- **Perpustakaan utama?** Aspose.3D for Java (digunakan untuk pembuatan mesh dan ekspor Draco).  
- **Waktu implementasi typical?** Sekitar 10‑15 menit untuk bola dasar.  
- **Prasyarat utama?** Lingkungan pengembangan Java dengan JAR Aspose.3D di classpath.  
- **Hasil?** File `.drc` yang **mengurangi ukuran model 3D** hingga 90 % dibandingkan mesh yang tidak terkompresi.

## Apa itu “mengurangi ukuran model 3D” dalam konteks pengembangan 3D?

Mengurangi ukuran model 3D berarti memperkecil jumlah data geometri yang perlu ditransfer atau disimpan, tanpa secara signifikan menurunkan kualitas visual. Draco mencapai ini dengan mengkodekan posisi vertex, normal, dan atribut lainnya dalam format biner yang sangat kompak. Ketika dipasangkan dengan Aspose.3D, seluruh alur kerja tetap berada di dalam Java, sehingga Anda tidak perlu mengelola binary native.

## Mengapa menggunakan kompresi mesh Google Draco dengan Aspose.3D?

- **Pengurangan ukuran yang besar:** Draco dapat memotong data mesh hingga 90 % dibandingkan format seperti OBJ atau STL.  
- **Dekoding runtime cepat:** Mesin seperti Unity, Unreal, dan three.js dapat mendekode Draco secara native, menghasilkan waktu muat yang lebih cepat.  
- **Integrasi Java yang mulus:** Aspose.3D mengabstraksi pustaka Draco native, memungkinkan Anda tetap berada di ekosistem Java.  
- **Ekspor Aspose 3D satu pintu:** API yang sama yang Anda gunakan untuk membuat geometri juga menangani ekspor, menyederhanakan alur kerja.

## Prasyarat

- **Java Development Kit (JDK)** – versi 8 atau lebih baru.  
- **Aspose.3D for Java** – unduh JAR terbaru dari halaman resmi [di sini](https://releases.aspose.com/3d/java/).  
- **Pemahaman dasar tentang Google Draco** – Anda akan menggunakan wrapper Aspose.3D, jadi tidak diperlukan pengaturan Draco native.

## Impor Paket

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Panduan Langkah‑per‑Langkah

### Langkah 1: Siapkan Proyek

Buat proyek Java baru (IDE apa pun dapat digunakan) dan tambahkan semua JAR Aspose.3D ke classpath. Simpan file sumber Anda dalam paket seperti `com.example.draco` untuk kejelasan.

### Langkah 2: Cara Membuat Mesh Bola di Java

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **Tip Pro:** Kelas `Sphere` menghasilkan mesh segitiga dengan radius default 1.0. Anda dapat memberikan radius khusus, tessellation, atau parameter material jika membutuhkan tingkat detail yang berbeda sebelum kompresi.

### Langkah 3: Cara Mengompres Mesh dengan Google Draco

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

Menetapkan level kompresi ke `OPTIMAL` memberikan pengurangan ukuran terbesar sambil mempertahankan fidelitas visual, secara langsung membantu Anda **mengurangi ukuran model 3D**.

### Langkah 4: Simpan Mesh yang Dikompres

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

File `SphereMeshtoDRC_Out.drc` yang dihasilkan dapat di-stream ke klien, disimpan di CDN, atau dimuat langsung oleh mesin apa pun yang kompatibel dengan Draco.

## Kasus Penggunaan Umum

| Skenario | Mengapa Mengurangi Ukuran Model? | Bagaimana Tutorial Ini Membantu |
|----------|--------------------------------|---------------------------------|
| Konfigurator produk berbasis web | Memuat halaman lebih cepat pada koneksi lambat | File `.drc` terkompresi Draco dimuat dalam hitungan detik |
| Aplikasi AR/VR seluler | Jejak memori lebih rendah pada perangkat | Mesh yang lebih kecil menjaga responsivitas aplikasi |
| Adegan yang dirender di cloud | Mengurangi biaya bandwidth | Ekspor satu klik dari Aspose.3D ke Draco |

## Masalah Umum dan Solusinya

| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| **`NoClassDefFoundError` untuk kelas Draco** | JAR Aspose.3D tidak ada di classpath | Pastikan *semua* file JAR Aspose.3D disertakan dan versinya cocok dengan dokumentasi. |
| **File output kosong** | `MyDir` mengarah ke folder yang tidak ada | Buat direktori secara programatis (`Files.createDirectories(Paths.get(MyDir))`) sebelum menulis file. |
| **Mesh terkompresi tampak terdistorsi** | Menggunakan level kompresi rendah atau tessellation tidak cukup | Ganti ke `DracoCompressionLevel.OPTIMAL` dan tingkatkan tessellation bola (mis., `new Sphere(1.0, 64, 64)`). |

## Pertanyaan yang Sering Diajukan

**Q: Apakah Aspose.3D kompatibel dengan berbagai format file 3D?**  
A: Ya, Aspose.3D mendukung OBJ, FBX, STL, GLTF, dan banyak lainnya, menjadikannya pilihan serbaguna untuk pipeline **ekspor Aspose 3D**.

**Q: Bisakah saya menggunakan Google Draco untuk kompresi dalam bahasa pemrograman lain?**  
A: Tentu saja. Draco menyediakan pustaka native untuk C++, Python, dan JavaScript. Tutorial ini berfokus pada Java, tetapi konsepnya berlaku lintas bahasa.

**Q: Di mana saya dapat menemukan dokumentasi Aspose.3D tambahan?**  
A: Kunjungi [dokumentasi Aspose.3D Java](https://reference.aspose.com/3d/java/) untuk referensi API lengkap dan contoh lebih banyak.

**Q: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?**  
A: Jelajahi opsi lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

**Q: Apakah ada forum komunitas untuk dukungan Aspose.3D?**  
A: Ya, bergabunglah dalam diskusi di [Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

## Kesimpulan

Dalam panduan ini kami menunjukkan cara **mengurangi ukuran model 3D** dengan membuat mesh bola di Java dan kemudian mengompresnya dengan Google Draco melalui Aspose.3D. Dengan mengikuti langkah-langkah singkat ini Anda dapat memangkas file mesh secara dramatis, meningkatkan waktu muat, dan menjaga aplikasi 3D berbasis Java Anda tetap responsif serta ramah bandwidth.

---

**Last Updated:** 2026-04-29  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}