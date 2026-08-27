---
date: 2026-06-03
description: Pelajari cara mengekspor adegan sebagai FBX dan membuat silinder 3D,
  kotak, serta model primitif lainnya menggunakan Aspose.3D untuk Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Membangun Model 3D Primitif dengan Aspose.3D untuk Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Ekspor adegan sebagai FBX dan buat silinder dengan Aspose.3D Java
url: /id/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ekspor adegan sebagai FBX dan bangun silinder dengan Aspose.3D Java

## Pendahuluan

Jika Anda pernah perlu **membuat silinder 3D** (atau bentuk dasar lainnya) langsung dari kode Java, Aspose.3D membuat tugas ini menjadi mudah. Dalam tutorial ini kami akan membahas seluruh alur kerja—dari menyiapkan lingkungan hingga **ekspor adegan sebagai FBX**—sehingga Anda dapat mulai menghasilkan geometri 3D secara programatis segera. Anda akan melihat bagaimana perpustakaan menangani primitif, cara mengatur mereka dalam grafik adegan, dan cara menyimpan hasilnya dalam format yang dapat dibaca oleh Unity, Blender, atau alat 3D lainnya.

## Jawaban Cepat

- **Perpustakaan apa yang memungkinkan saya membuat silinder 3D di Java?** Aspose.3D for Java.  
- **Format apa yang dapat saya ekspor adegan ke?** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.  
- **Apakah saya memerlukan lisensi untuk pengembangan?** A free trial works for testing; a permanent license is required for production.  
- **Apa primitif utama yang didukung?** Box, Cylinder, Sphere, Cone, and more than 10 additional shapes.  
- **Apakah kode kompatibel dengan Java 8 dan yang lebih baru?** Yes, Aspose.3D targets JDK 8+.

## Apa itu primitif silinder 3D?

Sebuah primitif silinder adalah bentuk geometris dasar yang didefinisikan oleh radius dan tinggi. Dalam banyak alur kerja 3D, ia berfungsi sebagai blok bangunan untuk model yang lebih kompleks seperti pipa, roda, atau kolom arsitektural. Aspose.3D menyediakan kelas `Cylinder` siap pakai, sehingga Anda tidak perlu menghitung vertex secara manual.

## Mengapa menggunakan Aspose.3D untuk Java?

Aspose.3D untuk Java menawarkan mesin 3D komprehensif berbasis Java murni yang menghilangkan kebutuhan akan pustaka native, menjadikannya ideal untuk pengembangan lintas platform. Ia mendukung berbagai format impor dan ekspor, menyediakan grafik adegan yang kuat untuk organisasi hierarkis, dan menyertakan primitif bawaan yang memungkinkan Anda membuat geometri dengan kode minimal. Fitur-fitur ini bersama-sama mempercepat pengembangan dan mengurangi beban pemeliharaan.

- **Mesin 3D lengkap** – mendukung impor/ekspor **lebih dari 30** format populer (FBX, OBJ, STL, GLTF, 3DS, dll).  
- **API Java murni** – tanpa ketergantungan native, sempurna untuk proyek lintas platform.  
- **Grafik adegan yang kuat** – memungkinkan Anda mengatur objek secara hierarkis, memudahkan pengelolaan adegan besar.  
- **Lisensi mudah** – mulailah dengan percobaan gratis, kemudian tingkatkan ke lisensi permanen saat Anda meluncurkan.

## Prasyarat

Sebelum menyelam ke kode, pastikan Anda memiliki:

