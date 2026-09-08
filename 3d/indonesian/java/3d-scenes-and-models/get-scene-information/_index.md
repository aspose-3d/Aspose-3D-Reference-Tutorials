---
date: 2026-09-08
description: Pelajari cara mendefinisikan satuan dan mengekspor adegan ke FBX dalam
  Java menggunakan Aspose.3D. Panduan langkah demi langkah ini menunjukkan cara mengatur
  nama aplikasi, satuan pengukuran, dan mengambil informasi adegan 3D.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Cara Menyimpan FBX dan Mengambil Info Adegan 3D dalam Java
og_description: Pelajari cara mendefinisikan satuan dan mengekspor adegan ke FBX dalam
  Java dengan Aspose.3D. Panduan ini mencakup pengaturan nama aplikasi, satuan pengukuran,
  dan pengambilan info adegan 3D dalam beberapa langkah.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Cara mendefinisikan satuan dan mengekspor adegan ke FBX dalam Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Cara mendefinisikan satuan dan mengekspor adegan ke FBX dalam Java
url: /id/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara mendefinisikan satuan dan mengekspor adegan ke FBX di Java

## Pendahuluan

Jika Anda mencari panduan praktis yang jelas tentang **cara mendefinisikan satuan** dan **mengekspor adegan ke FBX** sambil mengekstrak metadata berguna dari adegan 3D Anda, Anda berada di tempat yang tepat. Dalam tutorial ini kami akan membahas setiap langkah menggunakan perpustakaan **Aspose.3D for Java**: mulai dari membuat adegan, **menetapkan nama aplikasi**, **mendefinisikan satuan pengukuran**, hingga akhirnya **mengekspor adegan ke FBX**. Pada akhir tutorial Anda akan memiliki file FBX siap pakai yang membawa informasi aset yang Anda perlukan untuk pipeline hilir.

## Jawaban Cepat
- **Apa tujuan utama?** Mengekspor adegan ke FBX yang berisi informasi aset khusus.  
- **Perpustakaan apa yang digunakan?** Aspose.3D for Java.  
- **Apakah saya memerlukan lisensi?** Versi percobaan gratis cukup untuk pengembangan; lisensi komersial diperlukan untuk produksi.  
- **Bisakah saya mengubah satuan pengukuran?** Ya – gunakan `setUnitName` dan `setUnitScaleFactor`.  
- **Di mana output disimpan?** Ke jalur yang Anda tentukan dalam `scene.save(...)`.  

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- Pemahaman yang kuat tentang sintaks Java dasar.  
- **Aspose.3D for Java** yang diunduh dan ditambahkan ke proyek Anda (Anda dapat mendapatkannya dari halaman resmi) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- IDE Java favorit Anda (IntelliJ IDEA, Eclipse, NetBeans, dll.) yang dikonfigurasi dengan benar.

## Impor paket

Di file sumber Java Anda, impor kelas Aspose.3D yang menyediakan penanganan adegan dan dukungan format file.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Tip Pro:** Jaga daftar impor tetap minimal untuk menghindari dependensi yang tidak perlu dan meningkatkan waktu kompilasi.

## Apa proses untuk menyimpan file FBX?

Untuk menyimpan sebuah adegan sebagai file FBX, Anda membuat `Scene`, menetapkan metadata aset yang diinginkan, mendefinisikan satuan pengukuran, dan kemudian memanggil `scene.save(path, FileFormat.FBX7500ASCII)`. Urutan ini menulis geometri, material, dan metadata ke dalam FBX ASCII yang dapat diperiksa atau diimpor oleh alat hilir.

### Langkah 1: inisialisasi adegan 3D

Kelas `Scene` adalah kontainer tingkat atas Aspose.3D yang mewakili seluruh adegan 3D, termasuk geometri, cahaya, kamera, dan metadata. Pertama, buat objek `Scene` kosong. Ini akan menjadi kontainer untuk semua geometri, cahaya, kamera, dan metadata aset.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Cara menetapkan nama aplikasi di Java

Objek `AssetInfo` menyimpan metadata seperti nama aplikasi, vendor, dan versi untuk adegan. Menambahkan metadata khusus membantu alat hilir mengidentifikasi sumber file. Gunakan objek `AssetInfo` untuk **menetapkan nama aplikasi** (dan vendor) sebelum Anda menyimpan file.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Mengapa ini penting:** Banyak pipeline menyaring atau menandai aset berdasarkan aplikasi asal, menjadikan langkah ini penting untuk proyek besar.

### Langkah 3: definisikan satuan pengukuran

