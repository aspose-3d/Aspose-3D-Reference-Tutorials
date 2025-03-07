---
title: Putar dalam Ekstrusi Linier
linktitle: Putar dalam Ekstrusi Linier
second_title: Aspose.3D .NET API
description: Jelajahi dunia grafis 3D yang menawan dengan Aspose.3D untuk .NET. Pelajari langkah demi langkah Ekstrusi Linier dengan Twist.
weight: 14
url: /id/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Putar dalam Ekstrusi Linier

## Perkenalan

Di dunia perkembangan .NET yang terus berkembang, memanfaatkan kekuatan grafis 3D adalah upaya yang menarik. Aspose.3D untuk .NET muncul sebagai perangkat berharga, memberdayakan pengembang untuk membuat aplikasi yang imersif dan menakjubkan secara visual dengan mulus. Dalam panduan komprehensif ini, kita akan mempelajari satu fitur menarik - Ekstrusi Linier dengan Twist. Tutorial ini akan memandu Anda melalui proses langkah demi langkah, membuka potensi Aspose.3D untuk .NET.

## Prasyarat

Sebelum kita memulai perjalanan 3D ini, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D. Jika belum, Anda dapat mendownloadnya[Di Sini](https://releases.aspose.com/3d/net/).

- Pengetahuan Dasar Pengembangan .NET: Tutorial ini mengasumsikan pemahaman dasar tentang pengembangan .NET.

## Impor Namespace:

Dalam proyek .NET apa pun, penggunaan namespace yang tepat sangatlah penting. Mulailah dengan mengimpor namespace yang diperlukan untuk memanfaatkan fungsionalitas Aspose.3D secara efektif. Berikut cuplikan untuk memandu Anda:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Sekarang, mari kita uraikan proses menarik Ekstrusi Linier dengan Twist menggunakan Aspose.3D untuk .NET menjadi langkah-langkah yang mudah dicerna:

## Langkah 1: Inisialisasi Profil Dasar

```csharp
// Inisialisasi profil dasar yang akan diekstrusi
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Mulailah dengan menyiapkan profil dasar untuk ekstrusi. Dalam contoh ini, kita menggunakan bentuk persegi panjang dengan radius pembulatan tertentu.

## Langkah 2: Buat Adegan 3D

```csharp
// Membuat heboh
Scene scene = new Scene();
```

Ciptakan adegan 3D di mana semua keajaiban akan terjadi. Ini berfungsi sebagai kanvas untuk karya 3D kita.

## Langkah 3: Buat Node Kiri dan Kanan

```csharp
// Buat simpul kiri
var left = scene.RootNode.CreateChildNode();
// Buat simpul yang tepat
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

Hasilkan node kiri dan kanan dalam adegan. Sesuaikan terjemahan node kiri untuk memposisikannya dengan tepat.

## Langkah 4: Lakukan Ekstrusi Linier dengan Twist pada Node Kiri

```csharp
// Properti twist menentukan derajat rotasi saat mengekstrusi profil
//Lakukan ekstrusi linier pada node kiri menggunakan properti twist dan irisan
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

Ini adalah dimana keajaiban terjadi. Jalankan ekstrusi linier pada node kiri, dengan menggabungkan properti twist untuk menentukan derajat rotasi. Sesuaikan jumlah irisan untuk detail yang lebih halus.

## Langkah 5: Lakukan Ekstrusi Linier dengan Memutar pada Node Kanan

```csharp
// Lakukan ekstrusi linier pada node kanan menggunakan properti twist dan irisan
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

Cerminkan proses pada node kanan, bereksperimenlah dengan nilai putaran yang berbeda untuk mengamati variasi ekstrusi.

## Langkah 6: Simpan Adegan 3D

```csharp
// Simpan adegan 3D
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Terakhir, simpan karya 3D Anda ke direktori keluaran yang diinginkan. Sesuaikan nama file sesuai preferensi Anda.

## Kesimpulan

Dalam tutorial ini, kita telah menjelajahi ranah Ekstrusi Linier dengan Twist yang menawan menggunakan Aspose.3D untuk .NET. Fitur ini membuka pintu bagi kemungkinan kreatif, memungkinkan pengembang memasukkan elemen visual dinamis ke dalam aplikasi mereka dengan mudah.

## FAQ

### Q1: Bisakah saya menerapkan Ekstrusi Linier dengan Twist ke bentuk lain?

A1: Tentu saja! Anda dapat bereksperimen dengan berbagai profil dasar selain persegi panjang, membuka segudang kemungkinan desain.

### Q2: Apa peran properti 'Twist' dalam ekstrusi linier?

A2: Properti 'Twist' menentukan derajat rotasi selama proses ekstrusi, yang memengaruhi bentuk 3D akhir.

### Q3: Apakah ada pertimbangan kinerja saat menggunakan jumlah irisan yang banyak?

A3: Meskipun jumlah irisan yang lebih banyak menambah detail, hal ini dapat memengaruhi kinerja. Ciptakan keseimbangan berdasarkan kebutuhan aplikasi Anda.

### Q4: Dapatkah saya menggabungkan Ekstrusi Linier dengan fitur Aspose.3D lainnya?

A4: Tentu saja! Aspose.3D menawarkan serangkaian fitur yang kaya. Jangan ragu untuk menggabungkan Ekstrusi Linier dengan fungsi lain untuk desain yang lebih kompleks.

### Q5: Apakah ada komunitas untuk dukungan dan diskusi Aspose.3D?

 A5: Ya, bergabunglah dengan komunitas Aspose.3D di[Asumsikan Forum](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi yang menarik.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
