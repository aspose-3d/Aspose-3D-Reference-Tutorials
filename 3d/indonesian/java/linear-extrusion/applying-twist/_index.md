---
title: Menerapkan Twist dalam Ekstrusi Linier dengan Aspose.3D untuk Java
linktitle: Menerapkan Twist dalam Ekstrusi Linier dengan Aspose.3D untuk Java
second_title: Asumsikan.3D Java API
description: Pelajari cara menambahkan sentuhan unik pada model 3D Anda menggunakan Aspose.3D untuk Java. Ikuti panduan langkah demi langkah kami untuk meningkatkan efek ekstrusi linier.
type: docs
weight: 14
url: /id/java/linear-extrusion/applying-twist/
---
## Perkenalan

Selamat datang di tutorial langkah demi langkah tentang menerapkan twist dalam ekstrusi linier menggunakan Aspose.3D untuk Java. Aspose.3D adalah perpustakaan Java yang kuat yang memungkinkan pengembang untuk bekerja dengan format file 3D, menawarkan fungsionalitas yang kuat untuk membuat, memanipulasi, dan merender adegan 3D. Dalam tutorial ini, kita akan mempelajari cara menerapkan efek putaran selama proses ekstrusi linier untuk menyempurnakan model 3D Anda.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

- Lingkungan Pengembangan Java: Pastikan Anda telah menginstal Java di sistem Anda.
-  Perpustakaan Aspose.3D: Unduh dan instal perpustakaan Aspose.3D untuk Java dari[tautan unduhan](https://releases.aspose.com/3d/java/).
-  Dokumentasi: Lihat[Dokumentasi Aspose.3D](https://reference.aspose.com/3d/java/) untuk panduan komprehensif.

## Paket Impor

Sebelum memulai proses pengkodean, impor paket yang diperlukan ke proyek Java Anda. Berikut ini contoh cara melakukannya:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Atur Direktori Dokumen

Mulailah dengan mengatur direktori dokumen tempat adegan 3D Anda akan disimpan.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Langkah 2: Inisialisasi Profil Dasar

Inisialisasi profil dasar yang akan diekstrusi. Pada contoh ini, kita menggunakan bentuk persegi panjang dengan jari-jari pembulatan.

```java
// ExStart:InisialisasiBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd: InisialisasiBaseProfile
```

## Langkah 3: Buat Adegan

Buat adegan 3D untuk menampung node yang diekstrusi.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Langkah 4: Buat Node

Buat node kiri dan kanan dalam adegan. Sesuaikan terjemahan node kiri.

```java
// ExStart:BuatNode
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:BuatNode
```

## Langkah 5: Lakukan Ekstrusi Linier dengan Twist

Lakukan ekstrusi linier pada node kiri dan kanan, terapkan properti twist dan irisan.

```java
// ExStart: Ekstrusi Linier Dengan Twist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd: Ekstrusi Linier Dengan Twist
```

## Langkah 6: Simpan Adegan 3D

Simpan adegan 3D dalam format file Wavefront OBJ.

```java
// ExStart:Simpan3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:Simpan3DScene
```

## Kesimpulan

Selamat! Anda telah berhasil menerapkan twist dalam ekstrusi linier menggunakan Aspose.3D untuk Java. Tutorial ini memberikan panduan langkah demi langkah yang mendetail untuk membantu Anda meningkatkan kemampuan pemodelan 3D Anda.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk Java agar dapat bekerja dengan format file 3D lainnya?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, memungkinkan Anda mengimpor, mengekspor, dan memanipulasi beragam jenis file.

### Q2: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?

 A2: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.

### Q3: Apakah tersedia uji coba gratis untuk Aspose.3D untuk Java?

 A3: Ya, Anda dapat mengakses versi uji coba gratis dari[Di Sini](https://releases.aspose.com/).

### Q4: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk Java?

 A4: Dapatkan lisensi sementara dari[halaman lisensi sementara](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya bisa membeli Aspose.3D untuk Java?

 A5: Beli Aspose.3D untuk Java dari[halaman pembelian](https://purchase.aspose.com/buy).