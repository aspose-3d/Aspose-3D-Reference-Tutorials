---
date: 2026-08-22
description: Pelajari cara membuat adegan 3D dengan twist extrusion linear menggunakan
  Aspose 3D Java, kemudian ekspor hasilnya sebagai file OBJ.
keywords:
- aspose 3d java
- how to export obj
- export obj java
- view obj file blender
- save scene as obj
- author: Aspose
  dateModified: '2026-08-22'
  description: Learn how to create a 3D scene with a linear extrusion twist using
    Aspose 3D Java. Export OBJ files step‑by‑step and master java 3d scene creation.
  headline: 'Aspose 3D Java: Create 3D Scene with Twist in Linear Extrusion'
  type: TechArticle
- questions:
  - answer: Yes – pass a negative angle to `setTwist()` to rotate in the opposite
      direction.
    question: Can I change the twist direction?
  - answer: Aspose 3D Java applies a uniform twist; for variable twist you would need
      to generate multiple segments manually.
    question: Is it possible to apply different twist values along the extrusion?
  - answer: Any standard 3‑D viewer (e.g., Blender, MeshLab) can open OBJ files.
    question: How do I view the exported OBJ file?
  - answer: Yes – after extrusion you can assign materials or UV coordinates to the
      node’s mesh.
    question: Does the library support texture mapping on twisted extrusions?
  - answer: Call `scene.save("output.obj", FileFormat.WAVEFRONTOBJ);` after building
      the scene.
    question: How do I export OBJ with Aspose 3D Java?
  type: FAQPage
lastmod: 2026-08-22
linktitle: Buat Adegan 3D dengan Twist pada Linear Extrusion – Aspose.3D for Java
og_description: Pelajari cara menggunakan Aspose 3D Java untuk membuat adegan 3D dengan
  linear extrusion twist dan mengekspornya sebagai file OBJ. Ikuti kode langkah‑demi‑langkah
  serta tips ekspor untuk pengembang Java.
og_image_alt: Tutorial showing Aspose 3D Java twist extrusion and OBJ export
og_title: 'Aspose 3D Java: buat adegan 3D dengan twist extrusion'
schemas:
- author: Aspose
  dateModified: '2026-08-22'
  description: Learn how to create a 3D scene with a linear extrusion twist using
    Aspose 3D Java, then export the result as an OBJ file.
  headline: How to create a 3D scene with twist extrusion using Aspose 3D Java
  type: TechArticle
- questions:
  - answer: Yes – pass a negative angle to `setTwist()` to rotate in the opposite
      direction.
    question: Can I change the twist direction?
  - answer: Aspose 3D Java applies a uniform twist; for variable twist you would need
      to generate multiple segments manually.
    question: Is it possible to apply different twist values along the extrusion?
  - answer: Any standard 3‑D viewer (e.g., Blender, MeshLab) can open OBJ files.
    question: How do I view the exported OBJ file?
  - answer: Yes – after extrusion you can assign materials or UV coordinates to the
      node’s mesh.
    question: Does the library support texture mapping on twisted extrusions?
  - answer: Call `scene.save("output.obj", FileFormat.WAVEFRONTOBJ);` after building
      the scene.
    question: How do I export OBJ with Aspose 3D Java?
  type: FAQPage
second_title: Aspose.3D Java API
title: Cara membuat adegan 3D dengan twist extrusion menggunakan Aspose 3D Java
url: /id/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose 3D Java: buat adegan 3D dengan ekstrusi berputar

Dalam tutorial **java 3d scene** ini Anda akan belajar cara **membuat adegan 3D**, menerapkan *linear extrusion twist*, dan akhirnya **mengekspor file OBJ Java** menggunakan **Aspose 3D Java**. Baik Anda membuat aset game, prototipe CAD, atau efek visual, menambahkan twist selama ekstrusi memberi model Anda tampilan dinamis seperti spiral yang tidak mungkin dicapai dengan ekstrusi biasa.

## Jawaban Cepat
- **Apa arti “twist” dalam ekstrusi?** Itu memutar profil secara bertahap sepanjang jalur ekstrusi, menghasilkan efek spiral.  
- **Perpustakaan mana yang menyediakan fitur twist?** Aspose 3D Java.  
- **Apakah saya dapat mengekspor hasilnya sebagai OBJ?** Ya – gunakan `FileFormat.WAVEFRONTOBJ`.  
- **Apakah saya memerlukan lisensi untuk tutorial ini?** Lisensi sementara atau penuh diperlukan untuk penggunaan produksi.  
- **Versi Java apa yang diperlukan?** Java 8 atau lebih tinggi.

