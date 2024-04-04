---
title: Transformasi Node dengan Matriks Transformasi
linktitle: Transformasi Node dengan Matriks Transformasi
second_title: Aspose.3D .NET API
description: Transformasikan node dengan mudah dalam adegan 3D menggunakan Aspose.3D untuk .NET. Pelajari transformasi node langkah demi langkah dengan tutorial.
type: docs
weight: 21
url: /id/net/geometry-and-hierarchy/transformation-node-matrix/
---
## Perkenalan

Dalam dunia grafis dan visualisasi 3D yang dinamis, kemampuan memanipulasi objek dalam sebuah adegan merupakan aspek yang sangat penting. Aspose.3D untuk .NET memberdayakan pengembang untuk mengubah node dengan mulus menggunakan matriks transformasi, menambahkan lapisan kreativitas dan kontrol pada adegan 3D. Tutorial ini akan memandu Anda melalui proses transformasi node dalam adegan 3D langkah demi langkah.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

1.  Aspose.3D untuk Perpustakaan .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D di proyek .NET Anda. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/net/).

2. Lingkungan Pengembangan: Siapkan lingkungan pengembangan .NET yang berfungsi, dan jika Anda belum melakukannya, buat proyek baru tempat Anda akan mengimplementasikan transformasi.

## Impor Namespace

Mulailah dengan mengimpor namespace yang diperlukan ke proyek .NET Anda. Namespace ini menyediakan kelas dan metode penting untuk manipulasi adegan 3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Sekarang setelah kita membahas dasar-dasarnya, mari kita uraikan proses transformasi menjadi panduan langkah demi langkah.

## Langkah 1: Inisialisasi Adegan

```csharp
// ExStart:TambahkanTransformasiToNodeByTransformationMatrix
// Inisialisasi objek adegan
Scene scene = new Scene();

```

Pada langkah ini, kita membuat adegan 3D kosong baru.

## Langkah 2: Buat Mesh dan Lampirkan Ke Adegan

```csharp
// Panggil kelas Common membuat mesh menggunakan metode pembuat poligon untuk menyetel instance mesh
Mesh mesh = (new Box()).ToMesh();

// Buat node kontainer untuk mesh.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Di sini, kita membuat mesh menggunakan metode pembuat poligon dan menetapkannya ke node, sehingga membentuk geometri untuk kubus kita.

## Langkah 3: Tetapkan Matriks Terjemahan Kustom

```csharp
// Tetapkan matriks terjemahan khusus
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Tentukan matriks terjemahan khusus untuk menentukan transformasi spesifik yang diterapkan pada node. Sesuaikan nilai matriks sesuai kebutuhan untuk transformasi yang Anda inginkan.

Sertakan node kubus dalam adegan, menjadikannya bagian dari keseluruhan lingkungan 3D.

## Langkah 4: Simpan Adegan

```csharp
// Jalur ke direktori dokumen.
var output = "TransformationToNode.fbx";

// Simpan adegan 3D dalam format file yang didukung
scene.Save(output);
// ExEnd:TambahkanTransformasiToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Tentukan direktori keluaran dan nama file, lalu simpan adegan 3D dalam format file yang diinginkan. Dalam contoh ini, kami menyimpannya dalam format FBX7500ASCII.

## Kesimpulan

Selamat! Anda telah berhasil mengubah node menggunakan matriks transformasi dalam adegan 3D dengan Aspose.3D untuk .NET. Kemampuan ini membuka pintu bagi aplikasi 3D yang beragam dan menawan secara visual.

## FAQ

### Q1: Apa yang dimaksud dengan matriks transformasi dalam grafik 3D?

A1: Matriks transformasi adalah representasi matematis yang digunakan untuk menerapkan berbagai transformasi (translasi, rotasi, penskalaan) pada objek dalam ruang 3D.

### Q2: Dapatkah saya menerapkan beberapa transformasi ke satu node?

A2: Ya, Anda dapat menggabungkan beberapa transformasi dengan mengalikan matriksnya masing-masing dan menerapkan hasilnya ke node.

### Q3: Apakah ada format file lain yang didukung untuk menyimpan adegan 3D?

 A3: Aspose.3D untuk .NET mendukung berbagai format file, termasuk STL, GLTF, OBJ, dan banyak lagi. Mengacu kepada[dokumentasi](https://reference.aspose.com/3d/net/) untuk daftar lengkap.

### Q4: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk .NET?

 A4: Kunjungi[halaman lisensi sementara](https://purchase.aspose.com/temporary-license/)di situs web Aspose untuk mendapatkan lisensi sementara untuk tujuan evaluasi.

### Q5: Di mana saya bisa mencari bantuan atau terhubung dengan komunitas Aspose.3D?

 A5: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk mengajukan pertanyaan, berbagi pengalaman, dan terhubung dengan pengembang lain menggunakan Aspose.3D.