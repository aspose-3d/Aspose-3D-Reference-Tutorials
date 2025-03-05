---
title: Menyiapkan UV pada Kubus
linktitle: Menyiapkan UV pada Kubus
second_title: Aspose.3D .NET API
description: Pelajari cara menyiapkan pemetaan UV pada kubus 3D menggunakan Aspose.3D untuk .NET. Ciptakan pemandangan yang menakjubkan secara visual dengan pemetaan tekstur yang presisi.
type: docs
weight: 18
url: /id/net/geometry-and-hierarchy/setup-uv-cube/
---
## Perkenalan

Membuat pemandangan 3D yang menawan dan menarik secara visual sering kali melibatkan proses yang cermat dalam menyiapkan pemetaan UV pada bentuk geometris. Dalam tutorial ini, kita akan mempelajari cara mengatur UV pada kubus menggunakan Aspose.3D untuk .NET. Aspose.3D adalah perpustakaan .NET yang kuat yang menyediakan serangkaian fitur lengkap untuk pemodelan dan manipulasi 3D.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

1. Aspose.3D untuk Perpustakaan .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/net/).

2. Lingkungan Pengembangan: Siapkan lingkungan pengembangan .NET dengan alat yang diperlukan.

Sekarang, mari kita lanjutkan ke tutorialnya.

## Impor Namespace

Pertama, impor namespace yang diperlukan untuk mengakses fungsionalitas Aspose.3D di aplikasi .NET Anda.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Tentukan UV untuk Kubus

Tentukan koordinat UV untuk setiap titik sudut kubus. Ini melibatkan penentuan nilai U dan V untuk setiap sudut kubus.

```csharp
// ExStart:DefineUVs
Vector4[] uvs = new Vector4[]
{
    new Vector4(0.0, 1.0, 0.0, 1.0),
    new Vector4(1.0, 0.0, 0.0, 1.0),
    new Vector4(0.0, 0.0, 0.0, 1.0),
    new Vector4(1.0, 1.0, 0.0, 1.0)
};
// ExEnd:DefineUV
```

## Langkah 2: Tentukan Indeks UV

Tentukan indeks koordinat UV untuk setiap poligon kubus. Ini mendefinisikan bagaimana UV dipetakan ke permukaan kubus.

```csharp
// ExStart:DefineUVIndices
int[] uvsId = new int[]
{
    0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 9, 8, 1, 10, 11, 3, 12, 0, 2, 13
};
// ExEnd: Tentukan Indeks UV
```

## Langkah 3: Buat Jaring

Manfaatkan pustaka Aspose.3D untuk membuat mesh menggunakan metode pembuat poligon. Ini akan menjadi fondasi kubus 3D kita.

```csharp
// ExStart:CreateMesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
// ExEnd:BuatMesh
```

## Langkah 4: Buat Elemen UV

Buat elemen UV di mesh untuk menyimpan data pemetaan UV.

```csharp
// ExStart:BuatUVEelemen
VertexElementUV elementUV = mesh.CreateElementUV(TextureMapping.Diffuse, MappingMode.PolygonVertex, ReferenceMode.IndexToDirect);
// ExEnd:BuatUVEelemen
```

## Langkah 5: Salin Data UV ke Mesh

Salin koordinat dan indeks UV yang telah ditentukan sebelumnya ke elemen simpul UV pada mesh.

```csharp
// ExStart:SalinUVData
elementUV.Data.AddRange(uvs);
elementUV.Indices.AddRange(uvsId);
// ExEnd:SalinUVData
```

## Kesimpulan

Selamat! Anda telah berhasil menyiapkan pemetaan UV pada kubus menggunakan Aspose.3D untuk .NET. Hal ini membuka kemungkinan untuk menciptakan pemandangan 3D yang rumit dan menakjubkan secara visual dengan pemetaan tekstur yang presisi.

## FAQ

### Q1: Apa itu Aspose.3D untuk .NET?

A1: Aspose.3D untuk .NET adalah perpustakaan yang kuat untuk pemodelan dan manipulasi 3D dalam aplikasi .NET.

### Q2: Di mana saya dapat menemukan dokumentasi Aspose.3D?

 A2: Dokumentasi tersedia[Di Sini](https://reference.aspose.com/3d/net/).

### Q3: Apakah tersedia uji coba gratis?

 A3: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D?

 A4: Kunjungi forum dukungan[Di Sini](https://forum.aspose.com/c/3d/18).

### Q5: Apakah lisensi sementara tersedia?

 A5: Ya, Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).