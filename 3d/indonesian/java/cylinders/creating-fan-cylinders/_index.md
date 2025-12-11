---
date: 2025-12-09
description: Pelajari cara menambahkan node anak, memposisikan objek 3D, dan menyimpan
  adegan sebagai OBJ sambil membuat silinder kipas khusus menggunakan Aspose.3D untuk
  Java.
language: id
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Tambahkan Node Anak untuk Membuat Silinder Kipas dengan Aspose.3D untuk Java
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tambahkan Child Node untuk Membuat Silinder Kipas dengan Aspose.3D untuk Java

## Pendahuluan

Siap untuk **add child node** ke dalam adegan 3‑D dan membuat silinder kipas yang menarik? Dalam tutorial ini kami akan membahas setiap langkah—mulai dari menyiapkan adegan, memposisikan objek 3D, hingga akhirnya **save scene as OBJ**—menggunakan Aspose.3D untuk Java. Baik Anda sedang memoles aset game atau membangun prototipe cepat, konsep-konsep di sini akan memberi Anda kontrol yang solid atas model 3‑D Anda.

## Jawaban Cepat
- **Apa yang dilakukan “add child node”?** Ia menyisipkan objek baru ke dalam grafik adegan, mewarisi transformasi dari induknya.  
- **Bagaimana cara memposisikan objek 3D?** Dengan menerapkan translasi (atau rotasi/skala) pada transformasi node.  
- **Format file apa yang digunakan untuk ekspor?** Contoh ini menyimpan model sebagai file Wavefront OBJ.  
- **Apakah saya memerlukan lisensi untuk menjalankan kode?** Versi percobaan gratis dapat digunakan untuk evaluasi; lisensi diperlukan untuk produksi.  
- **IDE apa yang paling cocok?** Semua IDE Java (IntelliJ IDEA, Eclipse, VS Code) yang mendukung JDK 8+.

## Apa itu “add child node” dalam Aspose.3D?
Menambahkan child node berarti membuat node baru di bawah parent yang sudah ada dalam hierarki adegan. Child mewarisi sistem koordinat parent, sehingga memudahkan **position 3d object** relatif satu sama lain.

## Mengapa menambahkan child node saat membangun silinder kipas?
- **Desain modular:** Setiap silinder (kipas atau non‑kipas) berada di node masing‑masing, mempermudah penyuntingan di kemudian hari.  
- **Pewarisan transformasi:** Memindahkan, memutar, atau menskala parent akan otomatis memengaruhi semua child.  
- **Grafik adegan yang lebih bersih:** Meningkatkan keterbacaan dan debugging model yang kompleks.

## Prasyarat

- **Java Development Kit (JDK)** – unduh dari [official site](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – dapatkan pustaka terbaru dari [download link](https://releases.aspose.com/3d/java/).

## Impor Paket

Mulailah dengan mengimpor paket yang diperlukan ke dalam proyek Java Anda. Langkah ini penting untuk mengakses fungsionalitas yang disediakan oleh Aspose.3D.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Membuat Scene

Pertama, kami membuat scene 3‑D kosong yang akan menampung semua objek kami.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Langkah 2: Membuat Silinder Kipas

Selanjutnya, kami membangun silinder yang akan dirender sebagai kipas (sweep parsial).

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Langkah 3: Tambahkan Child Node & Posisi Objek 3D

Sekarang kami **add child node** ke scene dan **position the 3d object** dengan mengatur translasi-nya. Di sinilah silinder kipas menjadi bagian dari grafik adegan.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Langkah 4: Membuat Silinder Non‑Kipas

Untuk menunjukkan fleksibilitas Aspose.3D, kami juga membuat silinder biasa tanpa kipas dan menambahkannya sebagai child node lain.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Langkah 5: Simpan Scene sebagai OBJ

Akhirnya, kami **save scene as OBJ** sehingga Anda dapat melihat hasilnya di penampil 3‑D standar mana pun.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Selamat! Anda telah berhasil **added child node**, memposisikan objek-objek Anda, dan mengekspor model.

## Masalah Umum & Tips

| Masalah | Solusi |
|-------|----------|
| **File not found** saat menyimpan | Pastikan direktori target ada dan Anda memiliki izin menulis. |
| **Cylinder appears flat** | Verifikasi nilai radius dan tinggi; Aspose.3D mengharapkan satuan dalam skala yang sama. |
| **Fan slice looks incomplete** | Sesuaikan `ThetaLength` (dalam radian) untuk mencakup sudut yang diinginkan. |
| **Scene not visible in viewer** | Pastikan file OBJ disimpan bersama file `.mtl` (material) yang menyertainya jika diperlukan. |

## Pertanyaan yang Sering Diajukan

**Q:** *Apakah Aspose.3D kompatibel dengan pustaka Java lain untuk pemodelan 3D?*  
**A:** Ya, Aspose.3D dapat bekerja bersama pustaka Java 3‑D lainnya, memungkinkan Anda menggabungkan fitur sesuai kebutuhan.

**Q:** *Bisakah saya menyesuaikan tampilan silinder kipas yang dihasilkan lebih lanjut?*  
**A:** Tentu saja. Anda dapat menerapkan material, tekstur, dan pencahayaan menggunakan kelas `Material` dan `Light`.

**Q:** *Di mana saya dapat menemukan dukungan atau bantuan tambahan untuk Aspose.3D?*  
**A:** Kunjungi [Aspose.3D forum](https://forum.aspose.com/c/3d/18) untuk bantuan komunitas dan respons resmi.

**Q:** *Apakah ada versi percobaan gratis untuk Aspose.3D?*  
**A:** Ya, Anda dapat menjelajahi Aspose.3D dengan [free trial](https://releases.aspose.com/) sebelum membeli.

**Q:** *Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?*  
**A:** Dapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/) untuk pengujian dan pengembangan.

## Kesimpulan

Dalam panduan ini kami menunjukkan cara **add child node**, **position 3d object**, dan **save scene as OBJ** sambil membuat silinder kipas yang disesuaikan dengan Aspose.3D untuk Java. Blok‑blok bangunan ini memberi Anda fleksibilitas untuk menyusun hierarki 3‑D yang kompleks dan mengekspornya untuk alur kerja selanjutnya.

---

**Terakhir Diperbarui:** 2025-12-09  
**Diuji Dengan:** Aspose.3D 24.12 untuk Java  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}