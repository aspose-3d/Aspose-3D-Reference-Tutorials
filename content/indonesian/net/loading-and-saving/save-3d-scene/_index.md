---
title: Memuat dan Menyimpan - Menyimpan Adegan 3D
linktitle: Memuat dan Menyimpan - Menyimpan Adegan 3D
second_title: Aspose.3D .NET API
description: Jelajahi kekuatan Aspose.3D untuk .NET. perpustakaan serbaguna untuk manipulasi pemandangan 3D yang mulus. Muat, simpan, dan kompres dengan mudah.
type: docs
weight: 20
url: /id/net/loading-and-saving/save-3d-scene/
---
## Perkenalan

Selamat datang di perjalanan mengasyikkan ke dunia manipulasi adegan 3D menggunakan Aspose.3D untuk .NET! Baik Anda seorang pengembang berpengalaman atau penggemar yang penasaran, tutorial ini akan memandu Anda melalui proses memuat, menyimpan, dan mengompresi adegan 3D dengan mudah.

## Prasyarat

Sebelum terjun ke dunia manipulasi pemandangan 3D yang menawan, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Unduh dan instal perpustakaan Aspose.3D dari[tautan unduhan](https://releases.aspose.com/3d/net/).
-  Dokumentasi: Biasakan diri Anda dengan fungsi perpustakaan secara komprehensif[dokumentasi](https://reference.aspose.com/3d/net/).
- Direktori Output Anda: Siapkan direktori untuk menyimpan file output yang dihasilkan selama tutorial.

## Impor Namespace

Mari kita mulai eksplorasi dengan mengimpor namespace yang diperlukan ke lingkungan .NET kita:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Memuat dan Menyimpan - Menyimpan Adegan 3D

### Langkah 1: Muat Dokumen 3D

```csharp
Scene scene = new Scene();
scene.Open(RunExamples.GetDataFilePath("document.fbx"));
```

 Pada langkah ini, kami membuat yang baru`Scene` objek dan memuat dokumen 3D yang ada menggunakan`Open` metode.

### Langkah 2: Simpan Adegan ke Aliran

```csharp
MemoryStream dstStream = new MemoryStream();
scene.Save(dstStream, FileFormat.FBX7500ASCII);
```

 Simpan adegan 3D yang dimuat ke aliran memori menggunakan`Save` metode, menentukan format file yang diinginkan (dalam hal ini, FBX7500ASCII).

### Langkah 3: Putar Ulang Posisi Aliran

```csharp
dstStream.Position = 0;
```

Atur ulang posisi aliran untuk mempersiapkannya bagi pembaca berikutnya, memastikan pemrosesan yang lancar.

### Langkah 4: Simpan Adegan ke Jalur Lokal

```csharp
scene.Save("Your Output Directory" + "output_out.fbx", FileFormat.FBX7500ASCII);
```

Simpan adegan 3D ke jalur lokal, berikan direktori keluaran dan nama file yang bermakna.

## Kompresi

Sekarang, mari jelajahi opsi kompresi untuk adegan 3D.

### Langkah 1: Muat Dokumen 3D

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("document.fbx"));
```

 Mirip dengan contoh sebelumnya, memuat dokumen 3D ke dalam`Scene` obyek.

### Langkah 2: Nonaktifkan Kompresi dan Simpan

```csharp
scene.Save("Your Output Directory" + "UncompressedDocument.fbx", new FbxSaveOptions(FileFormat.FBX7500ASCII) { EnableCompression = false });
```

Nonaktifkan kompresi saat menyimpan adegan 3D, berikan jalur keluaran dan nama file yang jelas.

## Kesimpulan

Dalam tutorial ini, kami telah mempelajari aspek dasar memuat, menyimpan, dan mengompresi adegan 3D menggunakan Aspose.3D untuk .NET. Berbekal pengetahuan ini, Anda siap memulai perjalanan 3D Anda sendiri dan mengeluarkan kemungkinan kreatif dalam ranah Aspose.3D.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan berbagai format file 3D?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, memberikan fleksibilitas dalam proyek Anda.

### Q2: Dapatkah saya mengintegrasikan Aspose.3D dengan perpustakaan .NET lainnya?

A2: Tentu saja! Aspose.3D terintegrasi secara mulus dengan perpustakaan .NET lainnya, meningkatkan kemampuan aplikasi Anda.

### Q3: Bagaimana saya bisa mendapatkan lisensi sementara untuk Aspose.3D?

 A3: Kunjungi[izin sementara](https://purchase.aspose.com/temporary-license/) halaman di situs web Aspose untuk mendapatkan lisensi sementara.

### Q4: Di mana saya bisa mencari bantuan atau terhubung dengan komunitas?

 A4: Bergabunglah dengan komunitas Aspose.3D yang dinamis di[forum](https://forum.aspose.com/c/3d/18) untuk mencari dukungan, berbagi pengalaman, dan berkolaborasi dengan sesama peminat.

### Q5: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D?

 A5: Ya, jelajahi fitur Aspose.3D dengan mengambil[uji coba gratis](https://releases.aspose.com/) Hari ini!