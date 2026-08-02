---
date: 2026-08-02
description: Pelajari cara mengubah arah ekstrusi pada linear extrusion dan mengekspor
  file OBJ menggunakan Aspose.3D untuk Java. Ikuti panduan langkah demi langkah kami.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Ubah Arah Ekstrusi – Aspose.3D Java
og_description: Ubah arah ekstrusi pada linear extrusion dengan Aspose.3D untuk Java
  dan ekspor file OBJ. Panduan ini menampilkan kode langkah demi langkah serta tips
  untuk pengembang.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Ubah Arah Ekstrusi – Tutorial Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Ubah Arah Ekstrusi pada Model 3D – Aspose.3D Java
url: /id/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ubah Arah Ekstrusi pada Model 3D – Aspose.3D Java

## Pendahuluan

Dalam tutorial komprehensif ini Anda akan menemukan **cara mengubah arah ekstrusi** saat melakukan ekstrusi linear dengan Aspose.3D untuk Java. Baik Anda sedang membangun alat mirip CAD, menyiapkan aset untuk mesin game, atau menghasilkan bagian untuk pencetakan 3‑D, mengontrol arah ekstrusi memungkinkan Anda membuat bentuk yang tepat sesuai kebutuhan. Kami akan membimbing Anda melalui setiap langkah, mulai dari menginisialisasi profil hingga menyimpan hasil sebagai file OBJ, sehingga Anda juga dapat **mengekspor file model 3D OBJ** langsung dari Java.

## Jawaban Cepat
- **Kelas apa yang melakukan ekstrusi linear?** `LinearExtrusion`
- **Metode apa yang mengatur vektor ekstrusi?** `setDirection(Vector3 direction)`
- **Apakah hasil dapat disimpan sebagai OBJ?** Ya—gunakan `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Apakah lisensi diperlukan untuk produksi?** Versi percobaan gratis tersedia; lisensi wajib untuk penggunaan komersial.
- **IDE mana yang paling cocok dengan Aspose.3D?** IntelliJ IDEA dan Eclipse didukung sepenuhnya.

## Apa itu Ekstrusi Linear?

Ekstrusi linear adalah proses memperluas sketsa 2‑D (seperti persegi panjang atau lingkaran) sepanjang garis lurus untuk menghasilkan padatan 3‑D. Secara default ekstrusi mengikuti sumbu Z‑positif, tetapi Aspose.3D memungkinkan Anda mengubah jalur tersebut dengan properti `setDirection`, memberi Anda kontrol penuh atas geometri akhir.

## Mengapa Mengubah Arah Ekstrusi pada Ekstrusi Linear?

Mengubah arah ekstrusi memungkinkan Anda menyelaraskan geometri baru dengan objek yang ada, membuat komponen miring tanpa transformasi tambahan, dan menghasilkan model yang cocok dengan sistem koordinat yang dibutuhkan oleh alur kerja downstream (mis., printer 3‑D atau mesin game). Ini menghilangkan kebutuhan langkah pasca‑pemrosesan dan mengurangi overhead ukuran file hingga 15 % ketika menggunakan vektor arah yang menghindari rotasi yang tidak perlu.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- Pengetahuan dasar tentang Java.
- Perpustakaan Aspose.3D terpasang. Anda dapat mengunduhnya dari [here](https://releases.aspose.com/3d/java/). Anda juga dapat menelusuri semua rilis Aspose di halaman utama [here](https://releases.aspose.com/).
- IDE seperti Eclipse atau IntelliJ IDEA.

## Impor Paket

Namespace `com.aspose.threed` menyediakan kelas‑kelas inti 3‑D dan tipe utilitas.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Inisialisasi Profil Dasar

Kelas `RectangleShape` membuat profil 2‑D yang akan diekstrusi. Radius pembulatan kecil memberikan tepi tampilan yang halus.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Langkah 2: Buat Scene

Kelas `Scene` adalah kontainer tingkat atas Aspose.3D yang menampung semua node 3‑D, cahaya, kamera, dan material.

```java
Scene scene = new Scene();
```

## Langkah 3: Buat Node

`Node` mewakili objek dalam grafik scene, memungkinkan Anda melampirkan geometri, transformasi, dan properti lainnya.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Langkah 4: Lakukan Ekstrusi Linear pada Node Kiri

`LinearExtrusion` melakukan operasi ekstrusi, mengubah profil 2‑D menjadi mesh 3‑D.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Langkah 5: Lakukan Ekstrusi Linear pada Node Kanan dengan Arah

Di sini kita **mengubah arah ekstrusi**. Dengan memberikan `Vector3` khusus ke `setDirection`, ekstrusi mengikuti vektor (0.3, 0.2, 1), menghasilkan bentuk miring yang selaras dengan sistem koordinat scene.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Langkah 6: Simpan Scene 3D

Metode `save` menulis scene ke file dalam format yang ditentukan.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|---------|-----------------|--------|
| File OBJ muncul kosong | Profil tidak ditambahkan ke node | Pastikan `createChildNode` dipanggil pada node yang valid |
| Arah tampaknya tidak berubah | `setDirection` dipanggil setelah ekstrusi sudah dibangun | Atur arah di dalam inisialisasi `LinearExtrusion` seperti yang ditunjukkan |
| Mesh resolusi rendah | Nilai `setSlices` terlalu rendah | Tingkatkan jumlah slice (mis., 100 atau lebih) |

## Kesimpulan

Anda kini mengetahui **cara mengubah arah ekstrusi** dalam ekstrusi linear, cara menyesuaikan pengaturan twist dan slice, serta **mengekspor file model 3D OBJ** menggunakan Aspose.3D untuk Java. Teknik ini memberi Anda kontrol detail atas pembuatan geometri dan memudahkan integrasi aset 3‑D ke dalam alur kerja yang lebih besar.

## Pertanyaan yang Sering Diajukan

**Q:** Apakah saya dapat menggunakan Aspose.3D dengan bahasa pemrograman lain?  
**A:** Ya—Aspose.3D menyediakan API untuk .NET dan Java, memungkinkan pengembangan lintas platform.

**Q:** Apakah tersedia trial gratis untuk Aspose.3D?  
**A:** Tentu saja. Anda dapat menjelajahi semua fitur dengan trial gratis [here](https://releases.aspose.com/).

**Q:** Di mana saya dapat menemukan dokumentasi detail untuk Aspose.3D untuk Java?  
**A:** Referensi lengkap tersedia [here](https://reference.aspose.com/3d/java/).

**Q:** Bagaimana cara mendapatkan dukungan untuk Aspose.3D?  
**A:** Kunjungi forum resmi [Aspose.3D forum](https://forum.aspose.com/c/3d/18) untuk bantuan dari komunitas dan tim produk.

**Q:** Apakah lisensi sementara tersedia untuk pengujian?  
**A:** Ya—lisensi sementara dapat diperoleh [here](https://purchase.aspose.com/temporary-license/).

---

**Last Updated:** 2026-08-02  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose

{{< blocks/products/products-backtop-button >}}

## Tutorial Terkait

- [Cara Mengekstrusi Bentuk - Membuat Model 3D dengan Ekstrusi Linear di Java](/3d/java/linear-extrusion/)
- [Buat Ekstrusi 3D Java dengan Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Tutorial Grafik 3D Java – Pusat dalam Ekstrusi Linear](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}