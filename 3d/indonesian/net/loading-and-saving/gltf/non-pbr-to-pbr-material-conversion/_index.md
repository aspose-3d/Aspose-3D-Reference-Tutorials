---
title: Konversi Material Non PBR ke PBR
linktitle: Konversi Material Non PBR ke PBR
second_title: Aspose.3D .NET API
description: Jelajahi Aspose.3D untuk .NET - Konversi materi Non-PBR ke PBR dengan mudah. Tutorial komprehensif dan API yang kuat.
type: docs
weight: 16
url: /id/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## Perkenalan

Selamat datang di panduan langkah demi langkah tentang penggunaan Aspose.3D untuk .NET untuk mengonversi materi Non-PBR (Rendering Berbasis Fisik) menjadi materi PBR. Aspose.3D adalah API canggih yang memungkinkan pengembang bekerja secara lancar dengan format file 3D di aplikasi .NET mereka.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D untuk .NET. Anda dapat menemukan tautan unduhan[Di Sini](https://releases.aspose.com/3d/net/).

- Pemahaman Dasar C#: Tutorial ini mengasumsikan Anda memiliki pemahaman mendasar tentang pemrograman C#.

- IDE (Lingkungan Pengembangan Terpadu): Pilih IDE pilihan Anda untuk pengembangan .NET, seperti Visual Studio.

## Impor Namespace

Dalam kode C# Anda, mulailah dengan mengimpor namespace yang diperlukan:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Langkah 1: Inisialisasi Adegan 3D Baru

Mulailah dengan membuat adegan 3D baru menggunakan kode berikut:

```csharp
// ExStart:Non_PBRtoPBRMahan
// menginisialisasi adegan 3D baru
var scene = new Scene();
```

## Langkah 2: Buat Objek 3D

Selanjutnya buatlah objek 3D, misalnya kotak:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Langkah 3: Konfigurasikan Konversi Material

Menyiapkan opsi konversi material untuk konversi Non-PBR ke PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Langkah 4: Simpan dalam Format GLTF 2.0

Simpan adegan yang dikonversi dalam format GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd: Bahan Non_PBR ke PBR
```

Ulangi langkah-langkah ini sesuai kebutuhan untuk kasus penggunaan spesifik Anda, pastikan setiap detail dikonfigurasi dengan benar.

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara mengonversi materi Non-PBR ke PBR menggunakan Aspose.3D untuk .NET. Alat canggih ini membuka kemungkinan tak terbatas untuk manipulasi grafis 3D di aplikasi .NET Anda.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan semua format file 3D?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, memberikan fleksibilitas dalam proyek Anda.

### Q2: Bisakah saya menggunakan Aspose.3D untuk aplikasi komersial?

 A2: Tentu saja! Aspose.3D adalah produk komersial, dan Anda dapat membelinya[Di Sini](https://purchase.aspose.com/buy).

### Q3: Apakah saya memerlukan lisensi sementara untuk pengujian?

 A3: Ya, Anda bisa mendapatkan lisensi sementara untuk tujuan pengujian[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q4: Di mana saya dapat menemukan dukungan untuk Aspose.3D?

 A4: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.

### Q5: Apakah tersedia uji coba gratis?

 A5: Ya, Anda dapat menjelajahi versi uji coba gratis[Di Sini](https://releases.aspose.com/).