1. **Java Development Kit (JDK)** – JDK 8 atau yang lebih baru terpasang di mesin Anda.  
2. **Aspose.3D for Java library** – unduh dan instal dari [halaman unduhan](https://releases.aspose.com/3d/java/).  

## Impor Paket

Mulailah dengan mengimpor namespace inti Aspose.3D. Ini memberi Anda akses ke `Scene`, `Box`, `Cylinder`, dan konstanta format file.

```java
import com.aspose.threed.*;
```

Setelah pustaka direferensikan, mari buat sebuah adegan dan tambahkan beberapa geometri primitif.

## Cara mengekspor adegan sebagai FBX dan membuat primitif 3D?

Muat objek `Scene` baru, tambahkan node primitif (Box, Cylinder, dll.), lalu panggil `save` dengan format FBX7500ASCII. Dalam beberapa baris saja Anda akan memperoleh file FBX lengkap yang dapat dibuka di editor 3D utama mana pun, memungkinkan integrasi mulus dengan mesin game, alur rendering, atau aplikasi AR/VR.

### Langkah 1: Inisialisasi Objek Scene

Kelas `Scene` adalah kontainer tingkat atas Aspose.3D yang menyimpan semua node, cahaya, kamera, dan material dalam memori.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Langkah 2: Bangun model kotak 3D

Kelas `Box` mewakili prisma persegi panjang dan berguna untuk menguji sistem koordinat. Menambahkannya sebagai anak node akar adegan menempatkannya di asal.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Langkah 3: Buat model silinder 3D

Kelas `Cylinder` adalah primitif silinder bawaan Aspose.3D. Ia memiliki dimensi default (radius = 1, tinggi = 2) tetapi Anda dapat menyesuaikannya melalui konstruktor.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Langkah 4: Simpan gambar dalam format FBX

Setelah menyusun adegan, ekspor sehingga alat lain (mis., Unity, Blender) dapat membacanya. Kami menggunakan format `FBX7500ASCII`, yang didukung luas dan dapat dibaca manusia.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|-------|----------------|-----|
| **File tidak ditemukan** saat menyimpan | `myDir` mengarah ke folder yang tidak ada | Pastikan direktori ada atau buat dengan `new File(myDir).mkdirs();` |
| **Adegan kosong** setelah ekspor | Tidak ada node yang ditambahkan sebelum memanggil `save` | Verifikasi bahwa pemanggilan `createChildNode` dijalankan (debug dengan `scene.getRootNode().getChildCount()` ) |
| **Pengecualian lisensi** | Menjalankan tanpa lisensi yang valid di produksi | Terapkan lisensi sementara atau permanen menggunakan `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Pertanyaan yang Sering Diajukan

**Q:** Apakah saya dapat menggunakan Aspose.3D untuk Java dengan bahasa pemrograman lain?  
A: Aspose.3D primarily supports Java, but there are versions available for .NET and C++ as well.

**Q:** Apakah Aspose.3D cocok untuk tugas pemodelan 3D yang kompleks?  
A: Absolutely. It provides a comprehensive set of features—including mesh manipulation, material assignment, and animation—making it suitable for both simple primitives and intricate models.

**Q:** Di mana saya dapat menemukan bantuan dan dukungan tambahan?  
A: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community support and discussions.

**Q:** Bisakah saya mencoba Aspose.3D sebelum membeli?  
A: Yes, you can explore a [free trial](https://releases.aspose.com/) before making a purchase decision.

**Q:** Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?  
A: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/) for Aspose.3D through the website.

## Kesimpulan

Anda kini telah mempelajari cara **mengekspor adegan sebagai FBX**, dan cara **membuat silinder 3D**, kotak, serta model primitif lainnya menggunakan Aspose.3D untuk Java. Jangan ragu bereksperimen dengan primitif tambahan seperti Sphere, Cone, atau Torus, dan jelajahi penugasan material untuk memberikan tampilan realistis pada model Anda. Setelah Anda merasa nyaman, Anda dapat mengintegrasikan file FBX yang dihasilkan ke dalam mesin game, alur AR/VR, atau alur kerja 3D lainnya.

---

**Terakhir Diperbarui:** 2026-06-03  
**Diuji Dengan:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Penulis:** Aspose

## Tutorial Terkait

- [Cara Mengekspor Adegan ke FBX dan Mengambil Info Adegan 3D di Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Cara Mengekspor FBX dan Membangun Hierarki Node di Java](/3d/java/geometry/build-node-hierarchies/)
- [Cara Membuat Model Silinder dengan Aspose.3D untuk Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}