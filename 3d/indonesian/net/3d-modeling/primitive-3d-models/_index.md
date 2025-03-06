---
title: Membuat Model 3D Primitif
linktitle: Membuat Model 3D Primitif
second_title: Aspose.3D .NET API
description: Jelajahi dunia pemodelan 3D dengan Aspose.3D untuk .NET. Buat model primitif yang menakjubkan dengan mudah.
weight: 10
url: /id/net/3d-modeling/primitive-3d-models/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Membuat Model 3D Primitif

## Perkenalan

Selamat datang di dunia pemodelan 3D yang menarik dengan Aspose.3D untuk .NET! Dalam tutorial komprehensif ini, kita akan mengeksplorasi proses pembuatan model 3D primitif menggunakan Aspose.3D secara langkah demi langkah. Baik Anda seorang pengembang berpengalaman atau pemula yang penasaran, panduan ini akan membantu Anda memanfaatkan kekuatan Aspose.3D untuk membuat elemen 3D yang menakjubkan secara visual untuk proyek Anda.

## Prasyarat

Sebelum kita menyelami dunia pemodelan 3D yang menarik, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Unduh dan instal perpustakaan Aspose.3D untuk .NET dari[tautan unduhan](https://releases.aspose.com/3d/net/).

- Lingkungan Pengembangan: Siapkan lingkungan pengembangan .NET, pastikan kompatibilitas dengan Aspose.3D.

Sekarang setelah Anda memiliki hal-hal penting, mari memulai perjalanan kita membuat model 3D primitif selangkah demi selangkah.

## Impor Namespace

Mulailah dengan mengimpor namespace yang diperlukan untuk mengakses fungsionalitas yang disediakan oleh Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

Dengan namespace ini, Anda siap untuk melepaskan kekuatan Aspose.3D dalam aplikasi .NET Anda.

## Langkah 1: Inisialisasi Objek Adegan

```csharp
//Inisialisasi objek Scene
Scene scene = new Scene();
```

Buat objek pemandangan baru, yang berfungsi sebagai kanvas untuk karya 3D Anda.

## Langkah 2: Buat Model Kotak

```csharp
// Buat model Kotak
scene.RootNode.CreateChildNode("box", new Box());
```

Tambahkan model kotak ke akar adegan Anda. Sesuaikan dimensi dan properti kotak sesuai dengan visi kreatif Anda.

## Langkah 3: Buat Model Silinder

```csharp
// Buat model Silinder
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Sempurnakan pemandangan Anda dengan memperkenalkan model silinder. Sesuaikan parameternya untuk mencapai bentuk dan ukuran yang diinginkan.

## Langkah 4: Simpan Gambar dalam Format FBX

```csharp
// Simpan gambar dalam format FBX
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Simpan karya 3D Anda dalam format FBX. Pilih direktori keluaran dan nama file yang sesuai untuk kreasi Anda.

## Langkah 5: Tampilkan Pesan Sukses

```csharp
// Tampilkan pesan sukses
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Rayakan pencapaian Anda! Adegan berhasil dibuat dari model 3D primitif, dan file disimpan.

## Kesimpulan

 Selamat! Anda telah berhasil membuat model 3D yang menakjubkan menggunakan Aspose.3D untuk .NET. Panduan ini mencakup dasar-dasarnya, tetapi kemungkinannya tidak terbatas. Jelajahi[dokumentasi](https://reference.aspose.com/3d/net/) untuk fitur dan teknik lebih lanjut.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

A1: Aspose.3D terutama mendukung .NET, namun ada versi lain yang tersedia untuk Java dan platform lainnya.

### Q2: Apakah tersedia uji coba gratis?

 A2: Ya, Anda dapat mengeksplorasi kemampuan Aspose.3D dengan a[uji coba gratis](https://releases.aspose.com/).

### Q3: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk .NET?

 A3: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.

### Q4: Bagaimana cara mendapatkan lisensi sementara?

 A4: Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q5: Apakah ada contoh tutorial yang tersedia?

 A5: Ya, jelajahi lebih banyak tutorial dan contoh di[dokumentasi](https://reference.aspose.com/3d/net/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
