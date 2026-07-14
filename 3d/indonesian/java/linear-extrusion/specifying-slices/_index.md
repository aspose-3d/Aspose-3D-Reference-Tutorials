---
date: 2026-05-24
description: Pelajari cara membuat extrusi 3D dengan irisan menggunakan Aspose.3D
  for Java. Panduan langkah demi langkah ini mencakup extrusi linear, mengatur radius
  pembulatan, dan mengekspor OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Buat Extrusi 3D dengan Irisan – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Buat Extrusi 3D dengan Irisan – Aspose.3D for Java
url: /id/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat Ekstrusi 3D dengan Irisan – Aspose.3D untuk Java

## Pendahuluan

Jika Anda perlu **membuat ekstrusi 3d** objek yang tampak halus dan presisi, mengendalikan jumlah irisan adalah kuncinya. Dalam tutorial ini kami akan menjelaskan cara menentukan irisan saat melakukan ekstrusi linear dengan Aspose.3D untuk Java. Anda akan melihat mengapa jumlah irisan penting, cara mengatur radius pembulatan, dan cara mengekspor hasilnya sebagai file OBJ yang dapat digunakan dalam pipeline 3‑D apa pun.

## Jawaban Cepat
- **Apa yang dikontrol oleh “slices”?** Jumlah penampang menengah yang digunakan untuk memperkirakan permukaan ekstrusi.  
- **Metode mana yang mengatur jumlah irisan?** `LinearExtrusion.setSlices(int)`  
- **Bisakah saya mengubah radius pembulatan profil?** Ya, melalui `RectangleShape.setRoundingRadius(double)`  
- **Format file apa yang digunakan dalam contoh ini?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Apakah saya memerlukan lisensi untuk menjalankan kode?** Versi percobaan gratis cukup untuk evaluasi; lisensi komersial diperlukan untuk produksi.

`LinearExtrusion.setSlices(int)` menentukan berapa banyak irisan menengah yang akan dihasilkan oleh ekstrusi.  
`RectangleShape.setRoundingRadius(double)` mendefinisikan radius sudut dari profil persegi panjang.

## Cara membuat ekstrusi 3d java dengan irisan?

Muat profil 2‑D Anda, pilih jumlah irisan, atur radius pembulatan, dan panggil `save` – seluruh alur kerja muat dalam beberapa baris. Aspose.3D untuk Java menangani pembuatan geometri, interpolasi irisan, dan ekspor OBJ secara otomatis, sehingga Anda dapat fokus pada kualitas visual daripada perhitungan mesh tingkat rendah.

## Apa itu ekstrusi linear dengan irisan?

Ekstrusi linear dengan irisan mengubah bentuk 2‑D datar menjadi padatan 3‑D dengan menyapu bentuk tersebut sepanjang garis lurus sambil menghasilkan sejumlah penampang menengah yang dapat dikonfigurasi. Jumlah irisan secara langsung memengaruhi seberapa halus tepi melengkung, seperti sudut bulat, ditampilkan.

## Mengapa menggunakan Aspose.3D untuk Java untuk membuat ekstrusi 3d?

Aspose.3D menyediakan **kontrol programatik penuh** atas setiap parameter ekstrusi, mendukung **lebih dari 50 format input dan output** (termasuk OBJ, FBX, STL, dan GLTF), dan dapat memproses **model multi‑ratus‑halaman** tanpa memuat seluruh file ke memori. Ia berjalan di platform apa pun yang mendukung Java, tidak memerlukan DLL native, dan menjamin hasil yang deterministik di Windows, Linux, dan macOS.

## Prasyarat

