---
date: 2025-12-18
description: Pelajari cara membuat adegan 3D dan menyimpan file OBJ menggunakan Aspose.3D
  untuk Java. Ikuti panduan langkah demi langkah kami untuk arah ekstrusi linear.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Buat Adegan 3D – Atur Arah Ekstrusi Aspose.3D Java
url: /id/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat 3D Scene – Atur Arah Extrusi Aspose.3D Java

## Pendahuluan

Dalam tutorial ini Anda akan belajar **cara membuat 3d scene** objek dan mengontrol arah ekstrusi dengan Aspose.3D untuk Java. Baik Anda membuat visualisasi arsitektur, prototipe produk, atau aset game, menguasai ekstrusi linear memberi Anda fleksibilitas untuk memodelkan bentuk kompleks dengan cepat. Kami akan membimbing Anda melalui setiap langkah, mulai dari menambahkan node di Java hingga **ekspor model 3d obj** file, sehingga Anda dapat melihat hasilnya secara langsung.

## Jawaban Cepat
- **Apa arti “create 3d scene”?** Itu berarti menginisialisasi objek Aspose.3D `Scene` yang akan menampung semua geometri, cahaya, dan kamera.  
- **Bagaimana cara mengatur arah ekstrusi?** Gunakan metode `setDirection(Vector3)` pada instance `LinearExtrusion`.  
- **Format apa yang harus saya gunakan untuk mengekspor?** Format OBJ (`FileFormat.WAVEFRONTOBJ`) secara luas didukung untuk alur kerja 3‑D.  
- **Apakah saya memerlukan lisensi untuk Aspose.3D?** Versi percobaan gratis dapat digunakan untuk pengembangan; lisensi komersial diperlukan untuk produksi.  
- **Bisakah saya menambahkan lebih banyak node di Java?** Ya—gunakan `scene.getRootNode().createChildNode()` untuk menambahkan sebanyak mungkin objek yang dibutuhkan.

## Apa itu alur kerja “create 3d scene”?

Alur kerja **create 3d scene** dimulai dengan objek `Scene` kosong, menambahkan geometri (seperti profil yang diekstrusi), menempatkannya dengan transformasi, dan akhirnya menyimpan scene ke format file seperti OBJ. Pola ini menjadi tulang punggung sebagian besar aplikasi 3‑D yang dibangun dengan Aspose.3D.

## Mengapa mengatur arah ekstrusi?

Mengatur arah ekstrusi memungkinkan Anda memiringkan, memutar, atau memiringkan bentuk saat diekstrusi, memberi Anda kontrol atas geometri akhir tanpa proses pasca‑pemrosesan tambahan. Ini sangat berguna untuk:

- Membuat kolom yang meruncing atau pipa berbentuk khusus.  
- Menyelaraskan ekstrusi dengan sumbu non‑standar pada bagian mekanik.  
- Menghasilkan bentuk artistik untuk efek visual.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- Pengetahuan dasar Java.  
- Perpustakaan Aspose.3D terpasang – unduh dari [here](https://releases.aspose.com/3d/java/).  
- IDE seperti Eclipse atau IntelliJ IDEA.

## Impor Paket

Pertama, impor kelas Aspose.3D yang diperlukan:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Inisialisasi Profil Dasar

Buat profil 2‑D yang akan diekstrusi. Pada contoh ini kami menggunakan persegi panjang dengan sudut melengkung:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro tip:** Sesuaikan radius pembulatan untuk mengontrol seberapa tajam atau halus sudut persegi panjang muncul sebelum ekstrusi.

## Langkah 2: Buat Scene

Sekarang kami **create 3d scene** yang akan menampung objek-objek kami:

```java
Scene scene = new Scene();
```

## Langkah 3: Tambahkan Node Java – Menempatkan Objek

Kami akan menambahkan dua node anak (kiri dan kanan) ke node akar scene dan memindahkan node kiri sedikit ke samping:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Langkah 4: Cara Mengekstrusi – Node Kiri (arah default)

Ekstrusi profil pada node kiri menggunakan arah sumbu Z default. Kami juga mengatur putaran penuh 360° dan meningkatkan jumlah slice untuk kelancaran:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Langkah 5: Cara Mengatur Arah – Node Kanan

Di sini kami **how to set direction** dengan memberikan `Vector3` khusus. Ini memiringkan ekstrusi menuju vektor (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Langkah 6: Simpan File OBJ – Ekspor Model 3D

Akhirnya, kami **save obj file** untuk melihat hasilnya di penampil 3‑D apa pun:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Saat Anda membuka file OBJ yang dihasilkan, Anda akan melihat dua persegi panjang yang diekstrusi: satu dengan arah default dan satu lagi miring sesuai vektor yang kami atur.

## Masalah Umum dan Solusinya

| Masalah | Alasan | Perbaikan |
|---------|--------|-----------|
| File OBJ muncul kosong | Scene tidak disimpan atau path salah | Verifikasi `MyDir` mengarah ke folder yang dapat ditulisi dan nama file berakhiran `.obj`. |
| Ekstrusi tampak datar | `setSlices` terlalu rendah | Tingkatkan `setSlices` (misalnya, 200) untuk geometri yang lebih halus. |
| Arah tampak tidak berubah | Vektor tidak ternormalisasi | Gunakan `Vector3` yang ternormalisasi atau sesuaikan nilai untuk mencerminkan kemiringan yang diinginkan. |

## Pertanyaan yang Sering Diajukan

### Q1: Bisakah saya menggunakan Aspose.3D dengan bahasa pemrograman lain?
A1: Aspose.3D mendukung berbagai bahasa, termasuk .NET dan Java.

### Q2: Apakah ada versi percobaan gratis untuk Aspose.3D?
A2: Ya, Anda dapat menjelajahi fitur Aspose.3D dengan percobaan gratis [here](https://releases.aspose.com/).

### Q3: Di mana saya dapat menemukan dokumentasi detail untuk Aspose.3D untuk Java?
A3: Dokumentasi lengkap tersedia [here](https://reference.aspose.com/3d/java/).

### Q4: Bagaimana caraungan untuk Aspose.3D?
A4: Kunjungi [Aspose.3D forum](https://forum.aspose.com/c/3d/18) untuk bantuan atau pertanyaan apa pun.

### Q5: Apakah lisensi sementara tersedia untuk Aspose.3D?
A5: Ya, Anda dapat memperoleh lisensi sementara [here](https://purchase.aspose.com/temporary-license/).

---

**Terakhir Diperbarui:** 2025-12-18  
**Diuji dengan:** Aspose.3D 24.11 untuk Java  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}