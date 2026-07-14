---
date: 2026-05-24
description: Pelajari cara mengatur lisensi aspose 3d di Java, menerapkan file lisensi,
  mengalirkannya, atau menggunakan metered licensing dengan public and private keys.
keywords:
- set aspose 3d license
- aspose 3d java licensing
- metered licensing java
linktitle: Cara Mengatur Lisensi Aspose di Aspose.3D untuk Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  headline: How to Set Aspose 3D License in Java (set aspose 3d license)
  type: TechArticle
- description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  name: How to Set Aspose 3D License in Java (set aspose 3d license)
  steps:
  - name: Create a `License` object
    text: Instantiate the `License` class; this prepares the runtime to accept a license
      file.
  - name: Apply the license file
    text: Provide the absolute or relative path to your `.lic` file and call `setLicense`.
      The method returns `void`, and the license is cached after the first successful
      call, so subsequent calls are inexpensive.
  - name: Create a `License` object
    text: As before, start by creating an instance of the `License` class.
  - name: Load the license via `FileInputStream`
    text: Open a `FileInputStream` pointing to your `.lic` file (or any `InputStream`)
      and pass it to `setLicense`. The stream is read once and then closed automatically.
  - name: Initialize a `Metered` license object
    text: The `Metered` class represents a cloud‑based license that validates usage
      against Aspose’s metering server.
  - name: Set public and private keys
    text: Call `setMeteredKey(publicKey, privateKey)` with the keys you received when
      you purchased a metered license. The library contacts the server once to verify
      the keys and then caches the result.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports Java 6 through Java 21, covering more than 15
      major releases.
    question: Is Aspose.3D compatible with all Java versions?
  - answer: You can refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find additional documentation?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Can I try Aspose.3D before purchasing?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for support.
    question: How can I get support for Aspose.3D?
  - answer: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).
    question: Do I need a temporary license for testing?
  type: FAQPage
second_title: Aspose.3D Java API
title: Cara Mengatur Lisensi Aspose 3D di Java (atur lisensi aspose 3d)
url: /id/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Mengatur Lisensi Aspose 3D di Java (set aspose 3d license)

## Pendahuluan

Dalam tutorial komprehensif ini Anda akan menemukan **cara mengatur lisensi aspose 3d** untuk Aspose.3D dalam lingkungan Java. Apakah Anda lebih suka memuat file lisensi, streaming, atau menggunakan lisensi metered dengan kunci publik dan pribadi, kami akan membahas setiap pendekatan langkah demi langkah sehingga Anda dapat membuka semua fitur Aspose.3D dengan cepat dan percaya diri. Mengatur lisensi dengan benar menghapus watermark evaluasi, mengaktifkan format 3D premium, dan memastikan kepatuhan penuh dengan model lisensi Aspose.

## Jawaban Cepat
- **Apa cara utama untuk mengatur lisensi Aspose.3D?** Gunakan kelas `License` dan panggil `setLicense` dengan jalur file atau stream.  
- **Apakah saya dapat memuat lisensi dari stream?** Ya – bungkus file `.lic` dalam `FileInputStream` dan berikan ke `setLicense`.  
- **Bagaimana jika saya membutuhkan lisensi metered?** Inisialisasi objek `Metered` dan panggil `setMeteredKey` dengan kunci publik dan pribadi Anda.  
- **Apakah saya memerlukan lisensi untuk build pengembangan?** Lisensi percobaan atau sementara diperlukan untuk skenario non‑evaluasi apa pun.  
- **Versi Java mana yang didukung?** Aspose.3D bekerja dengan Java 6 hingga Java 21, mencakup lebih dari 15 rilis utama.

## Apa itu kelas `License`?
Kelas `License` adalah objek lisensi inti Aspose.3D yang memuat file `.lic` ke memori, memvalidasi informasi lisensi, dan setelah diinstansiasi menerapkan lisensi secara global untuk proses JVM, memastikan semua operasi Aspose.3D berikutnya berjalan dalam mode berlisensi tanpa batasan evaluasi.

## Mengapa mengatur lisensi Aspose 3D?
Menerapkan lisensi yang valid mengaktifkan **lebih dari 50 format file 3D premium** (termasuk FBX, OBJ, STL, dan GLTF) dan menghapus watermark “Evaluation” dari gambar yang dirender. Ini juga menghapus batas ukuran scene, memungkinkan pemrosesan model dengan **hingga 1 juta vertex** tanpa penurunan kinerja.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki prasyarat berikut:

