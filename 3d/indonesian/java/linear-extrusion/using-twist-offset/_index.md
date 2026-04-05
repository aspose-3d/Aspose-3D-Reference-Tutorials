---
date: 2026-02-22
description: Pelajari cara membuat adegan 3D dan mengekspor adegan 3D menggunakan
  Aspose.3D untuk Java dengan ekstrusi linier, putaran, dan offset putaran.
linktitle: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cara membuat adegan 3D dengan Twist Offset dalam Linear Extrusion menggunakan
  Aspose.3D untuk Java
url: /id/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menggunakan Twist Offset dalam Linear Extrusion dengan Aspose.3D untuk Java

## Pendahuluan

Dalam dunia grafis 3D yang dinamis, menguasai seni **create 3d scene** menjadi pengubah permainan bagi proyek pemodelan 3D Java apa pun. Dengan Aspose.3D untuk Java Anda tidak hanya dapat mengekstrusi bentuk secara linier tetapi juga menambahkan twist offset untuk menghasilkan geometri yang rumit dan berputar. Tutorial ini memandu Anda melalui setiap langkah yang diperlukan untuk **create 3d scene**, menerapkan twist linear extrusion, dan akhirnya **export 3d scene** ke file OBJ umum.

## Jawaban Cepat
- **Apa yang dilakukan Twist Offset?** Itu menggeser titik awal twist, memungkinkan Anda mengoffset rotasi sepanjang jalur ekstrusi.  
- **Kelas mana yang melakukan linear extrusion?** `LinearExtrusion` – Anda dapat mengatur twist, slices, dan twist offset padanya.  
- **Bisakah saya mengekspor hasilnya?** Ya, panggil `scene.save(..., FileFormat.WAVEFRONTOBJ)` untuk mengekspor scene 3D.  
- **Apakah saya memerlukan lisensi untuk pengembangan?** Lisensi sementara dapat digunakan untuk pengujian; lisensi penuh diperlukan untuk produksi.  
- **Versi Java apa yang didukung?** Runtime Java 8+ apa pun dapat bekerja dengan perpustakaan Aspose.3D terbaru.

## Apa itu “create 3d scene” dalam Aspose.3D?
Membuat scene 3D berarti menginstansiasi objek `Scene`, menambahkan node (objek) ke dalam hierarkinya, dan akhirnya menyimpan scene ke format file pilihan Anda. Ini merupakan dasar bagi alur kerja pemodelan 3D apa pun di Java.

## Mengapa menggunakan linear extrusion twist dengan twist offset?
Menambahkan twist saat mengekstrusi memberi Anda bentuk spiral seperti kolom heliks atau pegangan dekoratif. Twist offset memungkinkan Anda memulai twist pada posisi khusus, memberikan kontrol lebih halus atas bentuk akhir—sempurna untuk komponen mekanik, model artistik, atau detail arsitektur.

## Prasyarat

