---
date: 2026-05-14
description: Pelajari cara mengekspor STL di Java dengan membuat adegan 3D, menerapkan
  material PBR realistis menggunakan Aspose.3D, dan menyimpan model untuk rendering.
keywords:
- how to export stl
- Aspose 3D PBR materials
- Java 3D scene creation
linktitle: Cara Mengekspor STL di Java – Buat Adegan 3D dengan Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-05-14'
  description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  headline: How to Export STL in Java – Create 3D Scene with Aspose.3D
  type: TechArticle
- description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  name: How to Export STL in Java – Create 3D Scene with Aspose.3D
  steps:
  - name: '**Java Development Environment** – JDK 8 or newer installed.'
    text: '**Java Development Environment** – JDK 8 or newer installed.'
  - name: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
    text: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
  - name: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
    text: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
  - name: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
    text: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
  type: HowTo
- questions:
  - answer: It’s the process of building a `Scene` object that holds geometry, lights,
      and cameras in a Java application.
    question: What does “create 3d scene java” mean?
  - answer: Aspose.3D provides a ready‑made `PbrMaterial` class.
    question: Which library handles PBR materials?
  - answer: Yes – the `Scene.save` method supports STL (ASCII and binary).
    question: Can I export the result as STL?
  - answer: A permanent Aspose.3D license is required for commercial use; a temporary
      license works for testing.
    question: Do I need a license for production?
  - answer: Any Java 8+ runtime is supported.
    question: What Java version is required?
  type: FAQPage
second_title: Aspose.3D Java API
title: Cara Mengekspor STL di Java – Buat Adegan 3D dengan Aspose.3D
url: /id/java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Mengekspor STL di Java – Membuat Adegan 3D dengan Aspose.3D

## Pendahuluan

Dalam tutorial praktis ini Anda akan belajar **cara mengekspor STL** dari aplikasi Java dengan membangun adegan 3D lengkap, menerapkan material Physically Based Rendering (PBR), dan menyimpan hasilnya dengan Aspose.3D. Baik Anda menargetkan pencetakan 3D, pipeline mesin game, atau visualisasi produk, langkah‑langkah di bawah ini memberikan alur kerja yang dapat diulang, terkontrol versi, yang berfungsi pada runtime Java 8+ apa pun.

## Jawaban Cepat
- **Apa arti “create 3d scene java”?** Itu adalah proses membangun objek `Scene` yang menyimpan geometri, lampu, dan kamera dalam aplikasi Java.  
- **Perpustakaan mana yang menangani material PBR?** Aspose.3D menyediakan kelas `PbrMaterial` siap pakai.  
- **Apakah saya dapat mengekspor hasilnya sebagai STL?** Ya – metode `Scene.save` mendukung STL (ASCII dan biner).  
- **Apakah saya memerlukan lisensi untuk produksi?** Lisensi Aspose.3D permanen diperlukan untuk penggunaan komersial; lisensi sementara dapat digunakan untuk pengujian.  
- **Versi Java apa yang diperlukan?** Runtime Java 8+ apa pun didukung.

## Cara membuat adegan 3d java dengan Aspose.3D

`Scene` adalah kelas kontainer utama yang mewakili dokumen 3D. Muat, konfigurasikan, dan simpan sebuah adegan hanya dalam beberapa baris kode. Pertama, Anda membuat instance `Scene`, kemudian Anda melampirkan geometri dan `PbrMaterial`, dan akhirnya Anda memanggil `Scene.save` dengan format STL. Alur end‑to‑end ini memungkinkan Anda mengotomatisasi pembuatan aset tanpa pernah membuka editor 3D.

## Apa itu adegan 3D di Java?

Sebuah *scene* adalah kontainer yang menyimpan semua objek (node), geometri mereka, material, lampu, dan kamera. Anggaplah sebagai panggung virtual tempat Anda menempatkan model 3D Anda. Kelas `Scene` milik Aspose.3D memberikan cara yang bersih dan berorientasi‑objek untuk membangun panggung ini secara programatis.

## Mengapa menggunakan material PBR untuk merender objek 3D di Java?

PBR (Physically Based Rendering) meniru interaksi cahaya dunia nyata menggunakan parameter metallic dan roughness. Hasilnya adalah material yang tampak konsisten di bawah kondisi pencahayaan apa pun, yang penting untuk visualisasi produk realistis, AR/VR, dan mesin game modern. Dengan mengontrol peta metallic, roughness, albedo, dan normal, Anda dapat mencapai berbagai hasil permukaan—dari logam mengkilap hingga plastik matte—tanpa harus mengutak‑atik shader secara manual.

## Prasyarat

