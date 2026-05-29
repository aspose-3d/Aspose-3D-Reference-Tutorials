---
date: 2026-04-03
description: Pelajari cara membuat bentuk kipas silinder di Java dengan Aspose.3D.
  Panduan ini mencakup pemodelan 3D Java dan teknik menyimpan file OBJ di Java.
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
linktitle: Cara membuat bentuk kipas silinder menggunakan Aspose.3D untuk Java
second_title: Aspose.3D Java API
title: Cara membuat bentuk kipas silinder menggunakan Aspose.3D untuk Java
url: /id/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara membuat bentuk kipas silinder menggunakan Aspose.3D untuk Java

## Pendahuluan

Siap menguasai **cara membuat bentuk kipas silinder** dalam lingkungan Java? Dalam tutorial ini kami akan membahas setiap langkah— mulai dari menyiapkan scene hingga mengekspor file Wavefront OBJ— menggunakan Aspose.3D. Baik Anda sedang membuat aset game, prototipe CAD, atau sekadar bereksperimen dengan geometri 3D, Anda akan melihat betapa mudahnya pemodelan 3D Java dengan pustaka yang kuat ini.

## Jawaban Cepat
- **Apa tujuan utama?** Membuat silinder berbentuk kipas yang dapat disesuaikan dan menyimpannya sebagai file OBJ.  
- **Pustaka mana yang digunakan?** Aspose.3D untuk Java.  
- **Apakah saya memerlukan lisensi?** Versi percobaan gratis dapat digunakan untuk pengembangan; lisensi komersial diperlukan untuk produksi.  
- **Apa prasyaratnya?** JDK terpasang dan paket Aspose.3D Java ditambahkan ke proyek Anda.  
- **Bisakah saya mengekspor format lain?** Ya—Aspose.3D mendukung banyak format; contoh ini menggunakan Wavefront OBJ.

## Apa itu Silinder Kipas?

Silinder kipas adalah silinder permukaan parsial di mana sebuah sektor dari basis melingkar dihilangkan, menghasilkan bukaan “kipas”. Geometri ini berguna untuk memvisualisasikan irisan, dasbor, atau bagian mekanik khusus.

## Mengapa menggunakan Aspose.3D untuk pemodelan 3D Java?

Aspose.3D menyediakan API yang bersih dan berorientasi objek yang mengabstraksi matematika tingkat rendah dari grafik 3D. Anda dapat fokus pada desain daripada keanehan format file, dan pustaka ini menangani operasi **save obj file java** secara otomatis.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- **Java Development Kit (JDK)** – unduh di [sini](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – dapatkan JAR terbaru dari [tautan unduhan](https://releases.aspose.com/3d/java/).  

Tambahkan JAR Aspose.3D ke classpath proyek Anda.

## Impor Paket

Mulailah dengan mengimpor kelas yang diperlukan. Ini memberi Anda akses ke scene 3D, primitif geometri, dan metode utilitas.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Membuat Scene

Pertama, kita membuat instance baru `Scene`. Anggap scene sebagai wadah yang menampung semua objek 3D, cahaya, dan kamera Anda.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Langkah 2: Membuat Silinder Kipas (cara membuat silinder)

Sekarang kita membangun silinder kipas itu sendiri. Parameter konstruktor menentukan radius, tinggi, tessellation, dan apakah geometri dihasilkan sebagai kipas.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Pro tip:** Sesuaikan `setThetaLength` untuk mengubah sudut bukaan. 270° menghasilkan kipas tiga perempat; 180° akan menghasilkan setengah silinder.

## Langkah 3: Menempatkan Silinder Kipas

Selanjutnya, kita menambahkan silinder kipas ke scene dan memindahkannya ke lokasi yang nyaman. Koordinat translasi berada dalam urutan (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Langkah 4: Membuat Silinder Non‑Kipas (perbandingan pemodelan 3D Java)

Untuk mengilustrasikan fleksibilitas Aspose.3D, kami juga membuat silinder biasa tanpa bukaan kipas.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Langkah 5: Menyimpan Scene (java save obj file)

Akhirnya, kami mengekspor seluruh scene ke file Wavefront OBJ. Format ini didukung secara luas oleh sebagian besar editor 3D dan mesin game.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Catatan:** Ganti `"Your Document Directory"` dengan jalur absolut atau relatif di mana Anda memiliki izin menulis.

## Cara menyimpan file OBJ di Java menggunakan Aspose 3D

Metode `Scene.save` Aspose.3D secara otomatis menangani proses **aspose 3d export obj**. Anda hanya perlu menentukan nama file target dan nilai enum `FileFormat.WAVEFRONTOBJ`, seperti yang ditunjukkan pada langkah sebelumnya.

## Masalah Umum dan Solusinya

| Masalah | Alasan | Solusi |
|-------|--------|-----|
| File OBJ kosong | Scene tidak disimpan atau path tidak benar | Verifikasi direktori output ada dan memiliki izin menulis. |
| Bukaan kipas terlihat salah | Nilai `ThetaLength` tidak tepat | Gunakan `MathUtils.toRadian(degrees)` untuk mengatur sudut tepat yang Anda butuhkan. |
| Kesalahan kompilasi | JAR Aspose.3D tidak ada di classpath | Tambahkan JAR ke folder `libs` proyek Anda dan sertakan dalam path build. |

## Pertanyaan yang Sering Diajukan

**Q: Apakah Aspose.3D kompatibel dengan pustaka Java 3D lainnya?**  
A: Ya, Aspose.3D dapat berkoeksistensi dengan pustaka seperti Java 3D atau jMonkeyEngine, memungkinkan Anda mengintegrasikan geometri khusus ke dalam pipeline yang lebih besar.

**Q: Bisakah saya lebih lanjut menyesuaikan tampilan silinder kipas?**  
A: Tentu saja. Anda dapat menerapkan material, tekstur, dan pencahayaan dengan mengakses koleksi `Material` dan `Light` pada node.

**Q: Di mana saya dapat memperoleh dukungan tambahan?**  
A: Kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk bantuan komunitas dan respons resmi.

**Q: Apakah tersedia versi percobaan gratis?**  
A: Ya, Anda dapat menjelajahi Aspose.3D dengan [versi percobaan gratis](https://releases.aspose.com/) sebelum membeli.

**Q: Bagaimana cara mendapatkan lisensi sementara untuk pengujian?**  
A: Dapatkan satu [di sini](https://purchase.aspose.com/temporary-license/) untuk membuka semua fungsi selama pengembangan.

---

**Terakhir Diperbarui:** 2026-04-03  
**Diuji Dengan:** Aspose.3D 24.11 for Java  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}