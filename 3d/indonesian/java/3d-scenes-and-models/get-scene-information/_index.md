---
date: 2025-12-06
description: Pelajari cara menyimpan file FBX dan mengambil informasi adegan menggunakan
  Aspose.3D untuk Java. Panduan langkah demi langkah ini mencakup pengaturan nama
  aplikasi, penentuan satuan pengukuran, dan mengekspor adegan ke FBX.
language: id
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Cara Menyimpan FBX dan Mengambil Info Adegan 3D di Java
url: /java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Menyimpan FBX dan Mengambil Info Adegan 3D di Java

## Pendahuluan

Jika Anda mencari panduan yang jelas dan langsung tentang **cara menyimpan fbx** sambil mengekstrak metadata berguna dari adegan 3D Anda, Anda berada di tempat yang tepat. Dalam tutorial ini kami akan membimbing Anda melalui setiap langkah menggunakan perpustakaan **Aspose.3D Java**: mulai dari membuat adegan, **menetapkan nama aplikasi**, **mendefinisikan satuan pengukuran**, hingga akhirnya **mengekspor adegan ke FBX**. Pada akhir tutorial Anda akan memiliki file FBX siap pakai yang membawa informasi aset yang Anda perlukan untuk pipeline hilir.

## Jawaban Cepat
- **Apa tujuan utama?** Simpan file FBX yang berisi informasi aset khusus.  
- **Perpustakaan apa yang digunakan?** Aspose.3D untuk Java.  
- **Apakah saya memerlukan lisensi?** Versi percobaan gratis dapat digunakan untuk pengembangan; lisensi komersial diperlukan untuk produksi.  
- **Bisakah saya mengubah satuan pengukuran?** Ya – gunakan `setUnitName` dan `setUnitScaleFactor`.  
- **Di mana output disimpan?** Ke jalur yang Anda tentukan dalam `scene.save(...)`.

## Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- Pemahaman yang kuat tentang sintaks Java dasar.  
- **Aspose.3D for Java** yang diunduh dan ditambahkan ke proyek Anda (Anda dapat mendapatkannya dari halaman resmi [Aspose 3D download page](https://releases.aspose.com/3d/java/)).  
- IDE Java favorit Anda (IntelliJ IDEA, Eclipse, NetBeans, dll.) dikonfigurasi dengan benar.

## Impor Paket

Di file sumber Java Anda, impor kelas Aspose.3D yang menyediakan penanganan adegan dan dukungan format file.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Jaga daftar impor tetap minimal untuk menghindari dependensi yang tidak perlu dan mempercepat waktu kompilasi.

## Apa proses untuk menyimpan file FBX?

Berikut adalah panduan singkat langkah‑demi‑langkah yang menunjukkan **cara menambahkan informasi aset** ke sebuah adegan dan kemudian **mengekspor adegan ke FBX**.

### Langkah 1: Inisialisasi Adegan 3D

Pertama, buat objek `Scene` kosong. Ini akan menjadi wadah untuk semua geometri, cahaya, kamera, dan metadata aset.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Langkah 2: Atur Informasi Aplikasi dan Vendor

Menambahkan metadata khusus membantu alat hilir mengidentifikasi sumber file. Di sini kami **menetapkan nama aplikasi** dan vendor menggunakan objek `AssetInfo`.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Mengapa ini penting:** Banyak pipeline menyaring atau menandai aset berdasarkan aplikasi asal, sehingga langkah ini penting untuk proyek berskala besar.

### Langkah 3: Definisikan Satuan Pengukuran

Aspose.3D memungkinkan Anda menentukan sistem satuan yang digunakan adegan Anda. Dalam contoh ini kami menggunakan satuan Mesir kuno yang disebut “pole” dengan faktor skala khusus.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Sesuaikan `unitScaleFactor` agar cocok dengan ukuran dunia nyata model Anda; 1.0 mewakili pemetaan 1‑ke‑1 dengan satuan yang dipilih.

### Langkah 4: Ekspor Adegan ke FBX

Set informasi aset terlampir, kami menyimpan adegan sebagai file FBX. Opsi `FileFormat.FBX7500ASCII` menghasilkan FBX ASCII yang dapat dibaca manusia, sangat berguna untuk debugging.

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

## Kasus Penggunaan Umum

- **Pipeline aset game** – sematkan informasi pembuat langsung dalam file FBX untuk pelacakan versi.  
- **Visualisasi arsitektural** – simpan satuan spesifik proyek untuk menghindari kesalahan skala saat mengimpor ke mesin rendering.  
- **Pelaporan otomatis** – menghasilkan file FBX secara langsung dengan metadata yang dapat dibaca oleh alat analitik hilir.

## Pemecahan Masalah & Tips

| Masalah | Solusi |
|-------|----------|
| **File tidak ditemukan setelah penyimpanan** | Pastikan `MyDir` mengarah ke folder yang ada dan aplikasi Anda memiliki izin menulis. |
| **Satuan terlihat tidak tepat di penampil eksternal** | Periksa kembali `unitScaleFactor`; beberapa penampil mengharapkan meter sebagai satuan dasar. |
| **Metadata aset hilang** | Pastikan Anda memanggil `scene.getAssetInfo()` **sebelum** menyimpan; perubahan setelah `save()` tidak akan dipertahankan. |

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan semua IDE Java?

A1: Ya, Aspose.3D dirancang untuk bekerja mulus dengan semua IDE Java utama.

### Q2: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?

A2: Tentu saja. Aspose.3D menawarkan lisensi komersial untuk pengembang, memastikan Anda mematuhi persyaratan lisensi.

### Q3: Di mana saya dapat menemukan dukungan tambahan untuk Aspose.3D?

A3: Untuk pertanyaan atau bantuan, kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Apakah ada versi percobaan gratis untuk Aspose.3D?

A4: Ya, Anda dapat menjelajahi fitur dengan versi percobaan gratis yang tersedia [di sini](https://releases.aspose.com/).

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

A5: Dapatkan lisensi sementara untuk tujuan pengujian [di sini](https://purchase.aspose.com/temporary-license/).

## Pertanyaan yang Sering Diajukan

**Q: Bagaimana cara mengubah format output menjadi FBX biner?**  
A: Ganti `FileFormat.FBX7500ASCII` dengan `FileFormat.FBX7500` saat memanggil `scene.save(...)`.

**Q: Bisakah saya menambahkan metadata yang didefinisikan pengguna selain bidang aset bawaan?**  
A: Ya, gunakan `scene.getUserData().add("Key", "Value")` untuk menyematkan pasangan kunci‑nilai tambahan.

**Q: Apakah Aspose.3D mendukung format ekspor lain seperti OBJ atau GLTF?**  
A: Ya. Cukup ubah enum `FileFormat` menjadi `OBJ` atau `GLTF2` sesuai kebutuhan.

**Q: Versi Java apa yang diperlukan?**  
A: Aspose.3D untuk Java mendukung Java 8 dan yang lebih baru.

**Q: Apakah memungkinkan memuat FBX yang ada, mengubah info asetnya, dan menyimpannya kembali?**  
A: Tentu saja. Muat file dengan `new Scene("input.fbx")`, ubah `scene.getAssetInfo()`, lalu simpan kembali.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Terakhir Diperbarui:** 2025-12-06  
**Diuji Dengan:** Aspose.3D for Java 24.11  
**Penulis:** Aspose