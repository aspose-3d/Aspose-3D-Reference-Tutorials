---
title: Mengekspor ke Format PLY sebagai Point Cloud
linktitle: Mengekspor ke Format PLY sebagai Point Cloud
second_title: Aspose.3D .NET API
description: Jelajahi dunia pemodelan 3D dengan Aspose.3D untuk .NET. Pelajari cara mengekspor model ke format PLY dengan mudah. Tingkatkan proyek Anda dengan visual yang menakjubkan.
type: docs
weight: 16
url: /id/net/loading-and-saving/ply/export-to-ply-point-cloud/
---
## Perkenalan
Dalam dunia pemodelan dan pengembangan 3D yang dinamis, Aspose.3D untuk .NET menonjol sebagai perangkat yang canggih. Tutorial ini akan memandu Anda melalui proses mengekspor model 3D ke format PLY sebagai point cloud menggunakan Aspose.3D untuk .NET. Jika Anda siap untuk menyempurnakan proyek Anda dengan visual yang menakjubkan, ikuti dan buka potensi penuh dari perpustakaan serbaguna ini.
## Prasyarat
Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:
-  Aspose.3D untuk .NET: Unduh dan instal perpustakaan dari[Unduh Halaman](https://releases.aspose.com/3d/net/).
- Lingkungan Pengembangan: Siapkan lingkungan pengembangan .NET pilihan Anda, seperti Visual Studio.
## Impor Namespace
Untuk memulai Aspose.3D untuk .NET, impor namespace yang diperlukan dalam proyek Anda:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Langkah 1: Buat Model 3D
Mulailah dengan membuat model 3D yang ingin Anda ekspor sebagai point cloud. Sebagai contoh, mari kita buat sebuah bola:
```csharp
Sphere sphere = new Sphere();
```
## Langkah 2: Tentukan Pengaturan Ekspor
Tentukan pengaturan ekspor, termasuk format file (PLY) dan aktifkan ekspor point cloud:
```csharp
PlySaveOptions saveOptions = new PlySaveOptions() { PointCloud = true };
```
## Langkah 3: Tetapkan Jalur Ekspor
Tentukan direktori tempat Anda ingin menyimpan file PLY yang diekspor:
```csharp
string exportPath = "Your Document Directory" + "sphere.ply";
```
## Langkah 4: Enkode dan Ekspor
 Memanfaatkan`Encode` metode untuk mengekspor model 3D ke format PLY:
```csharp
FileFormat.PLY.Encode(sphere, exportPath, saveOptions);
```
## Kesimpulan
Selamat! Anda telah berhasil mengekspor model 3D ke format PLY sebagai point cloud menggunakan Aspose.3D untuk .NET. Ini membuka kemungkinan tak terbatas untuk mengintegrasikan visual yang imersif ke dalam aplikasi Anda.

## FAQ
### 1. Apakah Aspose.3D kompatibel dengan semua kerangka .NET?
Aspose.3D mendukung berbagai kerangka .NET, memastikan kompatibilitas di berbagai lingkungan pengembangan.
### 2. Bisakah saya menggunakan Aspose.3D untuk proyek komersial?
 Sangat! Aspose.3D menawarkan opsi lisensi yang fleksibel, termasuk penggunaan komersial. Lihat[halaman pembelian](https://purchase.aspose.com/buy) untuk detailnya.
### 3. Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D?
 Mengunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk terhubung dengan masyarakat dan mendapatkan bantuan dari para ahli.
### 4. Apakah tersedia uji coba gratis?
 Ya, jelajahi fitur-fiturnya dengan a[uji coba gratis](https://releases.aspose.com/) sebelum membuat komitmen.
### 5. Bagaimana cara mendapatkan izin sementara?
 Untuk opsi lisensi sementara, kunjungi[Link ini](https://purchase.aspose.com/temporary-license/).