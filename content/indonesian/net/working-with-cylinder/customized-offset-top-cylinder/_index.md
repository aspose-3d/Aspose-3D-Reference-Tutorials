---
title: Silinder Atas Offset yang Disesuaikan
linktitle: Silinder Atas Offset yang Disesuaikan
second_title: Aspose.3D .NET API
description: Jelajahi keajaiban grafis 3D dengan Aspose.3D untuk .NET. Pelajari cara membuat silinder atas offset khusus dengan mudah. Tingkatkan pengalaman coding Anda sekarang!
type: docs
weight: 11
url: /id/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Perkenalan
Selamat datang di dunia manipulasi grafis 3D dengan Aspose.3D untuk .NET! Dalam tutorial ini, kami akan memandu Anda melalui proses pembuatan silinder atas offset yang disesuaikan menggunakan Aspose.3D, pustaka canggih untuk bekerja dengan adegan, objek, dan format 3D dalam aplikasi .NET.
## Prasyarat
Sebelum kita masuk ke tutorialnya, pastikan Anda memiliki prasyarat berikut:
- Pengetahuan dasar bahasa pemrograman C#.
- Visual Studio diinstal pada mesin Anda.
- Aspose.3D untuk perpustakaan .NET diunduh dan direferensikan dalam proyek Anda.
Sekarang, mari kita mulai dengan panduan langkah demi langkah!
## Impor Namespace
Pertama, pastikan untuk mengimpor namespace yang diperlukan dalam kode C# Anda:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Langkah 1: Buat Adegan
```csharp
// Membuat heboh
Scene scene = new Scene();
```
Ini menginisialisasi adegan 3D baru menggunakan Aspose.3D.
## Langkah 2: Inisialisasi Silinder
```csharp
// Inisialisasi silinder
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Di sini, kita membuat silinder dengan parameter tertentu seperti radius, tinggi, dan irisan.
## Langkah 3: Atur OffsetTop untuk Silinder Pertama
```csharp
// Setel OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Ini menetapkan bagian atas offset yang disesuaikan untuk silinder pertama.
## Langkah 4: Buat ChildNode untuk Silinder Pertama
```csharp
// Buat Node Anak
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Kami menambahkan silinder pertama sebagai simpul anak ke tempat kejadian, menyesuaikan posisinya.
## Langkah 5: Inisialisasi Silinder Kedua
```csharp
//Inisialisasi silinder kedua tanpa OffsetTop yang disesuaikan
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Silinder kedua diinisialisasi tanpa bagian atas offset yang disesuaikan.
## Langkah 6: Buat ChildNode untuk Silinder Kedua
```csharp
// Buat Node Anak
scene.RootNode.CreateChildNode(cylinder2);
```
Kami menambahkan silinder kedua sebagai node anak ke tempat kejadian.
## Langkah 7: Simpan Adegan
```csharp
// Menyimpan
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Ini menyimpan adegan 3D, termasuk silinder atas offset yang disesuaikan, dalam format Wavefront OBJ.
Sekarang Anda telah berhasil membuat silinder atas offset yang disesuaikan menggunakan Aspose.3D untuk .NET!
## Kesimpulan
Dalam tutorial ini, kita telah menjelajahi dasar-dasar bekerja dengan Aspose.3D untuk .NET untuk membuat silinder atas offset yang disesuaikan. Pustaka ini membuka kemungkinan tak terbatas untuk manipulasi grafis 3D dalam aplikasi .NET Anda.
## FAQ
### T: Di mana saya dapat menemukan dokumentasi Aspose.3D untuk .NET?
 J: Dokumentasinya tersedia[Di Sini](https://reference.aspose.com/3d/net/).
### T: Bagaimana cara mengunduh Aspose.3D untuk .NET?
 J: Anda dapat mendownloadnya[Di Sini](https://releases.aspose.com/3d/net/).
### T: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D untuk .NET?
 A: Ya, Anda bisa mendapatkan uji coba gratis[Di Sini](https://releases.aspose.com/).
### T: Di mana saya bisa mendapatkan dukungan Aspose.3D untuk .NET?
 J: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan.
### T: Bisakah saya mendapatkan lisensi sementara Aspose.3D untuk .NET?
 A: Ya, Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).