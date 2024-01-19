---
title: Memuat dan Menyimpan - Opsi Pemuatan Khusus
linktitle: Memuat dan Menyimpan - Opsi Pemuatan Khusus
second_title: Aspose.3D .NET API
description: Jelajahi Aspose.3D untuk .NET, solusi terbaik untuk pemuatan dan penyimpanan model 3D yang lancar.
type: docs
weight: 15
url: /id/net/loading-and-saving/custom-load-options/
---
## Perkenalan

Selamat datang di dunia Aspose.3D untuk .NET – perpustakaan canggih yang memberdayakan pengembang untuk bekerja secara lancar dengan file 3D. Dalam tutorial ini, kita akan mempelajari seluk-beluk memuat dan menyimpan model 3D, dengan fokus pada opsi pemuatan khusus. Baik Anda pengembang berpengalaman atau pendatang baru, panduan ini akan memandu Anda melalui proses langkah demi langkah, memastikan Anda memanfaatkan potensi penuh Aspose.3D untuk .NET.

## Prasyarat

Sebelum kita memulai perjalanan ini, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/net/).

- Direktori Dokumen: Buat direktori untuk menyimpan file model 3D Anda.

Sekarang setelah Anda memiliki hal-hal penting, mari selami dunia manipulasi model 3D yang menarik!

## Impor Namespace

Hal pertama yang pertama, mari impor namespace yang diperlukan. Ini akan menyiapkan panggung untuk perjalanan kita ke dunia Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Memuat dan Menyimpan - Opsi Pemuatan Khusus

### Langkah 1: Memuat File Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    // Jalur ke direktori dokumen.
    string dataDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Tetapkan opsi khusus
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Langkah 2: Memuat File OBJ

```csharp
private static void ObjLoadOption()
{
    // Jalur ke direktori dokumen.
    string dataDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Tetapkan opsi khusus
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Langkah 3: Memuat File STL

```csharp
private static void STLLoadOption()
{
    // Jalur ke direktori dokumen.
    string dataDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Tetapkan opsi khusus
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Langkah 4: Memuat File U3D

```csharp
private static void U3DLoadOption()
{
    // Jalur ke direktori dokumen.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Tetapkan opsi khusus
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Langkah 5: Memuat File glTF

```csharp
private static void glTFLoadOptions()
{
    // Jalur ke direktori dokumen.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Tetapkan opsi khusus
    loadOpt.FlipTexCoordV = true;
    scene.Open(dataDir + "Duck.gltf", loadOpt);
}
```

### Langkah 6: Memuat File PLY

```csharp
private static void PlyLoadOptions()
{
    // Jalur ke direktori dokumen.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Tetapkan opsi khusus
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open(RunExamples.GetDataFilePath("vase-v2.ply"), loadPLYOpts);
}
```

### Langkah 7: Memuat File FBX

```csharp
private static void FBXLoadOptions()
{
    // Jalur ke direktori dokumen.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Tetapkan opsi khusus
    scene.Open(dataDir + "test.FBX", opt);

    // Properti keluaran ditentukan dalam GlobalSettings di file FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Kesimpulan

Selamat! Anda telah berhasil menavigasi dunia pemuatan dan penyimpanan model 3D yang rumit menggunakan Aspose.3D untuk .NET. Tutorial ini mencakup berbagai format file dan opsi pemuatan khusus, sehingga memungkinkan Anda memanipulasi aset 3D dengan mudah.

## FAQ

### Q1: Apakah Aspose.3D untuk .NET cocok untuk pemula?

A1: Tentu saja! Aspose.3D untuk .NET menyediakan antarmuka yang ramah pengguna, sehingga dapat diakses oleh pengembang dari semua tingkatan.

### Q2: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?

A2: Ya, Aspose.3D untuk .NET hadir dengan lisensi komersial, memungkinkan Anda menggunakannya dalam proyek Anda.

### Q3: Apakah ada batasan pada format file yang didukung?

 A3: Aspose.3D untuk .NET mendukung berbagai format file 3D populer, termasuk OBJ, STL, FBX, dan banyak lagi. Mengacu kepada[dokumentasi](https://reference.aspose.com/3d/net/) untuk daftar lengkap.

### Q4: Apakah ada versi uji coba yang tersedia?

A4: Ya, Anda dapat menjelajahi kemampuan Aspose.3D untuk .NET dengan mengunduh[uji coba gratis](https://releases.aspose.com/).

### Q5: Di mana saya dapat mencari dukungan untuk Aspose.3D untuk .NET?

A5: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan bantuan masyarakat.