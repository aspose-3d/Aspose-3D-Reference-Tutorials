---
date: 2026-01-09
description: Pelajari cara membuat adegan 3D menggunakan Aspose.3D untuk .NET, termasuk
  mengekspor wavefront OBJ dan cara memutar offset dalam ekstrusi linear.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Cara Membuat Adegan 3D dengan Twist Offset pada Ekstrusi Linear
url: /id/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat 3D Scene: Twist Offset dalam Linear Extrusion

## Introduction

Jika Anda perlu **create 3d scene** objek dengan cepat dan menambahkan geometri dinamis, Aspose.3D untuk .NET memberikan Anda alat yang tepat. Dalam **Aspose 3D tutorial** ini kami akan membahas teknik *how to twist offset* sambil melakukan **linear extrusion twist** dan akhirnya **export Wavefront OBJ** file. Pada akhir Anda akan memiliki model 3‑D lengkap siap untuk rendering atau pemrosesan lebih lanjut.

## Quick Answers
- **Apa yang dilakukan “twist offset”?** Ia menggeser titik awal twist sepanjang sumbu ekstrusi.  
- **Metode mana yang mengekspor Wavefront OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Apakah saya memerlukan lisensi untuk menjalankan contoh?** Lisensi sementara berfungsi untuk pengujian; lisensi penuh diperlukan untuk produksi.  
- **Versi .NET apa yang didukung?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Berapa banyak slices yang direkomendasikan untuk twist yang halus?** Sekitar 100 slices memberikan keseimbangan yang baik antara kualitas dan kinerja.

## Apa itu **create 3d scene**?

Membuat 3‑D scene berarti membangun struktur hierarkis yang menyimpan geometri, cahaya, kamera, dan transformasi. Aspose.3D menyediakan kelas `Scene` yang berfungsi sebagai kontainer akar untuk semua node yang Anda tambahkan.

## Mengapa menggunakan **linear extrusion twist**?

Linear extrusion dengan twist memungkinkan Anda mengubah profil 2‑D menjadi objek 3‑D berspiral—sempurna untuk sekrup, pegas, atau kolom dekoratif. Menambahkan twist offset memberi Anda kontrol lebih pada awal rotasi, memungkinkan desain asimetris.

## Prerequisites

Sebelum kita mulai, pastikan Anda memiliki:

- Aspose.3D for .NET Library: Unduh dan instal pustaka dari [release page](https://releases.aspose.com/3d/net/).  
- Lingkungan Pengembangan Anda: Visual Studio 2022 (atau IDE C# apa pun) siap untuk pengembangan .NET.

## Import Namespaces

Mulailah dengan mengimpor namespace yang diperlukan untuk mengakses fungsionalitas Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Langkah 1: Inisialisasi Profil Dasar  

Kami akan menggunakan persegi panjang dengan radius pembulatan kecil sebagai profil yang akan diekstrusi.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Langkah 2: Buat Scene  

Ini adalah kontainer tempat kami akan **create 3d scene** node.

```csharp
Scene scene = new Scene();
```

### Langkah 3: Buat Node  

Dua node saudara ditambahkan ke root – satu untuk ekstrusi reguler dan satu untuk versi offset.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Langkah 4: Linear Extrusion pada Node Kiri (twist dasar)  

Di sini kami mendemonstrasikan **linear extrusion twist** klasik tanpa offset.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Langkah 5: Linear Extrusion pada Node Kanan dengan **Twist Offset**  

Sekarang kami menerapkan teknik **how to twist offset** dengan menyediakan vektor `TwistOffset`.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Langkah 6: **Export Wavefront OBJ**  

Akhirnya, simpan scene yang telah dirakit ke file OBJ sehingga Anda dapat melihatnya di viewer 3‑D standar apa pun.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Common Issues & Tips

- **Twist terlihat datar?** Tingkatkan nilai `Slices` untuk geometri yang lebih halus.  
- **Offset tidak terlihat?** Pastikan vektor `TwistOffset` tidak nol dan sejajar dengan arah ekstrusi.  
- **File OBJ tidak memiliki tekstur?** OBJ hanya menyimpan geometri; gunakan file MTL untuk definisi material jika diperlukan.

## Frequently Asked Questions

**T: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?**  
A: Aspose.3D terutama menargetkan bahasa .NET, tetapi pustaka setara tersedia untuk Java dan platform lainnya.

**T: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D untuk .NET?**  
A: Kunjungi [this link](https://purchase.aspose.com/temporary-license/) untuk memperoleh lisensi sementara untuk keperluan pengujian.

**T: Apakah ada forum komunitas untuk Aspose.3D untuk .NET?**  
A: Tentu saja! Bergabunglah dengan komunitas di [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) untuk berinteraksi dengan sesama pengembang dan mencari bantuan.

**T: Apakah ada contoh dan dokumentasi tambahan yang tersedia?**  
A: Jelajahi [documentation](https://reference.aspose.com/3d/net/) untuk panduan dan contoh yang lengkap.

**T: Di mana saya dapat membeli Aspose.3D untuk .NET?**  
A: Kunjungi [this link](https://purchase.aspose.com/buy) untuk melakukan pembelian dan membuka potensi penuh Aspose.3D.

## Conclusion

Dalam **aspose 3d tutorial** ini Anda belajar cara **create 3d scene**, menerapkan **linear extrusion twist**, mengontrol **twist offset**, dan **export Wavefront OBJ** file. Teknik ini memungkinkan Anda menambahkan geometri berputar yang canggih ke proyek 3‑D apa pun dengan hanya beberapa baris kode.

---

**Terakhir Diperbarui:** 2026-01-09  
**Diuji Dengan:** Aspose.3D 24.11 for .NET  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}