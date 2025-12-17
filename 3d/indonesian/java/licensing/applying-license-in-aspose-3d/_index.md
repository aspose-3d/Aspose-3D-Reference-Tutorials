---
date: 2025-12-17
description: Pelajari cara mengatur lisensi di Aspose.3D untuk Java dan cara menggunakan
  kunci publik serta privat untuk lisensi berbasis meter.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cara Mengatur Lisensi di Aspose.3D untuk Java – Panduan Lengkap
url: /id/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Menetapkan Lisensi di Aspose.3D untuk Java

## Pendahuluan

Selamat datang! Dalam tutorial langkah‑demi‑langkah ini Anda akan menemukan **cara menetapkan lisensi** untuk Aspose.3D dalam aplikasi Java dan juga belajar **cara menggunakan kunci publik dan privat** untuk lisensi bermeter. Aspose.3D adalah perpustakaan Java yang kuat yang menyederhanakan pekerjaan dengan format file 3D, dan lisensi yang valid membuka seluruh set fitur. Pada akhir panduan ini Anda akan dapat mengintegrasikan lisensi secara mulus ke dalam proyek Java apa pun.

## Jawaban Cepat
- **Apa cara utama untuk menetapkan lisensi?** Gunakan kelas `License` dan panggil `setLicense` dengan jalur file atau stream.  
- **Apakah saya dapat memuat lisensi dari stream?** Ya – `FileInputStream` berfungsi dengan sempurna.  
- **Untuk apa kunci publik/privat?** Mereka memungkinkan lisensi bermeter melalui kelas `Metered`.  
- **Apakah saya memerlukan lisensi untuk pengembangan?** Lisensi sementara atau percobaan sudah cukup untuk pengujian; lisensi penuh diperlukan untuk produksi.  
- **Versi Java mana yang didukung?** Aspose.3D bekerja dengan Java 6 dan yang lebih baru.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- Pemahaman dasar tentang pemrograman Java.
- Perpustakaan Aspose.3D yang ditambahkan ke proyek Anda. Unduh dari [halaman rilis](https://releases.aspose.com/3d/java/).
- File `.lic` yang valid atau kunci metered publik dan privat Anda.

## Impor Paket

Tambahkan impor yang diperlukan ke file sumber Java Anda. Pastikan JAR Aspose.3D berada di classpath.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Cara Menetapkan Lisensi Menggunakan File

### Langkah 1: Buat Objek License

Instansiasi kelas `License` – objek ini akan menyimpan informasi lisensi.

```java
License license = new License();
```

### Langkah 2: Tetapkan Lisensi dari File

Berikan jalur relatif atau absolut ke file `.lic` Anda dan terapkan.

```java
license.setLicense("Aspose._3D.lic");
```

> **Tip pro:** Simpan file lisensi di luar direktori kontrol sumber Anda untuk menghindari paparan tidak sengaja.

## Cara Menetapkan Lisensi Menggunakan Stream

### Langkah 1: Buat Objek License

Seperti sebelumnya, mulai dengan instance `License` yang baru.

```java
License license = new License();
```

### Langkah 2: Tetapkan Lisensi dari Stream

Baca file lisensi ke dalam `FileInputStream` dan berikan stream tersebut ke `setLicense`. Blok try‑with‑resources menjamin stream ditutup secara otomatis.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Cara Menggunakan Kunci Publik Privat untuk Lisensi Metered

### Langkah 1: Inisialisasi Objek Lisensi Metered

Buat instance dari kelas `Metered`, yang menangani lisensi bermeter (bayar‑sesuai‑penggunaan).

```java
Metered metered = new Metered();
```

### Langkah 2: Tetapkan Kunci Publik dan Privat

Berikan kunci yang Anda terima dari Aspose. Kunci ini memungkinkan perpustakaan melaporkan penggunaan kembali ke server lisensi.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Peringatan:** Jangan pernah menuliskan secara keras (hard‑code) kunci privat Anda dalam JAR yang didistribusikan secara publik. Pertimbangkan memuatnya dari lokasi yang aman atau variabel lingkungan.

## Kasus Penggunaan Umum

- **Pipeline rendering 3D perusahaan** – buka kunci API berperforma tinggi setelah menetapkan lisensi.
- **Lingkungan pengujian otomatis** – gunakan lisensi sementara (lihat FAQ) untuk memvalidasi fungsionalitas tanpa membeli lisensi penuh.
- **Solusi SaaS bermeter** – integrasikan kunci publik/privat untuk menagih pelanggan berdasarkan penggunaan aktual.

## Kesimpulan

Selamat! Anda kini tahu **cara menetapkan lisensi** untuk Aspose.3D di Java menggunakan file, stream, dan **cara menggunakan kunci publik privat** untuk lisensi bermeter. Dengan langkah‑langkah ini Anda dapat dengan percaya diri mengintegrasikan Aspose.3D ke dalam aplikasi Java apa pun dan memanfaatkan sepenuhnya kemampuan pemrosesan 3D‑nya.

## Pertanyaan yang Sering Diajukan

**Q1: Apakah Aspose.3D kompatibel dengan semua versi Java?**  
A1: Ya, Aspose.3D bekerja dengan Java 6 dan versi yang lebih baru.

**Q2: Di mana saya dapat menemukan dokumentasi tambahan?**  
A2: Anda dapat merujuk ke dokumentasi [di sini](https://reference.aspose.com/3d/java/).

**Q3: Bisakah saya mencoba Aspose.3D sebelum membeli?**  
A3: Ya, Anda dapat menjelajahi percobaan gratis [di sini](https://releases.aspose.com/).

**Q4: Bagaimana saya dapat mendapatkan dukungan untuk Aspose.3D?**  
A4: Kunjungi [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas dan resmi.

**Q5: Apakah saya memerlukan lisensi sementara untuk pengujian?**  
A5: Ya, dapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Terakhir Diperbarui:** 2025-12-17  
**Diuji Dengan:** Aspose.3D 24.11 for Java  
**Penulis:** Aspose  

---