- **Lingkungan Java:** Pastikan Anda memiliki lingkungan pengembangan Java yang terpasang di sistem Anda.  
- **Aspose.3D untuk Java:** Unduh dan instal perpustakaan Aspose.3D dari [download link](https://releases.aspose.com/3d/java/).  
- **Dokumentasi:** Kenali [dokumentasi Aspose.3D untuk Java](https://reference.aspose.com/3d/java/).

## Mengimpor Paket

Dalam proyek Java Anda, impor paket yang diperlukan untuk mulai menggunakan Aspose.3D untuk Java. Pastikan Anda menyertakan perpustakaan yang dibutuhkan untuk integrasi yang mulus.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Cara membuat 3d scene – Panduan Langkah‑per‑Langkah

### Langkah 1: Siapkan Lingkungan
Mulailah dengan menyiapkan lingkungan pengembangan Java Anda dan memastikan bahwa Aspose.3D untuk Java terinstal dengan benar. Langkah ini penting untuk setiap pekerjaan **java 3d modeling**.

### Langkah 2: Inisialisasi Profil Dasar
Buat profil dasar untuk ekstrusi, dalam hal ini, `RectangleShape` dengan radius pembulatan 0.3. Profil mendefinisikan penampang yang akan disapu sepanjang jalur ekstrusi.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Langkah 3: Buat 3D Scene
Bangun sebuah 3D scene untuk menampung objek ekstrusi Anda. Di sinilah Anda akan **create child node** elemen yang mewakili setiap potongan geometri.

```java
// Create a scene
Scene scene = new Scene();
```

### Langkah 4: Buat Node
Hasilkan node dalam scene untuk mewakili entitas yang berbeda. Di sini kami membuat dua node saudara—satu untuk ekstrusi polos dan satu lagi yang menggunakan twist offset.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Langkah 5: Lakukan Linear Extrusion dengan Twist dan Twist Offset
Terapkan linear extrusion pada kedua node. Node kiri menunjukkan twist dasar, sementara node kanan menambahkan twist offset untuk menggambarkan kontrol ekstra yang Anda dapatkan dengan fitur ini.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

> **Pro tip:** Sesuaikan `setSlices()` untuk meningkatkan resolusi mesh ketika Anda membutuhkan kelengkungan yang lebih halus.

### Langkah 6: Simpan 3D Scene (Export 3d scene)
Akhirnya, ekspor scene yang telah dirakit ke file OBJ sehingga Anda dapat melihatnya di penampil 3D standar mana pun atau mengimpornya ke alur kerja lain.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Ketika kode berhasil dijalankan, Anda akan menemukan `TwistOffsetInLinearExtrusion.obj` di direktori yang ditentukan, siap dibuka di alat seperti Blender, MeshLab, atau perangkat lunak CAD apa pun.

## Masalah Umum dan Solusinya
| Masalah | Mengapa Terjadi | Solusi |
|-------|----------------|-----|
| **Scene disimpan sebagai file kosong** | Path `MyDir` tidak benar atau tidak memiliki izin menulis. | Pastikan direktori ada dan dapat ditulisi, atau gunakan path absolut. |
| **Twist terlihat datar** | `setSlices()` terlalu rendah, menghasilkan mesh kasar. | Tingkatkan jumlah slice (misalnya, 200) untuk twist yang lebih halus. |
| **Twist offset tidak berpengaruh** | Vektor offset sejajar dengan arah ekstrusi. | Gunakan komponen X atau Y yang tidak nol untuk melihat pergeseran offset. |

## Pertanyaan yang Sering Diajukan

### Q1: Bisakah saya menggunakan Aspose.3D untuk Java dalam proyek non‑komersial?
A1: Ya, Aspose.3D untuk Java dapat digunakan baik dalam proyek komersial maupun non‑komersial. Periksa [licensing options](https://purchase.aspose.com/buy) untuk detail lebih lanjut.

### Q2: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?
A2: Kunjungi [forum Aspose.3D untuk Java](https://forum.aspose.com/c/3d/18) untuk mendapatkan bantuan dan terhubung dengan komunitas.

### Q3: Apakah tersedia percobaan gratis untuk Aspose.3D untuk Java?
A3: Ya, Anda dapat menjelajahi versi percobaan gratis dari [halaman rilis](https://releases.aspose.com/).

### Q4: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D untuk Java?
A4: Dapatkan lisensi sementara untuk proyek Anda dengan mengunjungi [tautan ini](https://purchase.aspose.com/temporary-license/).

### Q5: Apakah ada contoh dan tutorial tambahan yang tersedia?
A5: Ya, lihat [dokumentasi](https://reference.aspose.com/3d/java/) untuk contoh lebih banyak dan tutorial mendalam.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Terakhir Diperbarui:** 2026-02-22  
**Diuji Dengan:** Aspose.3D for Java 24.11 (terbaru)  
**Penulis:** Aspose