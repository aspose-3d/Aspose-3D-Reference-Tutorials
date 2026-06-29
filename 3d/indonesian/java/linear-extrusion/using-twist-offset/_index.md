---
date: 2026-06-29
description: Pelajari cara menggunakan lisensi Aspose 3D untuk membuat adegan 3D dengan
  twist offset linear extrusion di Java dan mengekspornya sebagai file Wavefront OBJ.
keywords:
- aspose 3d license
- wavefront obj export
- linear extrusion twist
- java 3d modeling
linktitle: Menggunakan Twist Offset dalam Linear Extrusion dengan Aspose.3D untuk
  Java
schemas:
- author: Aspose
  dateModified: '2026-06-29'
  description: Learn how to use an Aspose 3D license to create a 3D scene with twist
    offset linear extrusion in Java and export it as a Wavefront OBJ file.
  headline: Using Aspose 3D License for Twist Offset Extrusion in Java
  type: TechArticle
- description: Learn how to use an Aspose 3D license to create a 3D scene with twist
    offset linear extrusion in Java and export it as a Wavefront OBJ file.
  name: Using Aspose 3D License for Twist Offset Extrusion in Java
  steps:
  - name: Set Up the Environment
    text: Begin by setting up your Java development environment and ensuring that
      Aspose.3D for Java is correctly installed. This step is essential for any **java
      3d modeling** work.
  - name: Initialize the Base Profile
    text: '`RectangleShape` is a class representing a rectangular 2‑D shape used as
      an extrusion profile. Create a base profile for extrusion, in this case, a `RectangleShape`
      with a rounding radius of 0.3. The profile defines the cross‑section that will
      be swept along the extrusion path.'
  - name: Create a 3D Scene
    text: '`Scene` is the container that holds all nodes, lights, and cameras for
      your model. Building the scene first gives you a place to attach the extruded
      geometry.'
  - name: Create Nodes
    text: Generate nodes within the scene to represent different entities. Here we
      create two sibling nodes—one for a plain extrusion and another that uses a twist
      offset.
  - name: Perform Linear Extrusion with Twist and Twist Offset
    text: Apply linear extrusion on both nodes. The left node demonstrates a basic
      twist, while the right node adds a twist offset to illustrate the extra control
      you get with this feature. `setSlices(int)` sets the number of slices (segments)
      used to approximate the twist, controlling mesh resolution. > **Pr
  - name: Save the 3D Scene (Export 3d scene)
    text: '`save(String, FileFormat)` writes the scene to a file in the specified
      format. Finally, export the assembled scene to an OBJ file so you can view it
      in any standard 3D viewer or import it into other pipelines. CODE_BLOCK_PLACEHOLDER_6_END
      When the code runs successfully, you’ll find `TwistOffsetInLi'
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D for Java can be used in both commercial and non‑commercial
      projects. Check the [licensing options](https://purchase.aspose.com/buy) for
      more details.
    question: Can I use Aspose.3D for Java in non‑commercial projects?
  - answer: Visit the [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18)
      to get assistance and connect with the community.
    question: Where can I find support for Aspose.3D for Java?
  - answer: Yes, you can explore a free trial version from the [releases page](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Get a temporary license for your project by visiting [this link](https://purchase.aspose.com/temporary-license/).
    question: How do I obtain a temporary license for Aspose.3D for Java?
  - answer: Yes, refer to the [documentation](https://reference.aspose.com/3d/java/)
      for more examples and in‑depth tutorials.
    question: Are there additional examples and tutorials available?
  type: FAQPage
second_title: Aspose.3D Java API
title: Menggunakan Lisensi Aspose 3D untuk Twist Offset Extrusion di Java
url: /id/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menggunakan Lisensi Aspose 3D untuk Twist Offset Extrusion di Java

## Pendahuluan

Membuat adegan 3D di Java menjadi jauh lebih kuat ketika Anda menggabungkan **lisensi Aspose 3D** dengan fitur putaran ekstrusi linier dan offset putaran. Tutorial ini memandu Anda melalui setiap langkah yang diperlukan untuk **membuat adegan 3D**, menerapkan offset putaran, dan akhirnya **mengekspor adegan 3D** sebagai file Wavefront OBJ. Dengan versi berlisensi, Anda membuka kemampuan pembuatan mesh resolusi penuh, ukuran file tak terbatas, dan kinerja tingkat komersial.

## Jawaban Cepat
- **Apa yang dilakukan Twist Offset?** Ini menggeser titik awal putaran, memungkinkan Anda mengoffset rotasi sepanjang jalur ekstrusi.  
- **Kelas mana yang melakukan ekstrusi linier?** `LinearExtrusion` – Anda dapat mengatur twist, slices, dan twist offset padanya.  
- **Bisakah saya mengekspor hasilnya?** Ya, panggil `scene.save(..., FileFormat.WAVEFRONTOBJ)` untuk mengekspor adegan 3D.  
- **Apakah saya memerlukan lisensi Aspose 3D untuk pengembangan?** Lisensi sementara berfungsi untuk pengujian; **lisensi Aspose 3D** penuh diperlukan untuk produksi dan menghapus watermark evaluasi.  
- **Versi Java apa yang didukung?** Setiap runtime Java 8+ dapat bekerja dengan perpustakaan Aspose.3D terbaru.

## Apa itu “create 3d scene” dalam Aspose.3D?

`Scene` adalah objek tingkat‑atas Aspose.3D yang mewakili lingkungan 3D lengkap. Membuat adegan 3D dalam Aspose.3D berarti menginstansiasi objek `Scene`, menambahkan node anak yang berisi geometri, lampu, atau kamera, dan kemudian menyimpan hierarki ke format file seperti OBJ. `Scene` berfungsi sebagai kontainer akar untuk semua konten 3D dalam aplikasi Java Anda.

## Mengapa menggunakan twist ekstrusi linier dengan twist offset?

`LinearExtrusion` adalah kelas Aspose.3D untuk menyapu profil 2‑D sepanjang garis lurus guna menghasilkan geometri 3‑D. Menggunakannya dengan twist menambahkan komponen rotasi, dan twist offset memungkinkan Anda menggeser titik awal rotasi, memberi kontrol presisi atas bentuk spiral seperti kolom heliks, pegangan dekoratif, atau pegas mekanik. Kontrol tambahan ini sangat berharga dalam **java 3d modeling** untuk bagian mekanik dan desain artistik.

## Prasyarat

- **Lingkungan Java:** Pastikan Anda memiliki lingkungan pengembangan Java yang terpasang di sistem Anda.  
- **Aspose.3D for Java:** Unduh dan instal perpustakaan Aspose.3D dari [download link](https://releases.aspose.com/3d/java/).  
- **Dokumentasi:** Kenali [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  

## Impor Paket

Di proyek Java Anda, impor paket yang diperlukan untuk mulai menggunakan Aspose.3D for Java. Pastikan Anda menyertakan perpustakaan yang dibutuhkan untuk integrasi yang mulus.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Cara membuat 3d scene – Panduan Langkah‑per‑Langkah

Untuk membuat adegan 3D dengan twist offset linear extrusion di Java, pertama Anda menyiapkan lingkungan pengembangan, kemudian mendefinisikan profil persegi panjang, menginstansiasi `Scene`, menambahkan dua node anak, menerapkan `LinearExtrusion` dengan dan tanpa twist offset, dan akhirnya menyimpan adegan sebagai file Wavefront OBJ. Ikuti bagian langkah‑per‑langkah di bawah ini untuk potongan kode yang tepat.

### Langkah 1: Siapkan Lingkungan
Mulailah dengan menyiapkan lingkungan pengembangan Java Anda dan memastikan bahwa Aspose.3D for Java terpasang dengan benar. Langkah ini penting untuk setiap pekerjaan **java 3d modeling**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Langkah 2: Inisialisasi Profil Dasar
`RectangleShape` adalah kelas yang mewakili bentuk 2‑D persegi panjang yang digunakan sebagai profil ekstrusi. Buat profil dasar untuk ekstrusi, dalam hal ini, sebuah `RectangleShape` dengan radius pembulatan 0.3. Profil ini mendefinisikan penampang yang akan disapu sepanjang jalur ekstrusi.

```java
// Create a scene
Scene scene = new Scene();
```

### Langkah 3: Buat Adegan 3D
`Scene` adalah kontainer yang menampung semua node, lampu, dan kamera untuk model Anda. Membuat adegan terlebih dahulu memberi Anda tempat untuk menempelkan geometri yang diekstrusi.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Langkah 4: Buat Node
Buat node dalam adegan untuk mewakili entitas yang berbeda. Di sini kami membuat dua node saudara—satu untuk ekstrusi biasa dan satu lagi yang menggunakan twist offset.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

### Langkah 5: Lakukan Linear Extrusion dengan Twist dan Twist Offset
Terapkan linear extrusion pada kedua node. Node kiri menunjukkan twist dasar, sementara node kanan menambahkan twist offset untuk menggambarkan kontrol tambahan yang Anda dapatkan dengan fitur ini. `setSlices(int)` mengatur jumlah slice (segmen) yang digunakan untuk memperkirakan twist, mengontrol resolusi mesh.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

> **Pro tip:** Sesuaikan `setSlices()` untuk meningkatkan resolusi mesh ketika Anda membutuhkan kelengkungan yang lebih halus.

### Langkah 6: Simpan Adegan 3D (Ekspor 3d scene)
`save(String, FileFormat)` menulis adegan ke file dalam format yang ditentukan. Akhirnya, ekspor adegan yang telah dirakit ke file OBJ sehingga Anda dapat melihatnya di penampil 3D standar mana pun atau mengimpornya ke alur kerja lain.

CODE_BLOCK_PLACEHOLDER_6_END

Ketika kode berhasil dijalankan, Anda akan menemukan `TwistOffsetInLinearExtrusion.obj` di direktori yang ditentukan, siap dibuka di alat seperti Blender, MeshLab, atau perangkat lunak CAD apa pun.

## Masalah Umum dan Solusinya
| Masalah | Mengapa Terjadi | Solusi |
|-------|----------------|-----|
| **Scene disimpan sebagai file kosong** | Path `MyDir` tidak tepat atau tidak memiliki izin menulis. | Verifikasi direktori ada dan dapat ditulis, atau gunakan path absolut. |
| **Twist terlihat datar** | `setSlices()` terlalu rendah, menghasilkan mesh kasar. | Tingkatkan jumlah slice (misalnya, 200) untuk twist yang lebih halus. |
| **Twist offset tidak berpengaruh** | Vektor offset sejajar dengan arah ekstrusi. | Gunakan komponen X atau Y yang tidak nol untuk melihat pergeseran offset. |

## Pertanyaan yang Sering Diajukan

**Q: Bisakah saya menggunakan Aspose.3D for Java dalam proyek non‑komersial?**  
A: Ya, Aspose.3D for Java dapat digunakan baik dalam proyek komersial maupun non‑komersial. Periksa [licensing options](https://purchase.aspose.com/buy) untuk detail lebih lanjut.

**Q: Di mana saya dapat menemukan dukungan untuk Aspose.3D for Java?**  
A: Kunjungi [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18) untuk mendapatkan bantuan dan terhubung dengan komunitas.

**Q: Apakah tersedia versi percobaan gratis untuk Aspose.3D for Java?**  
A: Ya, Anda dapat menjelajahi versi percobaan gratis dari [releases page](https://releases.aspose.com/).

**Q: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D for Java?**  
A: Dapatkan lisensi sementara untuk proyek Anda dengan mengunjungi [this link](https://purchase.aspose.com/temporary-license/).

**Q: Apakah ada contoh dan tutorial tambahan yang tersedia?**  
A: Ya, lihat [documentation](https://reference.aspose.com/3d/java/) untuk contoh lebih banyak dan tutorial mendalam.

---

**Terakhir Diperbarui:** 2026-06-29  
**Diuji Dengan:** Aspose.3D for Java 24.11 (latest)  
**Penulis:** Aspose

{{< blocks/products/products-backtop-button >}}

## Tutorial Terkait

- [Buat Ekstrusi 3D Java dengan Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Buat Adegan 3D dengan Twist dalam Linear Extrusion – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)
- [Cara Mengatur Arah dalam Linear Extrusion dengan Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}