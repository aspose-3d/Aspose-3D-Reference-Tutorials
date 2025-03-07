---
title: Menerapkan Bahan PBR ke Kotak
linktitle: Menerapkan Bahan PBR ke Kotak
second_title: Aspose.3D .NET API
description: Jelajahi dunia grafis 3D dengan Aspose.3D untuk .NET. Buat adegan yang imersif dengan mudah menggunakan materi Rendering Berbasis Fisik.
weight: 10
url: /id/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menerapkan Bahan PBR ke Kotak

## Perkenalan

Selamat datang di dunia grafis 3D yang menakjubkan! Dalam panduan langkah demi langkah ini, kita akan menjelajahi pustaka Aspose.3D untuk .NET yang canggih dan mempelajari cara membuat pemandangan 3D yang menakjubkan menggunakan materi Rendering Berbasis Fisik (PBR). Aspose.3D menyederhanakan proses kompleks grafik 3D dan membuka banyak kemungkinan bagi pengembang.

## Prasyarat

Sebelum kita terjun ke dunia grafis 3D yang menarik, pastikan Anda sudah menyiapkan semuanya:

### Unduh dan Instal Aspose.3D untuk .NET

 Mengunjungi[Aspose.3D untuk dokumentasi .NET](https://reference.aspose.com/3d/net/) untuk petunjuk rinci tentang mengunduh dan menginstal perpustakaan.

### Dapatkan Lisensi

Untuk membuka potensi penuh Aspose.3D, dapatkan lisensi yang valid. Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/) atau membeli lisensi penuh[Di Sini](https://purchase.aspose.com/buy).

## Impor Namespace

Pertama, pastikan untuk mengimpor namespace yang diperlukan untuk memanfaatkan kemampuan Aspose.3D untuk .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Langkah 1: Inisialisasi Adegan

Mulailah dengan menginisialisasi adegan 3D menggunakan cuplikan kode berikut:

```csharp
Scene scene = new Scene();
```

## Langkah 2: Inisialisasi Materi PBR

Buat objek material PBR untuk mencapai rendering realistis:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Langkah 3: Tetapkan Properti Material

Sempurnakan sifat material, menjadikannya hampir seperti logam dan sangat kasar:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Langkah 4: Buat Kotak

Hasilkan kotak di mana material PBR akan diterapkan:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Langkah 5: Terapkan Bahan ke Kotak

Tetapkan material PBR ke node kotak yang dibuat:

```csharp
boxNode.Material = mat;
```

## Langkah 6: Simpan Adegan 3D

Simpan adegan 3D ke dalam format STL dengan direktori keluaran yang diinginkan:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Selamat! Anda telah berhasil menerapkan materi PBR ke kotak dalam adegan 3D menggunakan Aspose.3D untuk .NET.

## Kesimpulan

Menjelajah ke dalam grafik 3D dengan Aspose.3D untuk .NET membuka pintu menuju kemungkinan kreatif tanpa batas. Dengan API intuitif dan fitur-fitur canggihnya, menciptakan pemandangan visual yang menakjubkan menjadi pengalaman yang menyenangkan bagi pengembang.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan format file 3D lainnya?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, memastikan fleksibilitas dalam proyek Anda.

### Q2: Bisakah saya menggunakan Aspose.3D untuk aplikasi komersial?

A2: Tentu saja! Aspose.3D memberikan lisensi komersial untuk integrasi tanpa batas ke dalam aplikasi Anda.

### Q3: Apakah ada versi uji coba yang tersedia?

 A3: Ya, Anda dapat menjelajahi kemampuan Aspose.3D dengan mengunduh uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Di mana saya bisa mendapatkan dukungan dan diskusi komunitas?

 A4: Bergabunglah dengan komunitas Aspose.3D di[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi.

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A5: Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/) untuk tujuan evaluasi.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
