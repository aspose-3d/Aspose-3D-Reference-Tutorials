---
date: 2026-05-04
description: Pelajari cara mengekspor adegan ke FBX dan mengatur nama aplikasi Java
  menggunakan Aspose.3D untuk Java. Panduan langkah demi langkah ini juga menunjukkan
  cara mendefinisikan satuan ukuran dan mengambil informasi adegan 3D.
keywords:
- export scene to fbx
- set application name java
- aspose 3d java
linktitle: Cara Menyimpan FBX dan Mengambil Info Adegan 3D di Java
second_title: Aspose.3D Java API
title: Cara Mengekspor Adegan ke FBX dan Mengambil Info Adegan 3D di Java
url: /id/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Mengekspor Adegan ke FBX dan Mengambil Info Adegan 3D di Java

## Pendahuluan

Jika Anda mencari panduan yang jelas dan praktis tentang **cara mengekspor adegan ke FBX** sambil mengekstrak metadata berguna dari adegan 3D Anda, Anda berada di tempat yang tepat. Dalam tutorial ini kami akan membahas setiap langkah menggunakan perpustakaan **Aspose.3D Java**: mulai dari membuat adegan, **menetapkan nama aplikasi**, **mendefinisikan satuan pengukuran**, hingga akhirnya **mengekspor adegan ke FBX**. Pada akhir tutorial Anda akan memiliki file FBX siap pakai yang membawa informasi aset yang Anda perlukan untuk alur kerja hilir.

## Jawaban Cepat
- **Apa tujuan utama?** Mengekspor adegan ke FBX yang berisi informasi aset khusus.  
- **Perpustakaan mana yang digunakan?** Aspose.3D untuk Java.  
- **Apakah saya memerlukan lisensi?** Versi percobaan gratis cukup untuk pengembangan; lisensi komersial diperlukan untuk produksi.  
- **Bisakah saya mengubah satuan pengukuran?** Ya – gunakan `setUnitName` dan `setUnitScaleFactor`.  
- **Di mana output disimpan?** Ke jalur yang Anda tentukan dalam `scene.save(...)`.  

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- Pemahaman yang kuat tentang sintaks Java dasar.  
- **Aspose.3D untuk Java** yang diunduh dan ditambahkan ke proyek Anda (Anda dapat mendapatkannya dari halaman resmi) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- IDE Java favorit Anda (IntelliJ IDEA, Eclipse, NetBeans, dll.) yang telah dikonfigurasi dengan benar.

## Impor Paket

Di file sumber Java Anda, impor kelas Aspose.3D yang menyediakan penanganan adegan dan dukungan format file.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Jaga daftar impor tetap minimal untuk menghindari ketergantungan yang tidak perlu dan mempercepat waktu kompilasi.

## Apa proses untuk menyimpan file FBX?

Berikut adalah panduan singkat langkah‑demi‑langkah yang menunjukkan **cara menambahkan informasi aset** ke sebuah adegan dan kemudian **mengekspor adegan ke FBX**.

### Langkah 1: Inisialisasi Adegan 3D

Pertama, buat objek `Scene` kosong. Ini akan menjadi wadah untuk semua geometri, lampu, kamera, dan metadata aset.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Cara mengatur nama aplikasi di Java

Menambahkan metadata khusus membantu alat hilir mengidentifikasi sumber file. Gunakan objek `AssetInfo` untuk **menetapkan nama aplikasi** (dan vendor) sebelum Anda menyimpan file.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Mengapa ini penting:** Banyak alur kerja menyaring atau menandai aset berdasarkan aplikasi asal, sehingga langkah ini penting untuk proyek berskala besar.

### Langkah 3: Tentukan Satuan Pengukuran

Aspose.3D memungkinkan Anda menentukan sistem satuan yang digunakan adegan Anda. Dalam contoh ini kami menggunakan satuan Mesir kuno yang disebut “pole” dengan faktor skala khusus.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Sesuaikan `unitScaleFactor` agar cocok dengan ukuran dunia nyata model Anda; 1.0 mewakili pemetaan 1‑ke‑1 dengan satuan yang dipilih.

### Langkah 4: Ekspor Adegan ke FBX

Sekarang informasi aset sudah terlampir, kami menyimpan adegan sebagai file FBX. Opsi `FileFormat.FBX7500ASCII` menghasilkan FBX ASCII yang dapat dibaca manusia, sangat berguna untuk debugging.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Ingat:** Ganti `"Your Document Directory"` dengan jalur absolut atau jalur relatif terhadap direktori kerja proyek Anda.

