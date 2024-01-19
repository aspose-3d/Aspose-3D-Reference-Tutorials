---
title: Melakukan Ekstrusi Linier
linktitle: Melakukan Ekstrusi Linier
second_title: Aspose.3D .NET API
description: Jelajahi dunia grafis 3D dengan Aspose.3D untuk .NET. Melakukan Ekstrusi Linier dalam panduan langkah demi langkah ini.
type: docs
weight: 12
url: /id/net/linear-extrusion/performing-linear-extrusion/
---
## Perkenalan:

Mulailah perjalanan mendebarkan ke dunia grafis 3D dengan Aspose.3D untuk .NET, pembangkit tenaga listrik yang meningkatkan permainan pengembangan Anda. Dalam tutorial ini, kita akan mempelajari seluk-beluk Ekstrusi Linier – sebuah teknik menarik yang menghidupkan profil 2D statis, mendorongnya ke dunia 3D yang dinamis. Mari buka pintu kreativitas dan inovasi menggunakan Aspose.3D!

## Prasyarat:

Sebelum terjun ke dunia manipulasi 3D yang mempesona, pastikan Anda memiliki prasyarat berikut:

1. Instalasi Aspose.3D:
   -  Mulailah dengan mengunduh dan menginstal Aspose.3D untuk .NET dari[Di Sini](https://releases.aspose.com/3d/net/).
   -  Ikuti petunjuk instalasi yang disediakan dalam dokumentasi[Di Sini](https://reference.aspose.com/3d/net/).

2. Menyiapkan Lingkungan Pengembangan Anda:
   - Pastikan lingkungan pengembangan Anda dikonfigurasi dengan benar dengan namespace yang diperlukan untuk Aspose.3D.

Sekarang setelah Anda bersiap, mari terjun ke keajaiban Aspose.3D!

## Impor Namespace:

Sertakan namespace penting untuk memulai petualangan 3D Anda:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Namespace ini meletakkan dasar bagi perjalanan pengkodean 3D Anda, menyediakan akses ke alat yang diperlukan untuk integrasi fungsionalitas Aspose.3D tanpa hambatan.

## Melakukan Ekstrusi Linier:

Mari buat objek 3D yang memukau melalui Linear Extrusion menggunakan Aspose.3D. Ikuti langkah ini:

## Langkah 1: Inisialisasi Profil Dasar
```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Langkah ini menyiapkan profil 2D yang akan menjadi fondasi karya 3D kita. Sesuaikan parameter sesuai kebutuhan untuk mencapai bentuk dan bentuk yang diinginkan.

## Langkah 2: Ekstrusi Linier
```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

Di sini, Ekstrusi Linier dilakukan, mengambil profil 2D dan memperluasnya ke dimensi ketiga. Bereksperimenlah dengan parameter seperti 'Irisan' dan 'Putar' untuk membentuk kreasi Anda.

## Langkah 3: Buat Adegan
```csharp
Scene scene = new Scene();
```

Kanvas kosong dibuat – pemandangan di mana objek 3D Anda akan menjadi hidup.

## Langkah 4: Tambahkan Ekstrusi ke Adegan
```csharp
scene.RootNode.CreateChildNode(extrusion);
```

Karya agung Anda yang diekstrusi ditambahkan sebagai simpul anak ke tempat kejadian.

## Langkah 5: Simpan Adegan 3D
```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Terakhir, simpan kreasi Anda dalam format yang diinginkan. Dalam contoh ini, disimpan sebagai file Wavefront OBJ.

Sekarang, lihatlah keajaiban 3D Anda!

## Kesimpulan:

Selamat! Anda baru saja menggali permukaan potensi Aspose.3D. Tutorial ini hanya memberi petunjuk pada lanskap luas yang menunggu untuk Anda jelajahi. Selami dokumentasi, bereksperimen dengan berbagai bentuk, dan buka berbagai kemungkinan dengan Aspose.3D untuk .NET.

## FAQ:

### Q1: Apakah Aspose.3D cocok untuk pemula?

A1: Tentu saja! Aspose.3D menawarkan lingkungan yang ramah pengguna, dan tutorial kami memandu Anda melalui dasar-dasarnya.

### Q2: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?

 A2: Ya, Aspose.3D hadir dengan opsi lisensi untuk penggunaan pribadi dan komersial. Memeriksa[Di Sini](https://purchase.aspose.com/buy) untuk detailnya.

### Q3: Bagaimana saya bisa mendapatkan lisensi sementara untuk pengujian?

 A3: Kunjungi[Link ini](https://purchase.aspose.com/temporary-license/) untuk mendapatkan izin sementara untuk tujuan pengujian.

### Q4: Di mana saya bisa mendapatkan dukungan komunitas?

 A4: Bergabunglah dengan[Forum Asumsikan.3D](https://forum.aspose.com/c/3d/18) untuk terhubung dengan komunitas yang dinamis dan mencari bantuan.

### Q5: Apakah tersedia uji coba gratis?

 A5: Tentu saja! Unduh versi uji coba gratis[Di Sini](https://releases.aspose.com/) untuk merasakan kemampuan Aspose.3D secara langsung.