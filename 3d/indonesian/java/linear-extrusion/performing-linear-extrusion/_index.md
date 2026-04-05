---
date: 2026-02-25
description: Pelajari cara membuat ekstrusi 3D di Java dengan Aspose.3D dan mengekspor
  file OBJ di Java, menghasilkan model 3D berkualitas tinggi dalam aplikasi Java.
linktitle: Create 3D Extrusion Java with Aspose.3D
second_title: Aspose.3D Java API
title: Buat Ekstrusi 3D Java dengan Aspose.3D
url: /id/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

 (maybe keep as is). Translate label: "**Terakhir Diperbarui:**". "Tested With:" => "**Diuji Dengan:**". "Author:" => "**Penulis:**". Keep values unchanged.

Then close shortcodes.

Now produce final output with all content.

Be careful to keep shortcodes unchanged.

Let's craft final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat 3D Extrusion Java dengan Aspose.3D

## Pendahuluan

Jika Anda perlu **create 3d extrusion java** dengan cepat dan dapat diandalkan, Anda berada di tutorial yang tepat. Dalam beberapa menit ke depan kami akan menjelaskan cara menghasilkan linear extrusion, menyesuaikan geometri, dan **export obj file java** menggunakan pustaka Aspose.3D. Baik Anda sedang membangun alat mirip CAD, pipeline aset game, atau alur kerja 3‑D berbasis Java apa pun, panduan ini memberi Anda dasar yang kuat dan siap produksi.

