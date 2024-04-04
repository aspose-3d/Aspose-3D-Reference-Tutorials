---
title: Pusatkan dalam Ekstrusi Linier
linktitle: Pusatkan dalam Ekstrusi Linier
second_title: Aspose.3D .NET API
description: Jelajahi dunia pemodelan 3D dengan Aspose.3D untuk .NET. Pusatkan teknik ekstrusi linier, ciptakan desain menakjubkan, dan bebaskan kreativitas Anda.
type: docs
weight: 10
url: /id/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---
## Perkenalan

Selamat datang di panduan komprehensif tentang menguasai ekstrusi linier menggunakan Aspose.3D untuk .NET. Jika Anda ingin meningkatkan keterampilan pemodelan 3D dan membuat ekstrusi yang menakjubkan, Anda berada di tempat yang tepat. Dalam tutorial ini, kita akan mempelajari teknik ekstrusi linier, khususnya berfokus pada aspek pemusatan untuk membawa desain Anda ke tingkat yang benar-benar baru.

## Prasyarat

Sebelum kita memulai perjalanan menarik ini, pastikan Anda memiliki prasyarat berikut:

- Pemahaman dasar bahasa pemrograman C#.
- Visual Studio diinstal pada mesin Anda.
-  Aspose.3D untuk perpustakaan .NET, yang dapat Anda unduh dari[Dokumentasi Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  Pastikan Anda memiliki akses ke[Dokumentasi Aspose.3D .NET](https://reference.aspose.com/3d/net/) untuk referensi sepanjang tutorial.

## Impor Namespace

Untuk memulai, mari impor namespace yang diperlukan. Ini akan meletakkan dasar bagi mahakarya pemodelan 3D kami.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Inisialisasi Profil Dasar

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Langkah 2: Buat Adegan 3D

```csharp
Scene scene = new Scene();
```

## Langkah 3: Buat Node Kiri dan Kanan

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Langkah 4: Lakukan Ekstrusi Linier pada Node Kiri

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Langkah 5: Tetapkan Bidang Tanah untuk Referensi

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Langkah 6: Lakukan Ekstrusi Linier pada Node Kanan

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Langkah 7: Tetapkan Bidang Tanah untuk Referensi (Node Kanan)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Langkah 8: Simpan Adegan 3D

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Kesimpulan

Selamat! Anda telah berhasil menguasai seni ekstrusi linier dengan pemusatan menggunakan Aspose.3D untuk .NET. Jangan ragu untuk bereksperimen dengan berbagai parameter dan jelajahi kemungkinan luas yang ditawarkan teknik ini.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

A1: Aspose.3D terutama mendukung bahasa .NET seperti C# dan VB.NET.

### Q2: Di mana saya dapat menemukan dukungan untuk pertanyaan terkait Aspose.3D?

 A2: Kunjungi[Forum Asumsikan.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi khusus.

### Q3: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D untuk .NET?

 A3: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk .NET?

 A4: Anda dapat memperoleh lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya dapat membeli lisensi Aspose.3D untuk .NET?

 A5: Beli lisensi Anda[Di Sini](https://purchase.aspose.com/buy).
