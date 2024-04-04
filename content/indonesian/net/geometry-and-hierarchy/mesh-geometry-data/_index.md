---
title: Bekerja dengan Data Geometri Mesh
linktitle: Bekerja dengan Data Geometri Mesh
second_title: Aspose.3D .NET API
description: Kuasai seni pemrograman grafis 3D dengan Aspose.3D untuk .NET. Buat, manipulasi, dan simpan pemandangan 3D yang menakjubkan dengan mudah.
type: docs
weight: 15
url: /id/net/geometry-and-hierarchy/mesh-geometry-data/
---
## Perkenalan

Selamat datang di dunia pemrograman grafis 3D yang menarik dengan Aspose.3D untuk .NET! Dalam tutorial ini, kita akan mempelajari seluk-beluk bekerja dengan Data Geometri Mesh dalam adegan 3D menggunakan Aspose.3D, perpustakaan yang kuat dan serbaguna untuk pengembang .NET. Baik Anda seorang programmer berpengalaman atau baru memulai dengan grafik 3D, panduan langkah demi langkah ini akan membantu Anda menguasai seni menangani data geometri mesh dengan mudah.

## Prasyarat

Sebelum kita memulai perjalanan 3D ini, pastikan Anda memiliki prasyarat berikut:

- Pengetahuan tentang pemrograman C# dan .NET.
- Visual Studio diinstal pada mesin Anda.
- Aspose.3D untuk perpustakaan .NET, yang dapat Anda unduh[Di Sini](https://releases.aspose.com/3d/net/).

Sekarang setelah Anda siap, mari terjun ke dunia pemrograman grafis 3D yang menakjubkan!

## Impor Namespace

Dalam proyek C# Anda, mulailah dengan mengimpor namespace yang diperlukan:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
```

Namespace ini menyediakan akses ke kelas dan metode penting yang diperlukan untuk bekerja dengan pemandangan 3D dan data geometri mesh.

## Langkah 1: Inisialisasi Adegan

```csharp
// Inisialisasi objek adegan
Scene scene = new Scene();
```

Ini menciptakan adegan 3D kosong tempat Anda dapat membuat dan memanipulasi model 3D Anda.

## Langkah 2: Tentukan Vektor Warna

```csharp
// Definisikan vektor warna
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

Tentukan serangkaian vektor warna yang akan diterapkan ke berbagai bagian adegan 3D Anda.

## Langkah 3: Buat Mesh dan Atur Warna

```csharp
// Panggil kelas Common membuat mesh menggunakan metode pembuat poligon untuk menyetel instance mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();

int idx = 0;
foreach (Vector3 color in colors)
{
    // Inisialisasi objek simpul kubus
    Node cube = new Node("cube");
    cube.Entity = mesh;
    LambertMaterial mat = new LambertMaterial();
    
    // Tetapkan warna
    mat.DiffuseColor = color;
    
    // Tetapkan materi
    cube.Material = mat;
    
    // Atur terjemahan
    cube.Transform.Translation = new Vector3(idx++ * 20, 0, 0);
    
    // Tambahkan simpul kubus
    scene.RootNode.ChildNodes.Add(cube);
}
```

Buat mesh menggunakan metode pembuat poligon dan terapkan warna ke berbagai bagian pemandangan.

## Langkah 4: Simpan Adegan 3D

```csharp
// Jalur ke direktori dokumen.
var output = "Your Output Directory" + "MeshGeometryData.fbx";

// Simpan adegan 3D dalam format file yang didukung
scene.Save(output, FileFormat.FBX7400ASCII);
```

Tentukan direktori keluaran dan simpan adegan 3D Anda dalam format file FBX7400ASCII.

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara bekerja dengan data geometri mesh dalam adegan 3D menggunakan Aspose.3D untuk .NET. Tutorial ini telah membekali Anda dengan langkah-langkah penting untuk membuat dan memanipulasi model 3D. Bereksperimen, jelajahi, dan tingkatkan keterampilan pemrograman grafis 3D Anda!

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

A1: Aspose.3D terutama dirancang untuk .NET, namun Anda dapat menjelajahi produk Aspose lainnya yang mendukung platform dan bahasa berbeda.

### Q2: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D?

 A2: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q3: Di mana saya dapat menemukan dukungan dan sumber daya tambahan?

 A3: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.

### Q4: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A4: Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q5: Format file apa yang didukung untuk menyimpan adegan 3D?

 A5: Aspose.3D mendukung berbagai format file, termasuk FBX, STL, dan lainnya. Mengacu kepada[dokumentasi](https://reference.aspose.com/3d/net/) untuk daftar lengkap.