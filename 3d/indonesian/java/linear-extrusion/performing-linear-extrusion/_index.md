---
title: Melakukan Ekstrusi Linier di Aspose.3D untuk Java
linktitle: Melakukan Ekstrusi Linier di Aspose.3D untuk Java
second_title: Asumsikan.3D Java API
description: Jelajahi dunia pemodelan 3D dengan Aspose.3D untuk Java. Belajar melakukan ekstrusi linier dengan mudah.
weight: 10
url: /id/java/linear-extrusion/performing-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Melakukan Ekstrusi Linier di Aspose.3D untuk Java

## Perkenalan

Selamat datang di tutorial komprehensif tentang melakukan ekstrusi linier di Aspose.3D untuk Java! Jika Anda ingin meningkatkan keterampilan pemodelan 3D menggunakan Java, Anda berada di tempat yang tepat. Dalam tutorial ini, kami akan memandu Anda melalui proses melakukan ekstrusi linier menggunakan Aspose.3D, pustaka Java yang kuat untuk pemodelan 3D.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

1. Lingkungan Pengembangan Java: Pastikan Anda telah menyiapkan lingkungan pengembangan Java di mesin Anda.

2.  Perpustakaan Aspose.3D: Unduh dan instal perpustakaan Aspose.3D. Anda dapat menemukan perpustakaan[Di Sini](https://releases.aspose.com/3d/java/).

## Paket Impor

Setelah Anda menyiapkan lingkungan pengembangan dan menginstal pustaka Aspose.3D, saatnya mengimpor paket yang diperlukan. Dalam kode Java Anda, sertakan yang berikut ini:

```java
import com.aspose.threed.*;
```

Mari kita uraikan setiap langkah untuk memastikan pemahaman yang jelas.

## Langkah 1: Atur Direktori Dokumen

Tentukan jalur ke direktori dokumen Anda:

```java
String MyDir = "Your Document Directory";
```

Ini memastikan bahwa model 3D yang dihasilkan akan disimpan di direktori yang ditentukan.

## Langkah 2: Inisialisasi Bentuk Dasar

Buat bentuk persegi panjang sebagai profil dasar untuk ekstrusi:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Sesuaikan radius pembulatan sesuai kebutuhan untuk menyesuaikan bentuk.

## Langkah 3: Lakukan Ekstrusi Linier

Lakukan ekstrusi linier pada profil dasar:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

Di sini, kita mengekstrusi bentuk sebanyak 10 unit, mengatur jumlah irisan, mengaktifkan pemusatan, dan menerapkan twist dan twist offset.

## Langkah 4: Buat Adegan 3D

Buat adegan 3D dan tambahkan ekstrusi sebagai node anak:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Langkah 5: Simpan Adegan 3D

Simpan adegan 3D yang dihasilkan sebagai file Wavefront OBJ:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Sekarang, Anda telah berhasil melakukan ekstrusi linier menggunakan Aspose.3D untuk Java!

## Kesimpulan

Selamat! Anda telah mempelajari cara memanfaatkan Aspose.3D untuk Java untuk melakukan ekstrusi linier. Perpustakaan yang kuat ini membuka banyak kemungkinan untuk proyek pemodelan 3D Anda.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan semua versi Java?

A1: Aspose.3D dirancang untuk bekerja dengan Java 1.6 dan versi yang lebih baru.

### Q2: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?

A2: Ya, Aspose.3D dapat digunakan untuk proyek pribadi dan komersial. Periksa detail lisensi[Di Sini](https://purchase.aspose.com/buy).

### Q3: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D?

 A3: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas atau mempertimbangkan untuk membeli a[izin sementara](https://purchase.aspose.com/temporary-license/) untuk dukungan premium.

### Q4: Apakah ada fitur pemodelan 3D lainnya di Aspose.3D?

 A4: Tentu saja! Jelajahi dokumentasi ekstensif[Di Sini](https://reference.aspose.com/3d/java/) untuk daftar lengkap fitur dan contoh.

### Q5: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D?

 A5: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
