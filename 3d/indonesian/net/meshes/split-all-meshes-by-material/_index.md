---
title: Memisahkan Semua Jalinan Adegan berdasarkan Materi
linktitle: Memisahkan Semua Jalinan Adegan berdasarkan Materi
second_title: Aspose.3D .NET API
description: Pelajari cara membagi jerat 3D berdasarkan materi menggunakan Aspose.3D untuk .NET. Ikuti panduan langkah demi langkah kami untuk pengorganisasian dan pengelolaan model 3D yang efisien.
type: docs
weight: 21
url: /id/net/meshes/split-all-meshes-by-material/
---
## Perkenalan
Selamat datang di panduan langkah demi langkah tentang memisahkan semua jerat adegan 3D berdasarkan materi menggunakan Aspose.3D untuk .NET. Jika Anda bekerja dengan model 3D dan ingin mengatur jerat berdasarkan bahan secara efisien, tutorial ini cocok untuk Anda. Aspose.3D adalah perpustakaan .NET yang kuat yang menyediakan berbagai fitur untuk bekerja dengan file 3D, menjadikannya pilihan yang sangat baik bagi pengembang.
## Prasyarat
Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:
- Pemahaman dasar bahasa pemrograman C#.
- Visual Studio diinstal pada mesin Anda.
-  Aspose.3D untuk perpustakaan .NET. Anda dapat mengunduhnya dari[Di Sini](https://releases.aspose.com/3d/net/).
- File masukan 3D (misalnya, "test.fbx") yang ingin Anda pisahkan.
## Impor Namespace
Mulailah dengan mengimpor namespace yang diperlukan dalam proyek C# Anda:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Langkah 1: Muat File 3D
```csharp
// Jalur ke direktori dokumen.
string input = RunExamples.GetDataFilePath("test.fbx");
// Muat file 3D
Scene scene = new Scene(input);
```
 Pada langkah ini, kita memuat file 3D menggunakan Aspose.3D`Scene` kelas.
## Langkah 2: Pisahkan Semua Jerat
```csharp
// Pisahkan semua jerat
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 Di sini, kami menggunakan`SplitMesh` metode dari`PolygonModifier` kelas untuk membagi semua jerat berdasarkan materi.
## Langkah 3: Simpan Adegan Terpisah
```csharp
// Menyimpan file
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
Simpan adegan yang dimodifikasi ke file baru untuk menyimpan perubahan.
## Langkah 4: Tampilkan Pesan Sukses
```csharp
// Tampilkan pesan sukses
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
Cetak pesan sukses yang menunjukkan bahwa operasi berhasil diselesaikan.
## Kesimpulan
Selamat! Anda telah berhasil mempelajari cara membagi semua jerat adegan 3D berdasarkan materi menggunakan Aspose.3D untuk .NET. Ini bisa menjadi teknik yang berharga untuk mengatur dan mengelola model 3D yang kompleks.
## FAQ
### 1. Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?
Aspose.3D terutama dirancang untuk .NET, tetapi menyediakan interoperabilitas dengan bahasa lain melalui pengikatan bahasa .NET.
### 2. Apakah tersedia versi uji coba?
 Ya, Anda dapat mengakses versi uji coba gratis[Di Sini](https://releases.aspose.com/).
### 3. Di mana saya dapat menemukan contoh dan dokumentasi lainnya?
 Jelajahi dokumentasi komprehensif di[Dokumentasi Aspose.3D](https://reference.aspose.com/3d/net/).
### 4. Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D?
 Mengunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.
### 5. Bisakah saya memperoleh izin sementara?
 Ya, Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).