- Pemahaman dasar tentang pemrograman Java.  
- Perpustakaan Aspose.3D terpasang. Anda dapat mengunduhnya dari [halaman rilis](https://releases.aspose.com/3d/java/).

## Impor Paket

Untuk memulai, impor paket yang diperlukan ke dalam proyek Java Anda. Pastikan Aspose.3D ditambahkan ke classpath Anda. Berikut contoh:

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

Kelas `License` bertanggung jawab untuk memuat file `.lic` dan menerapkannya secara global, sementara kelas `Metered` memungkinkan lisensi metered berbasis cloud dengan memvalidasi kunci publik dan pribadi terhadap server lisensi Aspose.

## Cara menerapkan lisensi dari file?

Muat lisensi Anda langsung dari file `.lic` di disk. Metode ini adalah pendekatan paling sederhana untuk aplikasi desktop atau on‑premises, dan memastikan lisensi dibaca sekali saat startup dan disimpan dalam cache selama masa hidup JVM, menghilangkan beban runtime setelah pemuatan awal.

### Langkah 1: Buat objek `License`
Instansiasikan kelas `License`; ini menyiapkan runtime untuk menerima file lisensi.

### Langkah 2: Terapkan file lisensi
Berikan jalur absolut atau relatif ke file `.lic` Anda dan panggil `setLicense`. Metode ini mengembalikan `void`, dan lisensi disimpan dalam cache setelah panggilan pertama yang berhasil, sehingga panggilan selanjutnya tidak mahal.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Cara menerapkan lisensi dari stream?

Streaming lisensi berguna ketika file di-embed sebagai sumber daya, disimpan di lokasi aman, atau diambil dari layanan remote saat runtime. Dengan menggunakan `InputStream`, Anda menghindari paparan jalur file fisik dan dapat menjaga data lisensi tetap terenkripsi atau dikemas di dalam JAR Anda, meningkatkan keamanan sambil tetap memungkinkan perpustakaan membaca byte lisensi.

### Langkah 1: Buat objek `License`
Seperti sebelumnya, mulailah dengan membuat instance kelas `License`.

### Langkah 2: Muat lisensi melalui `FileInputStream`
Buka `FileInputStream` yang mengarah ke file `.lic` Anda (atau `InputStream` apa pun) dan berikan ke `setLicense`. Stream dibaca sekali dan kemudian ditutup secara otomatis.

```java
License license = new License();
```

## Cara menggunakan kunci publik dan pribadi untuk lisensi metered?

Lisensi metered memungkinkan Anda mengaktifkan Aspose.3D tanpa file `.lic` fisik, menggunakan kunci yang dikeluarkan oleh layanan cloud Aspose. Pendekatan ini ideal untuk penyebaran SaaS atau berbasis cloud di mana mengelola file lisensi pada setiap instance tidak praktis; perpustakaan menghubungi server metering Aspose sekali untuk memvalidasi kunci dan kemudian menyimpan hasilnya dalam cache untuk sesi.

### Langkah 1: Inisialisasi objek lisensi `Metered`
Kelas `Metered` mewakili lisensi berbasis cloud yang memvalidasi penggunaan terhadap server metering Aspose.

### Langkah 2: Atur kunci publik dan pribadi
Panggil `setMeteredKey(publicKey, privateKey)` dengan kunci yang Anda terima saat membeli lisensi metered. Perpustakaan menghubungi server sekali untuk memverifikasi kunci dan kemudian menyimpan hasilnya dalam cache.

```java
license.setLicense("Aspose._3D.lic");
```

## Masalah Umum & Tips

- **File tidak ditemukan** – Pastikan jalur file `.lic` benar relatif terhadap direktori kerja atau gunakan jalur absolut.  
- **Stream ditutup terlalu cepat** – Saat menggunakan stream, pertahankan objek `License` tetap hidup selama aplikasi berjalan; lisensi disimpan dalam cache setelah panggilan pertama yang berhasil.  
- **Kunci metered tidak cocok** – Periksa kembali bahwa kunci publik dan pribadi sesuai dengan lisensi metered yang sama; kesalahan ketik akan menyebabkan pengecualian runtime.  
- **Tips pro:** Simpan file lisensi di lokasi aman di luar pohon sumber dan muat melalui variabel lingkungan untuk menghindari komit ke kontrol versi.

## Kesimpulan

Selamat! Anda telah berhasil mempelajari **cara mengatur lisensi aspose 3d** di Java menggunakan tiga metode andal: menerapkan lisensi dari file, streaming, dan mengonfigurasi lisensi metered dengan kunci publik dan pribadi. Dengan lisensi yang sudah terpasang, Anda kini dapat mengintegrasikan Aspose.3D secara mulus ke dalam aplikasi Java Anda, membuka semua fitur pemrosesan 3D premium, dan mematuhi persyaratan lisensi Aspose.

## Pertanyaan yang Sering Diajukan

**Q: Apakah Aspose.3D kompatibel dengan semua versi Java?**  
A: Ya, Aspose.3D mendukung Java 6 hingga Java 21, mencakup lebih dari 15 rilis utama.

**Q: Di mana saya dapat menemukan dokumentasi tambahan?**  
A: Anda dapat merujuk ke dokumentasi [di sini](https://reference.aspose.com/3d/java/).

**Q: Bisakah saya mencoba Aspose.3D sebelum membeli?**  
A: Ya, Anda dapat menjelajahi percobaan gratis [di sini](https://releases.aspose.com/).

**Q: Bagaimana saya dapat mendapatkan dukungan untuk Aspose.3D?**  
A: Kunjungi [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan.

**Q: Apakah saya memerlukan lisensi sementara untuk pengujian?**  
A: Ya, dapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

**Q: Apa perbedaan antara lisensi file dan lisensi metered?**  
A: Lisensi file adalah file `.lic` statis yang terkait dengan versi produk tertentu, sedangkan lisensi metered memvalidasi penggunaan terhadap layanan metering berbasis cloud Aspose menggunakan kunci publik/pribadi.

**Q: Bisakah saya menyematkan kode pemuatan lisensi dalam inisialisator statis?**  
A: Tentu – menempatkan inisialisasi `License` dalam blok statis memastikan lisensi diterapkan sekali saat kelas pertama kali dimuat.

```java
License license = new License();
```
```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```
```java
Metered metered = new Metered();
```
```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

{{< blocks/products/products-backtop-button >}}

## Tutorial Terkait

- [Panduan Lisensi Langkah demi Langkah untuk Aspose.3D Java](/3d/java/licensing/)
- [Buat Scene 3D Java dengan Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [Buat Kubus 3D, Terapkan Material PBR di Java dengan Aspose.3D](/3d/java/geometry/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}