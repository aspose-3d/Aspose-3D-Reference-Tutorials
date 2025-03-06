---
title: Menetapkan Arah dalam Ekstrusi Linier dengan Aspose.3D untuk Java
linktitle: Menetapkan Arah dalam Ekstrusi Linier dengan Aspose.3D untuk Java
second_title: Asumsikan.3D Java API
description: Kuasai ekstrusi linier dengan Aspose.3D untuk Java! Ikuti panduan kami untuk pemrograman 3D yang lancar. Unduh sekarang untuk pengalaman menawan.
weight: 12
url: /id/java/linear-extrusion/setting-direction/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menetapkan Arah dalam Ekstrusi Linier dengan Aspose.3D untuk Java

## Perkenalan

Selamat datang di panduan langkah demi langkah kami tentang pengaturan arah dalam ekstrusi linier menggunakan Aspose.3D untuk Java. Aspose.3D adalah perpustakaan Java yang kuat yang memungkinkan pengembang untuk bekerja secara lancar dengan file dan adegan 3D. Dalam tutorial ini, kami akan fokus pada tugas khusus mengatur arah dalam ekstrusi linier, meningkatkan kemahiran Anda dalam pemrograman 3D.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

- Pengetahuan dasar bahasa pemrograman Java.
-  Pustaka Aspose.3D diinstal. Anda dapat mengunduhnya dari[Di Sini](https://releases.aspose.com/3d/java/).
- Lingkungan pengembangan terintegrasi (IDE) untuk Java, seperti Eclipse atau IntelliJ.

## Paket Impor

Pastikan Anda mengimpor paket yang diperlukan untuk memulai proyek Anda:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Inisialisasi Profil Dasar

 Mulailah dengan menginisialisasi profil dasar yang akan diekstrusi. Dalam contoh ini, kami menggunakan a`RectangleShape` dengan radius pembulatan 0,3:

```java
// Jalur ke direktori dokumen.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Langkah 2: Buat Adegan

Selanjutnya, buat adegan 3D untuk memuat objek yang diekstrusi:

```java
Scene scene = new Scene();
```

## Langkah 3: Buat Node

Buat node kiri dan kanan dalam adegan:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Langkah 4: Lakukan Ekstrusi Linier pada Node Kiri

 Lakukan ekstrusi linier pada node kiri menggunakan`LinearExtrusion`kelas dengan parameter tertentu seperti twist dan irisan:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Langkah 5: Lakukan Ekstrusi Linier pada Node Kanan dengan Arah

 Lakukan ekstrusi linier pada simpul kanan, masukkan`setDirection` properti untuk menentukan arah ekstrusi:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Langkah 6: Simpan Adegan 3D

Simpan adegan 3D ke format file yang diinginkan. Dalam contoh ini, kami menyimpannya sebagai file Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara mengatur arah dalam ekstrusi linier menggunakan Aspose.3D untuk Java. Tutorial ini meningkatkan keterampilan Anda dalam pemrograman 3D dan membuka kemungkinan baru untuk proyek kreatif.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D dengan bahasa pemrograman lain?

A1: Aspose.3D mendukung berbagai bahasa pemrograman, termasuk .NET dan Java.

### Q2. Apakah ada uji coba gratis yang tersedia untuk Aspose.3D?

 A2: Ya, Anda dapat menjelajahi fitur Aspose.3D dengan uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q3: Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D untuk Java?

 A3: Dokumentasi lengkap tersedia[Di Sini](https://reference.aspose.com/3d/java/).

### Q4: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D?

 A4: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk bantuan atau pertanyaan apa pun.

### Q5: Apakah lisensi sementara tersedia untuk Aspose.3D?

 A5: Ya, Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