1. **Java Development Environment** – JDK 8 atau yang lebih baru terinstal.  
2. **Aspose.3D Library** – Unduh JAR terbaru dari [download link](https://releases.aspose.com/3d/java/).  
3. **Documentation** – Biasakan diri Anda dengan API melalui [documentation](https://reference.aspose.com/3d/java/) resmi.  
4. **Temporary License (Optional)** – Jika Anda tidak memiliki lisensi permanen, dapatkan [temporary license](https://purchase.aspose.com/temporary-license/) untuk pengujian.

## Kasus penggunaan umum

| Kasus penggunaan | Bagaimana tutorial membantu |
|------------------|-----------------------------|
| **Pencetakan 3‑D** | Mengekspor ke STL memungkinkan Anda mengirim model langsung ke slicer. |
| **Pipeline aset game** | Parameter material PBR sesuai dengan harapan mesin game modern. |
| **Konfigurator produk** | Mengotomatisasi variasi warna/finishing dengan menyesuaikan nilai metallic/roughness. |

## Impor Paket

Namespace `Aspose.3D` harus diimpor agar kompilator dapat menemukan kelas‑kelas yang digunakan dalam tutorial.

```java
import com.aspose.threed.*;
```

## Langkah 1: Inisialisasi Scene

`Scene` adalah kontainer utama untuk semua konten 3D. Membuat instance baru memberi Anda kanvas bersih yang dapat Anda tambahkan geometri, lampu, dan kamera.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **Tip pro:** Pastikan `MyDir` mengarah ke folder yang dapat ditulisi; jika tidak, panggilan `save` akan gagal.

## Langkah 2: Inisialisasi Material PBR

`PbrMaterial` mendefinisikan properti rendering berbasis fisik seperti metallic dan roughness. Sebuah `PbrMaterial` mendefinisikan nilai metallic, roughness, dan properti permukaan lainnya. Menetapkan faktor metallic tinggi (≈ 0.9) dan roughness 0.9 menghasilkan tampilan logam sikat yang realistis.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Mengapa nilai‑nilai ini?** Faktor metallic tinggi membuat permukaan berperilaku seperti logam, sementara roughness tinggi menambahkan difusi halus, mencegah tampilan cermin sempurna.

## Langkah 3: Buat Objek 3D dan Terapkan Material

Di sini kami menghasilkan geometri kotak sederhana, melampirkannya ke node akar adegan, dan menetapkan `PbrMaterial` yang baru saja kami buat.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Kesalahan umum:** Lupa menetapkan material pada node akan membuat objek memiliki tampilan default (bukan PBR).

## Langkah 4: Simpan Adegan 3D (Ekspor STL)

`Scene.save` menulis adegan ke file dalam format yang ditentukan. Ekspor seluruh adegan—termasuk kotak yang ditingkatkan dengan PBR—ke file STL. STL adalah format yang banyak didukung untuk pencetakan 3‑D dan pemeriksaan visual cepat.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

`FileFormat.STLBINARY` menentukan output STL biner, yang lebih kecil daripada ASCII. Anda juga dapat memilih `FileFormat.STLASCII` jika file yang dapat dibaca manusia lebih diinginkan.

## Mengapa ini penting

Parameter material yang konsisten memastikan setiap model yang dihasilkan terlihat sama di berbagai penampil dan kondisi pencahayaan. Otomatisasi memungkinkan Anda menghasilkan batch besar variasi dengan upaya minimal, sementara output STL lintas‑platform menjamin kompatibilitas dengan alat mulai dari Blender hingga slicer untuk printer 3‑D. Bersama‑sama, manfaat ini mempercepat pipeline pengembangan dan mengurangi kesalahan manual.

## Tips Pemecahan Masalah

| Masalah | Penyebab kemungkinan | Perbaikan |
|---------|----------------------|-----------|
| **File tidak tersimpan** | `MyDir` mengarah ke folder yang tidak ada atau tidak memiliki izin menulis | Pastikan direktori ada dan proses Java Anda memiliki akses menulis |
| **Material tampak datar** | Nilai Metallic/Roughness diatur ke 0 | Tingkatkan `setMetallicFactor` dan/atau `setRoughnessFactor` |
| **File STL tidak dapat dibuka** | Flag format file salah (ASCII vs Biner) untuk penampil | Gunakan enum `FileFormat` yang sesuai untuk penampil target Anda |

## Pertanyaan yang Sering Diajukan

**Q:** Dapatkah saya menggunakan Aspose.3D untuk proyek komersial?  
**A:** Ya. Beli lisensi komersial di [purchase page](https://purchase.aspose.com/buy).

**Q:** Bagaimana cara mendapatkan dukungan untuk Aspose.3D?  
**A:** Bergabunglah dengan komunitas di [Aspose.3D forum](https://forum.aspose.com/c/3d/18) untuk bantuan gratis, atau buka tiket dukungan dengan lisensi yang valid.

**Q:** Apakah ada versi percobaan gratis?  
**A:** Tentu saja. Unduh versi percobaan dari [free trial page](https://releases.aspose.com/).

**Q:** Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D?  
**A:** Semua referensi API tersedia di [documentation](https://reference.aspose.com/3d/java/) resmi.

**Q:** Bagaimana cara memperoleh lisensi sementara untuk pengujian?  
**A:** Minta melalui [temporary license link](https://purchase.aspose.com/temporary-license/).

---

**Terakhir Diperbarui:** 2026-05-14  
**Diuji Dengan:** Aspose.3D 24.12 (latest)  
**Penulis:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Tutorial Terkait

- [Buat Adegan 3D Java dengan Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [Cara Mengekspor Adegan ke FBX dan Mengambil Info Adegan 3D di Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Cara Mengekspor OBJ - Mengubah Orientasi Plane untuk Penempatan Adegan 3D yang Tepat di Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}