1. **Java Development Kit** – JDK 8 atau lebih tinggi terpasang.  
2. **Aspose.3D for Java** – Download library dari situs resmi [here](https://releases.aspose.com/3d/java/).  
3. Sebuah IDE atau editor teks pilihan Anda.

## Impor Paket

Tambahkan namespace Aspose.3D ke proyek Anda sehingga Anda dapat mengakses kelas pemodelan 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Panduan Langkah‑per‑Langkah

### Langkah 1: Siapkan adegan dan definisikan profil

`RectangleShape` adalah kelas yang mendefinisikan profil persegi panjang 2‑D.  
Pertama kami membuat `RectangleShape` dan memberikan **radius pembulatan** sehingga sudutnya halus.  
`Scene` adalah kontainer akar untuk semua node dan geometri.  
Kemudian kami menginisialisasi `Scene` baru yang akan menampung semua geometri.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Langkah 2: Buat objek node anak untuk setiap ekstrusi

`Node` mewakili elemen dalam grafik adegan yang dapat menampung geometri dan transformasi.  
Setiap bagian geometri berada di bawah sebuah `Node`. Di sini kami menghasilkan dua node saudara – satu untuk ekstrusi irisan rendah dan satu lagi untuk ekstrusi irisan tinggi – dan memindahkan node kiri sedikit ke samping agar hasilnya mudah dibandingkan.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Langkah 3: Lakukan ekstrusi linear dan atur irisan

`LinearExtrusion` adalah kelas yang membuat padatan dengan menyapu profil secara linear.  
`LinearExtrusion` adalah kelas Aspose.3D yang menghasilkan padatan dengan mengekstrusi profil 2‑D sepanjang garis lurus. Menggunakan **kelas dalam anonim** kami memanggil `setSlices` untuk mengontrol kehalusan. Node kiri hanya mendapatkan 2 irisan (kasar), sementara node kanan mendapatkan 10 irisan (halus).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Langkah 4: Ekspor OBJ – simpan adegan

Akhirnya kami menulis adegan ke file Wavefront OBJ, format yang banyak didukung oleh editor 3‑D dan mesin game. Ini menunjukkan kemampuan **ekspor OBJ Java** dari Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|---------|----------------|--------|
| **Ekstrusi tampak datar** | Jumlah irisan diatur ke 1 atau 0 | Pastikan `setSlices` dipanggil dengan nilai ≥ 2. |
| **Sudut bulat terlihat bergerigi** | Radius pembulatan terlalu kecil relatif terhadap jumlah irisan | Tingkatkan radius atau jumlah irisan untuk kurva yang lebih halus. |
| **File tidak ditemukan saat menyimpan** | `MyDir` mengarah ke folder yang tidak ada | Buat direktori terlebih dahulu atau gunakan path absolut. |

## Pertanyaan yang Sering Diajukan

**Q: Bagaimana saya dapat mengunduh Aspose.3D untuk Java?**  
A: Anda dapat mengunduh library [here](https://releases.aspose.com/3d/java/).

**Q: Di mana saya dapat menemukan dokumentasi untuk Aspose.3D?**  
A: Lihat dokumentasi [here](https://reference.aspose.com/3d/java/).

**Q: Apakah ada versi percobaan gratis yang tersedia?**  
A: Ya, Anda dapat menjelajahi versi percobaan gratis [here](https://releases.aspose.com/).

**Q: Bagaimana saya dapat mendapatkan dukungan untuk Aspose.3D?**  
A: Kunjungi forum dukungan [here](https://forum.aspose.com/c/3d/18).

**Q: Apakah saya dapat membeli lisensi sementara?**  
A: Ya, lisensi sementara dapat diperoleh [here](https://purchase.aspose.com/temporary-license/).

---

**Terakhir Diperbarui:** 2026-05-24  
**Diuji Dengan:** Aspose.3D for Java 24.11 (terbaru pada saat penulisan)  
**Penulis:** Aspose

## Tutorial Terkait

- [Buat Ekstrusi 3D Java dengan Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Cara Mengatur Arah dalam Ekstrusi Linear dengan Aspose.3D untuk Java](/3d/java/linear-extrusion/setting-direction/)
- [Buat Adegan 3D dengan Twist dalam Ekstrusi Linear – Aspose.3D untuk Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}