Sistem satuan menentukan skala dunia nyata dari adegan; Aspose.3D memungkinkan Anda menentukan nama satuan dan faktor skala relatif terhadap meter. Dalam contoh ini kami menggunakan satuan Mesir kuno yang disebut “pole” dengan faktor skala khusus.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Sesuaikan `unitScaleFactor` agar cocok dengan ukuran dunia nyata model Anda; 1.0 mewakili pemetaan 1‑ke‑1 dengan satuan yang dipilih.

### Langkah 4: ekspor adegan ke FBX

Sekarang informasi aset sudah terlampir, kami menyimpan adegan sebagai file FBX. Opsi `FileFormat.FBX7500ASCII` menghasilkan FBX ASCII yang dapat dibaca manusia, yang berguna untuk debugging.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Ingat:** Ganti `"Your Document Directory"` dengan jalur absolut atau jalur relatif terhadap direktori kerja proyek Anda.

## Mengapa mengekspor adegan ke FBX dengan Aspose.3D?

Aspose.3D mendukung **lebih dari 50 format input dan output** dan dapat memproses adegan ratusan halaman tanpa memuat seluruh file ke memori, memberi Anda kontrol penuh atas file yang diekspor—metadata, satuan, dan geometri—tanpa memerlukan aplikasi authoring 3D yang berat. Hal ini membuat pembuatan aset otomatis, pemrosesan batch, dan konversi sisi server menjadi cepat dan dapat diandalkan.

## Kasus penggunaan umum

- **Pipeline aset game** – menyematkan informasi pembuat langsung dalam file FBX untuk pelacakan versi.  
- **Visualisasi arsitektural** – menyimpan satuan khusus proyek untuk menghindari kesalahan skala saat mengimpor ke mesin rendering.  
- **Pelaporan otomatis** – menghasilkan file FBX secara langsung dengan metadata yang dapat dibaca oleh alat analitik hilir.  
- **Layanan 3D berbasis cloud** – secara programatis membuat dan mengekspor adegan tanpa GUI, cocok untuk platform SaaS.

## Pemecahan Masalah & Tips

| Masalah | Solusi |
|-------|----------|
| **File tidak ditemukan setelah disimpan** | Verifikasi bahwa `MyDir` mengarah ke folder yang ada dan aplikasi Anda memiliki izin menulis. |
| **Satuan terlihat tidak tepat di penampil eksternal** | Periksa kembali `unitScaleFactor`; beberapa penampil mengharapkan meter sebagai satuan dasar. |
| **Metadata aset hilang** | Pastikan Anda memanggil `scene.getAssetInfo()` **sebelum** menyimpan; perubahan setelah `save()` tidak akan disimpan. |
| **Bottleneck kinerja pada adegan besar** | Gunakan `scene.optimize()` sebelum menyimpan untuk mengurangi penggunaan memori. |
| **FBX ASCII terlalu besar** | Beralih ke FBX biner dengan menggunakan `FileFormat.FBX7500` (lihat FAQ). |

## Pertanyaan yang Sering Diajukan

**T: Bagaimana cara mengubah format output menjadi FBX biner?**  
J: Ganti `FileFormat.FBX7500ASCII` dengan `FileFormat.FBX7500` saat memanggil `scene.save(...)`.

**T: Bisakah saya menambahkan metadata yang ditentukan pengguna selain bidang aset bawaan?**  
J: Ya, gunakan `scene.getUserData().add("Key", "Value")` untuk menyematkan pasangan kunci‑nilai tambahan.

**T: Apakah Aspose.3D mendukung format ekspor lain seperti OBJ atau GLTF?**  
J: Ya. Cukup ubah enum `FileFormat` menjadi `OBJ` atau `GLTF2` sesuai kebutuhan.

**T: Versi Java apa yang diperlukan?**  
J: Aspose.3D for Java mendukung Java 8 dan yang lebih baru.

**T: Apakah memungkinkan memuat FBX yang ada, mengubah info asetnya, dan menyimpannya kembali?**  
J: Tentu saja. Muat file dengan `new Scene("input.fbx")`, ubah `scene.getAssetInfo()`, lalu simpan.

---

**Terakhir Diperbarui:** 2026-09-08  
**Diuji Dengan:** Aspose.3D for Java 24.11  
**Penulis:** Aspose

## Tutorial Terkait

- [Kurangi Ukuran File 3D – Kompres Adegan dengan Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Cara mengatur warna vector3 java: Ubah Warna Diffuse dan Kelola Properti 3D dalam Adegan Java menggunakan Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}