---
date: 2026-03-13
description: Pelajari cara membuat silinder 3D, kotak, dan model primitif lainnya
  menggunakan Aspose.3D untuk Java dan menyimpan adegan sebagai FBX.
linktitle: Building Primitive 3D Models with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cara membuat silinder 3D dan model 3D primitif lainnya dengan Aspose.3D untuk
  Java
url: /id/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Membuat Model 3D Primitive dengan Aspose.3D untuk Java

## Pendahuluan

Jika Anda pernah perlu **membuat objek 3D cylinder** (atau bentuk dasar lainnya) langsung dari kode Java, Aspose.3D membuat tugas ini menjadi mudah. Dalam tutorial ini kami akan membahas seluruh alur kerja—dari menyiapkan lingkungan hingga menyimpan scene akhir sebagai file FBX—sehingga Anda dapat mulai menghasilkan geometri 3D secara programatis segera.

## Jawaban Cepat
- **Perpustakaan apa yang memungkinkan saya membuat 3D cylinder di Java?** Aspose.3D for Java.
- **Format apa yang dapat saya ekspor scene?** FBX (ASCII 7500) menggunakan `FileFormat.FBX7500ASCII`.
- **Apakah saya memerlukan lisensi untuk pengembangan?** Versi percobaan gratis dapat digunakan untuk pengujian; lisensi permanen diperlukan untuk produksi.
- **Apa saja primitif utama yang didukung?** Box, Cylinder, Sphere, Cone, dan lainnya.
- **Apakah kode kompatibel dengan Java 8 dan versi lebih baru?** Ya, Aspose.3D menargetkan JDK 8+.

## Apa itu primitif 3D cylinder?

Primitif cylinder adalah bentuk geometris dasar yang didefinisikan oleh radius dan tinggi. Dalam banyak pipeline 3D, ia berfungsi sebagai blok bangunan untuk model yang lebih kompleks seperti pipa, roda, atau kolom arsitektural. Aspose.3D menyediakan kelas `Cylinder` siap pakai, sehingga Anda tidak perlu menghitung vertex secara manual.

## Mengapa menggunakan Aspose.3D untuk Java?

- **Mesin 3D lengkap** – mendukung impor/ekspor format populer (FBX, OBJ, STL, dll.).
- **API Java murni** – tanpa ketergantungan native, sempurna untuk proyek lintas platform.
- **Grafik scene yang kuat** – memungkinkan Anda mengatur objek secara hierarkis.
- **Lisensi mudah** – mulai dengan percobaan gratis, kemudian tingkatkan ke lisensi permanen.

## Prasyarat

Sebelum menyelam ke kode, pastikan Anda memiliki:

1. **Java Development Kit (JDK)** – JDK 8 atau yang lebih baru terpasang di mesin Anda.  
2. **Perpustakaan Aspose.3D untuk Java** – unduh dan instal dari [halaman unduhan](https://releases.aspose.com/3d/java/).  

## Mengimpor Paket

Mulailah dengan mengimpor namespace inti Aspose.3D. Ini memberi Anda akses ke `Scene`, `Box`, `Cylinder`, dan konstanta format file.

```java
import com.aspose.threed.*;
```

Setelah perpustakaan direferensikan, mari buat scene dan tambahkan beberapa geometri primitif.

## Cara membuat 3D cylinder dan primitif lainnya dalam sebuah scene

### Langkah 1: Inisialisasi Objek Scene

Pertama, kita memerlukan kontainer `Scene` yang akan menampung semua node 3D kita.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Langkah 2: Bangun model kotak 3D

Primitif kotak berguna untuk menguji sistem koordinat. Di sini kami menambahkannya sebagai anak dari node akar scene.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Langkah 3: Buat model 3D cylinder

Sekarang kami benar‑benarnya **membuat geometri 3D cylinder**. Kelas `Cylinder` memiliki dimensi default yang masuk akal, tetapi Anda dapat menyesuaikan radius dan tinggi melalui konstruktornya jika diperlukan.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Langkah 4: Simpan gambar dalam format FBX

Setelah menyusun scene, ekspor sehingga alat lain (misalnya Unity, Blender) dapat membacanya. Kami menggunakan format `FBX7500ASCII`, yang didukung secara luas.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|---------|----------------|--------|
| **File tidak ditemukan** saat menyimpan | `myDir` mengarah ke folder yang tidak ada | Pastikan direktori ada atau buat dengan `new File(myDir).mkdirs();` |
| **Scene kosong** setelah ekspor | Tidak ada node yang ditambahkan sebelum memanggil `save` | Verifikasi bahwa panggilan `createChildNode` dijalankan (debug dengan `scene.getRootNode().getChildCount()` ) |
| **Pengecualian lisensi** | Menjalankan tanpa lisensi yang valid di produksi | Terapkan lisensi sementara atau permanen menggunakan `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Pertanyaan yang Sering Diajukan

**T: Bisakah saya menggunakan Aspose.3D untuk Java dengan bahasa pemrograman lain?**  
J: Aspose.3D terutama mendukung Java, tetapi ada versi yang tersedia untuk bahasa lain seperti .NET.

**T: Apakah Aspose.3D cocok untuk tugas pemodelan 3D yang kompleks?**  
J: Tentu saja! Aspose.3D menyediakan rangkaian fitur lengkap, sehingga cocok untuk tugas pemodelan 3D sederhana maupun kompleks.

**T: Di mana saya dapat menemukan bantuan dan dukungan tambahan?**  
J: Kunjungi [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas dan diskusi.

**T: Bisakah saya mencoba Aspose.3D sebelum membeli?**  
J: Ya, Anda dapat menjelajahi [versi percobaan gratis](https://releases.aspose.com/) sebelum memutuskan pembelian.

**T: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?**  
J: Anda dapat memperoleh [lisensi sementara](https://purchase.aspose.com/temporary-license/) untuk Aspose.3D melalui situs web.

## Kesimpulan

Anda kini telah mempelajari cara **membuat 3D cylinder**, kotak, dan model primitif lainnya menggunakan Aspose.3D untuk Java, serta cara **menyimpan scene sebagai FBX** untuk penggunaan selanjutnya. Silakan bereksperimen dengan primitif lain (Sphere, Cone, dll.) dan jelajahi penugasan material untuk memberi model Anda tampilan yang realistis.

---

**Last Updated:** 2026-03-13  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}