---
title: Membuat Silinder Kipas
linktitle: Membuat Silinder Kipas
second_title: Aspose.3D .NET API
description: Buka dunia desain 3D dengan Aspose.3D untuk .NET! Buat silinder kipas dan non-kipas yang menakjubkan dengan mudah. Unduh uji coba Anda sekarang.
type: docs
weight: 10
url: /id/net/working-with-cylinder/create-fan-cylinder/
---
## Perkenalan
Selamat datang di dunia pemodelan dan visualisasi 3D dengan Aspose.3D untuk .NET! Dalam panduan langkah demi langkah ini, kita akan mempelajari cara membuat silinder kipas yang menawan menggunakan Aspose.3D untuk .NET. Aspose.3D adalah perpustakaan canggih yang menyediakan kemampuan luas untuk bekerja dengan konten 3D dalam aplikasi .NET.
## Prasyarat
Sebelum kita terjun ke dunia pemodelan 3D yang menarik, pastikan Anda memiliki prasyarat berikut:
- Pemahaman dasar tentang pemrograman .NET.
- Visual Studio diinstal pada mesin Anda.
-  Aspose.3D untuk perpustakaan .NET, yang dapat Anda unduh[Di Sini](https://releases.aspose.com/3d/net/).
- Minat tulus untuk mengeluarkan kreativitas Anda melalui desain 3D.
## Impor Namespace
Mari kita mulai dengan mengimpor namespace yang diperlukan untuk membuat fungsionalitas Aspose.3D tersedia di proyek .NET Anda.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Impor namespace Aspose.3D
```
Sekarang kita sudah siap, mari kita bagi proses pembuatan silinder kipas menjadi langkah-langkah yang dapat dikelola.
## Langkah 1: Buat Adegan
```csharp
// Membuat heboh
Scene scene = new Scene();
```
Mulailah dengan menginisialisasi adegan 3D baru. Ini berfungsi sebagai kanvas tempat silinder kipas kita akan hidup.
## Langkah 2: Buat Silinder Kipas
```csharp
// Buat silinder
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Tentukan karakteristik silinder kipas Anda, tentukan parameter seperti radius, tinggi, dan resolusi.
## Langkah 3: Sesuaikan Properti Silinder Kipas
```csharp
// Setel GenerateFanCylinder ke benar
fan.GenerateFanCylinder = true;
// Setel Panjang Theta
fan.ThetaLength = MathUtils.ToRadian(270);
```
Sesuaikan silinder kipas Anda dengan mengaktifkan pembuatan bagian kipas dan menyesuaikan sapuan sudut menggunakan ThetaLength.
## Langkah 4: Posisikan Silinder Kipas di Pemandangan
```csharp
// Buat Node Anak
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Tambahkan silinder kipas sebagai node anak ke node akar adegan dan posisikan dalam ruang 3D.
## Langkah 5: Buat Silinder Non-Kipas
```csharp
// Buat silinder tanpa kipas
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Jelajahi fleksibilitas Aspose.3D dengan membuat silinder tanpa bagian kipas.
## Langkah 6: Sesuaikan Properti Silinder Non-Kipas
```csharp
// Setel GenerateFanCylinder ke salah
nonfan.GenerateFanCylinder = false;
// Setel Panjang Theta
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Bedakan silinder non-kipas dengan menonaktifkan pembangkitan bagian kipas.
## Langkah 7: Posisikan Silinder Non-Kipas di Pemandangan
```csharp
// Buat Node Anak
scene.RootNode.CreateChildNode(nonfan);
```
Demikian pula, tambahkan silinder non-kipas sebagai simpul anak ke simpul akar adegan.
## Langkah 8: Simpan Adegan
```csharp
// Simpan adegan
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Simpan karya Anda dalam format dan lokasi yang diinginkan. Sekarang, Anda telah berhasil membuat silinder kipas dan non-kipas menggunakan Aspose.3D untuk .NET!
## Kesimpulan
Selamat telah menyelesaikan panduan praktis pemodelan 3D dengan Aspose.3D untuk .NET! Anda telah mengeluarkan kreativitas Anda di dunia digital, membuat silinder kipas dan non-kipas dengan mudah.
## Pertanyaan yang Sering Diajukan
### Bisakah saya menggunakan Aspose.3D untuk .NET dengan kerangka .NET lainnya?
Ya, Aspose.3D kompatibel dengan berbagai kerangka .NET, memberikan fleksibilitas dalam proyek pengembangan Anda.
### Apakah ada uji coba gratis yang tersedia untuk Aspose.3D untuk .NET?
 Ya, Anda dapat menjelajahi uji coba gratis[Di Sini](https://releases.aspose.com/).
### Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D untuk .NET?
 Dokumentasi tersedia[Di Sini](https://reference.aspose.com/3d/net/).
### Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D untuk .NET?
 Kunjungi forum dukungan[Di Sini](https://forum.aspose.com/c/3d/18)atas bantuan dari masyarakat dan pakar Aspose.
### Apakah lisensi sementara tersedia untuk Aspose.3D untuk .NET?
 Ya, lisensi sementara dapat diperoleh[Di Sini](https://purchase.aspose.com/temporary-license/).