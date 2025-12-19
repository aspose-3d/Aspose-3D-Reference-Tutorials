---
date: 2025-12-19
description: Pelajari cara membuat adegan 3D dan mengekspor file OBJ 3D menggunakan
  Twist Offset pada Linear Extrusion dengan Aspose.3D untuk Java.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Buat adegan 3D dengan Twist Offset – Aspose.3D Java
url: /id/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat adegan 3d dengan Twist Offset – Aspose.3D untuk Java

## Pendahuluan

Di dunia grafis 3D yang dinamis, mempelajari cara **create 3d scene** dengan ekstrusi linear merupakan perubahan besar. Dengan Aspose.3D untuk Java, Anda dapat meningkatkan keterampilan pemodelan 3D Anda dengan menggabungkan fitur Twist Offset ke dalam proses ekstrusi linear. Tutorial ini akan memandu Anda melalui langkah‑langkah penggunaan Twist Offset dalam Linear Extrusion menggunakan Aspose.3D untuk Java, memberikan Anda alat untuk membuat adegan 3D yang menakjubkan.

## Jawaban Cepat
- **Apa yang dilakukan Twist Offset?** Ini menggeser awal twist sepanjang jalur ekstrusi, memberi Anda kontrol lebih besar atas geometri.  
- **Format file apa yang digunakan untuk ekspor?** Contoh ini menyimpan model sebagai Wavefront OBJ (`.obj`).  
- **Apakah saya memerlukan lisensi untuk pengembangan?** Versi percobaan gratis dapat digunakan untuk pengujian; lisensi komersial diperlukan untuk produksi.  
- **Versi Java apa yang diperlukan?** Java 8 atau yang lebih baru.  
- **Bisakah saya mengubah jumlah slice?** Ya – metode `setSlices` menentukan kelancaran twist.

## Prasyarat

Sebelum memulai tutorial, pastikan Anda memiliki prasyarat berikut:

- Lingkungan Java: Pastikan Anda memiliki lingkungan pengembangan Java yang terpasang di sistem Anda.  
- Aspose.3D untuk Java: Unduh dan instal pustaka Aspose.3D dari [tautan unduhan](https://releases.aspose.com/3d/java/).  
- Dokumentasi: Kenali [dokumentasi Aspose.3D untuk Java](https://reference.aspose.com/3d/java/).

## Impor Paket

Dalam proyek Java Anda, impor paket yang diperlukan untuk mulai menggunakan Aspose.3D untuk Java. Pastikan Anda menyertakan pustaka yang dibutuhkan untuk integrasi yang mulus.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Langkah 1: Siapkan Lingkungan

Mulailah dengan menyiapkan lingkungan pengembangan Java Anda dan memastikan bahwa Aspose.3D untuk Java terinstal dengan benar.

## Langkah 2: Inisialisasi Profil Dasar

Buat profil dasar untuk ekstrusi, dalam hal ini, sebuah `RectangleShape` dengan radius pembulatan 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Langkah 3: Buat Adegan 3D

Bangun adegan 3D untuk menampung objek yang diekstrusi.

```java
// Create a scene
Scene scene = new Scene();
```

## Langkah 4: Buat Node

Hasilkan node dalam adegan untuk mewakili entitas yang berbeda.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Langkah 5: Lakukan Ekstrusi Linear

Gunakan ekstrusi linear pada node kiri dan kanan dengan berbagai properti.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Langkah 6: Simpan Adegan 3D

Simpan adegan 3D yang baru Anda buat dengan format file yang ditentukan.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Cara menyimpan model 3d dan mengekspor 3d obj

Pemanggilan `scene.save` pada langkah sebelumnya **menyimpan model 3d** sebagai file OBJ, yang merupakan format **export 3d obj** yang banyak didukung. Anda dapat mengubah nama file atau memilih format lain yang didukung (mis., STL, FBX) dengan menyesuaikan enum `FileFormat`.

## Kesimpulan

Selamat! Anda telah berhasil menerapkan Twist Offset dalam Linear Extrusion menggunakan Aspose.3D untuk Java. Fitur kuat ini membuka dunia kemungkinan untuk upaya pemodelan 3D Anda, memungkinkan Anda untuk **create 3d scene** dengan twist dan offset yang rumit, dan kemudian **save 3d model** dalam format yang siap untuk alur kerja selanjutnya.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk Java dalam proyek non-komersial?

A1: Ya, Aspose.3D untuk Java dapat digunakan dalam proyek komersial maupun non-komersial. Periksa [opsi lisensi](https://purchase.aspose.com/buy) untuk detail lebih lanjut.

### Q2: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?

A2: Kunjungi [forum Aspose.3D untuk Java](https://forum.aspose.com/c/3d/18) untuk mendapatkan bantuan dan terhubung dengan komunitas.

### Q3: Apakah tersedia versi percobaan gratis untuk Aspose.3D untuk Java?

A3: Ya, Anda dapat menjelajahi versi percobaan gratis dari [halaman rilis](https://releases.aspose.com/).

### Q4: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D untuk Java?

A4: Dapatkan lisensi sementara untuk proyek Anda dengan mengunjungi [tautan ini](https://purchase.aspose.com/temporary-license/).

### Q5: Apakah ada contoh dan tutorial tambahan yang tersedia?

A5: Ya, lihat [dokumentasi](https://reference.aspose.com/3d/java/) untuk contoh lebih banyak dan tutorial mendalam.

## Pertanyaan yang Sering Diajukan

**Q: Apakah tutorial ini bagian dari seri tutorial Aspose 3d?**  
A: Ya – ini adalah **aspose 3d tutorial** resmi yang menunjukkan fitur spesifik dari pustaka.

**Q: Bisakah saya menggunakan bentuk lain selain persegi panjang?**  
A: Tentu saja. Setiap implementasi `IProfile` (mis., `CircleShape`, `PolygonShape` khusus) dapat diekstrusi.

**Q: Apa yang terjadi jika saya melewatkan `setTwistOffset`?**  
A: Ekstrusi akan mulai memutar dari asal profil, menghasilkan twist yang simetris.

**Q: Bagaimana cara meningkatkan kelancaran twist?**  
A: Tingkatkan nilai yang diberikan ke `setSlices`; jumlah slice yang lebih tinggi menghasilkan geometri yang lebih halus.

**Q: Format file lain apa yang dapat saya ekspor selain OBJ?**  
A: Aspose.3D mendukung STL, FBX, GLTF, 3MF, dan beberapa lainnya melalui enum `FileFormat`.

---

**Terakhir Diperbarui:** 2025-12-19  
**Diuji Dengan:** Aspose.3D 24.11 untuk Java  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}