---
title: Mengubah Torus Primitif menjadi Mesh
linktitle: Mengubah Torus Primitif menjadi Mesh
second_title: Aspose.3D .NET API
description: Jelajahi kekuatan Aspose.3D untuk .NET dengan panduan langkah demi langkah kami dalam mengonversi primitif Torus menjadi jerat. Tingkatkan pengembangan 3D Anda dengan mudah!
type: docs
weight: 17
url: /id/net/objects/convert-torus-primitive-to-mesh/
---
## Perkenalan
Apakah Anda ingin memanfaatkan kekuatan Aspose.3D untuk .NET untuk mengonversi primitif Torus menjadi mesh dengan mulus? Tidak perlu mencari lagi! Dalam tutorial ini, kami akan memandu Anda melalui prosesnya, menguraikan setiap langkah untuk memastikan perjalanan yang lancar. Aspose.3D untuk .NET menyediakan platform yang kuat untuk memanipulasi adegan 3D, menjadikannya alat yang tepat bagi pengembang yang mencari efisiensi dan fleksibilitas.
## Prasyarat
Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:
-  Aspose.3D untuk .NET: Unduh dan instal perpustakaan. Anda dapat menemukan tautan unduhan[Di Sini](https://releases.aspose.com/3d/net/).
-  File 3D: Siapkan contoh file 3D dalam format yang didukung. Jika Anda tidak memilikinya, Anda dapat memanfaatkannya[tes.fbx](https://reference.aspose.com/3d/net/) file dari dokumentasi Aspose.3D.
## Impor Namespace
Dalam proyek .NET Anda, impor namespace yang diperlukan untuk memastikan kelancaran integrasi dengan Aspose.3D. Tambahkan yang berikut ini di awal kode Anda:
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
Scene scene = new Scene(RunExamples.GetDataFilePath("test.fbx"));
```
Muat file 3D Anda ke dalam adegan. Mengganti`"test.fbx"` dengan jalur ke file Anda.
## Langkah 2: Inisialisasi Objek Kelas Node
```csharp
Node torusNode = new Node("torus");
```
Buat objek simpul baru untuk primitif Torus.
## Langkah 3: Ubah Torus menjadi Mesh
```csharp
IMeshConvertible convertible = new Torus();
Mesh mesh = convertible.ToMesh();
```
Manfaatkan kemampuan Aspose.3D untuk mengubah primitif Torus menjadi mesh.
## Langkah 4: Arahkan Node ke Geometri Mesh
```csharp
torusNode.Entity = mesh;
```
Kaitkan geometri mesh dengan node.
## Langkah 5: Tambahkan Node ke Adegan
```csharp
scene.RootNode.ChildNodes.Add(torusNode);
```
Integrasikan node torus ke dalam scene.
## Langkah 6: Simpan Adegan 3D
```csharp
var output = "Your Output Directory" + "TorusToMeshScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
Console.WriteLine("\nConverted the primitive Torus to a mesh successfully.\nFile saved at " + output);
```
Simpan adegan 3D yang dimodifikasi dalam format file dan lokasi yang diinginkan.
## Kesimpulan
Selamat! Anda telah berhasil mengubah primitif Torus menjadi mesh menggunakan Aspose.3D untuk .NET. Pustaka yang kuat ini membuka banyak kemungkinan untuk manipulasi 3D dalam proyek .NET Anda.
## FAQ
### Apakah Aspose.3D kompatibel dengan semua format file 3D?
Aspose.3D mendukung berbagai format file 3D. Periksa dokumentasi untuk daftar lengkapnya.
### Bisakah saya menggunakan Aspose.3D untuk proyek komersial?
 Ya, Aspose.3D menawarkan lisensi komersial. Mengunjungi[pembelian.aspose.com/buy](https://purchase.aspose.com/buy) untuk detailnya.
### Apakah ada lisensi sementara yang tersedia untuk tujuan pengujian?
 Ya, Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/) untuk pengujian.
### Di mana saya dapat menemukan dukungan untuk Aspose.3D?
 Mengunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan bantuan masyarakat.
### Bisakah saya menjelajahi lebih banyak tutorial dan contoh?
 Ya, lihat[dokumentasi](https://reference.aspose.com/3d/net/) untuk tutorial dan contoh yang komprehensif.