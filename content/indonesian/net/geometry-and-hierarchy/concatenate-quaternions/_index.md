---
title: Penggabungan Kuarter
linktitle: Penggabungan Kuarter
second_title: Aspose.3D .NET API
description: Jelajahi kekuatan manipulasi angka empat dalam adegan 3D dengan Aspose.3D untuk .NET. Pelajari cara menggabungkan angka empat selangkah demi selangkah untuk transformasi yang mendalam.
type: docs
weight: 11
url: /id/net/geometry-and-hierarchy/concatenate-quaternions/
---
## Perkenalan

Selamat datang di tutorial komprehensif tentang menggabungkan angka empat dalam adegan 3D menggunakan Aspose.3D untuk .NET! Jika Anda seorang pengembang atau penggemar 3D yang ingin meningkatkan keterampilan Anda dalam manipulasi angka empat, Anda berada di tempat yang tepat. Tutorial ini akan memandu Anda melalui proses langkah demi langkah, memastikan pengalaman belajar yang lancar.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET Library: Unduh dan instal perpustakaan dari[Asumsikan situs web](https://releases.aspose.com/3d/net/).
- Lingkungan Pengembangan: Pastikan Anda memiliki lingkungan pengembangan yang berfungsi untuk .NET.

## Impor Namespace

Dalam proyek .NET Anda, sertakan namespace yang diperlukan untuk memanfaatkan kekuatan Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Buat Adegan

Mulailah dengan membuat adegan 3D menggunakan perpustakaan Aspose.3D. Adegan tersebut akan berfungsi sebagai kanvas untuk manipulasi angka empat.

```csharp
Scene scene = new Scene();
```

## Langkah 2: Tentukan Quaternion

 Tentukan tiga angka empat,`q1`, `q2` , Dan`q3`, masing-masing mewakili rotasi tertentu.

```csharp
Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
Quaternion q3 = q1.Concat(q2);
```

## Langkah 3: Buat Silinder

Buat tiga silinder, masing-masing mewakili angka empat. Atur properti rotasi dan translasi berdasarkan angka empat yang ditentukan.

```csharp
Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.Transform.Rotation = q1;
cylinder.Transform.Translation = new Vector3(-5, 2, 0);

// Ulangi untuk q2 dan q3
```

## Langkah 4: Simpan ke File

Simpan adegan ke file, tentukan format output dan nama file.

```csharp
var output = "Your Output Directory" + "test_out.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

## Langkah 5: Tampilkan Pesan Sukses

Cetak pesan sukses bersama dengan jalur file setelah angka empat digabungkan dan file disimpan.

```csharp
Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);
```

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara menggabungkan angka empat dalam adegan 3D menggunakan Aspose.3D untuk .NET. Bereksperimenlah dengan kombinasi angka empat yang berbeda untuk mencapai transformasi unik dalam proyek Anda.

## FAQ

### Q1: Apa yang dimaksud dengan angka empat dalam grafik 3D?

A1: Quaternion adalah entitas matematika yang digunakan untuk merepresentasikan rotasi dalam ruang 3D, sehingga memberikan keunggulan dibandingkan representasi rotasi lainnya.

### Q2: Bisakah saya menggunakan Aspose.3D untuk .NET dengan perpustakaan .NET lainnya?

A2: Ya, Aspose.3D untuk .NET dirancang untuk bekerja secara lancar dengan pustaka .NET lainnya.

### Q3: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D untuk .NET?

A3: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D untuk .NET?

 A4: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.

### Q5: Bisakah saya menggunakan lisensi sementara Aspose.3D untuk .NET?

 A5: Ya, Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).