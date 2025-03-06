---
title: Menggunakan Twist Offset dalam Ekstrusi Linier dengan Aspose.3D untuk Java
linktitle: Menggunakan Twist Offset dalam Ekstrusi Linier dengan Aspose.3D untuk Java
second_title: Asumsikan.3D Java API
description: Tingkatkan keterampilan pemodelan 3D Anda dengan Aspose.3D untuk Java. Pelajari cara menggunakan Twist Offset dalam Ekstrusi Linier dalam tutorial komprehensif ini.

weight: 15
url: /id/java/linear-extrusion/using-twist-offset/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menggunakan Twist Offset dalam Ekstrusi Linier dengan Aspose.3D untuk Java

## Perkenalan

Dalam dunia grafis 3D yang dinamis, menguasai seni ekstrusi linier adalah sebuah terobosan. Dengan Aspose.3D untuk Java, Anda dapat meningkatkan keterampilan pemodelan 3D Anda dengan menggabungkan fitur Twist Offset ke dalam proses ekstrusi linier Anda. Tutorial ini akan memandu Anda melalui langkah-langkah memanfaatkan Twist Offset dalam Ekstrusi Linier menggunakan Aspose.3D untuk Java, memberi Anda alat untuk membuat pemandangan 3D yang menakjubkan.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

- Lingkungan Java: Pastikan Anda telah menyiapkan lingkungan pengembangan Java di sistem Anda.
-  Aspose.3D untuk Java: Unduh dan instal perpustakaan Aspose.3D dari[tautan unduhan](https://releases.aspose.com/3d/java/).
-  Dokumentasi: Biasakan diri Anda dengan[Aspose.3D untuk dokumentasi Java](https://reference.aspose.com/3d/java/).

## Paket Impor

Di proyek Java Anda, impor paket yang diperlukan untuk mulai menggunakan Aspose.3D untuk Java. Pastikan Anda menyertakan perpustakaan yang diperlukan untuk integrasi yang lancar.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Langkah 1: Siapkan Lingkungan

Mulailah dengan menyiapkan lingkungan pengembangan Java Anda dan memastikan bahwa Aspose.3D untuk Java diinstal dengan benar.

## Langkah 2: Inisialisasi Profil Dasar

Buat profil dasar untuk ekstrusi, dalam hal ini, RectangleShape dengan radius pembulatan 0,3.

```java
// Jalur ke direktori dokumen.
String MyDir = "Your Document Directory";
// Inisialisasi profil dasar yang akan diekstrusi
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Langkah 3: Buat Adegan 3D

Bangun pemandangan 3D untuk menampung objek yang Anda ekstrusi.

```java
// Membuat heboh
Scene scene = new Scene();
```

## Langkah 4: Buat Node

Hasilkan node dalam adegan untuk mewakili entitas yang berbeda.

```java
// Buat simpul kiri
Node left = scene.getRootNode().createChildNode();
// Buat simpul yang tepat
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Langkah 5: Lakukan Ekstrusi Linier

Memanfaatkan ekstrusi linier pada node kiri dan kanan dengan berbagai properti.

```java
// Lakukan ekstrusi linier pada node kiri menggunakan properti twist dan irisan
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Lakukan ekstrusi linier pada node kanan menggunakan properti twist, twist offset, dan irisan
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Langkah 6: Simpan Adegan 3D

Simpan adegan 3D yang baru Anda buat dengan format file yang ditentukan.

```java
// Simpan adegan 3D
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Kesimpulan

Selamat! Anda telah berhasil mengimplementasikan Twist Offset di Linear Extrusion menggunakan Aspose.3D untuk Java. Fitur canggih ini membuka banyak kemungkinan untuk upaya pemodelan 3D Anda, memungkinkan Anda membuat pemandangan yang rumit dan menawan.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk Java dalam proyek non-komersial?

 A1: Ya, Aspose.3D untuk Java dapat digunakan dalam proyek komersial dan non-komersial. Periksalah[pilihan lisensi](https://purchase.aspose.com/buy) untuk lebih jelasnya.

### Q2: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?

 A2: Kunjungi[Aspose.3D untuk forum Java](https://forum.aspose.com/c/3d/18) untuk mendapatkan bantuan dan berhubungan dengan masyarakat.

### Q3: Apakah tersedia uji coba gratis untuk Aspose.3D untuk Java?

 A3: Ya, Anda dapat menjelajahi versi uji coba gratis dari[halaman rilis](https://releases.aspose.com/).

### Q4: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk Java?

 A4: Dapatkan lisensi sementara untuk proyek Anda dengan mengunjungi[Link ini](https://purchase.aspose.com/temporary-license/).

### Q5: Apakah ada contoh dan tutorial tambahan yang tersedia?

 A5: Ya, lihat[dokumentasi](https://reference.aspose.com/3d/java/) untuk lebih banyak contoh dan tutorial mendalam.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