### Langkah 5: Cetak Pesan Keberhasilan

Output konsol sederhana mengonfirmasi bahwa operasi berhasil dan memberi tahu Anda di mana file ditulis.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Mengapa mengekspor adegan ke FBX dengan Aspose.3D?

Mengekspor ke FBX adalah kebutuhan umum karena FBX didukung secara luas oleh mesin game, alat DCC, dan alur kerja AR/VR. Aspose.3D memberi Anda kontrol penuh atas file yang diekspor—metadata, satuan, dan geometri—tanpa memerlukan aplikasi authoring 3D yang berat. Ini membuat pembuatan aset otomatis, pemrosesan batch, dan konversi sisi server menjadi cepat dan dapat diandalkan.

## Kasus Penggunaan Umum

- **Pipeline aset game** – menyematkan informasi pembuat langsung dalam file FBX untuk pelacakan versi.  
- **Visualisasi arsitektural** – menyimpan satuan khusus proyek untuk menghindari kesalahan skala saat diimpor ke mesin rendering.  
- **Pelaporan otomatis** – menghasilkan file FBX secara langsung dengan metadata yang dapat dibaca oleh alat analitik hilir.  
- **Layanan 3D berbasis cloud** – membuat dan mengekspor adegan secara programatik tanpa GUI, cocok untuk platform SaaS.

## Pemecahan Masalah & Tips

| Masalah | Solusi |
|-------|----------|
| **File tidak ditemukan setelah penyimpanan** | Pastikan `MyDir` mengarah ke folder yang ada dan aplikasi Anda memiliki izin menulis. |
| **Satuan terlihat tidak tepat di penampil eksternal** | Periksa kembali `unitScaleFactor`; beberapa penampil mengharapkan meter sebagai satuan dasar. |
| **Metadata aset tidak muncul** | Pastikan Anda memanggil `scene.getAssetInfo()` **sebelum** menyimpan; perubahan setelah `save()` tidak akan dipertahankan. |
| **Bottleneck kinerja pada adegan besar** | Gunakan `scene.optimize()` sebelum menyimpan untuk mengurangi penggunaan memori. |
| **ASCII FBX terlalu besar** | Beralih ke FBX biner dengan menggunakan `FileFormat.FBX7500` (lihat FAQ). |

## Pertanyaan yang Sering Diajukan

**Q: Bagaimana cara mengubah format output menjadi FBX biner?**  
A: Ganti `FileFormat.FBX7500ASCII` dengan `FileFormat.FBX7500` saat memanggil `scene.save(...)`.

**Q: Bisakah saya menambahkan metadata yang didefinisikan pengguna selain bidang aset bawaan?**  
A: Ya, gunakan `scene.getUserData().add("Key", "Value")` untuk menyematkan pasangan kunci‑nilai tambahan.

**Q: Apakah Aspose.3D mendukung format ekspor lain seperti OBJ atau GLTF?**  
A: Ya. Cukup ubah enum `FileFormat` menjadi `OBJ` atau `GLTF2` sesuai kebutuhan.

**Q: Versi Java apa yang diperlukan?**  
A: Aspose.3D untuk Java mendukung Java 8 dan yang lebih baru.

**Q: Apakah memungkinkan memuat FBX yang sudah ada, mengubah info asetnya, dan menyimpannya kembali?**  
A: Tentu saja. Muat file dengan `new Scene("input.fbx")`, ubah `scene.getAssetInfo()`, lalu simpan.

## Kesimpulan

Anda kini memiliki alur kerja lengkap yang siap produksi untuk **mengekspor adegan ke FBX** sambil menyematkan informasi aset berharga seperti nama aplikasi, vendor, dan satuan pengukuran khusus. Pendekatan ini menyederhanakan manajemen aset, mengurangi pencatatan manual, dan memastikan bahwa alat hilir menerima semua konteks yang mereka butuhkan. Jangan ragu untuk menjelajahi format ekspor lain, menambahkan data pengguna khusus, atau mengintegrasikan kode ini ke dalam pipeline otomasi yang lebih besar.

---

**Terakhir Diperbarui:** 2026-05-04  
**Diuji Dengan:** Aspose.3D untuk Java 24.11  
**Penulis:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}