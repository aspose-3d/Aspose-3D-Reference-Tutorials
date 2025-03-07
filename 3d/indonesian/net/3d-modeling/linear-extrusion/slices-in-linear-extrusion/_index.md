---
title: Irisan dalam Ekstrusi Linier
linktitle: Irisan dalam Ekstrusi Linier
second_title: Aspose.3D .NET API
description: Jelajahi dunia desain 3D dengan Aspose.3D untuk .NET. Buat model menakjubkan menggunakan tutorial ekstrusi linier kami.
weight: 13
url: /id/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Irisan dalam Ekstrusi Linier

## Perkenalan

Selamat datang di dunia desain 3D menggunakan Aspose.3D untuk .NET! Baik Anda seorang pengembang berpengalaman atau baru memulai, tutorial ini akan memandu Anda melalui proses pembuatan visualisasi 3D yang menakjubkan menggunakan pustaka Aspose.3D yang canggih.

## Prasyarat

Sebelum terjun ke dunia desain 3D dengan Aspose.3D, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk Perpustakaan .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D. Anda dapat mengunduhnya dari[Di Sini](https://releases.aspose.com/3d/net/).

- Lingkungan Pengembangan Terpadu (IDE): Gunakan IDE pilihan apa pun yang kompatibel dengan pengembangan .NET.

- Pemahaman Dasar C#: Biasakan diri Anda dengan dasar-dasar bahasa pemrograman C#.

- Keinginan untuk Menjelajahi Desain 3D: Semangat untuk menciptakan model 3D yang menakjubkan secara visual!

## Impor Namespace

Untuk memulai perjalanan desain 3D Anda dengan Aspose.3D, Anda perlu mengimpor namespace yang diperlukan. Ini memastikan bahwa kode Anda dapat mengakses kelas dan fungsi yang diperlukan.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Ekstrusi Linier - Irisan dalam Ekstrusi Linier

Sekarang, mari selami contoh praktisnya - Ekstrusi Linier dengan Irisan. Teknik ini memungkinkan Anda membuat model 3D yang rumit dengan tingkat detail yang bervariasi.

### Langkah 1: Inisialisasi Profil Dasar

```csharp
// ExStart:InisialisasiBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd: InisialisasiBaseProfile
```

### Langkah 2: Buat Adegan 3D

```csharp
// ExStart:Buat3DScene
Scene scene = new Scene();
// ExEnd:Buat3DScene
```

### Langkah 3: Buat Node Kiri dan Kanan

```csharp
// ExStart:BuatNodeKiriKanan
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:BuatNodeKiriKanan
```

### Langkah 4: Lakukan Ekstrusi Linier pada Node Kiri

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Langkah 5: Lakukan Ekstrusi Linier pada Node Kanan

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Langkah 6: Simpan Adegan 3D

```csharp
// ExStart:Simpan3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
//ExEnd:Simpan3DScene
```

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara melakukan Ekstrusi Linier dengan Irisan menggunakan Aspose.3D untuk .NET. Ini hanyalah awal dari perjalanan desain 3D Anda dengan Aspose.3D - keluarkan kreativitas Anda dan jelajahi kemungkinan tanpa batas!

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

A1: Aspose.3D terutama dirancang untuk .NET, namun Anda dapat menjelajahi opsi interoperabilitas dengan bahasa seperti Python menggunakan pengikatan .NET.

### Q2: Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D untuk .NET?

 A2: Lihat dokumentasi[Di Sini](https://reference.aspose.com/3d/net/) untuk informasi mendalam tentang kemampuan dan penggunaan Aspose.3D.

### Q3: Apakah ada uji coba gratis yang tersedia untuk Aspose.3D untuk .NET?

 A3: Ya, Anda dapat mengikuti uji coba gratis[Di Sini](https://releases.aspose.com/)untuk menjelajahi fitur perpustakaan sebelum melakukan pembelian.

### Q4: Bagaimana saya bisa mendapatkan dukungan teknis untuk Aspose.3D untuk .NET?

 A4: Kunjungi forum Aspose.3D[Di Sini](https://forum.aspose.com/c/3d/18) untuk mencari bantuan dan terlibat dengan masyarakat.

### Q5: Bisakah saya menggunakan lisensi sementara Aspose.3D untuk .NET?

 A5: Ya, dapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/) untuk tujuan evaluasi.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
