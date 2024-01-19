---
title: Mengubah Node demi Quaternion dalam Adegan 3D
linktitle: Mengubah Node demi Quaternion dalam Adegan 3D
second_title: Aspose.3D .NET API
description: Pelajari cara mengubah node 3D dengan angka empat menggunakan Aspose.3D untuk .NET. Panduan langkah demi langkah untuk pemula.
type: docs
weight: 20
url: /id/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## Perkenalan

Selamat datang di panduan langkah demi langkah tentang mengubah simpul demi angka empat dalam adegan 3D menggunakan Aspose.3D untuk .NET. Dalam tutorial ini, kita akan menjelajahi kemampuan hebat Aspose.3D untuk .NET dan menelusuri proses penambahan transformasi ke node 3D menggunakan angka empat.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D. Anda dapat mengunduhnya dari[halaman rilis](https://releases.aspose.com/3d/net/).

- Lingkungan Pengembangan: Siapkan lingkungan pengembangan .NET Anda dengan alat dan konfigurasi yang diperlukan.

- Pemahaman Dasar Konsep 3D: Keakraban dengan grafik dan konsep 3D akan sangat membantu.

## Impor Namespace

Dalam proyek .NET Anda, sertakan namespace yang diperlukan untuk Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Inisialisasi Objek Pemandangan

```csharp
// ExStart:TambahkanTransformasiToNodeByQuaternion
// Inisialisasi objek adegan
Scene scene = new Scene();
```

## Langkah 2: Inisialisasi Objek Kelas Node

```csharp
// Inisialisasi objek kelas Node
Node cubeNode = new Node("cube");
```

## Langkah 3: Buat Mesh menggunakan Polygon Builder

```csharp
// Panggil kelas Common membuat mesh menggunakan metode pembuat poligon untuk menyetel instance mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Langkah 4: Arahkan Node ke Geometri Mesh

```csharp
// Arahkan simpul ke geometri Mesh
cubeNode.Entity = mesh;
```

## Langkah 5: Atur Rotasi menggunakan Quaternion

```csharp
// Atur rotasi
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Langkah 6: Atur Terjemahan

```csharp
// Atur terjemahan
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Langkah 7: Tambahkan Kubus ke Adegan

```csharp
// Tambahkan kubus ke tempat kejadian
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Langkah 8: Simpan Adegan 3D

```csharp
// Jalur ke direktori dokumen.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Simpan adegan 3D dalam format file yang didukung
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:TambahkanTransformasiToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara mengubah simpul demi angka empat dalam adegan 3D menggunakan Aspose.3D untuk .NET. Jelajahi lebih banyak fitur dan kemungkinan dengan mengacu pada[dokumentasi](https://reference.aspose.com/3d/net/).

## FAQ

### Q1: Apa yang dimaksud dengan angka empat dalam grafik 3D?

A1: Quaternion adalah entitas matematika yang digunakan untuk merepresentasikan rotasi dalam ruang 3D.

### Q2: Bagaimana cara mengunduh Aspose.3D untuk .NET?

 A2: Anda dapat mengunduh perpustakaan dari[halaman rilis](https://releases.aspose.com/3d/net/).

### Q3: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D untuk .NET?

 A3: Ya, Anda bisa mendapatkan uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk .NET?

 A4: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi.

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A5: Dapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).