## Apa itu “twist” dalam linear extrusion?

Sebuah twist memutar setiap penampang lintas dari profil yang diekstrusi dengan sudut konstan, mengubah sapuan lurus menjadi heliks halus. Transformasi ini memungkinkan Anda memodelkan sekrup botol, pegangan berspiral, atau pita dekoratif tanpa harus membangun setiap segmen secara manual. Besaran rotasi dikendalikan oleh parameter sudut twist, yang menentukan berapa derajat profil berputar dari awal hingga akhir.

## Mengapa menggunakan Aspose 3D Java?

Aspose 3D Java memungkinkan Anda bekerja dengan **50+ format input dan output**—termasuk OBJ, FBX, STL, dan glTF—sementara memproses model berukuran ratusan halaman tanpa harus memuat seluruh file ke memori. API murni‑Java-nya menghilangkan ketergantungan native, sehingga Anda dapat mengintegrasikannya ke dalam pipeline berbasis Java apa pun, mulai dari utilitas desktop hingga farm rendering sisi‑server.

## Prasyarat
- **Java Development Kit (JDK) 8+** terpasang di mesin Anda.  
- **Aspose 3D for Java** – unduh dari [download link](https://releases.aspose.com/3d/java/).  
- Familiaritas dengan sintaks dasar Java dan konsep 3‑D.  
- Akses ke [Aspose.3D documentation](https://reference.aspose.com/3d/java/) resmi untuk referensi.  
- Anda dapat mengakses versi percobaan gratis dari [Aspose 3D Java free trial page](https://releases.aspose.com/).

## Impor paket

Namespace `com.aspose.threed` berisi semua kelas yang Anda perlukan. Impor mereka di bagian atas file Java Anda.

## Langkah 1: atur direktori dokumen

Tentukan di mana file OBJ yang dihasilkan akan disimpan. Ganti placeholder dengan jalur folder nyata di sistem Anda, pastikan jalur berakhir dengan pemisah yang tepat (`/` pada Unix, `\` pada Windows).

## Langkah 2: inisialisasi profil dasar

Buat bentuk yang akan diekstrusi. Di sini kami menggunakan persegi panjang dengan radius pembulatan kecil untuk memberikan tepi tampilan yang lebih lembut.

## Langkah 3: buat adegan untuk menampung node Anda

Kelas `Scene` adalah kontainer tingkat‑atas Aspose 3D Java yang mewakili dunia 3‑D lengkap. Semua mesh, lampu, kamera, dan entitas lainnya berada di dalam instance `Scene`.

## Langkah 4: tambahkan node kiri dan kanan

Kami akan membuat dua node saudara: satu tanpa twist (untuk perbandingan) dan satu dengan twist 90‑derajat. Setiap node memiliki mesh masing‑masing, memungkinkan Anda melihat efeknya berdampingan.

## Langkah 5: lakukan linear extrusion dengan twist

`LinearExtrusion` adalah kelas yang mengubah profil 2‑D menjadi mesh 3‑D dengan menyapu sepanjang garis lurus.  
`setTwist` menentukan sudut rotasi total yang diterapkan sepanjang panjang ekstrusi.  
`setSlices` menentukan berapa banyak irisan penampang lintas menengah yang dihasilkan, memengaruhi kelancaran dan kinerja.

- `setTwist(0)` → tidak ada rotasi (ekstrusi lurus).  
- `setTwist(90)` → rotasi penuh 90‑derajat sepanjang panjang.  

Kedua node menggunakan **100 slices** untuk geometri halus, menyeimbangkan kualitas visual dan penggunaan memori.

## Langkah 6: simpan adegan 3D sebagai OBJ

Akhirnya, tulis adegan ke file OBJ sehingga Anda dapat melihatnya di penampil 3‑D standar mana pun. OBJ adalah format yang didukung luas, memudahkan impor hasil ke Blender, Maya, atau Unity.

## Masalah umum & tips
- **File path errors:** Pastikan `MyDir` berakhir dengan pemisah jalur (`/` atau `\\`) yang sesuai untuk OS Anda.  
- **Twist angle too high:** Sudut di atas 360° dapat menyebabkan geometri saling tumpang; pertahankan dalam rentang 0‑360° untuk hasil yang dapat diprediksi.  
- **Performance:** Meningkatkan `setSlices` meningkatkan kelancaran tetapi dapat memengaruhi memori; 100 slices adalah keseimbangan yang baik untuk kebanyakan skenario.

## Pertanyaan yang sering diajukan (asli)

### Q1: Bisakah saya menggunakan Aspose 3D untuk Java untuk bekerja dengan format file 3D lainnya?
A1: Ya, Aspose 3D mendukung berbagai format file 3D, memungkinkan Anda mengimpor, mengekspor, dan memanipulasi berbagai jenis file.

### Q2: Di mana saya dapat menemukan dukungan untuk Aspose 3D untuk Java?
A2: Kunjungi [Aspose.3D forum](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas dan diskusi.

### Q3: Apakah ada versi percobaan gratis untuk Aspose 3D untuk Java?
A3: Ya, Anda dapat mengakses versi percobaan gratis dari [here](https://releases.aspose.com/).

### Q4: Bagaimana saya dapat memperoleh lisensi sementara untuk Aspose 3D untuk Java?
A4: Dapatkan lisensi sementara dari [temporary license page](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya dapat membeli Aspose 3D untuk Java?
A5: Beli Aspose 3D untuk Java dari [buying page](https://purchase.aspose.com/buy).

## FAQ tambahan (dioptimalkan AI)

**Q: Bisakah saya mengubah arah twist?**  
A: Ya – berikan sudut negatif ke `setTwist()` untuk memutar ke arah berlawanan.

**Q: Apakah memungkinkan menerapkan nilai twist berbeda sepanjang ekstrusi?**  
A: Aspose 3D Java menerapkan twist seragam; untuk twist variabel Anda harus menghasilkan beberapa segmen secara manual.

**Q: Bagaimana cara melihat file OBJ yang diekspor?**  
A: Penampil 3‑D standar apa pun (misalnya Blender, MeshLab) dapat membuka file OBJ.

**Q: Apakah perpustakaan mendukung pemetaan tekstur pada ekstrusi ber‑twist?**  
A: Ya – setelah ekstrusi Anda dapat menetapkan material atau koordinat UV ke mesh node.

## FAQ referensi cepat (baru)

**Q: Bagaimana cara mengekspor OBJ dengan Aspose 3D Java?**  
A: Panggil `scene.save("output.obj", FileFormat.WAVEFRONTOBJ);` setelah membangun adegan.

**Q: Berapa jumlah slice yang direkomendasikan untuk twist halus?**  
A: 100 slices memberikan kompromi yang baik antara kelancaran dan kinerja untuk kebanyakan model.

**Q: Bisakah saya menggunakan kode ini dalam proyek Maven?**  
A: Ya – tambahkan dependensi Aspose 3D Java ke `pom.xml` Anda dan kode yang sama akan berfungsi tanpa perubahan.

**Q: Apakah saya memerlukan lisensi untuk build pengembangan?**  
A: Lisensi sementara cukup untuk evaluasi; lisensi penuh diperlukan untuk penyebaran komersial.

**Q: Apakah Java 11 didukung?**  
A: Tentu – Aspose 3D Java kompatibel dengan Java 8 hingga Java 17.

## Kesimpulan

Anda kini **telah membuat adegan 3D**, menerapkan **linear extrusion twist**, dan **mengekspor hasilnya sebagai file OBJ** menggunakan **Aspose 3D Java**. Bereksperimenlah dengan profil, sudut twist, dan jumlah slice yang berbeda untuk menciptakan geometri unik bagi game, simulasi, atau pencetakan 3‑D. Saat Anda siap melampaui OBJ, jelajahi dukungan perpustakaan untuk FBX, STL, dan glTF untuk mengintegrasikan model Anda ke dalam pipeline apa pun.

---

**Terakhir Diperbarui:** 2026-08-22  
**Diuji Dengan:** Aspose 3D for Java 24.11  
**Penulis:** Aspose

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Tutorial terkait

- [Cara membuat adegan 3d dengan Twist Offset dalam Linear Extrusion menggunakan Aspose.3D untuk Java](/3d/java/linear-extrusion/using-twist-offset/)
- [Cara Mengatur Arah dalam Linear Extrusion dengan Aspose.3D untuk Java](/3d/java/linear-extrusion/setting-direction/)
- [Buat Extrusi 3D Java dengan Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}