---
title: Pusat Pengendalian dalam Ekstrusi Linier dengan Aspose.3D untuk Java
linktitle: Pusat Pengendalian dalam Ekstrusi Linier dengan Aspose.3D untuk Java
second_title: Asumsikan.3D Java API
description: Jelajahi dunia grafis 3D di Java dengan Aspose.3D. Kontrol bagian tengah dalam ekstrusi linier dengan mudah.
weight: 11
url: /id/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Pusat Pengendalian dalam Ekstrusi Linier dengan Aspose.3D untuk Java

## Perkenalan

Dalam dunia grafik 3D dan pemrograman Java, mengendalikan pusat dalam ekstrusi linier memainkan peran penting dalam mencapai efek yang diinginkan dalam proyek Anda. Aspose.3D untuk Java menyediakan toolkit yang kuat untuk menangani tugas-tugas tersebut dengan lancar. Dalam tutorial ini, kita akan mendalami proses pengendalian pusat dalam ekstrusi linier menggunakan Aspose.3D untuk Java, menguraikan setiap langkah untuk memastikan pemahaman yang lancar dan komprehensif.

## Prasyarat

Sebelum kita memulai perjalanan tutorial ini, pastikan Anda memiliki prasyarat berikut:

1. Lingkungan Pengembangan Java: Pastikan Anda telah menyiapkan lingkungan pengembangan Java di mesin Anda.

2.  Aspose.3D untuk Java: Unduh dan instal perpustakaan Aspose.3D. Anda dapat menemukan perpustakaan dan dokumentasinya[Di Sini](https://reference.aspose.com/3d/java/).

3. Direktori Dokumen: Buat direktori untuk menyimpan dokumen Java Anda. Sebut saja "Direktori Dokumen Anda".

## Paket Impor

Di lingkungan pengembangan Java Anda, impor paket yang diperlukan untuk Aspose.3D. Hal ini memastikan bahwa kode Anda memiliki akses ke fungsi yang disediakan oleh perpustakaan.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Siapkan Profil Dasar

Inisialisasi profil dasar yang akan diekstrusi. Dalam contoh ini, kita akan menggunakan bentuk persegi panjang dengan radius pembulatan 0,3.

```java
// Jalur ke direktori dokumen.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Langkah 2: Buat Adegan 3D

Bangun fondasi dunia 3D Anda dengan menciptakan sebuah adegan.

```java
Scene scene = new Scene();
```

## Langkah 3: Buat Node Kiri dan Kanan

Tetapkan node kiri dan kanan dalam adegan Anda. Node ini berfungsi sebagai kanvas untuk objek 3D Anda.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Langkah 4: Ekstrusi Linier dengan Properti Pusat

Lakukan ekstrusi linier pada simpul kiri tanpa memusatkan, dan atur jumlah irisan menjadi 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Langkah 5: Tetapkan Bidang Tanah untuk Referensi

Tingkatkan representasi visual dengan menambahkan bidang dasar ke node kiri.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Langkah 6: Ekstrusi Linier dengan Properti Pusat (Node Kanan)

Lakukan ekstrusi linier pada node kanan, kali ini ekstrusi di tengah, dan atur lagi jumlah irisan menjadi 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Langkah 7: Tetapkan Bidang Tanah untuk Referensi (Node Kanan)

Mirip dengan node kiri, tambahkan ground plane ke node kanan sebagai referensi.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Langkah 8: Simpan Adegan 3D

Simpan adegan 3D Anda dalam format Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Kesimpulan

Mengontrol pusat dalam ekstrusi linier dengan Aspose.3D untuk Java membuka kemungkinan menarik dalam pengembangan grafis 3D. Dengan mengikuti panduan langkah demi langkah ini, Anda telah mempelajari cara memanipulasi properti pusat, memungkinkan Anda mencapai efek visual yang diinginkan dalam proyek Java Anda.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk Java dalam proyek komersial?

 A1: Ya, Aspose.3D untuk Java tersedia untuk penggunaan komersial. Untuk detail lisensi, kunjungi[Di Sini](https://purchase.aspose.com/buy).

### Q2: Apakah tersedia uji coba gratis?

 A2: Ya, Anda dapat menjelajahi uji coba gratis Aspose.3D untuk Java[Di Sini](https://releases.aspose.com/).

### Q3: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?

 A3: Forum komunitas Aspose.3D adalah tempat yang tepat untuk mencari dukungan dan berbagi pengalaman Anda. Kunjungi forumnya[Di Sini](https://forum.aspose.com/c/3d/18).

### Q4: Apakah saya memerlukan lisensi sementara untuk pengujian?

A4: Ya, jika Anda memerlukan lisensi sementara untuk tujuan pengujian, Anda bisa mendapatkannya[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya dapat menemukan dokumentasinya?

 A5: Dokumentasi Aspose.3D untuk Java tersedia[Di Sini](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
