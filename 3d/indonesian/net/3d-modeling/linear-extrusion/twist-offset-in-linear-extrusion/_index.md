---
title: Twist Offset dalam Ekstrusi Linier
linktitle: Twist Offset dalam Ekstrusi Linier
second_title: Aspose.3D .NET API
description: Jelajahi keajaiban Aspose.3D untuk .NET dengan panduan langkah demi langkah kami tentang Twist Offset dalam Linear Extrusion. Tingkatkan proyek 3D Anda dengan mudah.
type: docs
weight: 15
url: /id/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---
## Perkenalan

Selamat datang di dunia Aspose.3D untuk .NET, perpustakaan serbaguna yang memberdayakan pengembang untuk menangani manipulasi 3D dengan mudah. Dalam tutorial ini, kita akan mempelajari salah satu fitur menarik - "Twist Offset in Linear Extrusion." Jika Anda siap untuk meningkatkan keterampilan pemrograman 3D Anda, mari selami!

## Prasyarat

Sebelum kita memulai perjalanan menarik ini, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET Library: Unduh dan instal perpustakaan dari[halaman rilis](https://releases.aspose.com/3d/net/).

- Lingkungan Pengembangan Anda: Pastikan lingkungan pengembangan Anda telah diatur dan siap dijalankan.

## Impor Namespace

Mulailah dengan mengimpor namespace yang diperlukan untuk mengakses fungsionalitas yang disediakan oleh Aspose.3D untuk .NET. Dalam kode Anda, ini mungkin terlihat seperti:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Sekarang, mari kita bagi contoh ini menjadi langkah-langkah yang dapat dikelola untuk menguasai Twist Offset dalam Ekstrusi Linier:

## Langkah 1: Inisialisasi Profil Dasar

Mulailah dengan membuat profil dasar, di sini dicontohkan dengan bentuk persegi panjang dengan radius pembulatan yang ditentukan.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Langkah 2: Buat Adegan

Hasilkan adegan 3D untuk menampung node dan bentuk Anda.

```csharp
Scene scene = new Scene();
```

## Langkah 3: Buat Node

Bangun node dalam adegan, kiri dan kanan.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Langkah 4: Ekstrusi Linier pada Node Kiri

Lakukan ekstrusi linier pada simpul kiri menggunakan properti twist dan irisan.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Langkah 5: Ekstrusi Linier pada Node Kanan dengan Twist Offset

Pada node kanan, lakukan ekstrusi linier menggunakan properti twist, twist offset, dan irisan.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Langkah 6: Simpan Adegan 3D

Simpan adegan 3D ke direktori keluaran yang Anda inginkan, tentukan format file sebagai WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Selamat! Anda telah berhasil mengimplementasikan Twist Offset di Linear Extrusion menggunakan Aspose.3D untuk .NET.

## Kesimpulan

Dalam tutorial ini, kami menjelajahi kemampuan hebat Aspose.3D untuk .NET, khususnya berfokus pada Twist Offset di Linear Extrusion. Dengan keterampilan baru ini, Anda diperlengkapi dengan baik untuk memasukkan dinamisme ke dalam proyek 3D Anda.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

A1: Aspose.3D terutama mendukung bahasa .NET, namun Aspose menyediakan perpustakaan serupa untuk Java dan platform lainnya.

### Q2: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk .NET?

 A2: Kunjungi[Link ini](https://purchase.aspose.com/temporary-license/)untuk memperoleh lisensi sementara untuk tujuan pengujian.

### Q3: Apakah ada forum komunitas untuk Aspose.3D untuk .NET?

 A3: Tentu saja! Bergabunglah dengan komunitas di[Forum Asumsikan.3D](https://forum.aspose.com/c/3d/18) untuk terlibat dengan sesama pengembang dan mencari bantuan.

### Q4: Apakah ada contoh dan dokumentasi tambahan yang tersedia?

 A4: Jelajahi[dokumentasi](https://reference.aspose.com/3d/net/) untuk panduan dan contoh ekstensif.

### Q5: Di mana saya dapat membeli Aspose.3D untuk .NET?

 A5: Pergilah ke[Link ini](https://purchase.aspose.com/buy) untuk melakukan pembelian dan membuka potensi penuh Aspose.3D.