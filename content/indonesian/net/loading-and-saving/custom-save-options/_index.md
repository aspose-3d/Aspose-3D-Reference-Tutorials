---
title: Opsi Penyimpanan Kustom
linktitle: Opsi Penyimpanan Kustom
second_title: Aspose.3D .NET API
description: Jelajahi kekuatan Aspose.3D untuk .NET. Pelajari cara menyesuaikan penyimpanan adegan 3D Anda dengan panduan langkah demi langkah tentang format Collada, USD, 3DS, FBX, OBJ, STL, U3D, glTF, DRC, dan RVM.
type: docs
weight: 21
url: /id/net/loading-and-saving/custom-save-options/
---
## Perkenalan

Selamat datang di dunia Aspose.3D untuk .NET! Jika Anda ingin meningkatkan kemampuan pengembangan 3D, Anda berada di tempat yang tepat. Dalam tutorial ini, kita akan mendalami fungsi Memuat dan Menyimpan, khususnya berfokus pada Opsi Penyimpanan Kustom. Aspose.3D untuk .NET adalah perpustakaan canggih yang memberdayakan pengembang untuk memanipulasi dan menyimpan adegan 3D secara efisien.

## Prasyarat

Sebelum kita mulai menjelajahi fitur-fitur menarik Aspose.3D, pastikan Anda memiliki prasyarat berikut:

- Pemahaman dasar tentang pengembangan C# dan .NET.
-  Aspose.3D untuk perpustakaan .NET diinstal. Anda dapat mengunduhnya dari[halaman rilis](https://releases.aspose.com/3d/net/).
- Lingkungan pengembangan yang diatur dengan Visual Studio atau C# IDE pilihan lainnya.

## Impor Namespace

Untuk memulai, mari impor namespace yang diperlukan:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

Sekarang kita sudah menyiapkan tahapannya, mari kita bagi tutorialnya menjadi beberapa langkah.

## Langkah 1: Opsi Simpan Collada

Mari kita mulai dengan Collada, format file 3D yang populer. Ikuti langkah-langkah berikut untuk menyesuaikan opsi penyimpanan Collada:

### 1. Siapkan Direktori:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Inisialisasi Opsi Penyimpanan Collada:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. Konfigurasikan Opsi:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## Langkah 2: Opsi Penyimpanan 3DS yang Bijaksana

Sekarang, mari jelajahi Discreet 3DS dan opsi penyesuaiannya:

### 1. Siapkan Direktori:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Inisialisasi Opsi Penyimpanan 3DS:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. Konfigurasikan Opsi:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // Opsi konfigurasi tambahan...
   ```

Lanjutkan pendekatan langkah demi langkah ini untuk opsi penyimpanan FBX, OBJ, STL, U3D, glTF, dan DRC, sesuaikan masing-masing sesuai kebutuhan Anda.

## Langkah 3: Opsi Penyimpanan glTF

Sekarang, mari fokus pada glTF, format yang banyak digunakan di aplikasi web dan seluler. Sesuaikan opsi penyimpanan glTF Anda dengan langkah-langkah berikut:

### 1. Inisialisasi Objek Adegan:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. Tetapkan Opsi Penghematan glTF:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. Simpan File glTF:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

Ikuti struktur serupa untuk opsi penyimpanan lainnya seperti DRC dan RVM.

## Kesimpulan

Selamat! Anda telah berhasil menjelajahi opsi penyimpanan khusus di Aspose.3D untuk .NET. Pustaka canggih ini menyediakan segudang opsi untuk menyesuaikan proses penyimpanan adegan 3D Anda.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk .NET dengan kerangka .NET lainnya?

A1: Ya, Aspose.3D kompatibel dengan berbagai kerangka .NET, memastikan fleksibilitas dalam lingkungan pengembangan Anda.

### Q2: Apakah ada opsi lisensi yang tersedia untuk Aspose.3D?

 A2: Ya, Anda dapat menjelajahi opsi lisensi[Di Sini](https://purchase.aspose.com/buy).

### Q3: Di mana saya dapat menemukan dukungan untuk pertanyaan terkait Aspose.3D?

 A3: Anda dapat mencari dukungan di[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Apakah tersedia uji coba gratis?

 A4: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q5: Bagaimana saya bisa mendapatkan lisensi sementara untuk Aspose.3D?

 A5: Dapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).