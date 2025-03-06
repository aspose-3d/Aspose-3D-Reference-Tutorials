---
title: Mengekspor Adegan 3D ke Format AMF Terkompresi
linktitle: Mengekspor Adegan ke AMF Terkompresi
second_title: Aspose.3D .NET API
description: Pelajari cara mengekspor adegan 3D ke format AMF terkompresi menggunakan Aspose.3D untuk .NET. Tingkatkan keterampilan pengembangan Anda dengan panduan langkah demi langkah ini.
weight: 11
url: /id/net/loading-and-saving/amf/export-scene-compressed-amf/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Mengekspor Adegan 3D ke Format AMF Terkompresi

## Perkenalan

Dalam dunia pemodelan dan rendering 3D yang dinamis, efisiensi dan fleksibilitas adalah yang terpenting. Aspose.3D untuk .NET memberdayakan pengembang untuk mengekspor adegan 3D dengan lancar ke format AMF (Additive Manufacturing File) terkompresi, memastikan ukuran file optimal tanpa mengurangi kualitas. Tutorial ini akan memandu Anda melalui proses langkah demi langkah, sehingga memudahkan pemula dan pengembang berpengalaman untuk memanfaatkan kemampuan Aspose.3D untuk .NET.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

- Pemahaman dasar konsep pemodelan 3D
- Visual Studio diinstal pada mesin Anda
-  Aspose.3D untuk perpustakaan .NET. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/net/)
- Keinginan untuk meningkatkan keterampilan pengembangan 3D Anda!

## Impor Namespace

Dalam proyek Anda, pastikan Anda mengimpor namespace yang diperlukan untuk memanfaatkan fungsionalitas Aspose.3D untuk .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Langkah 1: Muat Adegan 3D

Mulailah dengan memuat adegan 3D menggunakan Aspose.3D untuk .NET. Buat objek adegan dan tambahkan entitas seperti kotak ke dalamnya:

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Langkah 2: Transformasi Skala

Selanjutnya, terapkan transformasi skala ke kotak lain di tempat kejadian:

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scaling = new Vector3(5, 5, 5);
```

## Langkah 3: Tetapkan Sudut Euler

Tetapkan sudut Euler untuk transformasi:

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Langkah 4: Simpan File AMF Terkompresi

Terakhir, simpan adegan 3D ke file AMF terkompresi di direktori keluaran yang Anda inginkan:

```csharp
scene.Save("Your Output Directory/" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Kesimpulan

Selamat! Anda telah berhasil mengekspor adegan 3D ke format AMF terkompresi menggunakan Aspose.3D untuk .NET. Pustaka yang kuat ini membuka banyak kemungkinan bagi pengembang 3D, memungkinkan mereka membuat model yang efisien dan menakjubkan secara visual.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan perangkat lunak pemodelan 3D populer?

A1: Aspose.3D mendukung berbagai format file, sehingga kompatibel dengan alat pemodelan 3D yang populer.

### Q2: Bisakah saya mengaktifkan kompresi untuk format file lain selain AMF?

A2: Ya, Aspose.3D menyediakan opsi untuk mengaktifkan kompresi untuk berbagai format file.

### Q3: Apakah Aspose.3D cocok untuk pemula dan pengembang tingkat lanjut?

A3: Tentu saja! Aspose.3D menawarkan kesederhanaan untuk pemula dan fitur-fitur canggih untuk pengembang berpengalaman.

### Q4: Apakah ada batasan ukuran adegan 3D yang dapat diekspor?

A4: Aspose.3D dirancang untuk menangani adegan dengan kompleksitas yang berbeda-beda, dan tidak ada batasan ukuran yang ketat.

### Q5: Di mana saya bisa mendapatkan dukungan tambahan dan diskusi komunitas?

 A5: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