## Jawaban Cepat
- **Apa arti “linear extrusion”?** Ia menggesek profil 2‑D sepanjang garis lurus untuk membentuk padatan 3‑D.  
- **Library mana yang menangani extrusion?** Aspose.3D untuk Java menyediakan API tingkat tinggi.  
- **Bisakah saya mengekspor hasilnya sebagai OBJ?** Ya – tutorial berakhir dengan `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Apakah saya memerlukan lisensi untuk pengembangan?** Versi percobaan gratis cukup untuk belajar; lisensi komersial diperlukan untuk produksi.  
- **Versi Java apa yang didukung?** Java 1.6 dan yang lebih baru.

## Apa itu Create 3D Extrusion Java?
Membuat 3D extrusion di Java berarti mengambil bentuk 2‑D sederhana (seperti persegi panjang) dan memperluasnya ke dimensi ketiga. Mesh yang dihasilkan dapat disimpan dalam format umum seperti OBJ, yang dipahami banyak editor 3‑D.

## Mengapa Menggunakan Aspose.3D untuk Linear Extrusion?
- **Pure Java API** – tanpa dependensi native, sempurna untuk proyek lintas‑platform.  
- **Kontrol geometri kaya** – rounding, twist, slices, dan offset semuanya tersedia melalui properti sederhana.  
- **Ekspor langsung** – simpan ke OBJ, STL, FBX, dan lainnya tanpa konverter tambahan.  
- **Dukungan tingkat perusahaan** – lisensi, dokumentasi, dan forum komunitas tersedia dengan mudah.

## Prasyarat

Sebelum Anda memulai, pastikan Anda memiliki:

1. **Lingkungan Pengembangan Java** – JDK 1.6+ terpasang dan terkonfigurasi.  
2. **Pustaka Aspose.3D** – Unduh JAR terbaru dari situs resmi [di sini](https://releases.aspose.com/3d/java/).  

## Impor Paket

Tambahkan namespace inti Aspose.3D ke file sumber Java Anda:

```java
import com.aspose.threed.*;
```

## Langkah 1: Atur Direktori Dokumen

Tentukan lokasi dimana file yang dihasilkan akan ditulis:

```java
String MyDir = "Your Document Directory";
```

> **Tips pro:** Gunakan path absolut atau properti yang dapat dikonfigurasi sehingga lokasi output berfungsi di berbagai lingkungan.

## Langkah 2: Inisialisasi Bentuk Dasar

Buat persegi panjang yang akan menjadi profil extrusion. Radius pembulatan melunakkan sudut:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Anda dapat bereksperimen dengan `setRoundingRadius` untuk mendapatkan profil yang lebih bulat atau lebih tajam.

## Langkah 3: Lakukan Linear Extrusion

Sekarang kami mengubah persegi panjang 2‑D menjadi objek 3‑D. Konstruktor mengambil profil dan kedalaman extrusion (10 unit dalam kasus ini). Properti tambahan menyempurnakan mesh:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Slices** – mengontrol kelancaran extrusion.  
- **Center** – menyejajarkan geometri di sekitar origin.  
- **Twist** – memutar profil sepanjang sumbu extrusion (di sini 360° penuh).  
- **TwistOffset** – memindahkan pivot twist, menunjukkan cara membuat spiral.

## Langkah 4: Buat 3D Scene

`Scene` adalah wadah untuk semua objek 3‑D. Menambahkan extrusion sebagai node anak menjadikannya bagian dari grafik scene:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Langkah 5: Simpan 3D Scene

Akhirnya, ekspor scene ke file Wavefront OBJ – format yang banyak didukung oleh editor 3‑D, mesin game, dan pipeline pencetakan:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Setelah menjalankan kode, Anda akan menemukan **LinearExtrusion.obj** di direktori yang Anda tentukan, siap dibuka di Blender, Maya, atau penampil lain yang kompatibel dengan OBJ.

## Masalah Umum dan Solusinya

| Gejala | Penyebab Kemungkinan | Perbaikan |
|---------|----------------------|-----------|
| `FileNotFoundException` saat menyimpan | `MyDir` tidak ada atau tidak memiliki izin menulis | Buat folder terlebih dahulu atau gunakan path absolut dengan izin yang tepat. |
| OBJ muncul kosong di penampil | Tidak ada geometri yang ditambahkan ke scene | Verifikasi bahwa objek `LinearExtrusion` telah diinstansiasi dengan benar dan terpasang pada node root. |
| Twist terlihat salah | Nilai `TwistOffset` tidak tepat | Sesuaikan koordinat `Vector3`; ingat offset diterapkan sebelum rotasi twist. |

## Pertanyaan yang Sering Diajukan

### Q1: Apakah Aspose.3D kompatibel dengan semua versi Java?
A1: Aspose.3D dirancang untuk bekerja dengan Java 1.6 dan versi yang lebih baru.

### Q2: Apakah saya dapat menggunakan Aspose.3D untuk proyek komersial?
A2: Ya, Aspose.3D dapat digunakan untuk proyek pribadi maupun komersial. Periksa detail lisensi [di sini](https://purchase.aspose.com/buy).

### Q3: Bagaimana saya dapat mendapatkan dukungan untuk Aspose.3D?
A3: Kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas atau pertimbangkan membeli [lisensi sementara](https://purchase.aspose.com/temporary-license/) untuk dukungan premium.

### Q4: Apakah ada fitur pemodelan 3D lain di Aspose.3D?
A4: Tentu! Jelajahi dokumentasi lengkap [di sini](https://reference.aspose.com/3d/java/) untuk daftar fitur dan contoh yang komprehensif.

### Q5: Apakah tersedia percobaan gratis untuk Aspose.3D?
A5: Ya, Anda dapat mengakses percobaan gratis [di sini](https://releases.aspose.com/).

## Kesimpulan

Anda sekarang tahu cara **create 3d extrusion java** dengan Aspose.3D, menyesuaikan geometri, dan **export obj file java** untuk penggunaan selanjutnya. Bereksperimenlah dengan profil, twist, dan format ekspor yang berbeda untuk memenuhi kebutuhan proyek spesifik Anda. Saat siap, jelajahi kemampuan Aspose.3D lainnya seperti manipulasi mesh, pemetaan tekstur, dan animasi untuk memperkaya aplikasi 3‑D berbasis Java Anda.

---

**Terakhir Diperbarui:** 2026-02-25  
**Diuji Dengan:** Aspose.3D 24.12 for Java  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}