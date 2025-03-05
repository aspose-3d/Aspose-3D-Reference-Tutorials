---
title: Menyiapkan Normal pada Cube
linktitle: Menyiapkan Normal pada Cube
second_title: Aspose.3D .NET API
description: Pelajari cara mengatur normal pada kubus 3D menggunakan Aspose.3D untuk .NET. Tingkatkan keterampilan pemodelan 3D Anda dengan panduan langkah demi langkah ini.
type: docs
weight: 17
url: /id/net/geometry-and-hierarchy/setup-normals-cube/
---
## Perkenalan

Selamat datang di panduan langkah demi langkah kami tentang menyiapkan normal pada kubus dalam adegan 3D menggunakan Aspose.3D untuk .NET. Aspose.3D adalah perpustakaan canggih yang memungkinkan pengembang .NET bekerja dengan file 3D, menyediakan berbagai fungsi untuk pemodelan dan manipulasi 3D.

Dalam tutorial ini, kami akan memandu Anda melalui proses pengaturan normal pada kubus dalam adegan 3D menggunakan Aspose.3D. Normal sangat penting untuk pencahayaan dan bayangan yang tepat dalam grafik 3D, dan memahami cara mengaturnya adalah hal mendasar untuk menciptakan model 3D yang realistis dan menarik secara visual.

## Prasyarat

Sebelum kita masuk ke tutorialnya, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D. Anda dapat mengunduhnya dari[Aspose.3D untuk dokumentasi .NET](https://reference.aspose.com/3d/net/).

## Impor Namespace

Untuk memulai, mari impor namespace yang diperlukan ke dalam proyek Anda:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Data Normal Mentah

Langkah pertama melibatkan pendefinisian data normal mentah untuk kubus kita. Normal direpresentasikan sebagai objek Vector4, dan berikut ini contohnya:

```csharp
// ExStart: Data Normal Mentah
Vector4[] normals = new Vector4[]
{
    new Vector4(-0.577350258,-0.577350258, 0.577350258, 1.0),
    //... (ulangi untuk 7 simpul lainnya)
};
// ExEnd: Data Normal Mentah
```

## Langkah 2: Buat Mesh Menggunakan Polygon Builder

Selanjutnya, kita akan membuat mesh menggunakan metode pembuat poligon. Hal ini dilakukan dengan memanggil kelas umum untuk membuat instance mesh:

```csharp
// ExStart:CreateMesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
// ExEnd:BuatMesh
```

## Langkah 3: Atur Normals di Cube

Sekarang, mari kita atur normal pada kubus dengan membuat VertexElementNormal dan menyalin data normal ke elemen vertex:

```csharp
// ExStart:SetupNormalsOnCube
VertexElementNormal elementNormal = mesh.CreateElement(VertexElementType.Normal, MappingMode.ControlPoint, ReferenceMode.Direct) as VertexElementNormal;
elementNormal.Data.AddRange(normals);
// ExEnd:SetupNormalsOnCube
```

## Langkah 4: Cetak Pesan Sukses

Terakhir, kami akan mencetak pesan sukses untuk mengonfirmasi bahwa pengaturan normal telah berhasil:

```csharp
Console.WriteLine("\nNormals have been set up successfully on the cube.");
```

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara menyiapkan normal pada kubus dalam adegan 3D menggunakan Aspose.3D untuk .NET. Pengetahuan ini penting untuk mencapai efek pencahayaan dan bayangan yang realistis dalam model 3D Anda.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan format file 3D lainnya?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, memungkinkan integrasi tanpa batas dengan proyek Anda yang sudah ada.

### Q2: Dapatkah saya mencoba Aspose.3D sebelum membeli?

A2: Tentu saja! Anda dapat mengunduh uji coba gratis dari[Di Sini](https://releases.aspose.com/).

### Q3: Di mana saya dapat menemukan lisensi sementara untuk Aspose.3D?

 A3: Lisensi sementara tersedia untuk dibeli[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q4: Apa tanggapan komunitas terhadap Aspose.3D?

 A4: Bergabunglah dengan komunitas Aspose.3D di[forum](https://forum.aspose.com/c/3d/18) untuk terhubung dengan pengembang lain dan berbagi pengalaman.

### Q5: Apakah ada sumber tambahan untuk mempelajari Aspose.3D?

 A5: Jelajahi yang luas[dokumentasi](https://reference.aspose.com/3d/net/) untuk menemukan lebih banyak fitur dan tip.