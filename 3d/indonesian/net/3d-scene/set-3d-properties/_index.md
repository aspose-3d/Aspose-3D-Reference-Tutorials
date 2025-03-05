---
title: Mengatur Properti Tiga Dimensi dalam Pemandangan 3D
linktitle: Mengatur Properti Tiga Dimensi dalam Pemandangan 3D
second_title: Aspose.3D .NET API
description: Jelajahi tutorial Aspose.3D untuk .NET tentang pengaturan properti 3D. Pelajari langkah demi langkah dengan contoh kode. Tingkatkan keterampilan manipulasi adegan 3D Anda.
type: docs
weight: 14
url: /id/net/3d-scene/set-3d-properties/
---
## Perkenalan

Membuat pemandangan tiga dimensi yang menawan sering kali memerlukan kemampuan untuk memanipulasi berbagai properti, menambah kedalaman dan realisme pada proyek Anda. Aspose.3D untuk .NET menyediakan seperangkat alat canggih untuk mencapai hal ini, memungkinkan Anda mengatur dan memodifikasi properti tiga dimensi dalam adegan 3D Anda dengan mudah. Dalam tutorial ini, kita akan menjelajahi proses langkah demi langkah, meningkatkan pemahaman Anda tentang cara memanfaatkan Aspose.3D untuk .NET secara efektif.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan di proyek .NET Anda. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/net/).

- Direktori Dokumen: Buat direktori untuk menyimpan dokumen 3D Anda.

Sekarang setelah Anda memiliki hal-hal penting, mari jelajahi proses pengaturan properti tiga dimensi dalam adegan 3D menggunakan Aspose.3D untuk .NET.

## Impor Namespace

Untuk memulai, impor namespace yang diperlukan ke dalam proyek Anda. Namespace ini menyediakan kelas dan metode yang diperlukan untuk bekerja dengan properti tiga dimensi di Aspose.3D untuk .NET.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Langkah 1: Muat Adegan 3D

Mulailah dengan memuat adegan 3D. Dalam contoh ini, kami menggunakan file FBX dengan tekstur tertanam.

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Langkah 2: Akses Properti Material

Akses properti material dari adegan 3D yang dimuat untuk memanipulasi karakteristiknya.

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Langkah 3: Daftar Semua Properti

Buat daftar semua properti material menggunakan perulangan foreach atau perulangan for ordinal.

```csharp
//ExStart: DaftarSemuaProperti
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//atau menggunakan for loop biasa
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: DaftarSemuaProperti
```

## Langkah 4: Dapatkan dan Ubah Properti berdasarkan Nama

Ambil dan ubah properti tertentu berdasarkan namanya.

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//ubah nilai properti berdasarkan nama
props["Diffuse"] = new Vector3(1, 0, 1);
//ExEnd: GetModifyPropertyByName
```

## Langkah 5: Dapatkan Instans Properti berdasarkan Nama

Ambil contoh properti berdasarkan namanya untuk manipulasi lebih lanjut.

```csharp
//ExStart: DapatkanPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: DapatkanPropertyInstanceByName
```

## Langkah 6: Melintasi Properti Properti

 Sejak`Property` diwarisi dari`A3DObject`Anda dapat melintasi properti suatu properti.

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//dan beberapa properti yang hanya ditentukan dalam file FBX:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal pada properti properti dimungkinkan
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Kesimpulan

Selamat! Anda sekarang telah menguasai seni mengatur properti tiga dimensi dalam adegan 3D menggunakan Aspose.3D untuk .NET. Bereksperimenlah dengan berbagai properti dan nilai untuk menghidupkan proyek 3D Anda.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk .NET dengan format file 3D lainnya?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, termasuk FBX, STL, dan masih banyak lagi.

### Q2: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk .NET?

 A2: Kunjungi[Di Sini](https://purchase.aspose.com/temporary-license/) untuk mendapatkan izin sementara.

### Q3: Apakah ada forum komunitas untuk pengguna Aspose.3D?

 A3: Ya, Anda dapat menemukan dukungan dan diskusi di[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D untuk .NET?

 A4: Lihat[dokumentasi](https://reference.aspose.com/3d/net/) untuk panduan komprehensif.

### Q5: Bisakah saya mencoba Aspose.3D untuk .NET secara gratis sebelum membeli?

 A5: Tentu saja! Unduh[versi percobaan gratis](https://releases.aspose.com/) untuk menjelajahi fitur-fiturnya.
