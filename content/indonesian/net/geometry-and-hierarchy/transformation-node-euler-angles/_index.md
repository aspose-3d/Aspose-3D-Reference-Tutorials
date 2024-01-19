---
title: Mengubah Node dengan Sudut Euler dalam Pemandangan 3D
linktitle: Mengubah Node dengan Sudut Euler dalam Pemandangan 3D
second_title: Aspose.3D .NET API
description: Pelajari cara mengubah node 3D dengan mudah dengan Aspose.3D untuk .NET. Ikuti panduan langkah demi langkah kami untuk hasil menakjubkan dalam proyek Anda.
type: docs
weight: 19
url: /id/net/geometry-and-hierarchy/transformation-node-euler-angles/
---
## Perkenalan

Selamat datang di tutorial komprehensif tentang mengubah node dengan sudut Euler dalam adegan 3D menggunakan Aspose.3D untuk .NET. Dalam panduan ini, kita akan mempelajari dunia grafis 3D yang menarik dan menjelajahi proses penambahan transformasi ke sebuah node menggunakan sudut Euler. Aspose.3D untuk .NET menyediakan alat canggih untuk bekerja dengan adegan dan jerat 3D, menjadikannya pilihan tepat bagi pengembang yang mencari keserbagunaan dan efisiensi dalam proyek mereka.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk Perpustakaan .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/net/).

- Lingkungan Pengembangan: Siapkan lingkungan pengembangan .NET pilihan Anda, seperti Visual Studio.

## Impor Namespace

Mulailah dengan mengimpor namespace yang diperlukan untuk mengakses fungsionalitas yang disediakan oleh Aspose.3D untuk .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Sekarang, mari kita bagi contoh ini menjadi beberapa langkah untuk pemahaman yang lebih jelas.

## Langkah 1: Inisialisasi Objek Adegan

```csharp
// ExStart:TambahkanTransformasiKeNodeByEulerAngles
// Inisialisasi objek adegan
Scene scene = new Scene();
```

 Mulailah dengan membuat adegan 3D baru menggunakan`Scene` kelas.

## Langkah 2: Inisialisasi Objek Kelas Node

```csharp
// Inisialisasi objek kelas Node
Node cubeNode = new Node("cube");
```

 Buat node dalam adegan menggunakan`Node`kelas. Node ini akan berfungsi sebagai wadah untuk objek 3D kita.

## Langkah 3: Buat Mesh Menggunakan Polygon Builder

```csharp
// Panggil kelas Common membuat mesh menggunakan metode pembuat poligon untuk menyetel instance mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 
```

 Panggil metode (dalam hal ini,`CreateMeshUsingPolygonBuilder` dari suatu adat`Common` class) untuk menghasilkan mesh untuk objek 3D.

## Langkah 4: Arahkan Node ke Geometri Mesh

```csharp
// Arahkan simpul ke geometri Mesh
cubeNode.Entity = mesh;
```

Kaitkan mesh yang dibuat dengan node.

## Langkah 5: Tetapkan Sudut Euler dan Terjemahan

```csharp
// Sudut Euler
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Atur terjemahan
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Tentukan sudut Euler dan translasi node untuk memposisikannya dalam ruang 3D.

## Langkah 6: Tambahkan Kubus ke Adegan

```csharp
// Tambahkan kubus ke tempat kejadian
scene.RootNode.ChildNodes.Add(cubeNode);
```

Gabungkan node ke dalam hierarki adegan.

## Langkah 7: Simpan Adegan 3D

```csharp
// Jalur ke direktori dokumen.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Simpan adegan 3D dalam format file yang didukung
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:TambahkanTransformasiKeNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Tentukan direktori output dan simpan adegan 3D, termasuk node yang diubah, dalam format file yang diinginkan (dalam hal ini FBX7500ASCII).

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara mengubah simpul berdasarkan sudut Euler dalam adegan 3D menggunakan Aspose.3D untuk .NET. Perpustakaan yang kuat ini membuka pintu menuju kemungkinan tak terbatas dalam pengembangan grafis 3D.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan alat pemodelan 3D lainnya?

A1: Aspose.3D mendukung berbagai format file 3D, meningkatkan kompatibilitas dengan alat pemodelan populer.

### Q2: Dapatkah saya menerapkan beberapa transformasi ke satu node?

A2: Ya, Anda dapat menggabungkan dan menerapkan beberapa transformasi untuk mencapai efek yang kompleks.

### Q3: Di mana saya dapat menemukan dokumentasi Aspose.3D tambahan?

 A3: Lihat[dokumentasi](https://reference.aspose.com/3d/net/) untuk informasi rinci dan contoh.

### Q4: Apakah saya memerlukan lisensi untuk menggunakan Aspose.3D untuk .NET?

 A4: Ya, Anda bisa mendapatkan lisensi[Di Sini](https://purchase.aspose.com/buy) atau jelajahi a[uji coba gratis](https://releases.aspose.com/).

### Q5: Butuh bantuan atau punya pertanyaan spesifik?

A5: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan masyarakat.