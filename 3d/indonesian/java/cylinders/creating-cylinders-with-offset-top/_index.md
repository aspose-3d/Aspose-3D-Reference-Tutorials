---
date: 2025-12-05
description: Pelajari cara membuat model silinder dengan bagian atas yang teroffset
  di Aspose.3D untuk Java, tambahkan langkah-langkah node anak Java, dan ekspor file
  model 3D OBJ dengan mudah.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cara Membuat Silinder dengan Bagian Atas Teroffset di Aspose.3D untuk Java
url: /id/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Membuat Silinder dengan Offset Top di Aspose.3D untuk Java

## Pendahuluan

Jika Anda ingin **cara membuat silinder** dengan offset top khusus dalam adegan 3D berbasis Java, Aspose.3D membuat prosesnya sederhana. Dalam tutorial ini kami akan membahas setiap langkah—dari menyiapkan scene hingga mengekspor model akhir sebagai file OBJ—sehingga Anda dapat mengintegrasikan silinder dengan offset‑top ke dalam aplikasi Anda dengan percaya diri.

## Jawaban Cepat
- **Apa perpustakaan yang digunakan?** Aspose.3D for Java  
- **Apakah saya dapat mengoffset bagian atas silinder?** Ya, menggunakan `setOffsetTop`  
- **Bagaimana cara menambahkan child node di Java?** Panggil `createChildNode` pada node root  
- **Format apa yang dapat saya ekspor?** Wavefront OBJ (`export 3d model obj`)  
- **Apakah saya memerlukan lisensi untuk pengujian?** Lisensi sementara tersedia untuk evaluasi  

## Apa itu “cara membuat silinder” dengan offset top?

Membuat silinder dengan offset top berarti permukaan melingkar bagian atas digeser relatif terhadap dasar, memungkinkan Anda memodelkan bentuk menipis atau asimetris tanpa manipulasi vertex manual. Aspose.3D menyediakan konstruktor khusus dan properti `OffsetTop` untuk mencapai hal ini dalam beberapa baris kode saja.

## Mengapa menggunakan Aspose.3D untuk Java?

- **API tingkat tinggi:** Tidak perlu mengelola data mesh tingkat rendah.  
- **Cross‑platform:** Berfungsi pada lingkungan yang kompatibel dengan JVM apa pun.  
- **Ekspor bawaan:** Simpan langsung ke OBJ, STL, FBX, dan lainnya.  
- **Dapat diperluas:** Mudah menambahkan child node, menerapkan transformasi, dan mengintegrasikan dengan perpustakaan Java lainnya.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- **Java Development Kit (JDK)** – versi yang kompatibel terpasang.  
- **Aspose.3D for Java library** – unduh JAR terbaru dari situs resmi [di sini](https://releases.aspose.com/3d/java/).  
- IDE pilihan Anda (Eclipse, IntelliJ IDEA, NetBeans, dll.).

## Impor Paket

Pertama, impor kelas‑kelas yang diperlukan. Letakkan pernyataan ini di bagian atas file Java Anda:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Panduan Langkah‑per‑Langkah

### Langkah 1: Buat Scene

Scene berfungsi sebagai wadah untuk semua objek 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Langkah 2: Inisialisasi Silinder dengan Offset Top

Di sini kami menjawab **cara membuat silinder** dengan offset khusus. Konstruktor mendefinisikan radius, tinggi, slices, stacks, dan apakah silinder ditutup. Setelah itu, kami menggeser bagian atas menggunakan `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Langkah 3: Cara **menambahkan child node Java** – Lampirkan Silinder Pertama

Kami membuat child node di bawah node root scene dan memindahkan silinder ke lokasi yang diinginkan.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Langkah 4: Inisialisasi Silinder Kedua (Tanpa Offset)

Untuk perbandingan, kami menambahkan silinder biasa tanpa offset.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Langkah 5: Cara **menambahkan child node Java** – Lampirkan Silinder Kedua

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Langkah 6: Cara **mengekspor model 3d OBJ** – Simpan Scene

Akhirnya, kami mengekspor seluruh scene (kedua silinder) sebagai file Wavefront OBJ, yang didukung secara luas oleh alat‑alat 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Saat Anda menjalankan program, Anda akan menemukan `CustomizedOffsetTopCylinder.obj` di direktori yang ditentukan, siap dibuka di Blender, Maya, atau penampil OBJ lainnya.

## Masalah Umum dan Solusinya

| Masalah | Penyebab | Solusi |
|-------|--------|-----|
| **File OBJ kosong** | Scene tidak disimpan dengan benar atau path salah. | Pastikan direktori output ada dan Anda memiliki izin menulis. |
| **Offset tidak diterapkan** | Menggunakan versi Aspose.3D yang lebih lama. | Perbarui ke perpustakaan terbaru yang mendukung `setOffsetTop`. |
| **Child node tidak terlihat** | Transformasi tidak diterapkan. | Pastikan Anda memanggil `getTransform().setTranslation` setelah membuat child node. |

## Pertanyaan yang Sering Diajukan

**Q: Apakah Aspose.3D kompatibel dengan berbagai IDE Java?**  
A: Ya, bekerja mulus dengan Eclipse, IntelliJ IDEA, NetBeans, dan IDE lainnya.

**Q: Apakah saya dapat menerapkan tekstur pada objek 3D yang dibuat?**  
A: Tentu! Gunakan kelas `Material` untuk menetapkan tekstur dan properti permukaan.

**Q: Apakah ada opsi lisensi untuk Aspose.3D?**  
A: Berbagai model lisensi tersedia; Anda dapat menjelajahinya [di sini](https://purchase.aspose.com/buy).

**Q: Bagaimana saya dapat mendapatkan bantuan atau berbagi pengalaman?**  
A: Bergabunglah dengan forum komunitas Aspose.3D [di sini](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi.

**Q: Apakah lisensi sementara tersedia untuk pengujian?**  
A: Ya, lisensi sementara dapat diperoleh untuk evaluasi [di sini](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Terakhir Diperbarui:** 2025-12-05  
**Diuji Dengan:** Aspose.3D for Java 24.12 (latest)  
**Penulis:** Aspose