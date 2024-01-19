---
title: Memuat dan Menyimpan - Membuat Dokumen 3D Kosong
linktitle: Memuat dan Menyimpan - Membuat Dokumen 3D Kosong
second_title: Aspose.3D .NET API
description: Jelajahi dunia pembuatan dokumen 3D dengan Aspose.3D untuk .NET. Buat, edit, dan simpan pemandangan 3D yang menakjubkan dengan mudah.
type: docs
weight: 11
url: /id/net/loading-and-saving/create-empty-3d-document/
---
## Perkenalan

Selamat datang di dunia pembuatan dokumen 3D menggunakan Aspose.3D untuk .NET! Dalam tutorial ini, kita akan mempelajari dasar-dasar memuat dan menyimpan dokumen 3D. Aspose.3D untuk .NET menyediakan seperangkat alat canggih untuk bekerja dengan adegan 3D, dan kami akan memandu Anda melalui setiap langkah untuk membantu Anda memulai dengan lancar.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan. Anda dapat mengunduhnya dari[Di Sini](https://releases.aspose.com/3d/net/).

## Impor Namespace

Untuk memulai, impor namespace yang diperlukan dalam proyek .NET Anda:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Memuat dan Menyimpan - Membuat Dokumen 3D Kosong

### Langkah 1: Siapkan Direktori Output Anda

```csharp
// Jalur ke direktori dokumen.
var output = "Your Output Directory" + "document.fbx";
```

### Langkah 2: Buat Dokumen 3D Kosong

```csharp
// ExStart:BuatDokumen 3DKosong

// Buat objek kelas Scene
Scene scene = new Scene();

// Simpan dokumen adegan 3D dalam format FBX
scene.Save(output, FileFormat.FBX7500ASCII);

// ExEnd:BuatDokumen 3DKosong
```

### Langkah 3: Tampilkan Hasilnya

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

Selamat! Anda baru saja membuat dokumen 3D kosong pertama Anda menggunakan Aspose.3D untuk .NET. Jangan ragu untuk menjelajahi lebih banyak fitur dan fungsi untuk mengeluarkan potensi penuh perpustakaan ini.

## Kesimpulan

 Dalam tutorial ini, kita membahas dasar-dasar membuat dokumen 3D kosong menggunakan Aspose.3D untuk .NET. Saat Anda melanjutkan perjalanan Anda dengan pengembangan 3D, lihat[dokumentasi](https://reference.aspose.com/3d/net/) untuk wawasan mendalam dan fitur-fitur canggih.

## FAQ

### Q1: Apakah Aspose.3D untuk .NET cocok untuk pemula?

A1: Ya, Aspose.3D untuk .NET menyediakan antarmuka yang ramah pengguna, sehingga dapat diakses oleh pemula dan pengembang berpengalaman.

### Q2: Bisakah saya mencoba Aspose.3D untuk .NET sebelum membeli?

 A2: Tentu saja! Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q3: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D untuk .NET?

 A3: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk mencari bantuan dan berhubungan dengan masyarakat.

### Q4: Apakah lisensi sementara tersedia untuk Aspose.3D untuk .NET?

 A4: Ya, Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya bisa membeli Aspose.3D untuk .NET?

 A5: Anda dapat membeli perpustakaan[Di Sini](https://purchase.aspose.com/buy).