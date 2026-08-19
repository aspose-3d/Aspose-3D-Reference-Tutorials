---
date: 2026-06-13
description: Pelajari tutorial grafis 3D Java tentang mengontrol pusat dalam ekstrusi
  linear dengan Aspose.3D, termasuk cara mengatur rounding radius dan menyimpan file
  OBJ Java.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Mengontrol Pusat dalam Ekstrusi Linear dengan Aspose.3D untuk Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: Buat Mesh 3D Java – Pusat dalam Ekstrusi Linear
url: /id/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat Mesh 3D Java – Pusat dalam Extrusi Linear

## Pendahuluan

Jika Anda membangun visualisasi 3‑D dalam Java, menguasai teknik ekstrusi sangat penting. Tutorial **java 3d graphics tutorial** ini menunjukkan cara **create 3d mesh java** objek dengan mengendalikan pusat ekstrusi linear menggunakan Aspose.3D untuk Java. Pada akhir panduan ini Anda akan memahami mengapa properti `center` penting, cara **set rounding radius**, dan cara **save obj file java**‑compatible output. Anda juga akan melihat cara **export 3d model obj** untuk digunakan di editor 3‑D utama mana pun.

## Jawaban Cepat
- **Apa fungsi properti center?** Menentukan apakah ekstrusi simetris di sekitar asal profil.  
- **Apakah saya memerlukan lisensi untuk menjalankan kode?** Lisensi sementara cukup untuk pengujian; lisensi penuh diperlukan untuk produksi.  
- **Format file apa yang digunakan untuk hasilnya?** Adegan disimpan sebagai file Wavefront OBJ.  
- **Bisakah saya mengubah jumlah irisan?** Ya, gunakan `setSlices(int)` pada objek `LinearExtrusion`.  
- **Apakah Aspose.3D kompatibel dengan Java 8+?** Tentu – mendukung semua versi Java modern.

## Apa itu tutorial grafis 3d java?

Sebuah **java 3d graphics tutorial** adalah panduan langkah‑per‑langkah yang mengajarkan cara menggunakan pustaka Java untuk membuat, memanipulasi, dan merender objek tiga‑dimensi. Dalam tutorial ini Anda akan belajar **create 3d mesh java** dengan mengubah profil 2‑D menjadi model 3‑D lengkap, mengontrol penyelarasan pusatnya, membulatkan sudut ekstrusi, dan akhirnya mengekspor hasilnya sebagai file OBJ yang dapat dibaca oleh program 3‑D apa pun.

## Mengapa menggunakan Aspose.3D untuk Java?

Aspose.3D untuk Java menyediakan API tingkat tinggi yang menghilangkan kebutuhan perhitungan mesh manual, memungkinkan Anda fokus pada desain daripada geometri tingkat rendah. Ia mendukung **50+ format input dan output**—termasuk OBJ, FBX, STL, dan GLTF—sehingga Anda dapat **export 3d model obj** atau format lain dengan satu pemanggilan metode. Pustaka ini memproses adegan ratusan halaman tanpa memuat seluruh file ke memori, memberikan **hingga 3× kinerja lebih cepat** dibandingkan pipeline OpenGL mentah pada perangkat keras server standar.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

