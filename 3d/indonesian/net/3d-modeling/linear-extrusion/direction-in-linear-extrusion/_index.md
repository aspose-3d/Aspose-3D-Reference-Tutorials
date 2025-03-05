---
title: Arah dalam Ekstrusi Linier
linktitle: Arah dalam Ekstrusi Linier
second_title: Aspose.3D .NET API
description: Buka dunia pemodelan 3D dengan Aspose.3D untuk .NET. Pelajari arah ekstrusi linier, tingkatkan kreativitas, dan buat aplikasi imersif dengan mudah.
type: docs
weight: 11
url: /id/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---
## Perkenalan

Dalam dunia pengembangan perangkat lunak yang dinamis, membuat model 3D yang imersif adalah keterampilan yang sangat diperlukan. Aspose.3D untuk .NET memberi pengembang seperangkat alat canggih untuk memanfaatkan potensi pemodelan 3D dalam aplikasi mereka. Dalam tutorial ini, kita akan mempelajari dunia ekstrusi linier yang menarik dan menjelajahi nuansa fitur "Arah dalam Ekstrusi Linier".

## Prasyarat

Sebelum kita memulai perjalanan menarik ini, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Unduh dan instal perpustakaan dari[Dokumentasi Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- Lingkungan Pengembangan: Pastikan Anda telah menyiapkan lingkungan pengembangan .NET yang berfungsi.

## Impor Namespace

Dalam proyek .NET Anda, impor namespace yang diperlukan untuk mengakses fungsionalitas Aspose.3D. Tambahkan baris berikut ke awal kode Anda:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Inisialisasi Profil Dasar

Mulailah dengan menginisialisasi profil dasar yang akan diekstrusi. Dalam contoh ini, kita membuat bentuk persegi panjang dengan radius pembulatan 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Langkah 2: Buat Adegan 3D

Bangun fondasi untuk karya 3D Anda dengan membuat sebuah adegan.

```csharp
Scene scene = new Scene();
```

## Langkah 3: Buat Node

Hasilkan node dalam adegan untuk mewakili berbagai komponen lingkungan 3D Anda.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Langkah 4: Ekstrusi Linier tanpa Arah

 Lakukan ekstrusi linier pada node kiri menggunakan`Twist` Dan`Slices` properti.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Langkah 5: Ekstrusi Linier dengan Arah

 Perluas kemampuan ekstrusi dengan menggabungkan`Direction` properti di node kanan.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Langkah 6: Simpan Adegan 3D

 Pertahankan kreasi Anda dengan menyimpan adegan 3D. Mengganti`"Your Output Directory"` dengan direktori yang diinginkan.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Selamat! Anda telah berhasil menerapkan ekstrusi linier dengan Aspose.3D untuk .NET, menjelajahi pendekatan tradisional dan terarah.

## Kesimpulan

Dalam tutorial ini, kita menavigasi dunia pemodelan 3D yang menakjubkan menggunakan Aspose.3D untuk .NET. Ekstrusi linier, dengan dan tanpa arah, membuka kemungkinan tak terbatas bagi pengembang yang ingin menciptakan aplikasi visual yang menakjubkan. Dengan Aspose.3D, kekuatan pemodelan 3D ada di ujung jari Anda.

## FAQ

### Q1: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk .NET?

 A1: Kunjungi[Ajukan Lisensi Sementara](https://purchase.aspose.com/temporary-license/) untuk mendapatkan izin sementara.

### Q2: Di mana saya dapat menemukan dukungan untuk Aspose.3D?

 A2: Bergabunglah dengan[Forum Asumsikan.3D](https://forum.aspose.com/c/3d/18) untuk mencari bantuan dan berhubungan dengan masyarakat.

### Q3: Apakah tersedia uji coba gratis?

 A3: Ya, jelajahi fitur-fiturnya dengan uji coba gratis di[Rilis Aspose.3D](https://releases.aspose.com/).

### Q4: Bagaimana cara membeli Aspose.3D untuk .NET?

 A4: Navigasikan ke[Asumsikan Halaman Pembelian](https://purchase.aspose.com/buy) untuk opsi lisensi dan detail pembelian.

### Q5: Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D untuk .NET?

 A5: Lihat secara komprehensif[Dokumentasi Aspose.3D .NET](https://reference.aspose.com/3d/net/) untuk informasi mendalam.