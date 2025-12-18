---
date: 2025-12-18
description: Pelajari cara mengekstrusi bentuk di Java menggunakan Aspose.3D, buat
  adegan 3D, dan ekspor file Wavefront OBJ dengan mudah.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Cara Mengekstrusi Bentuk di Java dengan Aspose.3D Ekstrusi Linear
url: /id/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Melakukan Linear Extrusion di Aspose.3D untuk Java

## Pendahuluan

Selamat datang di tutorial komprehensif ini tentang **how to extrude shape** di Aspose.3D untuk Java! Jika Anda ingin meningkatkan keterampilan pemodelan 3D menggunakan Java, Anda berada di tempat yang tepat. Kami akan memandu Anda melalui pembuatan 3D scene, melakukan linear extrusion, dan mengekspor hasilnya sebagai file Wavefront OBJ—semua dengan contoh kode yang jelas langkah demi langkah.

## Jawaban Cepat
- **Apa itu linear extrusion?** Memperpanjang profil 2D sepanjang jalur lurus untuk membuat padatan 3D.  
- **Pustaka mana yang menangani ini di Java?** Aspose.3D untuk Java.  
- **Bisakah saya mengekspor ke OBJ?** Ya, menggunakan fitur ekspor Wavefront OBJ.  
- **Apakah saya memerlukan lisensi untuk pengembangan?** Versi percobaan gratis dapat digunakan untuk pengujian; lisensi diperlukan untuk produksi.  
- **Versi Java apa yang diperlukan?** Java 1.6 atau lebih baru.

## Apa itu “how to extrude shape”?

Linear extrusion adalah teknik dasar dalam **3d modeling java** yang mengubah profil datar—seperti persegi panjang—menjadi objek volumetrik dengan menariknya sepanjang jarak yang ditentukan. Metode ini banyak digunakan untuk membuat komponen mekanik, elemen arsitektur, dan model dekoratif.

## Mengapa menggunakan Aspose.3D untuk linear extrusion?
- **Kontrol penuh** atas geometri (slices, twist, offset).  
- **Integrasi mulus** dengan proyek Java—tanpa ketergantungan native.  
- **Ekspor bawaan** untuk format populer, termasuk Wavefront OBJ, memudahkan **generate 3d model** file untuk alur kerja downstream.

## Prasyarat

Sebelum menyelam ke tutorial, pastikan Anda memiliki prasyarat berikut:

1 **Lingkungan Pengembangan Java** – JDK (1.6 atau lebih baru) dan IDE favorit Anda.  
2. **Pustaka Aspose.3D** – unduh dan instal pustaka dari situs resmi **[di sini](https://releases.aspose.com/3d/java/)**.

## Impor Paket

Setelah Anda menyiapkan lingkungan pengembangan dan menginstal pustaka Aspose.3D, impor paket yang diperlukan:

```java
import com.aspose.threed.*;
```

### Langkah 1: Atur Direktori Dokumen

Tentukan folder tempat file yang dihasilkan akan disimpan:

```java
String MyDir = "Your Document Directory";
```

> Ini memastikan bahwa operasi **generate 3d model** menulis file OBJ ke lokasi yang diketahui.

### Langkah 2: Inisialisasi Bentuk Dasar

Buat persegi panjang yang akan menjadi profil ekstrusi:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Anda dapat menyesuaikan radius pembulatan untuk mendapatkan sudut melengkung atau mengaturnya ke `0` untuk persegi panjang sempurna.

### Langkah 3: Lakukan Linear Extrusion

Sekarang kita mengekstrusi persegi panjang sepanjang sumbu Z, menambahkan slices, mengaktifkan centering, dan menerapkan twist dengan offset:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Panjang ekstrusi** – `10` unit.  
- **Slices** – `100` untuk geometri halus.  
- **Twist** – `360°` menghasilkan rotasi penuh.  
- **Twist offset** – memindahkan asal twist ke `(10, 0, 0)`.

### Langkah 4: Buat 3D Scene

Buat kontainer scene dan tambahkan ekstrusi sebagai node anak. Langkah ini **creates 3d scene** yang dapat menampung banyak objek:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Langkah 5: Simpan 3D Scene

Ekspor scene ke file Wavefront OBJ. Ini menunjukkan kemampuan **wavefront obj export** dan **save 3d obj**:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Setelah menjalankan kode, Anda akan menemukan `LinearExtrusion.obj` di direktori yang Anda tentukan, siap dibuka di viewer 3D apa pun atau diproses lebih lanjut.

## Masalah Umum dan Solusinya

| Masalah | Alasan | Solusi |
|-------|--------|-----|
| File OBJ kosong | Path direktori output tidak benar atau tidak dapat ditulis | Verifikasi bahwa `MyDir` mengarah ke folder yang ada dengan izin menulis. |
| Twist tidak diterapkan | `setCenter(true)` tidak disertakan | Pastikan centering diaktifkan atau sesuaikan nilai `setTwistOffset`. |
| Kesalahan kompilasi pada `LinearExtrusion` | Menggunakan versi Aspose.3D yang lebih lama | Perbarui ke rilis Aspose.3D terbaru. |

## Pertanyaan yang Sering Diajukan

**T: Apakah Aspose.3D kompatibel dengan semua versi Java?**  
J: Aspose.3D bekerja dengan Java 1.6 ke atas.

**T: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?**  
J: Ya, penggunaan komersial diizinkan dengan lisensi yang valid. Anda dapat memperoleh lisensi **[di sini](https://purchase.aspose.com/buy)**.

**T: Di mana saya dapat mendapatkan dukungan jika mengalami masalah?**  
J: Kunjungi **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)** untuk bantuan komunitas atau beli **[lisensi sementara](https://purchase.aspose.com/temporary-license/)** untuk dukungan premium.

**T: Fitur pemodelan 3D apa lagi yang disediakan Aspose.3D?**  
J: Pustaka ini mencakup manipulasi mesh, operasi Boolean, pemetaan tekstur, dan lainnya. Lihat daftar lengkap **[di sini](https://reference.aspose.com/3d/java/)**.

**T: Apakah tersedia versi percobaan gratis?**  
J: Ya, Anda dapat mengunduh versi percobaan **[di sini](https://releases.aspose.com/)**.

## Kesimpulan

Anda kini telah mempelajari **how to extrude shape** menggunakan Aspose.3D untuk Java, membuat 3D scene, dan mengekspor hasilnya sebagai file Wavefront OBJ. Teknik ini membuka pintu ke berbagai proyek **3d modeling java**—dari bagian sederhana hingga perakitan kompleks. Jelajahi fitur tambahan seperti operasi Boolean atau pemetaan tekstur untuk memperkaya model Anda lebih lanjut.

---

**Terakhir Diperbarui:** 2025-12-18  
**Diuji Dengan:** Aspose.3D 24.11 for Java  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## KATA KUNCI TARGET:

**Kata Kunci Utama (PRIORITAS TERTINGGI):**  
how to extrude shape

**Kata Kunci Sekunder (DUKUNGAN):**  
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj