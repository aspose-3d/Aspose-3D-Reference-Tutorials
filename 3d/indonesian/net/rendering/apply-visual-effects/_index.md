---
title: Menerapkan Efek Visual di Area Pandang 3D
linktitle: Menerapkan Efek Visual di Area Pandang 3D
second_title: Aspose.3D .NET API
description: Jelajahi dunia visualisasi 3D dengan Aspose.3D untuk .NET. Pelajari cara menerapkan efek visual menawan pada adegan Anda menggunakan tutorial langkah demi langkah. Tingkatkan proyek Anda dengan efek pikselasi, skala abu-abu, deteksi tepi, dan buram.
type: docs
weight: 10
url: /id/net/rendering/apply-visual-effects/
---
## Perkenalan

Meningkatkan daya tarik visual adegan 3D merupakan aspek penting dalam menciptakan pengalaman yang imersif. Aspose.3D untuk .NET menyediakan seperangkat alat canggih untuk menerapkan efek visual ke area pandang 3D. Dalam tutorial ini, kita akan memandu proses penerapan berbagai efek pada pemandangan 3D, termasuk pikselasi, skala abu-abu, deteksi tepi, dan buram.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki hal berikut:

- Pengetahuan tentang pengembangan C# dan .NET.
-  Aspose.3D untuk perpustakaan .NET diinstal. Anda dapat mengunduhnya dari[Di Sini](https://releases.aspose.com/3d/net/).
- File adegan 3D (misalnya, "scene.obj") untuk eksperimen.

## Impor Namespace

Untuk memulai, impor namespace yang diperlukan untuk Aspose.3D dan dependensi lainnya. Tambahkan baris berikut ke kode Anda:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Muat Adegan 3D yang Ada

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Muat adegan 3D Anda menggunakan`Scene` kelas.

## Langkah 2: Buat Kamera

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Buat contoh kamera dan atur posisi dan targetnya.

## Langkah 3: Tambahkan Cahaya ke Pemandangan

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Perkenalkan pencahayaan untuk meningkatkan efek visual.

## Langkah 4: Buat Renderer dan Target Render

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Konfigurasikan pengaturan penyaji
    renderer.EnableShadows = false;

    // Buat target render
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Konfigurasikan area pandang
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Render pemandangan menjadi tekstur
        renderer.Render(rt);

        // Simpan tekstur yang dirender ke file
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Lanjutkan dengan efek pasca-pemrosesan...
    }
}
```

Buat penyaji dan target render untuk menangkap pemandangan.

## Langkah 5: Terapkan Efek Pasca Pemrosesan

### Langkah 5.1 Efek Pikselasi

```csharp
// Buat efek pikselasi
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Terapkan efek pikselasi dan simpan hasilnya.

### Langkah 5.2 Efek Grayscale

```csharp
// Buat efek skala abu-abu
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Terapkan efek skala abu-abu dan simpan hasilnya.

### Langkah 5.3 Gabungkan Efek

```csharp
// Gabungkan efek skala abu-abu dan pikselasi
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Gabungkan beberapa efek untuk hasil yang unik.

### Langkah 5.4 Efek Deteksi Tepi

```csharp
// Buat efek deteksi tepi
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Terapkan efek deteksi tepi dan simpan hasilnya.

### Langkah 5.5 Efek Buram

```csharp
// Buat efek buram
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Terapkan efek blur dan simpan hasilnya.

## Kesimpulan

Bereksperimen dengan efek visual di area pandang 3D menambah kedalaman dan kreativitas pada pemandangan Anda. Aspose.3D untuk .NET menyederhanakan proses ini, menawarkan serangkaian efek pasca-pemrosesan untuk meningkatkan proyek Anda.

## FAQ

### Q1: Dapatkah saya menerapkan beberapa efek secara bersamaan?

A1: Ya, Anda dapat menggabungkan efek pasca-pemrosesan yang berbeda untuk hasil yang unik dan kompleks.

### Q2: Bagaimana cara menyesuaikan intensitas efek visual?

A2: Setiap efek mungkin memiliki parameter yang dapat Anda sesuaikan untuk mengontrol intensitasnya. Lihat dokumentasi untuk detail spesifik.

### Q3: Apakah Aspose.3D cocok untuk pengembangan game?

A3: Meskipun Aspose.3D terutama dirancang untuk pemodelan dan rendering 3D, Aspose.3D dapat digunakan dalam aspek pengembangan game tertentu.

### Q4: Apakah ada efek pasca-pemrosesan tambahan yang tersedia?

A4: Aspose.3D menyediakan berbagai efek pasca-pemrosesan bawaan, dan Anda dapat membuat efek khusus menggunakan perpustakaan.

### Q5: Dapatkah saya menggunakan Aspose.3D untuk proyek komersial?

 A5: Ya, Anda dapat menggunakan Aspose.3D untuk tujuan komersial. Mengacu kepada[halaman pembelian](https://purchase.aspose.com/buy) untuk rincian perizinan.