---
date: 2026-02-14
description: Pelajari cara mengatur lisensi Aspose di Aspose.3D untuk Java, termasuk
  cara menerapkan lisensi dari file dan mengatur kunci publik serta pribadi.
linktitle: How to Set Aspose License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cara Mengatur Lisensi Aspose di Aspose.3D untuk Java
url: /id/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Mengatur Lisensi Aspose di Aspose.3D untuk Java

## Pendahuluan

Dalam tutorial komprehensif ini Anda akan menemukan **cara mengatur lisensi Aspose** untuk Aspose.3D dalam lingkungan Java. Apakah Anda lebih suka memuat file lisensi, melakukan streaming, atau menggunakan lisensi metered dengan kunci publik dan pribadi, kami akan membimbing Anda melalui setiap pendekatan langkah demi langkah sehingga Anda dapat membuka seluruh set fitur Aspose.3D dengan cepat dan percaya diri.

## Jawaban Cepat
- **Apa cara utama untuk mengatur lisensi Aspose.3D?** Gunakan kelas `License` dan panggil `setLicense` dengan jalur file atau stream.  
- **Apakah saya dapat memuat lisensi dari stream?** Ya – bungkus file `.lic` dalam `FileInputStream` dan berikan ke `setLicense`.  
- **Bagaimana jika saya membutuhkan lisensi metered?** Inisialisasi objek `Metered` dan panggil `setMeteredKey` dengan kunci publik dan pribadi Anda.  
- **Apakah saya memerlukan lisensi untuk build pengembangan?** Lisensi percobaan atau sementara diperlukan untuk skenario selain evaluasi.  
- **Versi Java mana yang didukung?** Aspose.3D bekerja dengan Java 6 dan yang lebih baru.

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

## Menerapkan Lisensi Menggunakan File

### Langkah 1: Buat Objek License

Pertama, buat objek `License` dalam kode Java Anda.

```java
License license = new License();
```

### Langkah 2: Terapkan Lisensi dari File

Tentukan jalur ke file lisensi Anda dan atur lisensi menggunakan kode berikut. Ini menunjukkan teknik **apply license from file**.

```java
license.setLicense("Aspose._3D.lic");
```

## Menerapkan Lisensi Menggunakan Objek Stream

### Langkah 1: Buat Objek License

Demikian pula, buat objek `License` dalam kode Java Anda.

```java
License license = new License();
```

### Langkah 2: Atur Lisensi dari Objek Stream

Manfaatkan `FileInputStream` untuk membuat stream dan atur lisensi:

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Menggunakan Kunci Publik dan Pribadi untuk Lisensi Metered

### Langkah 1: Inisialisasi Objek Lisensi Metered

Inisialisasi objek lisensi `Metered`:

```java
Metered metered = new Metered();
```

### Langkah 2: Atur Kunci Publik dan Pribadi

Atur kunci publik dan pribadi Anda untuk mengaktifkan lisensi metered. Ini mencakup skenario **set public private keys**.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

## Mengapa Mengatur Lisensi Penting

Menerapkan lisensi yang tepat menghilangkan watermark evaluasi, membuka format file premium, dan memastikan kepatuhan dengan model lisensi Aspose. Menggunakan metode yang sesuai (file, stream, atau metered) memungkinkan Anda mengintegrasikan lisensi secara mulus ke dalam pipeline CI/CD, penyebaran cloud, atau aplikasi desktop.

## Masalah Umum & Tips

- **File tidak ditemukan** – Verifikasi bahwa jalur file `.lic` benar relatif terhadap direktori kerja atau gunakan jalur absolut.  
- **Stream tertutup terlalu cepat** – Saat menggunakan stream, pertahankan objek `License` tetap hidup selama aplikasi berjalan; lisensi akan di-cache setelah panggilan pertama yang berhasil.  
- **Kunci metered tidak cocok** – Periksa kembali bahwa kunci publik dan pribadi sesuai dengan lisensi metered yang sama; kesalahan ketik akan menyebabkan pengecualian runtime.  
- **Tips pro:** Simpan file lisensi di lokasi yang aman di luar pohon sumber dan muat melalui variabel lingkungan untuk menghindari komit ke kontrol versi.

## Kesimpulan

Selamat! Anda telah berhasil mempelajari **cara mengatur lisensi Aspose** di Aspose.3D untuk Java menggunakan berbagai metode, termasuk menerapkan lisensi dari file, streaming, dan mengonfigurasi lisensi metered dengan kunci publik dan pribadi. Sekarang Anda dapat mengintegrasikan Aspose.3D secara mulus ke dalam aplikasi Java Anda dan memanfaatkan sepenuhnya kemampuan pemrosesan 3D-nya.

## Pertanyaan yang Sering Diajukan

**T: Apakah Aspose.3D kompatibel dengan semua versi Java?**  
J: Ya, Aspose.3D kompatibel dengan Java 6 dan versi yang lebih baru.

**T: Di mana saya dapat menemukan dokumentasi tambahan?**  
J: Anda dapat merujuk ke dokumentasi [di sini](https://reference.aspose.com/3d/java/).

**T: Bisakah saya mencoba Aspose.3D sebelum membeli?**  
J: Ya, Anda dapat menjelajahi percobaan gratis [di sini](https://releases.aspose.com/).

**T: Bagaimana saya dapat mendapatkan dukungan untuk Aspose.3D?**  
J: Kunjungi [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan.

**T: Apakah saya memerlukan lisensi sementara untuk pengujian?**  
J: Ya, dapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

**T: Apa perbedaan antara lisensi file dan lisensi metered?**  
J: Lisensi file adalah file `.lic` statis yang terikat pada versi produk tertentu, sementara lisensi metered memvalidasi penggunaan terhadap layanan metering berbasis cloud Aspose menggunakan kunci publik/pribadi.

**T: Bisakah saya menyematkan kode pemuatan lisensi dalam inisialisator statis?**  
J: Tentu – menempatkan inisialisasi `License` dalam blok statis memastikan lisensi diterapkan sekali ketika kelas pertama kali dimuat.

---

**Last Updated:** 2026-02-14  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}