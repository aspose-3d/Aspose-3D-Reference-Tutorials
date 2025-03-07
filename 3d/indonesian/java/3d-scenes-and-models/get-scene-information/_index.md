---
title: Ambil Informasi dari Adegan 3D di Aplikasi Java
linktitle: Ambil Informasi dari Adegan 3D di Aplikasi Java
second_title: Asumsikan.3D Java API
description: Jelajahi dunia manipulasi adegan 3D di Java dengan Aspose.3D. Tutorial ini memandu Anda dalam mengambil informasi langkah demi langkah.
weight: 12
url: /id/java/3d-scenes-and-models/get-scene-information/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ambil Informasi dari Adegan 3D di Aplikasi Java

## Perkenalan

Selamat datang di panduan komprehensif tentang mengambil informasi dari adegan 3D di aplikasi Java menggunakan Aspose.3D. Jika Anda seorang pengembang Java yang ingin meningkatkan kemampuan aplikasi Anda dengan manipulasi pemandangan 3D, Anda berada di tempat yang tepat. Tutorial ini akan memandu Anda melalui proses langkah demi langkah, memastikan Anda memahami setiap konsep secara menyeluruh.

## Prasyarat

Sebelum kita masuk ke tutorialnya, pastikan Anda memiliki yang berikut ini:

- Pemahaman dasar pemrograman Java.
-  Pustaka Aspose.3D diinstal. Jika tidak, unduh[Di Sini](https://releases.aspose.com/3d/java/).
- Java IDE (Lingkungan Pengembangan Terpadu) diinstal dan dikonfigurasi.

## Paket Impor

Di proyek Java Anda, impor paket yang diperlukan untuk memanfaatkan fungsionalitas Aspose.3D. Tambahkan baris berikut ke kode Anda:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

## Langkah 1: Inisialisasi Adegan 3D

```java
// ExStart:TambahkanAssetInformationToScene
Scene scene = new Scene();
```

 Mulailah dengan membuat adegan 3D baru menggunakan Aspose.3D`Scene` kelas.

## Langkah 2: Tetapkan Informasi Aplikasi dan Vendor

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

Tentukan aplikasi dan nama vendor yang terkait dengan adegan 3D Anda.

## Langkah 3: Tentukan Satuan Pengukuran

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

Tentukan unit pengukuran untuk adegan 3D Anda. Dalam contoh ini, kami menggunakan satuan Mesir kuno.

## Langkah 4: Simpan Adegan ke File

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:TambahkanAssetInformationToScene
```

Tentukan direktori dan nama file untuk menyimpan adegan 3D. Contoh menyimpan adegan dalam format FBX dengan pengkodean ASCII.

## Langkah 5: Cetak Pesan Sukses

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

Menampilkan pesan sukses yang menunjukkan bahwa informasi aset telah berhasil ditambahkan ke adegan.

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara mengambil informasi dari adegan 3D di aplikasi Java menggunakan Aspose.3D. Pustaka yang kuat ini membuka kemungkinan tak terbatas untuk menyempurnakan proyek Java Anda dengan konten 3D yang mendalam.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan semua IDE Java?

A1: Ya, Aspose.3D dirancang untuk bekerja secara lancar dengan semua IDE Java utama.

### Q2: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?

A2: Tentu saja. Aspose.3D menawarkan lisensi komersial untuk pengembang, memastikan Anda mematuhi persyaratan lisensi.

### Q3: Di mana saya dapat menemukan dukungan tambahan untuk Aspose.3D?

 A3: Untuk pertanyaan atau bantuan apa pun, kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D?

 A4: Ya, Anda dapat menjelajahi fitur-fiturnya dengan uji coba gratis yang tersedia[Di Sini](https://releases.aspose.com/).

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A5: Dapatkan lisensi sementara untuk tujuan pengujian[Di Sini](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