1. **Lingkungan Pengembangan Java** – JDK 8 atau yang lebih baru terpasang.  
2. **Aspose.3D untuk Java** – Unduh pustaka dan dokumentasinya [di sini](https://reference.aspose.com/3d/java/).  
3. **Direktori Dokumen** – Buat folder di mesin Anda untuk menyimpan file yang dihasilkan; kami akan menyebutnya **“Your Document Directory.”**

## Impor Paket

Di IDE Java Anda, impor kelas Aspose.3D yang diperlukan. Ini memberi kompiler akses ke fitur ekstrusi dan pembuatan adegan.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Panduan Langkah‑per‑Langkah

### Langkah 1: Siapkan Profil Dasar

Pertama, buat bentuk 2‑D yang akan diekstrusi. Di sini kami menggunakan persegi panjang dan **set rounding radius** ke 0.3, yang melunakkan sudut dan memperlihatkan cara **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Langkah 2: Buat Adegan 3D

**Scene** adalah kontainer tingkat atas yang menampung semua objek 3‑D, cahaya, dan kamera.

```java
Scene scene = new Scene();
```

### Langkah 3: Tambahkan Node Kiri dan Kanan

**Node** mewakili objek yang dapat ditransformasi dalam grafik adegan, memungkinkan penempatan dan hierarki.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Langkah 4: Extrusi Linear – Tanpa Pusat (Node Kiri)

**LinearExtrusion** mengubah profil 2‑D menjadi mesh 3‑D dengan menyapu sepanjang garis lurus.  
**setCenter(boolean)** mengaktifkan atau menonaktifkan apakah ekstrusi dipusatkan di sekitar asal profil.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Langkah 5: Tambahkan Plane Dasar untuk Referensi (Node Kiri)

Kotak tipis berfungsi sebagai lantai visual, membantu Anda melihat orientasi ekstrusi.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Langkah 6: Extrusi Linear – Berpusat (Node Kanan)

Sekarang ulangi ekstrusi, kali ini mengaktifkan `center`. Geometri akan simetris di sekitar asal profil, memberikan hasil **create 3d mesh java** yang seimbang sempurna.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Langkah 7: Tambahkan Plane Dasar untuk Referensi (Node Kanan)

Plane dasar yang sama untuk sisi kanan, membuat perbandingan menjadi jelas.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Langkah 8: Simpan Adegan 3D

Akhirnya, ekspor seluruh adegan ke file Wavefront OBJ – format yang siap pakai di sebagian besar editor 3‑D. Metode `save` secara otomatis mengonversi mesh ke spesifikasi OBJ, memungkinkan Anda **save obj file java** tanpa pemrosesan lanjutan.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|---------|----------------|--------|
| **Extrusion appears offset** | `setCenter(false)` meninggalkan profil terpasang pada sudutnya. | Gunakan `setCenter(true)` untuk hasil simetris. |
| **OBJ file is empty** | Jalur direktori output salah atau tidak memiliki izin menulis. | Pastikan `MyDir` mengarah ke folder yang ada dan aplikasi memiliki akses menulis. |
| **Rounded corners look sharp** | Radius pembulatan terlalu kecil relatif terhadap ukuran persegi panjang. | Tingkatkan nilai radius (mis., `setRoundingRadius(0.5)`). |

## Pertanyaan yang Sering Diajukan

### Q1: Bisakah saya menggunakan Aspose.3D untuk Java dalam proyek komersial?

A1: Ya, Aspose.3D untuk Java tersedia untuk penggunaan komersial. Untuk detail lisensi, kunjungi [di sini](https://purchase.aspose.com/buy).

### Q2: Apakah ada percobaan gratis yang tersedia?

A2: Ya, Anda dapat menjelajahi percobaan gratis Aspose.3D untuk Java [di sini](https://releases.aspose.com/).

### Q3: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?

A3: Forum komunitas Aspose.3D adalah tempat yang bagus untuk mencari dukungan dan berbagi pengalaman. Kunjungi forum [di sini](https://forum.aspose.com/c/3d/18).

### Q4: Apakah saya memerlukan lisensi sementara untuk pengujian?

A4: Ya, jika Anda memerlukan lisensi sementara untuk tujuan pengujian, Anda dapat memperolehnya [di sini](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya dapat menemukan dokumentasi?

A5: Dokumentasi untuk Aspose.3D untuk Java tersedia [di sini](https://reference.aspose.com/3d/java/).

## Kesimpulan

Dengan menyelesaikan **java 3d graphics tutorial** ini, Anda kini tahu cara **create 3d mesh java**, mengendalikan pusat ekstrusi linear, menyesuaikan radius pembulatan, dan **save obj file java** output menggunakan Aspose.3D. Teknik ini memberi Anda kontrol halus atas simetri mesh, yang penting untuk aset game, prototipe CAD, dan visualisasi ilmiah. Jangan ragu untuk bereksperimen dengan profil berbeda, jumlah irisan, dan format ekspor untuk memperluas kotak peralatan 3‑D Anda.

---

**Terakhir Diperbarui:** 2026-06-13  
**Diuji Dengan:** Aspose.3D untuk Java 24.11  
**Penulis:** Aspose

## Tutorial Terkait

- [Buat Extrusi 3D Java dengan Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Cara Mengatur Arah dalam Extrusi Linear dengan Aspose.3D untuk Java](/3d/java/linear-extrusion/setting-direction/)
- [Buat Adegan 3D dengan Twist dalam Extrusi Linear – Aspose.3D untuk Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}