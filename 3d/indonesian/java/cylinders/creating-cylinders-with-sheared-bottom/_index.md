---
date: 2025-12-09
description: Pelajari cara menggunakan Aspose untuk membuat silinder yang disesuaikan
  dengan dasar miring di Java, sempurna untuk pemodelan 3D Java dan menyimpan adegan
  sebagai OBJ.
language: id
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 'Cara Menggunakan Aspose: Membuat Silinder dengan Dasar Miring di Java'
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Menggunakan Aspose: Membuat Silinder dengan Dasar Miring di Java

## Pendahuluan

Dalam tutorial praktis ini Anda akan menemukan **cara menggunakan Aspose** untuk membuat sebuah silinder yang dasar nya dimiringkan—sebuah teknik yang sering dibutuhkan dalam proyek *pemodelan 3d java*. Kami akan memandu Anda melalui setiap langkah, mulai dari menyiapkan scene hingga menyimpan model akhir sebagai file OBJ. Pada akhir tutorial, Anda akan memiliki potongan kode yang dapat digunakan kembali dan dapat disisipkan ke dalam aplikasi 3D berbasis Java mana pun.

## Jawaban Cepat
- **Apa arti “shear bottom”?** Itu memiringkan dasar silinder dengan sudut tertentu pada bidang XY.  
- **Perpustakaan mana yang menangani matematika 3D?** Aspose.3D untuk Java menyediakan kelas `Cylinder` dan `Vector2`.  
- **Apakah saya memerlukan lisensi untuk menjalankan contoh ini?** Lisensi sementara cukup untuk evaluasi; lisensi penuh diperlukan untuk produksi.  
- **Bisakah saya mengekspor model ke format lain?** Ya—gunakan `scene.save(..., FileFormat.WAVEFRONTOBJ)` untuk mendapatkan file OBJ.  
- **Versi Java apa yang dibutuhkan?** JDK 8 atau yang lebih baru sudah cukup.

## Apa arti “cara menggunakan aspose” dalam konteks pemodelan 3D?

Aspose.3D untuk Java adalah API tingkat tinggi yang menyederhanakan kompleksitas geometri 3D, format file, dan transformasi. Alih-alih berurusan dengan buffer vertex tingkat rendah, Anda memanggil metode intuitif seperti `new Cylinder(...)` dan membiarkan Aspose menangani pekerjaan berat.

## Mengapa menggunakan Aspose untuk Pemodelan 3D Java?

- **Pengembangan cepat:** Bangun bentuk kompleks dengan beberapa baris kode.  
- **Dukungan format luas:** Ekspor ke OBJ, STL, FBX, dan lainnya.  
- **Lintas‑platform:** Berfungsi pada sistem operasi apa pun yang mendukung Java.  
- **API konsisten:** Kode yang sama bekerja untuk desktop, server, atau lingkungan Android.

## Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- **Java Development Kit (JDK) 8+** terpasang dan terkonfigurasi di IDE Anda.  
- **Perpustakaan Aspose.3D untuk Java** yang ditambahkan ke classpath proyek Anda. Anda dapat mengunduhnya dari situs resmi [di sini](https://releases.aspose.com/3d/java/).  
- **Lisensi sementara atau penuh** (opsional untuk percobaan).

## Mengimpor Paket

Untuk memulai, impor kelas Aspose.3D yang penting serta utilitas Java:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Membuat Scene

*Scene* adalah wadah yang menampung semua objek 3D, cahaya, dan kamera. Anggaplah ini sebagai panggung tempat Anda menempatkan silinder.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Langkah 2: Membuat Silinder 1 (Dasar Miring)

Sekarang kita akan membuat silinder pertama dan menerapkan transformasi shear pada dasarnya. Metode `setShearBottom` menerima sebuah `Vector2` dimana komponen X mewakili faktor shear sepanjang sumbu X dan komponen Y sepanjang sumbu Y.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

> **Tips pro:** Faktor shear `0.83` kira‑kira setara dengan 47,5°; sesuaikan nilai ini untuk mendapatkan sudut yang tepat sesuai kebutuhan Anda.

## Langkah 3: Membuat Silinder 2 (Standar)

Sebagai perbandingan, kita akan menambahkan silinder kedua tanpa shear. Ini membantu Anda melihat perbedaan visual secara langsung pada file OBJ yang diekspor.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Langkah 4: Menyimpan Scene (Cara Menyimpan Scene sebagai OBJ)

Akhirnya, kita menyimpan scene ke disk. Konstanta `FileFormat.WAVEFRONTOBJ` memberi tahu Aspose untuk menulis file OBJ, yang didukung secara luas oleh editor 3D seperti Blender dan Maya.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Catatan:** Ganti `"Your Document Directory"` dengan jalur absolut atau relatif yang sesuai untuk lingkungan Anda.

## Masalah Umum dan Solusinya

| Masalah | Penyebab | Solusi |
|-------|-------|----------|
| **Silinder terlihat datar** | Faktor shear tidak tepat (di luar rentang 0‑1) | Gunakan nilai antara 0 dan 1; sesuaikan secara bertahap sambil melakukan pratinjau. |
| **File OBJ tidak dapat dimuat di viewer** | Definisi material yang hilang | Tambahkan material sederhana ke setiap node atau ekspor sebagai STL untuk pengujian hanya geometri. |
| **LicenseException saat runtime** | Tidak ada file lisensi yang valid | Letakkan `Aspose.3D.lic` di root proyek atau gunakan kelas `License` untuk memuatnya secara programatik. |

## Pertanyaan yang Sering Diajukan

### Q1: Bisakah saya menggunakan Aspose.3D untuk Java bersama perpustakaan 3D Java lainnya?
**A:** Aspose.3D untuk Java dirancang untuk bekerja secara mandiri. Meskipun Anda dapat mengintegrasikannya dengan perpustakaan lain, ia menyediakan rangkaian fitur lengkap untuk sebagian besar tugas pemodelan 3D secara sendiri.

### Q2: Apakah Aspose.3D cocok untuk pemula dalam pemodelan 3D?
**A:** Ya, Aspose.3D menawarkan API yang ramah pengguna yang menyederhanakan detail tingkat rendah, sehingga dapat diakses baik oleh pemula maupun pengembang berpengalaman.

### Q3: Di mana saya dapat menemukan dukungan tambahan untuk Aspose.3D untuk Java?
**A:** Kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas, tutorial, dan diskusi.

### Q4: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?
**A:** Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

### Q5: Bisakah saya membeli Aspose.3D untuk Java?
**A:** Ya, Anda dapat membeli Aspose.3D untuk Java [di sini](https://purchase.aspose.com/buy).

## Kesimpulan

Kami telah membahas **cara menggunakan Aspose** untuk membuat dua silinder—satu dengan dasar miring dan satu standar—kemudian menyimpan hasilnya sebagai file OBJ. Teknik ini merupakan blok bangunan untuk model 3D yang lebih canggih, seperti bagian khusus, elemen arsitektural, atau aset game. Jangan ragu untuk bereksperimen dengan nilai shear, radius, dan tinggi yang berbeda agar sesuai dengan kebutuhan proyek Anda.

---

**Terakhir Diperbarui:** 2025-12-09  
**Diuji Dengan:** Aspose.3D untuk Java 24.11 (versi terbaru saat penulisan)  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}