---
title: Silinder Bawah Geser yang Disesuaikan
linktitle: Silinder Bawah Geser yang Disesuaikan
second_title: Aspose.3D .NET API
description: Pelajari cara membuat silinder bawah geser khusus menggunakan Aspose.3D untuk .NET dengan panduan langkah demi langkah terperinci kami. Tingkatkan keterampilan pemodelan 3D Anda hari ini!
type: docs
weight: 12
url: /id/net/3d-modeling/working-with-cylinder/
---
## Perkenalan
Selamat datang di panduan komprehensif kami tentang cara membuat silinder khusus menggunakan Aspose.3D untuk .NET. Jika Anda ingin meningkatkan keterampilan pemodelan 3D dan menambahkan fitur unik ke proyek Anda, Anda berada di tempat yang tepat. Dalam tutorial ini, kami akan memandu Anda melalui proses langkah demi langkah, menggunakan penjelasan yang jelas dan cuplikan kode.
## Prasyarat
Sebelum kita mendalami tutorialnya, pastikan Anda memiliki hal-hal berikut:
- Pemahaman dasar tentang pemrograman C# dan .NET.
-  Aspose.3D untuk perpustakaan .NET diinstal. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/net/).
- Lingkungan pengembangan yang disiapkan untuk pemrograman .NET.
## Impor Namespace
Dalam kode C# Anda, mulailah dengan mengimpor namespace yang diperlukan:
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
Mulailah dengan membuat adegan 3D menggunakan Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Langkah 2: Buat Silinder 1
Hasilkan silinder pertama dan atur propertinya:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Langkah 3: Sesuaikan Shear Bottom untuk Silinder 1
Terapkan dasar geser khusus ke silinder pertama:
```csharp
//Geser 47,5 derajat pada bidang xy (sumbu z)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Setel GenerateFanCylinder ke benar
cylinder1.GenerateFanCylinder = true;
// Setel Panjang Theta
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Setel OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## Langkah 4: Tambahkan Silinder 1 ke Adegan
Tambahkan silinder pertama ke tempat kejadian dan atur terjemahannya:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Langkah 5: Buat Silinder 2
Hasilkan silinder kedua dengan properti serupa:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Langkah 6: Tambahkan Silinder 2 ke Adegan
Tambahkan silinder kedua ke tempat kejadian tanpa parameter khusus:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Langkah 7: Simpan Adegan
Simpan adegan sebagai file Wavefront OBJ di direktori dokumen Anda:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Kesimpulan
Selamat! Anda telah berhasil membuat silinder bawah geser khusus menggunakan Aspose.3D untuk .NET. Tutorial ini bertujuan untuk memberikan panduan langkah demi langkah bagi pengguna dengan berbagai tingkat keahlian dalam pemodelan dan pemrograman 3D.
## Pertanyaan yang Sering Diajukan
### Apakah Aspose.3D untuk .NET cocok untuk pemula?
Sangat! Aspose.3D untuk .NET menawarkan antarmuka yang ramah pengguna, sehingga dapat diakses oleh pemula dan pengembang berpengalaman.
### Bisakah saya menerapkan sudut geser yang berbeda pada silinder?
Ya, Anda dapat menyesuaikan dasar geser untuk setiap silinder satu per satu, sehingga Anda dapat memperoleh efek unik.
### Apakah ada versi uji coba yang tersedia?
 Ya, Anda dapat menjelajahi versi uji coba gratis[Di Sini](https://releases.aspose.com/).
### Di mana saya bisa mendapatkan dukungan tambahan?
 Mengunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.
### Bagaimana saya bisa mendapatkan lisensi sementara?
 Dapatkan lisensi sementara Anda[Di Sini](https://purchase.aspose.com/temporary-license/).