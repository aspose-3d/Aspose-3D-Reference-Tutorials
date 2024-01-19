---
title: Memisahkan Mesh berdasarkan Bahan
linktitle: Memisahkan Mesh berdasarkan Bahan
second_title: Aspose.3D .NET API
description: Pelajari cara membagi jerat 3D berdasarkan materi dengan Aspose.3D untuk .NET. Meningkatkan organisasi dan efisiensi adegan. Panduan langkah demi langkah untuk pengembang.
type: docs
weight: 22
url: /id/net/objects/split-mesh-by-material/
---
## Perkenalan
Selamat datang di tutorial komprehensif tentang pemisahan mesh berdasarkan material menggunakan Aspose.3D untuk .NET! Jika Anda seorang pengembang yang bekerja dengan grafik 3D dan ingin mengelola dan memanipulasi jerat secara efisien, Anda berada di tempat yang tepat. Dalam panduan ini, kita akan menjelajahi proses pemisahan mesh berdasarkan material, tugas penting dalam menciptakan pemandangan 3D yang beragam dan menarik secara visual.
## Prasyarat
Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:
-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D di proyek .NET Anda. Jika belum, Anda dapat mendownloadnya dari[rilis](https://releases.aspose.com/3d/net/) halaman.
- Pengetahuan Dasar Grafik 3D: Biasakan diri Anda dengan konsep dasar grafik 3D untuk memahami nuansa manipulasi mesh.
- Lingkungan Pengembangan: Siapkan lingkungan pengembangan .NET yang sesuai, seperti Visual Studio.
## Impor Namespace
Mulailah dengan mengimpor namespace yang diperlukan untuk mengakses fungsionalitas Aspose.3D. Sertakan yang berikut ini di awal kode Anda:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
Sekarang, mari kita bagi contoh ini menjadi beberapa langkah:
## Langkah 1: Membuat Kotak Mesh
```csharp
// Buat jaring kotak (terdiri dari 6 bidang)
Mesh box = (new Box()).ToMesh();
```
Di sini, kami menginisialisasi mesh yang mewakili sebuah kotak dengan enam bidang menggunakan Aspose.3D.
## Langkah 2: Menambahkan Bahan ke Mesh
```csharp
// Buat elemen material pada mesh ini
VertexElementMaterial mat = (VertexElementMaterial)box.CreateElement(VertexElementType.Material, MappingMode.Polygon, ReferenceMode.Index);
// Tentukan indeks material yang berbeda untuk setiap bidang
mat.Indices.AddRange(new int[] { 0, 1, 2, 3, 4, 5 });
```
Langkah ini melibatkan penambahan elemen material ke mesh dan menetapkan indeks material yang berbeda pada setiap bidang.
## Langkah 3: Memisahkan Mesh berdasarkan Material (Kebijakan CloneData)
```csharp
// Bagi menjadi 6 sub mesh, masing-masing bidang menjadi sub mesh
Mesh[] planes = PolygonModifier.SplitMesh(box, SplitMeshPolicy.CloneData);
```
Di sini, kami membagi mesh menjadi enam sub-mesh berdasarkan bahan yang ditentukan, menggunakan kebijakan CloneData.
## Langkah 4: Memperbarui Indeks Material untuk Data Ringkas
```csharp
mat.Indices.Clear();
mat.Indices.AddRange(new int[] { 0, 0, 0, 1, 1, 1 });
```
Perbarui indeks material untuk mempersiapkan operasi pemisahan berikutnya dengan kebijakan CompactData.
## Langkah 5: Memisahkan Mesh berdasarkan Material (Kebijakan CompactData)
```csharp
//Pisahkan menjadi 2 sub jerat, masing-masing berisi bidang tertentu
planes = PolygonModifier.SplitMesh(box, SplitMeshPolicy.CompactData);
```
Sekarang, kami membagi mesh menjadi dua sub-mesh, mengelompokkan bidang berdasarkan material, dan menggunakan kebijakan CompactData.
## Kesimpulan
Selamat! Anda telah berhasil mempelajari cara membagi mesh berdasarkan material menggunakan Aspose.3D untuk .NET. Teknik ini penting untuk mengelola pemandangan 3D yang kompleks secara efisien.
## Pertanyaan yang Sering Diajukan
### T: Dapatkah saya menerapkan teknik ini pada jerat khusus?
Sangat! Selama mesh Anda memiliki material tertentu, Anda dapat menggunakan pendekatan ini.
### T: Apa perbedaan kebijakan CloneData dengan kebijakan CompactData?
Kebijakan CloneData memastikan setiap sub-jaringan berbagi informasi titik kontrol yang sama, sedangkan kebijakan CompactData memberikan setiap sub-jaringan informasi titik kontrolnya sendiri.
### T: Apakah ada pertimbangan performa saat menggunakan metode ini?
Secara umum, kebijakan CloneData mungkin memiliki kinerja yang sedikit lebih baik karena informasi titik kontrol bersama.
### T: Dapatkah saya memvisualisasikan hasil pemisahan mesh?
Ya, Anda dapat merender dan memvisualisasikan sub-mesh yang dihasilkan menggunakan kemampuan rendering Aspose.3D.
### T: Apakah Aspose.3D cocok untuk pengembangan game?
Meskipun terutama digunakan untuk pemodelan dan rendering, Aspose.3D dapat diintegrasikan ke dalam jalur pengembangan game untuk tugas tertentu.